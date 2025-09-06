import subprocess
import time
import os
import signal
import requests
from args_30B import experiments  # Import experiment configurations from parameter file

# Configuration section
SERVER_LOG_FILE_TEMPLATE = "server_benchmark_{}.log"  # Each experiment uses an independent log file
HEALTH_CHECK_URL = "http://localhost:8001/health"
MAX_RETRY = 1200  # Maximum 1200 attempts (1 second each, total maximum waiting time 20 minutes)
RETRY_INTERVAL = 1  # Check every 1 second

# Server base command
base_server_cmd = [
    "ncu", "--set", "full",
    "--nvtx",
    "-o", "/mnt/ssd/mayiling.myl/run_vllm/ncu_file",
    "--target-processes", "all",
    "-f",
    "python3", "-m", "vllm.entrypoints.openai.api_server",
    # "--model", "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
    "--trust-remote-code",
    # "--enable-prefix-caching",
    "--disable-log-requests"
]

# Client base command
base_client_cmd = [
    "python", "/mnt/ssd/mayiling.myl/vllm/benchmarks/benchmark_serving.py",
    # "--model", "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
    # "--dataset-name", "random",
    # "--random-input-len", "1000",
    # "--random-range-ratio", "0",
    # "--num-prompts", "80",
    "--trust-remote-code",
    "--ignore-eos",
    "--metric-percentiles", "90,99"
]

def build_command(base_cmd, args_dict):
    """Build the final command list based on base_cmd and argument dictionary"""
    cmd = base_cmd.copy()
    for key, value in args_dict.items():
        cmd.append(key)
        if value is not None:
            cmd.append(value)
    return cmd

def start_server(server_cmd, log_file_path):
    """Start server and write output to log file"""
    print("Starting vLLM server...")
    log_file = open(log_file_path, "w")
    server_process = subprocess.Popen(server_cmd, stdout=log_file, stderr=subprocess.STDOUT)
    return server_process, log_file

def wait_for_server():
    """Poll /health endpoint until server is ready"""
    print("Waiting for server to start...")
    retry = 0
    while retry < MAX_RETRY:
        try:
            response = requests.get(HEALTH_CHECK_URL, timeout=5)
            if response.status_code == 200:
                print("Server started and ready!")
                return True
        except requests.exceptions.RequestException:
            pass  # Ignore errors and continue retrying

        time.sleep(RETRY_INTERVAL)
        retry += 1

    print("Timeout: Server failed to start within the specified time.")
    return False

def run_benchmark(client_cmd):
    """Run benchmark client"""
    print("Starting benchmark test...")
    subprocess.run(client_cmd)

def stop_server(process, log_file):
    """Stop server and close log file"""
    print("\nStopping vLLM server...")
    process.send_signal(signal.SIGINT)
    process.wait()
    log_file.close()

if __name__ == "__main__":
    for idx, exp in enumerate(experiments):
        print(f"\nRunning experiment group {idx + 1}...")

        log_file_path = SERVER_LOG_FILE_TEMPLATE.format(idx + 1)
        print(f"Current log file: {log_file_path}")

        # Build server and client commands for current experiment
        server_cmd = build_command(base_server_cmd, exp["server_args"])
        client_cmd = build_command(base_client_cmd, exp["client_args"])

        print("Server command:", " ".join(server_cmd))
        print("Client command:", " ".join(client_cmd))

        # Start server
        server_process, log_file = start_server(server_cmd, log_file_path)

        # Wait for server to start completely
        if not wait_for_server():
            print("Server startup failed, skipping current experiment.")
            stop_server(server_process, log_file)
            continue

        try:
            run_benchmark(client_cmd)
        finally:
            stop_server(server_process, log_file)

    print("\nAll experiments completed.")

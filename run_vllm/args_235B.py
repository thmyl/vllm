experiments = [
    # enable
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-235B-A22B",
            "--tensor-parallel-size": "8",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-235B-A22B",
            "--dataset-name": "random",
            "--random-input-len": "150",
            "--random-output-len": "3800",
            "--random-range-ratio": "0",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        }
    },
]
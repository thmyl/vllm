experiments = [
    # 1
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "200",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 2
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "3000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 2.1
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "1000",
            "--random-output-len": "200",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 3
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "1000",
            "--random-output-len": "3000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 4
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "3000",
            "--random-output-len": "3000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 5
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 6
    {
        "server_args": {
            "--max-num-batched-tokens": "8192",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 7
    {
        "server_args": {
            "--max-num-batched-tokens": "4096",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 8
    {
        "server_args": {
            "--max-num-batched-tokens": "2048",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 9
    {
        "server_args": {
            "--max-num-batched-tokens": "1024",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 10
    {
        "server_args": {
            "--max-num-batched-tokens": "512",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "185",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 11
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "128",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 12
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "64",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 13
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "32",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 14
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "16",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
    # 15
    {
        "server_args": {
            "--max-num-batched-tokens": "16384",
            "--max-model-len": "16384",
            "--long-prefill-token-threshold": "0",
            "--enable-prefix-caching": None,
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--tensor-parallel-size": "1",
            "--gpu-memory-utilization": "0.9",
            "--port": "8001",
        },
        "client_args": {
            "--model": "/nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B",
            "--dataset-name": "random",
            "--random-input-len": "200",
            "--random-output-len": "1000",
            "--random-range-ratio": "0.3",
            "--max-concurrency": "8",
            "--num-prompts": "80",
            "--append-result": None,
            "--result-filename": "/mnt/ssd/mayiling.myl/output/benchmark_results.json",
            "--port": "8001"
        },
    },
]
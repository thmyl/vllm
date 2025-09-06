total_runs=$1

for ((i=1;i<=total_runs;i++)); do
    echo "The $i-th running cycle"
    python run_vllm.py
done
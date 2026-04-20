from huggingface_hub import snapshot_download

local_path = snapshot_download(
    repo_id="Qwen/Qwen3.5-0.8B",
    cache_dir=r"D:\hf\hub"
)
print(local_path)
vllm serve --model "Qwen/Qwen3-ASR-0.6B" \
--hf-overrides '{"architectures": ["Qwen3ASRRealtimeGeneration"]}' \
--api-key secret
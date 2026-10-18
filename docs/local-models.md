# Local models

The whole pipeline works offline with a local model. Start here:

- **canirun.ai**: checks your hardware and recommends a model that actually runs.
- **localllm-advisor.com** and **localllm.run**: model fit and runtime comparisons.

## What you need

| Job | Minimum feel | Notes |
|---|---|---|
| Chunk writing | 8B instruction-tuned, decent prose | The quality gate catches weak output; rerun it |
| Quality gate | any | The gate is deterministic checks, not a model |
| qa-tutor | 8B+, better at 14B+ | Answering from provided chunks is easier than open reasoning |
| Dense textbooks | 14B+ or a frontier model online | Long, technical sources reward stronger models |

Sensible local defaults: Qwen3 8B or 14B Instruct, Llama 3.3 8B/70B if you have the memory. All run under Ollama, LM Studio or llama.cpp.

## Repetitive scheduled work is the sweet spot

Lesson delivery is the classic local-model job: the same short prompt, one chunk at a time, weeks on end. A local model keeps the monthly cost at zero and the data on the machine. Reserve frontier models for the initial chunk writing on hard sources.

## Hybrid default

`chunk-write` and `qa-tutor` may use a frontier model; `deliver-chunk` (the scheduled messages) is the natural place to run local. Config note in `config.yaml` shows the Ollama switch.

---
name: embedder_finetune_pilot9_lost_to_base_bge_small_2026_11_12
description: "[VERIFIED] Should we fine-tune the dense embedder on read-memory pairs? Pilot 9 on mini 1: no, B lost to base bge-small (hit@5 1 vs 4 of 78, sign p 0.25)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T15:51:18+02:00
  status: provisional
  evidence: ""
---

Pilot 9 (Mac mini 1, 12 Nov 2026, an agent): bge-small-en-v1.5 fine-tuned on 1,255 read-memory pairs (2 epochs, lr 2e-5, batch 16, maxlen 256, hard_k 20, CPU training) did worse than the base model on 78 held-out prompts: hit@5 1/78 vs 4/78, hit@20 4/78 vs 6/78, MRR@100 0.0197 vs 0.0304; discordant at hit@5 A-only 3, B-only 0, two-sided sign p 0.25. Training loss fell 2.89 -> 2.35 while held-out recall fell: fitting labels, not the task. By the pilot's PLAN.md this is a loss and B ships nowhere. Limits: the dense lane alone is weak (4/78 base), and the gold is what sessions read, which the existing lanes chose. Only a much larger pair set (reads mined from transcripts) justifies another try. Files and README: 12_cognitive_architecture/brain_improvement/embedder_finetune_mini1_2026_11_12/pilot9/. Path to the result: MPS OOM in pilots 4-8, so training moved to the CPU (patch_emb_cputrain); a cores:2 job starved behind one-core fillq jobs ([[fillq_multicore_job_starves_behind_one_core_queue_2026_11_12]]). status: verified

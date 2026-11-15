---
name: t403_compression_barely_moves_test_error_2026_11_01
description: [PROVISIONAL] T403: after train err 0, noisy tanh layer's late compression moves test err <=0.011 while I(X;T) moves 0.13-0.35 nats; test loss rises always
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T08:53:14+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed e635884, move 5e687b5b. Follows [[t403_ixt_is_a_function_of_norm_alone_2026_11_01]].

One tanh layer, width 8, 64 inputs, sigma 0.3, lr 0.05, 40k steps, 5,000 fixed test inputs (se about 0.004).

- Linear, seed 1: I(X;T) falls 3.13 -> 2.78 and test err goes 0.080 -> 0.069.
- Linear, seed 2: I(X;T) rises 3.62 -> 3.75 and test err goes 0.069 -> 0.072.
- Test loss rises on both seeds.
- Xor memorizes: test err 0.50 and I(X;T) stays near log 64.
- Two seeds cannot settle the sign of the compression-generalization link.

**Why:** this closes the last T403 open item at toy scale.

**How to apply:** do not read late compression as generalization. Measure test error directly, and use many seeds before claiming a sign.

Folder: research-repo research_pushes/2026-11-01-loop-T403-test

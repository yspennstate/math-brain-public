---
name: t403_64_seeds_compression_no_test_gain_2026_11_01
description: [VERIFIED] T403 sign: 64 seeds, late compression moves test err -0.0005 +- 0.0007, rho(dI, d test) +0.18 n.s.; null
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T10:27:25+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Result in research_pushes/2026-11-01-loop-T403-seeds (push queued behind the GitHub quota at 06:27 UTC). Follows [[t403_compression_barely_moves_test_error_2026_11_01]].

- 58 of 64 seeds compress after the training error reaches 0.
- Test error changes by -0.0005 on average (sd 0.0056, se 0.0007), and by under 0.02 on every seed.
- Spearman rho(dI, d test err) is +0.18; the 5 percent threshold at n = 64 is about 0.25, so it is not significant.
- d log|W| correlates with dI at +0.52: the seeds whose norm grows most are the expanders.
- The weak benefit that seed 1 suggested on two seeds did not survive.

**Why:** this closes the sign item of T403 as a null at this resolution.

**How to apply:** a two-seed direction is not a sign. Rerun at 64 seeds before reading one, which takes about 6 minutes for this model.

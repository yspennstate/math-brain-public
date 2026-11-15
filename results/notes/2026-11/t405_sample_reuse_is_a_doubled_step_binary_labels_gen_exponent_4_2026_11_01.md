---
name: t405_sample_reuse_is_a_doubled_step_binary_labels_gen_exponent_4_2026_11_01
description: [VERIFIED] T405 sample reuse: two steps per sample at eta = plain SGD at 2 eta (paired median 1.00-1.10, 9 cells, d 16-32); binary y makes generative exponent = information exponent 4, so reuse stays d^3; smoothing is the route to d^2
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T16:42:58+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed 0c93bd9 (research_pushes/2026-11-01-loop-T405-reuse), card claim_85ebd9c9e4994f7fb715ebe562a40cf9 export ad0829c, frontier move c49ad142.
Lesson for the next pre-registered comparison: medians over escaped rows only compare different subsets when escape counts differ; use the censored median (non-escaped = inf). That artifact made the reuse exponent look like 1.94 against 2.96.
With 16 rows, escape-time quartiles span 4 to 20 d^3, so best-cell medians move by about 2x between seeds; paired common-seed ratios are the test that works.

Related: [[t403_late_gain_at_n256_comes_with_rising_ixt_2026_11_01]] is the same loop's other SGD row.

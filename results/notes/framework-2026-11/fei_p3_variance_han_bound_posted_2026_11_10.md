---
name: fei_p3_variance_han_bound_posted_2026_11_10
description: "[VERIFIED] FEI P3 'A variance form of Han's bound' posted? Yes, github.com/yspennstate/fei-variance-han-bound b726c21 (10 Nov 23:1x): H <= (2+3/ln2) I + sum Inf_k log2(1+Var/Inf_k)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T23:08:20+02:00
  status: provisional
  evidence: ""
---

Paper 3 of the FEI papers loop (an agent, owner order 10 Nov 17:18). Theorem: H(f) <= c0 I(f) + sum_k Inf_k log2(1 + Var(f)/Inf_k), c0 = 2 + 3/ln2; adaptive form along any decision tree; corollaries (all Inf_k >= eps Var gives c0 + log2(1+1/eps); H <= (c0+1+H(pi)) I). AND_k: < 7.92 I against Han's (k+1+3/ln2) I. No gain for majority or tribes (variance bounded below, the loss is the log itself) - not a route to FEI without a one-coordinate step D_i <= C Inf_i. Checks: random f n=2..10 max H/RHS 0.486; separate D,E,J transforms on 4767 steps (J/(2/ln2 Inf) up to 0.869, so the JSD lemma is near tight); 928 adaptive trees max 0.484; monotone census n=6 max 0.4735, n=7 max 0.4812 at AND_7 (an agent's census, leaders recomputed independently). Referee scars: a remark said Han follows 'without Jensen' (it needs concavity of t log2(1+1/t)); Dedekind counts include the two constants; KKLMS is min-entropy, not H. Sources: 06_math_research/fei_papers_agent/p3 and repo_p3; state LOOP_STATE.md item 28. Related: [[fei_p2_good_coordinates_posted_2026_11_10]].

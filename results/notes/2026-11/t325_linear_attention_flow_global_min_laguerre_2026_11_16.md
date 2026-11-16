---
name: t325_linear_attention_flow_global_min_laguerre_2026_11_16
description: "T325 posted: untied scalar linear-attention layers trained by gradient flow reach a global minimizer from almost every start; step sizes are reciprocal zeros of a Laguerre polynomial; non-minimizing critical points are strict saddles"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:14:44+02:00
  status: verified
  evidence: "fillq_ctl/t325_public/paper/main.tex"
---

T325, posted (paper "Gradient flow for factored scalar linear attention"; source fillq_ctl/t325_public/paper/main.tex).

Result: in-context learning of scalar linear regression by L untied linear-attention layers, each with a key scalar k_i and a query scalar q_i. For every depth L and prompt length n, population gradient flow on the 2L factors is bounded and converges to a critical point; every critical point that is not a global minimizer has a negative Hessian eigenvalue (strict saddle); from all initializations outside a Lebesgue null set (so almost surely under Gaussian initialization) the flow reaches a global minimizer. The trained network performs L gradient descent steps on the prompt's least-squares loss with step sizes k_i q_i equal to the reciprocals of the zeros of the rescaled Laguerre polynomial L_L^(n/2); the risk is 2^L L! / prod_{j=1..L} (n+2j). Initializations with k_i = -q_i in some layer converge to a non-minimizing critical point, so the null set is not empty.

Context: the untied, scalar-data counterpart of Gatmiry-Saunshi-Reddi-Jegelka-Kumar (looped layers, gradient dominance). No gradient dominance holds here: the origin is a critical point and the risk is invariant under (k_i, q_i) -> (lambda k_i, q_i / lambda); the proof goes through the coefficients of a polynomial in the step sizes.

Plain words: training a stack of simple attention layers to do regression from the prompt always ends at the best answer, except from a measure-zero set of starts.

Earlier note on the same problem: [[t325_l6_step_minima_are_strict_not_stalls_2026_11_01]]. Why this memory exists: a 16 Nov recall probe from the posted abstracts found T325 0 of 3 because only that side note existed (fillq_ctl/recall_probe_1115_RESULTS.md).


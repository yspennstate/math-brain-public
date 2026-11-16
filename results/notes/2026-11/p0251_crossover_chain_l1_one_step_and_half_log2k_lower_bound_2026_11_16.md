---
name: p0251_crossover_chain_l1_one_step_and_half_log2k_lower_bound_2026_11_16
description: "[PROVISIONAL] P0251 crossover chain, single column: original chain is uniform after ONE step (relabel by pi); labeled variant and every L>=2 need (1/2)log2 K - O(1) steps (mean contraction lambda=(K-2)/(2(K-1)), Wilson/Chebyshev)"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:39:06+02:00
  status: provisional
  evidence: ""
---

status: two audits (16 Nov 00:4x simulation K=1024; 00:5x explicit constant |Cov| <= 3/(K-3) for matching partner indicators, so t_mix(1/4) >= (1/2)log2 K - 5 for K >= 8). Still not refereed by anyone but me. Paper: yspennstate/crossover-chain-mixing (Zenodo 10.5281/zenodo.24257131), Aldous-Fill Open Problem 12.5.

In the original chain the new words get the labels of the pair positions under a uniform pi, so one column goes to x o pi o tau with pi o tau uniform: at L=1 the law is u_s after one step. The paper's remark that a log K lower bound at L=1 'would have to come from columns with many ones' holds only for the labeled variant.

Lower bound: start with ones on half the positions A; Z = ones in A minus K/4 has E[Z'|omega] = lambda Z with lambda = (K-2)/(2(K-1)), and Var stays O(K) (pairs independent given the matching, partner indicators of a uniform matching have covariance O(1/K)). Chebyshev against the centred hypergeometric gives TV >= 1 - C 4^-m at t = (1/2)log2 K - m (K >= 8). For the original chain with L >= 2 use two identical columns and their overlap count W, which relabeling leaves invariant; E[W'|x] - s1s2/K contracts by the same lambda. So tau = Theta(log K + log L) for 2 <= L <= K in both versions; the paper's log2 min(K,L) - 3 is O(1) for fixed L.

Sim K=1024: mean Z 128.2, 64.2, 31.9, 16.4, 8.2 vs predicted 127.9..8.0; TV >= 0.95, 0.68, 0.39 at t=3,4,5. Record: 12_cognitive_architecture/brain_improvement/agent_run/referee_P0251_crossover_chain_2026_11_16.md (addendum points 5-6) with p0251_l1_check.py, p0251_l2_check.py. Would change it: an explicit covariance constant failing, or the paper defining the state differently from main.tex par. 1.

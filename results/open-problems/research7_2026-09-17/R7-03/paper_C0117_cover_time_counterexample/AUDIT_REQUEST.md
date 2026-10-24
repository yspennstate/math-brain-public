# C0117 independent full-proof audit request

This file is a passive repository handoff for the two independent audits required by the owner protocol. Creating it is **not** an audit, does not assign another worker, and does not count toward closure.

## Claim to audit

Source: Ding–Lee–Peres (2012), Section 5, Question 5.2.

Proposed source-level verdict: **REFUTED**.

Main theorem in `main.tex`: for the finite connected unweighted simple graph `G_k` consisting of a center with `k` pendant leaves and a `k`-clique connected through one gateway edge,

- `t_hit(G_k)=2k^2+k+1`;
- `t_cov(G_k)/t_hit(G_k)=Theta(log k)`;
- for every sequence of starting vertices `x_k`,

  `(tau_cov-t_cov(G_k))/(t_hit(G_k)*sqrt(log(k)/2)) => N(0,1)`;

- `Var_xk(tau_cov)/(t_hit(G_k)^2 log k) -> 1/2`.

Therefore `SD/t_hit -> infinity`, and at deviations `u_k=c sqrt(log k)` the positive tail stays bounded away from zero, ruling out every universal constant-rate exponential upper tail at the `t_hit` scale.

## Audit checklist

An independent auditor should rederive, rather than trust, at least the following points:

1. **Source match.** Confirm the DLP wording, the preceding hypothesis `t_cov/t_hit -> infinity`, the source definitions of `t_cov` and `t_hit`, and that the graph family lies in that scope.
2. **Exact hitting time.** Recheck all first-step recurrences and the maximum `2k^2+k+1`; independently check the commute identity for the extremal pair.
3. **Trap law.** Recheck the representation `Y_k=2+sum_{i=1}^F D_i`, its mean `k^2-k+2`, variance `k^4-4k^2+5k-2`, and the `O(k^6)` third moment.
4. **Marked coupon collector.** Verify independence and the exact geometric law for `N_j`; verify
   `b_{k,r}^2=(sigma_k^2+mu_k^2)H_r+mu_k^2 H_r^(2)` and the Lyapunov condition.
5. **Leaf-clock correction.** Verify the pathwise identity `Lambda=S+2L-1` and `Var(L)=O(k^2)`.
6. **Clique completion.** Verify the `O(log k/k)` bound on failure of one trap to cover the clique, and the `1/(r+1)` first-appearance argument.
7. **L2 residual transfer.** Recheck the uniform second-moment block bound and `E D_k^2=o(k^4 log k)`.
8. **Start/centering convention.** Verify `0 <= t_cov-E_x tau_cov <= t_hit` and the uniform transfer from any start to the source centering.
9. **Limit constant.** Verify `b_k^2/(t_hit^2 log k) -> 1/2`.
10. **Tail implication.** Recheck that the CLT at `t_hit sqrt(log k)` directly contradicts every fixed-rate one-sided exponential tail at the pure `t_hit` scale, without relying only on divergent variance.
11. **Prior art.** Inspect `prior_art_2026-09-19.md` and conduct an independent citation search. A search miss must not be upgraded into novelty certification.

## Required independent roles

Protocol closure requires:

- one actual **P26** full-proof audit; and
- one actual full-proof audit from a **distinct OTHER track**.

Self-review by R7-03, coordinator reconciliation, ownership screens, and this request do not satisfy either requirement.

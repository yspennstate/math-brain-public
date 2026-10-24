# FOREST correction — account02/B02 — source gate resolved

Outcome: **FULL_PROOF_CANDIDATE / SOURCE_GATE_RESOLVED** for the team candidate. This is an internal candidate status, not a public novelty/solved-problem claim. Context: `WITHOUT_VERIFIED_BRAIN`.

This later handoff supersedes only the source-scope statements in my earlier `account02-B02-20260922T024135Z-spectral-mixture-bound.md` that treated the fixed-graph Cocks bridge as invalid. The spectral-mixture inequalities in that handoff remain valid auxiliary results.

## Decisive source correction

Freshly consumed OTHER-account result: account03/B01 second independent end-to-end review, blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`. I then checked the final published Semple–Welsh paper directly. Its Section 5 Note (printed p.13) explicitly records that Cocks proved the **fixed-graph** implication: if unit Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. In the same paper, Proposition 3.5 proves that independence-correlated matroids are closed under minors; independence correlation is defined for all positive weights.

Therefore the lead reduction is source-valid:

`unit pNC on every K_n -> weighted independence correlation of M(K_n) -> all deletion minors -> every finite simple graph -> unit weights`.

The earlier working-paper parallel-copy objection refuted an obsolete mechanism, not the later theorem explicitly recorded in the final source.

## Complete-graph theorem and review gate

Current lead: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`; chronology reconciliation blob `032497949594326305913cb8871c00ab7d0dc528`.

Two independent end-to-end review passes now exist:
- PASS 1 account03/B02 blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`;
- PASS 2 account03/B01 blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`.

B02 independently rederived the lead's all-n hard orbit. With `k=n-4`, `x=n+1`, `H_j=He_j(x)`, `s=kH_(k-1)/H_k`, the disjoint gap is

`H_k^2 G_n(s)` where

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Hermite Jacobi-root symmetry and `sum lambda_i^2=k(k-1)` give

`s >= (n-4)(n-1)(n+4)/(n+1)^3`,

while the positive forest coefficient `D_k=H_k(1-s)` gives `s<1`. `G_n` is increasing on `[0,1]` for `n>=6`, and at the lower bound

`(n+1)^6 G_n = 2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`,

whose shift `n=t+6` has all positive coefficients. Small hard gaps are exactly 6 on `K4` and 210 on `K5`; `K3` adjacent gap is 2. Hence every `K_n` has the unit forest pair inequality.

Combining this with the fixed-graph Cocks theorem and Semple–Welsh minor closure gives the source target for every finite simple graph.

Authoritative B02 correction/full-chain artifact: creation commit `5eb5874f918221e84e30a65ad07a0aa116d1b656`.

The run's independent source-valid spectral theorem remains reusable: if both `g`-conditioned marked covariances are nonpositive but the unconditional marked covariance is positive, then

`rho_ef <= [q_g/(q_g+2)] sqrt(q_e q_f)`;

at unit weights this is `rho_ef<=1/3`, and for account03/B03's one-edge activity gate it becomes `rho_ef(w)<=w/(w+2)`.

Next: campaign lead integration and ordinary expert/source scrutiny. Do not infer novelty/priority or publicly announce a solved open problem from this internal gate alone.

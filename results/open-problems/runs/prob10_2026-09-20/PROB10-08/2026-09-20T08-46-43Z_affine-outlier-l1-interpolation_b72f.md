Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested but is not authenticated. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains `OPEN/PARTIAL`, `W_exp=1/2 provisional -> 1/2 provisional`. **MECHANISM MOVEMENT:** the actual Haiman affine slow eigenvector, not merely the canonical coset contrast, now has a proved L1 rarity exponent; three approaches compared: two-norm outlier resolvent (retained), heat-superlevel parabolic thickening (rejected), multiplicity-only elimination (rejected).

# PROB10-08 — actual affine slow-mode L1 interpolation

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL / new auxiliary theorem proved / no new complete source-level cutoff class this run / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Required continuity, ownership and consumed state

This run followed the PROB10 contract and did not reset the target or its failures. I read/recovered:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`; the already-written Abelian Cayley/product-condition target remains excluded and is not this problem;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved pre-refocus R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`; it preserves active H0002 and its all-prefix isotonic/KKT obstruction rather than silently erasing that successor;
- historical stuck recovery `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, preserving the failed product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature, ordinary-curvature, local-limit/AEP and global subcommutation routes;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T07-58-54Z_trace-nuclear-superlevel-affine-info_84f2.md`, blob `d88dd1e2dff02b25eaa3cddbc82826679d25cb68`;
- newest neighboring P26 cutoff-transfer report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`, blob `fd122a821741be5930402d33bed302d43a6f9544`; P26 owns the Green/spherical/biregular-halving route and already has a distinct non-LRE source-valid restricted class;
- newest neighboring NM13 cutoff report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`, blob `1c033f20afeaee2d9e1e5b1028afc45e3bd9a01c`; NM13 owns arc-cover/Hodge/reversal/orbit routes.

Accordingly I did not duplicate P26's halved-bigraph Green transfer, NM13's arc construction, or any of the old R16 product/Poincare/tensor routes.

## 1. Primary-source refresh and exact place where Altschuler uses LRE

Frozen source: Justin Salez, arXiv:2508.21055v1, Problem 2.3: all bounded-degree vertex-transitive spectral-expander sequences exhibit total-variation cutoff for the source's rate-one continuous-time SRW

\[
H_t=e^{t(P-I)}.
\]

Primary new lead: Dylan J. Altschuler, arXiv:2609.14945. I rechecked the complete current proof and the arXiv record. The bounded current check still shows only **v1, submitted 14 September 2026**; no v2, correction or erratum surfaced.

The exact proof boundary remains:

1. LRE transfers maximal-rate vertex growth to the oriented-edge NBRW state space (Lemma 3.2);
2. that growth is converted by the forest/restart argument to near-maximal NBRW Shannon entropy (Lemma 3.3);
3. Proposition 3.1 obtains endpoint entropy `log n - O(log log n)`;
4. only after this point does ordinary spectral expansion perform the short entropy-to-TV cleanup.

Thus ordinary transitive spectral expansion still lacks the entropy/Green replacement for Steps 1--3. Altschuler's theorem itself is a baseline, not fleet progress.

I also refreshed Haiman--Schildkraut--Zhang--Zhao, arXiv:2109.13131 / Bull. LMS 54 (2022), because the present recovery attacks their 18-regular affine Cayley family. Their paper proves the large second-eigenvalue multiplicity; it does not prove cutoff or the L1 estimate below.

## 2. Why a different recovery was mandatory

Several consecutive PROB10-08 runs have not changed the frozen source metric. The predecessor had already pushed the generic invariant-superlevel argument to

\[
M_u\le \frac{m_u}{n}+e^{-\gamma t}\sqrt{m_u}
\]

for every heat-kernel superlevel relation and showed that formal Schatten interpolation does not remove the remaining constant exponent. Repeating that method would violate the stuck rule.

The 06:57 affine report left a sharper concrete gap: for the canonical `Pi_q`-fixed contrast the slow representation's matrix coefficient is exactly L2-heavy but L1-rare, yet the **true perturbed second-eigenvector** had only a fixed L2 perturbation bound. Thus it was unknown whether the high multiplicity really represented TV mass or mostly rare L2 spikes.

This run changes category from heat-kernel superlevel sets to **eigenvector coefficient geometry** and resolves part of that exact gap.

## 3. Main new theorem — L1 rarity for the actual affine slow eigenvector

Let

\[
\Gamma_q=\operatorname{SL}(2,q)\ltimes\mathbb F_q^2,
\qquad r=q^2,
\]

with Haiman et al.'s 16 lifted LPS subgroup generators and two translations. On the mean-zero induced permutation representation `phi_q` of dimension `r-1`, write

\[
C=A_0+B,
\]

where `A_0` is the 16-generator subgroup operator and `B` is the two-translation perturbation. For the normalized point contrast `u_0`,

\[
A_0u_0=16u_0,
\qquad
\|u_0\|_{1,\pi}=O(r^{-1/2}).
\]

On

\[
W=\{1,u_0\}^{\perp},
\]

the lifted LPS estimate and `||B||<=2` give

\[
\|P_WCP_W\|_{2\to2}
\le\beta:=2+4\sqrt7=12.583005\ldots<16.
\]

The exact perturbation source

\[
s=P_WBu_0
\]

satisfies

\[
\|s\|_2\le\sqrt2,
\qquad
\|s\|_{1,\pi}=O(r^{-1/2}),
\qquad
\|s\|_\infty\|u_0\|_{1,\pi}=2+o(1).
\]

This yields the nontrivial compressed L1 bound

\[
\|P_WCP_W f\|_{1,\pi}
\le(20+o(1))\|f\|_{1,\pi}
\qquad(f\in W).
\]

Let `u` be the **actual** unit top eigenvector of `C` on `phi_q`, with eigenvalue `mu_q`, and write

\[
u=\alpha u_0+w,\qquad w\in W.
\]

Rayleigh testing gives `mu_q>=16-2/(r-1)>beta` for large `q`, and projection gives the exact resolvent equation

\[
(\mu_qI-C_W)w=\alpha s.
\]

Split its Neumann series at

\[
K\sim\frac{\log r}{2\log(20/\beta)}.
\]

Use the `20^k` L1 estimate before `K` and the `beta^k` L2 estimate after `K`. The matching artifact proves that for every

\[
\eta<\eta_*:=
\frac{\log(16/\beta)}{2\log(20/\beta)}
=0.2592245387\ldots,
\]

one has

\[
\boxed{
\|u\|_{1,\pi}=O_\eta(r^{-\eta}).
}
\tag{3.1}
\]

This is new relative to the R16 chain: the predecessor only controlled the true perturbation in L2 and therefore could not transfer the canonical contrast's rare-spike behavior to the true slow eigenmode.

## 4. Actual matrix coefficient, not the canonical surrogate

For any transitive action on `r` points and any vector `v`, averaging the elementary inequality

\[
|\langle v,\rho(g)v\rangle|
\le\frac1r\sum_x|v(x)|\,|v(g^{-1}x)|
\]

gives

\[
\mathbb E_g|\langle v,\rho(g)v\rangle|
\le\|v\|_{1,\pi}^2.
\]

Thus (3.1) yields, for the true slow eigenvector,

\[
\boxed{
\mathbb E_g|\langle u,\phi_q(g)u\rangle|
=O_\eta(r^{-2\eta})
\quad\forall\eta<\eta_*.
}
\tag{4.1}
\]

Hence every exponent below

\[
\boxed{2\eta_*=0.5184490776\ldots}
\]

is certified. Generic Schur orthogonality alone only supplies the `r^{-1/2}` scale. So the actual perturbed mode is rigorously more L1-rare than the generic high-multiplicity heuristic predicts.

Using the predecessor's exact multiplicity audit, the genuine slow block in the continuous-time likelihood ratio is

\[
(r-1)e^{-\delta_qt}\langle u,\phi_q(g)u\rangle,
\qquad
\delta_q=1-\mu_q/18.
\]

Therefore

\[
\operatorname{TV}_{\rm slow}(t)
\le O_\eta\bigl(r^{1-2\eta}e^{-\delta_qt}\bigr).
\tag{4.2}
\]

The same block decomposition gives

\[
\mu_q\le16.5093762187\ldots,
\qquad
\delta_q\ge0.0828124323\ldots,
\]

so the high-multiplicity outlier is rigorously TV-negligible by

\[
\boxed{
(5.8149593\ldots+o(1))\log r.
}
\tag{4.3}
\]

The separated bulk is already negligible by the crude L2-to-TV estimate at `(4.153595+o(1)) log r`. Thus the true outlier coefficient, not the bulk spectrum, is now the limiting piece of this particular affine spectral upper-bound route.

Equation (4.3) is **not** asserted to be the mixing time or a cutoff location. There is no matching lower profile, and no new source-level graph class is promoted this run.

## 5. The two other nonexhausted attacks and why they failed

### Approach B — parabolic thickening of the high-likelihood relation: rejected

If `H_t(x,y)>=theta`, force `k` prescribed additional jumps along a path during an interval of length `s`. This gives endpoint mass at least on the scale

\[
e^{-s}\frac{s^k}{k!d^k}\theta.
\]

Optimizing at `s=k` leaves a Stirling-scale loss of approximately `(ed)^{-k}` per path layer. Ordinary spectral/vertex expansion cannot compensate this loss at the ambient tree branching rate required by Altschuler's entropy proof. So one-step or finite-block heat propagation does not bootstrap ordinary expansion into LRE. This route was stopped rather than dressed up as a new sufficient criterion.

### Approach C — eliminate the affine family using multiplicity bounds: rejected

Haiman et al. constructed this family precisely to force polynomial second-eigenvalue multiplicity, and their paper records the general `O(n/log log n)` multiplicity scale together with constructions showing the approximate-multiplicity approach is close to its natural limit. A count of slow modes alone cannot remove the family. The missing datum is coefficient geometry/entropy, which is why Approach A was retained.

## 6. What actually changed and what did not

**Source-level before:** Salez Problem 2.3 `OPEN/PARTIAL`; `W_exp=1/2 provisional`.

**Source-level after:** unchanged. No new complete source-admissible class with a proved TV cutoff is claimed, so the metric remains `1/2 provisional`.

**Mechanism before:** the affine canonical coset contrast was exactly L1-rare, but the actual slow eigenvector had only a fixed L2 perturbation estimate; high multiplicity could not be translated reliably into TV relevance or irrelevance.

**Mechanism after:** the actual slow eigenvector satisfies (3.1), its actual matrix coefficient satisfies (4.1), and its whole high-multiplicity spectral block has the TV bound (4.2)--(4.3). This strictly narrows the affine counterexample/cutoff bottleneck.

## 7. Prior-art boundary

The Haiman--Schildkraut--Zhang--Zhao paper supplies the affine family and high multiplicity; its stated objective is eigenvalue multiplicity. A bounded current search for combinations of `Haiman eigenvector L1`, `high multiplicity Cayley matrix coefficient`, and `L1 eigenvector localization Cayley expander` surfaced that paper and generic eigenvector-localization work, but no exact match to the two-norm estimate above. Negative search evidence is not a priority certificate. Worldwide novelty remains **UNVERIFIED**.

Altschuler remains v1 in the bounded current check. His LRE theorem is not counted as new progress and LRE is not inferred from transitive spectral expansion.

## 8. Tests actually run

No finite mixing plots, simulations, graph enumerations, numerical optimizers or brute-force checkers were run. The new result has no finite computational core.

Analytic self-checks recorded in the artifact:

- exact point-contrast inner products and perturbation source norms;
- the `20+o(1)` L1 compression estimate;
- the `2+4sqrt(7)` L2 bulk estimate;
- the Neumann split and exponent calculation;
- the transitivity-only matrix-coefficient averaging inequality;
- the Peter--Weyl multiplicity factor and continuous-time decay normalization.

Independent audit count remains `0`.

## 9. Matching artifact and readback

Complete proof artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T08-46-43Z_affine-outlier-l1-interpolation_b72f.md`

created at commit

`37c8ec549d16557a7ef8cd255789582ffc6c835e`,

blob

`26b3c3927c6685027a0e5de952afef143e45ce72`,

and read back at that exact commit before this report write.

## 10. Ledger delta and remaining full-scope gap

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  new_graph_class_with_TV_cutoff: false
  mechanism_after:
    - "actual affine slow eigenvector L1(pi)=O(r^{-eta}) for all eta<0.2592245387"
    - "actual slow matrix coefficient L1 exponent can be any value below 0.5184490776"
    - "whole slow block is TV-negligible by (5.8149593+o(1)) log r"
    - "naive parabolic thickening cannot replace LRE because of the (ed)^(-k) path loss"
    - "multiplicity-only elimination is quantitatively exhausted by the Haiman construction"
  finite_checker: "not applicable"
  independent_audits: 0
  publication_novelty: "UNVERIFIED"
  status_label: "OPEN/PARTIAL"
```

The next full-scope mathematical obligation is now sharper: either upgrade the affine coefficient estimate into a Shannon/varentropy bound strong enough to prove cutoff for this genuinely non-LRE source-admissible stress family, or find a transitivity mechanism that controls the positive-information mass for arbitrary source graphs. Another generic L2, multiplicity or superlevel nuclear bound would repeat an exhausted route.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, workflow, shared root, peer file or force push was changed.
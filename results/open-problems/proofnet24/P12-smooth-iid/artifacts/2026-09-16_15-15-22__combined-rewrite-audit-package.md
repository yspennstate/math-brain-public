# P12/P13 combined submatrix-universality rewrite — frozen audit package

**Status:** PERSONAL FINISHING package; not an outside-source problem and not a new conjecture.  
**Repository:** `yspennstate/math-open-problems`, `master`.  
**Owner source:** 2026 P12/P13 submatrix-universality manuscript chain.  
**Purpose:** freeze the corrected theorem scope, source boundary, proof dependencies, no-go results, variance normalization, and the exact claims to be checked by the two required OTHER-track audits. This package does not re-prove the already posted August row-submatrix paper.

## 1. Source boundary

The accessible original June 28 source is

`paper19/sources/extracted_text/extreme_least_singular_values_radial_phase_retrieval_20260628_171349.txt`

with source manifest

`paper19/sources/SOURCE_MANIFEST.md`.

Its Section 8.2 Conjecture 8.2 is a **real fixed-law** smooth-iid conjecture: iid entries are mean zero, variance one, have a bounded sufficiently smooth density, and have sufficiently many finite moments; for fixed integer `r >= 0` and `N_m/m -> gamma>1`,

\[
\frac1m\log M_{m,r}(A_m)\to_{\mathbb P}-\frac{h(\gamma)}{r+1},
\qquad
h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1).
\]

The same source predicts the complex exponent `-h(gamma)/(2(r+1))`. The accessible source does **not** specify the exact differentiability order or the exact number of moments in the words “sufficiently smooth” and “sufficiently many”; those orders are not reconstructed here.

The August 24/25 redundancy attachment is not a separately accessible original binary under the current GitHub-only source surface. Its exact assumptions and theorem were recovered and repeatedly source-certified in immutable P12/P13 reports: centered variance-one **real** bounded-density smooth subgaussian entries, with the stronger moderate-surplus regime `k_m=r_m+1`, `k_m log m=o(m)`, and limit `(k_m/m) log M -> -h(gamma)`. The August 30 request that subgaussianity “may can be replaced by bounded fourth moment” was a rewrite motivation, not a theorem.

The public paper `arXiv:2608.07410` is already posted/excluded by repository policy and is not re-proved in this package.

## 2. Corrected restricted theorem to retain

The combined rewrite does **not** claim universality under bounded fourth moment alone, under arbitrary smooth triangular laws, or under an unspecified weakening of Conjecture 8.2.

For `F in {R,C}`, write `d_F=1` for `R`, `d_F=2` for `C`. For a density `f_m` on `F`, fix once and for all an integer `q>=1` and `M<infinity` and assume

\[
\sup_m\|f_m^{*q}\|_\infty\le M.
\tag{FC}
\]

Let `A_m in F^{N_m x m}` have iid entries `xi_m` satisfying

\[
E\xi_m=0,
\qquad
E|\xi_m|^2=1,
\qquad
(FC),
\]

and assume

\[
N_m/m\to\gamma>1,
\qquad
k_m=r_m+1,
\qquad
k_m\log m=o(m).
\]

Then the retained theorem is

\[
\boxed{
\frac{k_m}{m}\log M^{\mathbb F}_{m,r_m}(A_m)
\to_{\mathbb P}-\frac{h(\gamma)}{d_{\mathbb F}}.
}
\tag{T-FC}
\]

In particular, for fixed `r`,

\[
\frac1m\log M^{\mathbb F}_{m,r}(A_m)
\to_{\mathbb P}
-\frac{h(\gamma)}{d_{\mathbb F}(r+1)}.
\]

This is a **restricted sufficient theorem**, not a claim that `(FC)` is equivalent to the source’s unspecified smoothness/moment package and not a claim of universality for every smooth iid law. No positive moment above two is part of `(T-FC)`.

Canonical theorem records to audit:

1. Real theorem: `P13-REAL-FINCONV-TRIANG-MAIN-27` in  
   `proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_16-07-26__run-report.md`, creation commit `9a39a3c9d0245a98911e646ce9d60950a7828809`, blob `8f06a000273e81633a4590160832e7446fb46dbe`.
2. Unified real/complex theorem: `P12-COMPLEX-FC-TRIANG-MAIN-29`, `P12-REAL-FC-TRIANG-MAIN-29`, and real phase-retrieval corollary `P12-REAL-FC-PHASE-RETRIEVAL-29` in  
   `proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_16-27-01__run-report.md`, creation commit `d3e9069827d796ddf8d8280674ea1fc22f110d27`, blob `d3c2ae8a6c6a7e5a852ae6ca4503bdbd234bc2f6`.

The audits must check the whole inherited proof chain, not merely the displayed final theorem.

## 3. Exact variance normalization

For every scalar `sigma != 0`,

\[
M_{m,r}(\sigma A)=|\sigma|M_{m,r}(A).
\]

Thus a fixed nonzero variance scale is irrelevant to the normalized exponent. For a triangular scale `sigma_m`, the moderate-surplus statistic changes by

\[
\frac{k_m}{m}\log|\sigma_m|,
\]

so the exact exponent-neutral condition is

\[
\boxed{\frac{k_m}{m}|\log|\sigma_m||\to0.}
\]

Scaling does not remove a nonzero mean. Under normalization `Y=xi/sigma`, the finite-convolution ceiling also rescales and must be checked **after** normalization:

\[
\|(f_Y)^{*q}\|_\infty
=|\sigma|^{d_{\mathbb F}}\|f_\xi^{*q}\|_\infty.
\]

Therefore the clean statement of `(T-FC)` is centered, variance-one, and has one uniform post-normalization `(FC)` ceiling.

## 4. Frozen proof dependency map

The two OTHER auditors must verify the following chain end to end.

### A. Analytic consequences of `(FC)`

For real laws, `P13-FINCONV-ANTICONC-27` gives

\[
Q_\xi(r)\le(2qMr)^{1/q}.
\]

The corresponding complex disk estimate is

\[
Q_\xi(r)\le(\pi q^2Mr^2)^{1/q}.
\]

The same fixed-convolution assumption supplies an integrable finite Fourier power by applying the density/Fourier-power estimate to the `q`-fold sum. These are the fixed microscopic regularity inputs used by the inherited local-density/local-CLT modules.

### B. Lower extreme

For each candidate `(m+k-1) x m` matrix, the negative second-moment identity turns `s_min <= t` into a small distance of one fresh column to the span of the others. The orthogonal complement has dimension `k`; bounded projection density/anti-concentration gives the required `t^{d_F k}` factor. Candidate entropy is

\[
\log\binom{N_m}{m+k_m-1}=h(\gamma)m+o(m),
\]

and `k_m log m=o(m)` absorbs polynomial factors. This yields the source lower extreme.

### C. Constructive upper extreme

The nontrivial half uses the validated useful-normal / clean-core / density-level microscopic approximation / adaptive pair / marked-row staging architecture. The auditors must specifically verify that:

- probability is applied only to genuinely fresh original iid rows/columns after adaptive data are frozen;
- no projected coordinates are silently declared iid;
- the marked-row scalar width is `s=t/sqrt(k)`;
- the one-normal source-scale law has no Berry–Esseen additive floor;
- the pair estimate carries the exact projective-angle determinant singularity;
- the near-parallel exceptional set is controlled before the second-moment count;
- all constants are uniform under one fixed `(q,M)` and finite aspect range;
- the real/complex dimension factor is exactly `d_F`.

The canonical P12/P13 theorem reports above contain the complete derivations and references to their predecessor modules; an audit that checks only the top display is not a closure audit.

## 5. Retained no-go results and statement exclusions

The combined rewrite must preserve these restrictions rather than silently upgrading them to a false or unsupported universality theorem.

1. **Triangular smoothness without uniform microscopic regularity is insufficient.** The proved two-column concentration obstruction constructs smooth compactly supported, uniformly subgaussian triangular laws with a narrowing dominant cluster for which the source exponent fails. Therefore the corrected triangular theorem needs a uniform microscopic hypothesis such as `(FC)`.
2. **Bounded fourth moment alone is not promoted to full universality.** P12/P13 derived useful coarse anti-concentration, compressibility, RLogLCD, row-trimming and no-go results, but the full all-aspect constructive upper extreme under B4 alone was never source-matched and end-to-end audited.
3. **Deterministic spread alone is insufficient at source scale.** Smoothed Rademacher-type triangular examples retain polynomial-scale resonant small-ball mass along flat deterministic directions.
4. **Noncentered universality is not claimed.** Scalar variance normalization does not remove the mean.
5. **Complex phase-retrieval stability is not claimed.** The deterministic complex analogue of the real full-spark/Balan–Wang reduction is not supplied by the current package.
6. **No unrestricted logarithmic expectation/UI claim is retained for arbitrary triangular arrays.** Previously recorded rare-event counterexamples remain in force.

These are route/scope boundaries, not claims that the owner’s fixed-law smooth-iid Conjecture 8.2 is false.

## 6. Real phase-retrieval implication

For an absolutely continuous real frame with

\[
N_m=2m-1+r_m,
\]

full spark holds almost surely. The deterministic identity in the owner manuscript gives

\[
\omega(A_m)=M^{\mathbb R}_{m,r_m}(A_m).
\]

Hence `(T-FC)` implies

\[
\boxed{
\frac{k_m}{m}\log\omega(A_m)\to_{\mathbb P}-\log4
}
\]

when `k_m log m=o(m)`. For fixed `r`, the exponent is `-log(4)/(r+1)`. This is the Balan–Wang-type rank-deficient-side obstruction described by the source; for redundant `r>0` the package does not identify it with every possible optimal phaseless lower-Lipschitz constant.

## 7. Independent P12 audit of one P13 component

**Claim audited:** `P13-FINCONV-ANTICONC-27`.  
**Path:** `proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_16-07-26__run-report.md`.  
**Creation commit:** `9a39a3c9d0245a98911e646ce9d60950a7828809`.  
**Blob:** `8f06a000273e81633a4590160832e7446fb46dbe`.  
**Verdict:** PASS / PROVED.

Proof check: if `I=[z-r,z+r]` and `xi_1,...,xi_q` are iid, then the event `{xi_j in I for every j}` implies `xi_1+...+xi_q in qI`, an interval of length `2qr`. Since the `q`-fold sum has density bounded by `M`,

\[
P\{\xi\in I\}^q
\le P\{\xi_1+\cdots+\xi_q\in qI\}
\le2qrM.
\]

Taking the supremum over `z` and the `q`th root yields the stated bound. No centering, variance or moment assumption is used. The quantifiers and constant are exact. This is a component audit only and does not count as either required OTHER-track closure audit.

## 8. Current-source/literature check, 16 September 2026

A fresh arXiv search recovered `arXiv:2608.07410`, *Extreme least singular values of random row submatrices with bounded-density subgaussian entries* (Yang–Wen–Shmalo, submitted 7 August 2026), whose abstract states the centered real bounded-density subgaussian square-candidate theorem with exponent `-h(gamma)` and `C exp(-c sqrt(m))` fixed-epsilon deviations. The search also recovered the July Gaussian paper `arXiv:2607.06249`. No newer public source in the bounded search supplied a theorem matching the internal `(FC)` real/complex moderate-surplus package or resolving the owner’s full smooth-iid conjecture. This bounded search is evidence of no located public replacement, not proof of global absence.

## 9. Frozen obligations for closure

The finishing assignment has exactly seven claim-scoped obligations. This package discharges the first four and freezes the remaining three; future reports must not split or rename them merely to create apparent movement.

1. **DONE — source/scope reconciliation:** exact Conjecture 8.2 boundary, August proof state and posted-work exclusion.
2. **DONE — corrected theorem statement:** `(T-FC)` with real/complex, centered/variance-normalized, triangular uniformity and moderate-surplus assumptions separated.
3. **DONE — proof/no-go/phase-retrieval consolidation:** canonical dependency map and all retained exclusions recorded.
4. **DONE — immutable audit package:** exact paths, SHAs, claim IDs and component self-audit supplied.
5. **OPEN — P26 complete independent OTHER-track audit** of the entire frozen package and inherited proof chain.
6. **OPEN — second complete independent OTHER-track audit**, directed to P11 unless a documented qualified substitute is used.
7. **OPEN — post-audit finalization:** incorporate only audit-required corrections, create the final self-contained `paper_<name>/` handoff required by fleet policy, request P26 ledger retirement/update, and hand the slot to an eligible outside problem.

**Frozen metric after this package: 3 obligations remaining out of 7.**

Until obligations 5–7 close, the correct status is **PARTIAL / mathematically proved restricted theorem, protocol-open**. The owner’s broader smooth-iid Conjecture 8.2 is not relabeled PROVED by this package.
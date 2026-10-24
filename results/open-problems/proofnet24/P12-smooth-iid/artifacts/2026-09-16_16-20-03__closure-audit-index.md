# P12/P13 combined universality rewrite — closure-audit dependency index

**Role:** P12 author-side self-check and auditor navigation aid only. This artifact is **not** an OTHER-track audit and does not decrement the frozen closure metric.

**Frozen theorem scope.** For `F in {R,C}`, `d_R=1`, `d_C=2`, fix one integer `q>=1` and `M<infinity`. Let `A_m in F^{N_m x m}` have iid entries with density `f_m` satisfying

\[
E\xi_m=0,\qquad E|\xi_m|^2=1,\qquad \sup_m\|f_m^{*q}\|_\infty\le M,
\]

and assume

\[
N_m/m\to\gamma>1,\qquad k_m=r_m+1,\qquad k_m\log m=o(m).
\]

The corrected restricted theorem under audit is

\[
\frac{k_m}{m}\log M^{\mathbb F}_{m,r_m}(A_m)\xrightarrow{\mathbb P}-\frac{h(\gamma)}{d_{\mathbb F}},
\qquad h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1).
\]

It is **not** a claim of universality under bounded fourth moment, arbitrary smooth triangular laws, or the source's unspecified phrase “sufficiently smooth / sufficiently many finite moments.”

## A. Source boundary and deterministic normalization

Primary accessible owner source:

`paper19/sources/extracted_text/extreme_least_singular_values_radial_phase_retrieval_20260628_171349.txt`.

Its Section 8.2 Conjecture 8.2 is real, fixed-law, fixed-surplus, centered and variance one, with a bounded sufficiently smooth density and sufficiently many finite moments. The accessible source does not state the differentiability order or moment count. The same source predicts the complex exponent `-h(gamma)/(2(r+1))`.

The exact scalar identity is

\[
M_{m,r}(\sigma A)=|\sigma|M_{m,r}(A).
\]

Hence triangular normalization is exponent-neutral exactly under

\[
\frac{k_m}{m}|\log|\sigma_m||\to0.
\]

Scaling does not remove a nonzero mean. Under `Y=xi/sigma`, the finite-convolution density ceiling scales by `|sigma|^{d_F}`; therefore the uniform `(q,M)` ceiling must be imposed after variance normalization.

## B. Canonical theorem records

### Real finite-convolution theorem

Claim `P13-REAL-FINCONV-TRIANG-MAIN-27`:

`proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_16-07-26__run-report.md`

creation commit `9a39a3c9d0245a98911e646ce9d60950a7828809`, blob `8f06a000273e81633a4590160832e7446fb46dbe`.

### Unified real/complex theorem and real phase retrieval

Claims `P12-COMPLEX-FC-TRIANG-MAIN-29`, `P12-REAL-FC-TRIANG-MAIN-29`, `P12-REAL-FC-PHASE-RETRIEVAL-29`:

`proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_16-27-01__run-report.md`

creation commit `d3e9069827d796ddf8d8280674ea1fc22f110d27`, blob `d3c2ae8a6c6a7e5a852ae6ca4503bdbd234bc2f6`.

## C. Dependency chain an OTHER auditor must check

The top theorem is not auditable by reading only its final display. The end-to-end chain is:

1. **Finite-convolution anti-concentration.** `P13-FINCONV-ANTICONC-27` / `P12-FC-CONCENTRATION-29`: a bounded `q`-fold convolution gives scalar concentration tending to zero at a power rate. P12 independently rechecked the real formula in the frozen package.
2. **Finite Fourier power and projection densities.** The canonical P12 report proves real/complex Fourier-power bounds from the bounded `q`-fold convolution, then low-leverage and fixed-`2q`-basis projection density estimates.
3. **Lower extreme.** `P12-FC-TUNABLE-SPARSEKERNEL-29` supplies arbitrary exponential reliability for sparse-kernel avoidance. Cauchy–Binet extracts `2q` disjoint coordinate bases. The negative second-moment identity plus the projection-density bound gives the real `t^k` and complex `t^{2k}` factors; `k log m=o(m)` absorbs all polynomial losses and candidate entropy is `h(gamma)m+o(m)`.
4. **Clean-core stability.** A fixed tail reveal produces a clean conditional law `g` with `g^{*q}<=p_*^{-q}f^{*q}`. The clean real variance and complex covariance are uniformly nondegenerate.
5. **Microscopic one-normal lower law.** Grouping clean spread coordinates into fixed blocks of size `2q` produces bounded block densities. The inherited planar triangular local-CLT input is `P12-PLANAR-TRIANG-LOCALCLT-19` in `proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_11-30-37__run-report.md`, creation commit `9dd0f7638b1ddc926566ea3739303624a38edb8b`, blob `71a4651f5ba8068c436243531b3f94c457165637`.
6. **Useful-normal geometry.** The canonical P12 theorem reduces useful-normal incompressibility to a fixed symmetrized annulus plus second moments, via the cited Jain–Silwal random-rounding theorem. No projected-coordinate iid assumption is permitted.
7. **Actual adaptive-pair geometry.** The predecessor closure record is `proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_13-33-07__run-report.md`, creation commit `7bdfb3784cf1f65b96782b26bd744f819d6fa590`, blob `ec89bf94e512d1b17134813d75f8c9392a3d4cc4`. It proves the two-scale adaptive private-block transversality and `P12-COMPLEX-STAGE-3TIER-L2-21`; the critical filtration rule is to freeze shared/original adaptive data first and use probability only on genuinely fresh original iid rows.
8. **Real adaptive-pair modules.** The parallel P13 real staging record is `proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_14-07-03__run-report.md`, creation commit `a023f9022c11a92e81854e57316d2408b6d900ac`. The fixed-FC real theorem later imports this staging after replacing the coordinate-`L^2` analytic inputs by finite-convolution ones.
9. **Three-tier survivor arithmetic.** In the canonical P12 report, the complex marked scalar width is `s=k^{-1/2} exp[-lambda m/(2k)]`; the real width is `s=k^{-1/2} exp[-lambda m/k]`. The pair classes have the exact projective determinant singularity and ordinary/medium/bad bounds needed to iterate `k` fresh marked rows. The `O(k log m)` losses are negligible by hypothesis.
10. **Centering.** The lower extreme does not need centering. The constructive upper branch does, through the clean-core frozen-shift contraction. The final theorem therefore remains centered.

## D. Author-side hostile self-checks completed in this run

These checks do not count as independent closure audits.

### D1. Lower-side basis extraction

If an orthonormal row frame `A` for a fresh projection space has every unit vector at distance at least `tau` from every coordinate subspace supported on at most `(2q-1)k` coordinates, then after deleting any previously used coordinate set `R` of that size,

\[
A_{R^c}A_{R^c}^*\succeq \tau^2I_k.
\]

Cauchy–Binet gives a fresh `k`-coordinate basis with determinant at least `tau^k / sqrt(binomial(n,k))`. Iterating `2q` times is therefore legitimate, and the total determinant loss is `exp(O_q(k log m))`, not an exponential-in-`m` loss.

### D2. Marked-row scale

For the real upper extreme, with `s=k^{-1/2}e^{-lambda m/k}`, one stage costs one power of `s`, and

\[
k\log(1/s)=\lambda m+\frac{k}{2}\log k.
\]

For the complex upper extreme, with `s=k^{-1/2}e^{-lambda m/(2k)}`, one stage costs `s^2`, and

\[
2k\log(1/s)=\lambda m+k\log k.
\]

Thus the source exponent is recovered with only `O(k log m)` loss. This rechecks the previously important `s=t/sqrt(k)` correction.

### D3. Real phase-retrieval identity at redundancy

The June owner source defines

\[
\omega(A)=\inf_{J:\operatorname{rank}(A_J)<m,\ |J^c|\ge m}\sigma_m(A_{J^c}).
\]

If `A` is full spark and has `N=2m-1+r` rows, then `rank(A_J)<m` is equivalent to `|J|<=m-1`, hence every admissible complement has at least `m+r` rows. If `S subset S'`, then `A_{S'}^*A_{S'}-A_S^*A_S` is positive semidefinite, so `sigma_m(A_{S'})>=sigma_m(A_S)`. Consequently the infimum over complements of size at least `m+r` is attained at size exactly `m+r`, and

\[
\boxed{\omega(A)=M_{m,r}(A)}.
\]

This verifies the stated stability obstruction. It does **not** identify `omega` with every possible optimal phaseless lower-Lipschitz constant; the June source only asserts the deterministic obstruction `alpha(A)<=omega(A)` for its lower-Lipschitz parameter.

### D4. No silent universality upgrade

The following exclusions remain binding: no B4-only universality claim; no arbitrary triangular smooth-law claim without uniform microscopic regularity; no noncentered theorem; no complex phase-retrieval stability theorem; no unrestricted triangular logarithmic-expectation theorem.

## E. Current audit-slot state

The latest P26 report checked at this run is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_16-01-15__run-report.md`, creation commit `d2ec9d45f78bc19e5e7cee4ad9365790305663f7`, blob `578b7f36f4462da490fd373e73cb054b2d82350a`.

It audits Aldous–Fill/C31, not this P12 package. Therefore it does **not** satisfy obligation 5.

The latest P11 canonical run commit visible at run time is `9ad19b4daad9ca6eaa3d0f3797456b10e6ac46ac` (P11 run at 14:11 local), which predates the frozen P12 audit package and contains no complete P12 end-to-end audit. Therefore obligation 6 also remains open.

The frozen metric remains **3 obligations remaining out of 7**. No author-side self-check may decrement it.
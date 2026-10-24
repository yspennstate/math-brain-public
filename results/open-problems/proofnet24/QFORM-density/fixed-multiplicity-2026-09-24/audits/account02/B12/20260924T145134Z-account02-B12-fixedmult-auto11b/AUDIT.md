# account02/B12 auto11b — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned mathematical source audited here:
- repository: `yspennstate/math-open-problems`
- source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- bytes / lines: `47883 / 790`

This invocation freshly read the complete required package (`README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`) and also `DELIVERY_STATUS.md`, which the package README makes part of the live delivery contract. The live master moved while concurrent auditors wrote additive artifacts, but the delivery status still identifies the manuscript above as byte-for-byte unchanged. Peer verdicts were treated as data, not as proof substitutes.

## Overall verdict

**PASS** for the mathematical theorem actually stated in the pinned manuscript:

`independent real coordinate densities <= K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0` imply an essentially bounded density for `Q=X^TAX+b^TX+c` with

`||p_Q||_infinity <= 10000 K^2/s`.

I found no mathematical `FALSE` item and no proof-affecting `GAP`. The independent PDF build/visual-inspection receipt and bibliographic priority/completeness are `UNCHECKED` in this invocation; neither is a mathematical dependency. The finite checker is a diagnostic, not a proof certificate. The unrestricted three-eigenvalue QFORM conjecture is **not** proved here.

## Complete source-line ledger

Every source line and displayed equation was reread. Contiguous ranges below cover all 790 lines.

| lines | object | status | reasoning / impact / next obligation |
|---|---|---|---|
| 1--46 | preamble, abstract, conventions | PASS | Quantifiers and scope agree with the later theorem; no global-continuity or three-eigenvalue claim is smuggled in. |
| 47--61 | main theorem and 33-eigenvalue corollary | PASS | `s_17(A)>=s` is the actual theorem hypothesis; the corollary is immediate monotonicity of singular values. |
| 62--90 | architecture and constants | PASS | `eta=1/100`, `kappa=1/80^2`, and the `4k-3` rank bookkeeping agree with the later interpolation argument. |
| 91--160 | Fourier inversion, envelope, Riesz half-potential | PASS | Normalizations, Gaussian factor, gamma substitution and constants check; Tonelli is only used on nonnegative majorants. |
| 161--217 | singular-value rank bounds, Schur spectral count, diagonal dominance | PASS | Rank inequalities are applied to singular values where auxiliaries are nonsymmetric. The singular Schur limit is valid; fixed-threshold detail is given below. |
| 218--255 | geometric rank-one Brascamp--Lieb | PASS | Heat-flow sign, small-time Fatou and large-time domination are valid for rough integrable inputs. |
| 256--301 | product-projection density and scalar Fourier powers | PASS | Frame identity, `e^(d/2)` cap, scalar scaling and `p>=2` interpolation are correct; no hidden support/moment hypothesis. |
| 302--400 | decoupling, regularized determinant, crossing volumes | PASS | Copy independence, powers 2/4, graph weights, Jacobian and determinant exponents were checked. |
| 401--422 | scalar-square profile and conditional profile | PASS | Completing-square shifts are conditional translations of an original coordinate. The profile is a measure domination, not an independence assertion. |
| 423--434 | definite physical pair | PASS | Orthogonal diagonalization is only a deterministic integral change of variables; no rotated product law is asserted. |
| 435--482 | hyperbolic physical pair | PASS | Jacobian, middle interval, two tails and rough-density test-function formulation are correct; logarithmic blow-up is the genuine endpoint. |
| 483--525 | quarter-power concentration and logarithmic potential | PASS | Both diagonal/off-diagonal alternatives exclude atoms and give the stated layer-cake logarithmic bound. |
| 526--544 | pivot/volume definitions, no-pivot entry bounds | PASS | Principal-pair determinant condition gives the displayed off-diagonal entry bound; ordered-disjoint conventions are consistent. |
| 545--580 | sampled interpolation and completion | PASS | Bordered determinant identity; nonsymmetric interpolation support; global rank `<=3r`; restricted rank `<=r`; `D=0` on the seed; and zero diagonal of `E` all check. |
| 581--619 | spectral-to-volume proposition | PASS | Rank spending and forced diagonal entries close the contradiction. Numerical slack is exactly `371/400-23/28=297/2800>0`. |
| 620--645 | random coordinate cut and no-pivot analytic consequences | PASS | Each ordered disjoint minor survives the oriented fair cut with probability `4^-k`; constants are safe. |
| 646--653 | truncated half-potential definition | PASS | Atom convention is explicit and is later excluded where singular kernels require it. |
| 654--674 | square-root/logarithmic kernel integrals | PASS | `J(d)` is finite exactly for `d!=0`; the uniform log-kernel constant 8 is valid and sharp at aligned centers. |
| 675--714 | pivot control of truncated half-potentials | PASS | Scalar/definite/indefinite branches are exhaustive, every invoked hypothesis is met, and conditional critical values are handled by nonnegative domination/Tonelli. |
| 715--724 | nine-eigenvalue half-potential | PASS | Pivot branch needs only two surviving large eigenvalues; no-pivot branch correctly uses order-three half-potential. |
| 725--749 | proof of 17-eigenvalue theorem | PASS | Four branches close: no pivot, scalar pivot, definite pair, indefinite pair. Schur counts are sufficient and scaling is exactly `K^2/s`. |
| 750--781 | threshold accounting and limitations | PASS | Dependency summary matches the proof and explicitly leaves the unrestricted three-eigenvalue problem open. |
| 782--790 | acknowledgement/bibliography | UNCHECKED | Bibliographic priority/completeness not independently source-verified; no external theorem is left as an unproved mathematical dependency. |

### Label-by-label hypothesis check

`lem:fourier` PASS; `lem:envelope` PASS; `lem:riesz` PASS; `lem:rank` PASS; `lem:schur` PASS; `lem:dd` PASS; `thm:bl` PASS; `lem:projection` PASS; `lem:scalar-fourier` PASS; `lem:decoupling` PASS; `thm:determinant` PASS; `cor:vol-fourier` PASS; `lem:square` PASS; `lem:definite` PASS; `lem:hyperbola` PASS; `lem:quarter` PASS; `def:pivot-volume` PASS; `lem:sampling` PASS; `lem:completion` PASS; `prop:volume` PASS; `lem:cut` PASS; `cor:no-pivot` PASS; `lem:kernels` PASS; `prop:pivot-H` PASS; `prop:nine` PASS; `thm:main` PASS; `cor:33` PASS.

No invocation above uses a hypothesis stronger than its caller supplies.

## Schur singular-limit dispute resolved

A prior peer report had labelled the singular limit in `lem:schur` a repairable gap; that peer later retracted the label. Independent rereading confirms the original moving-threshold argument is valid.

Let `m=N_A(t)-k`. For `A_epsilon=A+epsilon I`, the invertible-case Schur inequality at threshold `t-|epsilon|` gives

`N_{S_epsilon}(t-|epsilon|) >= N_{A_epsilon}(t-|epsilon|)-k`.

Every eigenvalue of `A` with modulus at least `t` becomes `lambda+epsilon`, whose modulus is at least `t-|epsilon|`; hence the right side is at least `m`. Equivalently

`s_m(S_epsilon) >= t-|epsilon|`.

As `epsilon->0` through values for which the pivot block and full matrix are invertible, `S_epsilon->S`; singular values are continuous, so `s_m(S)>=t`. Therefore `N_S(t)>=m`. The use of a moving threshold is not a gap; phrasing the last step through ordered singular values is the clean fixed-threshold explanation.

## B12 scalar-pivot reconstruction

For an original-coordinate split

`A=[[a,c^T],[c,D]]`,

conditioning on `y=X_-i` gives exactly

`Q=a(X_i-m(y))^2+R(y)`,

`m(y)=-(c^Ty+b_i/2)/a`,

and the quadratic matrix of `R` is the Schur complement `D-cc^T/a`. Conditional translation preserves the density cap of the literal coordinate `X_i`. For nonnegative test functions, the square pushforward therefore implies the measure domination

`p_Q(z) <= |a|^-1/2 E|z-R|^-1/2`

for almost every `z`. There is no assertion that the square and `R` are independent.

The two-coordinate completion is analogous: translation by `-B^-1(Cy+u/2)` is deterministic after conditioning the complement; subsequent rotations occur only inside a deterministic two-dimensional integral.

## B12 endpoint counterexamples and kernel audit

1. **Scalar square cannot by itself give `L^infinity`.** If `X` is uniform on `[-1/2,1/2]`, then `X^2` has density `z^-1/2` on `(0,1/4)`. Thus the residual half-potential in the scalar-pivot branch is essential.

2. **Indefinite pair has a genuine logarithmic singularity.** For independent uniforms `X,Y` on `[-1/2,1/2]`, `Q=X^2-Y^2`. With `u=X-Y`, `v=X+Y`, the joint density is `1/2` on `|u|+|v|<=1`, and for `0<z<1/4`,

`p_Q(z)=log[(1+sqrt(1-4z))/(1-sqrt(1-4z))] ~ log(1/z)`.

Therefore a uniformly bounded indefinite-pair conditional density would be false even for compactly supported cap-one laws. The manuscript correctly keeps the logarithm.

3. **The square-root kernel really fails at exact collision.**

`J(d)=int_{-1}^1 |x|^-1/2 |x-d|^-1/2 dx`

is finite for `d!=0` but `J(0)=infinity`. The quarter-power lemma's atom exclusion and logarithmic-potential bound are therefore logically necessary.

4. **The logarithm is exactly integrable against the square kernel.**

`sup_a int_{-1}^1 |x|^-1/2 log_+(1/|x-a|) dx = 8`,

with equality at `a=0`. Hence the hyperbolic logarithm and scalar square-root singularity are compatible at the endpoint for arbitrary rough laws.

## New paired-source warning for the multiplicity-eight frontier

A recent source-valid multiplicity-eight reduction keeps the shared coordinate after first symmetrization through

`G(u,v)=(1/2) f((v+u)/2) f((v-u)/2)`.

For the uniform cap-one law `f=1_{[-1/2,1/2]}`, this is `G=1/2` on the diamond `|u|+|v|<=1`. Its `u`-slice has mass `1-|u|`; after normalization, the conditional density of `V|U=u` is

`1/[2(1-|u|)]`

on its interval and diverges as `|u|->1`. Therefore **normalizing paired-source slices and reusing a cap-one scalar-pivot/Fourier lemma is FALSE**. Any overlap-one receiver must keep the slice as a subdensity or use an integrated estimate.

There is, however, a safe integrated endpoint inherited directly from the audited hyperbolic kernel. Since `UV=X^2-X'^2` for an independent copy `X'`,

`sup_a intint G(u,v)|uv-a|^-1/2 du dv <= 33+4 log 16 < 45`.

Indeed the baseline indefinite-pair proof at determinant one gives truncated half-potential at most `32+4 log16`, and the contribution outside unit distance is at most one. This estimate requires no support, moment, smoothness or conditional normalization. It is a useful admissible input for a future overlap-one receiver, but by itself does not prove multiplicity eight.

A second logical trap is also ruled out: a uniform **fiberwise** half-potential plus an outer scalar square does not imply a bounded mixture if the fiber law may shift with the scalar coordinate. Let `R_0` be the logarithmically singular four-variable cap-one example from the rank-two crossing counterexample and set `R_h=R_0-gamma h^2`. Every fiber has the same finite, shift-invariant full half-potential, yet `gamma H^2+R_H=R_0` still has unbounded density. Thus any scalar-square use in the overlap-one program must control the dependence of the fiber critical shift; one cannot merely combine two separately finite kernel norms.

## Package files

- `README.md`: PASS for mathematical scope/source pin.
- `SOURCE_MANIFEST.json`: PASS for source identity (commit/blob/SHA/bytes/lines).
- `AUDIT.md`: PASS as historical self-audit, not independent certification.
- `proof_map.csv`: PASS; label/range map agrees with the 790-line source.
- `verify.py`: PASS as a finite diagnostic; it pins the exact manuscript SHA and separates exact assertions from floating diagnostics.
- `checks.json`: PASS as the recorded checker output (`534` exact interpolation seeds, `18` exact volume cases, `240` numerical Schur cases, `30` graph-weight cases). The checker was not treated as proof.
- `DELIVERY_STATUS.md`: PASS as delivery metadata; it explicitly says the release gate remains under review and preserves the Schur-review disagreement/retraction history.

## Status / next obligation

Mathematical baseline: **PASS**. Fatal `FALSE`: none. Proof-affecting `GAP`: none. `UNCHECKED`: independent PDF visual build and bibliographic priority/completeness only.

The complete nine-eigenvalue replacement is independently rechecked in the sibling improvement artifact and its dominant scalar-pivot constant is sharpened. Multiplicity eight remains open: the new B12 obligation is a dependence-safe overlap-one receiver that keeps the paired source unnormalized and controls the fiber critical shift; the half-potential estimates above are safe ingredients but not a density theorem.

Execution context: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native Brain ingestion.

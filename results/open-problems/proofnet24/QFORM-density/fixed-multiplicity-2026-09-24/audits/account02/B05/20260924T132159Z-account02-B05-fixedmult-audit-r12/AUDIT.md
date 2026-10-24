# account02/B05 r12 — full fixed-multiplicity audit

Run: `20260924T132159Z-account02-B05-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Role lens: product-projection densities, rough conditional laws, exceptional slices, adversarial counterexamples.

## Source pin

Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Bytes/lines: `47883 / 790`.

The working master was first read at `1b6a5a125347f5d07c79332ac9ab535d106de5fa` and refreshed during this audit to `6a3dcc2a560799c770b5db496e88179a31e566b6`. The manuscript blob remained exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`; only audit/improvement/support material changed.

I read the complete `README.md`, `SOURCE_MANIFEST.json`, all 790 source lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The support files that were absent in an earlier B05 pass are now present. `checks.json` reports PASS for the new scoped reproducibility suite; that suite is evidence only, not a proof certificate.

## Verdict

**PASS — no mathematical GAP or FALSE statement found in the pinned 17-eigenvalue manuscript.** This is one worker's independent end-to-end reconstruction, not formal verification, journal peer review, or a release certificate. The unrestricted three-eigenvalue QFORM conjecture remains open.

Nonmathematical `UNCHECKED`: I did not independently reproduce the conversation-only PDF render/visual-inspection claim or the historical finite-test counts quoted in the authoring self-audit. Neither is a dependency of the written theorem. The current `verify.py/checks.json` suite is internally consistent with the pinned source and explicitly says it does not reproduce those historical counts.

There is one harmless wording point in the projection proof: after factors with `b_i=0` are dropped, the displayed identity `sum_i(1-b_i)=d` is literally an identity when the sum is understood over all original rows (with `-b log b` continuously extended by zero at `b=0`). If the displayed sum were read only over retained rows, one has `<=d`, which is still sufficient. No constant or downstream conclusion changes.

## Continuous line-range ledger

| Source range | Label / content | Status | Independent check and downstream impact |
|---|---|---|---|
| 1–46 | setup, abstract, singular-value/density conventions | PASS | Quantifiers are arbitrary dimension/signature/remaining spectrum/affine terms and rough independent coordinate laws. No hidden continuity or moment assumption. |
| 47–61 | `thm:main`, `cor:33` | PASS | Exact statement is `s_17(A)>=s>0 => ||p_Q||_inf<=10^4 K^2/s`; 33 is immediate since `s_17>=s_33`. |
| 62–90 | architecture, parameters, Fourier conventions | PASS | `eta=1/100`, `kappa=1/80^2`; pivot/no-pivot split is exhaustive. No rotated-coordinate independence claim. |
| 91–120 | `lem:fourier` | PASS | Gaussian regularization proves Plancherel; `phi in L1` gives a bounded continuous density; Gaussian inversion/Fubini constants match the stated Fourier convention. |
| 121–130 | `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`, giving `ap/[pi(p-1)]`. |
| 131–160 | `lem:riesz` | PASS | Gamma/Tonelli calculation gives exactly `1/sqrt(2pi)` in the half-potential formula; the `3/4` envelope contributes `12 sqrt u`. Extended values handle atoms correctly. |
| 161–181 | singular-value conventions, `lem:rank` | PASS | Approximation formula gives both nonsymmetric perturbation and rank inequalities used later. |
| 182–207 | `lem:schur` | PASS | Invertible case follows from the complementary block of `A^{-1}` and positive/negative interlacing; singular case is valid under `A+eps I` with the moving threshold and eigenvalue continuity. |
| 208–217 | `lem:dd` | PASS | Standard max-coordinate proof works for nonsymmetric matrices. |
| 218–255 | `thm:bl` | PASS | Heat flow sign is correct: `partial_t F-Delta F=F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`; large-time normalization uses `sum c_i=d` and the frame identity; rough inputs follow by Lebesgue points, Fatou, truncation, monotone convergence. |
| 256–282 | `lem:projection` | PASS | Reconstructed below in detail. Bound is `||p_{U^T X}||_inf<=e^{d/2}` without any post-rotation independence. |
| 283–301 | `lem:scalar-fourier` | PASS | `g=f*tilde f<=1`; for `m=floor(p/2)`, `2m<=p` and `m>=p/4`; projection bound for the sum of `m` independent differences yields `2pi sqrt(2e)/sqrt p`. |
| 302–324 | cross-form definition, `lem:decoupling` | PASS | Cauchy–Schwarz and an independent copy give the squared product; Jensen gives the fourth-power version. Difference coordinates remain independent cap-one variables. No moments required. |
| 325–373 | `thm:determinant` | PASS | The regularized frame, Jacobian factors, `c_j,d_i` weights, scalar Fourier powers and entropy inequality cancel exactly at `alpha=(2pi e)^2`, giving determinant exponent `-1/8` and argument `t^2/(pi^2 e^2)`. |
| 374–400 | crossing volumes, `cor:vol-fourier` | PASS | Cauchy–Binet expansion is exact. Retaining the order-5 term gives density `5e Z_5^{-1/10}`; order 3 plus Riesz gives the stated half-potential. |
| 401–414 | `lem:square`, conditional profile | PASS | Two inverse branches give the exact `|z-v|^{-1/2}` profile. The manuscript correctly uses this as conditional measure domination via nonnegative tests/Tonelli, not as an unconditional independence statement. |
| 415–434 | profile consequence, `lem:definite` | PASS | Completing the square and deterministic orthogonal diagonalization preserve the joint density cap through Jacobian one; polar quadratic coordinates give `pi M/sqrt(|det B|)`. |
| 435–482 | `lem:hyperbola` | PASS | Hyperbolic Jacobian is `1/(2sqrt D)`; positive/negative tails are paid in an original coordinate by density cap plus mass one; middle length gives the logarithm; `Lambda>=2/sqrt D` yields the stated `16sqrt D/|z-v|`. The critical level is used only through test functions/Tonelli. |
| 483–525 | `lem:quarter` | PASS | Diagonal pivot gives square-root small ball; otherwise random-sign splitting yields a physical cross block of norm `>=L/4`, determinant decay `|t|^{-1/4}`, and the Gaussian calculation gives the quarter-power bound. Layer cake yields `4+4 log16` and no atoms. |
| 526–544 | pivot-volume definition and no-pivot entry bounds | PASS | No principal 2x2 pivot implies `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. |
| 545–564 | `lem:sampling` | PASS | Determinant-squared volume sampling, bordered determinant identity and the `(r+1)^2` extension count are correct. Singular seeds only decrease the count, so the inequality direction is correct. `P` may be nonsymmetric and interpolates rows `S`/columns `T` exactly. |
| 565–580 | `lem:completion` | PASS | `E` is the off-diagonal residual only on `LxL`; `D` is diagonal and vanishes on the seed. `R-P` is supported in rows `T` or columns `S`, giving global rank `<=3r`, while `R_LL=P_LL` has rank `<=r`. |
| 581–619 | `prop:volume` | PASS | Telescoping finds a bad ratio. `r=0` contradicts `||A||<1`. For `r>=1`, rank subtraction forces `r+1` large diagonal entries in `L`; `371/400` diagonal versus `<23/28` row sum makes `R_HH` invertible, contradicting restricted rank `<=r`. |
| 620–630 | `lem:cut` | PASS | Each ordered disjoint `(S,T)` survives a fair physical cut with probability `4^{-k}`. |
| 631–645 | `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160`; constants are `12sqrt(80e)<200` for `k=3` and `800e<2400` for `k=5`. |
| 646–674 | truncated half-potential definition, `lem:kernels` | PASS | Both singular integrals are locally integrable at their simultaneous singularities in the stated form; the far `J(d)` region gives the logarithm and interval-overlap rearrangement gives the uniform log-kernel bound 8. |
| 675–714 | `prop:pivot-H` | PASS | Scalar branch invokes Schur + quarter-power no-atom/log control; definite branch has a uniform conditional density; indefinite branch integrates the logarithmic envelope before averaging. Constants remain `<600`. |
| 715–724 | `prop:nine` | PASS | Pivot branch uses the preceding proposition; no-pivot branch has the stronger full half-potential `<200`; tail outside distance one costs at most one. |
| 725–749 | proof of main theorem | PASS | Scalar pivot leaves at least 16 unit directions and uses the nine-direction half potential, giving 6010; definite pair `<40`; indefinite pair leaves at least 15 and uses the log potential, `<251`; no-pivot `<2400`. All conditional assertions are test-function/Tonelli statements. Scaling by `Y=KX` gives exactly `K^2/s`. |
| 750–790 | threshold accounting, limitations, remarks, bibliography | PASS | Correctly distinguishes order-3 half potential from order-5 density, asserts only essential boundedness in mixed pivot branches, and explicitly does not claim the three-eigenvalue conjecture. Classical citations are attribution rather than proof dependencies. |

No source line is left mathematically `UNCHECKED` in this pass.

## B05 reconstruction: product-projection density

Let `U^T U=I_d` and complete it to the orthogonal matrix `(U,W)`. Fubini gives the marginal

`p(y)=int prod_i f_i((Uy)_i+w_i.z) dz`.

With `b_i=||w_i||^2=1-||U^T e_i||^2`, discard `b_i=0` factors only because they are bounded by one. For the rest, `v_i=w_i/sqrt(b_i)` and `sum b_i v_i v_i^T=I`. Apply the proved geometric Brascamp–Lieb theorem to

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`.

Since `0<=f_i<=1`, `int h_i<=b_i^{-1/2}`. Therefore

`p(y)<=prod b_i^{-b_i/2}`.

Using the continuous convention `0 log0=0`, `-b log b<=1-b`, and

`sum_i(1-b_i)=sum_i ||U^T e_i||^2=tr(U^T U)=d`,

we obtain `p(y)<=e^{d/2}`. No coordinate of `U^T X` is ever declared independent. The scalar consequence is `sqrt(e)/|a|` after normalizing `a`.

This exact bound is also safe under deterministic full-row-rank linear maps: if `L` has `d` rows, SVD gives

`||p_{LX}||_inf <= e^{d/2}/sqrt(det(LL^T))`.

That deterministic scaling is the only projection-density transfer used in the new grouped crossing compiler reviewed below.

## B05 exceptional-slice stress tests

These are valid cap-one counterexamples to tempting shortcuts; none contradicts the manuscript.

1. **Rotated conditional caps can blow up.** Let `X_1,X_2` be independent uniform variables on `[-1/2,1/2]`, and
   `Y=(X_1+X_2)/sqrt2`, `Z=(X_1-X_2)/sqrt2`. The joint density of `(Y,Z)` equals one on `|Y|+|Z|<=1/sqrt2`. Hence
   `p_Y(y)=sqrt2-2|y|`, while
   `p_{Z|Y=y}=1/(sqrt2-2|y|)` on its conditional interval. The conditional cap diverges as `|y|->1/sqrt2`. An unconditional projection-density bound therefore cannot be promoted to a conditional cap after rotation.

2. **The square critical slice is genuinely singular.** For `X~Unif[-1/2,1/2]`, `X^2` has density `t^{-1/2}` on `(0,1/4)`. The scalar profile must be integrated as a singular kernel; it cannot be replaced by a pointwise uniform density bound.

3. **The hyperbolic critical slice is genuinely logarithmic.** If `W_1,W_2` are independent uniform variables on `[-1/2,1/2]`, then for `Z=2W_1W_2`,
   `p_Z(z)=log(1/(2|z|))` for `0<|z|<1/2`. Thus a uniform bounded conditional hyperbolic density is false.

4. **Exceptional points can sweep a positive-measure set under conditioning.** If an independent `Y~Unif[-1/2,1/2]` is added and `Q=Y+2W_1W_2`, the conditional density given `Y=y` has its logarithmic singularity at `z=y`. There is no single output-null set on which all conditional pointwise formulas are simultaneously regular. The correct interface is exactly the manuscript's nonnegative-test-function domination followed by Tonelli; it integrates the singular kernel before choosing an output version.

A useful safe formulation is: if for almost every conditioning value `y`, the conditional output measure obeys
`int phi dmu_y <= int phi(z) K(z,y) dz` for every nonnegative measurable `phi`, then the mixed law is dominated by `E[K(z,Y)] dz` by Tonelli. No common pointwise exceptional set and no conditional independence assertion is needed.

## Fresh threshold reduction: independent B05 review of the nine-direction replacement

During this run a complete replacement proof was committed at
`improvements/account02/B10/20260924T131229Z-account02-B10-fixedmult-r11/NINE_THRESHOLD_REPLACEMENT.md` (blob `070c26607338258ae6feca3dd5d40427cc3dbc91`). I read the full replacement and independently reconstructed its product-projection/rough-law steps and endpoint assembly.

**B05 verdict on that replacement: PASS.** It proves, subject to the repository's ordinary independent-review gate,

` s_9(A)>=s > 0  =>  ||p_Q||_inf <= (2010+1200 log16) K^2/s < 5338 K^2/s. `

The central new grouped compiler is source-valid. For a literal hub bank `H` and disjoint original-coordinate banks `I,J`, the complex pushforward of `e^{itF}dP_H` through a `k`-dimensional orthogonal projection has variation density bounded by the ordinary projection density, hence `L^2` norm squared at most its cap. The second complex pushforward is mollified before taking an `L^2` norm. Expanding its square uses an independent copy only of the original `J` bank; averaging the original `I` variables yields scalar Fourier factors. Thus there is no illicit conditional cap or post-rotation independence.

For each weighted `ell`-subset, the map of the independent difference bank has Gram determinant
`S^2 det(C_T C_T^T)`. Applying the baseline projection theorem followed by deterministic SVD scaling gives exactly
`e^{(k+ell)/2}/[S sqrt(det(C_T C_T^T))]`. Weighted Hölder uses inclusion marginals `alpha_i`; the condition `alpha_i<=1/2` makes the baseline scalar Fourier power lemma applicable at `p=1/alpha_i>=2`. Ordering a random weighted `ell`-subset uniformly gives

`H(w)+sum alpha_i log alpha_i <= ell log ell-log(ell!)`,

so the determinant and marginal entropy factors combine with no dimension-dependent loss. This yields the claimed `|t|^{-(k+ell)/2}` envelope. All zero marginals are explicitly discarded, avoiding undefined `1/alpha_i` notation.

The promotion tree is also exact: a heavy order-three row satisfies
`J_i=||w||^2 e_2(CC^T)`; after a second promotion,
`H_ij=det(PP^T)||C_2||_F^2`; a third heavy row supplies a literal rank-three Gram determinant. Thus every order-three crossing volume is converted into a bounded density with worst constant

`C_3=3 sqrt2 e (9/2)^(1/6)=14.81833766...`.

Similarly every order-two crossing volume gives a full negative-half potential with

`C_2=8 sqrt(e) 2^(-1/8)=12.09507257...`.

Assembly is numerically consistent: no pivot and `s_9>=1` gives `E_3^{-1/6}<=160`, hence density `<2370.935`; at a scalar pivot the residual Schur complement has eight unit directions. If it has a pivot, its full half potential is at most `201+120 log16`; if it has no pivot, order two gives `<152.992`. Multiplying the worst residual half potential by `eta^{-1/2}=10` gives

`2010+1200 log16 = 5337.106466687737... < 5338`.

Definite and indefinite two-coordinate pivots remain much smaller. Scaling is exactly the baseline `K^2/s` scaling. The replacement includes a closed dependency map and preserves arbitrary affine terms, arbitrary signs/remaining spectrum, and arbitrary rough independent coordinate densities.

I therefore regard **nine** as the lowest fixed multiplicity for which a complete replacement proof is currently present and passes this independent B05 reconstruction. I do **not** mark it independently validated or released: the owner requires two genuinely separate complete reviews and reconciliation before that status.

The replacement also gives the correct barrier to an automatic `9->8` step. An order-two crossing lower bound alone cannot force bounded density: for independent `U,V~Unif[-1,1]`, each density is `1/2<=1`, `U^2` has density `1/(2sqrt y)` on `(0,1)`, and the density of `U^2-V^2` at zero contains `int_0^1 (1/(2sqrt y))^2 dy=infinity`. This is a counterexample to the proposed order-two receiver, not to an eight-eigenvalue theorem. No threshold below nine is claimed here.

## Package/support-file status

`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are all now present. The manifest pins the source blob/hash above and says the manuscript source is unchanged. The new checker reports 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur threshold cases and 30 floating graph-weight cases, all PASS. The checker itself correctly labels these as finite diagnostics rather than mathematical verification.

## Final status and next obligation

- Pinned 17-eigenvalue manuscript: **PASS** in this end-to-end audit.
- Product-projection and exceptional-slice interface: **PASS**, with four explicit shortcut counterexamples recorded above.
- Fresh complete nine-eigenvalue replacement: **PASS in this independent B05 reconstruction; independent-validation/release gate still pending**.
- Threshold below nine: **UNCHECKED/OPEN**. The next obligation is not to reuse order-two crossing volume as a black-box density receiver; it requires genuinely additional overlap/multibank structure or a different analytic endpoint.
- Unrestricted three-eigenvalue QFORM conjecture: **OPEN**.

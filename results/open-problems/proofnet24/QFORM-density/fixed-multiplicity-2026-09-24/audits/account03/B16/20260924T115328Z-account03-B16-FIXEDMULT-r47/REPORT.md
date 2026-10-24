# account03/B16 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T115328Z-account03-B16-FIXEDMULT-r47`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Execution status: `WITHOUT_VERIFIED_BRAIN`
Audited canonical source: `yspennstate/math-open-problems`, `master`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
Initial source commit specified by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Source git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Declared source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
Fresh master checked before publication: `e5f053b3e07a61548323bebca07a5e05687e3bb7`; the manuscript blob was still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B16 end-to-end audit, with one nonfatal local wording gap and one nonmathematical repository-package gap.** I found no fatal defect in the complete manuscript. The proof supports the stated conclusion

\[
 s_{17}(A)\ge s>0\quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signs and remaining spectrum, and arbitrary affine `b,c`.

This report is one independent scheduled-worker audit, not formal verification and not a self-awarded independent-validation certificate. The full three-large-eigenvalue conjecture remains open. The manuscript proves global essential boundedness, not global continuity; only the no-pivot Fourier branch automatically gives a continuous density.

I completed the mathematical audit before consulting any peer audit verdict. Afterward I compared against the already-published account03/B20 review and found agreement on the same local projection-lemma wording issue and the same missing-package issue. I do not alter the repository's review-status label here; the owner/release gate should adjudicate whether the separate reviews satisfy its two-review requirement.

## End-to-end source ledger

### Lines 1–120 — theorem, quantifiers, normalization architecture, Fourier inversion: PASS

The theorem keeps all required quantifiers: arbitrary dimension, independent rough coordinate laws with only `0<=f_i<=K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine terms. The normalization at the end is consistent: with `Y=KX`, the normalized quadratic is

`Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`,

and `Q=(s/K^2) \widetilde Q`; density scaling therefore produces `K^2/s`.

The Gaussian regularization, Plancherel convention and inversion constant are mutually consistent. No smoothness or moment assumption enters.

### Lines 121–240 — power envelope, Riesz half potential, singular-value/rank lemma, Schur count, heat-flow BL: PASS

The negative-half-moment identity has the correct normalization:

\[
 \mathbb E|Z-a|^{-1/2}
 \le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|\,dt.
\]

The `3/4` characteristic-function exponent is used only after multiplication by the Riesz weight, never as a direct `L^1` density estimate.

For an invertible principal pivot `B`, the complementary principal block of `A^{-1}` is `S^{-1}` for the Schur complement `S`. Positive and negative eigenvalue interlacing of that principal compression gives `N_S(t)>=N_A(t)-k`; the singular case is legitimately recovered through `A+epsilon I` and continuity.

The geometric Brascamp–Lieb heat-flow calculation has the correct sign. If `W` has columns `sqrt(c_i)u_i`, then `WW^T=I`; hence

\[
 \left|\sum_i c_i u_i v_i\right|^2\le\sum_i c_i v_i^2.
\]

The compact-support heat-flow limit and monotone truncation to general integrable nonnegative functions are adequate.

### Lines 241–360 — BL limit, product projections, scalar Fourier powers, decoupling, start of determinant theorem: PASS except one local wording GAP

The product-projection proof correctly keeps all rotations inside a deterministic marginal integral and never asserts rotated independence. The frame on the orthogonal complement is valid and gives the universal cap `e^{d/2}`.

**GAP-NONFATAL — product-projection entropy line.** After rows with `b_i=0` are dropped, the manuscript writes

`sum_i (1-b_i)=d`.

If that sum is understood over the retained indices `b_i>0`, equality is not generally true. The correct statement is

\[
 \sum_{b_i>0}(1-b_i)\le d.
\]

Equivalently, equality holds for the full sum over all physical rows before omitting the zero-`b_i` rows. Since this line is used only in an upper bound, replacing `=` by `<=` repairs the proof with no change in theorem or constants.

The integrated scalar Fourier-power lemma is not circular: `|fhat|^{2m}` is integrable because `|fhat|<=1` and `|fhat|^2` is integrable by Plancherel. Fourier inversion therefore legitimately evaluates the continuous convolution density at zero.

The two-copy decoupling uses only original-coordinate independence. The fourth-power bound is a Jensen consequence of the second-power nonnegative majorant.

### Lines 361–480 — regularized determinant, crossing-volume identities, square/definite/hyperbolic kernels: PASS

For `H=alpha I+a^2M^TM`, the vectors generated by the physical coordinate axes and the rows of `M` form the exact weighted frame. The weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2m_i^T H^{-1}m_i`

satisfy the trace identity used in the entropy cancellation. Applying the scalar Fourier-power estimate with `p=2/d_i` gives the exact `sqrt(d_i)` factor required to cancel the graph-BL scale. With `alpha=(2pi e)^2` and `a=2t`, fourth-rooting yields

\[
 |\phi_Z(t)|\le\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy–Binet gives the stated `Z_k` expansion. Retaining the order-`k` coefficient gives exponent `k/4`. Thus order five is genuinely integrable and order three is genuinely sufficient only for the half-potential calculation.

The scalar-square and definite-pair arguments are deterministic changes of variables applied after conditioning on original coordinates. The beginning of the hyperbolic-pair proof correctly parametrizes the two sheets and uses the Jacobian `1/(2 sqrt(|det B|))`.

### Lines 481–600 — hyperbolic tails, quarter-power concentration, disjoint-minor sampling and completion: PASS

The hyperbolic tail estimate uses only one original-coordinate density cap at a time plus total mass; it does not rotate the product law. Its exceptional critical level is harmless because the argument is a measure-domination/Tonelli statement.

The quarter-power concentration dichotomy is valid. If no diagonal entry carries half the operator norm, the sign-partition argument extracts an original-coordinate cross block of operator norm at least `L/4`; the regularized determinant theorem then supplies the `|t|^{-1/4}` envelope used under Gaussian smoothing. This does not invoke the refuted law-uniform pointwise quadratic van-der-Corput estimate.

For a sampled disjoint seed `B=A_{S,T}`, the bordered determinant identity

\[
 \det A_{S\cup\{\ell\},T\cup\{m\}}^2
 =\det(B)^2(A_{\ell m}-P_{\ell m})^2
\]

is correct up to sorting signs, which vanish after squaring. Singular seeds contribute zero seed weight, so the aggregate extension count is correctly used as an inequality rather than an equality.

For the completion `A=D+R+E`, I independently checked the support statement. `R-P` vanishes on rows `S`, columns `T`, and the full `L x L` block. Every remaining entry is therefore in a row of `T` or a column of `S`; decomposing those two supports gives rank at most `2r`, hence `rank R<=rank P+2r<=3r`. On `L x L`, however, `R=P`, so the sharper `rank R_{L,L}<=r` is exact. `D` really does vanish on all seed coordinates `S union T`.

### Lines 601–720 — spectral-to-volume contradiction, random cut, no-pivot estimates, singular kernels and pivot half-potential: PASS

Suppose the volume ratio at a sampled order `r` is below `kappa`. The manuscript obtains

`||E||_F <= (r+1)sqrt(kappa) <= 1/16` for `r<=4`.

With `m=4k-3` and global `rank R<=3r`, singular-value rank perturbation forces at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`; they must lie in `L` because `D` vanishes on the seed. On those coordinates,

\[
 |R_{ii}|\ge 371/400,
 \qquad
 |R_{ij}|<1/7+1/16.
\]

For `r<=4`, the row off-diagonal sum is `<23/28<371/400`, so `R_{H,H}` is invertible of rank `r+1`, contradicting the restricted rank bound `<=r`. The `r=0` case separately uses the Frobenius norm of the off-diagonal part and is correct.

A fair cut retains each ordered disjoint `k`-minor with probability `4^{-k}`. Combining this with `k=3` gives the full half-potential bound in the no-pivot nine-direction branch; `k=5` gives the no-pivot bounded density in the seventeen-direction branch.

The two elementary singular-integral bounds are used in the correct truncated/full roles. In the scalar-pivot half-potential estimate the remainder has one surviving large Schur direction, which is exactly what the logarithmic-potential lemma requires. The definite and indefinite pair alternatives cover all nonscalar pivots.

### Lines 721–790 — nine-eigenvalue half potential, main theorem, threshold accounting and regularity scope: PASS

The nine-eigenvalue proposition correctly separates the pivot and no-pivot branches. The tail outside distance one contributes at most one, giving the full half potential `<=601` from the truncated `<=600` estimate.

In the final theorem:

- no pivot + `s_17>=1` gives density `<2400`;
- scalar pivot removes one coordinate and Schur leaves at least sixteen large directions, more than the nine needed for the full half-potential bound, yielding `6010`;
- definite pair gives `<40`;
- indefinite pair removes two directions and leaves at least fifteen; one is enough for the logarithmic-potential bound, yielding `<251`.

All branches are below `10000`. The final scaling to arbitrary `K,s` is correct.

The manuscript's stated regularity scope is also correct: the no-pivot branch has `phi in L^1`, hence a continuous density. The pivot branches establish domination by an `L^infty` density but do not prove continuity, so the global theorem should remain an essential-density statement.

## Exact threshold analysis beyond the baseline

I did not find a rigorous theorem lowering 17 in this run. I did, however, isolate the exact obstruction to a one-step `17 -> 16` improvement in the manuscript's interpolation mechanism.

For a hypothetical no-pivot matrix with `s_16(A)>=1`, repeat the sampled-volume contradiction. For every sampled ratio index `r<=3`, sixteen directions are already enough because `16>=4r+1`; the existing diagonal-dominance contradiction works unchanged. The only new case is the saturated seed order `r=4`.

At `r=4`, the same seed estimate gives `epsilon<=5/80=1/16`. Global rank `rank R<=12` and `s_16(A)>=1` force only four, not five, large entries of `D` on the complement `L`. Choose those four coordinates as `H`. Then

\[
 |P_{ii}|=|R_{ii}|\ge1-1/16-1/100=371/400.
\]

Using the sharper no-pivot entry estimate

\[
 |A_{ij}|<\sqrt{\eta+\eta^2}=\sqrt{101}/100
\]

and `|E_{ij}|<=1/16`, for `i!=j` in `H` we get

\[
 |P_{ij}|<\sqrt{101}/100+1/16.
\]

Hence each off-diagonal row sum is strictly below

\[
 3\left(\frac{\sqrt{101}}{100}+\frac1{16}\right)
 =0.4889962686\ldots
 <\frac{371}{400}=0.9275.
\]

Therefore `P_{H,H}=R_{H,H}` is invertible of rank four. This **does not contradict** the available restricted rank bound `rank P_{L,L}<=4`; it saturates it exactly. Moreover

\[
 P_{H,H}=A_{H,T}B^{-1}A_{S,H},
\]

so its invertibility forces both `A_{H,T}` and `A_{S,H}` to be invertible. Thus the unresolved `s_16` endpoint is not arbitrary: after the preceding alternatives fail, one reaches a three-bank order-four configuration `(S,T,H)` with all three relevant 4x4 maps nondegenerate. A future 16-eigenvalue proof should exploit this triangular bank geometry rather than repeat the rank contradiction.

Likewise the direct `17 -> 13` attempt through order-four crossing volume does not close: the current determinant theorem gives characteristic-function exponent exactly `4/4=1`, i.e. only a borderline `|t|^{-1}` absolute envelope. A 13-eigenvalue theorem needs a new endpoint small-ball/density estimate or cancellation beyond absolute Fourier inversion. No multiplicity reduction is claimed from this observation.

## Repository-package gap

**GAP-REPRODUCIBILITY, nonmathematical.** At the fresh repository snapshot I inspected, the manuscript root contained `manuscript.tex`, `README.md`, `AUDIT.md`, and `audits/`. The README refers to `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json` as canonical package files, but those four files were absent from the root listing and a direct code search did not locate `proof_map.csv`. I therefore could not independently rerun the advertised finite checker from the repository package in this run. This does not affect the self-contained symbolic proof in `manuscript.tex`; it should be repaired before claiming the repository itself contains the complete reproducibility package.

## Final status and next obligation

- 17-eigenvalue mathematical baseline: **PASS in this independent B16 audit**.
- Fatal mathematical defect: **none found**.
- Local mathematical wording repair: **one**, in the product-projection entropy sum; theorem unaffected.
- Reproducibility package: **GAP**, four README-named files absent from the inspected root.
- Multiplicity reduction proved here: **none**.
- Useful threshold refinement: exact `s_16` saturation forces an invertible three-bank order-four configuration; this is a next structural target, not a theorem.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN/not proved by this manuscript**; essential bounded density is what is audited.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**.

Next mathematical obligation: exploit the forced order-four triangular bank geometry in the saturated `s_16` no-pivot case, or prove an order-four endpoint density/small-ball theorem that improves the borderline `|t|^{-1}` absolute Fourier envelope while retaining original-coordinate product provenance.

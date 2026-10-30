# fleet03/B18 independent audit and primary-source prior-art check

Run: `20260924T115853Z-fleet03-B18-QFORM-fixedmult-audit-r11`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Execution status: `WITHOUT_VERIFIED_BRAIN`

## Source pin

Audited repository: `yspennstate/math-open-problems`
Canonical manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
Owner-specified initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Git blob read in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Declared SHA-256 in the owner README/AUDIT: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
Fresh master observed during the audit: `e5f053b3e07a61548323bebca07a5e05687e3bb7`; the manuscript blob was still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem, with one nonfatal presentation clarification and one nonmathematical repository-package gap.** I found no fatal mathematical defect after an independent end-to-end reread and rederivation of the complete 790-line source.

The audited theorem is exactly:

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary dimension, independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`. The proof establishes an essentially bounded density. It does not establish global continuity, and it does not solve the full three-eigenvalue conjecture.

This is one independent worker review, not Lean/formal verification and not a self-awarded independent-validation certificate.

## Complete source ledger

### Lines 1-120: theorem, quantifiers, normalization, Fourier identities — PASS

The theorem keeps all quantifiers. With `Y=KX`, the normalized form is

`Y^T(A/s)Y + (K/s)b^T Y + (K^2/s)c = (K^2/s)Q`,

so density rescaling gives the claimed `K^2/s` factor. The Fourier convention, Gaussian regularization, Plancherel normalization, inversion constant, and the power-envelope integral are mutually consistent. No moments or smoothness are inserted.

### Lines 121-240: negative half moment, singular values, Schur count, heat-flow BL — PASS

The Riesz calculation gives

\[
\mathbb E|Z-a|^{-1/2}\le (2\pi)^{-1/2}
\int |t|^{-1/2}|\phi_Z(t)|\,dt.
\]

The `3/4` Fourier exponent is used only with this `|t|^{-1/2}` weight, not as an `L^1` density estimate.

For an invertible principal pivot `B`, `S^{-1}` is the complementary principal compression of `A^{-1}`. Positive and negative interlacing separately imply `N_S(t)>=N_A(t)-k`; the singular case is correctly recovered by `A+epsilon I` and eigenvalue continuity.

In the geometric Brascamp-Lieb proof, `sum c_i u_i u_i^T=I` makes the heat-flow error

\[
\sum c_i v_i^2-\left|\sum c_i u_i v_i\right|^2
\]

nonnegative. The large-time Gaussian limit, small-time Fatou step, and monotone truncation close the rough-function case.

### Lines 241-360: product projections, scalar Fourier powers, decoupling — PASS with a presentation clarification

The projection proof rotates only a deterministic integral; it never treats rotated random coordinates as independent. For `b_i=|w_i|^2`, the frame identity on the orthogonal complement is correct, and the manuscript obtains `||p_{U^T X}||_infinity<=e^{d/2}`.

**CLARIFICATION-NONFATAL.** After factors with `b_i=0` are dropped, the line `sum_i(1-b_i)=d` must be read as the sum over all physical rows, with the omitted `b_i=0` rows contributing `1` on the right and `0` to `-b_i log b_i`. If one instead reads that sum as restricted to retained `b_i>0` rows, only `<=d` is true. Either reading needed for the proof gives the same upper bound `e^{d/2}`. This is wording, not a theorem gap.

The scalar Fourier-power lemma is not circular: `|fhat|^{2m}` is integrable because `|fhat|<=1` and `|fhat|^2` is integrable by Plancherel, so inversion legitimately evaluates the continuous convolution density at zero. The two-copy decoupling uses only original-coordinate independence, and the fourth-power estimate is Jensen applied to the nonnegative second-power majorant.

### Lines 361-480: regularized determinant, crossing volumes, scalar/definite/hyperbolic changes of variables — PASS

For `H=alpha I+a^2 M^TM`, the manuscript's `c_j,d_i` form the exact weighted frame. The `d_i` powers from Brascamp-Lieb cancel those from the scalar Fourier estimate; the `c_j` entropy penalty is correctly bounded by `e^{theta/2}`. With `alpha=(2*pi*e)^2`, `a=2t`, and fourth-rooting, this gives

\[
|\phi_Z(t)|\le\det\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy-Binet gives the `Z_k` expansion. Retaining the order-five term produces an integrable `|t|^{-5/4}` envelope; retaining order three produces exactly the weighted half-potential estimate.

The scalar-square and definite-pair bounds are ordinary conditional changes of variables on original coordinates. The hyperbolic pair proof parametrizes deterministic level sets and retains the original-coordinate density factors; it never imports independence into the eigenbasis.

### Lines 481-600: hyperbolic tails, quarter-power concentration, disjoint-minor sampling/completion — PASS

The hyperbolic tail estimate needs only one original-coordinate density cap plus unit mass at each tail; the critical level is handled at the measure-domination/Tonelli level.

The quarter-power lemma first uses a physical diagonal if available. Otherwise a random sign cut of the off-diagonal matrix produces a physical cross block `M` with `||M||>=||S||/4`; the determinant theorem then gives the needed `|t|^{-1/4}` envelope under Gaussian smoothing. This is not the refuted law-uniform pointwise van-der-Corput estimate for a rough quadratic phase.

For a sampled disjoint seed `B=A_{S,T}`, the nonsymmetric interpolation

`P=A[:,T] B^{-1} A[S,:]`

is legitimate. The bordered determinant identity is correct up to sorting signs, which disappear after squaring. Singular seeds have zero sampling weight, so extensions are counted with an inequality, not a false equality.

In `A=D+R+E`, `D` is diagonal and vanishes on `S union T`; `E` has zero diagonal; `R-P` is supported only in rows `T` or columns `S`. Consequently `rank(R)<=3r`, while on the seed complement `L`, `R[L,L]=P[L,L]` and `rank(R[L,L])<=r`. These two different rank bounds are both needed and are correctly kept separate.

### Lines 601-720: spectral-to-volume conversion, random cut, no-pivot estimates, pivot half-potential — PASS

If a volume ratio is below `kappa`, the completion has `||E||_F<=1/16`. Rank perturbation forces at least `r+1` large diagonal entries of `D` in `L`. On those coordinates,

`|R_ii|>=371/400`,

while each off-diagonal entry is `<1/7+1/16`; for `r<=4`, the row sum is `<23/28<371/400`. Strict diagonal dominance therefore makes an `(r+1)x(r+1)` compression of `R[L,L]` invertible, contradicting `rank(R[L,L])<=r`. The arithmetic and direction of every singular-value inequality check out.

A fair physical coordinate cut includes each ordered disjoint `(S,T)` with probability `4^{-k}`, so `E Z_k(A_{I,J})=4^{-k}V_k(A)`. This closes the no-pivot `s_9` half-potential and `s_17` density estimates without rotated independence.

The two singular-kernel inequalities are sufficient for the scalar and indefinite-pair pivot branches. The scalar-pivot Schur complement keeps a genuine spectral direction before the quarter-power/log estimate is invoked.

### Lines 721-790: main case split, scaling, limitations — PASS

The four exhaustive main branches are valid:

1. no pivot + `s_17>=1`: density `<2400`;
2. scalar pivot: Schur complement retains at least sixteen large spectral directions, so the nine-direction full half-potential bound gives `<=6010`;
3. definite pair pivot: density `<=10*pi`;
4. indefinite pair pivot: Schur complement retains at least fifteen large directions; the one-direction logarithmic potential gives `<251`.

The rescaling to arbitrary `K,s` is correct. The manuscript also correctly limits its claim to essential boundedness; only the Fourier no-pivot branch automatically supplies continuity.

## Primary-source prior-art and hypothesis audit

I searched for a source-matching prior theorem rather than treating related anti-concentration results as interchangeable.

- **Rudelson-Vershynin, arXiv:1402.4492.** Theorem 1.1 assumes independent real coordinates with densities bounded by `K` and bounds densities of orthogonal projections; Theorem 1.2 gives the sharp one-dimensional bound `sqrt(2)K` for normalized linear combinations. These hypotheses match the rough product input class, but the results are linear/projection results, not a bounded-density theorem for indefinite quadratic pushforwards.
- **Livshyts-Paouris-Pivovarov, arXiv:1507.07949.** For product densities with each factor bounded by one, every `k`-dimensional marginal is bounded by `2^{k/2}`. This is a sharper linear-marginal theorem than the self-contained `e^{k/2}` lemma in the manuscript, but again it is not a quadratic-form theorem.
- **Bennett-Carbery-Christ-Tao, arXiv:math/0505065.** Their Brascamp-Lieb work includes heat-flow monotonicity methods of the kind used here. The manuscript proves the specialized geometric inequality it actually needs, so this is attribution/prior art rather than a hidden dependency.
- **Carbery-Wright (Math. Res. Lett. 8 (2001), 233-248).** Their polynomial anti-concentration framework is over convex/log-concave settings and does not match the owner's arbitrary rough product-density class without additional assumptions/scales. It does not subsume the present theorem.
- **Herry-Malicet-Poly, arXiv:2303.09488 / PTRF.** Their quadratic-form regularity results concern i.i.d. inputs whose common law has a sufficiently smooth Gaussian-field representation. Those hypotheses are strictly stronger and do not match arbitrary non-i.i.d. cap-`K` densities.

I found **no exact prior published theorem in the primary sources/searches checked** that already states the manuscript's arbitrary-law fixed-multiplicity conclusion. This is a limited prior-art check, not a priority/novelty certificate.

## Repository-package GAP (nonmathematical)

At fresh master `e5f053b3e07a61548323bebca07a5e05687e3bb7`, the fixed-multiplicity root contained `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`. The README/AUDIT also refer to `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json`, but those four files were not present at that root in the observed tree. This does **not** undermine the self-contained symbolic proof, but it means the claimed reproducibility package is incomplete in the repository state audited here. No claim is made that absent finite checks were rerun.

## Lowering multiplicity: mechanism audit

The present architecture does not lower `17` merely by improving constants. In the no-pivot branch, bounded density via the determinant envelope requires crossing order `k=5`, because its exponent is `k/4` and integrability needs `k/4>1`. In the bad-volume-ratio argument the worst seed order is then `r=4`; the global correction has rank at most `3r`, while contradicting the restricted rank `r` requires `r+1` large diagonal coordinates. Thus the current skeleton needs

`m-3r >= r+1`, i.e. `m>=4r+1=17`.

This is a barrier for this proof mechanism, not a theorem that sixteen can never suffice. A genuine `<=16` result needs either a better interpolation/rank mechanism or an analytic endpoint that extracts bounded density from order-four crossing information.

## Post-audit comparison

Only after completing the independent derivation above did I inspect the newly landed fleet03/B16 audit. It independently reports PASS for the same mathematical theorem and flags the same projection-line wording ambiguity plus the same missing-package issue. This agreement is corroboration, not a substitute for either review.

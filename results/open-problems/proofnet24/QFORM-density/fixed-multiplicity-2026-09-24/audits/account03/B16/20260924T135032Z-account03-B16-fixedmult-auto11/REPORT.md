SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T13:50:32Z.
attacking: independently audit the new nine-eigenvalue fixed-multiplicity compiler end-to-end, then test the first s_8 terminal projection-product implication rather than reusing a peer verdict.

# account03/B16 fixed-multiplicity audit auto11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Execution/memory status: **WITHOUT_VERIFIED_BRAIN**.

Pinned baseline source:

- repository: `yspennstate/math-open-problems`
- baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- size: 47,883 bytes / 790 lines.

`SOURCE_MANIFEST.json` confirms that the mathematical source is unchanged. The previously missing support files are now present: `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json`. The package records the finite checker as passing 534 exact interpolation seeds, 18 exact volume comparisons, 240 Schur diagnostics, and 30 graph-weight diagnostics; those checks are diagnostics, not proof.

## Verdict

**PASS for the source-identical 17-eigenvalue baseline in this B16 audit lineage, with the already identified nonfatal product-projection wording repair.**

**PASS for the new nine-eigenvalue candidate theorem after an independent equation-level reconstruction of the new grouped receiver and its compilation with the audited baseline:**

`boxed: s_9(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity < 3078 K^2/s.`

This is an independent worker audit, not a self-awarded formal validation certificate. The unrestricted three-eigenvalue conjecture remains **OPEN**, the general `s_8` theorem remains **OPEN**, and global continuity remains **OPEN/not claimed**. The no-pivot nine-eigenvalue branch does have a `C_0` density.

## A. Baseline dependency closure — source-identical 790-line manuscript

The complete baseline was audited by this slot before the present delta; its source blob is unchanged. I rechecked the exact interfaces used by the new nine-eigenvalue proof rather than accepting a peer PASS as a premise.

### Lines 1–160 — theorem/scaling/Fourier/Riesz: PASS

The theorem keeps arbitrary independent coordinate laws with density cap `K`, arbitrary dimension/signature/remaining spectrum, and arbitrary affine `b,c`. The Fourier normalization and half-Riesz representation are compatible with the manuscript convention. The scaling `Y=KX`, `A -> A/s`, and output factor `s/K^2` gives the final `K^2/s` density scaling.

### Lines 169–217 — singular-value rank perturbation and Schur count: PASS

The rank perturbation statement is in singular values and is therefore valid for nonsymmetric algebraic auxiliaries. A physical scalar Schur complement loses at most one unit-scale spectral direction; a physical pair loses at most two. The singular limiting argument keeps the selected pivot invertible before passage to the limit.

### Lines 221–301 — geometric BL/product projection/scalar Fourier powers: PASS with one local wording GAP

The product-projection theorem is used on literal linear images of product coordinates, never to infer independence after rotation. One sentence remains locally inaccurate after zero-leverage rows are omitted: it writes `sum_i(1-b_i)=d`; the correct retained-row relation is

`sum_{b_i>0}(1-b_i) <= d`.

That inequality is exactly sufficient for `p<=e^(d/2)`, so the theorem and every downstream constant remain valid. Status: **GAP, local wording only / no theorem impact**.

### Lines 310–400 — decoupling and determinant compiler: PASS

Copies are introduced only in original-coordinate banks. Difference coordinates remain independent and cap one. The graph/BL weights and scalar Fourier powers produce the stated determinant exponents; order three is used as a half-potential endpoint in the baseline, while the new grouped receiver below is what upgrades aggregate third crossing volume to an actual density.

### Lines 404–525 — square, definite pair, hyperbolic pair, quarter concentration: PASS

The square profile is conditional measure domination. The definite-pair orthogonal diagonalization is deterministic integration after conditioning, not a rotation of the random input. The indefinite pair logarithmic envelope keeps the moving critical value and is integrated by Tonelli. No refuted pointwise van-der-Corput statement is used.

### Lines 528–645 — ordered minors/interpolation/spectral-to-volume: PASS

For a sampled nonsingular disjoint seed `B=A[S,T]`, the bordered determinant identity gives the sampling inequality. The completion has

`rank R<=3r`, but crucially `rank R[L,L]<=r`, with `D=0` on the seed and `E` zero diagonal. In the spectral-to-volume contradiction, the `r+1` forced heavy diagonal coordinates lie in `L`; strict diagonal dominance therefore contradicts the **restricted** rank, not merely the global rank. This is valid for the nonsymmetric `R` because the diagonal-dominance lemma needs no symmetry.

### Lines 646–790 — pivot half potentials and baseline main proof: PASS

Scalar, definite-pair and indefinite-pair pivots exhaust the manuscript pivot definition. Full versus truncated half potentials are separated correctly: outside `|Q-a|<=1`, `|Q-a|^-1/2<=1`. The final 17-eigenvalue proof uses order-five density in the no-pivot branch and an at-least-nine-eigenvalue Schur child after a scalar pivot. Essential boundedness is the global conclusion; continuity is not silently inferred.

No baseline source region needed by the theorem remains `UNCHECKED` in this run lineage.

## B. Independent audit of the new grouped product-Fourier receiver

Source audited:

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.

### B1. Complex pushforward and Plancherel: PASS

For the promoted `k`-dimensional bank, pushing `e^{itF}dP` to its orthogonal projection gives a complex density `a_t` with `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. With the manuscript Fourier normalization,

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

This is a genuine integrated identity, not a false pointwise oscillatory-decay assertion.

### B2. Difference-bank decoupling: PASS

After smoothing the residual complex pushforward and squaring its `L^2` norm, an independent copy of the original `J` bank produces `D=X_J-X'_J`. Its coordinates are independent and have densities at most one by convolution. Pure same-bank phases cancel or remain modulus one as stated. No rotated-coordinate independence is inserted.

### B3. Weighted-subset Holder/Jacobian: PASS with a notation caveat

For a sampled `ell`-subset `T`, the map

`D -> (M_JD, (<c_i,D>)_{i in T})`

has Gram determinant

`S^2 det(C_T C_T^T)`.

The product-projection lemma therefore contributes

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`.

Weighted Holder uses powers `1/alpha_i`; the scalar Fourier-power lemma applies because the live marginals satisfy `alpha_i<=1/2`. If an inclusion marginal is exactly zero, its factor should simply be omitted from the Holder product rather than literally writing `1/alpha_i`. This is a harmless endpoint-notation repair, not a gap in the estimate.

### B4. Entropy/determinant geometric mean: PASS

For subset weights

`w_T=det(C_T C_T^T)/Z_ell`,

the determinant factors combine exactly to

`Z_ell^(-1/2) exp(H(w)/2)`.

If a random sampled subset is uniformly ordered, entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell - log(ell!)`.

This is the dimension-free step needed to prevent the weighted-subset promotion from paying the number of physical coordinates.

### B5. Promotion to marginal-free order three and order two: PASS

Repeated Gram-Schmidt identities promote any heavy inclusion marginal. At order three all branches end in

`||p_Q||_infinity <= C3 E_3(M)^(-1/6),`

`C3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.

At order two all branches end in the fractional-potential statement

`sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8),`

`C2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

The order-two result is not mislabeled as a density theorem.

## C. Reconstruction of the nine-eigenvalue theorem: PASS

Normalize `K=s=1`, with `eta=1/100`, `kappa=1/80^2`.

### C1. No pivot

The audited spectral-to-volume proposition at `k=3` requires exactly `4k-3=9` large singular/eigenvalue magnitudes. Thus

`V_3(A)>=kappa^3`.

A fair original-coordinate cut supplies a cross block with

`E_3(M)>=4^(-3)kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

The grouped receiver gives

`||p_Q||_infinity <=160 C3
 =2370.9340260548797...<2371`,

and this branch has a continuous `C_0` density.

### C2. Scalar pivot

After completing the square in a literal coordinate with `|a_hh|>=eta`, the Schur complement retains at least eight unit-scale eigenvalues.

If that child has a pivot, the sharpened B13 pivot estimate gives truncated half potential `<306.75`; adding the outside tail costs at most one, so the full half potential is `<307.75`.

If the child has no pivot, it certainly has `s_5>=1`; the baseline order-two spectral-to-volume argument plus the new order-two receiver gives

`C2 sqrt(160)=152.99191115498024...<153`.

The conditional square profile therefore yields in all scalar-pivot subcases

`||p_Q||_infinity < eta^(-1/2) 307.75
 =3077.5<3078`.

### C3. Pair pivots

A definite physical pair with determinant magnitude at least `eta` is paid directly by the two-dimensional polar estimate, `<=10 pi<32`. The sharpened indefinite-pair logarithmic envelope together with the quarter-concentration/log-moment estimate is also below the final `3078` constant. These branches require fewer surviving spectral directions than the scalar branch and do not control the theorem constant.

### C4. Scaling

Returning to density cap `K` and threshold `s`, the normalized variable `Y=KX` and matrix `A/s` give

`boxed: ||p_Q||_infinity <3078 K^2/s.`

No moment, compact-support, connected-support, Gaussian, log-concave, or diagonal-basis hypothesis enters.

**Conclusion for the nine-eigenvalue delta: PASS.**

## D. Threshold eight: exact remaining obstruction, not a theorem

I independently checked the account03/B08 terminal identities used to locate the `9 -> 8` debt. Under no `eta`-pivot, `s_8(A)>=1`, and failure of the order-three volume gate, the only possible failed sampled ratio is `r=2`. The canonical completion has

`||E||_F<=3/80`, `rank R<=6`, `rank R[L,L]<=2`,

`s_2(D)>=77/80`, `s_3(D)<=519/1400`, and

`s_6(R)>=1657/2800`.

For the two heavy coordinates `H subset L`, diagonal dominance gives the exact determinant lower bound

`|det P[H,H]| >=857233/980000`,

and because

`P[H,H]=A[H,T] B^(-1) A[S,H]`,

three disjoint physical two-banks obey

`|det A[H,T]| |det A[S,H]|
 >=(857233/980000)|det A[S,T]|`.

The further two-deletion window theorem correctly implies that every still-unpaid `s_8` state either has density `<64` with `C_0` regularity or carries three nested original-coordinate star norms larger than

`9/(6400 sqrt(2))`.

None of these facts gives an absolute lower bound for one cross two-minor: the seed determinant can still be arbitrarily small. Treating the determinant ratio as an absolute determinant would be invalid. Likewise, the nested stars need not be linearly independent.

Therefore **the general `s_8` theorem is still OPEN**.

## E. New B16 supporting theorem proved in this run

The sibling improvement

`improvements/account03/B16/20260924T135032Z-account03-B16-fixedmult-auto11/PROJECTION_PRODUCT_RECEIVER.md`

proves the dependence-safe receiver

`Q=2(W+alpha(Y)) dot Z(Y)+R(Y),`

where `W` is an orthogonal two-dimensional projection of one original product bank, `Y` is a disjoint original product bank, and `Z(Y)` has joint density cap `M`. Then

`boxed: ||p_Q||_infinity <=2 sqrt(pi M).`

For `Z=L Y` with row Gram `G=LL^T`, the actual two-dimensional projection theorem gives

`boxed: ||p_Q||_infinity <=2 sqrt(2 pi) (det G)^(-1/4).`

This precisely combines projection density with nonlinear inverse-radius integration while retaining dependence. It closes any `s_8` terminal subpacket exposing a uniformly nondegenerate pure-cross two-bank Gram, but the current determinant-ratio certificate does not force that absolute Gram lower bound.

## F. Designated account04/B16 result applied to an actual strict-target inequality

The completed account04/B16 definite-plane theorem gives, for a cap-one two-dimensional product projection with definite quadratic matrix `H`,

`||p_Q||_infinity <=2 pi/sqrt(|det H|)`.

For

`Q_partner=-2R^2+4RZ_1+3Z_1^2+2Z_2^2`,

where `R` is a disjoint cap-one original coordinate and `Z` is an orthogonal two-dimensional projection of another product bank, conditioning on `R` leaves `H=diag(3,2)`. Hence

`boxed: ||p_Q_partner||_infinity <=2pi/sqrt(6)
 =2.565099660323728...`.

The effective three-dimensional matrix

`[[-2,2,0],[2,3,0],[0,0,2]]`

has eigenvalues

`(1-sqrt(41))/2, 2, (1+sqrt(41))/2`,

so all three have modulus at least one. This is an actual target-level application of the designated partner result.

## Final status

- Pinned 17-eigenvalue baseline: **PASS in this B16 audit lineage**, one local nonfatal wording repair.
- Support package presence/reproducibility metadata: **PASS; previously missing files are now present**.
- Nine-eigenvalue candidate with constant `<3078 K^2/s`: **PASS in this independent B16 reconstruction; independent-validation/release gate still separate**.
- New projection-product inverse-radius receiver: **PROVED**.
- General eight-eigenvalue theorem: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuous-density conclusion: **OPEN/not claimed**.

Next proof obligation: construct a three-bank/cycle receiver that consumes the `s_8` determinant ratio before reciprocal local-minor payment, or prove that simultaneous rank-two saturation plus the nested deletion stars force a uniformly nondegenerate projected pure-cross Gram to which the new inverse-radius receiver applies.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T18:21:32Z.
attacking: close the exact-rank-three nested-heavy projection branch by combining the assigned partner determinant-bank geometry with a physical-pair/pivot dichotomy that keeps original-coordinate independence.

# fleet03/B16 — nested-heavy pair/pivot closure

Run: `20260922T182132Z-fleet03-B16-QFORM-r14`  
Assignment: Projection-product interaction.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: `PROVED SUPPORTING THEOREM / EXACT-RANK-THREE NESTED-HEAVY BRANCH CLOSED / FULL QFORM OPEN`.

## 1. Scope and current corrections

The full owner target is still open: for independent real coordinates with densities bounded by one and a real symmetric matrix having at least three eigenvalues of modulus at least one, prove one dimension- and matrix-independent bound on the density of `X^T A X`, or give a counterexample. Continuity is a separate desired conclusion.

This report does **not** use the false arbitrary-joint three-dimensional coarea estimate, the false positive conditional projection-density moment, a pointwise van-der-Corput estimate, independence after rotation, or a receiver-only projection-density bound. It works only in the exact-rank-three nested-heavy branch stated below. Additional spectral components remain a separate debt.

The newer correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` is therefore respected: no step below treats an arbitrary bounded joint three-dimensional density as sufficient for an indefinite quadratic pushforward.

## 2. Inputs read and actually used

### Assigned partner: fleet04/B16

The completed assigned-partner result is

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T161909Z-fleet04-B16-QFORM-r2/REPORT.md`.

For an exact-rank-three frame `A=R Lambda R^T`, `R^T R=I_3`, let `r_k` be the `k`th row. If

`c=||r_i||^2>1/2`, `e=r_i/sqrt(c)`, and `h=||(I-ee^T)r_j||^2>1/2`,

then the two-row Gram determinant is exactly

`G_ij = ||r_i||^2 ||r_j||^2 - <r_i,r_j>^2 = c h > 1/4`,                 (2.1)

and the fixed-pair determinant bank obeys

`P_ij := sum_{k != i,j} |det A_{ {i,j,k} }| = |det Lambda| G_ij > |det Lambda|/4`.  (2.2)

This exact bank lower bound is applied below.

### Previously completed analytic inputs

I use two source-valid completed supporting theorems already present in the current QFORM state.

1. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`: for exact rank three, if physical coordinate `i` has leverage `c_i=||r_i||^2`, `A_ii !=0`, and the three nonzero eigenvalues are the entries of `Lambda`, then

`||p_Q||_infinity <= 128 [c_i |A_ii| |det Lambda|]^(-1/4)`.            (2.3)

The arbitrary affine residual orientation is included; this is not a rotated-coordinate independence claim.

2. `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1` plus its rank-one remainder smoothing: if an original-coordinate physical pair `B` is invertible indefinite, `D=|det B|`, `kappa=sigma_min(B)`, and after pair completion the exact-rank-three Schur remainder is `lambda (u dot Z)^2` with `||u||=1`, then

`||p_Q||_infinity <= 8 sqrt(5) (D kappa |lambda|)^(-1/4)`.             (2.4)

For completeness, the narrow use of (2.4) is re-derived in Section 5 from the logarithmic pair envelope and the rank-one affine small-ball estimate; no arbitrary-joint coarea statement is imported.

## 3. New geometric lemma: a nested-heavy pair cannot be small in operator norm

Let

`H = R_{ {i,j},:} R_{ {i,j},:}^T`

be the `2 x 2` Gram matrix of the two physical spectral rows. By (2.1),

`det H = G_ij > 1/4`.

Every leverage is at most one because `RR^T` is an orthogonal projection, so

`tr H = ||r_i||^2+||r_j||^2 <= 2`.

Therefore

`lambda_min(H) = det(H)/lambda_max(H) >= det(H)/tr(H) > 1/8`.         (3.1)

Put `V=R_{ {i,j},:}` and `W=H^(-1/2)V`. Then `W W^T=I_2`. The physical pair is

`B = V Lambda V^T = H^(1/2) C H^(1/2)`,

where `C=W Lambda W^T` is the compression of `Lambda` to a two-dimensional spectral subspace.

Because all three eigenvalues of `Lambda` have modulus at least one, `||C||_op >=1`. Indeed, in the definite signatures this is immediate. In signature `(2,1)`, Cauchy interlacing gives the larger eigenvalue of `C` at least the second positive eigenvalue of `Lambda`, hence at least one. In signature `(1,2)`, the smaller eigenvalue of `C` is at most the second (negative) eigenvalue of `Lambda`, hence at most `-1`.

Since

`C=H^(-1/2) B H^(-1/2)`,

we have

`1 <= ||C||_op <= lambda_min(H)^(-1) ||B||_op`.

Combining with (3.1),

`boxed( ||B||_op > 1/8 ).`                                           (3.2)

This is the key new bridge from the partner's *spectral-row geometry* to an *original-coordinate physical pair* without rotating the input law.

## 4. Main theorem — `QFORM-NESTED-HEAVY-PAIR-PIVOT-CLOSURE-v1`

Assume `A=R Lambda R^T` has rank exactly three, `R^T R=I_3`, and all three nonzero eigenvalues satisfy `|lambda_s|>=1`. Suppose there are physical rows `i,j` satisfying the nested-heavy conditions in Section 2. Then, for arbitrary independent input coordinates with densities bounded by one,

`boxed( ||p_{X^T A X}||_infinity < 310 ).`                            (4.1)

Essential boundedness is proved. Continuity is **not** proved by this argument.

### Proof

Write the physical pair as

`B = [[a,b],[b,d]]`.

The partner geometry gives both physical leverages above one half:

`||r_i||^2=c>1/2`, and `||r_j||^2 >= h>1/2`.                          (4.2)

Set the exact threshold

`delta=1/17`.

#### Case A: one physical diagonal is not small

If `|a|>=delta`, apply (2.3) at coordinate `i`. Using (4.2) and `|det Lambda|>=1`,

`||p_Q||_infinity`
` <=128[(1/2)(1/17)]^(-1/4)`
` =128 * 34^(1/4)`
` <310`.                                                              (4.3)

If instead `|d|>=delta`, the identical argument applies at coordinate `j`, because `||r_j||^2>1/2`.

#### Case B: both physical diagonals are small

Assume now

`|a|<1/17`, `|d|<1/17`.                                               (4.4)

For a symmetric `2 x 2` matrix,

`||B||_op <= max(|a|+|b|, |d|+|b|) < |b|+1/17`.

Together with (3.2), this yields

`|b| > 1/8-1/17 = 9/136`.                                             (4.5)

Compare `B` with `B_0=[[0,b],[b,0]]`. Since the diagonal perturbation has operator norm `<1/17`, Weyl's singular-value inequality gives

`kappa:=sigma_min(B) >= |b|-1/17 > 9/136-8/136 = 1/136`.              (4.6)

Moreover

`det B = ad-b^2 < (1/17)^2-(9/136)^2 <0`,                             (4.7)

so `B` is automatically invertible and indefinite.

Because the full matrix has exact rank three and this pair has rank two, its Schur complement is rank one:

`S=lambda u u^T`, `||u||=1`.

For every `k` outside the pair, the block determinant formula gives

`det A_{ {i,j,k} } = det(B) S_kk = det(B) lambda u_k^2`.

Hence

`D |lambda| = sum_{k != i,j}|det A_{ {i,j,k} }| = P_ij`,              (4.8)

where `D=|det B|`. Applying the partner bank lower bound (2.2),

`D |lambda| = P_ij > 1/4`.                                            (4.9)

Now (2.4), (4.6), and (4.9) give

`||p_Q||_infinity`
` <=8 sqrt(5) (P_ij kappa)^(-1/4)`
` <8 sqrt(5) (1/544)^(-1/4)`
` =8 sqrt(5) 544^(1/4)`
` <87`.                                                               (4.10)

Thus Case B is substantially cheaper than Case A. Combining (4.3) and (4.10) proves (4.1). QED.

## 5. Narrow verification of the pair-log input used in Case B

I rechecked the precise step needed for (2.4). Conditional on every coordinate outside the physical pair, completing the pair leaves

`Q = ((U,V)+m(Z))^T B ((U,V)+m(Z)) + R(Z)`,

where `U,V` remain the two original independent cap-one coordinates. For every gradient cutoff `r>0`, the completed pair has the source-proved conditional density envelope

`p_pair(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2r^2/(kappa |t|))`.         (5.1)

In exact rank three, `R=lambda (u dot Z)^2 + affine` and the completed rank-one affine small-ball theorem gives

`sup_t P(|R-t|<rho) <= H sqrt(rho)`, `H=10/sqrt(|lambda|)`.            (5.2)

Layer cake applied to the logarithm in (5.1) gives

`E log_+(A/|t-R|) <=2H sqrt(A)`.

Substituting `A=2r^2/kappa` gives

`p_Q(t) <= 2sqrt(2)/r + 2sqrt(2) H r / sqrt(D kappa)`.

Optimizing at `r^2=sqrt(D kappa)/H` yields

`||p_Q||_infinity <=4 sqrt(2H)(D kappa)^(-1/4)`
` =8 sqrt(5)(D kappa |lambda|)^(-1/4)`,

which is (2.4). The shifts `m(Z)` may depend arbitrarily on the remainder; the critical value after completing the pair is exactly the scalar remainder being averaged. No conditional density cap on a rotated coordinate is asserted.

## 6. What is newly closed, and what remains

The assigned partner's previous r2 handoff left the nested-heavy diffuse determinant-bank regime unpaid unless one large zero-diagonal atom existed. The theorem above removes that atom requirement entirely: **every exact-rank-three nested-heavy configuration is now controlled**, irrespective of whether the normalized determinant bank is concentrated or diffuse and irrespective of whether either physical diagonal vanishes.

The result is not a full solution. It does not cover:

1. exact-rank-three frames outside the nested-heavy branch;
2. arbitrary matrices with additional spectral components;
3. the full continuity conclusion.

The next target-relevant implication is therefore a complete heavy/light frame dichotomy: combine this nested-heavy closure with the already available diffuse rank-two / outer-pivot mechanisms so that every exact-rank-three frame is covered without invoking the refuted arbitrary-joint coarea lemma, and then make the resulting argument stable under arbitrary additional spectrum.

## 7. Constant checks

All numerical displays are consequences of exact rational inequalities. The only rounded claims are

`128*34^(1/4) = 309.086259554... <310`,

`8*sqrt(5)*544^(1/4) = 86.392235909... <87`.

A companion checker in this run folder evaluates these constants and the exact determinant-sign threshold. The proof itself does not rely on Monte Carlo or floating-point certification.

## 8. Status

New claim: `QFORM-NESTED-HEAVY-PAIR-PIVOT-CLOSURE-v1` — **PROVED as a supporting exact-rank-three theorem, conditional only on the explicitly source-cited completed analytic inputs re-used above; the specific pair-log implication was re-derived in Section 5.**

Full QFORM conjecture: **OPEN / NOT PROVED**.  
Continuous density: **NOT PROVED by this run**.

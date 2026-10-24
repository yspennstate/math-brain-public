SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-22T22:39:00Z.
attacking: projection-product interaction via a Pluecker/disjoint-basis random-cut identity, followed by exact product-bank compression in the zero-disjointness endpoint.

# account01/B16 — Pluecker disjointness converts exact rank three into a product-preserving cross cut

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Projection-product interaction  
**Run:** `20260922T223900Z-qform-b16-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
**Continuity:** separately open globally; proved in the quantitative cross-cut branch below.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The full target remains open: for independent real coordinates with one-dimensional densities at most one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a dimension-free essential density bound for `X^T A X`.

This report proves a new exact-rank-three structural reduction. It does **not** delete additional spectral components, infer independence after rotation, use arbitrary-joint coarea, use positive conditional projection-density moments, or use law-uniform pointwise oscillatory decay.

Fresh control at invocation start was `yspennstate/math-research-brain@e9f17284db38497e3b51665a72590dce58af04f1`, OWNER CONTROL revision `2026-09-22.15`; the correction closure was refreshed through `yspennstate/math-research-brain@1a8c2a1c4c817529b96723313bd235ae65beac4c`. In particular this run preserves the fresh `QFORM-NONZERO-MUTUAL-EDGE-TWO-SLOPE-INSUFFICIENT-v1` and `QFORM-ONESTAR-ARBITRARY-SELF-HALFRIESZ-FALSE-v1` corrections: neither a nearly-zero physical edge nor a one-star half-Riesz estimate can be promoted without spending a genuine third product/spectral resource.

The completed analytic inputs actually used are:

1. **Own cross-bank theorem**, `QFORM-CROSSBANK-L2-FOURIER-v1`, canonical report `yspennstate/math-open-problems@46359b2c27090d3f268f080ddb14c5ef34aa6176:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/qform-b16-20260922T213856Z-r11/REPORT.md`. For a disjoint original-coordinate cut `I,J`, writing `R=H_I(X_I)+H_J(X_J)+2 X_I^T C X_J`, if `rank C=3` and `Delta_3(C)` is the product of its three nonzero singular values, then `||p_R||_infinity <= 6 Delta_3(C)^(-1/3)`, with a continuous density.

2. **Designated partner account02/B16**, run `20260922T220011Z-account02-B16-QFORM-auto11`, canonical report `yspennstate/math-open-problems@b9e19e2c19ecd6f6ede282cd3c73ad014c449e9f:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T220011Z-account02-B16-QFORM-auto11/REPORT.md`. Its `QFORM-FINITE-LINE-BANK-COMPRESSION-v1` says that for exact rank three `A=R Lambda R^T`, if all nonzero physical rows of `R` occupy `K` spectral line directions, then `||p_Q||_infinity <= 2 C_3 |det Lambda|^(-1/3) binom(K,3)^(1/3)`, where `C_3=16 sqrt(30) 2^(1/4)=104.21688998922089...`. This result is applied below to the exact zero-disjointness endpoint after a matroid structural reduction; it is not merely cited.

I also use the completed exact-rank-three physical-pivot consequence from `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`: for a full exact-rank-three target and any nonzero physical diagonal pivot, `||p_Q||_infinity <= 128/sqrt(|A_ii|)`.

## 2. Pluecker probability law

Assume the **entire** matrix has exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,                                      (2.1)

where `Lambda` is real symmetric invertible and `|lambda_j|>=1` for `j=1,2,3`. For each three-element physical set `S`, let

`w_S=det(R_S)^2`.                                                     (2.2)

Cauchy--Binet gives `sum_S w_S=det(R^T R)=1`, so `w` is a probability law on triples. Let `S,T` be independent triples from `w` and put

`d=P(S cap T=emptyset)=sum_(S cap T=emptyset) w_S w_T`.              (2.3)

## 3. Main theorem — `QFORM-PLUCKER-DISJOINT-CUT-v1`

There exists an original-coordinate bipartition `I union J=[n]` such that

`Delta_3(A_[I,J]) >= |det Lambda| sqrt(d)/8`.                         (3.1)

Consequently, for `d>0`,

`boxed: ||p_(X^T A X)||_infinity
        <=12 |det Lambda|^(-1/3)d^(-1/6)
        <=12 d^(-1/6).`                                              (3.2)

The density in this branch has a continuous representative.

### Proof

Assign each physical coordinate independently to `I` or `J` with probability `1/2`, and put `C=A_[I,J]`. Since `rank A=3`, `rank C<=3`. For `S subset I`, `T subset J`, `|S|=|T|=3`,

`det C_[S,T]=det(R_S) det(Lambda) det(R_T)`,                          (3.3)

hence `det C_[S,T]^2=|det Lambda|^2 w_S w_T`. For a rank-at-most-three matrix the sum of squared `3 x 3` minors equals the squared product `Delta_3(C)^2` of the three nonzero singular values (and is zero at rank below three). Therefore

`Delta_3(C)^2=sum_(S subset I,T subset J) det C_[S,T]^2`.             (3.4)

A fixed ordered pair `(S,T)` occurs with `S subset I,T subset J` iff it is disjoint, and then with probability `2^(-6)=1/64`. Thus

`E_(I,J) Delta_3(A_[I,J])^2=|det Lambda|^2 d/64`.                    (3.5)

Some cut satisfies (3.1). For that cut the full form is exactly

`X_I^T A_[I,I]X_I+X_J^T A_[J,J]X_J+2X_I^T A_[I,J]X_J`.              (3.6)

The banks `X_I,X_J` are genuinely independent original-coordinate sources; the within-bank quadratic terms are arbitrary phases covered by `QFORM-CROSSBANK-L2-FOURIER-v1`. Applying it gives

`||p_Q||_infinity <=6[|det Lambda|sqrt(d)/8]^(-1/3)
                    =12|det Lambda|^(-1/3)d^(-1/6)`.                 (3.7)

Since `|det Lambda|>=1`, (3.2) follows, together with continuity from the same Fourier theorem. QED.

If `d>=1/2`, this gives the explicit bound

`boxed: ||p_Q||_infinity <=12*2^(1/6)=13.469544579712476... .`       (3.8)

## 4. Complementary heavy-row consequence

Write `ell_i=||r_i||_2^2`. The Pluecker law has exact one-point marginals

`P(i in S)=ell_i`.                                                    (4.1)

Indeed, differentiate `det(R^T diag(z)R)=sum_S w_S prod_(j in S)z_j` at `z=1`: the polynomial derivative is the left side of (4.1), while the matrix derivative is `tr(r_i r_i^T)=ell_i`.

Since `S,T` are independent,

`1-d=P(S cap T !=emptyset)
    <=sum_i P(i in S,i in T)=sum_i ell_i^2`.                         (4.2)

Also `sum_i ell_i=3`, so

`boxed: max_i ell_i >=(1-d)/3.`                                      (4.3)

Thus if `d<1/2`, some physical coordinate has leverage `ell_i>1/6`. If its diagonal satisfies `|A_ii|>=eta`, the completed exact-rank-three pivot theorem gives

`||p_Q||_infinity <=128 eta^(-1/2)`.                                 (4.4)

Taking `eta=1/96`, this is `<=128 sqrt(96)=1254.138748304987...`.

If instead `d<1/2` and `|A_ii|<1/96`, then `A^2=R Lambda^2 R^T` gives

`sum_j A_ij^2=r_i^T Lambda^2 r_i>=ell_i`,                            (4.5)

hence

`boxed: ||A_[i,-i]||_2>sqrt(1/6-1/96^2)
        =0.40811537550332777... .`                                   (4.6)

So the unpaid branch is a high-leverage **near-null star**, not a generic diffuse frame. The fresh one-star correction prevents paying this branch with an arbitrary-self rank-one half-Riesz shortcut. If `Lambda` is definite, however, `|A_ii|=|r_i^T Lambda r_i|>=ell_i>1/6`, so this near-null endpoint is intrinsically indefinite.

## 5. Exact `d=0` endpoint and actual use of account02/B16

The triples with `w_S>0` are the bases of the rank-three vector matroid of the physical rows. If `d=0`, there are no two disjoint bases. The classical Edmonds base-packing criterion says a rank-three matroid has two disjoint bases iff

`|E\X|>=2(3-rank(X))`                                                (5.1)

for every `X`. Hence some `X` violates (5.1).

If `rank(X)=0`, at most five nonzero rows lie outside `X`; hence all nonzero rows occupy at most `K=5` spectral lines. Applying the **completed designated partner account02/B16 theorem** gives the actual inequality

`boxed: ||p_Q||_infinity
 <=2 C_3 binom(5,3)^(1/3)
 =449.0569661600281... .`                                            (5.2)

If `rank(X)=1`, the rows in `X` lie on one spectral line and at most three rows lie outside it. Treating the exceptional rows as singleton line banks gives `K<=4`, so the partner theorem yields

`boxed: ||p_Q||_infinity
 <=2 C_3 binom(4,3)^(1/3)
 =330.8680016034867... .`                                            (5.3)

This is an inequality-level application of the named partner result, after the disjoint-basis structure identifies the product-bank geometry.

If `rank(X)=2`, at most one nonzero row lies outside the plane `span(X)`. Total rank three forces exactly one such row `e`. Every basis contains `e`, so (4.1) gives `ell_e=1`: `e` is a coloop and all remaining spectral rows lie in its orthogonal plane. A non-negligible `A_ee` is paid by (4.4); the hard endpoint is a null/near-null coloop coupled to a rank-two spectral plane.

For the standard family `(J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`, every basis uses one coordinate from each of three line banks, so `d=0` but the partner theorem has `K=3` and gives

`||p_Q||_infinity <=2C_3=208.43377997844178...`,                     (5.4)

while uncompressed reciprocal physical-minor averaging diverges with `m`.

## 6. Remaining full-target debt

The theorem above is exact only when the **entire** matrix has rank three. For a general target with additional spectral components, selecting three large eigenvectors gives a rank-three component `A_0`, but the complementary matrix contributes a cross block on the same physical coordinates and may alter or cancel the cross singular structure. It is neither independent noise nor a block-separable perturbation; deleting or convolving it away would violate the live corrections.

Even at exact rank three, the rank-two-matroid endpoint above leaves a null/near-null coloop plus rank-two plane. The fresh rank-two and one-star corrections explain why a perturbative two-slope or arbitrary-self half-Riesz shortcut is invalid.

The first unpaid implication is therefore `QFORM-PLUCKER-CUT-WITH-RESIDUAL-OR-NULL-COLOOP-v1`: either retain an arbitrary complementary spectral component inside the disjoint-Pluecker cut argument, or prove a dependence-safe bound for the exact null/near-null coloop plus rank-two plane using a genuine third product-preserving resource.

## 7. Status

`QFORM-PLUCKER-DISJOINT-CUT-v1`: **PROVED** for the exact-rank-three full matrix.  
`QFORM-PLUCKER-HEAVY-ROW-DICHOTOMY-v1`: **PROVED**.  
`d=0`, matroid ranks 0 and 1: **PAID** by an actual account02/B16 finite-line-bank inequality.  
`d=0`, matroid rank 2: **REDUCED** to a leverage-one null/near-null coloop plus rank-two plane, not solved.  
Full arbitrary-rank QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**; continuity is established in the `d>0` cross-cut branch only.

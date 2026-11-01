SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B20, 2026-09-22T20:01:20Z.
attacking: dimension-free gluing of the partner's uniform-near-rank-one Schur survivor around the strong physical packet exported by the coherent triangle.

# fleet02/B20 QFORM r18 — strong-hub gluing inside the cutwise near-rank-one survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control:** owner revision `2026-09-22.15`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / DIMENSION-FREE HUB-GLUING / FULL_TARGET_OPEN`.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** no new continuity claim.

## 1. Exact target and correction boundary

The target remains: for every dimension, every product input with independent real coordinates and marginal densities at most one, and every real symmetric matrix `A` with `s_3(A)>=1`, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid counterexample.

This run uses only original-coordinate algebra and exact Schur complements. It does **not** use law-uniform pointwise oscillatory decay, an unrestricted fiber supremum, independence after rotating the product source, a generic conditional-density cap, arbitrary-joint rank-three coarea, a one-good-minor reduction, or absorption of arbitrary same-bank curvature into a linear marginal cap.

## 2. Fresh designated-partner result consumed exactly

The newest compatible completed designated-partner run available at the source snapshot is

- `fleet03/B20`, run `20260922T194915Z-fleet03-B20-QFORM-r16`;
- canonical report `yspennstate/math-open-problems@241e781422352daf5ca803898f1e2d20f4dfda8e`.

In the retained physical-pivot setup `|a|>=m:=3501/8000`, with exact physical Schur complement `S`, fleet01/B20 has already paid every residual original-coordinate cut `C=S[L,R]` having `s_2(C)>=beta:=1/64`. The partner then proves that a still-unpaid survivor satisfies, for **every** residual physical cut,

`dist_F(C,{rank<=1}) < delta := sqrt(10)/64`,                  (2.1)

unless a ridge cut has effective dimension at least five, in which case the full ambient density is `<800`.

The exact expression (2.1), including its numerical value

`delta = sqrt(10)/64 = 0.04941058844...`,                    (2.2)

is the quantitative input used below. The partner also proves approximate tetrad constraints and, on fleet04/B20's validated selected-row overlap only, the row gate `||c||_2<=max{|d|,1/36}`. I do not extend that row gate outside its validated overlap.

## 3. Prior B20 externalization input and the pivot/Schur interface

The previous B20 theorem `QFORM-COHERENT-TRIANGLE-EXTERNALIZATION-v1`, canonical report `yspennstate/math-open-problems@23f3d87a9e93f573c201efee403e45ce6c54098a`, shows that an unpaid compact coherent physical triangle `T={i,j,k}` either is already paid, exports an outside two-direction packet, or has

`||A[T,O]||_op > 1/2`,                                      (3.1)

where `O=[n]\T`.

Take the compact-cell pivot `i`, write

`a=A_ii`, `x=A_ij`, `y=A_ik`,
`r_i=A[i,O]`, `r_j=A[j,O]`, `r_k=A[k,O]`,                    (3.2)

and let `S` be the exact Schur complement after pivoting on `a`. Then

`s_j:=S[j,O]=r_j-(x/a)r_i`,
`s_k:=S[k,O]=r_k-(y/a)r_i`.                                  (3.3)

Because `a` is the largest of the three positive compact-cell diagonals and the normalized pair ratios are `<3/2`,

`|x/a|<sqrt(3/2)`, `|y/a|<sqrt(3/2)`.                        (3.4)

Hence, with `v=(1,x/a,y/a)`, `||v||_2<2`, and

`A[T,O] = v r_i + [0;s_j;s_k]`.                              (3.5)

Therefore (3.1) implies the source-coordinate dichotomy

`||r_i||_2 > 1/8`                                            (3.6)

or

`max{||s_j||_2,||s_k||_2} > eta := 1/(4 sqrt(2))`.            (3.7)

Indeed, if `||r_i||<=1/8` and both residual rows have norm at most `1/(4sqrt2)`, then (3.5) gives

`||A[T,O]||_op <= 2(1/8)+sqrt(2)(1/(4sqrt2)) <=1/2`,

contrary to (3.1).

Thus a cross packet that survives externalization either is already a **physical pivot star** of norm `>1/8`, or it produces a genuinely strong hub row in the same residual physical Schur matrix to which the partner's all-cut theorem applies.

## 4. New theorem — `QFORM-STRONG-HUB-CUT-GLUING-v1`

### Theorem

Let `S` be a real symmetric matrix on residual physical coordinates, let `p` be one residual physical coordinate, let `O` be a disjoint set of residual physical coordinates, and put

`c=S[p,O]`, `R=||c||_2`.

Assume

`R > eta := 1/(4 sqrt(2))`,                                  (4.1)

and assume every residual physical cut of `S` satisfies (2.1). Then one of the following holds.

**H (heavy Schur edge).** There exists `z in O` such that

`|S_pz| > 1/8`.                                               (4.2)

**B (balanced aligned banks).** There is a partition `O=U disjoint_union V` into two nonempty original-coordinate banks such that

`||c_U||_2 > 1/(8 sqrt(2))`,
`||c_V||_2 > 1/(8 sqrt(2))`,                                 (4.3)

and there are unit vectors `q_U in R^U`, `q_V in R^V` and a scalar `lambda` with

`sin angle(q_U,c_U) < sqrt(5)/4`,
`sin angle(q_V,c_V) < sqrt(5)/4`,                            (4.4)

and

`||S[U,V]-lambda q_U q_V^T||_F < sqrt(10)/32`.               (4.5)

The unit vectors in (4.4)-(4.5) are **only algebraic descriptions of the matrix packet**. No change of random coordinates is made and no independence after rotation is asserted.

### Proof

Write `w_z=c_z^2`, so `sum_O w_z=R^2`.

If some `w_z>R^2/2`, then

`|S_pz|>R/sqrt(2)>eta/sqrt(2)=1/8`,

which is H.

Otherwise every `w_z<=R^2/2`. Greedily add coordinates to `U` until its weight first reaches `R^2/4`. Before the last coordinate the weight is `<R^2/4`; the last contributes at most `R^2/2`. Hence

`R^2/4 <= ||c_U||_2^2 <= 3R^2/4`,

so for `V=O\U`,

`||c_V||_2^2 >= R^2/4`.                                      (4.6)

Thus both banks are nonempty and (4.3) follows from `R>eta`.

Let `q` denote any remaining residual physical coordinates not in `{p} union O`; assign them to the `p,U` side. Apply (2.1) to the full physical cut whose sides contain `{p} union U` and `V`. Restrict a rank-one approximant for that cut to the row `p` and columns `V`. It follows that the distance from `c_V` to a one-dimensional subspace is `<delta`. Since `||c_V||>=R/2>delta`, this subspace is nonzero; choose its unit direction `q_V`. Then

`sin angle(q_V,c_V) < delta/||c_V|| <= 2delta/R.              (4.7)

The same cut, restricted to rows `U` and columns `V`, also gives a row vector `a_U` such that

`||S[U,V]-a_U q_V^T||_F<delta`.                              (4.8)

Now apply (2.1) to the full physical cut with `U` on one side and `{p} union V` on the other, assigning all remaining coordinates to the `{p},V` side. Restricting to rows `U` and column `p` gives a unit direction `q_U` satisfying

`sin angle(q_U,c_U) < delta/||c_U|| <=2delta/R,               (4.9)

and restricting to `U x V` gives a row vector `b_V` with

`||S[U,V]-q_U b_V^T||_F<delta`.                              (4.10)

Put `M=S[U,V]`, `P_U=q_Uq_U^T`, `P_V=q_Vq_V^T`. Equations (4.8) and (4.10) imply

`||(I-P_U)M||_F<delta`,
`||M(I-P_V)||_F<delta`.                                      (4.11)

Therefore

`M-P_UMP_V=(I-P_U)M+P_UM(I-P_V)`

and hence

`||M-P_UMP_V||_F<2delta=sqrt(10)/32`.                        (4.12)

Since `P_UMP_V=lambda q_Uq_V^T` for a scalar `lambda`, this is (4.5). Finally

`2delta/R < 2delta/eta
 =8sqrt(2)*(sqrt(10)/64)
 =sqrt(5)/4`,                                                (4.13)

which proves (4.4). QED.

## 5. Combined external-packet corollary

Combining Section 3 with the theorem gives a three-way dimension-free structural conclusion for the still-unpaid coherent/externalized cross branch:

1. **pivot star:** `||A[i,O]||_2>1/8`; or
2. **heavy residual edge:** `|S_pz|>1/8` for physical residual coordinates `p,z`; or
3. **balanced aligned banks:** two disjoint original-coordinate banks `U,V` satisfy (4.3)-(4.5).

In case 2, the heavy Schur coefficient is an actual physical pivot minor:

`a S_pz = a A_pz-A_pi A_iz`,                                (5.1)

so

`|a A_pz-A_pi A_iz| > a/8 >= m/8 = 3501/64000`.              (5.2)

In case 3, the hub-bank Schur norms likewise encode aggregate source-coordinate pivot-minor mass; for example

`||(aA[p,U]-A_pi A[i,U])||_2
 =a||c_U||_2
 > m/(8sqrt(2)).`                                            (5.3)

Thus the gluing theorem does not manufacture a rotated source. It converts the partner's cutwise near-rank-one information into either a physical star, a quantitatively nonzero physical pivot minor, or two source-coordinate banks whose inter-bank Schur block is uniformly close to one aligned rank-one packet.

## 6. Exact zero-error endpoint, explaining the mechanism

There is a clean exact analogue. Suppose every physical cut of a symmetric matrix has rank at most one, and fix a hub `p` with `c_i=S_pi`. Let `H={i:c_i!=0}`. If `|H|>=3`, then there is a scalar `kappa` such that

`S_ij=kappa c_i c_j` for all distinct `i,j in H`,             (6.1)

and every off-diagonal coefficient having at least one endpoint outside `H` vanishes.

For distinct `i,j,k in H`, the `2x2` cut minor on rows `{p,i}` and columns `{j,k}` gives

`c_j S_ik-c_k S_ij=0`.                                      (6.2)

Thus for fixed `i`, `S_ij/c_j` is independent of `j`; symmetry makes the proportionality constant itself proportional to `c_i`, yielding (6.1). If `z notin H`, a cut minor with columns `{j,z}` forces `S_iz=0`; another cut minor with one support coordinate then forces `S_zw=0` for `z,w notin H`.

So exact all-cut rank one globally glues to a grouped/star rank-one off-diagonal endpoint. The new theorem is the dimension-free noisy version around a quantitatively strong hub; it avoids summing per-coordinate tetrad errors and therefore avoids dimension loss.

## 7. Strongest conditional end-to-end assembly and the first unpaid implication

For the coherent/externalized P1 route, the current source-pinned assembly is now:

- the physical-pair/triple payments pay the noncompact coherent triangle;
- B20 r17 makes every analytically unpaid compact coherent triangle export global spectral mass to original coordinates;
- fleet01/B20 plus partner fleet03/B20 r16 pay any residual cut with `s_2>=1/64` or ridge effective dimension at least five, leaving only the uniform cutwise near-rank-one survivor (2.1);
- the theorem above turns the external cross packet inside that survivor into the explicit pivot-star / heavy-Schur-edge / balanced-aligned-bank trichotomy, with no dimension-dependent gluing loss.

The first unpaid universal implication is therefore no longer generic cutwise gluing. It is

`QFORM-HUB-EDGE-OR-ALIGNED-BANK-PAYMENT-v1`:

> Under the full target product-source hypotheses and the retained physical-pivot reduction, prove a universal essential density bound whenever either (i) the physical pivot has an outside star of Euclidean norm `>1/8`, (ii) one physical Schur coefficient has modulus `>1/8`, or (iii) two disjoint original-coordinate banks satisfy (4.3)-(4.5), with arbitrary self blocks and all other couplings retained; alternatively reduce each case to an already-paid ridge/grouped-square/indefinite-pair packet by a source-preserving argument.

The natural next mechanism is aggregate-before-inversion: treat the star/bank as a physical-coordinate aggregate, use the aligned rank-one description only to identify the packet, and spend a second independent bank or a same-sign grouped square before any reciprocal minor estimate. A bare second Cauchy-Schwarz step is not enough, and the vectors `q_U,q_V` must not be promoted to independent random coordinates.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No full-target continuity claim is made.

## 8. Quantitative regression values

`m=3501/8000=0.437625`,
`delta=sqrt(10)/64=0.04941058844...`,
`eta=1/(4sqrt(2))=0.1767766953...`,
`eta/sqrt(2)=1/8`,
`eta/2=1/(8sqrt(2))=0.08838834765...`,
`2delta=sqrt(10)/32=0.09882117688...`,
`2delta/eta=sqrt(5)/4=0.5590169944...`,
`m/(8sqrt(2))=0.03868095064...`.

These numerical values only check the displayed constants; the proof above is analytic.

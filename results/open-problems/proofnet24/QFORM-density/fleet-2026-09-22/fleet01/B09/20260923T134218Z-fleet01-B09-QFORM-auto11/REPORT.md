SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T13:42:18Z.
attacking: elevate an aggregate-heavy physical row through an exact physical square, preserve the anchored third-volume under the Schur shear, and either pay by a two-volume half-Riesz estimate or localize the obstruction to a two-row collar.

# Pivoted heavy third-volume -> rank-two half-Riesz or a two-row collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T134218Z-fleet01-B09-QFORM-auto11`  
Assignment: fleet01/B09, Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. The result below advances the heavy-row survivor from my preceding aggregate singleton-volume compiler. It uses only original-coordinate partitions, exact Schur identities, and the completed fractional two-volume half-Riesz theorem. It does not rotate the random variables, does not use law-uniform pointwise quadratic stationary phase, and does not convert an `O(sqrt(epsilon))` small-ball estimate into a linear one.

## 1. Fresh source state and completed inputs


The exact target remains: independent real original coordinates `X_i` with densities at most one; real symmetric `A`; at least three eigenvalues of `A` have modulus at least one; prove one universal essential density bound or give a valid counterexample. Full-target continuity is tracked separately.

The completed analytic input used below is fleet03/B01's `QFORM-FRACTIONAL-VOLUME-COMPILER` / critical two-volume half-Riesz endpoint, source

`yspennstate/math-open-problems@edb2b0b98a27c56440959e9a13a9eebaa4dfc6f3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T013054Z-auto11/REPORT.md`.

For disjoint original-coordinate banks and arbitrary same-side measurable phases, let `M` be the physical cross block,

`Z_2=e_2(M^T M)=sum_(|S|=|T|=2) det(M[S,T])^2>0`,

and let `alpha_j` be the row inclusion marginals of the squared `2x2` minor law. If `h=max_j alpha_j<1`, set `q=max(1,2h)<2`. The source proves

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] Z_2^(-1/8)`.                 (1.1)

If `h<=3/4`, the coefficient is `<16.856`. Completing one genuine original-coordinate square `a(X_i+eta)^2` then gives directly

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.                (1.2)

This proves essential boundedness and the identical `O(|J|)` interval estimate. It does not, by itself, prove a continuous representative for the final square-peel output.

My immediately preceding B09 compiler is

`QFORM-AGGREGATE-SINGLETON-VOLUME-TO-CUT-v1`,
`yspennstate/math-open-problems@cb81bf5d552509918b2763d264e290e2de5ad284`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/20260923T124408Z-fleet01-B09-QFORM-auto11-r2/REPORT.md`.

It turns aggregate singleton third-volume `S` into one fixed physical cut. At the concrete cutoff `h_0=2/3`, either that cut is paid directly, or one literal row `i` of the fixed cut has anchored selected third-volume `N_i>S/24`. The global candidate set has fewer than 72 rows. The new theorem below continues exactly that second branch.

## 2. Setup and exact Schur shear

Partition the ORIGINAL coordinates into four disjoint banks

`{i} union U union V union W`.

Condition only the outside bank `W`; this may create arbitrary affine terms but preserves independence of the remaining original coordinates. Write the physical cross block from `{i} union U` to `V` as

`B = [ b ; B_0 ]`,                                              (2.1)

where `b=A[i,V]` is a row vector and `B_0=A[U,V]`. Let

`a=A_ii !=0`, `u=A[U,i]`.                                      (2.2)

All blocks `A[U,U]`, `A[V,V]`, and all conditioned affine terms are arbitrary.

Completing the genuine physical `X_i` square is exact:

`Q = a ( X_i + eta(X_U,X_V) )^2 + R(X_U,X_V)`,                (2.3)

and the physical `U x V` cross block of the Schur remainder `R` is

`C = B_0 - (u b)/a`.                                           (2.4)

The rank-one row shear in (2.4) is the only matrix change relevant below.

## 3. Anchored third-volume is invariant under the Schur shear

Define the squared third-volume anchored at physical row `i` by

`V_i(B)
 = sum_(J subset U, |J|=2) sum_(T subset V, |T|=3)
     det B[{i} union J,T]^2`.                                  (3.1)

Assume `V_i(B)>0`; then necessarily `b!=0`. Let `P_b` be the orthogonal projection in the physical column space `R^V` onto `b^perp`.

### Lemma 3.1 — exact anchored-volume identity

For `C` from (2.4),

`boxed: V_i(B) = ||b||_2^2 Z_2(C P_b)`,                       (3.2)

where

`Z_2(M)=e_2(M^T M)=sum_(|S|=|T|=2)det(M[S,T])^2`.            (3.3)

Consequently

`boxed: Z_2(C) >= V_i(B)/||b||_2^2`.                          (3.4)

### Proof

For two physical rows `j,k in U`, subtracting a scalar multiple of the first row from either of the other rows does not alter a determinant containing the first row. Hence for every physical three-column set `T`,

`det [b; C_j; C_k]_T = det [b; (B_0)_j; (B_0)_k]_T`.          (3.5)

Equivalently in exterior algebra,

`b wedge C_j wedge C_k = b wedge (B_0)_j wedge (B_0)_k`.      (3.6)

Since wedging with `b` kills the components parallel to `b`,

`||b wedge C_j wedge C_k||^2
 = ||b||^2 ||(C_j P_b) wedge (C_k P_b)||^2`.                   (3.7)

Summing (3.7) over `j<k` and using Cauchy--Binet on both sides gives (3.2). Finally `C P_b C^T <= C C^T` in Loewner order. Therefore every ordered eigenvalue of `C P_b C^T` is no larger than the corresponding eigenvalue of `C C^T`; the second elementary symmetric polynomial is increasing coordinatewise on the nonnegative orthant. Hence `Z_2(CP_b)<=Z_2(C)`, proving (3.4). QED.

The important feature is that the potentially large and completely arbitrary source-side coupling `u=A[U,i]` disappears from the lower bound: the Schur shear changes each row by a multiple of `b`, while the anchored exterior volume only sees directions transverse to `b`.

## 4. Main theorem — payment or a two-row collar

For each physical row `j in U`, define its participation in the full squared two-volume of the Schur cross `C` by

`T_j(C)
 = sum_(k in U, k!=j) sum_(S subset V, |S|=2, count each pair once)
     det C[{j,k},S]^2`.                                       (4.1)

Normalize

`alpha_j=T_j(C)/Z_2(C)`,                                      (4.2)

so

`sum_j alpha_j=2`.                                            (4.3)

Let `h=max_j alpha_j`.

### Theorem 4.1 — `QFORM-PIVOTED-HEAVY3VOLUME-TO-2ROW-COLLAR-v1`

In the setup above:

1. If `h<1`, put `q=max(1,2h)<2`. Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)]
    |a|^(-1/2) ||b||^(1/4) V_i(B)^(-1/8).
`                                                                 (4.4)

The same coefficient gives, for every interval `J`,

`P{Q in J} <= RHS_coefficient * |J|`.                         (4.5)

2. In particular, if `h<=3/4`,

`boxed:
 ||p_Q||_infinity
 <16.856 |a|^(-1/2) ||b||^(1/4) V_i(B)^(-1/8).
`                                                                 (4.6)

3. If `h>3/4`, then there is a literal original-coordinate row `j in U` satisfying

`boxed:
 T_j(C) > (3/4) Z_2(C)
       >= (3/4) V_i(B)/||b||^2.
`                                                                 (4.7)

Moreover at most two physical rows can satisfy `alpha_j>3/4`. Thus failure of the diffuse two-volume payment localizes the remaining obstruction to a physical collar consisting of the pivot `i` and at most two possible companion rows.

### Proof

If `h<1`, apply the completed two-volume half-Riesz estimate (1.1) to the exact Schur remainder `R`, whose same-side quadratic and affine terms are unrestricted. Then apply the dependence-safe square peel (1.2):

`||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] |a|^(-1/2) Z_2(C)^(-1/8)`.   (4.8)

Insert the exact lower bound (3.4), obtaining (4.4). This is a true density bound, so integrating it over an interval gives (4.5) without a square-root loss.

At `h<=3/4`, take `q<=3/2`; the source constant at `q=3/2` is `<16.856`, giving (4.6).

If `h>3/4`, choose a maximizing row `j`; then (4.7) follows from (3.4). Equation (4.3) implies that three such rows would have total marginal greater than `9/4>2`; hence there are at most two. QED.

## 5. Direct splice into the preceding aggregate-heavy-row compiler

In the preceding `QFORM-AGGREGATE-SINGLETON-VOLUME-TO-CUT-v1`, take the fixed physical cut obtained by the half-coloring argument and the cutoff `h_0=2/3`. In its unpaid branch there is a row `i` for which the selected anchored mass satisfies

`N_i>S/24`.                                                    (5.1)

The full anchored third-volume `V_i(B)` of that same actual fixed cut dominates the selected family, so

`V_i(B)>S/24`.                                                 (5.2)

If the physical diagonal `a=A_ii` is nonzero, Theorem 4.1 now gives the following explicit continuation.

Either the exact Schur cross has two-volume row marginal at most `3/4`, and

`boxed:
 ||p_Q||_infinity
 < 16.856 * 24^(1/8)
    |A_ii|^(-1/2) ||A[i,V]||^(1/4) S^(-1/8)
 < 25.078 |A_ii|^(-1/2) ||A[i,V]||^(1/4) S^(-1/8),
`                                                                 (5.3)

with the identical linear interval bound; or the obstruction is localized to at most two literal companion rows `j`, each satisfying

`T_j(C) > (3/4)Z_2(C) > S/(32 ||A[i,V]||^2)`.                 (5.4)

Thus the old “fewer than 72 heavy rows” branch no longer remains a diffuse high-dimensional state once a nonzero physical pivot is chosen: each actual heavy row is either paid by a rank-two fractional potential, or produces a two-row physical collar carrying a quantitative amount of Schur two-volume.

This does NOT yet supply a universal lower bound for the combination on the right of (5.3). In particular the zero/near-zero physical-pivot branch remains unpaid and is one of the current owner-priority gaps. Nor does (5.4) itself prove that the resulting physical pair has a uniformly conditioned principal `2x2` block; that is the next collar-elevation step.

## 6. A target-valid exact identity check

Take three source-side cross directions: one pivot row

`b=e_1 in R^3`,

and three remaining physical rows forming an equal-norm Parseval two-frame in `span{e_2,e_3}`:

`r_1=sqrt(2/3)e_2`,
`r_2=-e_2/sqrt(6)+e_3/sqrt(2)`,
`r_3=-e_2/sqrt(6)-e_3/sqrt(2)`.

Let `B=[b;r_1;r_2;r_3]`, set the physical pivot `A_ii=1`, and take `u=0`. Then `B^T B=I_3`, so the anchored third-volume is

`V_i(B)=1`,                                                     (6.1)

while the Schur cross is `C=[r_1;r_2;r_3]`,

`Z_2(C)=1`,                                                     (6.2)

and every two-volume row marginal is `2/3`. Theorem 4.1 uses `q=4/3` and gives

`||p_Q||_infinity
 <=4 sqrt(2e)(4/3)^(-1/4)/(2-4/3)
 =13.0190354...`.                                               (6.3)

Putting zero self blocks elsewhere, the full symmetric matrix with source--column cross `B` and pivot diagonal one decomposes into two exact hyperbolic `+/-1` directions and one `[[1,1],[1,0]]` block. It therefore has at least three eigenvalues of modulus at least one. This is a literal target-valid sanity family for every admissible product law.

The example is only a regression check; stronger rank-three cross smoothing is available for this especially clean matrix. The new content of Theorem 4.1 is the exact Schur-shear invariant (3.2) and its use in the aggregate-heavy-row routing where arbitrary same-side curvature is retained.

## 7. Newest designated partner fleet02/B09 applied to an actual inequality

The newest completed designated-partner result is fleet02/B09 run
`20260923T130908Z-fleet02-B09-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@57cb337f65c30114d12bc21ee05d2925663dc641`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T130908Z-fleet02-B09-QFORM-auto11/REPORT.md`.

Its `QFORM-FRACTIONAL-SUBVOLUME-BL-q-v1` / rank-two-hub-star compiler pays the physical hub-frame regime `eta<3/4`, including `eta>1/2`, while retaining arbitrary dense within-leaf curvature.

Apply it at `m=64` to its literal three-row equal-norm Parseval hub frame

`p_1=(sqrt(2/3),0)`,
`p_2=(-1/sqrt(6),1/sqrt(2))`,
`p_3=(-1/sqrt(6),-1/sqrt(2))`,

so every physical hub leverage is `eta=2/3`. Take a complete flat orthonormal 64-coordinate leaf basis `c_1,c_2,v_3,...,v_64`, put `C=[c_1,c_2]`, and let

`D=sum_(ell=3)^64 sigma_ell v_ell v_ell^T`

with 31 signs `+1` and 31 signs `-1`. For

`A=[[0, P C^T],[C P^T,D]]`,

all nonzero eigenvalues have modulus one, so the exact target hypothesis holds. The partner aggregate is

`G_*=64(1-2/64)^2 = 961/16 =60.0625`.                         (7.1)

Its completed theorem therefore gives the actual inequality

`boxed:
 ||p_(X^T A X)||_infinity
 <=30.824 (961/16)^(-1/6)
 <15.576,
`                                                                 (7.2)

and

`boxed: P{X^T A X in J}<15.576 |J|`.                          (7.3)

This application is beyond the old `eta<=1/2` hub-frame gate and retains the full dense same-side leaf operator `D`.

## 8. What remains

The first unpaid B09 implication is now

`QFORM-TWOROW-COLLAR-ZEROPIVOT-OR-PAIR-EXIT-v1`:

Starting from the companion-row branch (4.7)/(5.4), use the two literal original coordinates in the collar and the quantitative residual two-volume to force one of: a paid nonsingular/definite/singular physical pair endpoint; a grouped one-hub/one-square packet; a rank-three original-coordinate cross-volume exit; or a genuine zero/near-zero physical-pivot mechanism using conditional linear anti-concentration without a logarithmic loss. The key remaining difficulty is precisely the `A_ii ->0` regime; (3.2) shows that arbitrary source-side Schur couplings are not the problem once a real pivot exists.

No claim is made that the bare three-large-eigenvalue hypothesis already bounds the coefficient in (5.3) universally. Full QFORM remains OPEN. Full-target continuity remains OPEN. Continuity is not claimed for Theorem 4.1; it proves essential boundedness and the linear interval estimate.

## 9. Correction safety

This report does not use any of the refuted interfaces: no law-uniform pointwise van-der-Corput decay; no arbitrary-joint three-dimensional coarea cap; no positive conditional projection-density moment; no post-rotation independence; no bounded projection density as a substitute for an indefinite pushforward; no small operator residual discarded as a random error; and no Monte Carlo histogram as proof. The random inputs are manipulated only through original-coordinate conditioning and completed source-valid cross-volume/fractional-potential estimates.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T13:20:48Z.
attacking: integrated Fourier estimate — close the concentrated near-rank-one Schur collar by turning two-sided residual energy concentration into a genuine physical 3x3 cross pivot, then apply fleet02/B02's grouped L1 theorem at k=3.

# fleet01/B02 r30 — double-heavy Schur energy gives a genuine three-pivot L1 Fourier exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the branch below because the full characteristic function is genuinely in `L1`; unrestricted continuity remains open.  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`.

The exact owner target remains unchanged: independent ORIGINAL real coordinates with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, or independence after a rotation/shear is introduced.

## 1. Fresh source actually applied

The designated partner fleet02/B02 proves `QFORM-CROSS-SCHUR-SHEAR-GROUPED-L1-v1` in

`yspennstate/math-open-problems@b84e108c872878d108d736c123482d15b252b5df`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T110948Z-fleet02-B02-QFORM-r11/REPORT.md`.

For two disjoint ORIGINAL-coordinate banks with physical cross block

`B=[[P,R],[C,M]]`,

where `P` is an invertible physical `k x k` block and

`S=M-C P^{-1}R`,

if `r=rank(S)` and `d=k+r>2`, the partner theorem gives a genuine `L1_t` characteristic-function estimate and

`||p_Q||_infinity
 <= [d/(d-2)] exp(r/d)
    (|det P| Delta_r(S))^(-1/d)`.

More precisely its proof gives

`|phi_Q(t)|
 <= min{1,
   pi^(d/2)|t|^(-d/2)
   [B(U)B(V)]^(1/2)
   (|det P| Delta_r(S))^(-1/2)}`,

with the weighted affine-fiber projection factors `B(U),B(V)` and with arbitrary same-bank quadratic terms, outside couplings and affine terms retained. The proof uses only bankwise deterministic shears and never declares transformed coordinates independent.

The special case used below is `k=3,r=0,d=3`. For any invertible ORIGINAL-coordinate physical `3 x 3` cross block `P_3`, after conditioning on all other coordinates the theorem gives

`boxed:
 |phi_Q(t)| <= min{1, pi^(3/2)|det P_3|^(-1/2)|t|^(-3/2)},
}`

hence exactly

`boxed:
 integral_R |phi_Q(t)|dt <= 6 pi |det P_3|^(-1/3),
 ||p_Q||_infinity <= 3 |det P_3|^(-1/3).
}`                                                                  (1.1)

This is the partner result applied below at an actual new determinant inequality.

## 2. Exact anchored extension identity

Now specialize the partner setup to a genuine invertible physical `2 x 2` cross pivot. Let

`B=[[P,R],[C,M]]`, `P in R^(2x2)`, `det P !=0`,

between two disjoint banks of original coordinates, and define

`S=M-C P^(-1)R`,
`D=|det P|`,
`F=||S||_F^2`,
`G=D^2 F`.                                                         (2.1)

Assume `F>0`. For every residual physical row `i` and residual physical column `j`, let

`P_3(i,j) = [[P, R_:j],[C_i:, M_ij]]`.                              (2.2)

This is a literal `3 x 3` submatrix of the original physical cross block, not a rotated or sheared random-coordinate object. The block determinant formula gives the exact identity

`boxed:
 det P_3(i,j)=det(P) S_ij.
}`                                                                  (2.3)

Consequently

`sum_(i,j) |det P_3(i,j)|^2 = D^2 ||S||_F^2 = G`.                  (2.4)

Thus `G` is precisely the total squared mass of all physical `3 x 3` minors extending the fixed `2 x 2` anchor by one residual row and one residual column.

## 3. New theorem — `QFORM-DOUBLEHEAVY-SCHUR-THREEPIVOT-L1-v1`

Define normalized Schur row and column energy marginals

`a_i=||S_i:||_2^2/F`,
`b_j=||S_:j||_2^2/F`,
`h_r=max_i a_i`,
`h_c=max_j b_j`.                                                    (3.1)

If

`theta:=h_r+h_c-1 >0`,                                              (3.2)

then the full ambient quadratic form satisfies

`boxed:
 integral_R |phi_Q(t)|dt
 <= 6 pi theta^(-1/6) G^(-1/6),
}`                                                                  (3.3)

and

`boxed:
 ||p_Q||_infinity
 <= 3 theta^(-1/6) G^(-1/6).
}`                                                                  (3.4)

The density is continuous and vanishes at infinity.

### Proof

Choose a row `i` with `a_i=h_r` and a column `j` with `b_j=h_c`. The union of that row and column is a subset of the whole matrix, so

`||S_i:||_2^2 + ||S_:j||_2^2 - |S_ij|^2 <= ||S||_F^2`.

After division by `F`,

`|S_ij|^2/F >= h_r+h_c-1=theta`.                                   (3.5)

Using (2.3),

`|det P_3(i,j)|^2
 =D^2 |S_ij|^2
 >=theta D^2 F
 =theta G`.                                                         (3.6)

Now condition on every original coordinate except the three selected source coordinates and the three selected receiver coordinates. This preserves the independence and density caps of those six physical variables. All couplings to conditioned coordinates merely become affine terms, while arbitrary quadratic self-blocks on the selected triples remain present.

Apply the completed fleet02/B02 theorem (1.1) to the actual physical `3 x 3` pivot `P_3(i,j)`. From (3.6),

`|det P_3(i,j)|^(-1/3) <= theta^(-1/6)G^(-1/6)`.

Substitution into (1.1) proves (3.3)-(3.4), uniformly in every conditioning value. Averaging the conditional characteristic functions preserves (3.3), and Fourier inversion gives the continuous `C_0` density. QED.

### Scope note

The live correction that a generic low-order cross minor does not by itself solve QFORM is respected. What is used here is stronger and exact: a **scale-certified invertible 3 x 3 physical cross pivot**. Three bilinear directions give `|t|^(-3/2)`, which is integrable. No analogous claim is made for a single `2 x 2` cross minor, whose direct Fourier exponent is only the logarithmic endpoint.

## 4. Quantitative application to the partner's live double-anchor packet

The same fleet02/B02 report works with the double-anchor currency

`G=D^2||S||_F^2`

and on its live residue records

`G>Z3/24`.                                                          (4.1)

If the normalized Schur row and column energies are both at least `3/4`, then

`theta=h_r+h_c-1 >=1/2`.                                           (4.2)

The new theorem therefore gives

`||p_Q||_infinity
 <=3*2^(1/6)G^(-1/6)
 <3*48^(1/6) Z3^(-1/6)
 =5.719106... Z3^(-1/6)`,                                          (4.3)

and

`integral_R |phi_Q(t)|dt
 <6pi*48^(1/6) Z3^(-1/6)
 =35.934202... Z3^(-1/6)`.                                         (4.4)

This pays a genuinely arbitrary-rank **two-sided heavy Schur** branch. The entire residual matrix `S` may have as many additional nonzero singular directions as it likes; none is deleted or treated as independent noise. The proof conditions down to a literal physical six-coordinate pivot only after the scale lower bound (3.6) has been established.

## 5. Near-rank-one spectral consequence

The partner identifies the low-stable-rank Schur residue as an important remaining collar. The new theorem yields a sharp concentration/diffusion alternative there.

Let

`rho=sr(S)=||S||_F^2/s_1(S)^2 >=1`,                                (5.1)

and choose top left/right singular vectors `u,v`. Put

`L=max_i |u_i|^2`, `R=max_j |v_j|^2`.                              (5.2)

Because

`||S_i:||_2^2 >= s_1(S)^2 |u_i|^2`,
`||S_:j||_2^2 >= s_1(S)^2 |v_j|^2`,

we have

`h_r>=L/rho`, `h_c>=R/rho`.                                       (5.3)

Therefore, whenever

`L+R>rho`,                                                         (5.4)

the theorem applies with at least

`theta >= (L+R-rho)/rho`,                                         (5.5)

so

`boxed:
 ||p_Q||_infinity
 <=3 [rho/(L+R-rho)]^(1/6) G^(-1/6),
}`                                                                  (5.6)

with twice-pi times the right side as an `L1_t` bound.

Conversely, if the three-pivot gate fails (`h_r+h_c<=1`), then (5.3) forces the exact structural constraint

`boxed: L+R<=rho.`                                                  (5.7)

Thus a near-rank-one Schur matrix can remain outside this new physical-pivot Fourier exit only if at least one of its leading singular vectors is physically diffuse.

A useful fixed quantitative version is the following. If

`rho<=9/8`,                                                         (5.8)

then either

`L+R >= rho+1/8`,                                                   (5.9)

in which case `theta>=1/9` and

`||p_Q||_infinity <=3*9^(1/6)G^(-1/6)`,                            (5.10)

or

`min(L,R) <=(rho+1/8)/2 <=5/8`.                                   (5.11)

On the live packet (4.1), the first alternative becomes the clean bound

`boxed:
 ||p_Q||_infinity < 3 sqrt(6) Z3^(-1/6) <7.349 Z3^(-1/6),
 integral |phi_Q| < 6 pi sqrt(6) Z3^(-1/6) <46.172 Z3^(-1/6).
}`                                                                  (5.12)

So the partner's `near-rank-one transverse receiver` debt is reduced further: after this run, the quantitatively concentrated leading-left/leading-right case is paid by an actual three-pivot Fourier argument. A still-unpaid near-rank-one state must have a leading singular vector with a definite one-sided physical diffusion certificate (for example `<=5/8` in (5.8)-(5.11)), or lie in the arbitrarily thin transition where the margin `L+R-rho` is small.

## 6. Why this is not the full theorem

The bare global hypothesis `s_3(A)>=1` does not automatically supply a two-anchor packet with both `G` at universal scale and `h_r+h_c>1`. The fleet already contains source-valid families showing that local-pivot extraction can fail while grouped bank mechanisms still succeed. The theorem here is therefore a real receiver, not a global structural reduction.

In particular, no claim is made that:

- every three-large-eigenvalue matrix has a uniformly conditioned physical `3 x 3` cross minor;
- every low-stable-rank Schur residue is two-sided concentrated;
- a small residual tail can be discarded for arbitrary unbounded product laws;
- a general spectral rotation preserves independence.

The exact next unpaid implication for this slot is

`QFORM-SCHUR-NEARRANK1-ONE-SIDED-DIFFUSE-L1-v1`:

> Starting from the same genuine invertible physical `2 x 2` anchor and a low-stable-rank Schur residual, use the one-sided leading-vector diffusion forced by (5.7)/(5.11) to obtain a product-preserving integrated-Fourier or direct-density estimate **without deleting the transverse Schur tail**. The natural candidate is a fractional grouped projection/Hausdorff--Young receiver inside the bankwise shear representation.

The target-wide statement

`integral_R |E exp(it X^T A X)|dt <= C`

therefore remains `OPEN_NOT_REFUTED`. I found no target-valid counterexample in this run. The full universal bounded-density conjecture and full continuity conclusion also remain OPEN.

## 7. Correction audit

No refuted premise is used:

1. no law-uniform pointwise van-der-Corput decay;
2. no independence after spectral rotation or bankwise shear;
3. no arbitrary-joint coarea density theorem;
4. no conditional density cap after sum/difference transformations;
5. no deletion of a small coefficient/singular-value tail;
6. no inference that an unscaled low-order minor is enough;
7. no Gaussian, moment, support, interval-extremality or Monte Carlo assumption.

All selected pivots are literal ORIGINAL-coordinate submatrices, and all probabilistic conditioning is on disjoint ORIGINAL coordinates.

## 8. Status

This is a supporting target-level theorem and a quantitative narrowing of the partner's low-stable-rank Schur obstruction. It is not a full solution and has not yet received two independent end-to-end reviews. The universal Fourier-L1 criterion remains open rather than refuted.

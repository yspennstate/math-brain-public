# Addendum: diffuse-row norm defect forces a third child direction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker/run: `fleet01/B08`, `20260923T144019Z-fleet01-B08-qform-r30`  
Status: **PROVED SUPPORTING THEOREM / STRONGER PARTNER COMPILER / FULL TARGET OPEN**

This addendum strengthens the rank-loss-only route in `REPORT.md`. The key point is that in a diffuse selected-three eigenspace the rank-one defect created by deleting a physical coordinate has small **operator norm unless the physical star itself is large**. This preserves all three large directions in the principal child, not merely two.

## 1. Exact row-defect tradeoff

Let `A=A^T`, let `R in R^{n x 3}` have orthonormal columns, and suppose

`A R=R Lambda`,

`min_j |Lambda_jj|>=L>0`.

Fix an ORIGINAL coordinate `i`, and write

`A=[[a,b^T],[b,C]]`,

`R=[r; R_T]`,

where `r=R_i` is a `1 x 3` row, `b=A[-i,i]`, and `C=A[-i,-i]`. Put

`p=||r||_2^2`.

### Theorem A.1 — `QFORM-DIFFUSE-ROW-DEFECT-TRADEOFF-v1`

One has the exact deterministic inequality

`boxed:
 s_3(C) >= [L sqrt(1-p) - ||b||_2 sqrt(p)]_+.}`               (A.1)

Equivalently, whenever the bracket is positive,

`s_3(A[-i,-i]) + ||A[i,-i]||_2 sqrt(p)
 >= L sqrt(1-p).`                                              (A.2)

#### Proof

The `T`-row block of the genuine eigen-equation is

`b r + C R_T = R_T Lambda`,

so

`C R_T=R_T Lambda-b r`.                                       (A.3)

Because

`R_T^T R_T=I-r^T r`,

its smallest singular value is

`s_3(R_T)=sqrt(1-p)`.                                         (A.4)

Hence

`s_3(R_T Lambda)>=L sqrt(1-p)`.                               (A.5)

The rank-one defect in (A.3) has exact operator norm

`||b r||op=||b||_2 ||r||_2=||b||_2 sqrt(p)`.                  (A.6)

Ordinary Weyl perturbation now gives

`s_3(CR_T)
 >=L sqrt(1-p)-||b||_2 sqrt(p)`.                              (A.7)

Finally `||R_T||op<=1`, and therefore

`s_3(CR_T)<=s_3(C)||R_T||op<=s_3(C)`.                         (A.8)

Combining (A.7)-(A.8), with nonnegativity of singular values, proves (A.1). QED.

No complementary spectrum is removed anywhere in this argument: `C` and `b` are the literal blocks of the full matrix.

## 2. Uniform diffuse corollary

Under the B08 selected-three diffuse hypothesis

`p=||R_i||^2<=1/48`                                           (A.9)

for every physical coordinate, (A.1) yields

`boxed:
 s_3(A[-i,-i])
 >= [sqrt(47/48)L - ||A[i,-i]||_2/sqrt(48)]_+.}`              (A.10)

For any threshold `theta>=0`, this gives the dichotomy

`||A[i,-i]||_2>theta L`                                       (A.11)

or

`boxed:
 s_3(A[-i,-i])
 >= [sqrt(47/48)-theta/sqrt(48)]L.}`                          (A.12)

This is substantially stronger than the rank-only statement `s_2>=sqrt(47/48)L` whenever the star is not already large.

At the useful choice `theta=1/4`, define

`kappa=sqrt(47/48)-1/(4sqrt(48))
      =0.953444115428808...`.                                 (A.13)

Then at every physical coordinate in the selected-three diffuse regime,

`boxed:
 ||A[i,-i]||_2>L/4
   OR
 s_3(A[-i,-i])>=kappa L.}`                                   (A.14)

## 3. Stronger application of designated partner fleet02/B08

Use the completed partner source

`yspennstate/math-open-problems@41ee49f6e9c3383e4c3a322bdc52779768a17eb7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T130941Z-fleet02-B08-qform-diffuse-r27/REPORT.md`.

On its `k=1` high-top-two-leverage branch, the partner produces a physical coordinate `i` with cross row `g` satisfying

`||g||>(3/16)sqrt(3/10)L
      =0.102697979532218...L`.                                (A.15)

Since `g` is a subvector of the literal full star `b=A[-i,i]`,

`||b||>=||g||>0.102697979532218 L`.                            (A.16)

Apply (A.14) at this **same** coordinate. The entire partner high-row survivor therefore satisfies the sharper exhaustive alternative

**(S)**

`boxed: ||A[i,-i]||_2>L/4,`                                   (A.17)

or

**(C3+)**

`boxed:
 0.102697979532218L < ||A[i,-i]||_2 <=L/4,
 s_3(A[-i,-i])>=0.953444115428808L.}`                         (A.18)

Thus unless the partner star upgrades to a quarter-`L` star, deleting the same physical coordinate preserves **three** almost-`L` singular directions.

## 4. An actual density estimate on the C3+ branch

Let `C=A[-i,-i]` in (A.18), and let

`P_C=1_{|C|>=kappa L/64}`.                                    (A.19)

Apply the completed one-scale spectral-window theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

inside the child coordinates. Its general ridge criterion is ambient and allows arbitrary outside coordinates/couplings, so the original coordinate `i` and its star are retained rather than probabilistically deleted.

If

`max_j(P_C)_jj<=1/32`,                                        (A.20)

then the **original full form** has a continuous `C_0` density with

`boxed:
 ||p_Q||_infinity
 <= [288sqrt(3e)/(13 kappa)] L^(-1)
 =66.3531830068.../L <67/L.}`                                 (A.21)

If (A.20) fails, choose a child coordinate `j` with `(P_C)_jj>1/32`. Spectral energy in the literal child gives

`||C e_j||_2^2>(kappa L/64)^2/32`,                            (A.22)

hence

`boxed:
 max{|C_jj|,||C[j,(-i,-j)]||_2}
 > kappa L/512
 =0.00186219553795...L.}`                                    (A.23)

Combining with (A.16), every unpaid C3+ survivor is therefore a genuine two-coordinate physical core:

`i` carries a star `>0.1026979L`, while a distinct child coordinate `j` carries high child-window leverage and a scalar/star resource `>0.00186219L`.

This is a valid original-coordinate reduction. It does not assert that the two resources alone already form a good indefinite principal pair.

## 5. Updated first unpaid implication

After consuming the partner high-row branch, the sharper first gap is

`QFORM-QUARTER-STAR-OR-TWOLEVEL-CORE-RECEIVER-v1`:

* either pay a literal physical star `||A[i,-i]||>L/4` while the same deleted child still has the rank-conservation resource `s_2>=sqrt(47/48)L`; or
* pay the two-level core from (A.16),(A.23), where the first star is `>0.1026979L`, the child has three `>=0.953444L` singular directions, and the second child coordinate is high in the child spectral window.

Arbitrary same-bank curvature, all unused couplings, the full complementary spectrum and all affine terms must remain present. A bare `ell^2` star is not being promoted to a physical-pair determinant theorem.

Continuity is proved only on the paid branch (A.21), not on the remaining structural branches.

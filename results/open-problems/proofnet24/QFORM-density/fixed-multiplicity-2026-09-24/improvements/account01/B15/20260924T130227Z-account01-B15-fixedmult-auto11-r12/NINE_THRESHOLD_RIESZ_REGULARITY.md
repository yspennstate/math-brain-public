# B15 improvement — nine directions and the exact order-three regularity payoff

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Threshold-reduction source reviewed: account03/B04 commit `8ff490c177d0cd7d6f33130f1431785e312a9d10`, report blob `054facef834d29927713c5d42a1f09a541c5644b`.  
Explicit rough-law limit repair reviewed: account02/B04 commit `f1e43c2b688013aed9ff00a3e5ceba398d34793b`.

## 1. Threshold status

After an independent reconstruction in this B15 run, the repaired grouped-Fourier argument gives the following complete replacement theorem:

> If the independent coordinate densities are bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density. The original candidate constant `6010 K^2/s` is valid.

No Gaussianity, moment, support, sign, exact-rank, leverage, diagonal-basis, or post-rotation-independence assumption is introduced.

The proof is the following closed dependency chain. Normalize `K=s=1` and keep `eta=1/100`, `kappa=1/80^2`.

1. No pivot: baseline Proposition `prop:volume` at order three gives `V_3(A)>=kappa^3`; the fair original-coordinate cut gives a literal cross block `M` with `E_3(M)>=4^{-3}kappa^3`. The marginal-free third-crossing compiler then gives density `<2400`.
2. Scalar pivot: the Schur complement retains at least eight unit-scale directions. If it has a pivot, the baseline pivot half-potential theorem gives full half-potential `<=601`. If it has no pivot, then `s_5>=1`; baseline order-two volume plus the marginal-free `E_2` compiler gives full half-potential `<153`. The outer square profile therefore gives density `<=6010`.
3. Definite pair: conditional density `<=10pi`.
4. Indefinite pair: seven Schur directions remain, so the baseline one-direction logarithmic-potential argument applies and is `<251`.
5. Scale back with `Y=KX` and `Q=(s/K^2)Qtilde`.

At least two separate full PASS reconstructions of this nine-direction theorem are now recorded in the repository: account01/B16 commit `54ec2a651d854563f8db0d92c4c3426f76551786` and account03/B08 commit `c02a08f19d010e508578695a5906744fdbcfcd70`; account02/B04 also supplied the explicit rough-law limit repair and independent derivation. This file records the evidence but does not self-award release/validation status.

No theorem below nine directions is proved here. The present order-three structural route has a genuine bookkeeping endpoint at the worst sampled seed `r=2`: global interpolation rank is `<=6`, restricted rank is `<=2`; eight unit-scale singular values can force only two large diagonal residual coordinates, which does not contradict restricted rank two. Nine forces three. This is a barrier to this route, not a counterexample to an eight-direction theorem.

## 2. New B15 regularity lemma for the marginal-free third-crossing receiver

The grouped third-crossing proof contains more information than its stated density bound. It supplies a uniform `|t|^{-3/2}` characteristic-function envelope in every promotion branch.

### Proposition

Let a full quadratic polynomial be split across literal disjoint original-coordinate banks, retaining arbitrary same-bank quadratic and affine phases, and let `M` be the literal crossing block. Put

`Z=E_3(M)=e_3(MM^T)>0`.

Under independent cap-one original-coordinate laws,

`|phi_Q(t)| <= min(1, B_3 Z^{-1/4}|t|^{-3/2})`,

where

`B_3 = pi^(3/2) sqrt(6) e^(3/2)`.

Consequently the canonical density satisfies

`||p_Q||_infinity <= 3*6^(1/3)*e * Z^{-1/6}`

and

`p_Q in C_0(R) cap C^{0,1/2}(R)`

with

`[p_Q]_{C^{0,1/2}} <= 8 sqrt(3pi) e^(3/2) Z^{-1/4}`.

### Proof of the Fourier envelope

Use the physical-row promotion tree from the reviewed nine-direction compiler.

**Diffuse third volume.** If every canonical `E_3` row marginal is at most `1/2`, the grouped compiler with `(k,ell,d)=(0,3,3)` gives

`B_{0,3}=pi^(3/2) 2^(3/4)e^(3/2)(3^3/3!)^(1/4)Z^{-1/4}`.

Since `2^(3/4)(9/2)^(1/4)=sqrt(6)`, this is exactly `B_3 Z^{-1/4}`.

**One promoted physical row.** If an incident mass `J_i>Z/2`, project the other rows orthogonally off the promoted literal row. The exact Gram identity is

`J_i=S^2 Z_2`,

where `S` is the norm of the promoted crossing row and `Z_2` is the residual second volume. In the diffuse residual branch, `(k,ell,d)=(1,2,3)` gives

`|phi_Q(t)| <= pi^(3/2)2^(3/4)e^(5/4)J_i^{-1/4}|t|^{-3/2}`.

Using `J_i>Z/2` makes the coefficient at most

`2 pi^(3/2)e^(5/4) Z^{-1/4}`,

which is smaller than `B_3 Z^{-1/4}` because

`2e^(5/4) < sqrt(6)e^(3/2)`.

**Two promoted physical rows.** If a residual row is heavy, the next exact Gram identity is

`H_ij=det(PP^T) Z_1 > J_i/2 > Z/4`.

The `(2,1,3)` compiler gives raw coefficient

`pi^(3/2)2^(1/4)e H_ij^{-1/4}`.

Since `H_ij>Z/4`, this is at most

`pi^(3/2)2^(3/4)e Z^{-1/4}<B_3 Z^{-1/4}`.

**Three promoted physical rows.** A final heavy residual row gives a literal three-row Gram determinant `D>Z/8`. The terminal rank-three Plancherel receiver gives

`|phi_Q(t)| <= pi^(3/2)e^(3/4)D^{-1/4}|t|^{-3/2}`,

hence at most

`pi^(3/2)2^(3/4)e^(3/4)Z^{-1/4}|t|^{-3/2}<B_3 Z^{-1/4}`.

The four cases exhaust the promotion tree, proving the common envelope.

### Density and half-Hölder estimates

Write `B=B_3 Z^{-1/4}`. Since

`|phi_Q(t)|<=min(1,B|t|^{-3/2})`,

its Fourier transform is integrable. Direct integration, or the baseline power-envelope lemma with exponent `3/2`, gives

`||p_Q||_infinity <= (3/pi)B^(2/3)`

`=3*6^(1/3)e Z^{-1/6}`.

Fourier inversion also gives `p_Q in C_0`. For `h!=0`, use `|e^{-ith}-1|<=min(2,|h||t|)` and the global bound `|phi_Q(t)|<=B|t|^{-3/2}`:

`|p_Q(x+h)-p_Q(x)|`

`<= B/(2pi) int_R min(2,|h||t|)|t|^{-3/2}dt`.

The positive-half-line integral is

`|h| int_0^(2/|h|) t^{-1/2}dt + 2 int_(2/|h|)^infinity t^{-3/2}dt`

`=4 sqrt(2|h|)`.

Doubling for both signs and multiplying by `B/(2pi)` yields

`|p_Q(x+h)-p_Q(x)| <= (4sqrt(2)/pi)B |h|^(1/2)`

`=8sqrt(3pi)e^(3/2) Z^{-1/4}|h|^(1/2)`.

This proves the proposition.

## 3. Concrete regularity in the no-pivot nine-direction chamber

If `A` has no `eta`-pivot and `s_9(A)>=1`, the baseline structural proposition and fair cut give

`Z>=4^{-3}kappa^3`, with `kappa=1/80^2`.

Hence

`Z^{-1/6}<=160`

and

`Z^{-1/4}<=160^(3/2)`.

Therefore this branch has

`||p_Q||_infinity <= 160*3*6^(1/3)e <2400`

and

`[p_Q]_{C^{0,1/2}} <= 8sqrt(3pi)e^(3/2)160^(3/2)`

`< 2.228e5`.

The numerical Hölder constant is intentionally not optimized; the point is the exact regularity exponent and its provenance.

## 4. Exact B15 threshold interpretation

The analytic thresholds are now:

- Baseline determinant, order three: `|phi| ~ |t|^{-3/4}`. Not `L^1`; after the Riesz weight `|t|^{-1/2}` it is integrable, so it pays a negative half moment only.
- Grouped/promotion compiler, effective dimension two: `|phi| ~ |t|^{-1}`. Still not `L^1`; after the Riesz weight it is integrable, which is exactly what the scalar-pivot branch needs.
- Grouped/promotion compiler, effective dimension three: `|phi| ~ |t|^{-3/2}`. This is `L^1`, so it pays bounded density, `C_0`, and a sharp-for-this-envelope half-Hölder modulus.
- Baseline determinant, order five: `|phi| ~ |t|^{-5/4}`. Also `L^1`, hence bounded continuous density, but it is no longer needed once the repaired order-three grouped receiver is admitted.

This explains analytically why the new theorem can drop the no-pivot multiplicity threshold from 17 to 9 without pretending that the old raw order-three determinant envelope was itself integrable.

The full nine-direction theorem is still stated only in essential-`L^infinity` form: the scalar and pair pivot branches in the replacement proof are measure-domination arguments and this run does not promote them to a global continuity theorem.

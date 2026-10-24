# QFORM B12 — Krylov-footprint spectral-square stability

Run: `20260923T162217Z-account01-B12-QFORM-auto11`

Status: **proved supporting stability theorem; full QFORM remains OPEN.**

## Target and scope

The owner target is the universal bounded-density conjecture for `Q=X^T A X` under independent real coordinates with one-dimensional density caps `f_i<=1` and at least three eigenvalues of `A` of modulus at least one. This report addresses only the assigned additional-eigenvalue control problem. It never rotates the random vector and never treats a dependent quadratic remainder as an independent convolution.

The matrix theorem below separates arbitrarily large signed added modes from an arbitrary small dense remainder. Large modes are charged only by a finite-dimensional Krylov footprint; their amplitudes disappear completely.

## Theorem 1 — Krylov-footprint spectral-square stability

Let `A0,S,R` be real symmetric `n x n` matrices. Put

`U = Ran(S)`, `q = dim(U + A0 U)`.

Then `q<=2 rank(S)`. Let `H` be any set of original coordinates, and write `P_H` for the corresponding coordinate projection. For every integer `k>=1` with `k+q<=|H|`,

`lambda_k(((A0+S)^2)[H,H]) >= lambda_{k+q}((A0^2)[H,H]).`  (1)

If additionally `||R||op<=eps` and `A=A0+S+R`, then

`sqrt(lambda_k((A^2)[H,H])) >= ( sqrt(lambda_{k+q}((A0^2)[H,H])) - eps )_+`,  (2)

and hence

`lambda_k((A^2)[H,H]) >= ( sqrt(lambda_{k+q}((A0^2)[H,H])) - eps )_+^2.`  (3)

All eigenvalues of `S` may have arbitrary signs and arbitrarily large magnitudes.

### Proof

Set `B=A0+S`. The exact square identity is

`B^2-A0^2 = A0 S + S A0 + S^2.`

Since `Ran(S)=U`,

`Ran(A0 S) subset A0 U`,
`Ran(S A0) subset U`,
`Ran(S^2) subset U`.

Therefore

`Ran(B^2-A0^2) subset U + A0 U`,

so

`rank(B^2-A0^2) <= q`.

Compression cannot increase rank, hence

`rank( P_H(B^2-A0^2)P_H ) <= q`.

For Hermitian matrices `X,Y` with `rank(X-Y)<=q`, rank-interlacing gives

`lambda_k(X) >= lambda_{k+q}(Y)`

for every admissible `k`. Apply this with

`X=P_H B^2 P_H`, `Y=P_H A0^2 P_H`

to obtain (1).

For (2), observe the exact singular-value identity

`sqrt(lambda_k((M^2)[H,H])) = s_k(M P_H)`

for every real symmetric `M`, because

`(M P_H)^T(M P_H)=P_H M^2 P_H`

on the coordinate space `H`. Weyl's singular-value perturbation inequality gives

`s_k(A P_H) >= s_k(B P_H)-||R P_H||op >= s_k(B P_H)-eps`.

Combine with (1) and square to get (2)-(3). QED.

## Sharpness of the `2 rank(S)` reserve loss

The factor two cannot be improved in general using only `rank(S)`. Take

`A0=[[0,1],[1,0]]`, `S=t [[1,0],[0,0]]`, `t!=0`.

Then `rank(S)=1`, but

`(A0+S)^2-A0^2 = [[t^2,t],[t,0]]`

has determinant `-t^2`, hence rank two. Here `U+A0U=R^2`, so `q=2` exactly.

If `U` is `A0`-invariant, then `q=dim U=rank(S)` and only one reserve direction per arbitrary large mode is lost. Thus the correct parameter is the Krylov footprint `dim(U+A0U)`, not merely `2 rank(S)`.

## Corollary 2 — adaptive large/small spectral split

Let an arbitrary symmetric addition have spectral decomposition

`E=sum_j theta_j v_j v_j^T`.

For a threshold `h>=0`, define

`S_h=sum_{|theta_j|>h} theta_j v_j v_j^T`,
`W_h=sum_{|theta_j|<=h} theta_j v_j v_j^T`.

Then `||W_h||op<=h`. Put

`U_h=Ran(S_h)`, `q_h=dim(U_h+A0 U_h)`.

For any additional symmetric dense tail `T` with `||T||op<=delta`, the final matrix

`A=A0+E+T`

satisfies, for `k+q_h<=|H|`,

`sqrt(lambda_k((A^2)[H,H])) >= ( sqrt(lambda_{k+q_h}((A0^2)[H,H])) - h - delta )_+.`  (4)

Thus:

* every mode with `|theta_j|>h` may have arbitrary sign and arbitrary magnitude; its amplitude never appears in (4);
* the high modes cost only the dimension `q_h` of their physical Krylov footprint;
* every remaining mode, of arbitrary multiplicity, sign and orientation, costs only the single threshold `h`;
* a further full nonseparable symmetric tail costs only its matrix norm `delta`.

One may optimize (4) over `h`.

## Application to completed partner result `account02/B12`

Partner source: `yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`, path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

That completed theorem states: if the actual final symmetric matrix `A` satisfies `s3(A)>=s>0`, and an ORIGINAL-coordinate carrier `H`, `|H|=m>=6`, has a spectral-square lower carrier `lambda_6((A^2)[H,H])>=g^2`, then for `N=binom(m,2)`, `0<a<b/N`, `0<b<g`, `kappa=b/N-a`,

`||p_Q||inf <= max{ 2sqrt(6 pi m)/a, pi/kappa, 3*400^(1/3) kappa^(-5/6) s^(-1/6), 5sqrt(2e)/sqrt(g^2-b^2) }.`  (5)

The theorem is exhaustive and uses only original-coordinate conditioning / physical receivers. Continuity is not claimed for every exit.

Combining (4) at `k=6` with (5) yields an end-to-end compiler: any baseline carrier with `6+q_h` spectral-square reserve modes survives arbitrary signed high modes and a small dense low-mode remainder.

## Concrete exact-target inequality

Work on `R^16=H direct_sum J` with `|H|=|J|=8`, and let

`A0 = [[0,2 I8],[2 I8,0]].`

Thus `A0^2=4 I16`, so

`lambda_8((A0^2)[H,H])=4`.

Let `u=e_1` in the `H` bank and add the arbitrary signed rank-one mode

`S=tau u u^T`, `tau in R`,

with no restriction on `|tau|`. Since `A0 u=2 f_1` lies in the opposite bank,

`q=dim(span{u,A0u})=2`.

Finally add any real symmetric, globally dense `T` with

`||T||op<=1/4`.

Theorem 1 with `k=6` gives

`sqrt(lambda_6((A^2)[H,H])) >= 2-1/4=7/4`,

hence

`lambda_6((A^2)[H,H]) >= 49/16`  (6)

uniformly for every `tau`, including arbitrarily large positive or negative values.

The global target hypothesis is also preserved quantitatively. Since `rank(S)=1`, singular-value rank interlacing gives

`s3(A0+S) >= s4(A0)=2`.

The dense tail then gives

`s3(A) >= 2-1/4=7/4>1`.  (7)

So this is a literal family inside the exact owner target.

Now apply the completed partner theorem (5) with

`m=8`, `N=28`, `s=g=7/4`, `b=17/10`, `a=3/70`,

so

`kappa=b/N-a=1/56`.

The four exit constants are

`2sqrt(48 pi)/(3/70) = 573.0629564500...`,
`56 pi = 175.9291886010...`,
`3*400^(1/3)*56^(5/6)*(7/4)^(-1/6) = 576.4897627682...`,
`100 sqrt(2e)/sqrt(69) = 28.0696949817...`.

Therefore the actual final quadratic form obeys

`||p_Q||inf < 577`  (8)

for every independent cap-one product input, every `tau in R`, and every symmetric dense `T` with `||T||op<=1/4`.

This application is deliberately on the actual final matrix. No claim is made that `X^T T X` is small, independent, or convolved with a baseline law.

## What this resolves and what remains

Resolved: a general deterministic stability theorem for adding arbitrarily large signed low-rank spectral packets plus arbitrary-rank smaller signed packets. Large amplitudes cost only a Krylov footprint reserve `q_h`; the small packet costs only its operator threshold. The theorem is exact and coordinate-preserving.

Not resolved: the bare hypothesis `s3(A)>=1` does not itself provide a baseline with `6+q_h` physical spectral-square reserve modes. The remaining global implication is still structural: force such a reserve carrier for some original-coordinate set/threshold, or route its failure into one of the already-paid D5, ridge, grouped-bank/hub, physical-pair, rank-two-half-Riesz or Schur exits. This report does not claim the unrestricted conjecture or unrestricted continuity.

## Correction discipline

Consumed live corrections include the failure of uniform pointwise quadratic-phase decay, the failure of arbitrary-joint 3D coarea, the failure of positive conditional projection-density moments, the dimension loss of naive fiber-sup integration, and the loss of independence after spectral rotation. None is used as a premise here.

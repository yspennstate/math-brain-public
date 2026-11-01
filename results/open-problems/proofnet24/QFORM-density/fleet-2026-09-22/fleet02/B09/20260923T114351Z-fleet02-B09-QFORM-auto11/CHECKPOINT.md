# fleet02/B09 checkpoint — pivot plus grouped rank-two cross

Run: `20260923T114351Z-fleet02-B09-QFORM-auto11`

Status: substantive partial calculation; full QFORM remains open.

## First unpaid implication

After the now-paid grouped cross-rank-three branch, the immediate B09 debt is to spend a third source-compatible smoothing resource when a disjoint cross block has only rank two, without conditioning away arbitrary same-side curvature. A physical scalar pivot is one such third resource.

## Candidate theorem, with proof skeleton already closed

Let `k` be an original coordinate with `a=A_kk != 0`. Complete that physical square. The remaining quadratic matrix is the Schur complement

`S=A[-k,-k]-A[-k,k]A[k,-k]/a`.

Assume that for two disjoint original-coordinate banks `I,J` in the remaining coordinates the cross block `B=S[I,J]` has rank two, with nonzero singular values `sigma_1,sigma_2`, thin SVD `B=P Sigma R^T`, and `Delta_2=sigma_1 sigma_2`.

The grouped-cross Plancherel proof in fleet03/B09 r30 gives, before its rank `r>2` Fourier-inversion step, the rank-two characteristic-function estimate

`|phi_R(t)| <= min(1, K/|t|)`,

where

`K = pi [Bcal(P) Bcal(R)]^(1/2) Delta_2^(-1/2)`

and `Bcal(P),Bcal(R)` are the source-valid projection-density factors from the weighted affine-fiber theorem. All same-side quadratic blocks and affine terms remain inside complex amplitudes.

For any random variable `Z` with `|phi_Z(t)| <= min(1,K/|t|)`, Abel-regularized Fourier representation of the half-Riesz kernel yields

`sup_s E|Z-s|^(-1/2) <= sqrt(2/pi) int_0^infty t^(-1/2)|phi_Z(t)|dt`

`<= 4 sqrt(2/pi) sqrt(K)`.

Substituting `K` gives

`H_(1/2)(R) <= 4 sqrt(2) [Bcal(P)Bcal(R)]^(1/4) Delta_2^(-1/4)`.

The physical-square kernel after completing `X_k` obeys pointwise

`p_(Q | X_-k)(q) <= |a|^(-1/2)|q-R|^(-1/2)`

on its one-sided support. Averaging therefore gives the direct density estimate

`||p_Q||_infinity <= 4 sqrt(2) |a|^(-1/2) [Bcal(P)Bcal(R)]^(1/4) Delta_2^(-1/4)`.

Since the rank-two projection factors satisfy `Bcal(P),Bcal(R)<=e`, the universal corollary is

`||p_Q||_infinity <= 4 sqrt(2e) |a|^(-1/2) Delta_2^(-1/4)`.

The same coefficient multiplies every interval length. No probability squaring, post-rotation independence, support/moment assumption, or deletion of dense same-side curvature is used. Continuity is not asserted here.

## Required e5f source applied to an actual star

For one physical hub `X_0` and a leaf bank carrying three orthonormal flat source-coordinate projections `c,v_1,v_2`,

`F=2X_0<c,X_I> + <v_1,X_I>^2 + <v_2,X_I>^2`

has active spectrum `{1,-1,1,1}`. When each mixed-frame row has leverage at most `1/2`, Theorem H of `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives

`|phi_F(t)| <= 8 pi^2 |t|^(-2)`.

Hence integration of `min(1,8 pi^2/t^2)` gives

`||p_F||_infinity <= 4 sqrt(2)`

and `P(F in L)<=4 sqrt(2)|L|`. The two dense same-side leaf squares are retained; the three leaf projections are never declared independent.

## Still unpaid

The bare hypothesis `s_3(A)>=1` does not yet force either a quantitative physical pivot plus grouped rank-two Schur cross product, a grouped cross-rank-three exit, or another already-paid branch. The structural routing remains open.

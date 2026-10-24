# Aggregate rank-one physical bank corollary

This is an additional theorem in run `account01-B16-20260922T161036Z-r11`. It applies the translated-bank Frostman smoother to an exact-rank-three frame and converts an entire diffuse family of physical third minors into one aggregate quadratic coefficient matrix before reciprocal payment.

## Setup

Let

`A=R Lambda R^T`, `R^TR=I_3`,

with `Lambda` an invertible symmetric `3x3` matrix, and let `r_k` be the physical rows of `R`. Fix two physical indices `i,j`. Let `T` be a set disjoint from `{i,j}` such that the spectral rows in `T` are all collinear:

`r_k=c_k v`, `k in T`,

for one unit vector `v in R^3`. Put

`rho=sum_{k in T} c_k^2>0`,
`L_T=rho^(-1/2) sum_{k in T} c_k X_k`,
`w=sqrt(rho) v`.

By the source-transferred Rudelson--Vershynin projection theorem,

`||p_{L_T}||_infinity <= sqrt(2)`.

Condition on every original coordinate outside `{i,j} union T`. Since

`sum_{k in T} r_kX_k = w L_T`,

the remaining random quadratic polynomial is, up to conditioned linear and constant terms,

`[X_i,X_j,L_T]^T M [X_i,X_j,L_T]`,

where

`M=U^T Lambda U`, `U=[r_i r_j w]`.

Thus `X_i,X_j,L_T` are independent, with density caps `1,1,sqrt(2)`.

## Determinant aggregation identity

For every `k in T`,

`det A_{ {i,j,k} }=det(Lambda) det(r_i,r_j,r_k)^2
                  =det(Lambda)c_k^2 det(r_i,r_j,v)^2`.

All nonzero terms have the same sign. Hence

`sum_{k in T}|det A_{ {i,j,k} }|
 =|det Lambda| rho det(r_i,r_j,v)^2`.

On the other hand,

`det M=det Lambda * det(U)^2
     =det Lambda * rho det(r_i,r_j,v)^2`.

Therefore

`boxed(
 |det M|=sum_{k in T}|det A_{ {i,j,k} }|.
 )`                                                               (A.1)

So the determinant of the **aggregate bank triple** is exactly the total physical third-minor mass through that rank-one bank. No largest atom is selected.

## Nonlinear density theorem

Write

`M=[[B,c],[c^T,gamma]]`,

where the final coordinate is `L_T`. Assume `gamma!=0` and the two-dimensional Schur complement

`S=B-cc^T/gamma`

is nondegenerate indefinite. By Sylvester's determinant identity,

`det M=gamma det S`.

Complete the bank square:

`[x,L]^T M[x,L]
 = gamma[L+gamma^(-1)c^Tx]^2+x^TSx`,

up to the conditioned affine terms. The main run theorem `QFORM-TRANSLATED-BANK-FROSTMAN-SMOOTHER-v1`, using the completed account02/B16 binary Frostman result and the cap `sqrt(2)` for `L_T`, gives

`||p_Q||_infinity
 <= sqrt(2) C_ind |gamma|^(-1/2)|det S|^(-1/4)`

and therefore

`boxed(
 ||p_Q||_infinity
 <= sqrt(2) C_ind (|gamma det M|)^(-1/4)
 = sqrt(2) C_ind
   ( |gamma| sum_{k in T}|det A_{ {i,j,k} }| )^(-1/4).
 )`                                                               (A.2)

Here

`C_ind=8*3^(3/4)*5^(1/4)/sqrt(e)=16.53964516612327...`.

The bound is uniform in all conditioned outside coordinates, so averaging proves the ambient bound. Arbitrary outside couplings are permitted; they only create conditioned affine terms in the three active aggregate variables.

## Interpretation

Equation (A.2) is a genuine diffuse-bank aggregation statement. If a rank-one physical bank contains `m` atoms of comparable size, each local third minor may be `O(1/m)`, yet only the **sum** of their determinant masses enters the final density estimate. This directly avoids the reciprocal-local-minor divergence.

The theorem is more general than a coordinate-disjoint eigenbank: the common spectral direction `v` may have components in all three spectral axes. What is required is exact rank-one structure of the physical row bank, so that the original independent coordinates in `T` enter the spectral projection through one scalar innovation `L_T`.

It does not close the arbitrary overlapping-frame case. When the rows in a diffuse bank span dimension two or three, the bank no longer supplies one independent scalar innovation after the residual is formed, and the live conditional-cap/projection-trace corrections prevent replacing it by a generic marginal-density argument.

**Status:** proved supporting theorem; full QFORM target remains open; continuity not claimed.

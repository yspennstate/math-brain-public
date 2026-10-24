# account02/B18 r27 — early mathematical checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## First unpaid implication attacked

The preceding account02/B18 r26 left the exact-rank-three Schur-isotropic nonplanar survivor

`Q=(Y+r n X_0)^T D(Y+r n X_0)`, `Y=V^T X_R`, `V^T V=I_3`, `n^T Dn=0`,

with the single-cut volume theorem intrinsically losing `(1+r^2)^(1/6)`. This run tests the pinned e5f mixed-Fresnel theorem as a different whole-line mechanism and checks it against the circular full-spark stress family.

## Source transfer already obtained

Pinned source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem MF. For one genuine physical hub `H={0}` and a residual decomposition

`A_LL = Delta + S diag(lambda_1,lambda_2) S^T`, `S^T S=I_2`, `Delta` diagonal,

put `c=A_L0`, rows `w_l=(c_l,s(l))`, and `Gamma=sum_l w_l w_l^T`. If `Gamma` is invertible and every augmented leverage obeys `w_l^T Gamma^{-1}w_l<=1/2`, Theorem MF gives

`|phi(t)| <= 8 pi^2 |t|^-2 (|lambda_1 lambda_2| det Gamma)^-1/2`.

Integrating `min(1,K|t|^-2)` exactly gives the target-level compiler

`||p_Q||_infinity <= 4 sqrt(2) (|lambda_1 lambda_2| det Gamma)^(-1/4)`.

Arbitrary hub self-term, diagonal twist and affine terms are allowed by the source theorem; no post-rotation independence is used.

## New obstruction calculation

For the finite-shear circular family from the preceding B18 work, let `V` be the `m x 3` circular Parseval frame, `m>=9`, whose every three rows are independent, and let

`R_t=V D_t V^T`, `D_t=[[0,t,0],[t,0,0],[0,0,1]]`, `t>0`.

Then `rank R_t=3`, and every physical `3x3` principal minor is nonzero:

`det R_t[T,T]=det(V_T)^2 det(D_t) !=0` for every `|T|=3`.

If `Delta` is diagonal and `rank(R_t-Delta)<=3`, then necessarily `Delta=0`. Indeed `rank Delta<=rank R_t+rank(R_t-Delta)<=6`, so its support has at most six indices; since `m>=9`, choose three indices `T` off that support. For any supported index `i`, both `R_t` and `R_t-Delta` have rank at most three, hence the determinant of their principal block on `{i} union T` is zero. The two blocks differ only in the `(i,i)` entry, so multilinearity in that entry gives

`0 = - Delta_ii det R_t[T,T]`,

forcing `Delta_ii=0`, a contradiction. Thus the diagonal twist is unique.

Consequently every rank-at-most-three Theorem-MF decomposition of the circular residual block has `Delta=0` and rank exactly three. Its low-rank span is `Ran(V)`. The physical hub column is `c=k V e_2` (equivalently a nonzero scalar multiple of `R_t V e_1`) and therefore belongs to that same span. Hence the augmented feature matrix `[c,S]` has rank three rather than four and `Gamma` is singular. The exact source hypothesis of Theorem MF fails.

This is a new mechanism-level obstruction: the natural low-rank mixed-Fresnel transfer cannot pay finite shear in the full-spark circular family, even though it does pay genuine hub-plus-rank-two branches. It is not a counterexample to QFORM. The remaining work is to combine this with the designated account03/B18 two-plane theorem quantitatively and determine whether a higher-rank diagonal twist can escape the obstruction without losing a universal coefficient currency.

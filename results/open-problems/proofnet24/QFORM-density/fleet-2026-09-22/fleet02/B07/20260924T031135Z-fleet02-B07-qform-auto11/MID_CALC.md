# Mid calculation — sharper E2/E3 router and reciprocal-fan regression

## 1. A sharper spectral router than the early exterior-square estimate

Let the squared singular values of the literal r44 crossing `K` be

`x1>=x2>=...>=0`,

and write

`Z=e2(x)>=zeta`, `W=e3(x)<theta`, `tau=sum_{j>=3} xj`, `R=e2(x3,x4,...)`.

The already-completed fleet02/B07 compound inequality used by partner r44 is

`tau Z <= 3 W`,

so

`tau <= 3 theta/zeta`.                                             (1)

There is also the exact decomposition

`Z = x1 x2 + (x1+x2) tau + R`,                                    (2)

with

`R<=tau^2/2`.                                                       (3)

Fix `a in (0,1)`.  If

`(3 theta/zeta)^2 <= a zeta`,                                     (4)

then (1)-(3) give `R<=a zeta/2`.  Hence either

`x1 x2 >= (1-a) zeta`,                                             (5)

or, using `x2<=x1`,

`zeta <= Z < (1-a)zeta + 2 x1 tau + a zeta/2`,

so

`x1 tau > a zeta/4` and therefore

`boxed: s1(K) > zeta sqrt(a)/(sqrt(12 theta)).`                    (6)

Thus no determinant is selected: the complete E2 packet either survives in the top-two singular carrier or forces a quantitatively huge first singular value.

For partner r44, `zeta=2^-12`, `theta=(2C3/rho)^6`, `C3=3*2^(4/3)*e^(1/3)`.  Taking `a=1/2`, condition (4) already holds for `rho>=214.776`, hence in the live high-ratio chamber.  We obtain

`boxed: s1(K)s2(K) >= 1/(64 sqrt(2))`

or

`boxed: s1(K) > c_* rho^3`,

where

`c_* = 2^-12/[sqrt(24)(2C3)^3]`
`    = 5.30476580567e-9`.                                          (7)

This strengthens the early `1/128` / `1.326e-9 rho^3` alternative and uses only the actual singular compounds of `K`.

## 2. Exact reciprocal fan: vanishing Frobenius tail can carry asymptotically all E2 mass

Take `n=2^r>=2`, `M=n^4`.  Let `u_0,...,u_{n^2}` and `v_0,...,v_{n^2}` be columns of normalized Walsh-Hadamard matrices on two disjoint physical banks of size `M`.  Put

`K_n = n u_0 v_0^T + n^-2 sum_{a=1}^{n^2} u_a v_a^T`.              (8)

Its singular values are

`n, n^-2 (multiplicity n^2)`.

Therefore

`E2(K_n)=1+(n^2-1)/(2 n^6)`,                                      (9)

`E3(K_n)=(n^2-1)/(2 n^4)+(n^2-1)(n^2-2)/(6 n^10)`,               (10)

so `E2(K_n)->1` while `E3(K_n)~(2n^2)^-1`.

Let `K_{n,0}` be the top-two SVD truncation.  Then

`E2(K_{n,0})=n^-2`,                                                (11)

and

`||K_n-K_{n,0}||_F^2=(n^2-1)/n^4 ->0`.                            (12)

Thus asymptotically all of the second determinant-volume packet is carried by wedge interactions between the huge `n` direction and singular directions lying in a Frobenius-vanishing tail.  A receiver may not infer that r44's small coefficient residual is negligible at compound level.  The cubic-spike exponent in (7) is the correct deterministic scale: making (10) of order `rho^-6` requires `n` of order `rho^3`.

Every physical coefficient obeys

`|(K_n)_{ij}| <= n/M + n^2*n^-2/M = n^-3+n^-4`.                   (13)

Hence the geometry is fully diffuse in ORIGINAL coordinates.

## 3. Full-target, all-small-entry regression paid by the pinned e5 source

Add a disjoint physical star bank: one hub `h` and `P=n^6` leaves, with flat star vector `g=(1/sqrt P,...,1/sqrt P)`.  Define the full symmetric coefficient matrix by the two independent blocks

`A_star=[[0,g^T],[g,0]]`,

`A_cross=[[0,K_n],[K_n^T,0]]`,

and no coupling between them.

The nonzero spectrum is exactly

`{+n,-n,+1,-1,+n^-2 (n^2 times),-n^-2 (n^2 times)}`.              (14)

So this is an exact owner-target family, with four eigenvalues of modulus at least one.  By (13) and `|g_l|=n^-3`, every physical entry is at most `n^-3+n^-4`; consequently, for every fixed cardinality `L`,

`sup_{|C|<=L} ||A_n[C,C]||_op <= L(n^-3+n^-4) ->0`.               (15)

Thus no bounded-cardinality physical spectral core exists.

This is not a QFORM counterexample.  Apply two completed results from the mandatory pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

First, its `D_k` extension with `k=2,q=2`, on the literal crossing `K_n`, gives

`|phi_cross(t)| <= min(1,B |t|^-1/2)`,

`B=(2e pi^2)^(1/4) E2(K_n)^(-1/8) <= (2e pi^2)^(1/4)`.            (16)

Second, its completed hub theorem H applied to the literal star gives

`|phi_star(t)| <= min(1,2pi/|t|)`.                                (17)

The two coordinate blocks are independent, so their characteristic functions multiply.  Put `B0=(2e pi^2)^(1/4)`, so `B0^2=pi sqrt(2e)>2pi`.  Direct integration gives

`int_0^infinity min(1,2pi/t) min(1,B0 t^-1/2) dt`
` = 2pi + 2pi log(B0^2/(2pi)) + 4pi`.

Fourier inversion therefore yields the dimension-free exact cap

`boxed: ||p_{X^T A_n X}||_infinity <= 7-log 2 = 6.30685281944... .` (18)

In fact the product characteristic function is integrable, so this particular regression family has a continuous `C_0` density.  This does not settle continuity or height for the unrestricted target.

The family (8),(14) is the mandatory regression for the next receiver: it simultaneously has constant aggregate E2, vanishing E3, vanishing rank-two Frobenius residual, no bounded coordinate core, all physical coefficients tending to zero, and order-one determinant volume outside the rank-two carrier; nevertheless the pinned product-law Fourier mechanisms pay it uniformly.

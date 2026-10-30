# Nine-eigenvalue QFORM density bound with constant 342

Run: 20260924T183756Z-fleet03-B13-fixedmult-r7

Status: proved replacement argument; independent review pending. Full three-eigenvalue problem remains open.

Sources: standalone nine-eigenvalue proof yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f, path proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex. Partner input: fleet04/B13 at commit 0d1dd8180db0e205cab284c51b178af425e5c7f1, path proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet04/B13/20260924T181443Z-fleet04-B13-hyperbolic-envelope-r3/INDEFINITE_PAIR_274.md.

## Claim
For independent coordinate densities <=K, symmetric A with s_9(A)>=s>0, and arbitrary affine terms,
||p||_infinity < 342 K^2/s.
Global continuity is not claimed.

Normalize K=s=1. Set d=2/35, p=1/400, h=13/148, kappa=h^2. In the no-pivot case,
|A_ij|^2<p+d^2=113/19600.
Let q*=789/10360. Then
q*^2-(p+d^2)=3733/107329600>0,
so |A_ij|<q*. The interpolation proof needs
1-d-q*-4h=5339/10360>0
and
1-d-2q*-9h=0.
The second is strict for the actual matrix because |A_ij|<q*. Also d+h<1. Hence the source proof still gives
s_(4k-3)(A)>=1 and no pivot => V_k(A)>=h^(2k), k<=3.

For k=3, random cutting yields Z_3>=4^-3 h^6. With source constant C_3<15,
||p_Q||_infinity < 15 Z_3^-1/6 <=30/h=4440/13<342.
For k=2, the no-pivot five-direction half potential is <14 sqrt(2/h).

## Optimized scalar-scalar branch
Suppose the five-direction remainder has a scalar pivot |b|>=d. Its scalar square profile leaves a Schur remainder T with quadratic operator norm at least one, so
P(|T-a|<rho)<=min(1,5 rho^(1/4)).
For any cutoff delta,
E|R-a|^-1/2 <= delta^-1/2
+d^-1/2 [J0+2 E log_+(delta/|T-a|)],
J0=pi+4 log2.
This follows from
integral_{-delta}^{delta} |x|^-1/2 |x-u|^-1/2 dx = J(u/delta)
and J(v)<=J0+2 log_+(1/|v|).

Choose delta=d/16=1/280. Since delta>1/625,
E log_+(delta/|T-a|)
<= integral_0^infinity min(1,5 delta^(1/4)e^-u/4) du
=4+4 log5+log delta.
After the outer scalar pivot contributes another d^-1/2, the density is at most
d^-1 [12+pi+2 log(125/14)].
Use pi<22/7 and log(125/14)<219/100. The latter follows from
sum_{k=0}^8 (219/100)^k/k!
=400115557267268281849/44800000000000000000
>125/14.
Therefore this branch is
< (35/2)(12+22/7+219/50)=6833/20=341.65<342.

Other scalar branches are smaller:
d^-1/2 *14 sqrt(2/h)=279.47...<342,
and
d^-1/2 *16 p^-1/4=16 sqrt(350)=299.34...<342.

A definite pair gives ||p_Q||_infinity<=pi p^-1/2=20pi<63.

For an indefinite pair, p is unchanged at 1/400. Its Schur complement retains at least seven unit-scale spectral directions, so the completed fleet04/B13 theorem applies:
||p_Q||_infinity <=20(8+log(1444/5))<274<342.

These alternatives exhaust the source pivot/no-pivot architecture, proving the normalized bound <342. Scaling Y=KX and A by 1/s gives <342 K^2/s.

This improves the fixed-multiplicity constant but does not lower the supported multiplicity below nine, does not prove the unrestricted three-large-eigenvalue conjecture, and does not establish global continuity. No support, moment, Gaussian, log-concavity, or diagonal-basis assumption is introduced.

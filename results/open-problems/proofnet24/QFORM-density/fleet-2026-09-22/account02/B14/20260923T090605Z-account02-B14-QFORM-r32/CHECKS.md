# QFORM B14 r32 checks

Run: `20260923T090605Z-account02-B14-QFORM-r32`.

These are checks of constants/algebra in `REPORT.md`; they are not numerical evidence for the full conjecture.

1. Squared-sinc constants:

`m0=(sin(1/2)/(1/2))^2 = 0.9193953882637206`.

`c_E=2/m0 = 2.1753426496700214`.

`2 c_E = 1/sin^2(1/2) = 4.350685299340043`.

2. Claude-F rank-two specialization:

`K_F=4*pi/sqrt(P)`.

At the explicit choice `y=1`,

`4 sqrt(K_F/kappa)=8 sqrt(pi) kappa^(-1/2) P^(-1/4)`,

with `8 sqrt(pi)=14.179630807244127`.

For `D=kappa=P=1`, the resulting report bound is

`8 sqrt(pi)+1/sin^2(1/2)=18.53031610658417`.

3. Critical product witness:

For independent `X,Y ~ Uniform[-1/2,1/2]` and `R=2XY`, direct change of variables gives

`p_R(r)=log(1/(2|r|)) 1_{|r|<1/2}`.

Its squared L2 norm is exactly

`2 int_0^(1/2) log^2(1/(2r)) dr = int_0^1 log^2(1/u)du = 2`.

The characteristic function is

`phi_R(t)=2 Si(t/2)/t`,

so `t phi_R(t) -> pi` as `t -> +infinity`; hence `phi_R` is not in L1. For two independent copies, `||p_R*p_R||_infinity <= ||p_R||_2^2=2`.

4. Kernel-leakage stress spectrum:

For mutually orthonormal `a,b,c`, the homogeneous matrix of

`2U1U2+(a^T V)^2+(b^T V)^2+2 gamma(c^T V)Z`

splits into orthogonal blocks with eigenvalues `+1,-1`, `+1`, `+1`, and `+gamma,-gamma`; remaining eigenvalues are zero. Thus at least four eigenvalues have modulus one for every real `gamma`, while conditioning on `Z=z` creates affine bank term `2 gamma z c` in the kernel of `aa^T+bb^T`.

5. Layer-cake tail integral:

For `y<=1`,

`int_0^infinity y e^(-s)[1+log(1/y)+s] ds = y[2+log(1/y)]`.

For `y>=1`, splitting at `s=log y` gives

`log y + int_0^infinity e^(-u)(1+u)du = log y+2`.

Multiplying the tail by `c_E` yields the `Omega` function in the report.

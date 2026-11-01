# Scalar-conditioned projection-height no-go for every positive moment

This supplements r13 by strengthening the assigned partner fleet02/B15 r6 obstruction. The partner proved divergence at exponent `2/3`; the same fixed target and fragmented product source in fact destroy **every positive moment** of the scalar-conditioned three-dimensional projection-density height.

## Setup

Use the exact fleet02/B15 r6 construction. Let

`H=(1/2)[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]`

and

`A=H diag(1,2,-3,1/2) H^T`.

For each integer `M>=1`, put

`E_M=union_{j=1}^M [10j,10j+1/M]`,

and take independent physical-coordinate densities

`f_1=1_(E_M)`, `f_2=f_3=f_4=1_[0,1]`.

Let `Y=H^T X` and `Q'=Y_4^2/2`. The construction has `Y_4>0`, so conditioning on `Q'` is equivalent to conditioning on `Y_4`.

Write `p_4` for the density of `Y_4`. The M packets are disjoint and

`p_4(s)=(1/M) sum_{j=1}^M g_M(s-a_j)`,

where the translates have pairwise disjoint supports, `g_M` is a probability density, and

`||g_M||_infinity<=2`.

Because the orthogonal spectral transform preserves the unit indicator source density, for almost every `s` with `p_4(s)>0` the conditional density of `(Y_1,Y_2,Y_3)` is uniform on the corresponding section and has height

`H_M(s):=||rho_(123|Y4=s)||_infinity=1/p_4(s)`.

## Theorem — every positive moment diverges

For every fixed `beta>0`,

`E[ ||rho_(123|Q')||_infinity^beta ] >= (M/2)^beta`.

Hence no inequality

`E[ ||rho_(123|Q')||_infinity^beta ] <= C_beta`

can hold uniformly over target instances for **any** positive exponent `beta`.

### Proof

Since conditioning on `Q'` and on `Y_4` are equivalent here,

`E H_M(Y_4)^beta`
` = int_{p_4>0} p_4(s)^(1-beta) ds`.

The packet supports are disjoint, so

`int p_4^(1-beta)`
` = M * (1/M)^(1-beta) * int_{g_M>0} g_M(u)^(1-beta) du`
` = M^beta J_beta(g_M)`.

It remains to bound `J_beta` below uniformly.

If `0<beta<1`, then `g_M<=2` implies on `{g_M>0}`

`g_M^(1-beta)=g_M*g_M^(-beta) >= 2^(-beta) g_M`,

so

`J_beta(g_M)>=2^(-beta)`.

If `beta=1`, then

`J_1(g_M)=|{g_M>0}|>=1/||g_M||_infinity>=1/2=2^(-1)`.

If `beta>1`, then `1-beta<0`, hence `g_M<=2` gives

`g_M^(1-beta)>=2^(1-beta)`

on its support. Again the support has measure at least `1/2`, so

`J_beta(g_M)>=2^(1-beta)/2=2^(-beta)`.

Thus in every case

`E H_M(Y_4)^beta >= M^beta 2^(-beta)=(M/2)^beta`.

QED.

## Consequence for the full QFORM proof search

This is an intermediate-mechanism obstruction, **not** a QFORM counterexample. The target matrix `A` is fixed, invertible, simple-spectrum and has exactly three eigenvalues of modulus at least one. By the completed fleet02/B15 fixed-matrix theorem its actual quadratic output has a finite density-height bound independent of `M`; by the completed fleet02/B15 r3 theorem it even has a continuous density for every `M`.

Therefore no proof of the universal QFORM height can proceed by replacing the translated scalar mixture

`p_Q(t)=int p_(Q')(b) p_(Q3|Q'=b)(t-b) db`

with a universal positive moment of the scalar-conditioned projection-density height. The failure is not special to the scaling exponent `2/3`; **all positive exponents fail**. Any surviving route must retain output translation/overlap or work directly with the pre-normalized joint profile / product-source graph trace.

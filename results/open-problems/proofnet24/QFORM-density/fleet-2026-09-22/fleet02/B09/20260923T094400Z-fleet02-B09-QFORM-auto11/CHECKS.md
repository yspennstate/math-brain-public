# Deterministic checks for fleet02/B09 20260923T094400Z

## Exact spectrum of the obstruction family

In the grouped orthonormal basis `(e_h1,a,e_h2,e_s,c)`,

`A_k = [[k^-1,k],[k,0]] direct_sum [[0,k^-1],[k^-1,0]] direct_sum [1]`.

Therefore

`spec(A_k) = { (k^-1+sqrt(k^-2+4k^2))/2,
                (k^-1-sqrt(k^-2+4k^2))/2,
                k^-1,-k^-1,1 }`.

For `k>=2`, the first positive eigenvalue is `>=k`, while

`|(k^-1-sqrt(k^-2+4k^2))/2|
 = (sqrt(k^-2+4k^2)-k^-1)/2
 >= k-(2k)^-1 >=7/4`.

Hence at least three eigenvalues have modulus at least one.

## Physical-scale check

With `m=k^4`, every nonzero physical coefficient belongs to

`{k^-1, k/sqrt(m), k^-1, 1/m}={k^-1,k^-1,k^-1,k^-4}`.

Thus `max_ij |A_ij|=k^-1`. Any physical `3x3` principal block has maximum absolute row sum at most `3/k`, hence operator norm at most `3/k`. Every physical pair determinant has magnitude at most `k^-2`.

## Cross-frame / partner-collision check

The two hub-to-leaf columns are `u=k a`, `v=k^-1 e_s`, so

`G=[[k^2,0],[0,k^-2]]`, `det G=1`.

Whitening gives `U=[a,e_s]`. The only positive Pluecker weights are

`w_{j,s}=1/m`, `j in I_a`.

Thus every basis contains `s` and `rho=0`. The leverage vector is

`ell_s=1`, `ell_j=1/m` for `j in I_a`, all others zero.

The fleet03/B09 r26 identity evaluates to

`1-sum ell_i^2+sum w_ij^2
 =1-(1+1/m)+m*(1/m^2)=0`,

exactly as required.

The physical hub core is `diag(k^-1,0)`. In the rank-one notation `sigma=k^-1`, `n=e_h2`, and `||Hn||=k^-1`, so the reciprocal resource is

`|sigma| ||Hn||=k^-2 ->0`.

## Mixed-hub constant check

For the newest-Claude Theorem H partition, use physical hub `h_1`, leaf bank `I_a union I_c`, curvature coefficient `lambda=1`, curvature vector `c`, and hub coupling `k a`. Then

`det G_H=k^2`, and the normalized augmented rows have leverage `1/m<=1/2`.

Theorem H gives

`|phi(t)| <= (2|t|)^-1 (4pi|t|)^-1/2 (4pi)^2 k^-1
           =4 pi^(3/2) k^-1 |t|^-3/2`.

For `A=4pi^(3/2)k^-1`,

`int_R min(1,A|t|^-3/2)dt =6 A^(2/3)`.

Fourier inversion therefore gives

`||p||_infinity <= (1/(2pi))*6*(4pi^(3/2)/k)^(2/3)
                  =3*2^(4/3) k^(-2/3)`.

No stochastic simulation is used in these checks.

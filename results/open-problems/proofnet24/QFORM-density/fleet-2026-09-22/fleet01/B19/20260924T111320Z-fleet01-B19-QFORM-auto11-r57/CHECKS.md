# Checks for fleet01/B19 r57

Status: analytic checks PASSED on the stated scopes; no full-QFORM claim.

## 1. Exact constants

For the rank-12 branch,

`delta_12=3/16+2^-16=12289/65536=0.1875152587890625`.

Hence

`1/2-delta_12=20479/65536=0.3124847412109375`,

`1/4-delta_12=4095/65536=0.0624847412109375`.

The fixed-core bound at `m=15` is

`250*15*(8+log 15)/(20479/65536)=128502.8769...<128503`.

For the determinant-collapse branch,

`delta_11=3/16+2^-16+112*2^-20=1537/8192=0.1876220703125`,

so

`1/2-delta_11=2559/8192=0.3123779296875`,

`1/4-delta_11=511/8192=0.0623779296875`,

and at `m=14`

`250*14*(8+log 14)/(2559/8192)=119204.0061...<119205`.

The rank-12 finite hub has `h<=14`, so a crossing with `||C||op>=1/4` gives a physical row star at least

`1/(4 sqrt(14))=0.066815310478...`.

The finite-hub principal-core payment at scale `1/64`, `h=14`, is

`64*250*14*(8+log 14)=2383148.84...<2383149`.

## 2. Rank-perturbation inequality

For matrices of equal size and `rank E<=r`, singular-value Weyl gives

`s_(j+r)(B)<=s_j(B+E)+s_(r+1)(-E)=s_j(B+E)`.

Thus the report's use

`s_3(D_S+F_S+K_S)>=s_(r+3)(D_S+F_S)`

is valid without a sign assumption.

## 3. Finite-hub block perturbation

For

`E=[[0,C],[C^T,0]]`,

`E^2=diag(CC^T,C^TC)`, hence `||E||op=||C||op` exactly. Therefore

`s_3(diag(A_HH,A_LL))>=s_3(A)-||C||op>3/4`

under `s_3(A)>=1`, `||C||op<1/4`.

If `s_3(A_HH)<1/64`, at most two hub singular values can be at least `3/4`. Hence the light block contributes at least `3-m_H` singular values at least `3/4`.

## 4. Aligned-tail partner application

Section 4 is interpreted with `k=rank(K_LL+F_LL)` and `W` chosen with exactly `k` orthonormal columns spanning that range; then `H_0` is invertible on coefficient space and `pdet(H_0)=det(H_0)` up to sign. This is the exact form required by fleet02/B19 r14.

When `m_H=0` and `||C||op<1/4`, `s_3(A_LL)>=3/4`. Since `||D_L||op<1/2`,

`s_3(W H_0 W^T)>=1/4`.

For exact rank three this yields `|pdet H_0|>=1/64` and partner constant

`12*(1/64)^(-1/3)=48`.

For `4<=k<=12`, `|pdet H_0|>=2^-120` yields

`[4k/(k-2)] |pdet H_0|^-1/k <=8*2^30=8589934592`.

If instead `|pdet H_0|<2^-120`, then with nonzero singular values `s_1>=...>=s_k>0`,

`s_k^k<=prod_j s_j=|pdet H_0|<2^-120`,

so `s_k<2^(-120/k)<=2^-10` because `k<=12`.

This is only a deterministic near-rank-drop statement. No coefficient is deleted.

## 5. Correction checks

- No spectral rotation of random variables.
- No arbitrary joint-density coarea step.
- No pointwise law-uniform oscillatory decay.
- No conditional density-cap inheritance.
- No claim that `||F||op<0.188` makes `X^T F X` probabilistically small.
- No replacement of the near-rank-drop state by exact rank drop.
- Continuity is claimed only on the fleet02/B19 Fresnel branch; not on the generic fixed-core branch.

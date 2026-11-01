# fleet02/B20 early calculation — aggregate E3 payment in the diffuse D2 branch

Programme `QFORM-DENSITY-3EIG-20260922`.

Retain the literal physical pair `T={t1,t2}` and light bank `L` from the preceding B20 state. Put `M=A[T,L]`, `G=MM^T`, `S^2=det G`, with

`S>S0:=1/(480 sqrt(7626))`.

In the diffuse branch set `ell_j=m_j^T G^{-1}m_j<=3/4`. For `I_j=L\{j}`, let

`d_j=dist(A[I_j,j], col(M[:,I_j]^T))`

and define

`Zagg=sum_j S^2(1-ell_j)d_j^2`.

The exact Gram determinant identity is

`e_3(A[I_j,T union {j}] A[I_j,T union {j}]^T)=S^2(1-ell_j)d_j^2`.

Randomly put each light coordinate into `I` with probability `3/4` and `J` with probability `1/4`. Restricting the Cauchy--Binet sum for `e_3(A[I,T union J]A[I,T union J]^T)` to column triples `T union {j}`, every local squared 3x3 minor survives with probability `(1/4)(3/4)^3=27/256`. Hence some literal physical split satisfies

`Z3:=e_3(A[I,T union J]A[I,T union J]^T) >= (27/256) Zagg`.

Therefore the completed marginal-free physical `Z3` receiver gives, whenever `Zagg>=2^-50`,

`||p_Q||_infty <= C3 (27*2^-58)^(-1/6)`

with `C3=3*2^(4/3)e^(1/3)`, i.e.

`||p_Q||_infty <= 2048 sqrt(3) e^(1/3) <4950.573`.

On the complementary branch `Zagg<2^-50`, normalize `V=G^-1/2 M`, so `VV^T=I_2`. A tight-frame least-squares symmetrization gives

`A[L,L]=Delta+V^T K V+E`,

where `Delta` is physical diagonal, `K=K^T` is 2x2, `E=E^T` has zero diagonal, and

`||E||op <= sqrt(22) (sum_j d_j^2)^(1/2)
          <=2 sqrt(22) sqrt(Zagg)/S
          <2 sqrt(22) 2^-25/S0
          =0.0117187444121 <3/256`.

This nonzero tail is retained. Combining with fleet03/B20 r39's exact global representation

`A=diag(0_H,A[L,L])+K6+E39`, `rank K6<=6`,
`||E39||op<epsilon_H+1/64`, `epsilon_H=(3+122sqrt(10))2^-20<1/2048`,

gives

`A=diag(0_H,Delta)+K8+E*`, `rank K8<=8`, `||E*||op<1/32`,

and hence `s3(diag(0_H,Delta)+K8)>31/32` by Weyl. The coefficient error is not discarded as a random perturbation.

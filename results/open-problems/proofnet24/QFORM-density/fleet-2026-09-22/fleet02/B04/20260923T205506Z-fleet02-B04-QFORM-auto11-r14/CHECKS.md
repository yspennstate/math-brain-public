# Deterministic checks for fleet02/B04 r14

The following symbolic/numeric checks were executed in the current invocation with exact SymPy arithmetic before publication.

For

`U=2^(-1/2)[[1,1],[1,-1]]`,

`V=(1/3)[[2,1],[2,-2],[1,2]]`,

`M=U diag(L,1) V^T`,

SymPy returned

`M=(sqrt(2)/6)[[2L+1, 2L-2, L+2],[2L-1,2L+2,L-2]]`.

The three `2x2` determinants are exactly

`[2L/3, -L/3, -2L/3]`,

so their squared sum is `L^2` and the canonical weights are `(4/9,1/9,4/9)`.

For `A=[[0_2,M],[M^T,0_3]]`, exhaustive exact enumeration over all ordered pairs of physical `3`-subsets gave

`(C0,C1,C2,C3) = (0, (16/27)L^2(L^2+1), (38/27)L^2(L^2+1), 0)`.

The overlap-one anchored masses were

`[(8/27)L^2(L^2+L+1), (8/27)L^2(L^2-L+1), 0,0,0]`.

The number of nonzero ordered compound minors by overlap size was

`[0,12,24,0]`.

At `L=9`, the executed numeric audit returned

`receiver = sqrt(2*pi)/3 = 0.8355427582103334`,

`partner_phi_coeff = pi*2^(7/4)/3 = 3.5223386674547488`,

`partner_L2_squared = 2^(11/4)/3 = 2.242390440676572`,

`partner_half_Riesz = 8*2^(3/8)/sqrt(3) = 5.989845327788119`,

`C1=3936`, `C2=9348`, `C11=2184`, `C12=1752`.

Independent spectral check: since `U,V` have orthonormal columns, the singular values of `M` are exactly `(L,1)` and the eigenvalues of `A` are exactly `(L,1,0,-1,-L)`.

These checks are finite verification of the displayed algebra; the proofs in `REPORT.md` do not depend on floating-point numerics.

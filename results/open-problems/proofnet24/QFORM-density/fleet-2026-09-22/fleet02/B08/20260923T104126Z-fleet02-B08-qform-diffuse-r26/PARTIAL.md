# fleet02/B08 r26 — early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`, full target OPEN.

The first unpaid implication after r25 is the mixed `k=1` state: two actual cross directions at the physical gate plus one actual child eigendirection, under arbitrary complementary spectrum. The newest fleet03/B08 scalar-Schur theorem gives a full-ambient Linfinity receiver once a physical scalar pivot leaves residual physical E2. Two facts sharpen this state.

## A. General scalar-Schur two-cross router

Separate one ORIGINAL coordinate and two disjoint residual banks. Write the pivot coefficient `a!=0`, pivot-to-bank coupling vectors `u,v`, and the pre-Schur cross block `B`. The exact Schur cross block is

`M=B-u v^T/a`.

Put `r=||u||_2 ||v||_2/|a|`. Weyl gives

`s_2(M)>=s_2(B)-r`.

Hence, if `s_2(B)>r`, then

`E_2(M)>=s_1(M)^2 s_2(M)^2>= [s_2(B)-r]^4`.

Applying fleet03/B08 `QFORM-SCALAR-SCHUR-E2-LINF-v1` yields the full-ambient estimate

`||p_Q||_infinity <36.45 [ |a| (s_2(B)-r) ]^(-1/2)`.

In particular, at the actual hybrid gate `s_2(B)>=beta L`, if `|a|>=alpha L` and `r<=beta L/2`, then

`||p_Q||_infinity <36.45 sqrt(2/(alpha beta)) L^(-1)`.

Thus a localized scalar pivot is paid unless its rank-one Schur update is itself quantitatively large.

## B. Exact Hadamard stress calculation: E2 survives but the scalar pivot vanishes

For the r25 target-valid family

`A=[[UPU^T,U(I-P)U^T],[U(I-P)U^T,UPU^T]]`

with `U` the first three normalized Sylvester-Hadamard columns, choose `k=1`,

`P=diag(1-d,1/5,1/5)`, `0<d<=1/10`.

Every physical diagonal pivot in either half is

`a=(7/5-d)/m`.

For any such pivot, after physical sign conjugation write its Hadamard row as `z/sqrt(m)`, `z in {+-1}^3`. The exact Schur cross block has the same two nonzero singular values as

`K=(I-P z z^T/(7/5-d))(I-P)`.

Because `z^T K=0`, deleting the pivot row does not alter these singular values. Moreover `K` has rank two and

`E_2(K)=||adj K||_F^2
 = (768/625) * [ (1-d)^2+d^2/8 ]/(7/5-d)^2`.

This is decreasing on `0<d<=1/10` because the derivative numerator is proportional to `23d-16`, so

`E_2(K)>=62304/105625=0.5898603550...`.

Thus the newest partner compiler does not lose the residual pair-volume at all on this delocalized `k=1` witness; nevertheless its scalar coefficient is only `Theta(1/m)`, so its direct estimate is only `O(sqrt(m))`. This identifies a grouped-square aggregation debt, not an E2-survival debt. The final report will give the exact partner inequality, the `k=2` contrast, and a fifth-volume router for arbitrary complementary cross spectrum.

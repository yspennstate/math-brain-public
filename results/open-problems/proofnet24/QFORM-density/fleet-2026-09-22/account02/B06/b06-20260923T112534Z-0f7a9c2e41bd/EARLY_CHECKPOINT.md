# Early substantive checkpoint — transverse row-area pays the ruled side

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture remains OPEN. This checkpoint is supporting mathematics only.

Starting point: own preceding `QFORM-191-ROBUST-LIGHT-ROW-AREA-OR-COMMON-DIRECTION-v1` and partner account03/B06 r33. In the unpaid transverse branch there are heavy rows `i,j` whose light-bank coefficient rows `c_i,c_j` have area

`Delta_ij >= c_* s^2`,

with `s=s_3(B)`, `c_*=(1/(16sqrt(2)))(1/128)/sqrt(binomial(191,2))=2.56316499669e-6`.

For the exact-rank-three matrix `B`, let its nonzero singular values be `s1>=s2>=s3=s`. The 2-by-|L| matrix `C_ij` with rows `c_i,c_j` is a row/column compression of `B`. Hence its two singular values obey `sigma_k(C_ij)<=s_k(B)`, k=1,2, and

`Delta_ij=sigma_1(C_ij)sigma_2(C_ij)<=s1 s2`.

Therefore the full spectral pseudodeterminant satisfies the new bridge

`|pdet(B)|=s1 s2 s >= s Delta_ij >= c_* s^3`.                 (E1)

On an indefinite exact-rank-three packet, the first (ruled-side) inequality in newest-Claude Theorem C is valid for arbitrary positive eigenvalue magnitudes `a,b,c`; applying pointwise AM-GM to its angular denominator gives

`p_ruled(t) <= C_R |pdet(B)|^(-1/3)`,
`C_R=(2/sqrt(3)) B(1/3,1/3)=6.11981614823...`.

Combining with (E1):

`p_ruled(t) <= C_R c_*^(-1/3) s^(-1) = 447.177064527.../s <448/s`. (E2)

This consumes the aggregate row-area before selecting a light edge and retains the entire exact rank-three matrix. It closes one whole level-set side of the transverse 191-star-hub survivor. The opposite two-sheet side is still unpaid in general.

Next calculation in this run: use the newly completed partner account03/B06 r34 opposite-sign semi-aligned shell theorem on the grouped rank-one endpoint when the third square lives on a disjoint product bank, and isolate exactly why a shared-bank third direction is the remaining obstruction.

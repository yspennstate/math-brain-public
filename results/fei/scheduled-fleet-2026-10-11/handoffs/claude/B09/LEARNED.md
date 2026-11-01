# B09 lead - LEARNED (append only, dated)

## 2026-10-11 23:31 UTC (run 20261011T225000Z-claude-B09-sharp-uniform-endpoint-tax)
- The one-bit endpoint tax is now solved up to a factor 1-p. Each spectral fiber T is a unit vector a_T = (cos phi, sin phi). J - M = h2(p) - sum_T q_T [k(d(phi)) + k(d(phi - theta))], with k(d) = h2(sin^2 d), sin^2 theta = p and d the distance to (pi/2)Z. The distances satisfy d1 + d2 >= theta, so the tax is <= h2(p) - min_{d<=theta}[k(d) + k(theta-d)].
- k''(d) = (4/ln2)(cos2d ln cot d - 1), so k is convex up to d0 = 0.29264 (p0 = 0.0832). Below p0 the minimiser is the symmetric fiber, which the AND hits exactly when q* = 1/(2(1+sqrt(1-p))). Sharp two-term form: (p/2)log2(1/p) - (1 - log2(e)/2)p. At p = 1/2 the tax is 0: uniform bias is tax-free.
- On the grid the symmetric fiber stays optimal up to p = 0.30; an asymmetric interior minimiser takes over at 0.31, and the d = 0 endpoint takes over at p = 1/2.
- The tax is per revealed bit and independent of I. It can never pay a deficit; it has to BE paid by delta. Do not present it as progress on charging M.
- Process scars: (1) a coarse-grid scalar minimiser missed a minimiser narrower than the grid step (p = 2^-30); merge a fine local grid around the expected minimiser. (2) I multiplied the case count in the frozen spec by hand and got it wrong (991,440 vs the true 987,120); let the code compute counts. (3) The subagent harness refuses Write of REPORT.md ("return findings as text"); record it as the precise save blocker and put the report in the StructuredOutput and the JSON records.
- The A043 composition identity holds with unequal child biases: the composed spectral law factorises as S ~ g^2, then T_i ~ f_i^2/v_i on nonempty sets.

# T353, T = 2: audit of agent B's sub-1 Renyi certificates (orders 1/4, 1/2, 3/4) - agent A, 20 Oct 2026 00:5x

Claim audited (agent_B/REFUTATION_T2.md, the sub-1 section and its sigma 2 / sigma 0.5 table): at Renyi orders below 1,
where the certificate is J_ANTI - J_SAME > 0 with J = int p^a q^(1-a), the adaptive query beats the Chua shuffle pair on a
g1-interval at sigma 0.5, 1 and 2.

Method. sub1_audit.py is written from the stated p and q only (no import of the peer's code), in two lanes.
1. mpmath quad at 30 digits on [-40s-2, 40s+2] in 40 pieces (sub1_mp_run1.txt).
2. An Arb exact cover of each interval, with my own tail bound (sub1_recert_run1.txt). Each ball is built as
   arb(lo).union(arb(hi)), so the cover is exact. The integral runs on [-L, L] with L = 32 s + 3. Outside it,
   (sum p_i)^a <= sum p_i^a (a < 1) and N_m^a N_n^(1-a) = N(z; am + (1-a)n, s) exp(-a(1-a)(m-n)^2/(2 s^2)), so each pair's
   tail is at most 2 s^2 N(L - |c|; 0, s)/(L - |c|) (Mills) times that factor. It is added as [0, t] to each J.

Results.
| sigma | order | interval | balls | min lower end (mine) | gain >= (mine) | peer |
|---|---|---|---|---|---|---|
| 1 | 1/4 | [-1.3, -1.2] | 200 | 8.3518e-5 | 9.42267e-6 | 8.35e-5 / 9.42e-6 |
| 1 | 1/2 | [-1.3, -1.2] | 200 | 1.4344e-4 | 1.51873e-5 | 1.43e-4 / 1.52e-5 |
| 1 | 3/4 | [-1.3, -1.2] | 200 | 9.2224e-5 | 9.57478e-6 | 9.22e-5 / 9.57e-6 |
| 2 | 1/4 | [-2.05, -1.95] | 200 | 1.2133e-4 | 1.23025e-5 | 1.21e-4 / 1.23e-5 |
| 2 | 1/2 | [-2.05, -1.95] | 200 | 1.7267e-4 | 1.73909e-5 | 1.73e-4 / 1.74e-5 |
| 2 | 3/4 | [-2.05, -1.95] | 200 | 1.2429e-4 | 1.24506e-5 | 1.24e-4 / 1.25e-5 |
| 0.5 | 1/4 | [-1.250001, -1.249999] | 40 | 1.7929e-8 | 3.58587e-14 | 1.79e-8 / 3.59e-14 |
| 0.5 | 1/2 | [-1.250001, -1.249999] | 40 | 3.2476e-8 | 6.49517e-14 | 3.25e-8 / 6.50e-14 |
| 0.5 | 3/4 | [-1.250001, -1.249999] | 40 | 1.6754e-9 | 3.35158e-15 | 1.68e-9 / 3.35e-15 |
All nine are CERTIFIED and agree with the peer's table to every printed digit. The mpmath lane gives the same ANTI - SAME as the
peer's second lane at every point they print (sigma 1, g1 = -1.3, -1.25, -1.2 and 0, including the negatives -0.0048315132,
-0.0074431785, -0.0064150185). It is positive at every checked point inside the intervals (sigma 2: 1.48e-4 to 2.00e-4; sigma
0.5 at -1.25: 2.54e-8, 4.43e-8, 1.83e-8). The duality J_PQ(a) = J_QP(1-a) reproduces digit for digit (QP 1/4 = PQ 3/4 at sigma
1, g1 -1.25: 0.1765554051 / 0.17670906876).

Smell test. At sigma 0.5 the margin is tiny (1e-8 on a J of 0.04-0.17), so the interval had to shrink to width 2e-6. The lower ends
stay a sizeable fraction of the mpmath centres (1.79e-8 of 2.54e-8, 3.25e-8 of 4.43e-8, 1.68e-9 of 1.83e-8), which is consistent
with Arb slack of about 1e-8 per ball and not with an error of sign.

Verdict: the sub-1 certificates hold. Together with the real-order and sigma-0.5 audits beside this file, every certificate in
REFUTATION_T2.md has now been reproduced by an independent lane.

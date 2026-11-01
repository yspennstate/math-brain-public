# T067 q=4 d=2: second audit (agent H, 17-18 Oct 2026)

## Part 1, by hand: PASS
- Prop 6.1: every E phi_j (j>=2) is zero. Checked one by one from eq (weighted), the third-moment tensor and Table 1. Each Table 1 entry was re-derived (c^2, c ell, c^3, c p22, c p31, p21^2, p21 p12, (A+B)p22). E phi_0 = m(2sqrt2-2)T and E phi_1 = 0 come from E F3 = 2sqrt2 T and E F4 = 4V.
- g* = 16/3 - g0(2sqrt2-2): with sqrt2 < 70711/50000 the bound is exactly 863/375000000 (1726/750000000). The inequality is strict.
- eq (drift): re-derived from 1/s = 1 - c/4 + c^2/(16s), E N = 2m + m^2/6 and E[Nc] = 2m^2/3 + 4mT/3 + T^2/6.
- Sec 7 composition: m = 8x <= 8U = M. The support lemma (the vertex minima and the fixed point 0.67573 of f were re-done) and s >= 1 - lambda^2 both check (the minimum of c is -4 lambda^2).
- The composition needs only T >= 0 from Prop 5.1. The coset averaging for the per-coset upper constants M_C deserves one sentence in the paper, but the upper bound is not used in sec 7.
- Reduction in Prop 6.2: K is invariant under simultaneous permutations and affine in m. The ordered simplex equals {sorted, zero-sum, a_0 >= -rho}. The Sigma_k bounds hold.

## Part 2, own certificate (cert_b1e.py)
- The code shares nothing with indep_cover.py.
- K s^3 is built at bidegree (8,8), the lowest bihomogeneous degree.
- Selftest: the polynomial equals a separate plain-Fraction coding of Table 2 at random rational points, in 6/6 cases over both endpoints.
- Appendix A's two forms of g24 agree exactly.
- Full 192-case run: cert_b1e_results.jsonl (RUN DONE line in run.log).

## Part 2 verdict: PASS (18 Oct 2026, 01:3x)

- All 192 cases are certified: 24 permutations x 2 x 2 cells x m in {0, M_END}. In every case every coefficient of K s^3 (U V)^e is >= 0, and the exact cross-check against K_direct holds.
- The run was interrupted by the 00:09 power-off at 142 cases. It resumed from the results file, skipping cases already certified, and ended with "RUN DONE fails 0".
- Degrees used: e = 0 in 145 cases, e = 1 in 31, e = 2 in 16.
- gamma is nonzero in 24 cases, which matches the paper and agent C's run (24 gamma cases, 16 e = 2 cases).
- The e = 0 / e = 1 split differs from that run because the base degree differs: this run multiplies by s^3 at bidegree (8,8).
- Because K is affine in m, the two endpoints cover [0, M]. With s > 0 (Part 1), this proves K >= 0 on the domain of Prop 6.2.

### Negative arm

- With g24 lowered by 1/10, the shifted K is negative inside the domain, by direct exact evaluation:
  - point: m = M_END, a = -(12863/29000)(1,1,1,-3), b = a with coordinates 3 and 4 swapped
  - true K = +1.1952; shifted K = -1.1136 (Fraction arithmetic)
  - So no certificate can pass the shifted K, and this control is a negative arm in the strong sense (neg_ratio3.py).
- Over all 24 permutations of b, the smallest K/phi24 found is 0.0446, against a real g24 change of 0.1036.
- My first search (neg_ratio.py) kept b in a's chamber. It found 0.281 and wrongly suggested that -1/10 tested only tightness. That search was superseded the same hour.
- control_shift.log: the polynomial-side run of the same arm (count of failing cases), appended when it finishes.

## Control result (appended 02:00 18 Oct, shell clock)
`cert_b1e.py control shift 1` (g24 shift -1/10, m in {0, M_END}): **CONTROL shift cases failing 75 of 96** (control_shift.log). With the exact negative point above, this is a real falsity control: the certificate fails where the function is negative, as it should.

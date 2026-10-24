"""Evaluate the explicit upper-bound expressions of the B03 PP_q theorem (REPORT.md section 3.4) for q = 12..200.
Every quantity is an explicit closed-form UPPER bound proved in the report; this script only evaluates them
(mpmath, 40 digits; binomial sums exact as Python integers). No sampling, no fitting.
"""
import math
import mpmath as mp

mp.mp.dps = 40
LOG2E = 1 / mp.log(2)
K0 = mp.mpf(120) / 11 + 3 + 2 * mp.log(3, 2) + mp.log(6 * mp.e, 2)
BASE = 2 + LOG2E + K0
rows = []
for q in range(12, 201):
    n = q * q + q + 1
    s0 = mp.mpf(11) * (q + 1) / 120            # density threshold b_L / beta
    two_q = mp.mpf(2) ** q
    W = 1 / (1 - (q * q + mp.mpf(q) / 2) / two_q)  # >= (q+1)2^-q / Inf_j
    eps = 2 * q * (q + 1) / two_q * W          # >= ||r||^2 / Inf_j
    Delta = q / two_q * W                      # >= (q+1)q 4^-q / Inf_j  (empty-set excess)
    Gmax = mp.mpf(6) / 5 * mp.log(q + 1, 2) + (q + 1)
    # P(|T| < s0 - 1), T uniform subset of q points
    rare_cnt = sum(math.comb(q, i) for i in range(q + 1) if i < s0 - 1)
    rare = (q + 1) * mp.mpf(rare_cnt) / two_q
    EGL = mp.mpf(6) / 5 + rare                 # >= E_{nu_{E_L}} G_j(L)
    CR = 2 * W * EGL + (2 * Delta + 2 * eps) * Gmax   # eta = 1 in Lemma I
    I_low_over_n = (q + 1) / two_q / W         # I / n >= this
    label = 2 * n / two_q * mp.log(q + 1, 2) / (n * I_low_over_n)   # v log2 k / I
    Pq = mp.mpf(rare_cnt) / two_q              # P(Bin(q,1/2) < s0 - 1)
    other_over_I = 2 * W * Pq + 3 * eps        # >= sum_{other A} fhat^2 |A| / I  (Lemma O, eta = 1)
    other = mp.mpf(11) / 5 * mp.log(q + 1, 2) * other_over_I
    total = BASE + label + other + CR
    paper = 41 + 7 * mp.log(q + 1, 2)
    rows.append((q, total, label, other, CR, paper))
print(f"BASE = 2 + log2 e + K0 = {mp.nstr(BASE, 12)}   (K0 = {mp.nstr(K0, 12)})")
print(" q   refined_total   label   other    C_R    paper_41+7log2(q+1)")
for r in rows:
    if r[0] <= 30 or r[0] % 20 == 0:
        print(f"{r[0]:3d}  {mp.nstr(r[1], 8):>12}  {mp.nstr(r[2], 5):>7} {mp.nstr(r[3], 5):>7} {mp.nstr(r[4], 5):>7}  {mp.nstr(r[5], 8)}")
sup = max(rows, key=lambda r: r[1])
print(f"sup over 12<=q<=200 of refined_total = {mp.nstr(sup[1], 10)} at q = {sup[0]}")
# monotone decrease check on the tail of the range
dec = all(rows[i + 1][1] <= rows[i][1] for i in range(len(rows) - 1) if rows[i][0] >= 20)
print(f"refined_total non-increasing for 20 <= q <= 200: {dec}; value at q=200: {mp.nstr(rows[-1][1], 10)}")
lim = BASE + 2 * mp.mpf(6) / 5
print(f"limit q->inf of the bound (eta=1): BASE + 2*(6/5) = {mp.nstr(lim, 10)}")

# -*- coding: utf-8 -*-
"""Two checks of the referee's 7 September claims about Proposition 5.1 of the two-copy paper.

(1) The exponent: optimizing the split in the shift inequality gives S_m ~ m^beta with
    beta = log(1-alpha)/log(alpha), hence j_n = O(n^(beta-1)) = O(n^(-0.5379...)).
(2) The obstruction: the nonsummable sequence jt_n = c((n+1)^beta - n^beta) satisfies every
    shifted inequality S_m - S_r <= alpha (S_m + Delta_{m,n}), r + n = m, together with
    j_0 = c, monotone decrease, and 0 <= j <= log 2.  Checked exactly enough for m <= MMAX
    and every n in 1..m (integers exact; logs in double precision with a margin printed).
"""
import math, sys
a, b = math.log(2), math.log(3)
L = b - a; c = 2*b - 3*a; alpha = L / b
beta = math.log(1 - alpha) / math.log(alpha)
print(f"a={a:.9f} b={b:.9f} c=log(9/8)={c:.9f} alpha={alpha:.9f}")
print(f"beta = log(1-alpha)/log(alpha) = {beta:.9f}  ->  j_n exponent beta-1 = {beta-1:.9f}")
print(f"paper's rational exponent 12/25 = 0.48 (j_n ~ n^-0.52); sharpened {1-beta:.6f}")

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
S = lambda m: c * m**beta            # partial sums of jt: S_m = c m^beta exactly (telescoping)
worst = float("inf"); worst_at = None; viol = 0
for m in range(1, MMAX + 1):
    for n in range(1, m + 1):
        r = m - n
        M = 2**m; N = 3**n
        q = -(-M // N)                              # ceil(M/N), exact
        Delta = math.log(N) + math.log(q) - math.log(M) if False else (n*b + math.log(q) - m*a)  # log(N ceil(M/N)/M), q exact
        lhs = S(m) - S(r)
        rhs = alpha * (S(m) + Delta)
        slack = rhs - lhs
        if slack < worst: worst, worst_at = slack, (m, n)
        if slack < -1e-9: viol += 1
print(f"checked m<=MMAX={MMAX}, all n: violations {viol}; minimum slack rhs-lhs = {worst:.3e} at (m,n)={worst_at}")
# the pure part (N <= M, Delta < a): equality of the exponent condition r/m >= alpha
jt = [c*((n+1)**beta - n**beta) for n in range(0, 50)]
print("jt_0 = %.6f (= c? %s), decreasing: %s, <= log2: %s" % (jt[0], abs(jt[0]-c) < 1e-12, all(jt[i+1] <= jt[i] for i in range(49)), max(jt) <= a))
print("partial sums S_m = c m^beta grow without bound: S_1000 = %.4f, S_10^6 = %.4f" % (S(1000), S(10**6)))

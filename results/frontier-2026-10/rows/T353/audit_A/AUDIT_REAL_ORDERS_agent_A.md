# Audit of the non-integer order certificates, orders 3/2 and 5/2, sigma 1 (agent A, 19 Oct 2026)

Files audited (agent_B/): cert_renyi_real_arb_sigma.py; cert_renyi{pq,qp}{32,52}_real_s1_arb.txt with the argv of run_rr1_*.cmd;
cert_renyi_real_s1_scan.txt. Verdict: the four certificates hold. No fault found.

## 1. Tail bound (by hand)
On |z| > L: p^alpha <= 2^(alpha-1) sum_i a_i^alpha N_{m_i}^alpha (convexity of x^alpha, at most two terms); q^(1-alpha) <= (b_j N_{n_j})^(1-alpha)
for every j (q >= b_j N_{n_j} and 1 - alpha < 0), so taking the smaller over j per i is valid; N_m^alpha N_n^(1-alpha) = N(c) exp(alpha(alpha-1)
(m-n)^2/(2 s^2)) with c = alpha m - (alpha-1) n (the identity checked numerically in AUDIT_RENYI_S2); |c| <= 2 alpha - 1 < L = 30 s + 2 alpha;
Mills bound s^2 N(t; 0, s)/t for P(X > t). The bound is correct for every real alpha > 1. The branch cut: acb.pow with analytic=True returns an
indeterminate value if a ball meets the cut, and the certify loop treats any non-positive or indeterminate difference as a failure
(`if not d > 0`), so the cut cannot produce a false certificate.

## 2. Values (real_order_audit.py, real_order_audit_run1.txt)
J_SAME and J_ANTI recomputed from the raw densities with mpmath (dps 40, order as an exact rational) at both ends and the centre of each
certified interval and at 1-3 scan points per case, 21 points in all: every value agrees with arb to 10 digits (|difference| < 1e-12), and
S - A agrees in sign and size, including the negative scan points (3/2 PQ at -1.2, 5/2 PQ at -1.2, 3/2 QP at 0). Ball inclusion holds on the
first exact-cover sub-ball of each run.

## 3. Gains
Each gain is sum over 80 sub-intervals of width x lower(S - A) on that sub-interval, so it must lie between (min lower) x (b - a) and
(max of S - A) x (b - a). It does in all four:
  3/2 PQ  9.074e-6 <= 9.20947e-6 <= 1.19e-5     5/2 PQ  7.058e-5 <= 7.14287e-5 <= 1.06e-4
  3/2 QP  2.190e-5 <= 2.30495e-5 <= 2.60e-5     5/2 QP  1.793e-3 <= 1.80232e-3 <= 1.82e-3
The balls are built as arb(lo).union(arb(hi)), the exact cover recommended in AUDIT_S05, and the four argv sets have no cover gap.

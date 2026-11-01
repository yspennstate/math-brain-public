"""Is the renewal new information? Globally, no - it is the half-shift identity already known.

cos^2(3 pi v/2) = 1/2 + (1/2) cos(3 pi v), and (Q^2)hat(x) = 2 rho(2x) with rho = nu*nu. So the cross
term over the WHOLE line is int cos(3 pi v) Q^2 dv = 2 rho(3), and the renewal
    int_R Q^2 = (3/2) int_R cos^2(3 pi v/2) Q^2
collapses to 2 rho(0) = (3/4) 2 rho(0) + (3/2) rho(3) . 2 /2, i.e. rho(0) = 3 rho(3) - the half-shift
identity A(0) = 3 A(1/2) in nu's coordinates. PREDICTION, falsifiable and exact:

    int_R cos(3 pi v) Q(v)^2 dv = (1/3) int_R Q(v)^2 dv .

If that holds, the global renewal carries nothing new and ONLY the tail version does. Also report the
same ratio restricted to tails [M, inf), which is the quantity that actually matters.
"""
import numpy as np

M, PTS, CH = 100_000.0, 400, 2_000_000
n_tot = int(M * PTS); du = M / n_tot
cuts = [0.0, 10.0, 100.0, 1_000.0, 10_000.0]
tot_q = 0.0; tot_c = 0.0
tail_q = np.zeros(len(cuts)); tail_c = np.zeros(len(cuts))
for s in range(0, n_tot, CH):
    k = min(CH, n_tot - s)
    u = (s + np.arange(k) + 0.5) * du
    q = np.ones(k); j = 0
    while True:
        a = (2.0/3.0) ** j * u
        q *= np.cos(np.pi * a); j += 1
        if a.max() < 1e-9: break
    q2 = q * q
    cw = np.cos(3.0 * np.pi * u) * q2
    tot_q += q2.sum() * du; tot_c += cw.sum() * du
    for i, cut in enumerate(cuts):
        m = u >= cut
        if m.any():
            tail_q[i] += q2[m].sum() * du; tail_c[i] += cw[m].sum() * du

print(f"int_0^M Q^2            = {tot_q:.8f}   (half-line; x2 for the whole line)")
print(f"int_0^M cos(3 pi v)Q^2 = {tot_c:.8f}")
print(f"ratio                  = {tot_c/tot_q:.8f}   predicted 1/3 = 0.33333333")
print(f"so rho(3)/rho(0)       = {tot_c/tot_q:.8f}   predicted 1/3, i.e. A(0) = 3 A(1/2)")
print()
print(f"{'tail from M':>12} {'int Q^2':>14} {'ratio':>12}")
for i, cut in enumerate(cuts):
    if tail_q[i] > 0:
        print(f"{cut:>12.0f} {tail_q[i]:>14.6e} {tail_c[i]/tail_q[i]:>12.6f}")
print("\nthe tail ratio is corr_n - 1 in disguise; it is what has to stay away from +1/3-plus-a-margin")

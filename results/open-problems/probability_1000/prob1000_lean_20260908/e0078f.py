"""The quotable instance: m=24 cycle, rate 1, states 0..11 at rate 2/3 (lambda* = 1/3, exposure 8 per lap).
30-digit mpmath: locate the minimum of (pi-alpha)e^{Ct}1 and report both survivals there."""
import mpmath as mp
mp.mp.dps = 30
m, k = 24, 12; L = mp.mpf(2)/3
C = mp.zeros(m, m)
for i in range(m):
    C[i, i] = -1 - (L if i < k else 0); C[i, (i+1) % m] = 1
pi = [mp.mpf(1)/m]*m; ls = sum(pi[i]*(L if i<k else 0) for i in range(m)); al = [pi[i]*(L if i<k else 0)/ls for i in range(m)]
one = mp.matrix([1]*m)
def both(t):
    u = mp.expm(C*t)*one
    S = sum(pi[i]*u[i] for i in range(m)); A = sum(al[i]*u[i] for i in range(m)); return S, A
best = None
for t in [mp.mpf(x)/4 for x in range(60, 110)]:
    S, A = both(t)
    if best is None or S - A < best[0]: best = (S - A, t, S, A)
d, t, S, A = best
print(f"lambda* = {ls},  t = {t}:  P(T^pi > t) = {mp.nstr(S, 10)},  P(T^alpha > t) = {mp.nstr(A, 10)},  difference = {mp.nstr(d, 8)}, relative {mp.nstr(d/S, 6)}")
# refine on a finer grid around t
tt = min([t + mp.mpf(j)/40 for j in range(-10, 11)], key=lambda x: both(x)[0]-both(x)[1])
S, A = both(tt); print(f"refined t = {tt}: P(T^pi > t) = {mp.nstr(S,10)}, P(T^alpha > t) = {mp.nstr(A,10)}, ratio alpha/pi = {mp.nstr(A/S,6)}")

"""Check the K5 report's closed forms (section 5, eq. 10) for the fork comb against the
independent exact solver in k5/check_fork_comb.py (killed hitting systems, one per target)."""
import sys, io, contextlib
from fractions import Fraction as F
sys.path.insert(0, r"~\agent_run\k5")
with contextlib.redirect_stdout(io.StringIO()):
    import check_fork_comb as C

def closed(N, t):
    t = F(t); r = t**3; al = t
    G = lambda k: sum(r**l for l in range(1, k+1))
    B = 2 + al*(t+1)
    S = [t+1 + r**(k+1) + B*G(k) for k in range(N)]
    SN = t+1 + r**(N+2) + B*G(N) + (t+1)*al*r**(N+1)
    L = (N+2)*r**(N+4); W = L + r**(N+2) + SN
    M = t + sum(S[k]/r**(k+1) for k in range(N)) + SN/r**(N+2)
    Q = [S[k] + t*al*r**(k+1) for k in range(N)]
    A = t + sum(Q[k]/((1+al)*r**(k+1)) for k in range(N))
    mu = (t**2*(1+al*G(N+1)) + sum(S[k]**2/r**(k+1) for k in range(N)) + SN**2/r**(N+2))/W
    muh = (t**2*(1+al*r**(N+1)) + sum(Q[k]**2/((1+al)*r**(k+1)) for k in range(N)))/W
    ineq1 = W/r**(N+2) >= M
    ineq2 = True if N == 0 else W/((1+al)*r**N) >= A - t
    return M - mu, A + t - muh, ineq1, ineq2

ok = True
for N in (0, 1, 2, 3):
    for t in (2, 3, 10, 100):
        w, blocks = C.fork_comb(N, t)
        a = C.tmix(w); b = C.tmix(C.lump(w, blocks))
        x, y, i1, i2 = closed(N, t)
        good = (a == x and b == y and i1 and i2)
        ok &= good
        print(N, t, "tmix match" if a == x else "TMIX MISMATCH", "quot match" if b == y else "QUOT MISMATCH", i1, i2, f"ratio {float(b/a):.9f}", flush=True)
print("ALL CLOSED FORMS EXACT" if ok else "FAILURE")

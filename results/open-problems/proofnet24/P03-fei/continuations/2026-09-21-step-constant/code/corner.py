"""Break-it: the report names three tight sets - q = 2^-k, the strip p->1/2 with q->1,
and the arc pq = 1/2 near p = q = 0.71. Sample each densely at the candidate's margin."""
import numpy as np
from ladder import Phi

def scan(name, P, Q, cs=(0.0041, 0.0045, 0.0050, 0.0100)):
    for c in cs:
        v = Phi(P, Q, c)
        j = int(np.argmin(v))
        print("  %-34s c=%.4f  min Phi = %11.3e at p=%.8g q=%.8g  %s"
              % (name, c, v[j], P[j], Q[j], "ok" if v[j] >= 0 else "FAILS"))

if __name__ == '__main__':
    # 1. the strip p -> 1/2 from below, q -> 1
    e1 = 10.0**np.linspace(-12, -1, 600)
    p = 0.5 - e1
    q = 1.0 - 10.0**np.linspace(-12, -1, 600)
    PP, QQ = np.meshgrid(p, q, indexing='ij')
    scan("strip p->1/2, q->1", PP.ravel(), QQ.ravel())
    # 2. the arc pq = 1/2 near p = q = 0.71
    pa = np.linspace(0.5001, 0.999, 4000)
    qa = 0.5/pa
    m = (qa > 0) & (qa < 1)
    scan("arc pq = 1/2", pa[m], qa[m])
    # 3. q = 2^-k lines, p dense
    xs = np.linspace(1, 40, 8000)
    for k in range(1, 9):
        q0 = 2.0**-k
        scan("q = 2^-%d" % k, 2.0**(-xs), np.full_like(xs, q0), cs=(0.0041, 0.0050))
    # 4. both near 1/2
    a = np.linspace(0.30, 0.70, 1200)
    AA, BB = np.meshgrid(a, a, indexing='ij')
    scan("both in [0.30, 0.70]", AA.ravel(), BB.ravel())

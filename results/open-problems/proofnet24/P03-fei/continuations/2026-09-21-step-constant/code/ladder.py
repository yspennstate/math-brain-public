"""Where is the M=96 candidate short?  The region-2 run stops at a degenerate cell
x = 4.000000, v = 1.584632, i.e. p = 2^-4 = 1/16 and 1-q = 2^-log2(3) = 1/3, q = 2/3.
2/3 is q_1 of Hod's ladder q_0 = 1/2, q_{j+1} = 1/(1+q_j) -> 1/phi.
Question: is the candidate's residual concentrated on that ladder?  If so the fix is a
grid refined at the q_j, not a uniform 4x refinement."""
import numpy as np, sys
from math import log2, log, sqrt

CAND = r"~/AppData/Local/Temp/claude/<project>/07f56e82-b3da-42b4-8041-02c1a661a843/scratchpad/fei/cert_vi_h96k40.npz"
d = np.load(CAND)
print("candidate arrays:", {k: d[k].shape for k in d.files})
xs = d['xs']; G = d['G']; C0 = float(d['C']) if 'C' in d.files else 6.4548
print("C0 =", C0, " nodes =", len(xs), " x range", xs.min(), xs.max())

def h2(x):
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = (x > 0) & (x < 1)
    out[m] = -x[m]*np.log2(x[m]) - (1-x[m])*np.log2(1-x[m])
    return out

def Gnum(x):                      # piecewise linear in x = log2(1/p)
    return np.interp(x, xs, G)

def Gamma(p, c):
    """candidate potential, symmetric about 1/2"""
    p = np.asarray(p, float)
    pp = np.minimum(p, 1-p)
    x = -np.log2(pp)
    return pp*Gnum(x) + c*pp*(1-pp)

def phi_w(w):
    w = np.asarray(w, float)
    return np.where(w > 0, w*np.log2(np.where(w > 0, 1.0/np.maximum(w, 1e-300), 1.0)), 0.0)

def Psi(z):
    """Psi(z) = phi((1-2z)^2)/z, valid on all of (0,1) (the ell(2z) rewriting is not)"""
    z = np.asarray(z, float)
    return np.where(z > 0, phi_w((1-2*z)**2)/np.maximum(z, 1e-300), 0.0)

def E(p, q):
    L = lambda t: -np.log2(t)
    return (8*p*(1-q)*L(p) + 8*q*(1-p)*L(q) + 8*(1-p)*(1-q)
            + Psi(p*q) - Psi(p) - Psi(q))

def Phi(p, q, c):
    """(A) in the normalised form: G(p)+G(q)-G(pq)-E  with G = Gamma/p"""
    Gp = Gamma(p, c)/p; Gq = Gamma(q, c)/q; Gpq = Gamma(p*q, c)/(p*q)
    return Gp + Gq - Gpq - E(p, q)

if __name__ == '__main__':
    c = 0.003
    # Hod's ladder
    q = [0.5]
    for _ in range(12): q.append(1/(1+q[-1]))
    print("\nHod ladder q_j:", ", ".join("%.6f" % t for t in q[:8]), "-> 1/phi =", (sqrt(5)-1)/2)
    print("\nresidual Phi at (p = 2^-k, q = q_j), c = 0.003   [negative = candidate violates (A)]")
    print("      " + "".join("  q_%-9d" % j for j in range(6)))
    for k in range(1, 9):
        p = 2.0**-k
        row = "p=2^-%-2d" % k
        for j in range(6):
            row += "  %10.2e" % Phi(np.array([p]), np.array([q[j]]), c)[0]
        print(row)
    # the reported failing point
    print("\nthe run's failing cell: p = 1/16, q = 2/3 ->  Phi = %.4e" %
          Phi(np.array([1/16]), np.array([2/3]), c)[0])
    # is the ladder special?  compare with a random control sample
    rng = np.random.default_rng(3)
    P = rng.uniform(0.002, 0.5, 40000); Q = rng.uniform(0.002, 0.999, 40000)
    v = Phi(P, Q, c)
    print("random (p,q) control, 40000 points: min Phi = %.4e, fraction negative = %.4f"
          % (v.min(), (v < 0).mean()))
    # ladder-only sample
    lad = []
    for k in range(1, 20):
        for j in range(10):
            lad.append(Phi(np.array([2.0**-k]), np.array([q[j]]), c)[0])
    lad = np.array(lad)
    print("Hod-ladder grid (19 x 10):        min Phi = %.4e, fraction negative = %.4f"
          % (lad.min(), (lad < 0).mean()))

def map_line(c=0.003):
    """where along q = 2/3 is the candidate short, and how wide is the bad set?"""
    print("\n--- scan along q = 2/3, p = 2^-x ---")
    x = np.linspace(1.0, 12.0, 4401)
    p = 2.0**(-x); q = np.full_like(p, 2.0/3.0)
    v = Phi(p, q, c)
    bad = v < 0
    print("negative at %d of %d sampled x; x range of the bad set: %s"
          % (bad.sum(), len(x), ("%.4f .. %.4f" % (x[bad].min(), x[bad].max())) if bad.any() else "none"))
    j = int(np.argmin(v))
    print("worst: x = %.4f (p = %.6g), Phi = %.4e, Phi/v = %.4e" % (x[j], p[j], v[j], v[j]/(1-2/3)))
    print("\n--- same scan at several q, to see if 2/3 is special ---")
    for qq, lab in [(0.5,'q_0=1/2'), (2/3,'q_1=2/3'), (0.6,'q_2=3/5'), (0.625,'q_3=5/8'),
                    (0.618034,'1/phi'), (0.70,'0.70 (off ladder)'), (0.55,'0.55 (off ladder)')]:
        vv = Phi(2.0**(-x), np.full_like(x, qq), c)
        print("  %-18s min Phi = %10.3e   negatives: %d" % (lab, vv.min(), int((vv<0).sum())))

def margin_needed(c=0.003):
    """how much smaller must c be for this candidate to pass on the ladder?"""
    print("\n--- the candidate's own residual sets the floor ---")
    x = np.linspace(1.0, 12.0, 2201)
    for cc in (0.003, 0.002, 0.0015, 0.001, 0.0005):
        worst = 1e9
        for qq in (0.5, 2/3, 0.6, 0.625, 0.618034):
            vv = Phi(2.0**(-x), np.full_like(x, qq), cc)
            worst = min(worst, vv.min())
        print("  c = %-7.4f  worst Phi on the ladder = %10.3e  -> constant would be %.6f  %s"
              % (cc, worst, 6.4548 + cc/4, "PASSES" if worst >= 0 else "fails"))

map_line(); margin_needed()

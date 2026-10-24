"""Negative controls for xor_cert.py: two copies of the h24k40 potential with a planted violation of
Gamma(p) + Gamma(q) >= Gamma(p + q - 2pq) (a steep 60 per cent step on x in [1.25, 1.40], and a smooth Gaussian bump
doubling G near x = 1.32).  The certificate must report NOT VERIFIED on both.  The control potentials are written to logs/."""
import os, sys, subprocess
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
LOG = os.path.join(HERE, "..", "logs")
d = np.load(os.path.join(HERE, "..", "..", "inputs", "cert_vi_h24k40.npz"))
xs = d["xs"].copy(); G = d["G"].copy()
for tag in ("steep", "smooth"):
    if tag == "steep":
        m = (xs >= 1.25) & (xs <= 1.40); G2 = G.copy(); G2[m] *= 1.6
    else:
        G2 = G * (1 + np.exp(-((xs - 1.32) / 0.12) ** 2))
    f = os.path.join(LOG, "control_%s.npz" % tag)
    np.savez(f, xs=xs, G=G2, C=d["C"], M=d["M"], K=d["K"])
    pot = F.Pot(f, 0.0)
    p = np.linspace(0.005, 0.5, 500); P, Q = np.meshgrid(p, p)
    D = pot(P) + pot(Q) - pot(P + Q - 2 * P * Q)
    j = np.unravel_index(np.argmin(D), D.shape)
    print("control %s: min Gamma(p)+Gamma(q)-Gamma(p*q) on a 500^2 grid = %.4f at p=%.3f q=%.3f" % (tag, D.min(), P[j], Q[j]), flush=True)
    r = subprocess.run([sys.executable, os.path.join(HERE, "xor_cert.py"), f, "0.03125"], capture_output=True, text=True)
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    print("   " + "\n   ".join(lines[-3:]), flush=True)
    if r.returncode:
        print("   exit code %d; stderr tail: %s" % (r.returncode, r.stderr[-300:]), flush=True)

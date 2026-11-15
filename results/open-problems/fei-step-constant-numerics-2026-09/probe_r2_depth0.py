"""depth-0 probe of the region-2 bound: failing fraction and worst bound on the initial cells at two margins"""
import sys, os, time, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert23 as C2
from fei_cert import Iv, Cert
src = sys.argv[1]; cs = [float(a) for a in sys.argv[2:]]
d = np.load(src); xs, G = d["xs"], d["G"]; K = float(xs[-1])
for c in cs:
    cert = Cert(xs, G, c, tail_slope=(G[-1] - C2.BSTAR) / K); C2.build_slope_tables(cert)
    n = len(xs) - 1
    I, J = np.meshgrid(np.arange(n), np.arange(n), indexing="ij"); I = I.ravel(); J = J.ravel()
    t0 = time.time(); bad = 0; worst = np.inf; tot = 0
    I = I[::13]; J = J[::13]
    for s in range(0, len(I), 500000):
        e = min(len(I), s + 500000)
        lo = C2.phi2_over_v_lower(cert, Iv(xs[I[s:e]], xs[I[s:e] + 1]), Iv(xs[J[s:e]], xs[J[s:e] + 1]))[0]
        bad += int((lo < 0).sum()); worst = min(worst, float(lo.min())); tot += e - s
    print("c=%g: region-2 depth 0: %d of %d node cells fail (%.2f%%), worst bound %.3e  (%.0f s)" % (c, bad, tot, 100.0 * bad / tot, worst, time.time() - t0), flush=True)

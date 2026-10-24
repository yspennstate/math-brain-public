"""Region 2 with the exact A term. usage: run_r2x.py <npz> <c> [max_depth]"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert_r1x as R
src = sys.argv[1]; c = float(sys.argv[2]); md = int(sys.argv[3]) if len(sys.argv) > 3 else 30
cert, C0 = R.load_cert(src, c)
print("certificate %s: C0=%.7f, %d nodes, K=%g, c=%g -> C_cert = %.7f" % (src, C0, len(cert.xs), cert.K, c, cert.C_cert()), flush=True)
t0 = time.time()
ok = R.verify_region2_exact(cert, md)
print("RESULTS: {'R2x': %s}  (%.0f s)" % (ok, time.time() - t0))
print("REGION 2 (exact A): %s at c=%g (C_cert = %.7f)" % ("VERIFIED" if ok else "NOT verified", c, cert.C_cert()))

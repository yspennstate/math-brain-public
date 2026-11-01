"""Probe the minus-wedge seam at kappa = 0.05: (1) full record of a
failing Region-I band (which leaf, what enclosure); (2) float map of
S_star and the ray second derivative along minus-wedge directions."""
import math
import time

from core import set_prec
set_prec(50)
import certify_km_slab as C
import huang_cert_region1 as R1
import huang_cert_np as nr


def main():
    kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
    alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
    q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
    la = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
    lb = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
    R1.configure_region1(C.arb(C.dec('0.05')), alpha,
                         C.hull(la[0], lb[0]), C.hull(la[1], lb[1]))
    t0 = time.time()
    r = R1.band_job((0.00864, 0.012, 3.6054389046534583, 3.6214389046534583))
    print('failing band record (%.0fs):' % (time.time() - t0), flush=True)
    print('  ok=%s cells=%s worst=%s nfail=%s' % (
        r['ok'], r.get('cells'), r.get('worst'), r.get('nfail')))
    for f in r.get('fails', []):
        print('  fail leaf:', f, flush=True)

    wm = R1.W_ANG + math.pi
    print('minus-wedge float map (S in 1e-6 units, ray dd in 1e-3):',
          flush=True)
    for om in (0.13, 0.148, 0.155, 0.16):
        for sgn in (+1, -1):
            th = wm + sgn * om
            v1, v2 = math.cos(th), math.sin(th)
            row = []
            for rr in (0.006, 0.008, 0.0086, 0.009, 0.010, 0.012, 0.014):
                a1 = R1.A1S + rr * v1
                a2 = R1.A2S + rr * v2
                s = nr.S_star(a1, a2)
                s = s[0] if isinstance(s, tuple) else s
                row.append('%.1f' % (s * 1e6))
            print('  om=%+.3f: S = %s' % (sgn * om, '  '.join(row)),
                  flush=True)
    # ray second derivative (FD of S_star along the ray) at the failing spot
    for om in (0.148, 0.155, 0.16):
        th = wm + om
        v1, v2 = math.cos(th), math.sin(th)
        row = []
        for rr in (0.007, 0.009, 0.0105, 0.012):
            h = 4e-4
            vals = []
            for dr in (-h, 0.0, h):
                s = nr.S_star(R1.A1S + (rr + dr) * v1,
                              R1.A2S + (rr + dr) * v2)
                vals.append(s[0] if isinstance(s, tuple) else s)
            dd = (vals[0] - 2 * vals[1] + vals[2]) / h / h
            row.append('%.2f' % (dd * 1e3))
        print('  om=+%.3f: ddS = %s' % (om, '  '.join(row)), flush=True)
    # and the plus side for comparison
    for om in (0.155,):
        th = R1.W_ANG + om
        v1, v2 = math.cos(th), math.sin(th)
        row = []
        for rr in (0.007, 0.009, 0.0105, 0.012):
            h = 4e-4
            vals = []
            for dr in (-h, 0.0, h):
                s = nr.S_star(R1.A1S + (rr + dr) * v1,
                              R1.A2S + (rr + dr) * v2)
                vals.append(s[0] if isinstance(s, tuple) else s)
            dd = (vals[0] - 2 * vals[1] + vals[2]) / h / h
            row.append('%.2f' % (dd * 1e3))
        print('  PLUS om=+%.3f: ddS = %s' % (om, '  '.join(row)), flush=True)


if __name__ == '__main__':
    main()

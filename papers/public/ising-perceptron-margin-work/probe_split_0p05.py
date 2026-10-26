"""Measure the credit-restoration from radial band splitting at the
failing minus-wedge chunk, and compare the passing plus-side twin."""
import math

from core import set_prec, endpoints
set_prec(50)
import certify_km_slab as C
import huang_cert_region1 as R1


def ep(b):
    lo, hi = endpoints(b)
    return '[%.4g, %.4g]' % (float(lo), float(hi))


def probe(t0b, t1b, th0b, th1b, ta, tb_):
    xc = R1.xhull_of_band(t0b, t1b, th0b, th1b)
    lboxb = None
    for pm in (1.0, 1.6, 2.4):
        fan, lbox = R1.fan_and_box(t0b, t1b, th0b, th1b, pm)
        cand = tuple(R1._exact_decimal(x) for x in lbox)
        try:
            R1._validate_lbox(cand)
        except ValueError:
            continue
        if R1.edge_check(*cand, xc, fan):
            lboxb = cand
            break
    if lboxb is None:
        print('  no certified lbox', flush=True)
        return
    l2w = float(lboxb[3]) - float(lboxb[2])
    b11, b12, b22, cert = R1.B_Lambda(*lboxb)
    thb = (R1._dec(ta, 8).union(R1._dec(tb_, 8))
           + R1._ANG_PAD.union(-R1._ANG_PAD))
    v1, v2 = thb.cos(), thb.sin()
    qB = R1.Binv_form(b11, b12, b22, v1, v2)
    print('  t=[%.5f,%.5f] l2-width=%.3f qB=%s' % (t0b, t1b, l2w, ep(qB)),
          flush=True)


def main():
    kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
    alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
    q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
    la = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
    lb = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
    R1.configure_region1(C.arb(C.dec('0.05')), alpha,
                         C.hull(la[0], lb[0]), C.hull(la[1], lb[1]))
    print('MINUS chunk [3.6054, 3.6214], failing leaf [3.6194, 3.6214]:',
          flush=True)
    probe(0.00864, 0.012, 3.6054389046534583, 3.6214389046534583,
          3.6194389046534585, 3.6214389046534583)
    print(' radial halves:', flush=True)
    tm = 0.5 * (0.00864 + 0.012)
    probe(0.00864, tm, 3.6054389046534583, 3.6214389046534583,
          3.6194389046534585, 3.6214389046534583)
    probe(tm, 0.012, 3.6054389046534583, 3.6214389046534583,
          3.6194389046534585, 3.6214389046534583)
    print(' radial quarters of the outer half:', flush=True)
    tq = 0.5 * (tm + 0.012)
    probe(tm, tq, 3.6054389046534583, 3.6214389046534583,
          3.6194389046534585, 3.6214389046534583)
    probe(tq, 0.012, 3.6054389046534583, 3.6214389046534583,
          3.6194389046534585, 3.6214389046534583)
    print('PLUS twin [0.4638, 0.4798] (passed, for comparison):', flush=True)
    probe(0.00864, 0.012, 0.4638462510636653, 0.4798462510636653,
          0.4778462510636653, 0.4798462510636653)


if __name__ == '__main__':
    main()

"""Dissect the failing minus-wedge leaf at kappa = 0.05: mirror band_job's
radial walk for the failing angular cell and print every component's
enclosure (lbox, B_L, qB, quadT per radial piece)."""
import math
import time

from core import set_prec, endpoints
set_prec(50)
import certify_km_slab as C
import huang_cert_region1 as R1


def ep(b):
    lo, hi = endpoints(b)
    return '[%.4g, %.4g]' % (float(lo), float(hi))


def main():
    kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
    alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
    q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
    la = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
    lb = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
    R1.configure_region1(C.arb(C.dec('0.05')), alpha,
                         C.hull(la[0], lb[0]), C.hull(la[1], lb[1]))
    t0b, t1b, th0b, th1b = 0.00864, 0.012, 3.6054389046534583, \
        3.6214389046534583
    gz = R1.hg.get_zt_grid(9, R1.GRID_N_RAY)
    xc = R1.xhull_of_band(t0b, t1b, th0b, th1b)
    for pm in (1.0, 1.6, 2.4):
        fan, lbox = R1.fan_and_box(t0b, t1b, th0b, th1b, pm)
        lboxb = tuple(R1._exact_decimal(x) for x in lbox)
        try:
            R1._validate_lbox(lboxb)
        except ValueError as e:
            print('pad', pm, 'invalid lbox', e)
            continue
        okl = R1.edge_check(*lboxb, xc, fan)
        print('pad', pm, 'lbox', lbox, 'edge_check', okl, flush=True)
        if okl:
            break
    b11, b12, b22, cert = R1.B_Lambda(*lboxb)
    print('B_L: b11=%s b12=%s b22=%s' % (ep(b11), ep(b12), ep(b22)),
          flush=True)
    ta, tb_ = 3.6194389046534585, 3.6214389046534583
    thb = (R1._dec(ta, 8).union(R1._dec(tb_, 8))
           + R1._ANG_PAD.union(-R1._ANG_PAD))
    v1, v2 = thb.cos(), thb.sin()
    qB = R1.Binv_form(b11, b12, b22, v1, v2)
    print('qB =', ep(qB), flush=True)
    thc = 0.5 * (ta + tb_)
    sdf = R1._sdot_of(thc)
    print('sdot(float) =', sdf, flush=True)
    sdot = R1._dec(round(sdf, 6), 8)
    u, du = t0b, 4e-4
    while u < min(t1b, R1.T_max_over(ta, tb_)) - 1e-15:
        u1 = min(u + du, t1b)
        tt = (R1._dec(u, 12).union(R1._dec(u1, 12))
              + R1._RAD_PAD.union(-R1._RAD_PAD))
        x1 = R1.A1B + tt * v1
        x2 = R1.A2B + tt * v2
        sb = R1.S_BASE + tt * sdot
        t0 = time.time()
        qT = R1.quadT_box(x1, x2, sb, v1, v2, sdot, gz)
        val = None if qT is None else qT - qB
        print('u=[%.5f,%.5f] quadT=%s val=%s (%.0fs)'
              % (u, u1, 'None' if qT is None else ep(qT),
                 'None' if val is None else ep(val), time.time() - t0),
              flush=True)
        u = u1


if __name__ == '__main__':
    main()

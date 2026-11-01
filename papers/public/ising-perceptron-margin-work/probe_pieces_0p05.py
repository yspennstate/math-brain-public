"""Term-by-term widths of quadT at the failing minus leaf vs the passing
plus twin: T_derivs second derivatives, a_s mixed terms, Sss, and the
assembled form, at band_job's exact ball inputs."""
import math

from core import set_prec, endpoints
set_prec(50)
import certify_km_slab as C
import huang_cert_region1 as R1


def pr(name, b):
    lo, hi = endpoints(b)
    print('  %-8s [%10.4f, %10.4f]  w=%.3f'
          % (name, float(lo), float(hi), float(hi) - float(lo)), flush=True)


def probe(tag, ta, tb_, u, du):
    print('%s leaf th=[%.6f, %.6f] u=[%.5f, %.5f]:' % (tag, ta, tb_, u,
                                                       u + du), flush=True)
    gz = R1.hg.get_zt_grid(9, R1.GRID_N_RAY)
    thb = (R1._dec(ta, 8).union(R1._dec(tb_, 8))
           + R1._ANG_PAD.union(-R1._ANG_PAD))
    v1, v2 = thb.cos(), thb.sin()
    thc = 0.5 * (ta + tb_)
    sdf = R1._sdot_of(thc)
    print('  sdot = %.4f' % sdf, flush=True)
    sdot = R1._dec(round(sdf, 6), 8)
    tt = (R1._dec(u, 12).union(R1._dec(u + du, 12))
          + R1._RAD_PAD.union(-R1._RAD_PAD))
    x1 = R1.A1B + tt * v1
    x2 = R1.A2B + tt * v2
    sb = R1.S_BASE + tt * sdot
    Td = R1.hg.T_derivs(x1, x2, gz, sb)
    if Td is None:
        print('  T_derivs None', flush=True)
        return
    for k in ('d2T11', 'd2T12', 'd2T22'):
        pr(k, Td[k])
    asT1, asT2, Sss = R1.hg.a_s_mixed(x1, x2, sb, gz)
    pr('asT1', asT1)
    pr('asT2', asT2)
    pr('Sss', Sss)
    A = R1.ALPHA
    pr('aTerm', A * (v1 * v1 * Td['d2T11'] + 2 * v1 * v2 * Td['d2T12']
                     + v2 * v2 * Td['d2T22']))
    pr('sTerm', 2 * sdot * (v1 * asT1 + v2 * asT2))
    pr('ssTerm', sdot * sdot * Sss)
    pr('quadT', R1.quadT_box(x1, x2, sb, v1, v2, sdot, gz))


def main():
    kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
    alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
    q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
    la = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
    lb = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
    R1.configure_region1(C.arb(C.dec('0.05')), alpha,
                         C.hull(la[0], lb[0]), C.hull(la[1], lb[1]))
    probe('MINUS', 3.6194389046534585, 3.6214389046534583, 0.00864, 4e-4)
    probe('MINUS-thin', 3.6194389046534585, 3.6214389046534583,
          0.00864, 2.5e-5)
    probe('PLUS', 0.4778462510636653, 0.4798462510636653, 0.00864, 4e-4)


if __name__ == '__main__':
    main()

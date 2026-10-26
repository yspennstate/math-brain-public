"""Diagnose the weak-direction edge_check failures at kappa = 0.05:
print fan, lbox, validity, and the edge_check outcome per pad_mult."""
import time

from core import set_prec, endpoints
set_prec(50)
import certify_km_slab as C
import huang_cert_region1 as R1


def main():
    kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
    alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
    q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
    la = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
    lb = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
    R1.configure_region1(C.arb(C.dec('0.05')), alpha,
                         C.hull(la[0], lb[0]), C.hull(la[1], lb[1]))
    jobs = R1.bands()
    ch = [j for j in jobs if j[1] > 4.5e-4]
    for t1pick in (0.000624, 0.002322, 0.012):
        cand = [j for j in ch if abs(j[1] - t1pick) < 1e-5
                and j[2] <= R1.W_ANG < j[3]]
        if not cand:
            continue
        j = cand[0]
        print('== job', j, flush=True)
        xc = R1.xhull_of_band(*j)
        npoly = len(xc) if isinstance(xc[0][0], (tuple, list)) else 1
        print('  xhull polys:', npoly)
        for pm in (1.0, 1.6, 2.4):
            fan, lbox = R1.fan_and_box(j[0], j[1], j[2], j[3], pm)
            print('  pad_mult', pm, 'nfan', len(fan), 'lbox', lbox)
            lboxb = tuple(R1._exact_decimal(x) for x in lbox)
            try:
                R1._validate_lbox(lboxb)
            except ValueError as e:
                print('    INVALID lbox:', e)
                continue
            t0 = time.time()
            ok = R1.edge_check(*lboxb, xc, fan)
            print('    edge_check:', ok, '(%.0fs)' % (time.time() - t0))
            if ok:
                break


if __name__ == '__main__':
    main()

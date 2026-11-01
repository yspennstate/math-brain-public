"""Rerun the plus-side edge_check-failing band with the patched kernels
and per-pad diagnostics."""
import os
os.environ['R1_DEBUG'] = '1'

from core import set_prec
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
    band = (0.00864, 0.012, 0.7678462510636656, 0.7838462510636653)
    xc = R1.xhull_of_band(*band)
    for pm in (1.0, 1.6, 2.4):
        fan, lbox = R1.fan_and_box(band[0], band[1], band[2], band[3], pm)
        print('pad %.1f nfan=%d lbox=%s' % (pm, len(fan), lbox), flush=True)
        cand = tuple(R1._exact_decimal(x) for x in lbox)
        try:
            R1._validate_lbox(cand)
        except ValueError as e:
            print('  invalid:', e, flush=True)
            continue
        ok = R1.edge_check(*cand, xc, fan)
        print('  edge_check:', ok, flush=True)
        if ok:
            break
    r = R1.band_job(band)
    print('band -> ok=%s why=%s cells=%s nfail=%s worst=%s'
          % (r['ok'], r.get('why', '-'), r.get('cells'), r.get('nfail'),
             r.get('worst')), flush=True)


if __name__ == '__main__':
    main()

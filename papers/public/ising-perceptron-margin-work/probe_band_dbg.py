"""Rerun the two cell-failing minus-wedge bands with R1_DEBUG piece-level
failure prints (run from the dbg/ staging dir with the instrumented
huang_cert_region1)."""
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
    for band in ((0.00864, 0.012, 3.6054389046534583, 3.6214389046534583),
                 (0.00864, 0.012, 0.7678462510636656, 0.7838462510636653)):
        r = R1.band_job(band)
        print('band %s -> ok=%s why=%s cells=%s nfail=%s'
              % (band, r['ok'], r.get('why', '-'), r.get('cells'),
                 r.get('nfail')), flush=True)
        for f in r.get('fails', []):
            print('  fail leaf:', f, flush=True)


if __name__ == '__main__':
    main()

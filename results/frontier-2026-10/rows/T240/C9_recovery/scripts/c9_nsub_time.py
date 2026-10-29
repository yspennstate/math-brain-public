import os, sys, time, json
sys.path[:0] = ['.']
os.environ.setdefault('C9_U', '99/10000000'); os.environ.setdefault('C9_KAPPA', '1/500'); os.environ.setdefault('C9_HMAX', '0.5')
import c9_run as R, c9_blocks as CB
from c9_flow import F, fdrive, fl, ETA_F
P, Pinv, r_face, tq, nodes, slopes = R.setup('820', '0.004')
k = int(sys.argv[1]) if len(sys.argv) > 1 else 400
Pk, Pik, bl = CB.frame_b(fdrive.jac(fl(nodes[k]), ETA_F))
v = [F(1, 10**7)] * len(bl)
for ns in (24, 24):
    t0 = time.time()
    r = CB.segment_b(nodes[k], nodes[k+1], slopes[k], slopes[k+1], tq[k+1]-tq[k], Pk, Pik, bl, v, ns)
    print('k', k, 'nsub', ns, 'sec %.1f' % (time.time()-t0), 'd', ['%.2e' % x for x in r['d'][:3]] if r else None, flush=True)

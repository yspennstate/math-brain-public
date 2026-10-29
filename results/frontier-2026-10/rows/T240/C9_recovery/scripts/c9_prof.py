import os, sys, cProfile, pstats
sys.path[:0] = ['.']
os.environ.setdefault('C9_U', '99/10000000'); os.environ.setdefault('C9_KAPPA', '1/500'); os.environ.setdefault('C9_HMAX', '0.5')
import c9_run as R, c9_blocks as CB
from c9_flow import F, fdrive, fl, ETA_F
P, Pinv, r_face, tq, nodes, slopes = R.setup('820', '0.004')
k = 400
Pk, Pik, bl = CB.frame_b(fdrive.jac(fl(nodes[k]), ETA_F))
v = [F(1, 10**7)] * len(bl)
cProfile.run('CB.segment_b(nodes[k], nodes[k+1], slopes[k], slopes[k+1], tq[k+1]-tq[k], Pk, Pik, bl, v, 24)', 'logs/prof.out')
pstats.Stats('logs/prof.out').sort_stats('tottime').print_stats(14)

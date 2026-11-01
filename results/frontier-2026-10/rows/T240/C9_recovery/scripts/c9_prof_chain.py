import os, sys, cProfile, pstats
sys.path[:0] = ['.']
os.environ.setdefault('C9_U', '99/10000000'); os.environ.setdefault('C9_KAPPA', '1/500'); os.environ.setdefault('C9_HMAX', '0.5')
import c9_run as R, c9_blocks as CB
from c9_flow import F, fdrive, fl, ETA_F
P, Pinv, r_face, tq, nodes, slopes = R.setup('820', '0.004')
k = 12
Pk, Pik, bl = CB.frame_b(fdrive.jac(fl(nodes[k]), ETA_F))
v = [F(0)] + [F(2, 10**8)] * (len(bl) - 1)
cProfile.run("CB.run_chain_b(tq, nodes, slopes, Pk, Pik, bl, v, k, k+3, 'logs/prof_chain.jsonl', nsub=24)", 'logs/prof_chain.out')
pstats.Stats('logs/prof_chain.out').sort_stats('cumtime').print_stats(25)

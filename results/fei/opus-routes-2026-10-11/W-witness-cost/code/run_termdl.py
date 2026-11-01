"""Evidence: queue-law code length on term decision lists, natural vs sorted per-gate order.
Usage: python run_termdl.py WMAX NSETS"""
import sys
import random
import math
from termdl import TermDL

if __name__ == '__main__':
    wmax = int(sys.argv[1])
    nsets = int(sys.argv[2])
    rng = random.Random(3)
    for fam in ('TD1', 'TD2'):
        for w in range(2, wmax + 1):
            m = 2 ** w
            outs = [('dict', 1)] * m + ([('dict', 1)] if fam == 'TD1' else [('const-1', 0)])
            dl = TermDL([w] * m, outs)
            I = dl.influence()
            r_nat = dl.code_length_mc(rng, 'natural', nsets)
            r_srt = dl.code_length_mc(rng, 'sorted', nsets)
            print(f"{fam} w={w} m={m} v={dl.v:.4f} I={I:.4f}  natural: total/I={r_nat['total']/I:.3f} "
                  f"(rank/I={r_nat['rank']/I:.3f}, root/I={r_nat['root']/I:.3f})  sorted: total/I={r_srt['total']/I:.3f} "
                  f"(rank/I={r_srt['rank']/I:.3f})", flush=True)

"""Finite independent checks of the block algebra used in Theorem A."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import os
import time
from rwrs_exact import cut_edges, polymer_probability, brute_probability


def main():
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    started = time.monotonic()
    words = 0
    blocks = 0
    for length in range(15):
        for word in product((-1,1), repeat=length):
            s = [0]
            for x in word:
                s.append(s[-1]+x)
            cuts = cut_edges(s)
            endpoints = [-1]+cuts+[length]
            for k in range(len(endpoints)-1):
                u,v = endpoints[k]+1,endpoints[k+1]
                piece = s[u:v+1]
                local = [x-piece[0] for x in piece]
                assert not cut_edges(local)
                ell = word[u:v].count(-1)
                assert v-u <= 3*ell
                if u:
                    assert min(local) == 0
                if v < length:
                    assert max(local) == local[-1]
                if k:
                    assert max(s[:u]) < min(piece)
                for hole in (None, u, v):
                    constrained_sites = {s[j] for j in range(u,v+1) if j != hole}
                    h = v-u+1-int(hole is not None)
                    assert h-len(constrained_sites) <= 2*ell
                blocks += 1
            words += 1
    exact = 0
    for colours in product((0,1), repeat=6):
        record = list(colours[:3])+[None]+list(colours[3:])
        for p in (Fraction(4,5),Fraction(199,200)):
            assert polymer_probability(record,p) == brute_probability(record,p)
            exact += 1
    text = (f'walk_words_checked={words}\nblocks_checked={blocks}\n'
            f'exact_hole_record_factorizations={exact}\n'
            f'max_walk_length=14\nnice={os.getpriority(os.PRIO_PROCESS,0)}\n'
            f'elapsed_seconds={time.monotonic()-started:.6f}\nall_passed=true\n')
    Path('data/proof_audit.txt').write_text(text)
    print(text)


if __name__ == '__main__':
    main()

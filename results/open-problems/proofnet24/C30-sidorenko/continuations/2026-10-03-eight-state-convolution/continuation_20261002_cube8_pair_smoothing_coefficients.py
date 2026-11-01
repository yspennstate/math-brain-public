"""Exact eight-state pair smoothing coefficient exploration, no theorem claim."""
from pathlib import Path
from collections import Counter
from itertools import product
from math import comb
import json


def encode(P):return {','.join(map(str,a)):int(v) for a,v in sorted(P.items()) if v}

def expand_pairs(poly, upper):
    answer=Counter()
    for n,c in poly.items():
        ns=[n[upper[i]] for i in range(4)]
        totals=[n[2*i]+n[2*i+1] for i in range(4)]
        for k in product(*(range(v+1) for v in ns)):
            exp=tuple(z for i in range(4) for z in [totals[i]-k[i],k[i]])
            coeff=c
            for i in range(4):coeff*=comb(ns[i],k[i])
            answer[exp]+=coeff
    return answer


def main():
    path=Path(__file__).with_suffix('.json')
    poly={}
    for line in Path(__file__).with_name('continuation_20261002_cube8_vertex_polynomial.tsv').read_text().splitlines():
        key,c=map(int,line.split());n=tuple((key>>(4*i))&15 for i in range(8));assert sum(n)==15
        poly[n]=8**6*c
    four=json.loads(Path(__file__).with_name('continuation_20261002_klein4_schur.json').read_text())['density_polynomial']
    smooth=Counter()
    for raw,c in four.items():
        n=tuple(map(int,raw.split(',')))
        for k in product(*(range(v+1) for v in n)):
            exp=tuple(z for i in range(4) for z in [n[i]-k[i],k[i]])
            coeff=c
            for i in range(4):coeff*=comb(n[i],k[i])*2**(n[i]-k[i])
            smooth[exp]+=coeff
    out={'status':'exact coefficient exploration; no theorem claim','vertex_monomials':len(poly),'records':{}}
    for mode,upper in [('even',[0,2,4,6]),('odd',[1,2,4,6])]:
        print('expanding',mode,flush=True)
        gap=expand_pairs(poly,upper);gap.subtract(smooth)
        gap={a:v for a,v in gap.items() if v}
        negative=[(a,v) for a,v in gap.items() if v<0]
        out['records'][mode]={'gap_nonzero_terms':len(gap),'negative_terms':len(negative),
                              'gap_coefficients':encode(gap),
                              'negative_examples':[(list(a),v) for a,v in negative[:20]]}
        print(mode,'terms',len(gap),'negative',len(negative),flush=True)
        path.write_text(json.dumps(out,indent=2))
    print(json.dumps({k:{x:y for x,y in v.items() if x!='gap_coefficients'} for k,v in out['records'].items()},indent=2))
if __name__=='__main__':main()

"""Exact exponentiated-KL verification of optional reset histories, v1."""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import time
import quadratic_audit as Q

assertions = 0
edges_checked = 0
reference_only = 0
def ck(b,tag):
    global assertions
    assertions += 1
    if not b:
        raise AssertionError(tag)

@lru_cache(maxsize=20000)
def walk(tab,ref,allow_reset):
    global edges_checked,reference_only
    z = Q.info(tab)
    weights = {ref[s] for s,p in enumerate(z['p']) if p}
    ck(len(weights) == 1 and sum(ref) == 1,'constant normalized reference on actual affine support')
    c = next(iter(weights))
    ck(0 < c <= F(1,1 << z['r']),'finite nonnegative source KL')
    best = F(1)
    # exp2(TC-K) = 2^m c, valid even when its log is not dyadic/integer.
    reset_ratio = (1 << z['m'])*c
    if allow_reset and ref != z['Q']:
        best = max(best,max(F(1),reset_ratio)*walk(tab,z['Q'],False))
    n = len(tab).bit_length()-1
    for i in range(n):
        edges_checked += 1
        N = len(tab)//2
        erased = [z['p'][Q.insert(t,i,0)]+z['p'][Q.insert(t,i,1)] for t in range(N)]
        erased_ref = [ref[Q.insert(t,i,0)]+ref[Q.insert(t,i,1)] for t in range(N)]
        source_ref = {erased_ref[t] for t,a in enumerate(erased) if a}
        ck(len(source_ref) == 1,'erased reference constant on erased source support')
        cbar = next(iter(source_ref))
        for b in (0,1):
            child = Q.restrict(tab,i,b)
            child_info = Q.info(child)
            drop = (z['r']-child_info['r'])//2 if z['rows'][i] else 0
            # E = log2(cbar/c)-drop. Test the necessary bounds without logs.
            erasure_ratio = cbar/(c*(1 << drop))
            ck(1 <= erasure_ratio <= (1 if drop else 2),'ordinary erasure loss bound')
            new = tuple(erased_ref[t]*(child_info['p'][t]/(2*erased[t]) if erased[t] else F(1,2)) for t in range(N))
            reference_only += sum(erased[t] == 0 and erased_ref[t] > 0 for t in range(N))
            mass = sum(new)
            ck(mass == F(1,2),'actual outcome fair on all retained rows')
            new = tuple(a/mass for a in new)
            new_source = {new[s] for s,p in enumerate(child_info['p']) if p}
            ck(new_source == {cbar*(1 << drop)},'both actual source KL values use correct density')
            best = max(best,walk(child,new,True))
    return best

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pilot',action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    roots = 0
    maxima = {}
    for n in range((3 if args.pilot else 4)+1):
        pairs = list(itertools.combinations(range(n),2))
        max_factor = F(1)
        for mask in range(1 << len(pairs)):
            edges = [e for j,e in enumerate(pairs) if mask >> j & 1]
            tab = Q.make(n,edges,0,0)
            z = Q.info(tab)
            factor = walk(tab,z['Q'],False)
            ck(factor <= (1 << max(0,z['r']//2-1)),'all optional histories retain original rank bank')
            max_factor = max(max_factor,factor)
            roots += 1
        maxima[n] = str(max_factor)
    result = {'status':'PASS','mode':'pilot' if args.pilot else 'main','roots':roots,
              'query_states':edges_checked,'assertions':assertions,'helper_assertions':Q.ASSERTIONS,
              'positive_reference_only_rows_retained':reference_only,'max_gross_exp2_by_n':maxima,
              'memo':str(walk.cache_info()),'elapsed_seconds':round(time.monotonic()-started,3),
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'arithmetic':'exact rational comparisons of exponentiated KL; no floating logs'}
    out = Path(__file__).resolve().parent.parent/'out'/('prefix_pilot.json' if args.pilot else 'prefix_main.json')
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__ == '__main__':
    main()

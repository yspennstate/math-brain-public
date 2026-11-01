import argparse, json, time, hashlib
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction
from phase_exact import walsh, direct_walsh, admit, VERSION

ROOT = Path(__file__).resolve().parents[1]

def patterns(length, target, allowed, prefix=()):
    if not length:
        if target == 0:
            yield prefix
        return
    for v in allowed:
        if v*v <= target:
            yield from patterns(length-1, target-v*v, [a for a in allowed if a<=v], prefix+(v,))

def placements(pattern):
    N=len(pattern)
    counts=Counter(pattern)
    kinds=sorted([x for x in counts if x], reverse=True)
    a=[0]*N
    def rec(k, available):
        if k == len(kinds):
            yield tuple(a)
            return
        value=kinds[k]
        for selected in combinations(available, counts[value]):
            selected=set(selected)
            for i in selected: a[i]=value
            yield from rec(k+1, tuple(i for i in available if i not in selected))
            for i in selected: a[i]=0
    yield from rec(0, tuple(range(N)))

def run(n):
    started=time.monotonic(); N=1<<n
    laws={}; counts=Counter()
    for mask in range(1<<(N-1)):
        truth=[1]+[-1 if mask & (1<<(i-1)) else 1 for i in range(1,N)]
        a=walsh(truth)
        assert sum(v*v for v in a)==N*N
        inverse=walsh(a)
        assert inverse==[N*v for v in truth]
        # Different representation verifies the transform, all n<=3, first64 n=4.
        if n<=3 or mask<64: assert direct_walsh(truth)==a
        key=tuple(abs(v) for v in a)
        if key not in laws: laws[key]=mask
        counts[key]+=1
    with (ROOT/'out'/f'catalogue_n{n}.jsonl').open('w') as f:
        for law,mask in sorted(laws.items()):
            f.write(json.dumps({'magnitudes':law,'truth_mask_with_first_value_positive':mask,'phase_multiplicity_mod_global_sign':counts[law]})+'\n')
    domain_patterns=[]
    if n==0: domain_patterns=[(1,)]
    elif n==1: domain_patterns=[(2,0)]
    else:
        for residue in (0,2):
            domain_patterns.extend(patterns(N,N*N,list(range(residue,N+1,4))))
    ledger=[]; examples=[]; cases=0
    for pat in domain_patterns:
        accepted=rejected=0; first_bad=None
        for a in placements(pat):
            cases+=1
            if a in laws: accepted+=1
            else:
                rejected+=1
                if first_bad is None: first_bad=a
        row={'pattern':pat,'realizable_laws':accepted,'impossible_laws':rejected}
        ledger.append(row)
        if first_bad is not None:
            cert=admit([Fraction(v*v,N*N) for v in first_bad])
            assert cert['status']=='IMPOSSIBLE'
            examples.append({'magnitudes':first_bad,'probability_denominator':N*N,'certificate':cert})
    assert sum(row['realizable_laws'] for row in ledger)==len(laws)
    # Flat <=4 supports: independent phase checker and full truth catalogue agree.
    flat_counts={}
    for k in (1,2,3,4):
        if k>N: continue
        good=bad=0
        for support in combinations(range(N),k):
            p=[Fraction(1,k) if s in support else Fraction(0) for s in range(N)]
            result=admit(p)
            if result['status']=='REALIZABLE':
                good+=1
                a=tuple(abs(v) for v in direct_walsh(result['truth_table']))
                assert a in laws
            else:
                assert result['status']=='IMPOSSIBLE'; bad+=1
        flat_counts[k]={'realizable':good,'impossible':bad}
    result={'n':n,'helper_version':VERSION,'truth_tables_mod_global_sign':1<<(N-1),'distinct_spectral_laws':len(laws),'integer_magnitude_candidate_laws':cases,'pattern_ledger':ledger,'flat_support_checks':flat_counts,'impossibility_examples':examples,'seconds':time.monotonic()-started}
    (ROOT/'out'/f'summary_n{n}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--n',type=int,nargs='+',required=True)
    args=parser.parse_args()
    for n in args.n:
        assert 0<=n<=4
        run(n)

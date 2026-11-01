"""Frozen exact physical-overlap tests, original labels and both children retained."""
import hashlib, importlib.util, itertools, json, sys, time
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]; O=R/'out'
PREV=R.parent/'20261023T115918Z-fleet03-A017-recursive-addressing'
SRC=R.parent/'20261021T213328Z-fleet03-A017-recursive-addressing/out/boolean_counterexample.json'
s=importlib.util.spec_from_file_location('a017_previous',PREV/'code/check.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
fw,H,add,split=m.fw,m.H,m.add,m.split
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):(O/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def logs(p):return m.ln_bounds(p)
def lower(d):return sum((c*logs(p)[0 if c>=0 else 1] for p,c in d.items()),F(0))
def entropy_delta(t,i):
    a,b,_=split(t,list(range(len(t).bit_length()-1)),i)
    return add(H(t),add(H(a),H(b)),F(-1,2))
def sector(t,i,average=False):
    a,b,_=split(t,list(range(len(t).bit_length()-1)),i)
    return [(x+y)//2 if average else (x-y)//2 for x,y in zip(a,b)]
def energy(d):
    N=len(d); n=N.bit_length()-1; p=F(sum(v*v for v in d),N)
    es=[F(sum((d[x]-d[x^(1<<j)])**2 for x in range(N)),4*N) for j in range(n)]
    w=fw(d)
    assert p==F(sum(v*v for v in w),N*N)
    assert sum(es)==F(sum(s.bit_count()*v*v for s,v in enumerate(w)),N*N)
    return p,es
def phase(d,T):return [v*(-1 if (x&T).bit_count()%2 else 1) for x,v in enumerate(d)]
def coeff(d):return {str(p):str(c) for p,c in d.items()}
def freeze():
    O.mkdir(parents=True,exist_ok=True)
    save('spec.json',dict(helper_version='A017-overlap-phase-and-real-debit-v1',helper_sha256=sha(Path(__file__)),
      inherited_helper_sha256=sha(PREV/'code/check.py'),source_sha256=sha(SRC),
      family='Saved six-bit Boolean b times EVERY Boolean c on each three-element subset of its five unqueried original coordinates; no new coordinates',
      domain='10 subsets times256 truth tables=2560 actual Boolean roots; selected query original0; both full actual children',
      case_count=2560,symmetry='None; duplicate lower-support functions intentionally retained',
      phase_validation='All256 Boolean three-bit roots, all3 selected queries, both sectors, all4 unqueried characters:6144 sector-phase rows',
      arithmetic='Integer Walsh and independent exact physical-edge energies; Fraction prime-log entropy;48-term rational atanh logarithm enclosures',
      pilot='First subset,32 multipliers; first16 three-bit roots; frozen subset, not automatic growth',
      memory_estimate_MB=70,max_runtime_seconds=300,pilot_max_runtime_seconds=60))
    print('FROZEN:2560 shared-support roots;6144 sector-phase rows;70MB;300s')
def run(pilot):
    spec=json.loads((O/'spec.json').read_text(encoding='utf-8'))
    assert spec['helper_sha256']==sha(Path(__file__)) and spec['source_sha256']==sha(SRC)
    assert spec['inherited_helper_sha256']==sha(PREV/'code/check.py')
    start=time.monotonic(); tests=0; phase_rows=0
    for code in range(16 if pilot else 256):
        f=[1-2*((code>>x)&1) for x in range(8)]
        for i in range(3):
            delta=entropy_delta(f,i)
            for average in (False,True):
                d=sector(f,i,average); p,es=energy(d); ep=sum(min(e,p-e) for e in es)
                all_e=[]
                for T in range(4):
                    dp=phase(d,T); pp,ee=energy(dp)
                    assert pp==p
                    assert sum(ee)==sum(es)+p*T.bit_count()-2*sum(es[j] for j in range(2) if T&(1<<j))
                    # Full physical character and optional query-character implement BOTH sectors.
                    rest=[j for j in range(3) if j!=i]
                    physical=sum(1<<rest[j] for j in range(2) if T&(1<<j))
                    if average:physical|=1<<i
                    fp=phase(f,physical)
                    assert H(fp)==H(f) and entropy_delta(fp,i)==delta
                    all_e.append(sum(ee));phase_rows+=1;tests+=4
                assert min(all_e)==ep
                assert lower(add({2:2*ep},delta,F(-1)))+3*p>=0
                tests+=2
    base=json.loads(SRC.read_text(encoding='utf-8-sig'))['truth_table']
    db=sector(base,0); p,eb=energy(db); assert p==F(1,8)
    rows=[];best=None;positive=negative=equal=0
    subsets=list(itertools.combinations(range(1,6),3))
    for J in (subsets[:1] if pilot else subsets):
        for code in range(32 if pilot else 256):
            c=[1-2*((code>>sum(((x>>j)&1)<<k for k,j in enumerate(J)))&1) for x in range(64)]
            f=[a*b for a,b in zip(base,c)]; delta=entropy_delta(f,0)
            d=sector(f,0); pf,ef=energy(d); assert pf==p
            compact_c=c[::2]
            correction=sum((F(sum((db[x]*db[x^(1<<j)] if compact_c[x]!=compact_c[x^(1<<j)] else 0) for x in range(32)),32) for j in range(5)),F(0))
            assert sum(ef)-sum(eb)==correction
            # Natural log of actual debit minus K*p, K=4+2/ln2.
            gap=add(delta,{2:4*p},F(-1)); lo=lower(gap)-2*p; hi=-lower({q:-v for q,v in gap.items()})-2*p
            if lo>0:verdict='EXCEEDS_SAME_K';positive+=1
            elif hi<0:verdict='PAID_SAME_K';negative+=1
            elif not gap and p==0:verdict='EQUAL';equal+=1
            else:raise AssertionError('unresolved logarithmic interval')
            row=dict(subset=list(J),multiplier_code=code,verdict=verdict,delta=coeff(delta),derivative_energy=str(sum(ef)),phase_min_energy=str(sum(min(e,p-e) for e in ef)),signed_correction=str(correction))
            rows.append(row);tests+=3
            if best is None or lower(add(delta,best[0],F(-1)))>0:best=(delta,row,f,c)
        assert time.monotonic()-start<(60 if pilot else 300)
    # Independently check claimed maximum and the retained full witness children.
    for r in rows:
        other={int(q):F(v) for q,v in r['delta'].items()}
        assert lower(add(best[0],other,F(-1)))>=0
    tests+=len(rows)
    witness=dict(best[1],truth_table=best[2],multiplier_truth_table=best[3],full_children=[best[2][::2],best[2][1::2]])
    assert H(best[2],True)==H(best[2]);tests+=1
    result=dict(status='PASS',pilot=pilot,roots=len(rows),sector_phase_rows=phase_rows,assertions=tests,
      paid=negative,exceeds=positive,equal=equal,best=witness,rows=rows,elapsed_seconds=time.monotonic()-start,
      proof_scope='Finite exact validation only; all-dimensional phase identities are proved separately; author verification, no external review')
    save('pilot.json' if pilot else 'certificate.json',result)
    print(json.dumps({k:result[k] for k in ['status','pilot','roots','sector_phase_rows','assertions','paid','exceeds','elapsed_seconds']}))
    print(json.dumps({'best':{k:v for k,v in witness.items() if 'truth' not in k and k!='full_children'}}))
if __name__=='__main__':
    if '--freeze' in sys.argv:freeze()
    else:run('--pilot' in sys.argv)

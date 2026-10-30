"""v1: labelled-block reproduction independent of formula simplification/orbits."""
import descent_compositions as d
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
import ast, json, time, sys, hashlib

ROOT=Path(__file__).resolve().parent.parent
@lru_cache(maxsize=4096)
def stats(t): return d.spectrum_table(t)
def truth_g(n,modified=False):
    clauses={6:[(0,1),(2,3),(0,2,4),(1,3,5) if modified else (2,4,5)],
             8:[(0,1),(2,3),(2,4,5),(0,2,4,6),(1,2,5,7) if modified else (2,4,6,7)]}[n]
    return tuple(int(all(any(z>>i&1 for i in c) for c in clauses)) for z in range(1<<n))
def hybrid(s):
    g=truth_g(6)
    if s==1: leaf=(0,1)
    else: leaf=tuple(int(z!=(1<<s)-1) for z in range(1<<s))
    return tuple(1-g[z&63]*leaf[z>>6] for z in range(1<<(6+s)))

def run(t,name,deadline,reference=None):
    n=(len(t)-1).bit_length(); H,ii=stats(t); I=sum(ii)
    aa=d.fwht([2*x-1 for x in t])
    bb=[sum((2*v-1)*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
    d.ck(aa==bb)
    rows=[]
    for A in range(1,(1<<n)-1):
        ai=[i for i in range(n) if A>>i&1]; bi=[i for i in range(n) if not A>>i&1]
        am=[sum(((z>>j)&1)<<i for j,i in enumerate(ai)) for z in range(1<<len(ai))]
        bm=[sum(((z>>j)&1)<<i for j,i in enumerate(bi)) for z in range(1<<len(bi))]
        counts=Counter(tuple(t[a|b] for b in bm) for a in am)
        avg=d.add((F(count,len(am)),stats(u)[0]) for u,count in counts.items())
        IA=sum(ii[i] for i in ai); d.ck(IA+sum(F(count,len(am))*sum(stats(u)[1]) for u,count in counts.items())==I)
        L=d.add([(1,H),(-1,avg)]); ratio={p:x/IA for p,x in L.items()}
        rows.append({'mask':A,'ratio':d.enc(ratio),'interval':d.ei(d.interval(ratio))})
        if time.perf_counter()>deadline: raise TimeoutError('Frozen runtime cap')
    minhi=min(F(r['interval'][1]) for r in rows)
    winners=[r for r in rows if F(r['interval'][0])<=minhi]
    d.ck(all(r['ratio']==winners[0]['ratio'] for r in winners))
    phi=d.interval({int(p):F(x) for p,x in winners[0]['ratio'].items()}); R=d.interval({p:x/I for p,x in H.items()})
    if reference:
        d.ck(d.enc(H)==reference['H']); d.ck(str(I)==reference['I'])
        d.ck(d.ei(phi)==reference['phi'])
        bymask={r['mask']:r for r in rows}
        for r in reference['all_orbits']: d.ck(bymask[r['mask']]['ratio']==r['ratio'])
    # Independent root/direct children also certify the co-singleton proof.
    for i in range(n):
        A=((1<<n)-1)^(1<<i)
        d.ck(bymask[A]['ratio']==d.enc({p:x/(I-ii[i]) for p,x in H.items()})) if reference else None
    relative=(phi[0]/R[1],phi[1]/R[0])
    d.ck(relative[1]<F(n,n-1)+F(1,1<<90))
    return {'name':name,'n':n,'truth_sha256':hashlib.sha256(bytes(t)).hexdigest(),'H':d.enc(H),'I':str(I),'R':d.ei(R),'phi':d.ei(phi),'phi_over_R':d.ei(relative),'minimizing_masks':[r['mask'] for r in winners],'minimizing_block_sizes':sorted(set(r['mask'].bit_count() for r in winners)),'phi_gt_227_over_50':phi[0]>F(227,50),'labelled_blocks':len(rows),'all_labelled_blocks':rows}

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'; started=time.perf_counter(); cap=55 if mode=='pilot' else 300
    named=[('Hod_g3',truth_g(6)),('Hod_g3_prime',truth_g(6,True)),('Hod_g4',truth_g(8)),('Hod_g4_prime',truth_g(8,True))]+[(f'NAND_Hod_g3_PD_{s}',hybrid(s)) for s in (1,2,3)]
    if mode=='pilot': named=named[:2]
    summaries=[]
    for name,t in named:
        r=run(t,name,started+cap)
        d.save('out/seed_'+name+'.json',r)
        summaries.append({k:v for k,v in r.items() if k!='all_labelled_blocks'})
    replay=[]
    if mode=='full':
        summary=json.loads((ROOT/'out/full_SUMMARY.json').read_text())
        chosen=set()
        for n in range(6,10):
            ix=[i for i,r in enumerate(summary['cases']) if r['n']==n]
            chosen.add(max(ix,key=lambda i:F(summary['cases'][i]['phi'][0])))
            chosen.add(max(ix,key=lambda i:F(summary['cases'][i]['ratio_H_I'][0])))
        for i in sorted(chosen):
            ref=json.loads((ROOT/f'out/full_case_{i:04d}.json').read_text())
            t=d.tables(ast.literal_eval(ref['tree']))
            r=run(t,'replay_'+str(i),started+cap,ref)
            d.save(f'out/replay_{i:04d}.json',r)
            replay.append({k:v for k,v in r.items() if k!='all_labelled_blocks'})
    result={'status':'PASS','mode':mode,'helper_version':'A051-labelled-block-replay-v1','assertions':d.ASSERTIONS,'runtime_seconds':time.perf_counter()-started,'seed_cases':summaries,'replay_cases':replay,'total_labelled_blocks':sum(r['labelled_blocks'] for r in summaries+replay)}
    d.save('out/SEEDED_'+mode.upper()+'_SUMMARY.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('seed_cases','replay_cases')},indent=2))
if __name__=='__main__': main()

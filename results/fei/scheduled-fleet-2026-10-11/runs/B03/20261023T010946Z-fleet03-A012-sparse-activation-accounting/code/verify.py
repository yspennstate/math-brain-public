from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product,permutations
import json,time,sys
R=Path(__file__).resolve().parents[1];O=1<<64;CHECKS=0
def ck(v):
    global CHECKS
    assert v,CHECKS;CHECKS+=1
# Reconstructed from A013 stage17 replay.py; no source module imported.
@lru_cache(maxsize=60000)
def upperlog(n,d):
    assert n>=d>0
    k=0
    while n>=2*d:d*=2;k+=1
    S=1<<160;lo=n*S//d;hi=(n*S+d-1)//d;pre=k*O
    for bit in range(1,65):
        lo=lo*lo//S;hi=(hi*hi+S-1)//S
        if lo>=2*S:pre+=1<<(64-bit);lo//=2;hi=(hi+1)//2
        elif hi>=2*S:return pre+(1<<(65-bit))
    return pre+1
def ch(s,t):return (-1)**((s&t).bit_count()%2)
def walsh(c):return [sum(c[s]*ch(s,t) for s in range(8)) for t in range(8)]
def seed(j,D):
    flags=[0]*8
    if j in (1,2):flags[1]=1
    if j==2:flags[2]=1
    if j in (3,4):flags[0]=1
    if j==4:flags[1]=1
    return [D*x//2 for x in flags],[D*(x+1)//2 for x in flags]
def classify():
    global CHECKS
    t0=time.perf_counter();types={};maps={};sym=[]
    for u,v,w in permutations(range(1,8),3):
        im=[(u if s&1 else 0)^(v if s&2 else 0)^(w if s&4 else 0) for s in range(8)]
        if len(set(im))==8:sym.append(im)
    ck(len(sym)==168)
    for mask in range(256):
        c=[(-1)**((mask>>s)&1) for s in range(8)];a=walsh(c);n=sum(x!=0 for x in a);types[n]=types.get(n,0)+1
        ck(n in (1,4,8));ck(sum(x*x for x in a)==64)
        if n==8:
            witnesses=[(sg,t,w) for sg in (-1,1) for t in range(8) for w in range(8) if all(c[s]==sg*ch(s,t)*(-1 if s==w else 1) for s in range(8))]
            ck(len(witnesses)==1);maps[str(mask)]=witnesses[0]
            ck(sorted(abs(x) for x in a)==[2]*7+[6])
    seeds=[];counts={str(j):0 for j in range(5)};moderate=0
    for flags in product((0,1),repeat=8):
        if sum(flags)>=3:ck(3*sum(flags)>=8);moderate+=1;seeds.append({'flags':flags,'kind':'moderate'});continue
        count=sum(flags[1:]);j=count if flags[0]==0 else 3+count
        lo,_=seed(j,2);mp=next((im for im in sym if all(flags[im[s]]==lo[s] for s in range(8))),None)
        ck(mp is not None);counts[str(j)]+=1;seeds.append({'flags':flags,'job':j,'permutation':mp})
    ck(list(counts.values())==[1,7,21,1,7]);ck(moderate==219)
    out={'status':'PASS','phase_type_counts':types,'point_phase_maps':maps,'seed_maps':seeds,'seed_multiplicities':counts,'analytic_seed_boxes':moderate,'GL_maps':sym,'exact_assertions':CHECKS,'seconds':time.perf_counter()-t0}
    (R/'out'/'CLASSIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print({k:v for k,v in out.items() if k not in ('point_phase_maps','seed_maps','GL_maps')});CHECKS=0
def run(job):
    global CHECKS
    t0=time.perf_counter();x=json.loads((R/'out'/f'CONTINUUM_{job}.json').read_text(encoding='utf-8'));D=x['denominator']
    ck(x['status']=='PASS' and not x['unresolved']);ck(D==128)
    c=[-1]+[1]*7;a=walsh(c);mm=[[c[s]*ch(s,t) for s in range(8)] for t in range(8)]
    def key(lo,hi):return tuple(lo),tuple(hi)
    nodes={}
    for label in ('leaves','pruned','splits'):
        for lo,hi,v in x[label]:
            k=key(lo,hi);ck(k not in nodes);ck(all(0<=lo[i]<hi[i]<=D for i in range(8)));nodes[k]=(label,v)
    todo=[key(*seed(job,D))];seen=set();minimum=None
    while todo:
        k=todo.pop();ck(k in nodes and k not in seen);seen.add(k);lo,hi=k;kind,v=nodes[k]
        if kind=='splits':
            j=v;ck(0<=j<8 and hi[j]-lo[j]>=2);m=(lo[j]+hi[j])//2
            h=list(hi);h[j]=m;l=list(lo);l[j]=m;todo.extend([key(lo,h),key(l,hi)]);continue
        if kind=='pruned':
            ck((v=='rare' and 4*sum(hi)<=D) or (v=='moderate' and 3*sum(lo)>=4*D));continue
        mid=[lo[j]+hi[j] for j in range(8)];sl=[]
        for t in range(8):
            b=sum(mm[t][j]*mid[j] for j in range(8));aa=(2*D*a[t]-b)**2;bb=b*b
            nu,de=(1,4096) if not bb else ((4095,4096) if not aa else (bb,aa+bb))
            lam=upperlog(de,de-nu);mu=upperlog(de,nu);ck(lam+mu>=2*O);sl.append((lam,mu))
        worst=None
        # Direct corner character sums; no quadratic matrix or Gray recurrence.
        for bits in product((0,1),repeat=8):
            q=[hi[j] if bits[j] else lo[j] for j in range(8)];val=-16*D*O*sum(q)
            for t,(lam,mu) in enumerate(sl):
                b=sum(mm[t][j]*q[j] for j in range(8));val+=lam*(D*a[t]-b)**2+(mu-2*O)*b*b
            worst=val if worst is None else max(worst,val)
        ck(worst<0);gap=F(-worst,64*D*D*O);minimum=gap if minimum is None else min(gap,minimum)
        if time.perf_counter()-t0>52:raise RuntimeError('52 second verification cap, no PASS')
    ck(seen==set(nodes))
    out={'status':'PASS','job':job,'exact_assertions':CHECKS,'nodes':len(nodes),'leaves':len(x['leaves']),'minimum_gap':str(minimum),'seconds':time.perf_counter()-t0,'arithmetic':'binary-squaring160/64 log; direct256-corner character sums; exact recursive tree coverage'}
    (R/'out'/f'VERIFY_{job}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out),flush=True);CHECKS=0;upperlog.cache_clear()
if __name__=='__main__':
    if sys.argv[1]=='classify':classify()
    else:
        for j in map(int,sys.argv[1:]):run(j)

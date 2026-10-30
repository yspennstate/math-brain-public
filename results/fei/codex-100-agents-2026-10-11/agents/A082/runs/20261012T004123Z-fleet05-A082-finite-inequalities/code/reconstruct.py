import argparse,json,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
LOW=[0x55555555,0x33333333,0x0f0f0f0f,0x00ff00ff,0x0000ffff]
HIGH=[0xffffffff^x for x in LOW]
FAST=1<<40;PRECISE=1<<110
def ln_interval(r):
    z=(r-1)/(r+1);term=z;v=Q(0)
    for j in range(50):v+=term/Q(2*j+1);term*=z*z
    return 2*v,2*v+2*term/(101*(1-z*z))
L2,U2=ln_interval(Q(2))
def log_interval(m):
    k=m.bit_length()-1
    if m==1<<k:return k*PRECISE,k*PRECISE
    lo,hi=ln_interval(Q(m,1<<k))
    return (PRECISE*(k+lo/U2)).__floor__(),(PRECISE*(k+hi/L2)).__ceil__()
LOGS={m:log_interval(m) for m in range(1,513)}
def g(a,b):
    if not a or not b:return 0,0
    tl,tu=LOGS[a+b];al,au=LOGS[a];bl,bu=LOGS[b]
    return (a+b)*tl-a*au-b*bu,(a+b)*tu-a*al-b*bl
def factors(m):
    d={};p=2
    while p*p<=m:
        while m%p==0:d[p]=d.get(p,0)+1;m//=p
        p+=1
    if m>1:d[m]=d.get(m,0)+1
    return d
def vector(packets,D):
    out=defaultdict(int)
    for a,b in packets:
        if not a or not b:continue
        for m,c in [(a+b,a+b),(a,-a),(b,-b)]:
            for p,e in factors(m).items():out[p]+=c*e
    return {p:Q(c,D) for p,c in out.items() if c}
def vector_sign(v):
    from math import lcm
    d=lcm(*(c.denominator for c in v.values()));lhs=rhs=1
    for p,c in v.items():
        e=int(c*d)
        if e>0:lhs*=p**e
        elif e<0:rhs*=p**(-e)
    return (lhs>rhs)-(lhs<rhs)
def seed_certificate():
    cs=[16*(s==0)-sum(1 if (s&x).bit_count()%2==0 else -1 for x in [0,1,2]) for s in range(32)]
    assert sum(c*c for c in cs)==256
    target={2:Q(16,3),3:-Q(3,8),13:-Q(169,24),89:Q(89,24)}
    rows=[]
    for i in range(5):
        pairs=[(cs[s]**2,cs[s|(1<<i)]**2) for s in range(32) if not s&(1<<i)]
        D=sum(b for a,b in pairs);v=vector(pairs,D)
        delta={p:v.get(p,Q(0))-target.get(p,Q(0)) for p in set(v)|set(target)}
        assert vector_sign(delta)>=0
        lo=sum(g(a,b)[0] for a,b in pairs);hi=sum(g(a,b)[1] for a,b in pairs)
        rows.append({'i':i,'D':D,'prime_vector':{str(p):str(c) for p,c in sorted(v.items())},'lo':lo,'hi':hi,'equal_to_target':not any(delta.values())})
    tight=next(r for r in rows if r['equal_to_target'])
    lower=tight['lo']*FAST//(tight['D']*PRECISE)
    assert lower==2964159675584
    write('seed_certificate.json',{'mask':7,'coefficients_W_over_2':cs,'rows':rows,'precise_scale':str(PRECISE),'fast_lower':lower,'constant_vector':{str(p):str(c) for p,c in target.items()}})
    return lower
def write(name,obj):
    (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def flip(m,i):
    b=1<<i
    return ((m&np.uint32(LOW[i]))<<b)|((m&np.uint32(HIGH[i]))>>b)
def translate(m,t):
    for i in range(5):
        if t&(1<<i):m=flip(m,i)
    return m
def run(pilot):
    start=time.perf_counter();seedlo=seed_certificate();batch=131072
    stop=1<<19 if pilot else 1<<31;cap=55 if pilot else 1200
    upper=np.zeros((17,17),dtype=np.int64)
    for a in range(17):
        for b in range(17):
            gh=g(a*a,b*b)[1];upper[a,b]=(gh*FAST+PRECISE-1)//PRECISE
    assert upper.min()>=0 and int(upper.max())*16+256<2**63
    parity=[np.uint32(sum(1<<x for x in range(32) if (s&x).bit_count()%2)) for s in range(32)]
    count={'raw':0,'minority':0,'ordered_boundary':0,'canonical_translation':0,'strict':0,'candidates':0}
    digest=hashlib.sha256();candidates=[]
    for first in range(0,stop,batch):
        if time.perf_counter()-start>cap:raise RuntimeError('Frozen runtime cap exceeded')
        m=(2*np.arange(first,min(stop,first+batch),dtype=np.uint64)+1).astype(np.uint32)
        count['raw']+=len(m);m=m[np.bitwise_count(m)<=16];count['minority']+=len(m)
        previous=np.zeros(len(m),dtype=np.uint8)
        for i in range(5):
            edges=np.bitwise_count((m^flip(m,i))&np.uint32(LOW[i]))
            good=edges>=previous;m=m[good];previous=edges[good]
        count['ordered_boundary']+=len(m)
        for t in range(31,0,-1):
            if not len(m):break
            tm=translate(m,t);m=m[((tm&1)==0)|(tm>=m)]
        count['canonical_translation']+=len(m)
        if not len(m):continue
        digest.update(m.astype('<u4',copy=False).tobytes())
        size=np.bitwise_count(m).astype(np.int16)
        # Direct character sums: c_s=16*1_{s=0}-|A|+2|A intersect odd(s)|.
        c=np.empty((len(m),32),dtype=np.int16)
        for s in range(32):c[:,s]=16*(s==0)-size+2*np.bitwise_count(m&parity[s]).astype(np.int16)
        squares=c.astype(np.int64)**2;assert np.all(squares.sum(axis=1)==256)
        passing=np.zeros(len(m),dtype=bool)
        for i in range(5):
            left=[s for s in range(32) if not s&(1<<i)];right=[s|(1<<i) for s in left]
            D=squares[:,right].sum(axis=1)
            edges=np.bitwise_count((m^flip(m,i))&np.uint32(LOW[i])).astype(np.int64)
            assert np.array_equal(D,16*edges)
            numerator=upper[np.abs(c[:,left]),np.abs(c[:,right])].sum(axis=1)
            passing|=(D>0)&(numerator<=seedlo*D)
        survivors=m[~passing];count['strict']+=int(passing.sum());candidates+=list(map(int,survivors));count['candidates']=len(candidates)
        assert len(candidates)<100000
        if len(survivors):write('pilot_candidates.json' if pilot else 'candidates.json',candidates)
        if count['raw']%(batch*128)==0:
            write('pilot_checkpoint.json' if pilot else 'checkpoint.json',{'complete':False,'counts':count,'elapsed_seconds':time.perf_counter()-start,'hash':digest.hexdigest()})
    assert count['raw']==stop
    if not pilot:
        assert count['minority']==1<<30
        assert count['ordered_boundary']==80198472
        assert count['canonical_translation']==5778648
        assert count['strict']==5778647 and candidates==[7]
        assert digest.hexdigest()=='ac010403c1e2e329262b930668c4d34bf548c862cad687ebd9210579dd0c233b'
    out={'status':'PASS','complete':True,'pilot':pilot,'counts':count,'candidates':candidates,'representative_sha256':digest.hexdigest(),'seed_lower_scaled':seedlo,'scale':FAST,'elapsed_seconds':time.perf_counter()-start,'max_packet_upper':int(upper.max()),'int64_sum_limit_proved':True,'coefficient_method':'direct parity-mask population counts; no FWHT'}
    write('pilot.json' if pilot else 'review_census.json',out);print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');run(p.parse_args().pilot)

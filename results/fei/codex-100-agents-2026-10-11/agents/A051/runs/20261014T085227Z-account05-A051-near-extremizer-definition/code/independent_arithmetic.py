"""Direct character sums; no first-implementation imports."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def combine(*terms):
    r={}
    for k,d in terms:
        for p,v in d.items(): r[p]=r.get(p,Q(0))+k*v
    return {p:v for p,v in r.items() if v}
@lru_cache(None)
def factors(v):
    r={};p=2
    while p*p<=v:
        while v%p==0: r[p]=r.get(p,0)+1;v//=p
        p+=1
    if v>1:r[v]=r.get(v,0)+1
    return r
def logalg(x): return combine((1,factors(x.numerator)),(-1,factors(x.denominator)))
def ent(p): return combine(*[(-v,logalg(v)) for v in p if v])
def ln_bound(x):
    z=(x-1)/(x+1);s=Q(0)
    for k in range(64):s+=2*z**(2*k+1)/(2*k+1)
    return s,s+2*z**129/(129*(1-z*z))
two=ln_bound(Q(2))
@lru_cache(None)
def log_bound(p):
    k=p.bit_length()-1;lo,hi=ln_bound(Q(p,1<<k))
    return k+lo/two[1],k+hi/two[0]
def bounds(d):
    lo=hi=Q(0)
    for p,v in d.items():
        a,b=log_bound(p)
        lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
    return lo,hi
def direct_coeffs(t):
    return [Q(sum((2*v-1)*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def pack(x,inds):return sum(((x>>j)&1)<<i for j,i in enumerate(inds))
def calculate(t,mask):
    n=(len(t)-1).bit_length();A=[i for i in range(n) if mask>>i&1];C=[i for i in range(n) if not mask>>i&1]
    root=direct_coeffs(t);rp=[v*v for v in root];H=ent(rp)
    IA=sum(sum((s>>i)&1 for i in A)*v for s,v in enumerate(rp))
    I=sum(s.bit_count()*v for s,v in enumerate(rp));cp=[];ch=[]
    for a in range(1<<len(A)):
        child=tuple(t[pack(a,A)|pack(c,C)] for c in range(1<<len(C)))
        p=[v*v for v in direct_coeffs(child)];cp.append(p);ch.append(ent(p))
    N=len(cp);q=[sum(row[s] for row in cp)/N for s in range(len(cp[0]))]
    B=combine((1,H),(-1,ent(q)))
    J=combine((1,ent(q)),*[(Q(-1,N),h) for h in ch])
    G={}
    for s,v in enumerate(q):
        if v:G=combine((1,G),(v,logalg(sum(p[s]**2 for p in cp)/N/v**2)))
    return H,I,IA,B,J,G
def nand_table():
    # Explicit serial gates, independent of the tree helper.
    t=[]
    for z in range(64):
        bit=lambda i:(z>>i)&1
        u=1-bit(0)*bit(1)
        u=1-u*bit(2)*bit(3)
        u=1-u*bit(4)
        u=1-u*bit(5)
        t.append(u)
    return tuple(t)
def controls():
    yield 'NAND6_case0006',nand_table()
    for m in (2,3):yield 'quadratic_'+str(m),tuple(sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(m))%2 for z in range(1<<(2*m)))
    yield 'quadratic_times_PD3',tuple((((z&1)*((z>>1)&1))^int((z>>2)==0)) for z in range(32))
def main():
    start=time.perf_counter();total=0;receipts=[]
    for name,t in controls():
        saved=json.loads((ROOT/'out'/('CONTROL_'+name+'.json')).read_text())
        ck(saved['truth_sha256']==hashlib.sha256(bytes(t)).hexdigest())
        successes=[]
        for row in saved['all_blocks']:
            mask=row['mask'];H,I,IA,B,J,G=calculate(t,mask);total+=1
            for key,d in [('H',H),('B',B),('J',J),('Gamma',G)]:ck({str(p):str(v) for p,v in d.items()}==row[key])
            ck(str(I)==row['I']);ck(str(IA)==row['I_A'])
            gap=combine((1,G),(-1,J));ck(not gap or bounds(gap)[0]>=0)
            n=(len(t)-1).bit_length()
            if mask.bit_count()==n-1:ck(G==J);ck(combine((1,B),(1,G))==H)
            if name.startswith('quadratic_') and name!='quadratic_times_PD3':
                touched=sum(bool(mask&(3<<(2*j))) for j in range(n//2))
                singly=sum((mask&(3<<(2*j))).bit_count()==1 for j in range(n//2))
                ck(B=={2:Q(mask.bit_count())});ck(G==({2:Q(singly)} if singly else {}));ck(J==G)
                ck(combine((1,B),(1,J))=={2:Q(2*touched)})
            if I and IA:
                R=combine((1/I,H));V=combine((1/IA,B),(1/IA,G))
                diff=combine((1,V),(-1,R))
                if bounds(diff)[1]<0:successes.append(mask)
                if name=='NAND6_case0006':
                    ck(bounds(R)[0]>Q(12,5));ck(bounds(R)[1]<Q(241,100))
                    if mask.bit_count()==1:ck(bounds(V)[0]>Q(319,100))
                    if mask==48:
                        ck(bounds(V)[1]<Q(47,20));ck(bounds(combine((1,B),(1,J)))[1]<Q(23,10))
                        ck(bounds(gap)[1]<Q(11,250))
                        childH={2:Q(6),3:Q(-27,32),5:Q(-25,32)}
                        d=bounds(combine((1,childH),(-1,R)))
                        ck(Q(44,100)<d[0] and d[1]<Q(45,100))
                        ck(combine((Q(1,4),childH),(-Q(1,4),R))==combine((1,R),(-1,B),(-1,J)))
                        ck(G=={2:Q(2),7:Q(-217,128),31:Q(-217,128),37:Q(217,256),349:Q(217,256)})
            if time.perf_counter()-start>60:raise TimeoutError('Frozen replay cap')
        if name=='NAND6_case0006':ck(successes==[48])
        receipts.append({'name':name,'blocks':len(saved['all_blocks']),'strict_collision_admission_masks':successes})
    result={'blocks':total,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'receipts':receipts}
    (ROOT/'out'/'INDEPENDENT_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()

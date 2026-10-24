"""Frozen pilot: exact row collision bound and physical-child identities."""
from fractions import Fraction as F
from pathlib import Path
import json, time, hashlib
import exact_tools as d

ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def logs(x):
    x=F(x)
    return d.add([(1,d.factor(x.numerator)),(-1,d.factor(x.denominator))])
def entropy(p):
    return d.add((-v,logs(v)) for v in p if v)
def enc(v): return d.enc(v)
def box(v): return d.ei(d.interval(v))
def embed(z,indices):
    return sum(((z>>j)&1)<<i for j,i in enumerate(indices))
def calc(t,mask,details=False):
    n=(len(t)-1).bit_length(); aa=[i for i in range(n) if mask>>i&1]
    cc=[i for i in range(n) if not mask>>i&1]; N=1<<len(aa); M=1<<len(cc)
    root_w=d.fwht([2*x-1 for x in t]); root_p=[F(x*x,len(t)**2) for x in root_w]
    H=entropy(root_p); ii=[sum(v for s,v in enumerate(root_p) if s>>i&1) for i in range(n)]
    I=sum(ii); IA=sum(ii[i] for i in aa)
    child_w=[]; child_p=[]; child_h=[]; child_i=[]
    for a in range(N):
        table=tuple(t[embed(a,aa)|embed(c,cc)] for c in range(M))
        w=[F(v,M) for v in d.fwht([2*x-1 for x in table])]
        p=[v*v for v in w]; ck(sum(p)==1)
        child_w.append(w); child_p.append(p); child_h.append(entropy(p))
        child_i.append(sum(s.bit_count()*v for s,v in enumerate(p)))
    q=[sum(p[s] for p in child_p)/N for s in range(M)]
    ck(sum(q)==1); ck(I==IA+sum(child_i)/N)
    avgh=d.add((F(1,N),h) for h in child_h)
    B=d.add([(1,H),(-1,entropy(q))]); J=d.add([(1,entropy(q)),(-1,avgh)])
    L=d.add([(1,B),(1,J)])
    gamma={}; rows=[]
    for s,qs in enumerate(q):
        if not qs: continue
        moment=sum(p[s]*p[s] for p in child_p)/N/qs**2
        ck(1<=moment<=N)
        gamma=d.add([(1,gamma),(qs,logs(moment))])
        # Independent row Fourier convolution verifies the signed cancellation formula.
        row=[w[s] for w in child_w]; coeff=[v/N for v in d.fwht(row)]
        conv=[sum(coeff[u]*coeff[u^v] for u in range(N)) for v in range(N)]
        ck(conv[0]==qs); ck(sum(v*v for v in conv)/qs**2==moment)
        if details: rows.append({'retained_mask':s,'q':str(qs),'child_coefficients':[str(w) for w in row], 'collision_ratio':str(moment), 'square_fourier_coefficients':[str(v) for v in conv]})
    gap=d.add([(1,gamma),(-1,J)])
    ck(not gap or d.interval(gap)[0]>=0)
    out={'n':n,'mask':mask,'H':enc(H),'I':str(I),'I_A':str(IA),'B':enc(B),'J':enc(J),'Gamma':enc(gamma),'L':enc(L),'Gamma_minus_J':box(gap)}
    if IA and I:
        R={p:c/I for p,c in H.items()}; cost={p:c/IA for p,c in d.add([(1,B),(1,gamma)]).items()}
        out.update(R=box(R), L_over_I_A=box({p:c/IA for p,c in L.items()}), collision_cost=box(cost), collision_minus_root=box(d.add([(1,cost),(-1,R)])))
        deficits=[d.add([(1,h),(-ci,R)]) for h,ci in zip(child_h,child_i)]
        ck(d.add((F(1,N),z) for z in deficits)==d.add([(IA,R),(-1,L)]))
        if details:
            out['children']=[{'assignment':a,'H':enc(h),'I':str(ci),'D_at_root_ratio':box(z)} for a,(h,ci,z) in enumerate(zip(child_h,child_i,deficits))]
    if details: out['rows']=rows
    return out

def controls():
    tree=(((((),()),(),()),()),())
    yield 'NAND6_case0006', d.tables(tree), 48
    for m in (2,3):
        t=tuple(sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(m))%2 for z in range(1<<(2*m)))
        yield 'quadratic_'+str(m),t,3
    t=tuple((((z&1)*((z>>1)&1)) ^ int((z>>2)==0)) for z in range(32))
    yield 'quadratic_times_PD3',t,3

def main():
    start=time.perf_counter(); cases=blocks=0; special=[]
    for name,t,chosen in controls():
        rows=[calc(t,mask,mask==chosen) for mask in range(1,len(t)-1)]
        cases+=1; blocks+=len(rows)
        obj={'name':name,'truth_sha256':hashlib.sha256(bytes(t)).hexdigest(),'selected_mask':chosen,'selected':next(r for r in rows if r['mask']==chosen),'all_blocks':rows}
        (ROOT/'out'/('CONTROL_'+name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
        special.append({'name':name,'selected':obj['selected']})
        print(name,{k:obj['selected'].get(k) for k in ['R','L_over_I_A','collision_cost','collision_minus_root']},flush=True)
    for n in (1,2,3):
        for table in range(1<<(1<<n)):
            t=tuple((table>>x)&1 for x in range(1<<n))
            for mask in range(1,(1<<n)-1):
                calc(t,mask); blocks+=1
            cases+=1
            if time.perf_counter()-start>60: raise TimeoutError('Frozen 60-second cap')
    obj={'cases':cases,'blocks':blocks,'assertions':checks,'helper_assertions':d.ASSERTIONS,'elapsed_seconds':time.perf_counter()-start,'special':special}
    (ROOT/'out'/'SUMMARY.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in obj.items() if k!='special'}))
if __name__=='__main__': main()

from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
from arithmetic import log2,scale,plus,Q
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(b):
    global checks
    assert b;checks+=1
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def con(x):return scale((Q,Q),F(x))
def ent(ps):
    ans=(0,0)
    for p in ps:
        ck(p>=0)
        if p:ans=plus(ans,scale(log2(1/p),p))
    return ans
G=tuple(-1 if x in {0,1,2} else 1 for x in range(64))
hh=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
JJ=tuple(-hh[x^1] for x in range(64))
def restricted(assign):return tuple(G[x] for x in range(64) if all((x>>i&1)==b for i,b in assign.items()))
@lru_cache(None)
def inner(t):
    co=[sum(F(v*(-1 if (s&x).bit_count()%2 else 1),len(t)) for x,v in enumerate(t)) for s in range(len(t))]
    ps=[z*z for z in co];ck(sum(ps)==1)
    I=sum(F(s.bit_count())*p for s,p in enumerate(ps))
    n=(len(t)-1).bit_length();edges=sum(F(sum(t[x]!=t[x^2**i] for x in range(len(t))),len(t)) for i in range(n))
    ck(edges==I)
    return co[0],ent(ps),I
@lru_cache(None)
def moments(mus):
    vs=[1-m*m for m in mus];pminus=[(1-m)/2 for m in mus];active=[j for j,v in enumerate(vs) if v]
    probs=[]
    for x in range(64):
        p=F(1)
        for j in range(6):p*=pminus[j] if x>>j&1 else 1-pminus[j]
        probs.append(p)
    ck(sum(probs)==1);masses={}
    for T in range(64):
        if any(T>>j&1 and not vs[j] for j in range(6)):continue
        norm=F(1)
        for j in active:
            if T>>j&1:norm*=vs[j]
        ck(norm>0);moment=F(0)
        for x,p in enumerate(probs):
            if not p:continue
            term=p*JJ[x]
            for j in active:
                if T>>j&1:term*=1-2*(x>>j&1)-mus[j]
            moment+=term
        masses[T]=moment*moment/norm
    ck(sum(masses.values())==1)
    occ=[sum(p for T,p in masses.items() if T>>j&1) for j in range(6)]
    qs=[]
    for j in range(6):
        q=F(0)
        for x in range(64):
            if x>>j&1 or JJ[x]==JJ[x|1<<j]:continue
            w=F(1)
            for k in range(6):
                if k!=j:w*=pminus[k] if x>>k&1 else 1-pminus[k]
            q+=w
        ck(occ[j]==vs[j]*q);qs.append(q)
    return ent(list(masses.values())),occ,qs
def full(truths):
    inns=[inner(t) for t in truths];mus=tuple(x[0] for x in inns);vs=[1-m*m for m in mus]
    Hmask,occ,qs=moments(mus);hf=Hmask;ii=F(0)
    for j,(m,h,i) in enumerate(inns):
        if vs[j]:
            hf=plus(hf,scale(sub(h,ent([vs[j],1-vs[j]])),occ[j]/vs[j]))
            ii+=occ[j]*i/vs[j]
        else:ck(i==0 and h==(0,0))
    ck(ii==sum(q*t[2] for q,t in zip(qs,inns)))
    return hf,ii,sub(con(4*ii),hf)
def main():
    start=time.perf_counter();rows=json.loads((ROOT/'out/SATURATION_STATES.json').read_text(encoding='utf-8'));out=[]
    for r in rows:
        assign={2:0,0:0,3:0};assign.update({int(k):v for k,v in r['assignment'].items()})
        ts=[restricted(assign),restricted({0:r['anchor_bit_b']})]+[G]*4
        H,I,S=full(ts)
        ck(I==F(r['I_full']));ck(H[0]<=r['H_full'][1] and r['H_full'][0]<=H[1])
        ck(S[0]<=r['S4_full'][1] and r['S4_full'][0]<=S[1])
        if len(r['assignment'])==2 and set(r['assignment'].values())=={0}:ck(S[1]<0)
        else:ck(S[0]>0)
        out.append({'b':r['anchor_bit_b'],'assignment':r['assignment'],'H_full':H,'I_full':str(I),'S4_full':S})
        ck(time.perf_counter()-start<55)
    result={'version':'direct-centered-moment-reproduction-v1','states':len(out),'independent_exact_predicates_including_runtime':checks,
      'distinct_product_laws':moments.cache_info().currsize,'runtime_seconds':time.perf_counter()-start,'failed':0,'cases':out}
    (ROOT/'out/INDEPENDENT_REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()

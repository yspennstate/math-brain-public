from pathlib import Path
from fractions import Fraction as F
import json,math,time
from itertools import product
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter()

def compositions(n,k):
    if k==1:
        yield (n,);return
    for i in range(n+1):
        for t in compositions(n-i,k-1): yield (i,)+t

def spec(a,b,r):
    N=1<<(a+b+r);mask=(1<<a)-1
    vals=[1-2*int(x&mask==0)+2*int(x==0) for x in range(N)]
    z=list(vals);h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):x,y=z[j],z[j+h];z[j],z[j+h]=x+y,x-y
        h*=2
    return vals,[F(x*x,N*N) for x in z]

def source(a,b):
    s=F(1,1<<a);N=1<<(a+b)
    return [(1-2*s)**2]+[4*s*s if x<(1<<a) else F(0) for x in range(1,N)]

def floor(a,b,r,R):
    s,t,e=F(1,1<<a),F(1,1<<(a+b)),F(2,1<<(a+b+r));mu=1-2*s;N=len(R)
    P=spec(a,b,r)[1];M=[sum(P[T+U*N] for U in range(1<<r)) for T in range(N)]
    Rp=[(1-e/s)*v+(e/s)*mu*int(T==0)+2*e*t for T,v in enumerate(R)]
    Q=[Rp[x%N]*v/M[x%N] for x,v in enumerate(P)]
    assert sum(Q)==1 and all(x>=0 for x in Q)
    return P,Q

def marginal(P):return [P[2*x]+P[2*x+1] for x in range(len(P)//2)]

def one(a,b,r,R):
    P,Q=floor(a,b,r,R);old=marginal(Q);V=marginal(R);Pg=source(a-1,b)
    Rp=[Pg[0]]+[(1-Pg[0])*v/(1-V[0]) for v in V[1:]]
    Pc,Qn=floor(a-1,b,r,Rp)
    assert sum(old)==sum(Qn)==sum(Pc)==1
    ratios=[(p,qo/qn) for p,qo,qn in zip(Pc,old,Qn) if p]
    return sum(float(p)*math.log2(float(q)) for p,q in ratios)/2,ratios,old,Qn

def main():
    rows=[];count=0;best=None;planned=0
    for a,b,r in product([2,3,4],[0,1],[1,2,3]):
        Pg=source(a,b);N=len(Pg);non=1-Pg[0]
        raw=list(compositions(4,N-1)) if N-1<=7 else [tuple(4*int(i==j) for i in range(N-1)) for j in range(N-1)]
        raw.append(tuple(1 for _ in range(N-1)))
        planned+=2*len(raw)
    assert planned<=20000
    for a,b,r in product([2,3,4],[0,1],[1,2,3]):
        Pg=source(a,b);N=len(Pg);non=1-Pg[0]
        raw=list(compositions(4,N-1)) if N-1<=7 else [tuple(4*int(i==j) for i in range(N-1)) for j in range(N-1)]
        raw.append(tuple(1 for _ in range(N-1)))
        for weights,eps in product(raw,[F(1,1024),F(1,16)]):
            sm=sum(weights);R=[Pg[0]]+[(1-eps)*non*F(w,sm)+eps*p for w,p in zip(weights,Pg[1:])]
            value,ratios,old,new=one(a,b,r,R);count+=1
            if best is None or value>best['value']:
                best={'a':a,'b':b,'r':r,'value':value,'R':[str(x) for x in R],'ratios':[[str(p),str(q)] for p,q in ratios]}
                (RUN/'out/SEARCH_CHECKPOINT.json').write_text(json.dumps(best,indent=2)+'\n',encoding='utf-8')
            if value>1e-9:rows.append({'a':a,'b':b,'r':r,'value':value,'R':[str(x) for x in R]})
            if time.perf_counter()-START>55:
                result={'status':'PARTIAL_RUNTIME_GUARD','planned_cases':planned,'cases':count,'best':best,'positive_rows':rows,'seconds':time.perf_counter()-START};break
        else:continue
        break
    else:result={'status':'COMPLETE_FLOAT_DISCOVERY','planned_cases':planned,'cases':count,'best':best,'positive_rows':rows,'seconds':time.perf_counter()-START}
    (RUN/'out/RESET_SEARCH.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['best','positive_rows']}));print(json.dumps({k:v for k,v in best.items() if k not in ['R','ratios']}))
if __name__=='__main__':main()

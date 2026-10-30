import json,itertools,time
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import exact_library as e
import phase_library as p
import refund_library as r
ROOT=Path(__file__).resolve().parents[1];checks=0
def ck(x):
    global checks
    checks+=1
    if not x:raise AssertionError(checks)
@lru_cache(None)
def stats(v):
    N=len(v);n=N.bit_length()-1;w=e.fwht(v)
    if n<=3:ck(w==e.direct(v))
    law=[F(x*x,N*N) for x in w];H=p.entropy(law);I=sum(s.bit_count()*x for s,x in enumerate(law))
    ck(sum(law)==1);ck(I==F(sum(v[x]!=v[x^(1<<i)] for i in range(n) for x in range(N)),N))
    return H,I,w
def children(v,A):
    n=len(v).bit_length()-1;ai=[i for i in range(n) if A>>i&1];ci=[i for i in range(n) if not A>>i&1]
    return [tuple(v[e.unpack(x,ai)|e.unpack(y,ci)] for y in range(1<<len(ci))) for x in range(1<<len(ai))]
def diagnostic(v,w):
    N=len(v);n=N.bit_length()-1;w=[F(x,N) for x in w];O=F(0);M=F(0)
    for i in range(n):
        O+=sum(max(F(0),w[s|(1<<i)]**2-w[s]**2) for s in range(N) if not s>>i&1)
    for i,j in itertools.combinations(range(n),2):
        A=(1<<i)|(1<<j)
        for s in range(N):
            if s&A:continue
            row=r.quartet(w[s],w[s|(1<<i)],w[s|(1<<j)],w[s|A]);M+=row['Mi']+row['Mj']
    ck((O+M==0)==(len(set(v))==1))
    return O,M
def singleton(v,i):
    H,I,w=stats(v);N=len(v);d=sum(F(w[s]**2,N*N) for s in range(N) if s>>i&1)
    beta=F(0);J={};B={};rows=[]
    for s in range(N):
        if s>>i&1:continue
        a,b=F(w[s],N),F(w[s|(1<<i)],N);q=a*a+b*b
        if not q:continue
        minor=min(a*a,b*b)/q
        j=p.add({2:F(1)},p.entropy([(a+b)**2/(2*q),(a-b)**2/(2*q)]),-1)
        ck(p.sg(p.add({2:3*minor},j,-1))>=0)
        beta+=q*minor;B=p.add(B,p.entropy([minor,1-minor]),q);J=p.add(J,j,q)
        rows.append((q,minor,j))
    L=p.add(B,J);ch=children(v,1<<i);physical=dict(H)
    for child in ch:physical=p.add(physical,stats(child)[0],-F(1,2))
    ck(L==physical);O=d-beta;ck(O>=0)
    banks={}
    for K in (4,8,16):
        rho=1/(1+F(2)**(K-3));rk=p.lograt(1+F(2)**(3-K));KL={};A={}
        for q,x,j in rows:
            kl={}
            if x:kl=p.add(kl,p.lograt(x/rho),x)
            if x<1:kl=p.add(kl,p.lograt((1-x)/(1-rho)),1-x)
            ck(p.sg(kl)>=0);KL=p.add(KL,kl,q);A=p.add(A,p.add({2:3*x},j,-1),q)
        D=p.add(H,{2:K*I},-1);S={}
        for child in ch:
            hc,ic,_=stats(child);S=p.add(S,p.add(hc,{2:K*ic},-1),-F(1,2))
        left=p.add(p.add(p.add(p.add(D,S),{2:K*O}),KL),A)
        ck(left==rk);ck(p.sg(A)>=0)
        banks[K]=(KL,A,D,S,rk)
        remaining=p.add(p.add(p.add(rk,D,-1),S,-1),{2:K*O},-1)
        for u in ([F(1,2)] if K==4 else [F(1,4),F(1,2)]):
            ck(u>rho);tail=sum(q for q,x,_ in rows if x>=u)
            kl_u=p.add(p.add(rk,{2:(K-3)*u}),p.entropy([u,1-u]),-1)
            ck(p.sg(kl_u)>0);ck(p.sg(p.add(remaining,kl_u,-tail))>=0)
    return dict(d=d,O=O,B=B,J=J,banks=banks)
def compatible_pairs(v,single):
    H,I,w=stats(v);N=len(v);n=N.bit_length()-1
    for i,j in itertools.combinations(range(n),2):
        mask=(1<<i)|(1<<j);B={};IA=F(0);rows=[]
        for t in range(N):
            if t&mask:continue
            mass=[F(w[t|u]**2,N*N) for u in (0,1<<i,1<<j,mask)];q=sum(mass)
            if not q:continue
            nu=[x/q for x in mass];B=p.add(B,p.entropy(nu),q)
            IA+=mass[1]+mass[2]+2*mass[3];rows.append((q,nu))
        Z=p.add(p.add(B,single[i]['B'],-1),single[j]['B'],-1);ck(p.sg(Z)>=0)
        L=dict(H);ch=children(v,mask)
        for h in ch:L=p.add(L,stats(h)[0],-F(1,4))
        J=p.add(L,B,-1)
        for K in (4,8,16):
            rho=1/(1+F(2)**(K-3));pi=[(1-rho)**2,rho*(1-rho),rho*(1-rho),rho*rho];G={}
            for q,nu in rows:
                for x,y in zip(nu,pi):
                    if x:G=p.add(G,p.lograt(x/y),q*x)
            ck(p.sg(G)>=0)
            KLi,Ai,D,Si,rk=single[i]['banks'][K];KLj,Aj,_,Sj,_=single[j]['banks'][K]
            O=single[i]['O']+single[j]['O']
            ck(p.add(p.add(KLi,KLj),{2:(K-3)*O})==p.add(G,Z))
            bank=p.add(p.add(p.add(p.add(p.add(p.scale(D,2),Si),Sj),{2:3*O}),G),Z)
            bank=p.add(p.add(bank,Ai),Aj);ck(bank==p.scale(rk,2))
            S={}
            for h in ch:
                hc,ic,_=stats(h);S=p.add(S,p.add(hc,{2:K*ic},-1),-F(1,4))
            gap=p.add({2:3*IA},J,-1);ck(p.sg(gap)>=0)
            ck(p.add(p.add(p.add(D,S),G),gap)==p.scale(rk,2))
def main():
    start=time.perf_counter();tables=cuts=ratio_crit=positive_ratio_crit=threshold_viol=0
    records=[]
    for n in (1,2,3):
        for code in range(1<<(1<<n)):
            if time.perf_counter()-start>50:raise RuntimeError('Frozen 55-second pilot stopping guard')
            v=tuple(1 if code>>x&1 else -1 for x in range(1<<n));H,I,w=stats(v);tables+=1
            O,M=diagnostic(v,w)
            single=[singleton(v,i) for i in range(n)];ds=[x['d'] for x in single];cuts+=n
            compatible_pairs(v,single)
            if not I:continue
            critical=all(p.sg(p.add(p.scale(H,stats(h)[1]),p.scale(stats(h)[0],I),-1))>=0
                for A in range(1,(1<<n)-1) for h in children(v,A))
            if critical:
                ratio_crit+=1
                if p.sg(H)>0:
                    positive_ratio_crit+=1
                    for d in ds:
                        if d:ck(e.sign(p.add(p.scale(H,1/I),p.lograt(d)),-3)<0)
            D=p.add(H,{2:2*I},-1)
            if n<=2:ck(p.sg(D)<=0)
            if n==3 and p.sg(D)>0:
                threshold_viol+=1
                for i,d in enumerate(ds):
                    for h in children(v,1<<i):
                        hc,ic,_=stats(h);ck(p.sg(p.add(hc,{2:2*ic},-1))<=0)
                    ck(e.sign(p.add({2:F(2)},p.lograt(d)),-3)<0)
            if critical and p.sg(H)>0:records.append({'n':n,'code':code,'H':p.enc(H),'I':str(I),'influences':list(map(str,ds)),'O':str(O),'M':str(M)})
    point=[]
    for n in range(4,9):
        v=(-1,)+(1,)*((1<<n)-1);_,_,w=stats(v);O,M=diagnostic(v,w);z=F(1,1<<n)
        formula=16*F(n*(n-1),2)*z*z/((1-4*z+16*z*z)*(1-4*z+8*z*z))
        ck(O==0);ck(M==formula);point.append({'n':n,'O':str(O),'T':str(M),'closed_formula':str(formula)})
    result={'status':'PASS','Boolean_tables_n_le3':tables,'singleton_cuts':cuts,'ratio_critical_nonconstant':ratio_crit,
            'positive_ratio_critical':positive_ratio_crit,'minimal_K2_violations_n3':threshold_viol,
            'point_defect_formula_controls':point,'critical_records':records,
            'assertions_checker':checks,'assertions_refund_library':r.count,
            'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('critical_records','point_defect_formula_controls')}))
if __name__=='__main__':main()

from fractions import Fraction as Q
from pathlib import Path
import json,time,hashlib
import independent_arithmetic as a
ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def nonneg(v):ck(not v or a.bounds(v)[0]>=0)
def beta_entropy(b):return a.ent([b,1-b])
def singleton(t,i):
    n=(len(t)-1).bit_length();C=[j for j in range(n) if j!=i]
    coeff=a.direct_coeffs(t);rp=[v*v for v in coeff];H=a.ent(rp);I=sum(s.bit_count()*p for s,p in enumerate(rp));di=sum(p for s,p in enumerate(rp) if s>>i&1)
    B={};J={};beta=coll=Q(0)
    for s in range(1<<len(C)):
        j=a.pack(s,C);v,w=coeff[j],coeff[j|(1<<i)];q=v*v+w*w
        if not q:continue
        e=min(v*v,w*w)/q;c=4*e*(1-e);beta+=q*e;coll+=q*c
        B=a.combine((1,B),(q,beta_entropy(e)))
        p=[(v+w)**2/(2*q),(v-w)**2/(2*q)]
        rowJ=a.combine((1,{2:Q(1)}),(-1,a.ent(p)))
        J=a.combine((1,J),(q,rowJ));nonneg(a.combine((c,{2:Q(1)}),(-1,rowJ)))
        h=[1 if v+w>=0 else -1,1 if v-w>=0 else -1]
        rho=[x*x for x in a.direct_coeffs(tuple((z+1)//2 for z in h))]
        nu=[v*v/q,w*w/q]
        ck(sum(abs(x-y) for x,y in zip(rho,nu))/2==e)
    ck(2*beta<=coll<=4*beta);ck(di>=beta)
    L=a.combine((1,B),(1,J));nonneg(a.combine((1,beta_entropy(coll/2)),(coll,{2:Q(1)}),(-1,L)))
    children=[]
    for bit in (0,1):
        ch=tuple(t[a.pack(z,C)|(bit<<i)] for z in range(1<<len(C)))
        p=[x*x for x in a.direct_coeffs(ch)];children.append((a.ent(p),sum(s.bit_count()*x for s,x in enumerate(p))))
    ck(I==di+sum(v for h,v in children)/2)
    ck(L==a.combine((1,H),*[(-Q(1,2),h) for h,v in children]))
    critical=False
    for K in (2,4,8,16):
        D=a.combine((1,H),(-K*I,{2:Q(1)}))
        S=a.combine(*[(-Q(1,2),h) for h,v in children],(K*sum(v for h,v in children)/2,{2:Q(1)}))
        lhs=a.combine((1,D),(1,S),(K*(di-beta),{2:Q(1)}))
        ck(lhs==a.combine((1,L),(-K*beta,{2:Q(1)})))
        relaxed=a.logalg(1+Q(2)**(3-K));nonneg(a.combine((1,relaxed),(-1,lhs)))
        if K==2 and a.bounds(D)[0]>0:
            ck(n==3)
            for h,v in children:nonneg(a.combine((-1,h),(2*v,{2:Q(1)})))
            nonneg(S);critical=True
    return critical
def pair(t,mask):
    n=(len(t)-1).bit_length();A=[i for i in range(n) if mask>>i&1];C=[i for i in range(n) if not mask>>i&1]
    rp=[v*v for v in a.direct_coeffs(t)];H=a.ent(rp);I=sum(s.bit_count()*v for s,v in enumerate(rp));IA=sum(sum((s>>i)&1 for i in A)*v for s,v in enumerate(rp))
    wp=[];child=[]
    for b in range(4):
        tab=tuple(t[a.pack(b,A)|a.pack(c,C)] for c in range(1<<len(C)))
        w=a.direct_coeffs(tab);wp.append(w);p=[v*v for v in w];child.append((a.ent(p),sum(s.bit_count()*v for s,v in enumerate(p))))
    q=[sum(w[s]**2 for w in wp)/4 for s in range(len(wp[0]))]
    B={};G={};Ct=Q(0);W0=Wg=Wb=Q(0)
    for s,qs in enumerate(q):
        if not qs:continue
        values=[w[s] for w in wp];c=sum(v**4 for v in values)/(4*qs**2)-1
        ph=tuple(int(v>=0) for v in values);wh=a.direct_coeffs(ph);iph=sum(j.bit_count()*v*v for j,v in enumerate(wh))
        rowcoeff=[sum(v*(-1 if (x&j).bit_count()%2 else 1) for x,v in enumerate(values))/4 for j in range(4)]
        nu=[v*v/qs for v in rowcoeff];iv=sum(j.bit_count()*v for j,v in enumerate(nu))
        if len(set(ph))==1:W0+=qs;ck(1-nu[0]<=c)
        elif c<=Q(1,16):Wg+=qs;ck(iph>=1);ck(iv>=Q(1,2))
        else:Wb+=qs
        Ct+=qs*c;B=a.combine((1,B),(qs,a.ent(nu)));G=a.combine((1,G),(qs,a.logalg(1+c)))
    J=a.combine((1,a.ent(q)),*[(-Q(1,4),h) for h,v in child]);ck(B==a.combine((1,H),(-1,a.ent(q))))
    ck(W0+Wg+Wb==1);ck(Wb<=16*Ct);ck(Ct<=6*IA);banks=[]
    for K in (4,8,16):
        D=a.combine((1,H),(-K*I,{2:Q(1)}));S=a.combine(*[(-Q(1,4),h) for h,v in child],(K*sum(v for h,v in child)/4,{2:Q(1)}))
        lhs=a.combine((1,D),(1,S),((Q(K,2)-2)*Wg,{2:Q(1)}));rhs=a.combine((1,G),(W0,a.logalg(1+Q(3,1<<K))),(2*Wb,{2:Q(1)}));gap=a.combine((1,rhs),(-1,lhs));nonneg(gap)
        banks.append({'K':K,'D':{str(p):str(v) for p,v in D.items()},'S':{str(p):str(v) for p,v in S.items()},'gap':{str(p):str(v) for p,v in gap.items()}})
    return Ct,W0,Wg,Wb,G,banks
def controls():
    yield 'NAND6',a.nand_table()
    for r in range(1,5):yield 'rare_bent_'+str(r),tuple(1 if (z>>2)==0 else 1-((z&1)*((z>>1)&1)) for z in range(1<<(r+2)))
def main():
    start=time.perf_counter();singletons=critical=paircuts=0
    for n in (1,2,3):
        for truth in range(1<<(1<<n)):
            t=tuple((truth>>x)&1 for x in range(1<<n))
            for i in range(n):critical+=singleton(t,i);singletons+=1
            if time.perf_counter()-start>55:raise TimeoutError('Frozen replay cap')
    for name,t in controls():
        data=json.loads((ROOT/'out'/('CONTROL_'+name+'.json')).read_text());ck(data['truth_sha256']==hashlib.sha256(bytes(t)).hexdigest())
        for row in data['cuts']:
            C,W0,Wg,Wb,G,banks=pair(t,row['mask']);paircuts+=1
            ck(str(C)==row['C_A']);ck(str(W0)==row['W0']);ck(str(Wg)==row['Wg']);ck(str(Wb)==row['Wb']);ck({str(p):str(v) for p,v in G.items()}==row['Gamma'])
            for test,source in zip(banks,row['checks']):
                ck(test['D']==source['D']);ck(test['S']==source['S'])
            if time.perf_counter()-start>55:raise TimeoutError('Frozen replay cap')
    out={'singleton_cuts':singletons,'K2_minimal_critical_singleton_cuts':critical,'independent_pair_cuts':paircuts,'assertions':checks,'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'out/REVIEW_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()

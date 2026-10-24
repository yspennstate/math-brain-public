"""Independent exact checker. The complete domain is frozen before execution."""
from fractions import Fraction as F
from itertools import product
from math import isqrt, comb
from pathlib import Path
import json, time

run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def ck(t):
    global assertions
    assertions+=1
    assert t, assertions
def save(n,x):
    (run/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='')
def subsets(n):return [tuple(i for i in range(n) if (mask>>i)&1) for mask in range(1<<n)]
def mass(x,p):
    w=F(1)
    for b,q in zip(x,p): w*=q if b else 1-q
    return w
def variance(p,s):
    z=F(1)
    for i in s:z*=4*p[i]*(1-p[i])
    return z
def normalized_coefficient(table,p,s):
    # Centered expectation, divided by sqrt(v_s), remains rational.
    a=F(0)
    for x in product([0,1],repeat=len(p)):
        z=mass(x,p)*table[x]
        for i in s:z*=x[i]-p[i]
        a+=z
    for i in s:a/=2*p[i]*(1-p[i])
    return a
def difference_coefficient(table,p,s):
    rest=[i for i in range(len(p)) if i not in s];a=F(0)
    for xrest in product([0,1],repeat=len(rest)):
        w=F(1);x=[0]*len(p)
        for i,b in zip(rest,xrest):x[i]=b;w*=p[i] if b else 1-p[i]
        delta=0
        for b in product([0,1],repeat=len(s)):
            for i,y in zip(s,b):x[i]=y
            delta+=(-1)**(len(s)-sum(b))*table[tuple(x)]
        a+=w*F(delta,2**len(s))
    return a
def directional(table,p,reverse=False):
    # Slice-coefficient h_T(k), THEN signed count jumps; no source helper used.
    if reverse:
        perm=(2,3,0,1);q=tuple(p[i] for i in perm)
        tt={x:table[tuple(x[perm.index(i)] for i in range(4))] for x in product([0,1],repeat=4)}
        original=directional(tt,q,False)
        return {(tuple(i-2 for i in t),tuple(i+2 for i in u)):(k,r) for (u,t),(k,r) in original.items()}
    result={}
    for t in subsets(2)[1:]:
        h=[]
        for k in range(3):
            aa=(1,)*k+(0,)*(2-k)
            tb={b:table[aa+b] for b in product([0,1],repeat=2)}
            h.append(difference_coefficient(tb,p[2:],t))
        alpha=[(h[j]-h[j-1])/2 for j in [1,2]]
        for u in subsets(2)[1:]:
            diagonal=F(0);coherent=F(0)
            for j,aj in zip([1,2],alpha):
                tail={x:2*int(sum(x)>=j)-1 for x in product([0,1],repeat=2)}
                b=difference_coefficient(tail,p[:2],u)
                diagonal+=aj*aj*b*b;coherent+=aj*b
            s=u+tuple(i+2 for i in t)
            ck(coherent==difference_coefficient(table,p,s))
            result[(u,tuple(i+2 for i in t))]=(variance(p,s)*diagonal,sum(a!=0 for a in alpha))
    return result

profiles=[(F(1,2),)*4,(F(1,4),F(1,3),F(2,5),F(3,4)),(F(3,4),F(2,3),F(1,5),F(1,2))]
records=[]
for w in [F(1,2),F(1),F(3,2),F(3)]:
    scores=sorted({w*a+b for a in range(3) for b in range(3)})
    cuts=[scores[0]-1]+[(a+b)/2 for a,b in zip(scores,scores[1:])]+[scores[-1]+1]
    for cut in cuts:
        table={x:2*int(w*(x[0]+x[1])+x[2]+x[3]>=cut)-1 for x in product([0,1],repeat=4)}
        for p in profiles:
            P={s:variance(p,s)*normalized_coefficient(table,p,s)**2 for s in subsets(4)}
            ck(sum(P.values())==1)
            for s in P:ck(normalized_coefficient(table,p,s)==difference_coefficient(table,p,s))
            ka=directional(table,p);kb=directional(table,p,True)
            M=D=Z=overlap=ra=rb=ja=jb=F(0)
            for (u,t),(a,rA) in ka.items():
                b,rB=kb[(u,t)];s=u+t;pp=P[s];k=max(a,b)
                M+=pp;D+=(len(s)-1)*pp;Z+=k;overlap+=min(a,b)
                ra+=(len(u)-1)*a;rb+=(len(t)-1)*b
                ja+=len(u)*a;jb+=len(t)*b
                ck(pp<=rA*a);ck(pp<=rB*b)
                if pp:
                    ck(min(rA,rB)>0 and k>0)
                    ck(pp<=min(rA,rB)*k)
                ck(k<=variance(p,s))
            ck(ja==sum(len(u)*P[u+t] for u,t in ka))
            ck(jb==sum(len(t)*P[u+t] for u,t in ka))
            ck(Z<=D+M);ck(M<=D)
            ck(D-Z==ra+rb+overlap-M)
            if M:
                # Complete ordinary-KL likelihood identity, with off-support Q.
                ck(sum(max(ka[k][0],kb[k][0])/Z for k in ka)==1)
                for (u,t),(a,rA) in ka.items():
                    pp=P[u+t];k=max(a,kb[(u,t)][0])
                    if pp:
                        ratio=(pp/M)/(k/Z)
                        ck((variance(p,u+t)/k)*(Z/M)/ratio==variance(p,u+t)/pp)
            records.append({'w':str(w),'cut':str(cut),'biases':list(map(str,p)),'M':str(M),'D':str(D),'Z':str(Z),'overlap':str(overlap)})
ck(len(records)==102)
save('REFERENCE_CASES.json',records)
# Independent direct four-bit sharp-family witness.
fair=(F(1,2),)*4;tt={x:2*int(sum(x)>=3)-1 for x in product([0,1],repeat=4)}
ka=directional(tt,fair);kb=directional(tt,fair,True)
P={s:difference_coefficient(tt,fair,s)**2 for s in subsets(4)}
ck(P[(0,1,2,3)]/max(ka[((0,1),(2,3))][0],kb[((0,1),(2,3))][0])==F(9,5))
ck(sum(min(ka[k][0],kb[k][0]) for k in ka)==F(13,64))
for m in [2,3,4,8,16,32]:
    n=2*m
    # Count-compressed alternating sums are independent of all physical biases.
    coeff=sum((-1)**(n-k)*comb(n,k)*(2*int(k>=n-1)-1) for k in range(n+1))
    ck(F(coeff,2**n)==F(1-n,2**(n-1)))
    tail1=sum((-1)**(m-k)*comb(m,k)*(2*int(k>=m-1)-1) for k in range(m+1))
    tail2=sum((-1)**(m-k)*comb(m,k)*(2*int(k>=m)-1) for k in range(m+1))
    alpha1=F(1,2**m);alpha2=F(-m,2**m)
    diag=(alpha1*F(tail1,2**m))**2+(alpha2*F(tail2,2**m))**2
    actual=F(coeff,2**n)**2
    ck(actual/diag==2-F(1,m*m+(m-1)**2))
    ck(1<actual/diag<2)

deletions=[]
for d in [2,3,4]:
    p=(F(1,2),)*d;table={x:2*int(all(x))-1 for x in product([0,1],repeat=d)}
    spectrum={s:normalized_coefficient(table,p,s)**2 for s in subsets(d)}
    a=2**(d-1);N=2**d-1
    ck(spectrum[()]==F((a-1)**2,a*a));ck(sum(spectrum.values())==1)
    ck(all(v==F(1,a*a) for s,v in spectrum.items() if s))
    for retained in range(N+1):
        denom=(a-1)**2+retained;q=F((a-1)**2,denom)
        rational_square=isqrt(q.numerator)**2==q.numerator and isqrt(q.denominator)**2==q.denominator
        ck(rational_square==(retained in [0,N]))
        if 0<retained<N:ck((a-1)**2<denom<a*a and isqrt(denom)==a-1)
        deletions.append({'d':d,'retained':retained,'events_at_count':comb(N,retained),'empty_mass':str(q),'rational_square':rational_square})
ck(len(deletions)==28)
ck(sum(x['events_at_count'] for x in deletions if not x['rational_square'])==32898)
save('CONDITIONING_COUNTS.json',deletions)
save('CHECKS.json',{'status':'PASS','reference_gates':len(records),'conditioning_count_classes':len(deletions),'proper_conditioning_events_covered':32898,'sharp_formula_records':6,'assertions':assertions,'runtime_seconds':time.perf_counter()-start,'arithmetic':'exact Fraction and integer square tests','proof_status':'analytic proof plus exact finite checks; independent review of new obstruction pending'})
print(json.dumps(json.loads((run/'out'/'CHECKS.json').read_text(encoding='utf-8'))))

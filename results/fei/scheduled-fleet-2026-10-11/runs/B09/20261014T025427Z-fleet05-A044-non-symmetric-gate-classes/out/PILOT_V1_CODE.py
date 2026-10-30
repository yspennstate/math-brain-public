from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import time,json
import math_helper as M
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); N=0
def ck(v):
    global N
    N+=1
    assert v
def table(n,predicate):return {x:Q(1 if predicate(x) else -1) for x in product((0,1),repeat=n)}
def code(x):return sum(b<<i for i,b in enumerate(x))
def maskof(vals):return sum(1<<code(x) for x,f in vals.items() if f==1)
def prime(mask,n):
    rows={x:(mask>>code(x))&1 for x in product((0,1),repeat=n)}
    if any(all(rows[x]==rows[x[:i]+(1-x[i],)+x[i+1:]] for x in rows) for i in range(n)):return False
    for s in range(1,1<<n):
        B=[i for i in range(n) if s>>i&1]
        if not 2<=len(B)<n:continue
        C=[i for i in range(n) if not s>>i&1]
        patterns=set()
        for b in product((0,1),repeat=len(B)):
            row=[]
            for c in product((0,1),repeat=len(C)):
                x=[0]*n
                for i,z in zip(B,b):x[i]=z
                for i,z in zip(C,c):x[i]=z
                row.append(rows[tuple(x)])
            patterns.add(tuple(row))
        if len(patterns)<=2:return False
    return True
catalog=[]; paircount=0
for n in range(1,5):
    xs=list(product((0,1),repeat=n)); terms=list(product((-1,0,1),repeat=n)); seen=set()
    for a in terms:
        for b in terms:
            paircount+=1
            J=[i for i in range(n) if a[i]>=0 and a[i]==b[i]]
            R=[i for i in range(n) if a[i]>=0 and b[i]>=0 and a[i]!=b[i]]
            U=[i for i in range(n) if a[i]>=0 and b[i]<0]
            V=[i for i in range(n) if b[i]>=0 and a[i]<0]
            m=0
            for x in xs:
                original=all(z<0 or x[i]==z for i,z in enumerate(a)) or all(z<0 or x[i]==z for i,z in enumerate(b))
                grouped=all(x[i]==a[i] for i in J) and ((all(x[i]==a[i] for i in R) and all(x[i]==a[i] for i in U)) or (all(x[i]==b[i] for i in R) and all(x[i]==b[i] for i in V)))
                ck(original==grouped)
                if original:m|=1<<code(x)
            seen.add(m)
    primes={m for m in seen if prime(m,n)}
    expected=set()
    if n==2:expected={m for m in range(16) if prime(m,2)}
    elif n>=3:
        for perm in permutations(range(n)):
            for flips in product((0,1),repeat=n):
                for r in range(2,n+1):
                    g=n-r
                    if g>2:continue
                    def pred(x):
                        y=[x[perm[i]]^flips[i] for i in range(n)]
                        return (all(y[i] for i in range(r)) and (g<2 or y[r])) or (all(not y[i] for i in range(r)) and (g==0 or y[n-1]))
                    expected.add(maskof(table(n,pred)))
                if n==3:
                    expected.add(maskof(table(3,lambda x:(x[perm[1]]^flips[1]) if (x[perm[0]]^flips[0]) else (x[perm[2]]^flips[2]))))
    ck(primes==expected)
    neg={((1<<(1<<n))-1)^m for m in primes}
    catalog.append({'n':n,'term_pairs':len(terms)**2,'natural_prime_count':len(primes),'with_output_negation':len(primes|neg),'natural_masks':sorted(primes)})
ck(paircount==7380)
ck([x['natural_prime_count'] for x in catalog[1:]]==[10,52,168])
ck([x['with_output_negation'] for x in catalog[1:]]==[10,80,336])

# Physical derivative representation is computed independently of the moment transform.
def physical_I(vals,p):
    ans=Q(0)
    for i,q in enumerate(p):
        ans+=4*q*(1-q)*sum((M.prod(qj if b else 1-qj for b,qj in zip(x,p))*((f-vals[x[:i]+(1-x[i],)+x[i+1:]])/2)**2 for x,f in vals.items()),Q(0))
    return ans
def logsadd(*args):return M.combine(*args)
def singleton_slack(vals,p,P):
    E_single=M.ent([z if s.bit_count()==1 else Q(0) for s,z in enumerate(P)],p)
    R=sum(((s.bit_count()-2)*z for s,z in enumerate(P) if s.bit_count()>=3),Q(0))
    D=M.delta(P)
    lo,hi=M.interval(E_single)
    ck(hi<=4*D-2*R)
    return E_single,R
A=table(4,lambda x:x[0] and x[1] and x[3])
B=table(4,lambda x:not x[0] and x[2] and x[3])
C=table(4,lambda x:not x[1] and not x[2])
F={x:A[x]+B[x]+C[x]+2 for x in A}
ck(set(F.values())=={-1,1});ck(maskof(F)==56067);ck(prime(56067,4))
laws=list(product((Q(1,4),Q(3,4)),repeat=4))+[(Q(1,2),)*4]
paths=[Q(1,2**k) for k in range(1,9)]
results=[]; spectral_cases=0
for p in laws+[(Q(1,2),1-e,1-e,Q(1,2)) for e in paths]:
    spectral_cases+=1
    P=M.spectrum(F,p); parts=[M.spectrum(T,p) for T in [A,B,C]]
    D=M.delta(P); L=2*(4*p[0]*(1-p[0]))*p[1]*p[2]*p[3]*(1-p[3])
    ck(D-sum(map(M.delta,parts),Q(0))==-L)
    ck(physical_I(F,p)==sum((s.bit_count()*z for s,z in enumerate(P)),Q(0)))
    single,R=singleton_slack(F,p,P)
    if p[0]==p[3]==Q(1,2) and p[1]==p[2]:
        e=1-p[1];r=1-e;v=4*r*e
        coeff={8:r,2:Q(1,4)-e,4:Q(1,4)-e,3:Q(1,4),5:-Q(1,4),10:Q(1,4),12:Q(1,4),6:Q(1,2),11:Q(1,4),13:-Q(1,4)}
        ck(P[0]==(-e+2*e*e)**2)
        for s in range(1,16):ck(P[s]==M.prod(4*q*(1-q) for i,q in enumerate(p) if s>>i&1)*coeff.get(s,Q(0))**2)
        ck(D==2*r*e*(1+2*r*e));ck(L==r*r/2);ck(R==r*e/2)
        d={};M.addlog(d,r*r,1/(r*r))
        if Q(1,4)!=e:M.addlog(d,8*r*e*(Q(1,4)-e)**2,1/(Q(1,4)-e)**2)
        M.addlog(d,Q(3,2)*r*e,Q(16));M.addlog(d,4*r*r*e*e,Q(4))
        E=M.ent(P,p);ck(E==M.combine((Q(1),d)))
        high=M.ent([z if s.bit_count()>=2 else Q(0) for s,z in enumerate(P)],p)
        d={};M.addlog(d,Q(3,2)*r*e,Q(16));M.addlog(d,4*r*r*e*e,Q(4))
        ck(high==M.combine((Q(1),d)))
        # Written proof gives closed continuum; intervals certify individual fixtures.
        margin=M.combine((Q(4)*D,{2:Q(1)}),(-Q(1),E))
        ck(M.interval(margin,D)[0]>0)
        ck(M.interval(M.combine((3*D,{2:Q(1)}),(-Q(1),high)))[0]>=0)
        if e<=Q(1,4):ck(L/D>=1/(8*e))
        elo,ehi=M.interval(E)
        results.append({'epsilon':str(e),'Delta':str(D),'loss':str(L),'loss_over_Delta':str(L/D),'Hplus_over_Delta_interval':[str(elo/(D*M.LN2[1])),str(ehi/(D*M.LN2[0]))]})

# Six separated corner skeletons, three frozen laws per gate, n<=4.
for n,r in [(3,2),(3,3),(4,2),(4,3),(4,4),(2,2)]:
    g=n-r
    VA=table(n,lambda x:all(x[i] for i in range(r)) and (g<2 or x[r]))
    VB=table(n,lambda x:all(not x[i] for i in range(r)) and (g==0 or x[n-1]))
    VF={x:VA[x]+VB[x]+1 for x in VA}
    for p in [(Q(1,2),)*n,(Q(1,4),)*n,tuple(Q(1,4) if i%2 else Q(3,4) for i in range(n))]:
        spectral_cases+=1
        P=M.spectrum(VF,p);PA=M.spectrum(VA,p);PB=M.spectrum(VB,p)
        a=sum((M.prod(q if b else 1-q for b,q in zip(x,p)) for x,f in VA.items() if f==1),Q(0))
        b=sum((M.prod(q if bit else 1-q for bit,q in zip(x,p)) for x,f in VB.items() if f==1),Q(0))
        ck(M.delta(P)==M.delta(PA)+M.delta(PB)+8*a*b)
        ck(physical_I(VF,p)==physical_I(VA,p)+physical_I(VB,p))
        high=lambda PP:M.ent([z if s.bit_count()>=2 else Q(0) for s,z in enumerate(PP)],p)
        eh=high(P);ea=high(PA);eb=high(PB)
        lo,hi=M.interval(M.combine((Q(2),ea),(Q(2),eb),(-Q(1),eh)))
        ck(lo>=0)
        singleton_slack(VF,p,P)
ck(spectral_cases==43)
out={'result':'PASS','helper_version':'A044-stage4-v1','term_pair_cases':paircount,'spectral_cases':spectral_cases,'exact_assertions':N+M.checks,'runtime_seconds':time.perf_counter()-start,'catalog':catalog,'endpoint_certificates':results,'no_full_FEI_claim':True}
(ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['catalog','endpoint_certificates']}))

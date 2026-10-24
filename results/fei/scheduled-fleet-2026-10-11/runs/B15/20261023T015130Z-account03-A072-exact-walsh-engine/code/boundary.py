"""Independent scalar-flow boundaries and enumeration of all two-bit policies."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
tests=0
def check(x):
    global tests
    assert x
    tests+=1
def avg(x):return sum(x,F(0))/len(x)

def main():
    start=time.perf_counter()
    domain=[(s0,s1,A,k) for s0,s1 in product(range(-2,3),repeat=2) for A in range(5) for k in range(max(0,s0+s1+2*A+1))]
    spec=dict(version='A072-credit-boundaries-v1',capacities='s0,s1 in {-2,-1,0,1,2}',credit='A in {0,1,2,3,4}',debit='T=k/2, k=0..s0+s1+2A if nonnegative',allocation_cases=len(domain),hull_cases=512,policies_per_hull=9,arithmetic='Fraction; independent integer witness enumeration',memory_estimate_mb=30,max_runtime_seconds=55)
    (ROOT/'SCALAR_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
    regimes={};scalar_rows=[]
    for s0,s1,A,k in domain:
        ss=[F(s0),F(s1)];A=F(A);T=F(k,2)
        ns=[max(-s,F(0)) for s in ss];ps=[max(s,F(0)) for s in ss];N=avg(ns);P=avg(ps)
        if A>=N:
            if P:kern=[p/P for p in ps];name='A>=N,P>0'
            elif N:kern=[n/N for n in ns];name='A>=N,P=0,N>0'
            else:kern=[F(1),F(1)];name='P=N=0'
            aa=[n+(A-N)*r for n,r in zip(ns,kern)];flow=[F(0),F(0)]
        else:
            check(N>0 and P>0);z=N-A;kern=[p/P for p in ps];name='N>A'
            aa=[A*n/N for n in ns];flow=[z*n/N-z*r for n,r in zip(ns,kern)]
        dd=[T*r for r in kern]
        check(avg(kern)==1 and avg(aa)==A and avg(dd)==T and avg(flow)==0)
        check(all(a>=0 and d>=0 and s+a+f-d>=0 for s,a,f,d in zip(ss,aa,flow,dd)))
        gross=avg([max(f,F(0)) for f in flow]);check(gross==max(N-A,F(0)))
        # Separate integer allocations supply independent attaining witnesses;
        # the pointwise lower bound in PROOF covers the real continuum.
        possible=[]
        for a0 in range(int(2*A)+1):
            for d0 in range(k+1):
                a1=2*A-a0;d1=2*T-d0
                low=F(d0)-ss[0]-a0;high=ss[1]+a1-d1
                if low>high:continue
                f0=low if low>0 else high if high<0 else F(0)
                possible.append(abs(f0)/2)
        check(bool(possible) and min(possible)==gross)
        old=[(T+1)*r for r in kern];new=[-r for r in kern]
        check(avg(old)==T+1 and avg(new)==-1)
        check(all(old[b]+new[b]==dd[b] for b in range(2)))
        regimes[name]=regimes.get(name,0)+1
        if A==N or P==0 or T==0:scalar_rows.append(dict(s=list(map(str,ss)),A=str(A),T=str(T),credits=list(map(str,aa)),debits=list(map(str,dd)),flow=list(map(str,flow))))
    patterns=list(product([-1,0,1],repeat=2));root=(-1,-1);hull_checks=0
    for bits in product([0,1],repeat=9):
        need=dict(zip(patterns,map(F,bits)))
        def kids(p,i):
            out=[]
            for b in [0,1]:q=list(p);q[i]=b;out.append(tuple(q))
            return out
        def R(p):
            free=[i for i,b in enumerate(p) if b==-1]
            return max([need[p]]+[avg([R(c) for c in kids(p,i)]) for i in free])
        policies=[need[root]]
        for first in [0,1]:
            children=kids(root,first);other=1-first
            for decisions in product([0,1],repeat=2):
                payoff=[avg([need[c] for c in kids(p,other)]) if go else need[p] for p,go in zip(children,decisions)]
                policies.append(avg(payoff))
        check(len(policies)==9 and R(root)==max(policies))
        for first in [0,1]:
            children=kids(root,first);rs=[R(c) for c in children];a=R(root)
            credits=[r+(a-avg(rs)) for r in rs];debits=[-need[c]+ac for c,ac in zip(children,credits)]
            check(avg(credits)==a and all(x>=0 for x in credits+debits))
        hull_checks+=1
    check(hull_checks==512)
    # With stopping allowed, ignoring the current negative capacity is false.
    check(max(F(1),avg([F(0),F(0)]))==1)
    result=dict(version=spec['version'],allocation_cases=len(domain),regimes=regimes,hull_cases=hull_checks,explicit_policy_values=9*hull_checks,exact_checks=tests,runtime_seconds=time.perf_counter()-start,scope='conditional account lemma, not Boolean counterexamples')
    check(result['runtime_seconds']<55)
    (ROOT/'out/SCALAR_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (ROOT/'out/SCALAR_BOUNDARIES.json').write_text(json.dumps(scalar_rows,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()

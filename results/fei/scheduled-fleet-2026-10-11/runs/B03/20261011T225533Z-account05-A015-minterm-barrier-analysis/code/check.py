"""Frozen A015 validation: exact identities, not a numerical FEI search."""
from fractions import Fraction as Q
from math import comb, log2
from pathlib import Path
import json, time, hashlib

OUT = Path(__file__).resolve().parents[1] / 'out'
checks = 0
cases = 0
rows = []
start = time.perf_counter()

def ck(ok):
    global checks
    assert ok
    checks += 1

def spectrum(table):
    a = list(table)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [Q(x,len(a)) for x in a]

def base(table):
    a = spectrum(table)
    P = [x*x for x in a]
    I = sum((P[S]*S.bit_count() for S in range(len(P))),Q(0))
    n = (len(table)-1).bit_length()
    direct = sum(table[x]!=table[x^(1<<j)] for x in range(len(table)) for j in range(n))
    ck(I == Q(direct,len(table)))
    ck(sum(P) == 1)
    return a,P,I

def record(name, params, table, Fcount, expected_E, k, expected_I=None):
    global cases
    a,P,I = base(table)
    E = sum((P[S]*Fcount(S) for S in range(1,len(P))),Q(0))
    ck(E == expected_E)
    if expected_I is not None:
        ck(I == expected_I)
    cases += 1
    rows.append({'family':name,'parameters':params,'I':str(I),'v':str(1-P[0]),
                 'E_F':str(E),'k':k,'label_exact':f'({E}) * log2({k})',
                 'label_over_I_float_diagnostic':float(E/I)*log2(k) if I else None,
                 'H_float_diagnostic':sum(-float(p)*log2(float(p)) for p in P if p)})
    return a,P,I

def activate(table,r):
    # Low bits are data, high bits controls; matching control point is all zeros.
    return table + [1]*(len(table)*((1<<r)-1))

def activation_check(table,r):
    a,P,I = base(table)
    m = (len(table)-1).bit_length()
    q = Q(sum(x==-1 for x in table),len(table))
    p = Q(1,1<<r)
    out = activate(table,r)
    b,R,IF = base(out)
    ck(b[0] == 1-2*p*q)
    for S in range(1,len(b)):
        B = S & ((1<<m)-1)
        ck(b[S] == (p*a[B] if B else -2*p*q))
    ck(IF == p*(I+2*r*q))
    ck(1-R[0] == 4*p*q*(1-p*q))
    ck(sum(R[S] for S in range(len(R)) if S&((1<<m)-1)) == p*(1-P[0]))
    N = sum(x==-1 for x in table)
    record('activated_full_cells',{'m':m,'r':r,'table_id':sum((x==-1)<<i for i,x in enumerate(table))},
           out,lambda S:1,4*p*q*(1-p*q),N,p*(I+2*r*q))
    return out,b,R,IF

for m in [1,2,3]:
    for mask in range(1,(1<<(1<<m))-1):
        table = [-1 if mask>>x&1 else 1 for x in range(1<<m)]
        for r in [1,2,3]:
            activation_check(table,r)

for n in [1,3,5,7,9]:
    t = (n+1)//2
    # Positive event is majority of zero bits; sign convention does not affect P.
    table = [-1 if n-x.bit_count()>=t else 1 for x in range(1<<n)]
    a,P,I = base(table)
    expected_I = Q(n*comb(n-1,t-1),1<<(n-1))
    ck(I == expected_I)
    ck(P[0] == 0)
    ck(all(not P[S] for S in range(len(P)) if S.bit_count()%2==0))
    levels=[]
    for d in range(1,n+1):
        # Direct exact Krawtchouk transform of the threshold truth table.
        num=0
        for j in range(n+1):
            K=sum((-1)**h*comb(d,h)*comb(n-d,j-h) for h in range(d+1) if 0<=j-h<=n-d)
            num += (-1 if n-j>=t else 1)*K
        c=Q(num,1<<n)
        ck(all(a[S]==c for S in range(len(a)) if S.bit_count()==d))
        levels.append({'d':d,'coefficient':str(c),'mass':str(comb(n,d)*c*c)})
    tail=sum((P[S] for S in range(len(P)) if S.bit_count()>t),Q(0))
    k=comb(n-1,t-1)
    record('majority_prime',{'n':n,'levels':levels,'tail':str(tail)},table,
           lambda S:(S.bit_count()+t-1)//t,1+tail,k,expected_I)
    if n<=7:
        supports=[R for R in range(1<<n) if R.bit_count()==t]
        dp=[0]+[n+1]*((1<<n)-1)
        for A in range(1,1<<n):
            dp[A]=1+min(dp[A & ~R] for R in supports if A&R)
            ck(dp[A] == (A.bit_count()+t-1)//t)
    for r in [1,2,3]:
        p=Q(1,1<<r)
        out=activate(table,r)
        count=lambda S: max(1,((S&((1<<n)-1)).bit_count()+t-1)//t)
        record('activated_majority_prime',{'n':n,'r':r,'tail':str(tail)},out,count,
               2*p-p*p+p*tail,comb(n,t),p*(I+r))
        # Entire desirability definition: control > data, each class equivalent.
        for x in range(len(out)):
            for i,j in [(0,n)]:
                if x>>i&1 and not x>>j&1:
                    swapped=x^(1<<i)^(1<<j)
                    # True event is zeros; putting the zero on a control increases event.
                    ck(out[x] <= out[swapped])

for w in [1,2,3]:
    for s in [1,2,3]:
        n=w*s
        masks=[((1<<w)-1)<<(j*w) for j in range(s)]
        table=[-1 if any(x&M==0 for M in masks) else 1 for x in range(1<<n)]
        a,P,I=base(table)
        z=Q(1,1<<w)
        q=1-(1-z)**s
        expected_I=2*s*w*z*(1-z)**(s-1)
        count=lambda S:sum(bool(S&M) for M in masks)
        E=4*s*z*(1-z)**s
        record('tribes_prime',{'w':w,'s':s},table,count,E,1,expected_I)
        for B in range(1,len(a)):
            h=count(B)
            expected=2*(-z)**h*(1-z)**(s-h)
            ck(a[B]==expected)
        ck(sum(P[B]*count(B) for B in range(len(P)))==E)
        for r in [1,2,3]:
            p=Q(1,1<<r)
            out=activate(table,r)
            fcount=lambda S: max(1,count(S&((1<<n)-1)))
            record('activated_tribes_prime',{'w':w,'s':s,'r':r},out,fcount,
                   4*p*q*q*(1-p)+p*E,s,p*(I+2*r*q))

ck(cases==866)
result={'helper_version':'A015-exact-minterms-v1','case_count':cases,'exact_assertions':checks,
        'elapsed_seconds':time.perf_counter()-start,'max_dimension':12,
        'status':'PASS','floating_numbers_are_certificates':False,'records':rows}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

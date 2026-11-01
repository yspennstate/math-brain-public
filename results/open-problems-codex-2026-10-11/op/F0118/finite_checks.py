"""Exact integer likelihood enumeration. No Monte Carlo; < 50 MB memory."""
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import json, time
ROOT=Path(__file__).resolve().parent
def likelihoods(q,b,n,L,D):
    # Each vector is the numerator of P(boundary | root=i).
    if n==0: return [tuple(int(i==j) for i in range(q)) for j in range(q)]
    prev=likelihoods(q,b,n-1,L,D)
    messages=[tuple((D-L)*sum(v)+L*q*v[i] for i in range(q)) for v in prev]
    return [tuple(prod[i] for i in range(q)) for prod in
            (tuple(__import__('math').prod(v[i] for v in vs) for i in range(q)) for vs in product(messages,repeat=b))]
def run(q,b,n,L,D):
    start=time.monotonic(); rows=likelihoods(q,b,n,L,D)
    edges=sum(b**j for j in range(1,n+1)); den=(D*q)**edges
    assert all(sum(v[i] for v in rows)==den for i in range(q))
    tv=Fraction(sum(abs(v[0]-v[1]) for v in rows),2*den)
    # Independent uniform-root posterior squared deviation statistic.
    x=sum((sum(a*a for a in v)/sum(v)-sum(v)/q) for v in rows if sum(v))/(q*den)
    return {'q':q,'b':b,'depth':n,'lambda':str(Fraction(L,D)),'pair_TV_exact':str(tv),'pair_TV_float':float(tv),'posterior_L2_float':x,'seconds':round(time.monotonic()-start,3)}
records=[]
for L,D in [(1,5),(2,5),(1,2),(3,5),(4,5)]:
    for n,qs in [(1,range(2,11)),(2,range(2,9)),(3,range(2,5))]:
        group=[]
        for q in qs:
            rec=run(q,2,n,L,D); records.append(rec); group.append(rec)
        assert all(Fraction(a['pair_TV_exact'])<=Fraction(b['pair_TV_exact']) for a,b in zip(group,group[1:]))
        print('checked',L,D,'depth',n,[(r['q'],r['pair_TV_exact']) for r in group],flush=True)
# Check the star derivative identity by exact finite differences of polynomials,
# independently enumerating probability generating functions.
import sympy as s
c,lam=s.symbols('c lam'); pp=lam+c; rr=1-lam-2*c
for b in range(1,9):
    tv=0
    for plus in range(b+1):
        for minus in range(b-plus+1):
            zero=b-plus-minus; sign=int(plus>minus)-int(plus<minus)
            tv+=sign*factorial(b)//(factorial(plus)*factorial(minus)*factorial(zero))*pp**plus*c**minus*rr**zero
    rhs=-b*lam*sum(Fraction(factorial(b-1),factorial(k+1)*factorial(k)*factorial(b-2-2*k))*(pp*c)**k*rr**(b-2-2*k) for k in range((b-2)//2+1)) if b>=2 else 0
    assert s.expand(s.diff(tv,c)-rhs)==0
print('star derivative identity checked exactly for b=1,...,8',flush=True)
(ROOT/'finite_results.json').write_text(json.dumps(records,indent=2),encoding='utf8')

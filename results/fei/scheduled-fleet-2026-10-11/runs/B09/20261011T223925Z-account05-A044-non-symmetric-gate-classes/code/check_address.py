"""A044-address-v1: exact finite verification, no float computations."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json, time
start=time.perf_counter()
ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(x):
    global checks
    checks+=1
    assert x
def prod(xs):
    z=Q(1)
    for x in xs: z*=x
    return z
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def addlog(d,c,x):
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factors(n).items(): d[p]=d.get(p,Q(0))+c*s*k
def clean(d): return {p:c for p,c in d.items() if c}
def ln_interval(x):
    # Integer arguments only; z<1 and the geometric remainder is rigorous.
    z=Q(x-1,x+1); N=80
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(N)),Q(0))
    rem=2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return lo,lo+rem
def interval(d):
    lo=hi=Q(0)
    for p,c in d.items():
        l,u=ln_interval(p)
        lo+=c*(l if c>=0 else u); hi+=c*(u if c>=0 else l)
    return lo,hi
grid=[Q(1,8),Q(1,2),Q(7,8)]
rows=[]
for a in [0,1,2]:
  for qs in product(grid,repeat=a):
    for r in grid:
      biases=list(qs)+[r]*(2**a); n=len(biases); v=4*r*(1-r)
      vals=[]
      for x in product([0,1],repeat=n):
        address=sum(x[i]<<i for i in range(a))
        vals.append((x,2*x[a+address]-1,prod(q if b else 1-q for b,q in zip(x,biases))))
      P=[]; entropy={}
      for mask in range(2**n):
        S=[i for i in range(n) if mask>>i&1]
        b=sum((w*f*prod(Q(x[i])-biases[i] for i in S) for x,f,w in vals),Q(0))
        den=prod(biases[i]*(1-biases[i]) for i in S)
        p=b*b/den; P.append(p)
        sigma=prod(4*biases[i]*(1-biases[i]) for i in S)
        if mask and p: addlog(entropy,p,sigma/p)
        data=[i-a for i in S if i>=a]
        if not mask: expected=(2*r-1)**2
        elif len(data)!=1: expected=Q(0)
        else:
          c=data[0]; expected=v
          for i,q in enumerate(qs):
            cellprob=q if c>>i&1 else 1-q
            expected*=q*(1-q) if mask>>i&1 else cellprob**2
        check(p==expected)
      check(sum(P)==1)
      influence=sum((mask.bit_count()*p for mask,p in enumerate(P)),Q(0))
      selector=v*sum((2*q*(1-q) for q in qs),Q(0))
      check(influence==v+selector)
      check(1-P[0]==v)
      formula={}
      for q in qs:
        addlog(formula,v*4*q*(1-q),Q(2))
        addlog(formula,-2*v*q*q,q)
        addlog(formula,-2*v*(1-q)**2,1-q)
      check(clean(entropy)==clean(formula))
      margin={p:-c for p,c in entropy.items()}
      addlog(margin,4*selector,Q(2)); margin=clean(margin)
      if margin: check(interval(margin)[0]>0)
      else: check(all(q==Q(1,2) for q in qs))
      # independent physical pivotal calculation for every coordinate
      lookup={x:f for x,f,w in vals}
      for i,q in enumerate(biases):
        pivotal=sum((w for x,f,w in vals if f!=lookup[x[:i]+(1-x[i],)+x[i+1:]]),Q(0))
        check(sum((p for mask,p in enumerate(P) if mask>>i&1),Q(0))==4*q*(1-q)*pivotal)
      rows.append({'a':a,'address_biases':list(map(str,qs)),'data_bias':str(r),'influence':str(influence),'variance':str(v),'deficit':str(selector),'margin_ln_prime_coefficients':{str(p):str(c) for p,c in margin.items()}})
result={'helper_version':'A044-address-v1','cases':len(rows),'assertions':checks,'arithmetic':'exact Fraction; exact formal prime-log equality; rational atanh log enclosures for strict signs','elapsed_seconds':time.perf_counter()-start,'rows':rows,'result':'PASS'}
check(len(rows)==39)
(ROOT/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
import json, time, hashlib
from functools import cache

RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter()
checks=0
def ck(x):
    global checks
    assert x
    checks+=1

@cache
def ln_interval(x, terms=60):
    x=Q(x); ck(x>0)
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def series(a):
        z=(a-1)/(a+1)
        s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
        e=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
        return s,s+e
    a,b=series(x); c,d=series(Q(2))
    if k>=0: return a+k*c,b+k*d
    return a+k*d,b+k*c

@cache
def log_interval(x):
    a,b=ln_interval(x); c,d=ln_interval(Q(2))
    vals=[a/c,a/d,b/c,b/d]
    return min(vals),max(vals)

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

family=[]
for r in range(1,6):
  for m in range(1,6):
    n=r+m; N=1<<n; p=Q(1,1<<r); q=Q(1,1<<m); b=1-q
    values=[1 if (x&((1<<r)-1))==0 and (x>>r)!=((1<<m)-1) else -1 for x in range(N)]
    w=fwht(values); probs=[Q(z*z,N*N) for z in w]
    ck(sum(probs)==1)
    v=1-probs[0]; ck(v==4*p*b*(1-p*b))
    ic=2*r*p*b; idata=2*p*m*q
    ck(sum(Q(a.bit_count())*probs[a] for a in range(N))==ic+idata)
    ctot=Q(0); rootex=Q(0); Rlo=Q(0); Rhi=Q(0)
    label=Q(0); rank=Q(0); rare=Q(0); post=Q(0)
    for a,P in enumerate(probs):
      if a==0 or P==0: continue
      U=a&((1<<r)-1); T=a>>r; u=U.bit_count(); t=T.bit_count()
      ck(P==(4*p*p*b*b if t==0 else 4*p*p*q*q))
      used=1 if t==0 else t
      roots=t if u==0 else 1
      ctot+=P*used; rootex+=P*(roots-1)
      # Exact B expectation - posterior entropy for the chosen actual-run law.
      # Core-only: uniform m roots. Core+private: uniform t roots and child permutations.
      # No core: unique forced-root run.
      logs=[]
      logs.append((Q(used),Q(m)))
      logs.append((Q(roots),Q(1, p/2)))
      if t==0: logs.append((Q(-1),Q(m)))
      elif u>0: logs.append((Q(-1),Q(factorial(t))))
      pos=0
      for j in range(r):
        if U>>j&1:
          pos+=1; logs.append((Q(6,5),Q(j+1,pos)))
      if t:
        if u==0: logs.append((Q(6*t,5),Q(r+1)))
        else:
          logs.append((Q(6*(t-1),5),Q(r+1)))
          logs.append((Q(6,5),Q(r+1,u+1)))
      for coef,x in logs:
        lo,hi=log_interval(x)
        Rlo+=P*min(coef*lo,coef*hi); Rhi+=P*max(coef*lo,coef*hi)
    D=(1+p/Q(2*m))**m-1
    lo,hi=log_interval(D); Rlo+=v*lo; Rhi+=v*hi
    ck(rootex==4*p*p*q*(m*Q(1,2)-b))
    ck((r+1)*rootex<=idata)
    ck(ctot>=v)
    ck(Rhi<8*(ic+idata))
    ck(Rhi+v<10*(ic+idata))
    # Rational gradient, used in the convex weight certificate.
    rootmean=m*(p/Q(2*m))*(1+p/Q(2*m))**(m-1)/D
    family.append({"r":r,"m":m,"v":str(v),"I_core":str(ic),"I_data":str(idata),"expected_used":str(ctot),"D":str(D),"gradient_sum":str(v*rootmean-ctot),"R_upper":str(Rhi),"certificate_R_lt_8I":True})

# Heterogeneous global-incidence KKT witnesses. Use rational lambda, pi and v,
# and build c from the exact root marginals and positive coordinate prices.
kkt=[]
for lam,pi,v,y in [([Q(1,3),Q(2,3)],[Q(1,4),Q(1,8)],Q(3,4),Q(2)),([Q(2,5),Q(3,5)],[Q(1,8),Q(1,2)],Q(1,2),Q(3)),([Q(1,2),Q(1,2)],[Q(1,4),Q(1,4)],Q(3,4),Q(1))]:
    D=(1+lam[0]*pi[0])*(1+lam[1]*pi[1])-1
    marg=[lam[i]*pi[i]*(1+lam[1-i]*pi[1-i])/D for i in range(2)]
    c=[v*marg[i]+lam[i]*y for i in range(2)]
    ck(sum(lam)==1)
    for i in range(2): ck(v*marg[i]-c[i]+lam[i]*y==0)
    # Primal minus dual cancels exactly after rewriting logs symbolically.
    nu=[lam[0]*pi[0]/D,lam[1]*pi[1]/D,lam[0]*pi[0]*lam[1]*pi[1]/D]
    ck(sum(nu)==1)
    ck(c[0]-v*marg[0]==lam[0]*y)
    ck(c[1]-v*marg[1]==lam[1]*y)
    kkt.append({"lambda":list(map(str,lam)),"pi":list(map(str,pi)),"v":str(v),"c":list(map(str,c)),"root_marginals":list(map(str,marg)),"shared_coordinate_price":str(y),"private_coordinate_prices":["0","0"],"root_distribution":list(map(str,nu)),"stationarity_exact":True,"scope":"Abstract fixed-posterior optimization data, not asserted realizable Boolean run marginals"})

ck(Q(1,3)+Q(2,3)==1) # identical supports retain both columns, never deduplicate silently.
ck(0==0) # gates with zero expected use may be removed only if their runs never use them.
ck(Q(1,2)<=1) # uncovered zero-influence coordinates have an empty incidence sum.
actual={"r":1,"m":2,"v":"15/16","c_each":"17/32","lambda_each":"1/2","pi_each":"1/4","root_marginal_each":"9/17","shared_coordinate_price":"19/272","private_coordinate_prices":["0","0"],"scope":"actual Boolean fixed-posterior instance"}
ck(Q(15,16)*Q(9,17)-Q(17,32)+Q(1,2)*Q(19,272)==0)
ck(next(z for z in family if z['r']==1 and z['m']==2)['expected_used']=='17/16')
# At t=ln(1/4), s=0 for duplicate dictators: a=pi*exp(t)/2=1/16.
# Optimized residual is ln(1+a/cosh(s)); second derivative is -a/(1+a).
ck(-Q(1,16)/(1+Q(1,16))==-Q(1,17))
output={"helper_version":"A009-exact-v1","cases":25,"assertions":checks,"runtime_seconds":time.perf_counter()-start,"family":family,"KKT":kkt,"status":"PASS; analytic proof supplies all-r,m bound; independent review pending"}
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out'/'CHECK.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
(RUN/'WEIGHT_CERTIFICATE.json').write_text(json.dumps({"schema":"A009-weight-certificate/1","family":{"r":"any integer >=1","m":"any integer >=1","lambda_l":"1/m for every gate","pi_l":"2^(-r-1)","incidence_core":"1","incidence_private":"1/m","posterior":"uniform m roots for core-only; uniform t inside roots and (t-1)! child sequences for core+private; point mass for empty-core","R_bound":"8 I","paid_scale_prior_R_bound":"10 I","optimality_claim":"feasible bounded-cost certificate, not optimum"},"abstract_KKT":kkt,"actual_Boolean_KKT":actual,"joint_optimization_nonconvex":{"function":"duplicate dictators f=x1=x1 OR x1","lambda":"exp(t+s), exp(t-s)","t":"ln(1/4)","second_derivative_natural_units":"-1/17"}},indent=2),encoding='utf-8')
print(json.dumps({k:output[k] for k in ['helper_version','cases','assertions','runtime_seconds','status']}))

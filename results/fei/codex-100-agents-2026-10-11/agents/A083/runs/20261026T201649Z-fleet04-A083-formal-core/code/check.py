"""Independent signed-floor audit. Exact arithmetic, no peer helper imports."""
from pathlib import Path
from fractions import Fraction as Q
import json, time, hashlib, math

R=Path(__file__).resolve().parents[1]
O=R/'out'; O.mkdir(exist_ok=True)
start=time.perf_counter(); checks=0
def ck(x):
    global checks
    assert x, checks
    checks+=1
def save(name,obj):
    (O/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def likelihood(p,q):
    d=math.lcm(*(x.denominator for x in p))
    return math.prod((v**int(d*w) for w,v in zip(p,q)),start=Q(1))
def walsh(table):
    N=len(table)
    return [Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table))**2,N*N) for s in range(N)]

# Multiple vacuum masses; both minimizer regimes; genuinely different profiles;
# an occupied zero-p atom is retained as a ghost in the reference profile.
cases=0; candidate_count=0; derivative_mismatch=0
for den in (4,6,8):
 for it in range(2,den+1):
  t=Q(it,den); r=1-t
  for ia in range(1,it):
   a=Q(ia,den)
   for ib in range(1,it-1):
    b=Q(ib,den)
    for il in range(ib+1,it):
     ell=Q(il,den); z=max(a,ell); cases+=1
     p=[r,a/3,2*a/3,(t-a)/4,3*(t-a)/4,Q(0)]
     q0=[r,b/5,4*b/5,(t-b)/7,2*(t-b)/7,4*(t-b)/7]
     q=[r,z/5,4*z/5,(t-z)/7,2*(t-z)/7,4*(t-z)/7]
     ck(sum(p)==sum(q0)==sum(q)==1)
     ck(all(v>0 or w==0 for w,v in zip(p,q)))
     ck(q[5]>0 and p[5]==0)
     ck(sum(q[1:3])==z>=ell)
     ck(q[1]/q[2]==q0[1]/q0[2] and q[3]/q[5]==q0[3]/q0[5])
     d=math.lcm(*(w.denominator for w in p))
     # Discard only the common vacuum term, including its zero/zero boundary.
     ratio=math.prod(((old/new)**int(d*w) for w,old,new in zip(p[1:],q0[1:],q[1:])),start=Q(1))
     ck(ratio==(b/z)**int(d*a)*((t-b)/(t-z))**int(d*(t-a)))
     for iz in range(il,it):
      v=Q(iz,den); candidate_count+=1
      qv=[r,v/5,4*v/5,(t-v)/7,2*(t-v)/7,4*(t-v)/7]
      ck(likelihood(p,q)>=likelihood(p,qv))
      derivative=-a/v+(t-a)/(t-v)
      ck(derivative==t*(v-a)/(v*(t-v)))
      ck((derivative>0)==(v>a))
      ck((derivative<0)==(v<a))
      if t!=1 and v!=a:
       ck(derivative!=(v-a)/(v*(t-v))); derivative_mismatch+=1
     ck(time.perf_counter()-start<45)

# Actual Boolean root and both physical children, reconstructed from values.
g=[-1 if x in (0,7) else 1 for x in range(8)]
ck(walsh(g)==[Q(1,4),0,0,Q(1,4),0,Q(1,4),Q(1,4),0])
prices=[]
for branch in (0,1):
 ck(walsh([g[2*x+branch] for x in range(4)])==[Q(1,4)]*4)
 for old,expect in [([Q(1,4)]*4,Q(27,25)),([Q(1,4),Q(5,16),Q(5,16),Q(1,8)],Q(27,32))]:
  new=[Q(1,4),Q(5,24),Q(5,24),Q(1,3)]
  ck(math.prod((x/y for x,y in zip(old,new)),start=Q(1))==expect)
  prices.append(str(expect))
ck(Q(27,32)<1<Q(27,25))

# Boundary necessities and precise display error at t=3/4,a=1/4,z=1/3.
correct=-Q(1,4)/Q(1,3)+Q(1,2)/Q(5,12)
printed=Q(1,12)/(Q(1,3)*Q(5,12))
ck(correct==Q(9,20) and printed==Q(3,5) and correct!=printed)
# If a=0, minimizer is ell; if a=t, only a boundary infimum at t exists.
ck(Q(3,4)/(Q(3,4)-Q(1,3))>0)
ck(-Q(3,4)/Q(1,3)<0)
# Reference ghost discarded: normalization changes, and so does the bill.
ck(sum([Q(1,4),Q(1,4),Q(1,4),Q(1,8)])!=1)

# Entire signed transaction, unequal actual reaches, zero weights, old charges.
# This is rational accounting for arbitrary supplied signed CE changes, not a
# representation of arbitrary rational numbers as logarithmic conversion costs.
ledger_cases=0
for B in (Q(3),Q(9)):
 for C in (Q(1),Q(2)):
  for U in (Q(0),Q(1)):
   if C+U>B: continue
   M=B-C-U
   for d0 in (Q(-1),Q(0),Q(1),Q(3)):
    for d1 in (Q(-2),Q(0),Q(2)):
     for beta in (Q(0),Q(3,8),Q(1)):
      D=Q(1,4)*beta*d0+Q(3,4)*d1
      newC=C+D; remaining=M-D; ledger_cases+=1
      ck(B-newC-U==remaining)
      ck((newC+U<=B)==(D<=M))
      ck(newC+U+remaining==B)
      ck(D<=Q(1,4)*beta*max(d0,0)+Q(3,4)*max(d1,0))
      # Two consecutive changes telescope; a release counted twice fails.
      e=Q(1,7)
      ck(M-D-e==B-(C+D+e)-U)
      if D<0: ck(newC+U+(remaining-D)>B)
save('CHECK_RESULT.json',{'status':'PASS','parameter_cases':cases,'candidate_comparisons':candidate_count,'missing_factor_witnesses':derivative_mismatch,'ledger_cases':ledger_cases,'exact_assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'Fraction and integer powers; exact Walsh characters; no floating signs','correct_derivative_times_ln2':str(correct),'printed_derivative_times_ln2':str(printed),'boolean_log_arguments':prices})
print((O/'CHECK_RESULT.json').read_text(encoding='utf-8'))

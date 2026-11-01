"""A043 actual-charge collar v1; Fraction certificates, no subprocesses."""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
from math import isqrt
import hashlib,json,time
R=Path(__file__).resolve().parents[1]; O=R/'out'; O.mkdir(exist_ok=True)
spec={'helper':'A043-actual-charge-collar-v1','family':'actual reflected Boolean prime56067',
 'domain':'24 collar fixtures: alpha,q in {1/64,1/16}; e in {1/256,1/64,1/16}; d/e in {1/256,1/16}; their 24 swapped laws; three t,t^2,t^4,t paths t=1/16,1/64,1/1024; one fair negative control',
 'case_count':52,'symmetry':'24 swapped fixtures checked directly, not silently reduced',
 'arithmetic':'Fraction vertex sums and exact outward 20-term atanh logarithm intervals after power-of-two reduction; rational square-root upper bounds',
 'memory_estimate_mb':40,'max_runtime_seconds':55,'automatic_dimension_escalation':False}
(O/'frozen_spec.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 if not b: raise AssertionError(checks)
def prod(xs):
 r=Q(1)
 for x in xs:r*=x
 return r
def basiclog(x):
 z=(x-1)/(x+1);ck(0<=z<=Q(1,3))
 lo=sum((Q(2,2*j+1)*z**(2*j+1) for j in range(20)),Q(0))
 return lo,lo+2*z**41/(41*(1-z*z))
L2=basiclog(Q(2))
def ln(x):
 ck(x>0)
 if x<1:
  l,h=ln(1/x);return -h,-l
 k=0
 while x>=2:x/=2;k+=1
 l,h=basiclog(x);return l+k*L2[0],h+k*L2[1]
def h(t):
 t=abs(t)
 if t==0:return Q(0),Q(0)
 l,r=ln(1/t**2);return t*t*l,t*t*r
def AA(t):
 if t==1:return Q(1),Q(1)
 l,r=ln(1/t);return t*l/(1-t),t*r/(1-t)
def sqrtupper(x):
 D=2**40; k=isqrt((x.numerator*D*D)//x.denominator)
 if Q(k*k,D*D)<x:k+=1
 ck(Q(k*k,D*D)>=x)
 return Q(k,D)
values=[]
for i in range(16):
 a,x,y,z=[(i>>j)&1 for j in range(4)]
 values.append(-1+2*z+2*x*y-2*z*(a*x+(1-a)*y))
ck(set(values)=={-1,1});ck(all(values[i]==(1 if (56067>>(i^6))&1 else -1) for i in range(16)))
rows=[]
for k in (2,3):
 for B in combinations(range(4),k):
  C=[j for j in range(4) if j not in B]
  rs={tuple(values[sum(((b>>j)&1)<<B[j] for j in range(k))+sum(((c>>j)&1)<<C[j] for j in range(4-k))] for c in range(1<<(4-k))) for b in range(1<<k)}
  ck(len(rs)>2);rows.append({'block':B,'cofactor_rows':len(rs)})
def fixture(p,kind):
 ck(time.perf_counter()-start<55)
 a,e,d,q=p; v=[4*t*(1-t) for t in p]
 wt=[prod(p[j] if b>>j&1 else 1-p[j] for j in range(4)) for b in range(16)]
 c=[];P=[]
 for s in range(16):
  moment=sum((wt[b]*values[b]*prod(Q((b>>j)&1)-p[j] for j in range(4) if s>>j&1) for b in range(16)),Q(0))
  den=prod(p[j]*(1-p[j]) for j in range(4) if s>>j&1)
  c.append(moment/(2**s.bit_count()*den));P.append(moment*moment/den)
 ck(sum(P)==1)
 expected={1:q*(d-e),2:d-q*a,4:e-q*(1-a),8:1-a*e-(1-a)*d,
  3:-q/2,5:q/2,9:(d-e)/2,6:Q(1,2),10:-a/2,12:-(1-a)/2,
  7:Q(0),11:Q(-1,4),13:Q(1,4),14:Q(0),15:Q(0)}
 for s in range(1,16):ck(c[s]==expected[s]);ck(P[s]==c[s]*c[s]*prod(v[j] for j in range(4) if s>>j&1))
 Delta=sum(((s.bit_count()-1)*P[s] for s in range(1,16)),Q(0))
 Tx=v[0]*v[1]*v[3]/16;Ty=v[0]*v[2]*v[3]/16;T=Tx+Ty
 ck(T>0);ck(P[11]==Tx and P[13]==Ty)
 E1=[Q(0),Q(0)];Ehi=[Q(0),Q(0)]
 for s in range(1,16):
  l,r=h(c[s]);m=prod(v[j] for j in range(4) if s>>j&1)
  dest=E1 if s.bit_count()==1 else Ehi
  dest[0]+=m*l;dest[1]+=m*r
 Slo=4*Delta-2*T-E1[1];Shi=4*Delta-2*T-E1[0];ck(Slo>=0)
 gl=gh=Q(0)
 for mult,ar in ((2*T,AA(q)),(2*Tx,AA(a)),(2*Ty,AA(1-a)),(v[0]*v[3]/4,h(d-e))):
  gl+=mult*ar[0];gh+=mult*ar[1]
 directlo=Ehi[0]-2*L2[1]*Delta;directhi=Ehi[1]-2*L2[0]*Delta
 ck(max(gl,directlo)<=min(gh,directhi))
 residuallo=(4+2*L2[0])*Delta-E1[1]-Ehi[1]
 if kind!='fair-control':
  aa,ee,dd,qq=(a,e,d,q) if kind!='swapped' else (1-a,d,e,q)
  ck(0<aa<=Q(1,16) and 0<ee<=Q(1,16) and 0<qq<=Q(1,16) and 0<dd<=ee/16)
  K=2*sqrtupper(qq)+2*sqrtupper(aa)+2*dd/(ee*(1-ee))+2*sqrtupper(ee)/(1-ee)
  ck(K<=Q(5,3));ck(gh<=K*T);ck(directhi<=Q(5,3)*T);ck(residuallo>=T/3)
 else:
  ck(gl>2*T);ck(residuallo>0)
 return {'kind':kind,'p':list(map(str,p)),'G_over_T_interval':[str(gl/T),str(gh/T)],'sharp_residual_lower_over_T':str(residuallo/T)}
results=[]
for a,q,e,r in product((Q(1,64),Q(1,16)),(Q(1,64),Q(1,16)),(Q(1,256),Q(1,64),Q(1,16)),(Q(1,256),Q(1,16))):
 d=e*r;results.append(fixture((a,e,d,q),'collar'));results.append(fixture((1-a,d,e,q),'swapped'))
for t in (Q(1,16),Q(1,64),Q(1,1024)):results.append(fixture((t,t*t,t**4,t),'thin-path'))
results.append(fixture((Q(1,2),)*4,'fair-control'))
ck(len(results)==spec['case_count']);ck(time.perf_counter()-start<55)
output={'status':'PASS','case_count':len(results),'assertions':checks,'runtime_seconds':time.perf_counter()-start,'prime_rows':rows,'fixtures':results,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'scope':'finite exact coefficient/interval certificates; continuum proof in PROOF.md, independent review pending'}
(O/'checks.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:output[k] for k in ('status','case_count','assertions','runtime_seconds')}))

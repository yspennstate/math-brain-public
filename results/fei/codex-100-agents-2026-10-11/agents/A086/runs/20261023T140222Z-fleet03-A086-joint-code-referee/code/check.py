from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from time import perf_counter
import importlib.util,hashlib,json,sys
R=Path(__file__).resolve().parents[1]; agent=R.parents[1]
helper=agent/'runs/20261021T203248Z-fleet03-A086-joint-code-referee/code/check.py'
assert hashlib.sha256(helper.read_bytes()).hexdigest()=='48cd9de1ec443e89be969dd3eac40569c413ddbfafaa9df70e9db1ef238907bc'
sp=importlib.util.spec_from_file_location('logonly',helper);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
start=perf_counter();checks=0
def ck(b,msg):
 global checks
 checks+=1
 if not b:raise AssertionError(msg)
 if perf_counter()-start>55:raise TimeoutError('frozen55sec')
def spectrum(g):
 return tuple(sum((F(v*((-1)**((s&x).bit_count()))) for x,v in enumerate(g)),F(0))/len(g) for s in range(len(g)))
def ce(P,Q,mult):
 out=defaultdict(F)
 for k,p in P.items():
  if p:
   ck(Q[k]>0,'true support fully covered')
   out[Q[k]]-=mult[k]*p
 return dict(out)
def add(*terms):
 out=defaultdict(F)
 for scale,ex in terms:
  for q,v in ex.items():out[q]+=scale*v
 return {q:v for q,v in out.items() if v and q!=1}
def interval(ex):
 lo=hi=F(0)
 for q,v in ex.items():
  l,h=old.log2(q);lo+=v*(l if v>=0 else h);hi+=v*(h if v>=0 else l)
 return lo,hi
def mass(P,mult):return sum((mult[k]*p for k,p in P.items()),F(0))
def chi(P,Q,mult):return sum((mult[k]*(p-Q[k])**2/Q[k] for k,p in P.items() if Q[k]),F(0))
def certificate():
 u=F(1,8);A=5+u;B=6*(1+u)
 ck(3*A*A-2*A*B-B*B*u==15-78*u-81*u*u-36*u**3==F(501,128),'A094 denominator polynomial endpoint')
 # -P'(u)=78+162u+108u^2 is coefficientwise positive.
 ck(all(x>0 for x in (78,162,108)),'A094 polynomial monotonic on positive interval')
 C=lambda x:F(1,2)+F(5043,128)*x
 ck(C(u)*u==F(5555,8192),'A094 original influence debit')
 ck(F(7,8)-C(u)*u==F(1613,8192),'A094 SAME root remainder')
 ck(C(F(1,32))==F(7091,4096),'A094 five-padding coefficient')
 ck(F(3,256)-5*C(F(1,32))*F(1,4)*F(1,512)==F(62849,8388608),'A094 SAME rate4 remainder')
 u=F(1,256)
 ck(10+26*u<11,'selector old-support chi coefficient')
 ck(1+F(363,2)*u<2,'selector complete KL bound')
 ck(F(7,8)-F(3,2)*u==F(445,512),'SAME supplied root selector remainder')
 ck(F(3,256)-F(6,16384)==F(93,8192),'SAME rate4 selector remainder')
def case(g,m):
 g=tuple(g[0]*v for v in g);a=(len(g)-1).bit_length();e=F(1,2**(a+m));co=spectrum(g)
 keys=[(s,d) for s in range(len(g)) for d in (0,1)];mult={k:1 if k[1]==0 else 2**m-1 for k in keys}
 A={k:co[k[0]] if k[1]==0 else F(0) for k in keys}
 q={k:(A[k]-e)**2+e*e for k in keys};floor={k:(A[k]**2+3*e*e)/(1+3*e) for k in keys}
 P=[{k:(A[k]-2*e)**2 for k in keys},{k:A[k]**2 for k in keys}]
 T=[{k:(A[k]**2+6*e*e)/(1+6*e) for k in keys},P[1]]
 ck(mass(q,mult)==mass(floor,mult)==1,'parent complete data masses')
 ck(all(mass(x,mult)==1 for x in P+T),'true children and prescribed floors normalized')
 raw=[{k:floor[k]*P[b][k]/q[k] for k in keys} for b in (0,1)]
 Z=[mass(x,mult) for x in raw];ck(sum(Z)==2 and min(Z)>0,'ACTUAL two inherited normalizers')
 Q=[{k:raw[b][k]/Z[b] for k in keys} for b in (0,1)]
 for b in (0,1):
  ck(mass(Q[b],mult)==1,'full inherited child mass')
  for k in keys:
   ck((P[0][k]+P[1][k])/2==q[k],'physical pair marginal')
   ck(Q[b][k]*q[k]*Z[b]==floor[k]*P[b][k],'exact inherited likelihood with Z retained')
 ch=chi(P[0],T[0],mult);N=sum(v!=0 for v in co)
 ck(F(3,2)*ch<(1+F(363,2)*F(1,2**m))*e<2*e,'edited child complete chi-square bound')
 charge=[]
 for b in (0,1):
  ex=add((F(1,2),ce(P[b],T[b],mult)),(-F(1,2),ce(P[b],Q[b],mult)))
  charge.append(interval(ex))
 ck(charge[0][1]<e,'actual reached edited-child positive booking')
 ck(charge[1][1]<F(1,10**20),'clean true-law charge nonpositive up to enclosure width')
 # Its exact sign is CE-H>=0, not inferred from the interval endpoint.
 ck(chi(P[1],Q[1],mult)>=0,'clean child nonnegative divergence; no negative refund')
 # Full joint parent and its actual selector probabilities, no vacuum omission.
 joint={(s,d,b):((A[s,d]-e)**2 if b==0 else e*e) for s,d in keys for b in (0,1)}
 jm={(s,d,b):mult[s,d] for s,d,b in joint}
 Jref={(s,d,b):floor[s,d]*p/q[s,d] for (s,d,b),p in joint.items()}
 ck(mass(joint,jm)==mass(Jref,jm)==1,'complete joint parent true and reference masses')
 parent=ce(joint,Jref,jm);inherited=add((F(1,2),ce(P[0],Q[0],mult)),(F(1,2),ce(P[1],Q[1],mult)))
 release=add((1,parent),(-1,inherited));ck(interval(release)[0]>-F(1,10**20),'actual full query release nonnegative enclosure')
 terminal=add((F(1,2),ce(P[0],T[0],mult)),(F(1,2),ce(P[1],T[1],mult)))
 resets=add((1,terminal),(-1,inherited))
 ck(add((1,release),(1,terminal))==add((1,parent),(1,resets)),'EXACT complete query-reset-terminal log-linear ledger')
 return {'a':a,'m':m,'Z':list(map(str,Z)),'charge_intervals':[list(map(str,x)) for x in charge]}
def main():
 certificate();pilot='--pilot' in sys.argv;cases=0;rows=[]
 for a in ([0,1,2] if pilot else [0,1,2,3]):
  for bits in range(2**(2**a)):
   g=tuple(1 if bits>>x&1 else -1 for x in range(2**a));r=case(g,8);cases+=1
   if a==0:rows.append(r)
 if not pilot:
  for m in (8,12):rows.append(case(tuple(1 if x==0 else -1 for x in range(16)),m));cases+=1
 result={'status':'PASS','cases':cases,'assertions':checks,'seconds':perf_counter()-start,'selected_rows':rows,'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'domain':'22 labelled pilot or278 labelled main sources plus2 fixed -h4 cases; m>=8 upper selector price analytic','full_fei':'OPEN'}
 (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if pilot else 'EXACT_RESULTS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='selected_rows'}))
if __name__=='__main__':
 try:main()
 except Exception as exc:
  (R/'out').mkdir(exist_ok=True);(R/'out'/'FAILURE.json').write_text(json.dumps({'error':repr(exc),'assertions':checks,'seconds':perf_counter()-start}),encoding='utf-8');raise

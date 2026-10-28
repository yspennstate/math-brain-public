"""A043 singleton import v1: exact rational composition and fixed tower certificates."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'out';O.mkdir(exist_ok=True)
spec={'helper':'A043-singleton-import-v1','family':'actual disjoint Boolean compositions; fair ternary-majority tower',
 'domain':'288 binary compositions (16 outer masks,9 AND/OR/XOR child pairs,2 bias vectors);32 binary compositions with Maj3/literal children;256 ternary outer masks with AND2/literal/literal children;two sharp outer-import controls;AND3 source control;direct majority tower depths1,2;compressed exact tower moments at predeclared depths1,2,3,4,8,12',
 'composition_case_count':580,'direct_tower_profile_depths':[1,2],'compressed_depths':[1,2,3,4,8,12],
 'symmetry':'none','arithmetic':'Fraction spectra, exact dyadic scales and integer carries; entropy charges divided by ln4, no floating-point/logarithm signs',
 'memory_estimate_mb':45,'max_runtime_seconds':55,'automatic_dimension_escalation':False,'largest_enumerated_physical_dimension':9,
 'compressed_certificate_scope':'Fixed symbolic majority family; no truth tables beyond n=9 and no searching/increasing dimension.'}
(O/'frozen_spec.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0;profiles=0
def ck(b):
 global checks
 checks+=1
 if not b:raise AssertionError(checks)
def prod(xs):
 a=Q(1)
 for x in xs:a*=x
 return a
def signs(n,mask):return [Q(1) if mask>>i&1 else Q(-1) for i in range(1<<n)]
def profile(values,p):
 global profiles
 profiles+=1;ck(time.perf_counter()-start<55)
 n=len(p);v=[4*x*(1-x) for x in p];m=list(values)
 ck(set(values)<={Q(-1),Q(1)})
 for j in range(n):
  b=1<<j
  for x in range(1<<n):
   if x&b:continue
   a,c=m[x],m[x|b];m[x]=(1-p[j])*a+p[j]*c;m[x|b]=p[j]*(1-p[j])*(c-a)
 c=[];P=[];J=[]
 for s in range(1<<n):
  den=prod(p[j]*(1-p[j]) for j in range(n) if s>>j&1)
  c.append(m[s]/(2**s.bit_count()*den));P.append(m[s]*m[s]/den)
  t=abs(c[-1]);k=0
  if s and t:
   ck(t<=1)
   while t<=Q(1,2):t*=2;k+=1
   ck(Q(1,2)<t<=1);ck(2*abs(c[-1])*k<=1)
  J.append(k)
 ck(sum(P)==1)
 Is=[]
 for j in range(n):
  d=mean=Q(0)
  for x in range(1<<n):
   if x>>j&1:continue
   wt=prod(p[k] if x>>k&1 else 1-p[k] for k in range(n) if k!=j)
   z=(values[x|(1<<j)]-values[x])/2;mean+=wt*z;d+=wt*z*z
  influence=sum((P[s] for s in range(1,1<<n) if s>>j&1),Q(0));Is.append(influence)
  ck(mean==c[1<<j]);ck(d>=abs(mean));ck(influence==v[j]*d);ck(2*P[1<<j]*J[1<<j]<=influence)
 w=1-P[0];I=sum(Is);D=I-w;R=sum(((s.bit_count()-2)*P[s] for s in range(1,1<<n) if s.bit_count()>=3),Q(0))
 M=sum((P[s] for s in range(1,1<<n) if s.bit_count()>=2),Q(0));ck(M==D-R)
 J1=sum((P[1<<j]*J[1<<j] for j in range(n)),Q(0));Jh=sum((P[s]*J[s] for s in range(1,1<<n) if s.bit_count()>=2),Q(0));ck(2*J1<=I)
 return {'P':P,'c':c,'J':J,'J1':J1,'Jh':Jh,'w':w,'I':I,'Is':Is,'D':D,'R':R,'M':M,'mean':c[0]}
def compose(mask,blocks,p):
 sizes=[(len(b)-1).bit_length() for b in blocks];ck(sum(sizes)==len(p));m=len(blocks)
 children=[];off=0
 for b,k in zip(blocks,sizes):children.append(profile(b,p[off:off+k]));off+=k
 gp=tuple((1+x['mean'])/2 for x in children);g=profile(signs(m,mask),gp)
 vals=[]
 for x in range(1<<len(p)):
  off=0;z=0
  for i,(b,k) in enumerate(zip(blocks,sizes)):
   z|=int(b[(x>>off)&((1<<k)-1)]==1)<<i;off+=k
  vals.append(Q(1) if mask>>z&1 else Q(-1))
 F=profile(vals,p);a=[g['Is'][i]/ch['w'] for i,ch in enumerate(children)];b=[(g['Is'][i]-g['P'][1<<i])/ch['w'] for i,ch in enumerate(children)]
 Tout=sum((g['P'][1<<i]*ch['M']*g['J'][1<<i]/ch['w'] for i,ch in enumerate(children)),Q(0))
 Tin=sum((b[i]*ch['J1'] for i,ch in enumerate(children)),Q(0));T=Tout+Tin;carry=Q(0);allcarry=Q(0)
 for s in range(1,1<<len(p)):
  if not F['P'][s]:continue
  off=0;A=0;C=Q(1);Pf=Q(1);jchild=0
  for i,(ch,k) in enumerate(zip(children,sizes)):
   t=(s>>off)&((1<<k)-1);off+=k
   if t:
    A|=1<<i;C*=ch['c'][t];Pf*=ch['P'][t]/ch['w'];jchild+=ch['J'][t]
  ck(F['c'][s]==g['c'][A]*C);ck(F['P'][s]==g['P'][A]*Pf)
  kap=F['J'][s]-g['J'][A]-jchild;ck(kap>=0);allcarry+=F['P'][s]*kap
  if s.bit_count()>=2:carry+=F['P'][s]*kap
 inherited=g['Jh']+sum((a[i]*ch['Jh'] for i,ch in enumerate(children)),Q(0))
 ck(F['Jh']==inherited+carry+T);ck(F['D']==g['D']+sum((a[i]*ch['D'] for i,ch in enumerate(children)),Q(0)))
 refund=g['R']+sum(((a[i]-b[i])*ch['D']+a[i]*ch['R'] for i,ch in enumerate(children)),Q(0))
 ck(T>=0);ck(Tout<=sum((a[i]*ch['M']/2 for i,ch in enumerate(children)),Q(0)))
 ck(Tin<=(2*g['D']-g['R']+sum((b[i]*ch['D'] for i,ch in enumerate(children)),Q(0)))/2)
 ck(T<=F['D']-refund/2<=F['D'])
 return {'T':T,'Tout':Tout,'Tin':Tin,'carry':carry,'allcarry':allcarry,'F':F,'inherited':inherited,'outer_bound':sum((a[i]*ch['M']/2 for i,ch in enumerate(children)),Q(0))}
maj=signs(3,232);and2=signs(2,8);or2=signs(2,14);xor2=signs(2,6);lit=signs(1,2)
count=0
for mask,first,second,p in product(range(16),(and2,or2,xor2),(and2,or2,xor2),((Q(1,2),)*4,tuple(map(Q,('1/4','2/3','3/5','3/4'))))):compose(mask,[first,second],p);count+=1
for mask,p in product(range(16),((Q(1,2),)*4,tuple(map(Q,('1/4','2/3','3/5','3/4'))))):compose(mask,[maj,lit],p);count+=1
for mask in range(256):compose(mask,[and2,lit,lit],tuple(map(Q,('1/4','2/3','3/5','3/4'))));count+=1
sharp=[]
for otherp in (Q(1,2),Q(1,4)):
 z=compose(8,[xor2,lit],(Q(1,2),Q(1,2),otherp));count+=1
 ck(z['Tout']==z['outer_bound']>0);ck(z['F']['Jh']!=z['inherited']+z['carry'])
 sharp.append({'other_input_probability':str(otherp),'Tout_over_ln4':str(z['Tout']),'bound_equality':True})
source=compose(8,[and2,lit],(Q(1,2),)*3);count+=1
ck(source['T']==Q(3,16));ck(source['F']['Jh']==Q(1,2));ck(source['inherited']==Q(5,16));ck(source['allcarry']==0)
tower2=compose(232,[maj,maj,maj],(Q(1,2),)*9);count+=1
ck(tower2['T']==Q(3,4));ck(tower2['allcarry']==0)
tower1=profile(maj,(Q(1,2),)*3);ck(tower1['D']==Q(1,2));ck(tower1['Jh']==Q(1,4))
rows=[];acc=Q(0)
for depth in range(1,13):
 D=Q(3,2)**depth-1;J1=depth*Q(3,4)**depth;local=Q(3,4)+(depth-2)*Q(3,4)**depth
 acc=Q(3,2)*acc+local;closed=Q(3,2)*D-J1
 ck(acc==closed);ck(local>=0);ck(2*D-J1-Q(1,2)*D==acc)
 if depth in spec['compressed_depths']:rows.append({'depth':depth,'physical_leaves':3**depth,'Delta':str(D),'singleton_J_over_ln4':str(J1),'total_import_over_ln4':str(acc),'gap_from_ln4Delta_over_ln4':str(acc-D)})
 if depth==4:ck(acc-D==Q(49,64))
# An excluded real-valued fair literal has t=1/2,d=1/4,j=1, violating exactly the Boolean supplier inequality.
ck(Q(1,2)**2*1>Q(1,4)/2)
ck(count==spec['composition_case_count']);ck(time.perf_counter()-start<55)
out={'status':'PASS','composition_cases':count,'profiles_reconstructed':profiles,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'sharp_outer_import_controls':sharp,'A041_AND3_control':{'T_over_ln4':str(source['T']),'allcarry':str(source['allcarry'])},'tower_certificates':rows,'excluded_real_literal_supplier_failure':True,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite validations; universal boundary bound and all-depth tower proof in PROOF.md. No logarithmic numerical sign or full FEI closure.'}
(O/'checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','composition_cases','profiles_reconstructed','assertions','runtime_seconds')}))

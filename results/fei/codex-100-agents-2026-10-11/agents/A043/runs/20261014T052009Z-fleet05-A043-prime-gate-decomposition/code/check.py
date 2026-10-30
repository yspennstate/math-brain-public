from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,itertools,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
def prod(xs):
 r=Q(1)
 for x in xs:r*=x
 return r
def series(x):
 z=(x-1)/(x+1);ck(0<=z<=Q(1,3))
 lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
 return lo,lo+2*z**49/Q(49)/(1-z*z)
L2=series(Q(2))
@lru_cache(None)
def ln(x):
 ck(x>=1);k=0
 while x>=2:x/=2;k+=1
 lo,hi=series(x)
 return lo+k*L2[0],hi+k*L2[1]
def mesh(lo,hi):
 scale=10**12
 return [str(Q((lo*scale).__floor__(),scale)),str(Q((hi*scale).__ceil__(),scale))]
def energy(c,m,sets):
 lo=hi=Q(0)
 for s in sets:
  if not m[s]:continue
  l,h=ln(1/c[s]**2);lo+=m[s]*l;hi+=m[s]*h
 return lo,hi
values=[]
for i in range(16):
 a,x,y,z=[(i>>j)&1 for j in range(4)]
 values.append(Q(-1+2*z+2*x*y-2*z*(a*x+(1-a)*y)))
ck(all(values[i]==(1 if 56067>>(i^6)&1 else -1) for i in range(16)))
rows=[]
for size in (2,3):
 for B in itertools.combinations(range(4),size):
  C=[j for j in range(4) if j not in B]
  rr={tuple(values[sum(((a>>j)&1)<<B[j] for j in range(size))+sum(((z>>j)&1)<<C[j] for j in range(len(C)))] for z in range(1<<len(C))) for a in range(1<<size)}
  ck(len(rr)>2);rows.append({'block':[i+1 for i in B],'rows':len(rr)})

def coefficients(p):
 a,e,d,q=p
 c=[Q(0)]*16
 c[0]=-1+2*q+2*e*d-2*q*(a*e+(1-a)*d)
 c[1]=q*(d-e);c[2]=d-q*a;c[4]=e-q*(1-a);c[8]=1-a*e-(1-a)*d
 c[3]=-q/2;c[5]=q/2;c[9]=(d-e)/2;c[6]=Q(1,2);c[10]=-a/2;c[12]=-(1-a)/2
 c[11]=Q(-1,4);c[13]=Q(1,4)
 return c
def fixture(p):
 a,e,d,q=p;v=[4*t*(1-t) for t in p];u,vx,vy,w=v
 c=coefficients(p);mom=values.copy()
 for j in range(4):
  b=1<<j
  for x in range(16):
   if x&b:continue
   A,B=mom[x],mom[x|b]
   mom[x]=(1-p[j])*A+p[j]*B
   mom[x|b]=p[j]*(1-p[j])*(B-A)
 m=[]
 for s in range(16):
  denom=prod(p[j]*(1-p[j]) for j in range(4) if s>>j&1)
  actual=mom[s]/(2**s.bit_count()*denom)
  ck(actual==c[s]);ck(abs(actual)<=1)
  direct=mom[s]**2/denom
  ck(direct==prod(v[j] for j in range(4) if s>>j&1)*c[s]**2);m.append(direct)
 ck(sum(m)==1)
 D=sum(((s.bit_count()-1)*m[s] for s in range(1,16)),Q(0))
 Tx=u*vx*w/16;Ty=u*vy*w/16;T=Tx+Ty
 ck(m[11]==Tx and m[13]==Ty and m[15]==0)
 ck(D==sum(m[s] for s in (3,5,6,9,10,12))+2*T)
 Le=4*a*q*(2-a-q);Ld=4*(1-a)*q*(1+a-q)
 ck(D==Le*e*(1-e)+Ld*d*(1-d)+(u*w/4)*(d-e)**2+4*e*d*(1-e)*(1-d))
 E=energy(c,m,range(1,16));ES=energy(c,m,(1,2,4,8));EH=energy(c,m,(3,5,6,9,10,12,11,13))
 # Direct signed derivatives independently verify source reserve and local slack.
 reserve=Q(0);poly=Q(0)
 for j in range(4):
  mean=second=pos=neg=Q(0)
  for x in range(16):
   if x>>j&1:continue
   weight=prod(p[k] if x>>k&1 else 1-p[k] for k in range(4) if k!=j)
   diff=(values[x|(1<<j)]-values[x])/2
   mean+=weight*diff;second+=weight*diff*diff
   if diff==1:pos+=weight
   if diff==-1:neg+=weight
  ck(mean==c[1<<j]);ck(second-abs(mean)==2*min(pos,neg))
  reserve+=2*v[j]*(second-mean*mean)
  t=abs(mean);poly+=v[j]*(2*(second-t)+t*(1-t)**2)
 ck(reserve==4*D-2*T);ck(ES[1]<=reserve)
 for s,t,packet in ((3,q,Tx),(5,q,Ty),(10,a,Tx),(12,1-a,Ty)):
  ck(m[s]==packet*t/(1-t))
  lo,hi=ln(1/t)
  ck(2*m[s]*hi<=2*packet)
 diff=abs(d-e)
 if diff:
  lo,hi=ln(1/diff**2)
  ck(m[9]*hi<=2*T)
 ck(e*(1-e)+d*(1-d)>=diff*(1-diff))
 ck(EH[1]<=2*L2[0]*D+6*T)
 ck(E[1]<=(6+2*L2[0])*D)
 # Source tangent algebra is exact in formal basis 1,ln2,lnq,lnalpha.
 ck(Q(2)*w*a/Le==2*(1-q)/(2-a-q))
 ck((2*u*q*q+2*w*a*a+u*w)/Le==2)
 ck((-8*q*q*a*a-2*u*q*q)/Le==-2*q/(2-a-q))
 ck((-8*q*q*a*a-2*w*a*a)/Le==-2*a/(2-a-q))
 smin=reserve-ES[1]-4*T;smax=reserve-ES[0]-4*T
 sharpmin=(4+2*L2[0])*D-E[1];sharpmax=(4+2*L2[1])*D-E[0]
 status=lambda lo,hi:'PASS_CERTIFIED' if lo>=0 else 'FAIL_CERTIFIED' if hi<0 else 'UNRESOLVED_INTERVAL'
 return {'p':[str(t) for t in p],'D':str(D),'T':str(T),'ratio_interval':mesh(E[0]/D/L2[1],E[1]/D/L2[0]),
         'S_ge4T':status(smin,smax),'sharp_Cstar':status(sharpmin,sharpmax),
         'poly_minus4T_overD':str((poly-4*T)/D),'poly_slack_lower_bound':str(poly),
         'S_minus4T_overD_interval':mesh(smin/D,smax/D)}

grid=[Q(1,16),Q(1,4),Q(1,2),Q(3,4),Q(15,16)]
records=[]
for p in itertools.product(grid,repeat=4):records.append(fixture(p))
paths=[]
for k in range(2,11):
 t=Q(1,2**k);r=fixture([1-t*t,t**6,t**8,1-t]);r['k']=k;paths.append(r);records.append(r)
for a,q in ((Q(1,4),Q(1,2)),(Q(1,2),Q(1,2)),(Q(3,4),Q(3,4))):
 for t in (Q(1,16),Q(1,256)):
  for e,d in ((t,t),(t,t*t),(t*t,t)):records.append(fixture([a,e,d,q]))
slices=[]
for k in range(2,11):
 e=Q(1,2**k);r=fixture([Q(1,2),e,e,Q(1,2)])
 D=Q(r['D']);rr=1-e
 ck(D==2*rr*e*(1+2*rr*e))
 loss=rr*rr/2;ck(loss/D>=1/(8*e))
 r['loss_overD']=str(loss/D);r['k']=k;slices.append(r);records.append(r)
ck(len(records)==661)
poly_witness=min(records,key=lambda r:Q(r['poly_minus4T_overD']))
counts={key:{s:sum(r[key]==s for r in records) for s in ('PASS_CERTIFIED','FAIL_CERTIFIED','UNRESOLVED_INTERVAL')} for key in ('S_ge4T','sharp_Cstar')}
out={'helper':'A043-coherent-quadratic-payment-v1','cases':len(records),'assertions':checks,
     'all_main_checks_passed':True,'runtime_seconds':time.perf_counter()-start,'prime_block_rows':rows,
     'upper_constant_bit_interval':mesh(2+6/L2[1],2+6/L2[0]),'log_terms':24,
     'exploratory_only_counts':counts,'minimum_polynomial_slack_witness':poly_witness,
     'joint_paths':paths,'symmetric_loss_slices':slices,
     'finite_scope':'All661 cases check the proved global upper bound. Sharper slack/sharp-Cstar probes are finite evidence only; polynomial witness cannot refute actual log slack.',
     'records':records}
(ROOT/'out/checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('prime_block_rows','records','joint_paths','symmetric_loss_slices','minimum_polynomial_slack_witness')}))
print('polynomial probe:',poly_witness)

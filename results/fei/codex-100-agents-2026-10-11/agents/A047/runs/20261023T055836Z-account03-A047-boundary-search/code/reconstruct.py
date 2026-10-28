from fractions import Fraction as F
from pathlib import Path
import json,time,math,sys
R=Path(__file__).resolve().parents[1];T0=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-T0>55:raise TimeoutError('frozen55s')
def spectrum(t):
 n=len(t)
 # Dense direct character sums; no Walsh butterfly or imported search helper.
 h=[F(sum(v*(-1 if (s&z).bit_count()%2 else 1) for z,v in enumerate(t)),n) for s in range(n)]
 p={s:a*a for s,a in enumerate(h) if a};ck(sum(p.values())==1)
 return p
def child(t,j,b):
 return tuple(v for z,v in enumerate(t) if (z>>j)&1==b)
def erase(p,j):
 d={}
 for s,v in p.items():
  k=(s% (1<<j))+((s>>(j+1))<<j);d[k]=d.get(k,F(0))+v
 return d
def transport(t,q,j):
 p=spectrum(t);pe=erase(p,j);qe=erase(q,j);ts=[child(t,j,b) for b in [0,1]];ps=[spectrum(t) for t in ts]
 laws=[];out=[]
 for b in [0,1]:
  joint={s:v*(ps[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,v in qe.items()}
  rb=sum(joint.values());out.append(rb);laws.append({s:v/rb for s,v in joint.items() if v})
 ck(sum(out)==1);return ts,ps,laws,out
def qref(p,mask,alpha):
 if len(p)==1:return p.copy()
 q={s:(1-alpha)*v for s,v in p.items()};q[0]=p.get(0,F(0));q[mask]=q.get(mask,F(0))+alpha*(1-p.get(0,F(0)))
 return {s:v for s,v in q.items() if v}
def outer(t,q,eps,sp):
 n=len(t);k=n.bit_length()-1
 u=tuple(t[z&(n-1)]*sp[z>>k] for z in range(n*len(sp)))
 pu=spectrum(u);ps=spectrum(sp);mu=F(sum(u),len(u));qu={s|(z<<k):v*w for s,v in q.items() for z,w in ps.items()}
 actual=tuple(eps if z%2==0 else u[z>>1] for z in range(2*len(u)))
 law={0:(eps+mu)**2/4,1:(eps-mu)**2/4}
 for s,v in qu.items():
  if s:law[2*s]=v/4;law[2*s+1]=v/4
 return actual,{s:v for s,v in law.items() if v}
def multiplicative_reset(ps,old,new):
 denominator=math.lcm(*(2*v.denominator for p in ps for v in p.values()))
 prod=F(1)
 for p,o,n in zip(ps,old,new):
  ck(set(p)<=set(o) and set(p)<=set(n))
  for s,v in p.items():
   power=v*denominator/2;ck(power.denominator==1)
   prod*=(o[s]/n[s])**int(power)
 return prod,denominator

g=(1,-1,-1,1,-1,1,1,1);pg=spectrum(g);ck(pg=={s:F(9 if s==7 else 1,16) for s in range(8)})
rows=[]
for a in [F(1,16),F(1,8),F(1,6),F(1,3),F(1,2),F(3,4)]:
 q=qref(pg,7,a);ts,ps,old,out=transport(g,q,0)
 ck(out==[(2+a)/4,(2-a)/4]);ck(old[0]==ps[0])
 expected={0:F(1,4),1:(1-a)/(2*(2-a)),2:(1-a)/(2*(2-a)),3:(2+a)/(4*(2-a))};ck(old[1]==expected)
 fresh=[qref(p,3,a) for p in ps];prod,den=multiplicative_reset(ps,old,fresh)
 K=4*(2+a)/((2-a)**3*(1+2*a));ck(prod==K and den==8 and prod>1)
 ck(4*(2+a)-(2-a)**3*(1+2*a)==a*a*(18-11*a+2*a*a))
 rows.append({'kind':'core','alpha':str(a),'log_ratio':str(prod),'log_denominator':den,'support_matching':set(q)==set(pg) and all(set(p)==set(n)==set(o) for p,n,o in zip(ps,fresh,old))})
 for eps in [-1,1]:
  tt,qq=outer(g,q,eps,(1,));_,pp,oo,rr=transport(tt,qq,1)
  nn=[outer(z,qref(spectrum(z),3,a),eps,(1,))[1] for z in ts]
  z=14*a/65;ck(rr==[(1+z)/2,(1-z)/2])
  A=1-a/26;B=1-a/10;C=1+a/2;D=1+2*a
  expected=A**13*B**5*C**10/(D**2*(1-z*z)**16)
  product,power=multiplicative_reset(pp,oo,nn);ck(power==32 and product==expected)
  if a==F(1,6):ck(product>1)
  rows.append({'kind':'activation','epsilon':eps,'alpha':str(a),'log_ratio':str(product),'log_denominator':power,'outcome':list(map(str,rr)),'positive':product>1})
 # Character spectator is checked separately at the frozen requested alpha.
 if a==F(1,6):
  for eps in [-1,1]:
   tt,qq=outer(g,q,eps,(1,-1));_,pp,oo,rr=transport(tt,qq,1)
   nn=[outer(z,qref(spectrum(z),3,a),eps,(1,-1))[1] for z in ts]
   product,power=multiplicative_reset(pp,oo,nn);ck(product>1)
   rows.append({'kind':'character_activation','epsilon':eps,'alpha':str(a),'log_ratio':str(product),'log_denominator':power,'outcome':list(map(str,rr)),'positive':True})
result={'status':'PASS','cases':len(rows),'assertions':checks,'runtime_seconds':time.perf_counter()-T0,'arithmetic':'direct dense integer character sums; Fraction normalization; rational-power integer comparisons, no logarithm evaluations','rows':rows}
(R/'out/RECONSTRUCTION.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

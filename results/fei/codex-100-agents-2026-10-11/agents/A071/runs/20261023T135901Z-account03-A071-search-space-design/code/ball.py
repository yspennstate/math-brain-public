"""Frozen prime-ball exact pilot and binomial spectral certificate."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time,sys
from profile_engine import add,mul,lp,pack,ev,cmp,Q
R=Path(__file__).resolve().parents[1]
START=time.perf_counter(); CHECKS=0
def ck(v):
 global CHECKS
 assert v;CHECKS+=1
 assert time.perf_counter()-START<55
def save(name,obj):
 (R/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def eta(p):return mul(lp(p),-p) if p else {}
def spectrum(n):
 N=1<<n;mu=1-F(2*(n+1),N);H=mul(lp(abs(mu)),-2*mu*mu) if mu else {};rows=[];mass=mu*mu;I=F(0)
 for k in range(1,n+1):
  a=-2*(n+1-2*k);p=F(a*a,N*N);c=comb(n,k)
  H=add(H,mul(eta(p),c));mass+=c*p;I+=k*c*p
  rows.append({'weight':k,'multiplicity':c,'Walsh_numerator':a,'mass_each':str(p)})
 ck(mass==1);ck(I==F(2*n*(n-1),N))
 return H,I,mu,rows
def pilot():
 result=[];blocks=0;coeffs=0
 for n in range(3,7):
  N=1<<n;t=[-1 if x.bit_count()<=1 else 1 for x in range(N)]
  w=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)]
  H,I,mu,rows=spectrum(n);actual={}
  for s,a in enumerate(w):
   ck(a==(N-2*(n+1) if s==0 else -2*(n+1-2*s.bit_count())));coeffs+=1
   actual=add(actual,eta(F(a*a,N*N)))
  ck(actual==H);ck(sum(a*a for a in w)==N*N)
  edges=[F(sum(t[x]!=t[x^(1<<j)] for x in range(N)),N) for j in range(n)]
  ck(sum(edges)==I);ck(all(d==F(2*(n-1),N) for d in edges))
  profiles=[]
  for mask in range(1,N-1):
   if mask.bit_count()<2:continue
   inside=[j for j in range(n) if mask>>j&1];outside=[j for j in range(n) if not(mask>>j&1)]
   matrix=[]
   for u in range(1<<len(inside)):
    x=sum(((u>>j)&1)<<i for j,i in enumerate(inside));row=[]
    for v in range(1<<len(outside)):
     y=sum(((v>>j)&1)<<i for j,i in enumerate(outside));row.append(t[x|y])
    matrix.append(tuple(row))
   ck(len(set(matrix))==3);blocks+=1
   profiles.append({'block_mask':mask,'distinct_residual_rows':3})
  result.append({'n':n,'truth':t,'integer_Walsh':w,'H':pack(H),'I':str(I),'blocks':profiles})
 save('PILOT.json',{'rows':result,'functions':4,'coefficients':coeffs,'blocks':blocks,'checks':CHECKS,'seconds':time.perf_counter()-START,'full_FEI':'OPEN'})
 print(json.dumps({'pilot':'PASS','coefficients':coeffs,'blocks':blocks,'checks':CHECKS,'seconds':time.perf_counter()-START}))
def main():
 result=[]
 for n in range(3,33):
  H,I,mu,rows=spectrum(n);delta=1-mu*mu
  lower=mul(add({2:2*n-2},mul(lp(F(n+1)),-2)),delta)
  upper={2:F(4*n-1,2)*delta}
  ck(cmp(H,lower)>=0);ck(cmp(upper,H)>0)
  ck(cmp(H,{2:5*I})<0)
  if n==16:ck(cmp(H,{2:3*I})>0)
  if n==32:ck(cmp(H,{2:F(7,2)*I})>0)
  result.append({'n':n,'mean':str(mu),'H':pack(H),'I':str(I),'ratio_interval_scaled_by_Q':list(map(str,ev(mul(H,1/I)))),'Q':str(Q),'lower_entropy':pack(lower),'upper_entropy':pack(upper),'nonempty_weight_rows':rows})
 save('BINOMIAL.json',{'dimensions':result,'dimension_count':len(result),'spectral_weight_rows_including_empty':sum(z['n']+1 for z in result),'checks':CHECKS,'seconds':time.perf_counter()-START,'full_FEI':'OPEN','arithmetic':'exact rational prime logs and directed intervals'})
 print(json.dumps({'binomial':'PASS','dimensions':len(result),'checks':CHECKS,'seconds':time.perf_counter()-START}))
if __name__=='__main__':pilot() if '--pilot' in sys.argv else main()

from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time
R=Path(__file__).resolve().parents[1]
K=40
def ln(u):
 z=(u-1)/(u+1)
 assert 0<=z<=Q(1,3)
 s=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(K)),Q(0))
 tail=2*z**(2*K+1)/(Q(2*K+1)*(1-z*z))
 return s,s+tail
L2,U2=ln(Q(2))
def log2(q):
 assert q>0
 e=0;u=q
 while u<1:u*=2;e-=1
 while u>=2:u/=2;e+=1
 a,b=ln(u)
 return e+a/U2,e+b/L2
def eta(q):
 if not q:return Q(0),Q(0)
 a,b=log2(q);return -q*b,-q*a
def main():
 spec={'family':'radius-one Boolean balls','parameter_domain':[16,32],'case_count':2,'helper_version':'independent_atanh40_v1','arithmetic':'Fraction positive atanh series, explicit geometric tail, interval division by positive ln2','memory_estimate_mb':50,'maximum_runtime_seconds':55,'symmetry':'binomial spectrum multiplicities analytically derived, not sampled'}
 (R/'out/SOURCE_SIGN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
 t=time.monotonic();out=[]
 for n,target in [(16,Q(3)),(32,Q(7,2))]:
  N=1<<n;lo,hi=eta((1-Q(2*(n+1),N))**2)
  for k in range(1,n+1):
   a,b=eta(Q(4*(n+1-2*k)**2,N*N));lo+=comb(n,k)*a;hi+=comb(n,k)*b
  I=Q(2*n*(n-1),N)
  assert lo>target*I
  # A coarse simple rational margin is itself a certificate and keeps output small.
  margin=(lo-target*I)/I
  scale=10**8; lower=Q(margin.numerator*scale//margin.denominator,scale)
  assert lower>0
  out.append({'n':n,'target_ratio':str(target),'certified_ratio_excess_lower':str(lower),'I':str(I)})
  assert time.monotonic()-t<55
 receipt={'status':'PASS','checks':2,'seconds':time.monotonic()-t,'certificates':out,'ln_tail_proof':'For z in[0,1/3], sum_{j>=K}2z^(2j+1)/(2j+1)<=2z^(2K+1)/((2K+1)(1-z^2)).'}
 (R/'out/SOURCE_SIGNS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
if __name__=='__main__':main()

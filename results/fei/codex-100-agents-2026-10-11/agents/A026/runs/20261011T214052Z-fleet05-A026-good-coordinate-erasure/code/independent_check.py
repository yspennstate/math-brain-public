import json,time,hashlib
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter(); rows=[]; count=0; selections=bytearray()
 expected={1:Fraction(0),2:Fraction(2),3:Fraction(3),4:Fraction(7,2)}
 for n in range(1,5):
  N=1<<n; w=[N]+[0]*(N-1); prev=0; best=Fraction(0)
  chars={j:[1-2*((j&s).bit_count()%2) for s in range(N)] for j in range(1,N)}
  nonconstant=0
  for step in range(1<<(N-1)):
   gray=step^(step>>1)
   if step:
    flip=gray^prev; j=flip.bit_length()
    change=-2 if gray&flip else 2
    w=[v+change*c for v,c in zip(w,chars[j])]
   prev=gray
   assert sum(v*v for v in w)==N*N
   rr=[]
   for i in range(n):
    b=1<<i
    den=sum(w[s]**2 for s in range(N) if s&b)
    prod=sum(abs(w[s]*w[s^b]) for s in range(N) if s&b)
    if den:rr.append((Fraction(2*prod,den),i,prod,den))
   if rr:
    ratio,i,prod,den=min(rr)
    assert 4*prod<=7*den # 2 prod / den <=7/2
    best=max(best,ratio); nonconstant+=1; selections.append(i)
   else: selections.append(255)
   count+=1
   if time.perf_counter()-start>55:raise RuntimeError('frozen limit')
  assert best==expected[n]
  rows.append({'n':n,'cases':1<<(N-1),'nonconstant':nonconstant,'max_min_ratio':str(best)})
 # Independently check symmetric stress witness at n=32,t=24, via character generating polynomials.
 from math import comb
 n=32;t=24; ww=[]
 for k in range(n+1):
  poly=[1]
  for b in range(n):
   sign=-1 if b<k else 1
   nxt=[0]*(len(poly)+1)
   for j,v in enumerate(poly):nxt[j]+=v;nxt[j+1]+=sign*v
   poly=nxt
  ww.append(sum(v*(1 if j>=t else -1) for j,v in enumerate(poly)))
 assert sum(comb(n,k)*ww[k]**2 for k in range(n+1))==1<<(2*n)
 num=2*sum(comb(n-1,k)*abs(ww[k]*ww[k+1]) for k in range(n))
 den=sum(comb(n-1,k)*ww[k+1]**2 for k in range(n))
 assert Fraction(num,den)==Fraction(2220940451,536870912)>4
 result={'status':'PASS','helper_version':'A026-gray-independent-v1','cases':count,'elapsed_seconds':time.perf_counter()-start,'dimension_results':rows,'selection_bytes_sha256':hashlib.sha256(selections).hexdigest(),'symmetric_stress_ratio':str(Fraction(num,den))}
 (ROOT/'out'/'gray_selections.bin').write_bytes(selections)
 (ROOT/'out'/'independent_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()

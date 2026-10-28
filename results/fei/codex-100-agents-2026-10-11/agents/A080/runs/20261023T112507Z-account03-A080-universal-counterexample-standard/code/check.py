from pathlib import Path
import sys,time,json,hashlib
from collections import Counter
from arithmetic import Q,ell,ent,add,sub,scale,overlap,dump,LN
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out';OUT.mkdir(exist_ok=True)
start=time.monotonic();checks=0
def ck(ok,msg):
 global checks
 checks+=1
 if not ok:raise AssertionError(msg)
 if time.monotonic()-start>55:raise RuntimeError('frozen 55 second bound')
def fw(t):
 w=list(t);s=1
 while s<len(w):
  for j in range(0,len(w),2*s):
   for i in range(j,j+s):a,b=w[i],w[i+s];w[i],w[i+s]=a+b,a-b
  s*=2
 return w
def direct(n,point=0):
 N=1<<n;t=[1]*N;t[point]=-1;w=fw(t)
 ck(w[0]==N-2 and all(w[s]==-2*(-1 if (s&point).bit_count()%2 else 1) for s in range(1,N)),'signed integer Walsh at actual negative vertex')
 ck(sum(v*v for v in w)==N*N,'Parseval')
 ck(fw(w)==[N*v for v in t],'integer inversion')
 inf=Q(0)
 for j in range(n):
  edge=sum(t[x]!=t[x^(1<<j)] for x in range(N))
  ck(Q(edge,N)==Q(2,N),'each physical influence');inf+=Q(edge,N)
 masses=Counter(Q(v*v,N*N) for v in w)
 H=add(*(scale(m,ell(p)) for p,m in masses.items()))
 ck(overlap(H,E(n)),'full spectral entropy')
 ck(inf==2*n*Q(1,N),'total physical influence')
 return H,inf
def E(n):
 if n<=1:return Q(0),Q(0)
 p=Q(1,1<<n)
 return add(ell((1-2*p)**2),(8*(n-1)*p*(1-p),)*2)
def C(n):
 if n==0:return Q(0),Q(0)
 return sub(E(n+1),scale(Q(1,2),E(n)))
def V(n):return (Q(0),Q(0)) if n==0 else ((Q(2),Q(2)) if n==1 else scale(Q(2)**(2-n),C(2)))
def interval(x):return {'lo':str(x[0]),'hi':str(x[1]),'decimal_illustration':[float(t) for t in x]}
def main():
 pilot='--pilot' in sys.argv;limit=4 if pilot else 12;formula=4 if pilot else 128
 receipts=[]
 for n in range(1,limit+1):
  hg,ig=direct(n);hf,iff=direct(n+1,1<<n)
  ck(overlap(sub(hf,scale(Q(1,2),hg)),C(n)),'actual composition correction')
  # Independently substitute the two outer Fourier packets, retaining y-only atom.
  t=1-Q(2,1<<n);v=1-t*t
  cat=ent([(1+t)**2/4,(1-t)**2/4,v/4,v/4])
  cor=sub(cat,scale(Q(1,2),ent([t*t,v])))
  ck(overlap(cor,C(n)),'outer atomic correction')
  row={'n':n,'G_dimension':n,'F_dimension':n+1,'F_negative_vertex_mask':1<<n,'H_F':interval(hf),'I_F':str(iff),'C':interval(C(n))}
  receipts.append(row)
  dump(OUT/('PILOT_DIRECT.json' if pilot else 'DIRECT_FIXTURES.json'),receipts)
 witness=7**49-2**80*3**36
 ck(witness>0,'exact n3 power witness')
 ck(C(2)[0]>1,'C2 > half C1')
 ck(LN[0]>Q(2,3),'ln2 > 2/3')
 rows=[]
 for n in range(1,formula+1):
  p=Q(1,1<<n);h=E(n);c=C(n);v=V(n)
  ck(h[1]<8*n*p,'strict rate4 point-defect slack')
  ck(c[0]>0,'positive correction')
  if n>=3:
   d=sub(scale(Q(1,2),C(n-1)),c)
   ck(d[0]>0,'strict mean deficit')
   ck(v[0]>c[1],'strict repair cost')
   scaled=sub(scale(1/p,c),(Q(4),Q(4)))
   bound=(6*n+25)*p
   ck(scaled[0]>=-bound and scaled[1]<=bound,'explicit asymptotic error')
  else:d=(Q(0),Q(0))
  IF=Q(n+1,1<<n)
  ck(overlap(scale(1/IF,v),scale(Q(4,n+1),C(2))) if n>=2 else True,'influence normalization')
  rows.append({'n':n,'C':interval(c),'mean_deficit':interval(d),'V':interval(v),'I_F':str(IF),'V_over_I':interval(scale(1/IF,v)),'H_over_I':interval(scale(1/IF,E(n+1)))})
 dump(OUT/('PILOT_FORMULA.json' if pilot else 'FORMULA_CASES.json'),rows)
 result={'status':'PASS','helper':'A080-outer-correction-coherence-v1','pilot':pilot,'direct_fixtures':limit,'formula_cases':formula,'checked_assertions':checks,'exact_power_witness_difference':str(witness),'delta3':interval(sub(scale(Q(1,2),C(2)),C(3))),'C2':interval(C(2)),'runtime_seconds':time.monotonic()-start,'arithmetic_sha256':hashlib.sha256((ROOT/'code/arithmetic.py').read_bytes()).hexdigest(),'proof_scope':'Finite receipts; all-n and all-real-K bridges are analytic PROOF.md, not extrapolation.'}
 dump(OUT/('PILOT.json' if pilot else 'VALIDATION.json'),result)
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()

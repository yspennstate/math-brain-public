import json,sys,time,math
from fractions import Fraction as F
from pathlib import Path
from check import logbounds
ROOT=Path(__file__).resolve().parents[1]; count=0
def ck(t):
 global count
 assert t
 count+=1
def star(b,k):
 return F(1,b**(k-1)*24*8**(k-2)*(k-1)**2*k)
def queue(a,b,L,R):
 lam=F(1,b)
 if not R:
  return math.prod(F(b-(i==0),32*b) for i in L)
 if not L:
  return math.prod(F(a-(j==a),32*b) for j in R)
 k=len(L)+len(R)
 if L==[0] and R==[a]: return (lam/32)**2
 nl=[i for i in L if i!=0]; nr=[j for j in R if j!=a]
 if nl and nr: return star(b,k)
 if L==[0] and a in R: return star(b,k-1)*lam/32
 if R==[a] and 0 in L: return star(b,k-1)*lam/32
 return star(b,k)
def fwht(v):
 w=v[:]; d=1
 while d<len(w):
  for i in range(0,len(w),2*d):
   for j in range(i,i+d):
    x,y=w[j],w[j+d]; w[j],w[j+d]=x+y,x-y
  d*=2
 return w
def case(a,b):
 n=a+b; size=1<<n; all_edges=[(i,j) for i in range(a) for j in range(a,a+b)]; edges=[e for e in all_edges if e!=(0,a)]
 old=[2*int(any(x>>i&1 and x>>j&1 for i,j in all_edges))-1 for x in range(size)]
 new=[2*int(any(x>>i&1 and x>>j&1 for i,j in edges))-1 for x in range(size)]
 ck(sum(x!=y for x,y in zip(old,new))==1)
 wo,wn=fwht(old),fwht(new)
 I=sum(F(sum(new[x]!=new[x^(1<<i)] for x in range(size)),size) for i in range(n))
 u,v=F(1,2**a),F(1,2**b); IL=2*a*u*(1-v); IR=2*b*v*(1-u); Io=IL+IR
 ck(I>=F(2,3)*Io)
 ck(abs(I-Io)<=2*n*u*v)
 ck(Io>=6*n*u*v)
 ck(I==sum(F(wn[x]**2,size**2)*x.bit_count() for x in range(size)))
 D=(1+F(1,4*b))**len(edges)-1; variance=1-F(wn[0]**2,size**2)
 terms={D:variance}; qsum=F(0); rightcharge=F(0); mixcharge=F(0)
 for A in range(1,size):
  L=[i for i in range(a) if A>>i&1]; R=[j for j in range(a,a+b) if A>>j&1]; p=F(wn[A]**2,size**2)
  ck(wn[A]**2<=4*wo[A]**2)
  numerator=queue(a,b,L,R); qsum+=numerator/D
  lower=F(1,64**len(L)) if not R else F(a,64*b)**len(R) if not L else F(1,(64*b)**(len(L)+len(R)))
  ck(numerator>=lower)
  terms[numerator]=terms.get(numerator,F(0))-p
  if not L: rightcharge+=p*len(R)
  if L and R: mixcharge+=p*(len(L)+len(R))
 ck(qsum<=1)
 Ro=2*b*v*(1-u)**2; Mo=2*u*v*(a*(1-v)+b*(1-u))
 ck(rightcharge<=4*Ro); ck(mixcharge<=4*Mo)
 lo=hi=F(0)
 for x,c in terms.items():
  l,h=logbounds(x); lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
 ck(hi<F(297,8)*I)
 ck(sum(F(1,b) for i,j in edges if i==0)<=1)
 return {'a':a,'b':b,'I_original':str(Io),'I_actual':str(I),'D_actual':str(D),'queue_subprobability':str(qsum),'cost_interval':[str(lo),str(hi)],'ratio_upper_display':float(hi/I)}
if __name__=='__main__':
 start=time.perf_counter(); pilot='--pilot' in sys.argv
 pairs=[(2,2),(2,3),(3,3)] if pilot else [(a,b) for a in range(2,6) for b in range(a,6)]
 rows=[case(a,b) for a,b in pairs]
 result={'helper_version':'A009-one-missing-edge-v1','pilot':pilot,'functions':len(rows),'checks':count,'elapsed_seconds':time.perf_counter()-start,'all_passed':True,'cases':rows}
 ROOT.joinpath('out','DAMAGED_PILOT.json' if pilot else 'DAMAGED_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='cases'}))

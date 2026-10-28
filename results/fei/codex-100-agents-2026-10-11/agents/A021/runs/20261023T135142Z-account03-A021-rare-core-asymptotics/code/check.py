from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util,time,json,sys
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('arith',R/'code/arithmetic.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
plus,mul,const=m.plus,m.mul,m.const;count=0
def ck(x,s):
 global count
 count+=1;assert x,(count,s)
def tails(v):
 out=list(v);n=len(out).bit_length()-1
 for i in range(n):
  for s in range(len(out)):
   if not(s>>i&1):out[s]+=out[s|(1<<i)]
 return out
def V(f):
 a=m.fwht(f);weights=[x*x for x in a];up=tails(weights);N=len(a)
 return plus(*(mul(m.lg(Q(up[s],weights[s])),Q(weights[s],N*N)) for s in range(1,N) if weights[s]))
def GV(f,coords=None):
 n=len(f).bit_length()-1;root=V(f);out={}
 for i in (range(n) if coords is None else coords):out=plus(out,root,mul(plus(*(V(m.restrict(f,i,b)) for b in [0,1])),-Q(1,2)))
 return out
def phi(x):return mul(m.lg(1/x),x) if x else {}
def seed(x):return (-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1)
delta=Q(1,64);b=[seed(x) for x in range(64)];hat=[Q(v,64) for v in m.fwht(b)]
def T(s):
 A=[h+2*delta*(s-1)*(j&1) for j,h in enumerate(hat)]
 data=[v*v+4*delta*delta*(1-s*s)*(j&1) for j,v in enumerate(A)];up=tails(data)
 ck(sum(data)==1,'complete DATA law')
 return plus(*(mul(m.lg(up[j]/(A[j]*A[j])),A[j]*A[j]) for j in range(1,64) if A[j]),const(delta*5*(1-s*s)))
def run(pilot=False):
 start=time.perf_counter();rows=[];data_fixed=None;rootT=T(Q(0))
 for n in ([3] if pilot else [3,5,7]):
  a=[1 if z.bit_count()>n//2 else -1 for z in range(1<<n)]
  f=[seed(x)*(aa if x in [0,1] else 1) for aa in a for x in range(64)]
  h=[aa*(1 if y==0 else -1) for aa in a for y in [0,1]]
  d=Q(__import__('math').comb(n-1,(n-1)//2),1<<(n-1));ck(sum(a)==0,'majority balanced')
  ck(abs(m.fwht(a)[1])==d*len(a),'exact singleton coefficient magnitude')
  va=V(a);ga=GV(a);gh=GV(h);gf=GV(f);gd=GV(f,range(6));gc=plus(gf,mul(gd,-1))
  ck(V(f)==plus(mul(va,2*delta),rootT),'exact nonempty potential split')
  if data_fixed is None:data_fixed=gd
  ck(gd==data_fixed,'DATA increment independent of controller width')
  singleton=mul(phi(d*d),n)
  ck(plus(ga,mul(gh,-1))==singleton,'shared selector singleton cocycle')
  smooth=mul(plus(rootT,mul(plus(T(d),T(-d)),-Q(1,2))),n)
  residual=plus(gf,mul(gh,-2*delta))
  ck(residual==plus(mul(singleton,2*delta),smooth,gd),'EXACT mux-owner missing term')
  ck(m.ge(plus(smooth,const(Q(1,2)))) and m.ge(plus(const(Q(13,2)),mul(smooth,-1))),'uniform smooth curvature bill')
  corrected=plus(gf,mul(ga,-2*delta))
  ck(m.ge(plus(corrected,const(37))) and m.ge(plus(const(49),mul(corrected,-1))),'corrected owner uniformly bounded')
  Id=sum((m.inf(f,i) for i in range(6)),Q(0));ck(Id>=Q(21,16),'DATA boundary reserve')
  ck(m.ge(plus(const(256*Id),mul(corrected,-1))),'corrected SAME256 transfer')
  lo,hi=m.bounds(residual)
  rows.append({'control_bits':n,'singleton':str(d),'DATA_influence':str(Id),'residual_bounds':[str(lo),str(hi)],'residual_expression':{str(p):str(c) for p,c in residual.items()},'corrected_expression':{str(p):str(c) for p,c in corrected.items()}})
  if time.perf_counter()-start>110:raise RuntimeError('frozen120s cap')
 out={'status':'PASS','control_widths':[x['control_bits'] for x in rows],'assertions':count,'seconds':time.perf_counter()-start,'rows':rows}
 (R/'out'/('PILOT.json' if pilot else 'DIRECT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':run('--pilot' in sys.argv)

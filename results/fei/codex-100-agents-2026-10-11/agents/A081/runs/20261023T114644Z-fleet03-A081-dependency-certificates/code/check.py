from pathlib import Path
from fractions import Fraction as F
import json,time,sys,importlib.util
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261023T004705Z-fleet03-A081-dependency-certificates/code/check_resets.py'
sp=importlib.util.spec_from_file_location('scalar',old);lib=importlib.util.module_from_spec(sp);sp.loader.exec_module(lib)
N=0
def ck(x):
 global N
 N+=1
 if not x:raise AssertionError(N)
def spectrum(f):
 a=[F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f))]
 p=[v*v for v in a];ck(sum(p)==1);return p
def factor(v):
 z={};k=2
 while k*k<=v:
  while v%k==0:z[k]=z.get(k,0)+1;v//=k
  k+=1
 if v>1:z[v]=z.get(v,0)+1
 return z
def ce(p,q):
 out={}
 for a,b in zip(p,q):
  if not a:continue
  ck(b>0)
  for v,sgn in [(b.numerator,-1),(b.denominator,1)]:
   for prime,k in factor(v).items():out[prime]=out.get(prime,F(0))+sgn*a*k
 return {p:a for p,a in out.items() if a}
def add(*terms):
 z={}
 for e,c in terms:
  for p,a in e.items():z[p]=z.get(p,F(0))+a*c
 return {p:a for p,a in z.items() if a}
def interval(e):
 lo=hi=F(0)
 for p,a in e.items():
  l,h=lib.lib.log2(F(p));lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
 return lo,hi
def child(f,j,b):return [f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(f)//2)]
def main():
 start=time.perf_counter();cases=0;zerofibers=0
 for n in [1,2]:
  size=1<<n
  for tab in range(1,(1<<size)-1):
   f=[1 if tab>>x&1 else -1 for x in range(size)];p=spectrum(f)
   for mass in [F(1),F(1,3)]:
    for eta in [F(0),F(1,4)]:
     q=[mass*((1-eta)*v+eta/size) for v in p];ck(sum(q)==mass)
     D=add((ce(p,q),1),(ce(p,p),-1));ck(interval(D)[0]>=0)
     for j in range(n):
      pp=[spectrum(child(f,j,b)) for b in [0,1]];raw=[[],[]]
      for i in range(size//2):
       ix=(i&((1<<j)-1))|((i>>j)<<(j+1));m=p[ix]+p[ix+(1<<j)];r=q[ix]+q[ix+(1<<j)];ck(m==(pp[0][i]+pp[1][i])/2)
       if not m:zerofibers+=int(r>0)
       for b in [0,1]:raw[b].append(r*pp[b][i]/m if m else r)
      Z=[sum(v) for v in raw];ck(sum(Z)==2*mass);ck(min(Z)>0)
      qq=[[mass*v/Z[b] for v in raw[b]] for b in [0,1]];ds=[]
      for b in [0,1]:
       ck(sum(qq[b])==mass);ds.append(add((ce(pp[b],qq[b]),1),(ce(pp[b],pp[b]),-1)))
      gap=add((D,1),(ds[0],F(-1,2)),(ds[1],F(-1,2)));ck(interval(gap)[0]>=0)
      penalty=ce([F(1)],[mass]);ck(interval(add((D,1),(penalty,-1)))[0]>=0)
      cases+=1
 ck(cases==120);ck(zerofibers>0)
 # Exact coefficient/affine certificates. Entire half-lines are justified by
 # these nonnegative slopes/intercepts, not by the finite replay below.
 margins={'root_final':[F(3,2),F(45,4)],'padding':[F(2),F(11,2)],'source':[F(1),F(45,8)]}
 target=[F(1),F(11,2)]
 residuals={k:[a-target[0],b-target[1]] for k,(a,b) in margins.items()}
 ck(all(v>=0 for row in residuals.values() for v in row))
 ck(F(11,2)-F(37,8)==F(7,8));ck(F(37,8)-1==F(29,8))
 ck(F(7,8)*15-F(61,8)==F(11,2));ck(F(7,8)*15-F(15,2)==F(45,8))
 ck(3*3+13*3-9>0);ck(F(3*3+15*3+7,1<<3)==F(61,8))
 for q in range(3,65):
  ck(q*q+13*q-9>0);ck(F(q*q+15*q+7,1<<q)>=F((q+1)**2+15*(q+1)+7,1<<(q+1)))
  ck(F(q+1,1<<q)>=F(q+2,1<<(q+1)))
 for c in [F(k,8) for k in range(65)]:
  ck(min(a*c+b for a,b in margins.values())>=c+F(11,2))
  # sharper interface envelope keeps min(C0,1/8), without a new source claim
  cap=c+F(37,8)+min(c,F(1,8));ck(min(a*c+b for a,b in margins.values())-cap>=F(7,8))
  v=c
  for depth in range(9):
   ck(v==(c+5)*4**depth-5);v=4*v+15
 ck(time.perf_counter()-start<55)
 out={'status':'PASS','assertions':N,'source_query_cases':cases,'reference_only_zero_true_fibers':zerofibers,'coefficient_residuals':{k:[str(x) for x in v] for k,v in residuals.items()},'new_vs_old_allowance_difference':'29/8 times original I_g; same reserve7/8 I_g','seconds':time.perf_counter()-start,'scope':'Exact finite source-inheritance replay plus all-C0 affine certificate; full physical all-frontier theorem remains scoped to pinned interfaces','FEI':'OPEN'}
 (R/'out/EXACT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()

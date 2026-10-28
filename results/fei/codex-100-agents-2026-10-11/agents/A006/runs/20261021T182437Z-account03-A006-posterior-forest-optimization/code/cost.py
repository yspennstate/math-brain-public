from pathlib import Path
from fractions import Fraction as F
from math import prod
import sys,json,time
sys.dont_write_bytecode=True
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B.parents[1]/'runs/20261014T074929Z-account05-A006-posterior-forest-optimization/code'))
from star_full import enumerate_runs
start=time.monotonic();checks=0
def ck(p):
 global checks
 checks+=1;assert p,checks
def floor(x,bits):return F((x.numerator<<bits)//x.denominator,1<<bits)
def ceil(x,bits):return -floor(-x,bits)
def lnunit(y):
 ck(1<=y<=2)
 t=(y-1)/(y+1);z=t;lo=F(0)
 for j in range(20):lo+=2*z/(2*j+1);z*=t*t
 return lo,lo+2*z/(41*(1-t*t))
l2,u2=lnunit(F(2));ck(F(2,3)<l2<u2<1)
def log2(x):
 ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/(F(2)**k)
 if y<1:y*=2;k-=1
 a,b=lnunit(y)
 return floor(k+a/u2,40),ceil(k+b/l2,40)
ck(log2(F(1))==(0,0));ck(log2(F(8))==(3,3));ck(log2(F(1,8))==(-3,-3))
rows=[];data=json.loads((B/'out/CHECK.json').read_text(encoding='utf-8'))
for row in data['rows']:
 E=row['edges'];n=row['n'];N=len(E);degree=max(sum(v in e for e in E) for v in range(n))
 lam=F(1,2*degree);D=(1+lam/4)**N-1
 f=[1 if any(all(x>>v&1 for v in e) for e in E) else -1 for x in range(1<<n)]
 # Direct character sums, independent of the butterfly spectrum routine.
 P={A:F(sum(f[x]*(-1 if (x&A).bit_count()%2 else 1) for x in range(1<<n))**2,1<<(2*n)) for A in range(1,1<<n)}
 ck(sum(A.bit_count()*p for A,p in P.items())==F(row['I']))
 lo=F(0);hi=F(0)
 for A,p in P.items():
  if not p:continue
  C,_=enumerate_runs(A,n-1,edges=E)
  q=sum(c*lam**U.bit_count() for U,c in C.items())/D;ck(0<q<=1)
  a,b=log2(1/q);lo+=p*a;hi+=p*b
 clo,chi=floor(lo,32),ceil(hi,32);ck(0<=chi-clo<=F(1,1<<30))
 best=F(row['certificates']['lifted']['best_value']);gap=best-F(row['v']);ck(2*gap<F(9,10)*F(row['I']))
 # G0-gap/ln2 is a lower bound, not a claim that the relaxation is realizable.
 global_lo=floor(clo-gap/l2,32)
 rows.append({'n':n,'edges':E,'I':row['I'],'reference_cost_interval_bits':[str(clo),str(chi)],'joint_infimum_enclosure_bits':[str(global_lo),str(chi)],'certified_reference_gap_upper_bits':str(ceil(gap/l2,32))})
 (B/'out/COST_CHECKPOINT.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 ck(time.monotonic()-start<55)
out={'status':'PASS','graphs':len(rows),'assertions':checks,'all_bit_gaps_less_than_9I_over_10':True,'seconds':time.monotonic()-start,'rows':rows}
(B/'out/COST.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

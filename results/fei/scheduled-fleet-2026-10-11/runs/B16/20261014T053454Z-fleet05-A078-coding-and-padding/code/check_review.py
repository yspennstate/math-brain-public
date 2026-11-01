from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,itertools
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('ownlog',AGENT/'runs/20261013T234208Z-fleet05-A078-coding-and-padding/code/check.py')
L=importlib.util.module_from_spec(sp);sp.loader.exec_module(L)
sp=importlib.util.spec_from_file_location('owncode',ROOT/'code/check.py');C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
start=time.perf_counter();count=0
def ck(x):
 global count
 count+=1;assert x
 assert time.perf_counter()-start<55
def I(t):return sum((L.edge(t,j) for j in range(len(t).bit_length()-1)),F(0))
def entropy(t):
 d={}
 for w in C.walsh(t):
  p=F(w*w,len(t)**2)
  if p:L.addlog(d,p,-p)
 return d
def cert(d):
 if not d:return ['0','0']
 v=(F(0),F(0))
 for p,c in d.items():v=L.plus(v,L.scale(L.log(F(p)),c))
 ck(v[0]>=0)
 U=1<<80;return [str(F((v[0]*U).__floor__(),U)),str(F((v[1]*U).__ceil__(),U))]
def main():
 controls=[]
 for m in [1,2,3]:
  for mask in range(1<<(1<<m)):
   g=[1-2*(mask>>y&1) for y in range(1<<m)];root=[1]*len(g)+g;c=1-F(sum(g),len(g));j=c/2
   bound={2:3*j};L.combine(bound,L.Bmap(root,m),F(-1));bcert=cert(bound)
   signed={2:6*j};L.combine(signed,entropy(root),F(-1));L.combine(signed,entropy(g),F(1,2));dcert=cert(signed)
   ck(L.edge(root,m)==j)
   controls.append({'m':m,'mask':mask,'B_slack':bcert,'signed_slack':dcert})
 rows=[]
 cores=[[1-2*(mask>>y&1) for y in range(2)] for mask in range(4)]
 for idx in itertools.product(range(4),repeat=3):
  gs=[cores[j] for j in idx];Is=[I(g) for g in gs]
  gam={(i,j):F(sum(gs[i][y]!=gs[j][y] for y in range(2)),2) for i,j in [(0,1),(0,2),(1,2)]}
  Ip={(i,j):I([gs[i][y]*gs[j][y] for y in range(2)]) for i,j in gam}
  for r,s in [(1,1),(1,2),(2,1),(2,2)]:
   a=F(1,1<<r);b=F(1,1<<s);pi=[1-a,a*(1-b),a*b]
   t=[]
   for y in range(1<<(1+r+s)):
    x=y&1;ac=(y>>1)&((1<<r)-1);bc=y>>(1+r)
    t.append(gs[0 if ac else (1 if bc else 2)][x])
   IB=2*s*b*gam[1,2];IA=2*r*a*((1-b)*gam[0,1]+b*gam[0,2]);IC=IA+a*IB;IT=sum((pi[i]*Is[i] for i in range(3)),F(0))
   ck(I(t)==IC+IT);ck(L.edge(t,0)==IT)
   ck(sum((L.edge(t,j) for j in range(1,1+r+s)),F(0))==IC)
   RD=2*a*(1-a)*((1-b)*Ip[0,1]+b*Ip[0,2])+2*a*b*(1-b)*Ip[1,2]
   RS=2*sum((pi[i]*pi[j]*Ip[i,j] for i,j in Ip),F(0))
   ck(RD-RS==2*a*(1-a)*b*(1-b)*Ip[1,2])
   owners=sum((2*(1-pi[i])*pi[i]*Is[i] for i in range(3)),F(0))
   ck(RS<=owners<=2*IT)
   rows.append({'cores':idx,'r':r,'s':s,'IC':str(IC),'IT':str(IT),'R_star':str(RS),'grouping_difference':str(RD-RS)})
 out={'status':'PASS','assertions':count,'control_split_cases':len(controls),'independent_algebra_cases':len(rows),'seconds':time.perf_counter()-start,'controls':controls,'algebra':rows,'review_scope':'A023 stage5 independently reconstructed nested identities only; finite signed-refund theorem excluded'}
 (ROOT/'out/review.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['controls','algebra']}))
if __name__=='__main__':main()

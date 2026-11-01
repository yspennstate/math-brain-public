"""Independent integer-spectrum stress reconstruction of two prescribed edits."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from time import perf_counter
import importlib.util,json,sys
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('own',ROOT/'code/check.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
start=perf_counter();checks=0
def ck(b,label):
 global checks
 checks+=1
 if not b:raise AssertionError(label)
 if perf_counter()-start>58:raise TimeoutError('frozen 60sec')
def P(tab):
 a=list(tab);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(F(v*v,len(a)**2) for v in a)
def ce(p,q):
 groups=defaultdict(F)
 for x,y in zip(p,q):
  if x:ck(y>0,'true support');groups[y]+=x
 lo=hi=F(0)
 for y,x in groups.items():
  l,u=m.lib.log2(y);lo-=x*u;hi-=x*l
 return lo,hi
def H(p):return ce(p,p)
def D(p,q):return m.sub(ce(p,q),H(p))
def floor(tab,Q,factor,point=0):
 n=len(tab);rho=F(1,2*n);out=tuple(v-2*tab[point]*int(x==point) for x,v in enumerate(tab+tab));pp=P(out)
 beta=factor*rho;data=tuple((q+beta/n)/(1+beta) for q in Q)
 marginal=tuple(pp[k]+pp[k+n] for k in range(n));qq=tuple(data[k%n]*pp[k]/marginal[k%n] for k in range(2*n))
 ck(sum(qq)==(sum(Q)+beta)/(1+beta),'complete floor mass')
 return out,qq
def first(g,R,pad):
 tab=tuple(g[x%len(g)] for x in range(len(g)*2**pad));Q=tuple(R[x] if x<len(R) else F(0) for x in range(len(tab)))
 return floor(tab,Q,6)
def fixture(a,g,s,eta,z):
 b=6;D1=a+b+1;D2=D1+1;rho1=F(1,2**D1);rho2=rho1/2;pg=P(g);R=tuple(s*((1-eta)*x+eta/F(len(g))) for x in pg)
 c=ce(pg,R);Ig=m.lib.influence(g);C0=c[1]/Ig;K=4*C0+15
 tab,Q=first(g,R,b);F1=tab;F2,Qroot=floor(F1,Q,8,z);I1=m.lib.influence(F1);I2=m.lib.influence(F2);HF2=H(P(F2))
 d=sum(g[0]!=g[1<<j] for j in range(a));d1=sum(F1[z]!=F1[z^(1<<j)] for j in range(D1));G1=2*rho1*(D1-d);E1=2*rho1*d;G2=2*rho2*(D2-d1);E2=2*rho2*d1
 ck(I2==Ig+G1+G2-E1-E2,'two literal physical edge identities')
 ck(I2>=F(123,128)*Ig+G1+G2,'original source influence')
 U=min((C0+1)*Ig,K*G1);bound=F(13,4)*c[0]+105*rho1*D1+100*rho2*D2
 rootce=ce(P(F2),Qroot);ck(rootce[1]<bound,'root original price')
 leaves=[];labels=list(range(D1));assigned={};reach=F(1);src=g;model=R;remainingpad=b
 for depth,physical in enumerate(list(range(a,a+b))+list(range(a)),1):
  j=labels.index(physical);newlabels=labels[:j]+labels[j+1:]
  if physical>=a:
   offQ=tuple(model[k] if k<len(model) else F(0) for k in range(len(tab)//2));remainingpad-=1
  else:
   children,models=m.inherit(src,model,0);src=children[0];model=models[0]
   offQ=tuple(models[1][k] if k<len(models[1]) else F(0) for k in range(len(tab)//2))
  off=m.lib.child(tab,j,1);offassigned=dict(assigned);offassigned[physical]=1
  leaves.append((off,offQ,newlabels,offassigned,reach/2))
  assigned=dict(assigned);assigned[physical]=0;reach/=2;labels=newlabels;tab,Q=first(src,model,remainingpad)
  active=(tab,Q,labels,assigned,reach);avD=(F(0),F(0));L1D=(F(0),F(0));hits=0
  for oldtab,oldQ,labs,aa,rr in leaves+[active]:
   L1D=m.add(L1D,m.mul(rr,D(P(oldtab),oldQ)))
   if all(((z>>j)&1)==v for j,v in aa.items()):
    hits+=1;local=sum(((z>>j)&1)<<k for k,j in enumerate(labs));newtab,newQ=floor(oldtab,oldQ,8,local)
   else:
    newtab=oldtab+oldtab;newQ=oldQ+(F(0),)*len(oldQ)
   avD=m.add(avD,m.mul(rr,D(P(newtab),newQ)))
  ck(hits==1,'unique physical second-point leaf; no duplicate witnesses')
  L2=m.add(HF2,avD);L1=m.add(H(P(F1)),L1D)
  ck(L2[1]<bound,'every old frontier full two-edit bill')
  ck(K*I2-L2[1]>= (F(19,32)*C0+F(75,8))*Ig+K*(G1+G2),'same original bank lower bound')
  ck(K*I2-L2[1]-U>= (F(11,32)*C0+F(135,16))*Ig+K*(G1+G2),'entire old allowance retained')
  # Exact operation accounting verified algebraically, independent of log values.
  ck(K*I2-K*I1==K*(G2-E2),'operation influence increment, not KL-only reset')
 return {'a':a,'point':z,'frontiers':a+b,'I2':str(I2),'source_cost_upper':str(c[1])}
def main():
 rows=[]
 for a,g,s,eta in [(1,(-1,1),F(1),F(0)),(2,(-1,1,1,1),F(1,2),F(1,4))]:
  for z in (0,1<<a,1):
   rows.append(fixture(a,g,s,eta,z))
   if '--pilot' in sys.argv:break
  if '--pilot' in sys.argv:break
 # Reconstruct the actual physical third-reset child, not just supplied class rows.
 src=tuple(1 if x==0 else -1 for x in range(16));coef=m.lib.spectrum(src);eps=F(1,16);W=2*eps-16*eps*eps
 tab=tuple(src[x%16]-2*int(x==16) for x in range(32));Q=tuple((1-W)*coef[k]*coef[k] if k<16 else eps*eps for k in range(32))
 children,models=m.inherit(tab,Q,0);actual=P(children[0]);before=models[0]
 fresh=(F(63,128),)+(F(7,128),)*7+(F(1,64),)*8
 ck(actual==(F(49,64),)+(F(1,64),)*15,'literal physical third-reset child')
 ck(before==(F(18375,33856),)+(F(1695,33856),)*7+(F(113,8464),)*8,'independent full inherited reference classes')
 ck(sum(before)==sum(fresh)==1,'entire third-reset references normalized')
 ck(tuple(before[k]/fresh[k] for k in range(16))==(F(12250,11109),)+(F(3390,3703),)*7+(F(452,529),)*8,'literal likelihood ratios')
 N=12250**49*3390**7*452**8;den=11109**49*3703**7*529**8
 ck(N>16*den and N*N<512*den*den,'independent integer third-reset sign')
 ck(F(4039,32768)>F(1,10)>F(279,16384),'nonvanishing booking gap')
 result={'status':'PASS','assertions':checks,'fixtures':rows,'seconds':perf_counter()-start,'third_reset_integer_sign':'1/128<e3<9/1024','rare_allowance':'4039/32768>1/10>279/16384'}
 (ROOT/'out'/('TWO_PILOT.json' if '--pilot' in sys.argv else 'TWO_RESULTS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))
if __name__=='__main__':
 try:main()
 except Exception as e:
  (ROOT/'out'/'TWO_FAILURE.json').write_text(json.dumps({'status':'FAIL_OR_INCOMPLETE','error':repr(e),'assertions':checks,'seconds':perf_counter()-start}),encoding='utf-8');raise

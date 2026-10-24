from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,time,argparse,math
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];START=time.perf_counter();COUNT=0
def module(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
# Only own previously checked arithmetic primitives; no other agent helper.
R=module('own_fourth_roots',AGENT/'runs/20261012T023229Z-account05-A078-coding-and-padding/code/check_core_transport.py')
Z=module('own_prime_log',AGENT/'runs/20261013T234208Z-account05-A078-coding-and-padding/code/check.py')
def ck(ok):
 global COUNT
 COUNT+=1;assert ok
 if time.perf_counter()-START>55:raise TimeoutError('55 second frozen guard')
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def activation(g,l):return tuple(g[x&(len(g)-1)] if x>>((len(g)-1).bit_length())==0 else 1 for x in range(len(g)*(1<<l)))
@lru_cache(None)
def edge(t,i):return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
@lru_cache(None)
def totalI(t):return sum(edge(t,i) for i in range((len(t)-1).bit_length()))
@lru_cache(None)
def profile(t,i):
 u,v,D=R.pair(t,i);normal=R.profile(u,v,D);bounds=(F(0),F(0));unit=1<<80
 for rad,c in normal.items():
  n=math.isqrt(math.isqrt(rad<<(4*80)));hi=n if n**4==rad<<(4*80) else n+1
  bounds=add(bounds,(F(n,unit)*c,F(hi,unit)*c))
 return normal,mul(bounds,6)
@lru_cache(None)
def entropy(t):
 out={};D=len(t)
 for n in Z.walsh(t):
  p=F(n*n,D*D)
  if p:Z.addlog(out,p,-p)
 return out
def local(g,l,i,t):
 p=F(1,1<<l);u,v,D=R.pair(g,i);mu=F(u[0],D);nu=F(v[0],D)
 old,b0=profile(g,i);actual,b1=profile(t,i);expected={}
 R.plus_scaled(expected,old,p)
 rad,c=R.term(mu,nu);R.add(expected,rad,-p*c)
 rad,c=R.term(1-mu,nu);R.add(expected,rad,p*(1-p)*c)
 rad,c=R.root4(p**6*(1-p+p*mu)**2*nu**6);R.add(expected,rad,c)
 ck(actual==expected)
 a=edge(t,i);ck(a==p*edge(g,i))
 ck(b1[0]>=p*b0[1]-6*a);ck(b1[1]<=p*b0[0]+15*a)
 return b1,b0,a
def empty_acc():return {'dataL':(F(0),F(0)),'controlL':(F(0),F(0)),'shadowL':(F(0),F(0)),'dataI':F(0),'controlI':F(0),'leafI':F(0),'shadow_leafI':F(0),'shadow_control_leafI':F(0),'leafH':{},'shadow_leafH':{},'shadow_mass':F(0),'nodes':0}
def walk(g,l,policy,limit,depth,w,pi,p0,acc,active=True):
 t=activation(g,l) if active else (1,)*(len(g)*(1<<l));k=(len(g)-1).bit_length()
 if not active or len(set(t))==1 or (limit is not None and depth>=limit):
  acc['leafI']+=w*totalI(t);Z.combine(acc['leafH'],entropy(t),w)
  if active:
   p=F(1,1<<l);ck(w*p==p0*pi);acc['shadow_mass']+=pi
   acc['shadow_leafI']+=pi*totalI(g)
   acc['shadow_control_leafI']+=pi*l*(1-F(sum(g),len(g)))
   Z.combine(acc['shadow_leafH'],entropy(t),p0*pi/p)
  return
 ck(active);ck(w*F(1,1<<l)==p0*pi);acc['nodes']+=1
 controls=l>0 and (k==0 or policy=='control_first' or (policy=='alternating' and depth%2==0))
 if controls:
  i=k;normal,b=profile(t,i);j=edge(t,i);p=F(1,1<<l);ck(j==p*(1-F(sum(g),len(g))))
  expected={};R.add(expected,1,j-j*j);rad,c=R.term(1-j,j);R.add(expected,rad,c)
  ck(normal==expected);ck(b[1]<=F(15,2)*j)
  acc['controlL']=add(acc['controlL'],mul(b,w));acc['controlI']+=w*j
  walk(g,l-1,policy,limit,depth+1,w/2,pi,p0,acc)
  walk(g,l-1,policy,limit,depth+1,w/2,F(0),p0,acc,False)
 else:
  i=max(range(k),key=lambda z:(edge(g,z),-z));b,shadow,a=local(g,l,i,t)
  acc['dataL']=add(acc['dataL'],mul(b,w));acc['shadowL']=add(acc['shadowL'],mul(shadow,pi));acc['dataI']+=w*a
  for bit in [0,1]:
   child=tuple(g[x] for x in range(len(g)) if ((x>>i)&1)==bit)
   walk(child,l,policy,limit,depth+1,w/2,pi/2,p0,acc)
def tree(g,s,policy,limit):
 p=F(1,1<<s);a=empty_acc();walk(g,s,policy,limit,0,F(1),F(1),p,a)
 ck(a['shadow_mass']==1)
 ck(a['dataI']==p*(totalI(g)-a['shadow_leafI']))
 ck(a['controlI']==p*(s*(1-F(sum(g),len(g)))-a['shadow_control_leafI']))
 ck(a['leafI']==p*(a['shadow_leafI']+a['shadow_control_leafI']))
 ck(a['dataI']+a['controlI']+a['leafI']==totalI(activation(g,s)))
 ck(a['leafH']==a['shadow_leafH'])
 ck(a['dataL'][0]>=p*a['shadowL'][1]-6*a['dataI'])
 ck(a['dataL'][1]<=p*a['shadowL'][0]+15*a['dataI'])
 ck(a['controlL'][1]<=F(15,2)*a['controlI'])
 if limit is None:ck(a['leafI']==0 and not a['leafH'])
 return {'s':s,'policy':policy,'limit':limit,'data_influence':str(a['dataI']),'control_influence':str(a['controlI']),'terminal_influence':str(a['leafI']),'terminal_entropy_prime_map':{str(k):str(v) for k,v in a['leafH'].items()},'nodes':a['nodes']}
def review():
 out=[]
 for k in [2,4,6]:
  N=1<<k;a=F(1,N);b=F(1,1<<(k//2));h=tuple(-1 if sum(((s>>(2*j))&1)*((s>>(2*j+1))&1) for j in range(k//2))%2 else 1 for s in range(N))
  g=tuple(-1 if s==0 and x==0 else 1 for x in range(2) for s in range(N));f=g+tuple(h[s] for x in range(2) for s in range(N))
  for r in [1,2]:
   q=F(1,1<<r);c=(1-b+a)/2;w=activation(f,r)
   ck(edge(w,k)==q*a/2)
   for i in list(range(k))+[k+1]+list(range(k+2,k+2+r)):
    ck(edge(w,i)==(q*(a+F(1,2))/2 if i<k else q*c))
   ck(totalI(w)==q*(F(k,4)+F(k+1,2)*a+(r+1)*c))
   d=add(add(mul(Z.S(-a,a,b),q*(N-1)),mul(Z.S(-a,a,b-1),q*(1-q))),Z.S(1-q*a,q*a,1-q+q*b))
   if k>=4:ck(d[0]>=(q*a/2)*(k-4))
   # Independently reconstruct all signed common-row amplitudes of actual W.
   u,v,D=R.pair(w,k);gg=activation(g,r);ug,vg,DG=R.pair(gg,k);hh=R.walsh(activation(h,r))
   for C in range(len(ug)):
    hhindex=(C&((1<<k)-1))+((C>>k)<<k);hv=F(hh[hhindex],len(hh))
    for zz in [0,1]:
     j=(C&((1<<k)-1))+(zz<<k)+((C>>k)<<(k+1))
     ck(F(u[j],D)==(F(ug[C],DG)+(hv if zz==0 else -hv))/2)
     ck(F(v[j],D)==F(vg[C],DG)/2)
   out.append({'k':k,'r':r,'status':'PASS'})
 return out
def main(pilot):
 rows=[];cores=0
 for k in ([1,2] if pilot else [1,2,3]):
  masks=range(1<<(1<<k)) if k<3 else [0,1,7,15,23,105,150,255]
  for m in masks:
   cores+=1;g=tuple(1-2*((m>>x)&1) for x in range(1<<k))
   for s in ([1] if pilot else [1,2]):
    for policy in (['core_first','control_first'] if pilot else ['core_first','control_first','alternating']):
     for limit in ([1,None] if pilot else [1,2,None]):
      row=tree(g,s,policy,limit);row.update({'core_k':k,'core_mask':m});rows.append(row)
 rev=[] if pilot else review()
 result={'status':'PASS','helper':'interleaved-quarter-activation-v1','pilot':pilot,'assertions':COUNT,'cores':cores,'physical_trees':len(rows),'nodes':sum(r['nodes'] for r in rows),'review_roots':rev,'seconds':time.perf_counter()-START,'arithmetic':'Exact fourth-root identities;80-bit outward root intervals;prime-log terminal laws and physical edges','trees':rows}
 (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/('pilot.json' if pilot else 'full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='trees'}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();main(args.pilot)

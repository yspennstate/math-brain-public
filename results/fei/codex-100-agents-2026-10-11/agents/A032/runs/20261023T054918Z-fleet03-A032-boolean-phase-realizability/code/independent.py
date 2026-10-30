from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 assert time.perf_counter()-t0<55
def walsh(f):
 return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f))]
def spectrum(f):return [v*v for v in walsh(f)]
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,list):return [enc(v) for v in x]
 return x
# A033 phase-only four terminals, direct character sums, not main-checker helpers.
k=[-1,1,1,1]
phase=[]
for sigma in [-1,1]:
 for tau in [-1,1]:
  f=[(1 if c==0 else sigma*tau*v) for v in k for c in [0,1]]
  p=spectrum(f);ck(all(v in [-1,1] for v in f));ck(sorted(p[:2])==[F(1,16),F(9,16)])
  ck(sum(p[2:])==F(3,8));phase.append(p)
ck(3**9>4*5**5);ck(8**4<2*7**4)
# A033 paid first mixture, current marginal and second target.
h=[1,1,1,-1,1,1,1,-1];p=spectrum(h);ck(p[0]==F(1,4))
M=[F(0)]+[F(7,8)*v/F(3,4)+F(1,56) for v in p[1:]]
ck(sum(M)==1);ck(M[1]==F(13,42))
L=[F(0)]+[(M[2*v]+M[2*v+1])/(1-M[1]) for v in [1,2,3]]
ck(L[1:]==[F(26,29),F(3,58),F(3,58)])
N=[F(7,8)*v for v in L];N[2]+=F(1,8)
ck(N[1:]==[F(91,116),F(79,464),F(21,464)])
ck(1-F(3,8)*F(3,4)*(1-M[1])==F(361,448))
ck(448**40*7**15>2**8*361**40*8**15)
# Independently derive the new mask and group coefficients by direct Walsh.
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-v*v for v in a]
A=walsh(a);B=walsh(b);ck(A[:8]==[F(1,8)]*8)
ck([i for i in range(16) if B[i]==F(3,8)]==[0,4]);ck(sum(x*y for x,y in zip(A,B))==0)
mins=[]
for n in range(-32,33):
 mu=F(n,32);r=mu*mu;t=(35*r+7)/48;d=r-t
 for sig in [-1,1]:
  p=[(x+sig*mu*y)**2 for x,y in zip(A,B)]+[F(3,8)*(1-r)]
  q=[x*x+y*y*t for x,y in zip(A,B)]+[F(3,8)*(1-t)]
  ck(sum(p)==sum(q)==1);delta=[x-y for x,y in zip(p,q)]
  dl=delta[0]+delta[4];ds=sum(delta[i] for i in range(8) if i not in [0,4])
  ck(dl==3*sig*mu/16+9*d/32);ck(ds==-3*sig*mu/16+3*d/32)
  ck(dl-3*ds==3*sig*mu/4)
  l1=sum(abs(x) for x in delta);ck(l1>=abs(mu)/4);ck(l1>=3*abs(d)/4);ck(l1>=F(1,16))
  if abs(mu)<F(1,4):ck(abs(d)>F(33,256))
  mins.append(l1)
ck(F(99,1024)>F(1,16));ck(F(1,16)**2/2==F(1,512))
ck(F(1,512)-F(3,2048)==F(1,2048));ck(512**256<2*511**256)
ck(320**40*7**15>2**8*257**40*8**15)
# Direct transform of actual nonconstant arbitrary-core fixture.
k=[-1,-1,-1,1];h=[1 if not(x&1) else (1 if not(x&2) else -1)*k[x>>2] for x in range(16)]
ph=spectrum(h);pk=spectrum(k);ck(ph[:2]==[F(1,4)]*2)
for t,v in enumerate(pk):ck(ph[4*t+2]==ph[4*t+3]==v/4)
root=[aa+z*bb*v for z in [1,-1] for v in h for aa,bb in zip(a,b)]
ck(all(v in [-1,1] for v in root));pr=spectrum(root);ck(sum(pr)==1)
ck(pr[:16]==[v*v for v in A])
ck(sum(pr[16*len(h):])==F(3,8))
result={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'mean_grid_points':65,'minimum_observed_L1':min(mins),'A033_review':'HOLDS_AT_STATED_SCOPE','source_fixture_spectra':phase,'new_root_truth_table':root,'new_root_raw_walsh':[v*len(root) for v in walsh(root)],'formal_status':'NOT_CLAIMED'}
(R/'out/independent.json').write_text(json.dumps(enc(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:enc(v) for k,v in result.items() if k not in ['source_fixture_spectra','new_root_truth_table','new_root_raw_walsh']}))

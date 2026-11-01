from fractions import Fraction as F
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parents[1];start=time.monotonic();checks=nodes=trees=absorbed=0
def ck(x):
 global checks
 checks+=1;assert x
 if checks%1000==0 and time.monotonic()-start>55:raise TimeoutError('55s')
def fwht(v):
 a=[F(t,len(v)) for t in v];step=1
 while step<len(a):
  for i in range(0,len(a),step*2):
   for j in range(step):
    x,y=a[i+j],a[i+j+step];a[i+j]=x+y;a[i+j+step]=x-y
  step*=2
 return a
def remove(j,i):return (j%2**i)+(j//2**(i+1))*2**i
def walk(v,j,k,order,mode,depth=0,dead=False):
 global nodes,absorbed
 nodes+=1;d=len(v).bit_length()-1;rho=F(1,2**k);p=[a*a for a in fwht(v)]
 b=(d-1)*(1-p[j]) if j and not dead else F(0)
 V=(rho*b,rho*(1-rho)) if not dead else (F(0),F(0))
 if not order or mode==4 and depth==1:
  absorbed+=dead;return V,(F(0),F(0))
 i=order[0];nextorder=[a-(a>i) for a in order[1:]]
 children=[]
 if dead:
  # Exact-law absorption leaves zero reference potential and zero later resets.
  return (F(0),F(0)),(F(0),F(0))
 if i<d:
  vv=[[z for x,z in enumerate(v) if x//2**i%2==y] for y in range(2)];jj=remove(j,i)
  for y in range(2):children.append(walk(vv[y],jj,k,nextorder,mode,depth+1))
  cp=[1-fwht(w)[jj]**2 for w in vv]
  ck(sum(cp)/2==1-p[j]-p[j^2**i])
  local=(rho*sum(cp)/2 if jj else F(0),F(0))
 elif i==d:
  absorbed+=2
  children=[((F(0),F(0)),(F(0),F(0)))]*2;local=(F(0),F(0))
 else:
  ck(k>=1)
  children=[walk(v,j,k-1,nextorder,mode,depth+1),((F(0),F(0)),(F(0),F(0)))];local=(F(0),rho*rho)
 terminal=tuple(sum(c[0][r] for c in children)/2 for r in range(2))
 spent=tuple(local[r]+sum(c[1][r] for c in children)/2 for r in range(2))
 for r in range(2):ck(spent[r]<=V[r]-terminal[r])
 return terminal,spent
for d in [1,2]:
 for code in range(2**(2**d)):
  v=[2*(code>>x&1)-1 for x in range(2**d)]
  for j in range(1,2**d):
   for k in range(3):
    data=list(range(d));guard=[d];ctrl=list(range(d+1,d+k+1))
    orders=[ctrl+data+guard,data+ctrl+guard,guard+data+ctrl,list(reversed(ctrl+data+guard)),list(range(d+k+1))]
    for mode,order in enumerate(orders):walk(v,j,k,order,mode);trees+=1

# A physical data query can INCREASE ghost mass; fixed initial-z pricing is unsafe here.
v=[(-1 if x&1 else 1)*((-1 if x>>1&1 else 1) if not x>>2&1 else 1) for x in range(8)]
def ghost_mass(v):
 p=[a*a for a in fwht(v)];q=[F(5,6)*a for a in p];q[0]=p[0];q[1]+=(1-p[0])/6
 return sum(q[i] for i in range(len(p)) if p[i]==0)
z0=ghost_mass(v);zc=[ghost_mass([t for x,t in enumerate(v) if x>>2&1==y]) for y in range(2)]
ck(z0==0);ck(zc==[F(1,6),F(0)]);ck(sum(zc)/2>z0)
(HERE/'out/GHOST_INCREASE.json').write_text(json.dumps({'status':'PASS','truth_table':v,'anchor_mask':1,'queried_coordinate':2,'root_ghost':str(z0),'child_ghosts':[str(x) for x in zc],'interpretation':'A048 fixed-z controls-first bank cannot be assumed invariant under data resets; its original theorem remains valid.'},indent=2)+'\n',encoding='utf-8')
# Positive rational series; independent ln2 atanh enclosure and rigorous tail.
R=24;series=sum((F(1,r*(2**(2*r-1)-1)) for r in range(1,R+1)),F(0))
t=F(1,2**(2*R+1));tail=F(4,3)*t/((R+1)*(1-t))
ln=sum((F(2,(2*m+1)*3**(2*m+1)) for m in range(40)),F(0))
lnerr=F(2,81*3**81*(1-F(1,9)))
lo=series/(2*(ln+lnerr));hi=(series+tail)/(2*ln)
ck(lo<hi<F(4,5));ck(F(56,81)<ln)
ck((1+F(1,14)+F(4,279))/(2*F(56,81))<F(4,5))
# Reduced actual parity-product ghost states; no large truth table is generated.
for T in range(1,9):
 z=1-F(5,6)**T;ck(0<z<1)
 for k in range(1,9):
  rho=F(1,2**k)
  ck((1-rho*z)/2>0);ck(F(1,2)**2-rho*rho*z*z/4>0)
  # Exact controller outcomes; O(rho*z) increases to O(rho) as T grows.
  ck(1-rho*rho*z*z>=1-rho*rho>0)
cert={'status':'PASS','series_terms':R,'series':str(series),'tail_upper':str(tail),'ln2_lower':str(ln),'ln2_upper':str(ln+lnerr),'gamma_lower':str(lo),'gamma_upper':str(hi),'gamma_display':str(float(lo)),'uniform_guard_allowance':'4/5','sharpness':'Analytic increasing actual parity-product ghost witnesses; no actual-cost lower bound for alternative protocols or FEI'}
(HERE/'out/GAMMA.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
result={'status':'PASS','trees':trees,'nodes':nodes,'assertions':checks,'guard_absorptions':absorbed,'seconds':time.monotonic()-start,'arithmetic':'Independent exact FWHT/Fraction tree surrogate and rational positive-series certificate','scope':'Whole-tree conservative rho*(1-rho) controller bank; exact W local identities independently tested in main checker'}
(HERE/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result));print('gamma certified',float(lo),float(hi))

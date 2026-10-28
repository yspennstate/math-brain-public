import arithmetic as ar
from arithmetic import F,ck,CE,H,add,sub,scale,marg,log2i
from pathlib import Path
import itertools,json,time
R=Path(__file__).resolve().parents[1];EPS=F(1,10**18)
def ga(a,b):return a[0]+b[0],a[1]+b[1]
def gn(a):return -a[0],-a[1]
def gs(a):return a[0]*a[0]+a[1]*a[1]
def spec(t):
 a=list(t);N=len(a);h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(i,i+h):a[j],a[j+h]=ga(a[j],a[j+h]),ga(a[j],gn(a[j+h]))
  h*=2
 return tuple(gs(x)/N**2 for x in a)
def res(t,i,z):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(z<<i)] for x in range(len(t)//2))
zero=(F(0),F(0));one=(F(1),F(0));u=(F(399,401),F(40,401));b0=(one,one,u,gn(u));b=b0+b0
ck(set(spec(b0))=={F(1,4)});ck(all(gs(x)==1 for x in b))
h=(one,zero,u,zero);q1=spec(h);ck(sum(q1)==F(1,2));q1m=marg(q1,1)
ratios=[q1m[s&1]/q1[s] for s in range(4) if q1[s]];ck(max(ratios)==401);ck(401>8)
c=list(b)
for x in [0,2]:c[x]=gn(c[x])
c=tuple(c);q=spec(c);ck(q[4:]==q1)
root=scale(H(q1),F(1,2));frontiers=queries=0
for pol in range(4):
 leaves=[(c,q,h,q1,[0,1,2],F(1,2),True,0)];rd=(F(0),F(0));rw=(F(0),F(0));ret=(F(0),F(0))
 for depth in range(4):
  live=(F(0),F(0))
  for t,qq,hh,qh,labs,w,isLive,j in leaves:
   ck(sum(spec(t))==1);ck(sum(qq)==1)
   if isLive:live=add(live,scale(CE(spec(hh),qh),w))
  error=sub(root,add(add(rd,rw),add(ret,live)));ck(abs(error[0])<EPS and abs(error[1])<EPS);ck(add(rd,rw)[1]<=root[1]+EPS);frontiers+=1
  if depth==3:break
  new=[]
  for t,qq,hh,qh,labs,w,isLive,j in leaves:
   if not labs or all(x==zero for x in hh):new.append((t,qq,hh,qh,labs,w,isLive,j));continue
   lab=min(labs) if pol==0 else max(labs) if pol==1 else 2 if pol==2 and 2 in labs else (2 if pol==3 and j>=1 and 2 in labs else min(labs))
   ix=labs.index(lab);qm=marg(qq,ix);labs2=labs[:ix]+labs[ix+1:]
   if isLive and lab!=2:
    qhm=marg(qh,ix);c0=CE(spec(res(hh,ix,0)),qhm);c1=CE(spec(res(hh,ix,1)),qhm);drop=sub(CE(spec(hh),qh),scale(add(c0,c1),F(1,2)));ck(drop[0]>=-EPS);rd=add(rd,scale(drop,w))
   if isLive and lab==2:
    pc=spec(hh);price=sub(CE(pc,qh),CE(pc,qm));ck(price[0]>=-EPS);rw=add(rw,scale(price,w));ret=add(ret,scale(CE(pc,qm),w))
   for z in [0,1]:
    h2=res(hh,ix,z) if isLive and lab!=2 else hh;q2=qhm if isLive and lab!=2 else qh
    new.append((res(t,ix,z),qm,h2,q2,labs2,w/2,isLive and lab!=2,j+1))
   queries+=1
  leaves=new
# Every frozen signed real mask and every partial physical restriction.
real_states=0
for signs in range(64):
 h=tuple(((F(-1) if signs>>x&1 else F(1)),F(0)) if x<6 else zero for x in range(8));q=spec(h);mass=sum(q);ck(mass==F(3,4))
 for state in itertools.product([-1,0,1],repeat=3):
  hh=h;qq=q;labs=[0,1,2]
  for lab,z in enumerate(state):
   if z>=0:
    ix=labs.index(lab);hh=res(hh,ix,z);qq=marg(qq,ix);labs.remove(lab)
  pp=spec(hh);parent=CE(pp,qq);ck(all(x<=mass for x in qq));ck(parent[0]>=-EPS)
  for ix in range(len(labs)):
   qm=marg(qq,ix);cp=scale(add(CE(spec(res(hh,ix,0)),qm),CE(spec(res(hh,ix,1)),qm)),F(1,2));ck(sub(parent,cp)[0]>=-EPS)
   # The physical homogeneous square-sum identity is checked independently of log arithmetic.
   p0=spec(res(hh,ix,0));p1=spec(res(hh,ix,1));ck(tuple((x+y)/2 for x,y in zip(p0,p1))==marg(pp,ix))
  real_states+=1
ck(real_states==1728);ck(spec((one,u))==(F(400,401),F(1,401)));ck(401>16)
result={'assertions':ar.checks,'complex_frontiers':frontiers,'complex_queries':queries,'signed_mask_states':real_states,'max_complex_rare_ratio':401,'integer_bound':8,'seconds':time.monotonic()-ar.start,'status':'PASS: real/complex homogeneous sector lemma; integer gap fails; binary clean-node extension fails'}
(R/'out/SCOPE.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))

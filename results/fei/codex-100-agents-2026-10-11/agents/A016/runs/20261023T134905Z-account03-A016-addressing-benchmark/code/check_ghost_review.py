from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
import helper as h
from fractions import Fraction as F
from itertools import product
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-start<60,'frozen runtime'
def coretruth(k,m):
 def fun(x):
  G=1
  for j in range(m):G*= -1 if ((x>>(1+k+3*j))&7)==0 else 1
  active=((x>>1)&((1<<k)-1))==0 and G==-1
  return 1 if active else (-1 if x&1 else 1)
 return [fun(x) for x in range(1<<(1+k+3*m))]
def restrict(truth,fixed):
 n=(len(truth)-1).bit_length();rem=[i for i in range(n) if i not in fixed];ans=[]
 for y in range(1<<len(rem)):
  x=sum(v<<i for i,v in fixed.items())+sum(((y>>j)&1)<<i for j,i in enumerate(rem));ans.append(truth[x])
 return ans,rem
def activation(vals,Q):
 n=(len(vals)-1).bit_length();full=[]
 for x in range(1<<(n+3)):
  u=x&((1<<n)-1);w=-1 if ((x>>n)&3)==0 else 1
  full.append(vals[u]*w if (x>>(n+2))&1 else 1)
 P=h.walsh(full);rows=[];selected=h.val(0);mass=F(0)
 for d in range(1<<(n+2)):
  pd=P.get(d,F(0))+P.get(d+(1<<(n+2)),F(0))
  qd=(Q.get(d&((1<<n)-1),F(0))/4+int(d==0))/2
  for e in [0,1]:
   t=d+(e<<(n+2));pp=P.get(t,F(0));cond=pp/pd if pd else F(1,2)
   rows.append((t,pp,qd*cond))
 return P,{t:q for t,p,q in rows},h.cehist([(1,p,q) for t,p,q in rows])
pilot='--pilot' in sys.argv
fixtures=[(1,2)] if pilot else [(1,2),(2,2),(1,3)]
out=[];lam=h.add(h.scale(h.log(F(8,5)),F(1,2)),h.scale(h.log(F(4,3)),F(1,4)))
ck(lam[0]>F(3,8) and 75**2<2**13,'all-k strict ghost coefficient')
for k,m in fixtures:
 original=coretruth(k,m);P0=h.walsh(original);Q0={t:p/2 for t,p in P0.items()};Q0[0]=Q0.get(0,F(0))+F(1,2)
 rho=F(1,1<<k);mu=F(3,4)**m;p=rho*(1-mu)/2
 totalreach=F(0);mean4I=F(0);meanc=h.val(0);meansector=h.val(0);meanrelease=h.val(0);meanlogr=h.val(0);leaves=[]
 options=[([1],F(1,2),F(5,8),1),([0,1],F(1,4),F(3,4),1),([0,0,1],F(1,8),F(1),1),([0,0,0],F(1,8),F(1),-1)]
 for choices in product(options,repeat=m-1):
  fixed={};reach=F(1);r=F(1);phase=1
  for j,(bits,w,rr,ss) in enumerate(choices,1):
   for b,v in enumerate(bits):fixed[1+k+3*j+b]=v
   reach*=w;r*=rr;phase*=ss
  vals,rem=restrict(original,fixed);Q=h.project(Q0,rem);P,Qf,C=activation(vals,Q)
  live=[rem.index(1+k+b) for b in range(3)];selmask=sum(1<<i for i in live)
  sel=[(t,pp) for t,pp in P.items() if t&selmask]
  ck(sum(pp for t,pp in sel)==7*rho/64,'actual FULL active-sector mass')
  ck(all(pp==rho*rho/1024 and Qf[t]==rho*rho*r/2048 for t,pp in sel),'actual complete supported atom/ref values')
  sector=h.scale(h.sub(h.val(2*k+11),h.log(r)),7*rho/64)
  actualsector=h.add(*(h.scale(h.log(Qf[t]),-pp) for t,pp in sel))
  ck(not(actualsector[1]<sector[0] or actualsector[0]>sector[1]),'full sector cost reconstruction')
  # Independent physical core edges and actual activation formula.
  icore=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)) for j in range(len(rem))),len(vals))
  a=F(sum(vals),len(vals));fourI=2*icore+4-a
  ck(a==rho*(1-phase*F(3,4))/2,'signed actual event density')
  ck(fourI==6+3*rho/4+(2*k-3)*a,'full retained physical influence')
  # Clean only ghost coordinates; both actual children identical, so no physical reach loss.
  cleaned=dict(fixed)
  for i in rem:
   if i>=1+k+3:cleaned[i]=0
  cv,cr=restrict(original,cleaned);CQ=h.project(Q0,cr);_,_,CC=activation(cv,CQ)
  ghostcharge=h.scale(h.log(r),-7*rho/64)
  release=h.sub(C,CC)
  if r==1:ck(vals==cv and Q==CQ,'no ghost: literal probability/reference identity proves zero cleanup release')
  else:ck(release[0]>ghostcharge[1],'strict full cleanup release covers exact active-sector ghost charge')
  totalreach+=reach;mean4I+=reach*fourI;meanc=h.add(meanc,h.scale(C,reach));meansector=h.add(meansector,h.scale(sector,reach));meanrelease=h.add(meanrelease,h.scale(release,reach));meanlogr=h.add(meanlogr,h.scale(h.log(r),-reach))
  leaves.append({'physical_reach':str(reach),'r':str(r),'phase':phase,'CE':h.pack(C),'cleanup_CE':h.pack(CC),'cleanup_release':h.pack(release),'four_I':str(fourI)})
 ck(totalreach==1,'ALL short-circuit leaves retained, no overlap')
 expected=h.scale(lam,m-1);ck(not(meanlogr[1]<expected[0] or meanlogr[0]>expected[1]),'mean log ghost factor')
 ck((6+mean4I)/2==6+3*rho/8+(2*k-3)*p/2,'q0 and ALL q1 remaining physical influence')
 expectsector=h.scale(h.add(h.val(2*k+11),expected),7*rho/128)
 obssector=h.scale(meansector,F(1,2));ck(not(obssector[1]<expectsector[0] or obssector[0]>expectsector[1]),'exact whole-frontier active-sector leading coefficient')
 out.append({'k':k,'m':m,'q1_leaves':len(leaves),'all_q1_reach':str(totalreach),'global_four_I':str((6+mean4I)/2),'global_active_cost':h.pack(obssector),'leaves':leaves})
result={'status':'PASS','assertions':N,'helper_assertions':h.N,'seconds':time.perf_counter()-start,'fixtures':out,'lambda':h.pack(lam)}
(R/'out'/('GHOST_PILOT.json' if pilot else 'GHOST_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','assertions','helper_assertions','seconds']}))

from pathlib import Path
from fractions import Fraction as F
import importlib.util,itertools,json,time
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
p=OWN/'runs/20261023T105639Z-fleet03-A039-projection-under-restrictions/code/check.py';sp=importlib.util.spec_from_file_location('prior',p);M=importlib.util.module_from_spec(sp);sp.loader.exec_module(M);H=M.H
START=time.monotonic();N=0;fallback=0
def ck(x,s):
 global N
 N+=1
 assert x,s
 assert time.monotonic()-START<55,'frozen55s'
def qlaw(t):
 global fallback
 p=H.spectrum(t)
 if sum(a>0 for a in p)==1:return p
 choices=[i for i in range(1,len(p)) if p[i]]
 target=len(p)-1 if p[-1] else choices[0]
 if not p[-1]:fallback+=1
 q=[p[0]]+[F(5,6)*x for x in p[1:]];q[target]+=F(1,6)*(1-p[0])
 ck(sum(q)==1 and q[0]==p[0],'normalized matched-empty adaptive spike')
 ck(all((a>0)==(b>0) for a,b in zip(p,q)),'EXACT source support, no ghost atom')
 return q
def one(v,j):
 n=(len(v)-1).bit_length();p=H.spectrum(v);q=qlaw(v);V=1-p[0]
 t=M.selector(M.makecore([v,[1,-1]]));Q=H.lift(t,H.tensor([q,[F(0),F(1)]]))
 children,rr,pb,qb,ks=H.channel(t,Q,j+1);sigma=H.IV();fresh=H.IV();ev=F(0)
 for y,(ct,cp,old) in enumerate(children):
  vy=H.restrict(v,j,y);py=H.spectrum(vy);qy=qlaw(vy)
  nr=H.lift(ct,H.tensor([qy,[F(0),F(1)]]));ev+=(1-py[0])/2
  sigma+=(H.IV() if old==nr else H.KL(cp,nr)-H.KL(cp,old))*F(1,2)
  fresh+=H.KL(py,qy)*F(1,4)
 ck(sigma.hi<=fresh.hi,'full normalized conversion <=factor fresh KL')
 ck(fresh.hi<=(H.log2(F(6,5))*(ev/2)).hi,'fresh factor variance price')
 ck(V>=ev,'exact conditional variance contraction')
 ck(n*V-(n-1)*ev>=ev,'remaining-dimension variance bank pays next fresh bill')
 return {'remaining_dimension':n,'query':j,'variance':str(V),'mean_child_variance':str(ev),'sigma':sigma.json()}
original=[-1 if (x>>1)==0 or (x&1 and (x>>1)==3) else 1 for x in range(16)]
one(original,0)
rows=[]
for a in itertools.product([-1,0,1],repeat=4):
 v=original[:]
 for bit in range(3,-1,-1):
  if a[bit]!=-1:v=H.restrict(v,bit,a[bit])
 for j in range(a.count(-1)):rows.append({'restriction':a,'query_data':one(v,j)})
ck(len(rows)==108,'frozen exact physical domain')
ck(fallback>0,'source-zero-full support repair actually exercised')
out={'status':'PASS','cases':len(rows),'checks':N+M.EXTRA+H.CHECKS,'new_checks':N,'support_fallbacks':fallback,'runtime_seconds':time.monotonic()-START,'rows':rows,'external_review':'PENDING','full_FEI':'OPEN'}
(R/'out/PRIVATE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

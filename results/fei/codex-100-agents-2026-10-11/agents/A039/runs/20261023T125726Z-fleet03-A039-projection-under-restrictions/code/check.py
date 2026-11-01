"""Frozen partial-phase exact experiment, v1; no dimension escalation."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,sys
R=Path(__file__).resolve().parents[1]; OWN=R.parents[1]
p=OWN/'runs/20261023T105639Z-fleet03-A039-projection-under-restrictions/code/check.py'
s=importlib.util.spec_from_file_location('prior',p);M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
H=M.H; START=time.monotonic();N=0
def ck(x,label):
 global N
 N+=1
 assert x,label
 assert time.monotonic()-START<55,'frozen 55s guard'
def partial(w,k):
 return [(-1 if (x&((1<<k)-1)).bit_count()%2 else 1)*(-1 if x==0 else 1) for x in range(1<<w)]
def local(w,k,sp,eps,sign):
 v=partial(w,k);u=[1] if sp=='constant' else [1,-1]
 q=M.qlaw(v);qu=M.qlaw(u);p=H.spectrum(v);pu=H.spectrum(u)
 t=M.selector(M.signed(M.makecore([v,u]),sign),eps)
 P=H.spectrum(t);Q=H.lift(t,H.tensor([q,qu]));ll=H.ratios(q,p)
 B=[a*ll[(i>>1)&((1<<w)-1)] for i,a in enumerate(P)]
 children,r,pb,rb,ks=H.channel(t,Q,k+1);bb=H.erase(B,k+1)
 sigma=H.IV();fresh=H.IV()
 for y,(ct,cp,old) in enumerate(children):
  vy=H.restrict(v,k,y);qy=M.qlaw(vy)
  new=H.lift(ct,H.tensor([qy,qu]))
  sigma+=(H.IV() if old==new else H.KL(cp,new)-H.KL(cp,old))*F(1,2)
  fresh+=H.KL(H.spectrum(vy),qy)*F(1,4)
 rhs=fresh-H.KL(pb,bb)+H.KL([F(1,2)]*2,r)
 ck(max(sigma.lo,rhs.lo)<=min(sigma.hi,rhs.hi),'compensated identity interval consistency')
 ck(all(H.dot(bb,z)==rj for z,rj in zip(ks,r)),'exact spectator cancellation of outcome')
 inf=F(2,1<<w)
 ck(H.influence(v)-sum(H.influence(H.restrict(v,k,y)) for y in [0,1])/2==inf,'exact rare-coordinate influence')
 d=F(1,1<<w)
 if k<=w-2:
  A=F(1,2)+4*d*d;alpha=F(1,6);L=H.log2(F(6,5))
  gap=L*F(-1,4)+H.log2(1-2*alpha*d*d/A)*A+H.log2((2*alpha+(16-24*alpha)*d*d)/(alpha+(16-32*alpha)*d*d))*(4*d*d)
  bound=gap+H.log2(F(36,35))*F(1,2)
  ck(sigma.hi<0,'rare unphased reset nonpositive')
  ck(sigma.hi<=bound.hi,'analytic coarsened bound dominates actual reset')
  ck(bound.hi<0,'coarsened uniform certificate strictly negative')
 elif w==2:ck(sigma.hi<=0,'endpoint fresh KL zero / data processing')
 return {'w':w,'k':k,'spectator':sp,'epsilon':eps,'core_sign':sign,'sigma':sigma.json(),'reference_outcomes':list(map(str,r)),'query_influence':str(inf),'scope':'proved' if k<=w-2 or w==2 else 'boundary diagnostic'}
def main():
 pilot='--pilot' in sys.argv
 cases=[]
 for w in ([3] if pilot else range(2,7)):
  for k in ([1] if pilot else range(1,w)):
   for sp in (['constant'] if pilot else ['constant','character1']):
    for eps in [1,-1]:
     for sign in [1,-1]:cases.append(local(w,k,sp,eps,sign))
 certs={'L_gt_quarter':6**4>2*5**4,'ratio25over16_lt_two_thirds':25**3<4*16**3,'outcome_lt_one48':36**24<2*35**24,'initial_L0_lt_one5':8**5<2*7**5,'first_L_lt_11over40':6**40<2**11*5**40}
 ck(all(certs.values()),'integer-power log certificates')
 out={'status':'PASS','version':'A039-partial-phase-v1','pilot':pilot,'case_count':len(cases),'checks':N+M.EXTRA+H.CHECKS,'new_checks':N,'runtime_seconds':time.monotonic()-START,'integer_certificates':certs,'cases':cases,'full_FEI':'OPEN','external_review':'PENDING'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()

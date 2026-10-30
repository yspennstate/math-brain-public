from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,sys,time
HERE=Path(__file__).resolve().parents[1]
old=HERE.parents[1]/'runs/20261026T214918Z-fleet04-A039-projection-under-restrictions/code/check.py'
spec=importlib.util.spec_from_file_location('own_exact_log_helper',old);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x
 if checks%200==0 and time.monotonic()-start>55:raise TimeoutError('55s arithmetic guard')
def zero(w):ck(not w)
def le(w):ck(not w or h.bounds(w)[1]<=0)
def scale(c,w):return h.add((c,w))
def sparse(v,k):
 d=len(v).bit_length()-1
 return [v[x&((1<<d)-1)]*(-1 if x>>d&1 else 1) if x>>(d+1)==0 else 1 for x in range(1<<(d+1+k))]
def lift(q,k):
 d=len(q).bit_length()-1;rho=F(1,1<<k);out=[F(0)]*(1<<(d+k+1))
 for r in range(1<<k):
  out[r<<(d+1)]=(1-rho)**2 if r==0 else rho*rho
  for s,t in enumerate(q):out[(r<<(d+1))+(1<<d)+s]=rho*rho*t
 return out
def O(t):return scale(F(1,2),h.logword(1/(1-t*t)))
def W(k):return h.add(*[(F(1,1<<(k-j)),O(F(1,1<<j))) for j in range(1,k+1)])
def channel(p,q,pc,qc,i):
 pb=[F(0)]*(len(p)//2);qb=pb[:]
 for s in range(len(p)):pb[h.delete(s,i)]+=p[s];qb[h.delete(s,i)]+=q[s]
 ker=[[pc[y][t]/(2*pb[t]) if pb[t] else F(1,2) for t in range(len(pb))] for y in range(2)]
 r=[sum(qb[t]*ker[y][t] for t in range(len(pb))) for y in range(2)]
 ck(all(t>0 for t in r));ck(sum(r)==1)
 qi=[[qb[t]*ker[y][t]/r[y] for t in range(len(pb))] for y in range(2)]
 for y in range(2):ck(sum(qi[y])==sum(pc[y])==sum(qc[y])==1)
 K=h.kl(p,q);er=h.add((1,K),(-1,h.kl(pb,qb)));out=h.kl([F(1,2)]*2,r)
 inh=h.add(*[(F(1,2),h.kl(pc[y],qi[y])) for y in range(2)])
 fresh=h.add(*[(F(1,2),h.kl(pc[y],qc[y])) for y in range(2)])
 sigma=h.add((1,fresh),(-1,inh))
 zero(h.add((1,K),(-1,er),(-1,out),(-1,inh)))
 return er,out,sigma,r,fresh
def main():
 rows=data=ctrl=guard=ghost=0;pilot='--pilot' in sys.argv
 for d in range(1,2 if pilot else 3):
  for code in range(1<<(1<<d)):
   v=[2*((code>>x)&1)-1 for x in range(1<<d)];p=h.law(v)
   for j in range(1,1<<d):
    q=h.reference(p,j);z=sum(q[s] for s in range(len(p)) if not p[s]);ghost+=z>0
    B=F(d-1)*(1-p[j])
    for k in range(3):
     rho=F(1,1<<k);vF=sparse(v,k);pF=h.law(vF);qF=lift(q,k)
     ck(pF==lift(p,k));ck(sum(qF)==1)
     zero(h.add((1,h.kl(pF,qF)),(-rho,h.kl(p,q))))
     for i in range(d+1+k):
      rows+=1;pc=[h.law(h.restrict(vF,i,y)) for y in range(2)]
      bank=h.add((rho*B,h.ELL),(1,W(k)))
      if i<d:
       data+=1;vc=[h.restrict(v,i,y) for y in range(2)];pl=[h.law(t) for t in vc];jc=h.delete(j,i);ql=[h.reference(t,jc) for t in pl]
       qc=[lift(t,k) for t in ql];local=channel(p,q,pl,ql,i)
       er,out,sig,r,fresh=channel(pF,qF,pc,qc,i)
       zero(h.add((1,er),(-rho,local[0])))
       zero(h.add((1,sig),(-rho,local[2]),(-1,out),(rho,local[1])))
       ck(r==[(1-rho)/2+rho*t for t in local[3]])
       le(h.add((1,out),(-rho,local[1])))
       childB=sum(F(d-2)*(1-t[jc]) if jc else F(0) for t in pl)/2
       drop=scale(rho*(B-childB),h.ELL)
      elif i==d:
       guard+=1;qc=pc
       er,out,sig,r,fresh=channel(pF,qF,pc,qc,i);zero(fresh);le(sig);drop=bank
      else:
       ctrl+=1;qc=[lift(q,k-1),[F(1)]+[F(0)]*(len(pc[1])-1)]
       er,out,sig,r,fresh=channel(pF,qF,pc,qc,i)
       zero(er);ck(r==[(1-rho*z)/2,(1+rho*z)/2])
       zero(h.add((1,sig),(-1,O(rho*z))))
       drop=h.add((1,W(k)),(-F(1,2),W(k-1)))
       zero(h.add((1,drop),(-1,O(rho))))
      le(h.add((1,sig),(-1,drop)))
 result={'status':'PASS','rows':rows,'assertions':checks,'data_queries':data,'controller_queries':ctrl,'guard_queries':guard,'core_reference_ghost_fixtures':ghost,'seconds':time.monotonic()-start,'helper':'Own earlier exact arithmetic; no A048 producer import'}
 (HERE/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()

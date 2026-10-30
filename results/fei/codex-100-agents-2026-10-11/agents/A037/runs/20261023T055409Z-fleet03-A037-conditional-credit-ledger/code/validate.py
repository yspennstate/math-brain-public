from fractions import Fraction as F
from pathlib import Path
import sys,json,time
import exact as E
from reduced import local
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.perf_counter()-start<55
def KL(p,q):return E.kl(p,[E.iv(x) for x in q])
def point(w):return [1]*((1<<w)-1)+[-1]
def qfactor(t,alpha):
 p=E.law(t)
 if len(t)<=2 or abs(sum(t))==len(t):return p
 q=[p[0]]+[(1-alpha)*x for x in p[1:]];q[-1]+=alpha*(1-p[0]);ck(sum(q)==1);return q
def tensor(a,b):return [x*y for y in b for x in a]
def lift(v,u,epsilon,qv,qu):
 g=[a*b for b in u for a in v];t=[epsilon if not z&1 else g[z>>1] for z in range(2*len(g))]
 p=E.law(t);q=[F(0)]*len(t);q[0:2]=p[0:2];core=tensor(qv,qu)
 for s in range(1,len(core)):q[2*s]=q[2*s+1]=core[s]/4
 ck(sum(q)==1);ck(all((pp==0)==(qq==0) for pp,qq in zip(p,q)))
 return t,q
def step(t,q,i):
 p=E.law(t);ts=[E.restrict(t,i,y) for y in [0,1]];ps=[E.law(z) for z in ts]
 pp=[p[k]+p[k|(1<<i)] for k in range(len(p)) if not k>>i&1]
 qq=[q[k]+q[k|(1<<i)] for k in range(len(q)) if not k>>i&1]
 ck(pp==[(a+b)/2 for a,b in zip(*ps)])
 joint=[[qq[k]*(ps[y][k]/(2*pp[k]) if pp[k] else F(1,2)) for k in range(len(pp))] for y in [0,1]]
 outs=[sum(a) for a in joint];ck(sum(outs)==1);child=[[a/outs[y] for a in joint[y]] for y in [0,1]]
 ck(all(sum(a)==1 for a in child))
 loss=E.sub(KL(p,q),KL(pp,qq));out=KL([F(1,2)]*2,outs)
 old=E.scale(F(1,2),E.total(KL(a,b) for a,b in zip(ps,child)))
 ck(E.overlaps(KL(p,q),E.add(loss,E.add(out,old))))
 return ts,ps,child,outs,loss,out

def physical():
 rows=[];pilot='--pilot' in sys.argv
 specs=[('plus',[1]),('minus',[-1]),('char',[1,-1]),('point2',point(2)),('minuspoint2',[-x for x in point(2)])]
 if pilot:specs=[specs[0],specs[3]]
 for w in [2,3,4]:
  for name,u in specs:
   for epsilon in [1,-1]:
    for alpha in ([F(1,6)] if pilot else [F(1,6),F(1,5)]):
     v=point(w);qu=qfactor(u,F(1,3));t,q=lift(v,u,epsilon,qfactor(v,alpha),qu)
     ts,ps,old,outs,loss,out=step(t,q,1);first=E.iv(0);second=E.iv(0);terminal=E.iv(0)
     for y in [0,1]:
      vy=E.restrict(v,0,y);tt,new=lift(vy,u,epsilon,qfactor(vy,alpha),qu);ck(tt==ts[y])
      inc=E.sub(KL(ps[y],new),KL(ps[y],old[y]));first=E.add(first,E.scale(F(1,2),inc))
      tss,pss,olds,oo,ll,ot=step(tt,new,1);ss=E.iv(0)
      for z in [0,1]:
       vz=E.restrict(vy,0,z);ttt,nn=lift(vz,u,epsilon,qfactor(vz,alpha),qu);ck(ttt==tss[z])
       ss=E.add(ss,E.scale(F(1,2),E.sub(KL(pss[z],nn),KL(pss[z],olds[z]))))
      ck(ss[1]<0 or ss[0]<=0<=ss[1]);second=E.add(second,E.scale(F(1,2),ss))
     reduced,rr,*_=local(w,F(epsilon*sum(u),len(u)),1-alpha)
     ck(E.overlaps(first,reduced));ck(outs==rr);ck(first[1]<0)
     bound=E.scale(-F(308,255)*alpha*alpha/F(2**(2*w)),E.div(E.iv(1),E.LN2))
     if w>=3:ck(first[1]<=bound[0])
     rows.append({'w':w,'spectator':name,'epsilon':epsilon,'alpha':str(alpha),'sigma1':E.enc(first),'sigma2':E.enc(second),'reference_outcomes':list(map(str,outs))})
 return rows

def scalars():
 rows=[]
 for w in ([list(range(2,7)),list(range(7,12)),list(range(12,17)),list(range(17,21))][int(sys.argv[sys.argv.index("--block")+1])] if "--block" in sys.argv else range(2,21)):
  for alpha in [F(1,7),F(1,6),F(1,5),F(1,2),F(7,8)]:
   for mm in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    for sign in [1,-1]:
     mu=sign*mm;s,outs,*_=local(w,mu,1-alpha);ck(s[1]<0)
     eta=1-2*outs[0];d=F(1,2**w);ck(0<=eta<=4*alpha*d*d)
     if w>=3:
      bound=E.scale(-F(308,255)*alpha*alpha*d*d,E.div(E.iv(1),E.LN2));ck(s[1]<=bound[0])
     rows.append({'w':w,'alpha':str(alpha),'mu':str(mu),'sigma':E.enc(s)})
  E.logpoint.cache_clear()
 for mu in [F(0),F(1,2),F(1),F(-1)]:
  s,outs,*_=local(3,mu,F(1));ck(s[0]<=0<=s[1]);ck(outs==[F(1,2)]*2)
 return rows
if __name__=='__main__':
 rows=scalars() if '--scalar' in sys.argv else physical()
 summary={'status':'PASS','cases':len(rows),'assertions':checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'rows':rows}
 name=('SCALAR_'+sys.argv[sys.argv.index('--block')+1] if '--block' in sys.argv else 'SCALAR') if '--scalar' in sys.argv else ('PHYSICAL_PILOT' if '--pilot' in sys.argv else 'PHYSICAL')
 (R/'out'/f'{name}.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in summary.items() if k!='rows'}))

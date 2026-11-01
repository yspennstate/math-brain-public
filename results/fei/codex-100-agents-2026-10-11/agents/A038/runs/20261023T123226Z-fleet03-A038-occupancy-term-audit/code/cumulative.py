import json,sys,time
from pathlib import Path
from fractions import Fraction as F
import interval_primitives as m
import baseline as b
import postreset as p
R=Path(__file__).resolve().parents[1];V=m.V;start=time.monotonic();count=0
def ck(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55-second frozen watchdog')
def overlap(a,c,label):ck(a.a<=c.b and c.a<=a.b,label+' diagnostic only')
def norm(q):
 s=sum(q,V(0));ck(s.a>0,'positive reference own normalizer')
 return [x/s for x in q]
def stats(front):
 return sum((4*n['I']*w-n['H']*w for n,q,names,w in front),V(0))
def split(row,label):
 n,q,names,w=row;i=names.index(label);qn=norm(q);out=m.push(n,q,i)
 kids=[b.source(m.restrict(n['t'],i,s)) for s in range(2)]
 physical=m.push(n,[V(x) for x in n['p']],i)
 for s in range(2):
  for got,val in zip(physical[s],kids[s]['p']):ck(got.a==got.b==val/2,'physical common kernel exact')
 barp=[];barq=[];zero=0
 for j in range(len(q)):
  if j>>i&1:continue
  barp.append(n['p'][j]+n['p'][j|1<<i]);barq.append(qn[j]+qn[j|1<<i])
  if not barp[-1] and barq[-1].a>0:zero+=1
 K=m.kl(n['p'],qn);E=K-m.kl(barp,barq)
 mass=sum(q,V(0));O=m.kl([F(1,2)]*2,[sum(z,V(0))/mass for z in out])
 terminals=sum((m.kl(kids[s]['p'],norm(out[s]))/2 for s in range(2)),V(0))
 overlap(K,E+O+terminals,'complete KL chain with outcome normalization')
 rest=names[:i]+names[i+1:]
 return [(kids[s],out[s],rest,w/2) for s in range(2)],w*(E+O),int(O.a>0),zero
def reset(front):
 B=V(0);new=[]
 for n,q,names,w in front:
  qq=p.canonical(n);K=m.kl(n['p'],qq);B+=w*K;new.append((n,qq,names,w))
  ck(K.b<=F(7,8),'per-node full canonical terminal bill')
 ck(B.b<=F(7,32),'whole full reset bill')
 return new,B
def data(front,label,branch=False):
 new=[];release=V(0);posO=zero=0
 for row in front:
  # branch choice is an actual measurable truth-table-history decision:
  # after y0, the active point-defect branch is recognized by influence y1>0.
  lab=label
  if branch:
   n,q,names,w=row;lab='y1' if n['d'][names.index('y1')]>0 else 'z'
  kids,r,o,z=split(row,lab);new+=kids;release+=r;posO+=o;zero+=z
 oldK=sum((m.kl(n['p'],norm(q))*w for n,q,names,w in front),V(0))
 newK=sum((m.kl(n['p'],norm(q))*w for n,q,names,w in new),V(0))
 overlap(oldK,release+newK,'entire old current-reference bill retained')
 return new,{'old_K':oldK.out(),'release':release.out(),'terminal_K':newK.out(),'positive_outcome_nodes':posO,'reference_only_rows':zero}
def history(policy):
 N,q,A,c=p.root(4);names=['x','a','b','y0','y1','y2','y3','z']
 root=(N,q,names,F(1));bc,r,_,_=split(root,'b');untouched=[bc[0]]
 core,r2,_,_=split(bc[1],'x');front=untouched+core;S0=stats(front)
 preK=sum((m.kl(n['p'],norm(qq))*w for n,qq,nn,w in front),V(0))
 overlap(A,r+r2+preK,'all ORIGINAL source reference bills retained')
 L0=A+m.positive(S0-(4*N['I']-N['H']))
 overlap(L0,A,'b and x prefix neutral')
 first,B0=reset(core)
 lab1,lab2=[('y0','y1'),('z','y0'),('y0','z'),('y0','y1')][policy]
 first,ledger0=data(first,lab1);S1=stats(untouched+first);U1=m.positive(S1-S0)
 second,B1=reset(first);second,ledger1=data(second,lab2,policy==3)
 S2=stats(untouched+second);U2=m.positive(S2-S1)
 package=L0+U1+U2;remaining=S2-package-B0-B1-F(11,32)
 ck(S0.a>=2 and S1.a>=2 and S2.a>=2,'complete frontier surplus floors')
 ck(package.b<F(155,128),'cumulative source and positive-debit package')
 ck(remaining.a>F(1,128),'same original owner pays query AFTER second reset')
 ck(sum(w for n,qq,nn,w in untouched+second)==1,'both physical complementary branches retained')
 for n,qq,nn,w in untouched+second:ck(n['H'].b<=4*n['I'],'each terminal physical hereditary certificate')
 if policy==0:ck(U1.a>0 and U2.a>0 and B0.a>0 and B1.a>0,'two positive physical debits and BOTH positive full reset bills')
 if policy==1:
  net=m.positive(S2-S0);ck(U1.b==0 and U2.a>net.b,'down then up: cumulative debit STRICTLY exceeds net debit')
 if policy==2:ck(U1.a>0 and U2.b==0,'retain old positive debit despite subsequent decrease')
 return {'policy':policy,'queries':[lab1,lab2+(' or z by branch' if policy==3 else '')],'m':4,'A':A.out(),'L0':L0.out(),'S0':S0.out(),'S1':S1.out(),'S2':S2.out(),'U1_retained':U1.out(),'U2_after_second_reset':U2.out(),'B0_retained':B0.out(),'B1_retained':B1.out(),'omega':'11/32','cumulative_package':package.out(),'remaining':remaining.out(),'first_reference_ledger':ledger0,'second_reference_ledger':ledger1,'terminal_count':len(untouched+second)}
def scalar():
 rows=[];s={};H={};Q={1:V(0),2:V(0)}
 for k in range(1,17):
  e=F(1,2**k);p0=(1-2*e)**2
  H[k]=-(p0*m.lg(p0) if p0 else V(0))-(2**k-1)*4*e**2*m.lg(4*e**2)
  s[k]=8*k*e-H[k]
  if k>=2:
   d=s[k-1]/2-s[k]
   if k==2:ck(d.a==d.b==0,'k2 exact zero local increment')
   else:
    ck(d.a>0,'strict positive point increment k>=3')
    Q[k]=d+Q[k-1]/2
  target=H[k]-8*(k-1)*e
  overlap(Q[k],target,'Bellman telescoping identity')
  ck(Q[k].a>=0,'nonnegative attainable positive variation')
  if k>=3:
   envelope=2*m.h(F(1,4))+k*m.h(e/2)-1-2*(k-1)*e
   ck(envelope.b<F(155,128),'cumulative all-width package envelope on frozen domain')
  rows.append({'k':k,'H':H[k].out(),'surplus':s[k].out(),'Q':Q[k].out(),'telescoped':target.out()})
 return rows
if __name__=='__main__':
 scalars=scalar();policies=[0] if '--pilot' in sys.argv else list(range(4));histories=[history(i) for i in policies]
 out={'status':'PASS','assertions':count,'baseline_assertions':b.COUNT,'primitive_assertions':m.COUNT,'postreset_assertions':p.count,'runtime_seconds':time.monotonic()-start,'scalar_rows':scalars,'histories':histories,'identity_rung':'analytic exact KL chain and telescope; interval overlaps diagnostics only'}
 (R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps({k:out[k] for k in ['status','assertions','baseline_assertions','primitive_assertions','postreset_assertions','runtime_seconds']}))

from fractions import Fraction as F
from pathlib import Path
import json,sys,time
import exact as E
import review as C
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
 assert time.perf_counter()-start<55
L=E.logpoint(F(6,5));ghosts=0
def overlap(a,b):ck(E.overlaps(a,b))
def anchor(t,J):return C.ref(E.law(t),J)
def drop(J,i):return (J&((1<<i)-1))|((J>>(i+1))<<i)
def off(t,J):return 1-E.law(t)[J]
def local(t,J,i):
 global ghosts
 p=E.law(t);q=C.ref(p,J);ghosts+=sum(bool(qq) and not pp for pp,qq in zip(p,q));n=len(t).bit_length()-1;r=n-J.bit_count()
 ts,qs,out,O,er=C.step(t,q,i);Jc=drop(J,i);aa=off(t,J);ac=[off(v,Jc) for v in ts]
 b=F(E.fwht(t)[J|(1<<i)],len(t));ck(sum(ac)/2==aa-b*b)
 bd=r*aa-(r-1)*sum(ac)/2;ck(bd>=sum(ac)/2)
 fresh=[anchor(v,Jc) for v in ts]
 Ks=[C.KL(E.law(v),qq) for v,qq in zip(ts,fresh)]
 inh=[C.KL(E.law(v),qq) for v,qq in zip(ts,qs)]
 sig=E.scale(F(1,2),E.total(E.sub(a,b) for a,b in zip(Ks,inh)))
 bound=E.scale(bd,L);ck(sig[0]<=bound[1])
 rootK=C.KL(p,q);ck(rootK[0]<=E.scale(aa,L)[1])
 return ts,Jc,fresh,sig,E.add(O,er),qs
def tree(t,J,mode,path=()):
 n=len(t).bit_length()-1;eligible=[i for i in range(n) if not J>>i&1]
 if not eligible or (mode=='stop' and len(path)>=1 and path[-1]==0):
  p=E.law(t);H=E.entropy(p);I=sum((F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)),F(0))
  return E.iv(0),E.iv(0),C.KL(p,anchor(t,J)),H,I,off(t,J),1
 i=eligible[-1] if sum(path)%2 else eligible[0]
 ts,Jc,qs,sig,rel,_=local(t,J,i)
 children=[tree(v,Jc,mode,path+(y,)) for y,v in enumerate(ts)]
 avg=lambda j:E.scale(F(1,2),E.total(c[j] for c in children))
 return E.add(sig,avg(0)),E.add(rel,avg(1)),avg(2),avg(3),(children[0][4]+children[1][4])/2,(children[0][5]+children[1][5])/2,1+sum(c[6] for c in children)
def history(k,m,r,mode):
 t=C.core(k,m,r);p=E.law(t);J=1;qold=C.ref(p,len(p)-1);qnew=C.ref(p,J)
 old=C.KL(p,qold);new=C.KL(p,qnew);conv=E.sub(new,old);ck(p[J]>p[-1]);ck(conv[1]<0)
 sig,release,Kf,Hf,If,af,nodes=tree(t,J,mode)
 overlap(E.add(new,sig),E.add(release,Kf));ck(af<=off(t,J))
 inclusive=E.add(old,E.add(conv,sig));overlap(inclusive,E.add(new,sig))
 bound=E.scale((k+m)*off(t,J),L);ck(inclusive[0]<=bound[1])
 S=E.sub(E.iv(4*If),Hf);Hr=E.entropy(p);Ir=sum(E.marg(p));er=E.sub(E.sub(Hr,Hf),E.iv(4*(Ir-If)))
 argument=E.add(old,E.add(er,E.add(conv,sig)))
 plus=(max(F(0),argument[0]),max(F(0),argument[1]));recovery=E.sub(S,plus)
 margin=E.sub(E.sub(E.iv(4*Ir),Hr),inclusive)
 minimum=(min(S[0],margin[0]),min(S[1],margin[1]));overlap(recovery,minimum)
 return {'k':k,'m':m,'r':r,'mode':mode,'nodes':nodes,'old_K':E.enc(old),'conversion':E.enc(conv),'sigma_later':E.enc(sig),'actual_inclusive':E.enc(inclusive),'bank_bound':E.enc(bound),'outcome_plus_erasure':E.enc(release),'full_terminal_K':E.enc(Kf),'recovery':E.enc(recovery)}
def source(k,m,r):
 t=C.core(k,m,r);pd=E.law(t);qd=C.ref(pd,len(pd)-1)
 outer=[(1-2*((x>>2)&1)) if not x&1 else (t[x>>3] if x&2 else 1) for x in range(len(t)*8)]
 p=E.law(outer);q=p[:]
 for s in range(1,len(pd)):
  for c in range(4):q[(s<<3)|c]=qd[s]/16
 ck(sum(q)==1);overlap(C.KL(p,q),E.scale(F(1,4),C.KL(pd,qd)))
 ts,qs,out,O,er=C.step(outer,q,1);ck(out==[F(1,2)]*2);overlap(O,E.iv(0));overlap(er,E.iv(0))
 ls,rs,out,O,er=C.step(ts[1],qs[1],0);ck(out==[F(1,2)]*2);overlap(O,E.iv(0));overlap(er,E.iv(0))
 # The retained a coordinate is an actual dummy only in active x1.
 ck(all(ls[1][2*j]==ls[1][2*j+1] for j in range(len(t))))
 ck(all(rs[1][2*j+1]==0 for j in range(len(t))))
 ck(E.restrict(ls[1],0,0)==t);ck(rs[1][::2]==qd)
 return {'k':k,'m':m,'r':r,'initial_K':E.enc(C.KL(p,q)),'active_reach':'1/4','inherited_exact':True}
def main():
 pilot='--pilot' in sys.argv
 tables=range(16) if pilot else range(256);localcases=0
 for b in tables:
  t=[1-2*((b>>x)&1) for x in range(8)]
  for J in ([1] if pilot else range(1,8)):
   for i in range(3):
    if not J>>i&1:local(t,J,i);localcases+=1
 (R/'out/REPAIR_PROGRESS.json').write_text(json.dumps({'phase':'local queries complete','local_queries':localcases,'assertions':checks})+'\n',encoding='utf-8')
 histories=[]
 for m in ([2] if pilot else [2,4]):
  for r in ([0] if pilot else range(3)):
   for mode in ['full','stop']:
    histories.append(history(3,m,r,mode))
    (R/'out/REPAIR_PROGRESS.json').write_text(json.dumps({'phase':'histories','local_queries':localcases,'histories':histories,'assertions':checks},indent=2)+'\n',encoding='utf-8')
 sources=[source(3,2,0)] if pilot else [source(3,2,r) for r in range(3)]+[source(4,4,0)]
 ck(6**15<2**4*5**15)
 for N in [10,12,16,32,64,128,200,65536]:
  delta=F(1,1<<N);a=12*delta
  ck(a<F(1,2));ck(6*N*delta*F(4,15)<=F(1,64))
  ck(12*delta*(3*N+2)<=F(3,8));ck(3-a-F(3,32)>=F(741,256))
 ck(F(741,256)-F(1,64)-F(1,4)==F(673,256))
 result={'status':'PASS','local_queries':localcases,'histories':histories,'sources':sources,'reference_only_atoms_exercised':ghosts,'assertions':checks,'channel_assertions':C.checks,'interval_assertions':E.checks,'seconds':time.perf_counter()-start,'uniform_after_old_quarter_lower':'673/256'}
 (R/'out'/('REPAIR_PILOT.json' if pilot else 'REPAIR_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ['histories','sources']}))
if __name__=='__main__':main()

from pathlib import Path
from fractions import Fraction as F
import sys,time,json
import prior as p
e=p.e;R=Path(__file__).resolve().parents[1];MODE=p.MODE;start=time.monotonic();nodes=queries=resets=positive=0
def ck(x,msg=''):
 p.ck(x,msg)
 if time.monotonic()-start>(55 if MODE=='pilot' else 300):raise TimeoutError('stage21 frozen cap')
def split(Q,c):return tuple(sum(Q[c*t:c*t+c]) for t in range(len(Q)//c))
def mux(a,g,h):return tuple((g if a[u]==1 else h)[t] for t in range(len(g)) for u in range(len(a)))
def bern(k):return (1-k,k)
def account(a,g,h,ra,rg,rh,depth=0,path=(),policy=0):
 c=len(a);pa=p.spectrum(a);pg=p.spectrum(g);ph=p.spectrum(h);prob=F(sum(x==-1 for x in a),len(a));V=1-pa[0];gamma=F(sum(x!=y for x,y in zip(g,h)),len(g));eta=V*gamma
 q=tuple((1-prob)*x+prob*y for x,y in zip(pg,ph));r=tuple((1-prob)*x+prob*y for x,y in zip(rg,rh));P=p.spectrum(mux(a,g,h));ck(split(P,c)==q)
 W=e.add(e.scale(p.KL(pg,rg),1-prob),e.scale(p.KL(ph,rh),prob));Da=p.KL(pa,ra);Z=p.sub(W,p.KL(q,r));T=e.add(W,e.scale(Da,gamma));s=1-ra[0]
 Cvac=p.KL(bern(V),bern(s));S=e.add(Z,e.scale(Cvac,gamma));p.nn(Z);p.nn(S)
 J=(1-prob)*e.edges(g,range(len(g).bit_length()-1))+prob*e.edges(h,range(len(h).bit_length()-1));E=J/8+eta/2
 B=tuple(x/s for x in ra[1:]) if s else None
 # Keep the literal selected-root shape then controller query, followed by first odds in child0.
 eps=F(0) if depth==0 or (depth==1 and path==(1,)) else (F(1,16) if depth==1 else (F(0),F(1,32),F(1,16))[(depth+sum(path)+policy)%3])
 lam=F(1) if depth<2 else (F(1,2),F(1),F(2))[(depth+policy+sum(path))%3]
 out=[];star=[];C={};floorrows=0
 for t in range(len(q)):
  k=sum(P[c*t+1:c*t+c])/q[t] if q[t] else F(0)
  ell=k
  if q[t] and B is not None:
   ell=(1-eps)*k+eps/2 if t else lam*k/(1+(lam-1)*k)
   if ell!=k:floorrows+=1
  if q[t]:C=e.add(C,e.scale(p.KL(bern(k),bern(ell)),q[t]))
  for u in range(c):
   star.append(r[t]*((1-k) if u==0 else k*B[u-1] if B is not None else 0))
   out.append(r[t]*((1-ell) if u==0 else ell*B[u-1] if B is not None else 0))
 Q=tuple(out);Qstar=tuple(star);ck(sum(Q)==sum(Qstar)==1)
 p.eq(p.KL(P,Qstar),p.sub(T,S),'canonical source/controller interface')
 p.eq(p.KL(P,Q),e.add(p.sub(T,S),C),'actual full row-odds KL')
 p.nn(p.sub(p.const(E),C),'influence envelope');ck(sum(q[1:])<=J)
 ck(eta<=gamma*e.edges(a,range(c.bit_length()-1)))
 return {'a':a,'g':g,'h':h,'ra':ra,'rg':rg,'rh':rh,'P':P,'Q':Q,'Qstar':Qstar,'T':T,'S':S,'C':C,'E':E,'J':J,'eta':eta,'gamma':gamma,'changed':floorrows}
def descend(st,policy,depth=0,path=(),incoming=None):
 global nodes,queries,resets,positive
 nodes+=1;a,g,h=st['a'],st['g'],st['h'];ra,rg,rh=st['ra'],st['rg'],st['rh'];c=len(a);r=c.bit_length()-1;d=len(g).bit_length()-1
 if incoming is None:incoming=st['Qstar']
 raw=p.sub(p.CE(st['P'],st['Q']),p.CE(st['P'],incoming));resets+=1
 if e.enclosure(raw)[0]>0:positive+=1
 n=r+d
 stop=not n or (policy==5 and depth>2 and sum(path)%3==1)
 if stop:return {'payment':p.CE(st['P'],st['Q']),'raw':raw,'refund':{},'release':{},'leafslack':e.add(st['S'],p.const(st['E']),p.neg(st['C']))}
 if depth==0:j=0
 elif not r:j=0
 elif not d:j=(policy+depth)%r
 elif policy==0:j=r if depth%2 else 0
 elif policy==1:j=0 if depth%2 else r+d-1
 elif policy==2:j=r+d-1
 elif policy==3:j=r-1
 else:j=(depth+sum(path)+policy)%n
 vv,qq,rho=p.physical(mux(a,g,h),st['Q'],j);queries+=1
 if j<r:
  aa,rr,_=p.physical(a,ra,j);gg=[g,g];hh=[h,h];rgs=[rg,rg];rhs=[rh,rh]
 else:
  k=j-r;gg,rgs,_=p.physical(g,rg,k);hh,rhs,_=p.physical(h,rh,k);aa=[a,a];rr=[ra,ra]
 children=[account(aa[z],gg[z],hh[z],rr[z],rgs[z],rhs[z],depth+1,path+(z,),policy) for z in (0,1)]
 expected=(st['gamma']*F(e.walsh(a)[1<<j],len(a))**2/2) if j<r else F(sum(vv[0][i]!=vv[1][i] for i in range(len(vv[0]))),len(vv[0]))/8
 ck(st['E']-(children[0]['E']+children[1]['E'])/2==expected,'exact physical envelope release')
 base_release=p.sub(st['T'],p.avg(*(x['T'] for x in children)));p.nn(base_release)
 release=e.add(base_release,p.const(expected))
 dh=p.sub(e.entropy(st['P']),p.avg(*(e.entropy(p.spectrum(x)) for x in vv)))
 refund=p.sub(p.CE(st['P'],st['Q']),e.add(dh,p.avg(*(p.CE(p.spectrum(vv[z]),qq[z]) for z in (0,1)))))
 p.nn(refund,'CURRENT full output refund')
 cs=[descend(children[z],policy,depth+1,path+(z,),qq[z]) for z in (0,1)]
 pay=e.add(dh,p.avg(*(x['payment'] for x in cs)));rrr=e.add(raw,p.avg(*(x['raw'] for x in cs)));ref=e.add(refund,p.avg(*(x['refund'] for x in cs)))
 releases=e.add(release,p.avg(*(x['release'] for x in cs)));leaf=p.avg(*(x['leafslack'] for x in cs))
 p.eq(pay,e.add(p.CE(st['P'],incoming),rrr,p.neg(ref)),'raw physical/reconstruction ledger')
 p.eq(pay,e.add(e.entropy(st['P']),st['T'],p.const(st['E']),p.neg(releases),p.neg(leaf)),'single original energy envelope')
 return {'payment':pay,'raw':rrr,'refund':ref,'release':releases,'leafslack':leaf}
def guards():
 rows=[]
 for n in range(3,9):
  delta=F(1,1<<n);q=1-2*delta+2*delta*delta;k=delta*delta/q;ell=F(15,16)*k+F(1,32);lam=ell*(1-k)/(k*(1-ell));ck(lam>=F(49,19)>2)
  C=e.scale(p.KL(bern(k),bern(ell)),q);minimum=e.scale(p.KL(bern(k),bern(F(1,32))),q);E=(1+n*delta)/8+delta/2
  p.nn(p.sub(p.const(E),C));p.nn(p.sub(C,minimum))
  if n>=4:p.nn(p.sub(minimum,p.const(F(63,50176))));ck(F(63,50176)>F(1,1024))
  rows.append({'n':n,'q':str(q),'k':str(k),'effective_lambda':str(lam),'positive_cost_interval':p.bounds(C),'necessary_floor_cost_interval':p.bounds(minimum),'original_energy':str(E),'source_channel_image':'singleton true profile because alpha=rho'})
 return rows
def main():
 ck(16**8<2*15**8);rows=[]
 for m in ([1] if MODE=='pilot' else [1,2]):
  root,kids=p.instance(m);v,Q,W,Z=kids[1];g=tuple(v[8*t+3] for t in range(len(v)//8));h=tuple(v[8*t] for t in range(len(v)//8))
  # Reconstruct the inherited source references directly from original uniform source channels.
  og=tuple((-1 if (x&7)==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
  oh=tuple((-1 if (x&7).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(len(og)));un=(F(1,len(og)),)*len(og)
  _,rgs,_=p.physical(og,un,0);_,rhs,_=p.physical(oh,un,0)
  pa=p.spectrum(p.AA);V=1-pa[0];ra=(pa[0],)+tuple(V*x for x in p.prof(F(1,8)))
  C1=e.scale(p.KL(p.PI,p.prof(F(1,8))),F(45,64));p.nn(p.sub(p.const(F(1,128)),C1))
  for policy in (range(1) if MODE=='pilot' else range(6)):
   st=account(p.AA,g,h,ra,rgs[1],rhs[1],policy=policy);ck(st['J']==m+F(3,8));ck(st['E']==F(m,8)+F(51,128))
   p.eq(st['T'],e.add(W,C1));before=(nodes,queries,resets,positive);ans=descend(st,policy)
   p.nn(p.sub(e.add(e.entropy(st['P']),st['T'],p.const(st['E'])),ans['payment']))
   dh=p.sub(e.entropy(p.spectrum(root[0])),p.avg(*(e.entropy(p.spectrum(x[0])) for x in kids)))
   total=e.add(dh,p.avg(p.CE(p.spectrum(kids[0][0]),kids[0][1]),ans['payment']));reserve=p.sub(p.const(4*(m+F(29,16))-F(1,8)),total);lower=F(47*m,16)-F(133,64)
   p.nn(p.sub(reserve,p.const(lower)))
   rows.append({'m':m,'policy':policy,'nodes':nodes-before[0],'queries':queries-before[1],'resets':resets-before[2],'positive_raw_resets':positive-before[3],'reserve_interval':p.bounds(reserve),'proved_lower':str(lower)})
 guardrows=guards()
 out={'status':'PASS','mode':MODE,'assertions':p.count,'nodes':nodes,'queries':queries,'resets':resets,'positive_raw_resets':positive,'seconds':time.monotonic()-start,'rows':rows,'guards':guardrows}
 (R/'out'/('PILOT.json' if MODE=='pilot' else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','guards')}))
if __name__=='__main__':main()

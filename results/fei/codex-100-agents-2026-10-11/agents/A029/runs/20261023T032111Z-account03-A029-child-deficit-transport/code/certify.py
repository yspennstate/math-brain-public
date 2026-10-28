"""One genuine conditional-nonempty profile change, SAME inherited source slack."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import source_bridge as b
e=b.e;RUN=Path(__file__).resolve().parents[1];START=time.monotonic()
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
count=0
def ck(v):
 global count
 count+=1
 if not v:raise AssertionError(count)
def eq(x,y):ck(not e.add(x,e.scale(y,-1)))
def nn(x):ck(e.enclosure(x)[0]>=0)
def diff(x,y):return e.add(x,e.scale(y,-1))
def cst(x):return {2:F(x)} if x else {}
def enc(x):return {str(k):str(v) for k,v in x.items()}
def bounds(x):return [str(v) for v in e.enclosure(x)]

def instance(m):
 a=tuple(-1 if x<3 else 1 for x in range(8))
 g=tuple((-1 if x%8==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 h=tuple((-1 if (x%8).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 r=tuple(F(1,len(g)) for _ in g)
 return a,g,h,r,r

def profile_reset(args,theta):
 a,g,h,rg,rh=args;s=b.profile(*args);pf=b.spectrum(b.mux(a,g,h))
 pa=b.spectrum(a);V=1-pa[0];K=len(a)-1
 ck(V>0)
 A=tuple(x/V for x in pa[1:]);B=tuple((1-theta)*x+theta/F(K) for x in A)
 ck(sum(A)==sum(B)==1)
 gamma=F(sum(x!=y for x,y in zip(g,h)),len(g))
 C=e.scale(b.kl(A,B),V*gamma)
 p=s['p'];q=tuple((1-p)*x+p*y for x,y in zip(b.spectrum(g),b.spectrum(h)))
 r=tuple((1-p)*x+p*y for x,y in zip(rg,rh));new=[]
 for t,qt in enumerate(q):
  row=pf[t*len(a):(t+1)*len(a)]
  if qt:
   z=row[0]/qt;nonempty=sum(row[1:])/qt
   new.append(r[t]*z);new.extend(r[t]*nonempty*x for x in B)
  else:new.append(r[t]);new.extend(F(0) for _ in B)
 new=tuple(new);ck(sum(new)==1)
 eq(diff(b.kl(pf,new),s['D']),C)
 ck(all(not x or y>0 for x,y in zip(pf,new)))
 return new,C,A,B,s

def continuation(t,r,labels,policy,history=()):
 sD=b.kl(b.spectrum(t),r);sH=e.entropy(b.spectrum(t))
 stop=not labels or (policy==1 and len(history)>=3 and sum(history)%2==0) or (policy==2 and len(history)>=3)
 if stop:return dict(path={},terminal=e.add(sH,sD),refund={},nodes=0,leaves=1)
 i=0 if policy!=1 or sum(history)%2==0 else len(labels)-1
 rr,E,O,rho=b.physical(t,r,i)
 cs=[b.restrict(t,i,k) for k in (0,1)]
 delta=diff(sH,b.avg(*(e.entropy(b.spectrum(x)) for x in cs)));nn(delta)
 ret=[continuation(cs[k],rr[k],labels[:i]+labels[i+1:],policy,history+(k,)) for k in (0,1)]
 ans={key:b.avg(*(x[key] for x in ret)) for key in ('path','terminal','refund')}
 ans['path']=e.add(delta,ans['path']);ans['refund']=e.add(E,O,ans['refund'])
 ans['nodes']=1+sum(x['nodes'] for x in ret);ans['leaves']=sum(x['leaves'] for x in ret)
 eq(e.add(ans['path'],ans['terminal'],ans['refund']),e.add(sH,sD))
 return ans

def main():
 rows=[];histories=[]
 ms=[1] if MODE=='pilot' else [0,1,2,3,4]
 targets=[F(0),F(1,64),F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]
 for m in ms:
  args=instance(m);a,g,h,rg,rh=args;s=b.profile(*args);f=b.mux(a,g,h)
  I=e.stats(f)[3];ck(I==m+F(29,16))
  Rg,Eg,Og,rhog=b.physical(g,rg,0);Rh,Eh,Oh,rhoh=b.physical(h,rh,0)
  kids=[(a,b.restrict(g,0,k),b.restrict(h,0,k),Rg[k],Rh[k]) for k in (0,1)]
  ps=[b.profile(*v) for v in kids]
  Aroot=diff(s['W'],b.avg(*(x['W'] for x in ps)));nn(Aroot)
  inf,Eout,Oout,rhoout=b.physical(f,s['rf'],3)
  sigma=diff(b.avg(*(x['D'] for x in ps)),s['D'])
  raw=diff(b.avg(*(b.kl(b.spectrum(b.mux(*kids[k][:3])),ps[k]['rf']) for k in (0,1))),b.avg(*(b.kl(b.spectrum(b.mux(*kids[k][:3])),inf[k]) for k in (0,1))))
  eq(raw,e.add(sigma,Eout,Oout))
  M=1<<(m+2);beta=F(40*M,55*M-36)
  Zformula=e.scale(b.kl((F(20,23),F(3,23)),(beta,1-beta)),F(23,32))
  eq(ps[1]['Z'],Zformula)
  if m==0:eq(ps[1]['Z'],{})
  else:
   nn(diff(ps[1]['Z'],cst(F(1,64))))
   ck(all(len(set(t))==2 for ar in kids for t in ar[1:3]))
  for theta in targets:
   new,C,AA,BB,child=profile_reset(kids[1],theta)
   ck(sorted(AA)==[F(1,15)]*6+[F(3,5)])
   ck((not theta) or AA!=BB)
   eligible=e.enclosure(diff(child['Z'],C))[0]>=0
   if m>=1 and theta<=F(1,8):ck(eligible)
   if m==0 and theta>0:ck(not eligible);ck(e.enclosure(C)[0]>0)
   if theta==F(1,8):
    Cformula=e.scale(e.add(e.scale(e.lg(F(21,19)),F(3,5)),e.scale(e.lg(F(7,8)),F(2,5))),F(45,64))
    eq(C,Cformula);nn(diff(cst(F(1,128)),C))
   rows.append(dict(m=m,theta=str(theta),Z=enc(child['Z']),C=enc(C),eligible=eligible,remaining=enc(diff(child['Z'],C)),remaining_bounds=bounds(diff(child['Z'],C)),source_branch_masses_g=[str(v) for v in rhog],source_branch_masses_h=[str(v) for v in rhoh],output_branch_masses=[str(v) for v in rhoout]))
   if MODE=='full' and m in (1,2) and theta==F(1,8):
    labels=('C0','C1','C2','D1','D2')+tuple('Z'+str(i) for i in range(m))
    delta=diff(s['H'],b.avg(*(x['H'] for x in ps)));nn(delta)
    for policy in range(3):
     rs=[continuation(b.mux(*kids[k][:3]),ps[k]['rf'] if k==0 else new,labels,policy) for k in (0,1)]
     payment=e.add(delta,b.avg(*(e.add(x['path'],x['terminal']) for x in rs)))
     fullrhs=e.add(s['H'],s['W'],e.scale(Aroot,-1),e.scale(b.avg(ps[0]['Z'],diff(ps[1]['Z'],C)),-1),e.scale(b.avg(*(x['refund'] for x in rs)),-1))
     eq(payment,fullrhs)
     U=4*I;old=F(1,8);reserve=diff(cst(U-old),payment)
     lower=3*m-F(15,8)+F(1,256);nn(diff(reserve,cst(lower)))
     histories.append(dict(m=m,policy=policy,nodes=1+sum(x['nodes'] for x in rs),leaves=sum(x['leaves'] for x in rs),payment=enc(payment),unused_original_quota=enc(reserve),unused_bounds=bounds(reserve),original_U=str(U),old_debit=str(old),lower_bound=str(lower),old_raw_reset=enc(raw),old_net_sigma=enc(sigma),E_output=enc(Eout),O_output=enc(Oout),source_contraction=enc(Aroot),both_terminal_CE=b.encoded(b.avg(*(x['terminal'] for x in rs)))))
  if time.monotonic()-START>(55 if MODE=='pilot' else 180):raise RuntimeError('frozen time limit')
 result=dict(status='PASS',mode=MODE,parameter_cases=len(rows),assertions=count,source_bridge_assertions=b.checks,seconds=round(time.monotonic()-START,6),rows=rows,histories=histories)
 (RUN/'out'/('pilot.json' if MODE=='pilot' else 'main.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','histories')}))
if __name__=='__main__':main()

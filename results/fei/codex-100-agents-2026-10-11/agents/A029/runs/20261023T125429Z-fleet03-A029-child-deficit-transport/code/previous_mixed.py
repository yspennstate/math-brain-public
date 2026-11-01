"""Actual first profile debit, CONTROL exposure, then genuine row-odds change."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time
import prior_adapter as c
b=c.b;e=c.e;R=Path(__file__).resolve().parents[1];START=time.monotonic()
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
checks=0
def ck(v,msg=''):
 global checks
 checks+=1
 if not v:raise AssertionError((checks,msg))
def sub(x,y):return e.add(x,e.scale(y,-1))
def eq(x,y,msg=''):ck(not sub(x,y),msg)
def const(q):return {2:F(q)} if q else {}
def nn(x,msg=''):ck(e.enclosure(x)[0]>=0,(msg,x,e.enclosure(x)))
def enc(x):return {str(k):str(v) for k,v in x.items()}

def shaped(args,ra):
 a,g,h,rg,rh=args;s=b.profile(*args);pa=b.spectrum(a)
 V=1-pa[0];beta=1-ra[0];gamma=F(sum(x!=y for x,y in zip(g,h)),len(g))
 Da=b.kl(pa,ra);vac=b.kl((1-V,V),(1-beta,beta))
 shape=b.kl(tuple(v/V for v in pa[1:]),tuple(v/beta for v in ra[1:])) if V else {}
 eq(Da,e.add(vac,e.scale(shape,V)),'vacuum chain')
 qref=[];na=len(a)
 for t in range(len(g)):
  row=s['rf'][t*na:(t+1)*na];mass=sum(row[1:])
  qref.append(row[0]);qref.extend(mass*v/beta if beta else F(0) for v in ra[1:])
 Q=tuple(qref);D=b.kl(b.spectrum(b.mux(a,g,h)),Q)
 T=e.add(s['W'],e.scale(Da,gamma));S=e.add(s['Z'],e.scale(vac,gamma))
 eq(D,sub(T,S),'T-S');eq(D,e.add(s['D'],e.scale(shape,V*gamma)),'shape charge')
 nn(S);nn(vac)
 return dict(Q=Q,D=D,T=T,S=S,Da=Da,vac=vac,base=s)

def odds(args,Q,epsilon):
 a,g,h,rg,rh=args;pf=b.spectrum(b.mux(a,g,h));na=len(a)
 out=[];C={};rows=[]
 for t in range(len(g)):
  p=pf[t*na:(t+1)*na];row=Q[t*na:(t+1)*na];q=sum(p);r=sum(row)
  if q:
   k=sum(p[1:])/q;ell=(1-epsilon)*k+epsilon/2
   non=sum(row[1:]);ck(non>0 if k else True)
   B=tuple(v/non for v in row[1:]) if non else tuple(F(1,na-1) for _ in row[1:])
   out.append(r*(1-ell));out.extend(r*ell*v for v in B)
   C=e.add(C,e.scale(b.kl((1-k,k),(1-ell,ell)),q));rows.append((q,k,ell))
  else:out.extend(row)
 out=tuple(out);ck(sum(out)==1)
 eq(sub(b.kl(pf,out),b.kl(pf,Q)),C,'odds exact charge')
 return out,C,rows

def one(m,epsilon,history=False):
 args=c.instance(m);a,g,h,rg,rh=args;root=b.profile(*args);f=b.mux(a,g,h)
 pa=b.spectrum(a);V=1-pa[0];A=tuple(v/V for v in pa[1:]);B=tuple(F(7,8)*v+F(1,56) for v in A)
 ra=(pa[0],)+tuple(V*v for v in B)  # declared before either physical query
 rgg,Eg,Og,rhog=b.physical(g,rg,0);rhh,Eh,Oh,rhoh=b.physical(h,rh,0)
 data=[(a,b.restrict(g,0,k),b.restrict(h,0,k),rgg[k],rhh[k]) for k in (0,1)]
 ds=[b.profile(*v) for v in data]
 A0=sub(root['W'],b.avg(*(x['W'] for x in ds)));nn(A0)
 current,C1,_,_,_=c.profile_reset(data[1],F(1,8))
 first=shaped(data[1],ra);ck(current==first['Q']);eq(sub(first['T'],ds[1]['W']),C1)
 nn(sub(const(F(1,128)),C1))
 raa,Ea,Oa,rhoa=b.physical(a,ra,0)
 control=[(b.restrict(a,0,k),)+data[1][1:] for k in (0,1)]
 cs=[shaped(control[k],raa[k]) for k in (0,1)]
 Ac=sub(first['T'],b.avg(*(x['T'] for x in cs)))
 eq(Ac,e.scale(e.add(Ea,Oa),F(3,4)),'actual controller source release');nn(Ac)
 outrefs,Ef,Of,rhof=b.physical(b.mux(*data[1][:3]),current,0)
 Dinh=[b.kl(b.spectrum(b.mux(*control[k][:3])),outrefs[k]) for k in (0,1)]
 raw=sub(b.avg(*(x['D'] for x in cs)),b.avg(*Dinh))
 sigma=sub(b.avg(*(x['D'] for x in cs)),first['D'])
 eq(raw,e.add(sigma,Ef,Of),'actual current-output reset/refund')
 eq(sigma,sub(sub(first['S'],b.avg(*(x['S'] for x in cs))),Ac))
 M=1<<(m+2);beta=F(8*M,13*M-12)
 formula=e.scale(b.kl((F(4,5),F(1,5)),(beta,1-beta)),F(5,8))
 eq(cs[0]['base']['Z'],formula,'inherited posterior formula')
 new,C,rows=odds(control[0],cs[0]['Q'],epsilon)
 Cformula=e.scale(b.kl((F(9,10),F(1,10)),(F(9,10)-F(2,5)*epsilon,F(1,10)+F(2,5)*epsilon)),F(5,8))
 eq(C,Cformula,'odds scalar formula');nn(C)
 ck(sorted((q,k) for q,k,ell in rows)==[(F(1,8),F(1,2))]*3+[(F(5,8),F(9,10))])
 delta0=sub(root['H'],b.avg(*(x['H'] for x in ds)))
 deltac=sub(ds[1]['H'],b.avg(*(x['base']['H'] for x in cs)))
 terminals=[e.add(ds[0]['H'],ds[0]['D']),e.add(cs[0]['base']['H'],cs[0]['D'],C),e.add(cs[1]['base']['H'],cs[1]['D'])]
 payment=e.add(delta0,e.scale(deltac,F(1,2)),e.scale(terminals[0],F(1,2)),e.scale(e.add(terminals[1],terminals[2]),F(1,4)))
 rhs=e.add(root['H'],root['W'],e.scale(A0,-1),e.scale(ds[0]['Z'],-F(1,2)),e.scale(C1,F(1,2)),e.scale(Ac,-F(1,2)),e.scale(e.add(sub(cs[0]['S'],C),cs[1]['S']),-F(1,4)))
 eq(payment,rhs,'full three-terminal bill, first C1 ONCE')
 margin=sub(b.avg(sub(cs[0]['S'],C),cs[1]['S']),C1)
 I=e.stats(f)[3];ck(I==m+F(29,16));reserve=sub(const(4*I-F(1,8)),payment)
 if m and epsilon<=F(1,16):
  nn(sub(formula,const(F(1,48))));nn(sub(const(F(1,256)),C));nn(sub(margin,const(F(1,1536))))
  nn(sub(reserve,const(3*m-F(15,8)+F(1,3072))))
  ck(all(len(set(t))==2 for ar in control for t in ar[:3]))
 if not m:eq(formula,{})
 if epsilon:ck(e.enclosure(C)[0]>0)
 hist=[]
 if history:
  fronts=[(b.mux(*data[0][:3]),ds[0]['rf']),(b.mux(*control[0][:3]),new),(b.mux(*control[1][:3]),cs[1]['Q'])]
  for policy in range(3):
   traces=[c.continuation(t,r,tuple(range((len(t)).bit_length()-1)),policy) for t,r in fronts]
   weights=(F(1,2),F(1,4),F(1,4))
   path=e.add(delta0,e.scale(deltac,F(1,2)))
   term={};refund={}
   for w,tr in zip(weights,traces):
    path=e.add(path,e.scale(tr['path'],w));term=e.add(term,e.scale(tr['terminal'],w));refund=e.add(refund,e.scale(tr['refund'],w))
   paid=e.add(path,term);eq(e.add(paid,refund),payment,'CURRENT odds reference full continuation')
   nn(sub(sub(const(4*I-F(1,8)),paid),const(3*m-F(15,8)+F(1,3072))))
   hist.append(dict(m=m,policy=policy,nodes=2+sum(tr['nodes'] for tr in traces),leaves=sum(tr['leaves'] for tr in traces),paid=enc(paid),terminal=enc(term),refund=enc(refund)))
 return dict(m=m,epsilon=str(epsilon),first_C1=enc(C1),odds_C=enc(C),selected_Z=enc(formula),selected_S=enc(cs[0]['S']),account_margin=enc(margin),payment=enc(payment),reserve=enc(reserve),controller_rho=[str(v) for v in rhoa],actual_output_rho=[str(v) for v in rhof],raw_control_reset=enc(raw),control_net_sigma=enc(sigma),control_output_refunds=enc(e.add(Ef,Of)),source_release=enc(Ac)),hist

def main():
 rows=[];hist=[]
 for m in ([1] if MODE=='pilot' else range(5)):
  for eps in map(F,('0','1/64','1/32','1/16','1/8','1/4','1')):
   row,hh=one(m,eps,MODE=='full' and m in (1,2) and eps==F(1,16));rows.append(row);hist+=hh
   if time.monotonic()-START>(55 if MODE=='pilot' else 180):raise TimeoutError('frozen cap')
 result=dict(status='PASS',mode=MODE,cases=len(rows),assertions=checks,bridge_assertions=b.checks,prior_adapter_assertions=c.count,seconds=round(time.monotonic()-START,6),rows=rows,histories=hist)
 (R/'out'/('pilot.json' if MODE=='pilot' else 'main.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('rows','histories')}))
if __name__=='__main__':main()

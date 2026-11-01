"""Independent direct-edge and weighted-suffix audit; no source-author code."""
import arithmetic as a
from fractions import Fraction as F
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();CHECKS=0
def ck(p):
 global CHECKS
 assert p
 CHECKS+=1
def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def parameters(s,L,R,T,Ig):
 alpha=F(1,2**s);q=F(1,2**R);r=F(1,2**T);eta=F(1,2**(L+R+T));e=q+r-q*r-eta
 JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);JD=JB+JC;pi=eta+alpha*e
 # ceil(log2(min(R,T)+2)) by exact integer arithmetic.
 m=(min(R,T)+1).bit_length()+2
 Is=s*alpha*e;Io=(1-alpha)*JB+alpha*JC;It=pi*Ig
 return {'alpha':alpha,'eta':eta,'e':e,'JB':JB,'JC':JC,'JD':JD,'pi':pi,'m':m,'Is':Is,'Io':Io,'It':It,'I':Is+Io+It}
def cost(j,p,Ig):return F(1,2**j)*(p['JD']+(j-1)*p['e']+p['e']*Ig)
def suffix(j,p,Ig):
 # Definition from distinct reached layers, independently of the closed form.
 return sum((F(1,2**(j-ell))*cost(ell,p,Ig) for ell in range(1,min(j,p['m'])+1)),F(0))
def closed(j,p,Ig):
 M=min(j,p['m']);return F(1,2**j)*(M*p['JD']+p['e']*M*(M-1)/2+M*p['e']*Ig)
def coordinate_owners(s,L,R,T,Ig,p):
 M=min(s,p['m']);alpha=p['alpha'];eta=p['eta'];q=F(1,2**R);r=F(1,2**T)
 # Per physical coordinate, not a separately opened account per event.
 owners=[('W',L,(1-alpha)*eta,M*alpha*eta),
         ('U',R,(1-alpha)*eta+alpha*q*(1-r),M*alpha*(eta+q*(1-r))),
         ('V',T,(1-alpha)*eta+alpha*r*(1-q),M*alpha*(eta+r*(1-q))),
         ('core aggregate',1,p['pi']*Ig,M*alpha*p['e']*Ig)]
 owners += [('S remaining-index '+str(ell),1,alpha*p['e'],max(M-ell,0)*alpha*p['e']) for ell in range(1,s+1)]
 ck(sum(count*owned for name,count,physical,owned in owners)==closed(s,p,Ig))
 ck(sum(count*physical for name,count,physical,owned in owners)==p['I'])
 for name,count,physical,owned in owners:ck(owned<=M*physical)
 return owners
def make(s,L,R,T,g):
 n=s+L+R+T;A=[]
 for x in range(1<<n):
  off=0;points=[]
  for w in [s,L,R,T]:points.append((x>>off)&((1<<w)-1)==(1<<w)-1);off+=w
  S,W,U,V=points;A.append(int((W and U and V) or (S and (U or V))))
 return tuple(g[x>>n] if A[x&((1<<n)-1)] else 1 for x in range((1<<n)*len(g))),tuple(A),n
def physical(case):
 s,L,R,T,kind,k=case;g=a.core(kind,k);v,A,n=make(s,L,R,T,g);a.spectrum.cache_clear();P,ds,H,TC,W=a.spectrum(v);_,gd,gH,_,_=a.spectrum(g);Ig=sum(gd)
 p=parameters(s,L,R,T,Ig);ck(sum(g)==0);ck(F(sum(A),len(A))==p['pi'])
 ck(sum(ds[:s])==p['Is']);ck(sum(ds[s:n])==p['Io']);ck(sum(ds[n:])==p['It']);ck(sum(ds)==p['I'])
 totals={q:{} for q in ['B','JS','J','Gamma']};removed=F(0);Qbad=F(0);Qsep=F(0);Qall=F(0);leafQ=F(0);leafH={};leafTC={};leafI=F(0);active=F(0);nodes=[]
 def walk(v,labels,reach):
  nonlocal removed,Qbad,Qsep,Qall,leafQ,leafH,leafTC,leafI,active
  P,ds,H,TC,W=a.spectrum(v);chosen=next((z for z in range(n) if z in labels and ds[labels.index(z)]),None)
  if chosen is None:
   leafI+=reach*sum(ds);leafH=a.add((1,leafH),(reach,H));leafTC=a.add((1,leafTC),(reach,TC));leafQ+=reach*a.odd_faces(v)
   if len(set(v))>1:active+=reach
   return
  i=labels.index(chosen);v0,v1=a.halves(v,i);p0,d0,H0,TC0,_=a.spectrum(v0);p1,d1,H1,TC1,_=a.spectrum(v1)
  packet=tuple(P[z]+P[z|(1<<i)] for z in range(len(P)) if not(z>>i&1));HP=a.ent(packet)
  B=a.add((1,H),(-1,HP));JS=a.add((1,HP),(-F(1,2),H0),(-F(1,2),H1));J=a.add((1,a.h(ds[i])),(-1,B))
  Gamma=a.add(*[(1,a.h((x+y)/2)) for x,y in zip(d0,d1)],*[(-F(1,2),a.h(x)) for x in d0+d1])
  ck(not a.add((1,TC),(-1,J),(1,JS),(-1,Gamma),(-F(1,2),TC0),(-F(1,2),TC1)))
  ck(sum(ds)==ds[i]+(sum(d0)+sum(d1))/2)
  face=sum(a.infs(tuple(x*y for x,y in zip(v0,v1))))/2
  sign=a.add((1,B),(-4*ds[i],{2:F(1)}));lo,hi=a.bounds(sign);ck(not sign or hi<0 or lo>0);bad=lo>0
  if chosen<s:
   j=s-chosen;ck(reach==F(1,2**(s-j)));ck(ds[i]==F(1,2**j)*p['e']);ck(face==cost(j,p,Ig))
   V=suffix(j,p,Ig);drift=V-suffix(j-1,p,Ig)/2
   ck(V==closed(j,p,Ig));ck(drift==(face if j<=p['m'] else 0));ck(not bad or j<=p['m'])
   if bad:Qsep+=reach*face
  else:ck(not bad)
  removed+=reach*ds[i];Qall+=reach*face
  if bad:Qbad+=reach*face
  for z,val in [('B',B),('JS',JS),('J',J),('Gamma',Gamma)]:totals[z]=a.add((1,totals[z]),(reach,val))
  nodes.append({'coordinate':chosen,'reach':str(reach),'d':str(ds[i]),'face':str(face),'separator':chosen<s,'bad':bad,'B_minus_4d':a.packed(sign)})
  labs=labels[:i]+labels[i+1:];walk(v0,labs,reach/2);walk(v1,labs,reach/2)
 walk(v,tuple(range(len(ds))),F(1))
 ck(removed==p['Is']+p['Io']);ck(leafI==p['It']);ck(active==p['pi']);ck(not a.add((1,leafH),(-p['pi'],gH)))
 ck(not a.add((1,H),(-1,leafH),(-1,totals['B']),(-1,totals['JS'])))
 ck(not a.add((1,totals['J']),(1,totals['Gamma']),(1,leafTC),(-1,TC),(-1,totals['JS'])))
 ck(Qbad==Qsep);ck(Qsep<=suffix(s,p,Ig));ck(Qall+leafQ==a.odd_faces(v))
 return {'case':list(case),'dimension':len(ds),'I':str(p['I']),'I_separator':str(p['Is']),'I_other':str(p['Io']),'I_terminal':str(p['It']),'terminal_entropy':a.packed(leafH),'root_entropy':a.packed(H),'Q_bad':str(Qbad),'reserve':str(suffix(s,p,Ig)),'nodes':nodes}
def accounts():
 rows=[];drifts=0
 for s in range(1,11):
  for L in range(1,5):
   for R in range(1,5):
    for T in range(1,5):
     for Ig in [F(1),F(5,2),F(10)]:
      p=parameters(s,L,R,T,Ig);V=suffix(s,p,Ig);M=min(s,p['m'])
      ck(p['e']>=max(F(1,2**R),F(1,2**T)))
      for j in range(1,s+1):
       ck(suffix(j,p,Ig)==closed(j,p,Ig));drift=suffix(j,p,Ig)-suffix(j-1,p,Ig)/2
       ck(drift==(cost(j,p,Ig) if j<=p['m'] else 0));drifts+=1
      ck(V<=M*p['Io']+F(M-1,2)*p['Is']+M*p['It']);ck(V<=M*p['I'])
      ck(V==sum((F(1,2**(s-j))*cost(j,p,Ig) for j in range(1,min(s,p['m'])+1)),F(0)))
      coordinate_owners(s,L,R,T,Ig,p)
      rows.append({'s':s,'L':L,'R':R,'T':T,'Ig':str(Ig),'m':p['m'],'reserve':str(V),'I':str(p['I'])})
 dump(ROOT/'out/ACCOUNTS.json',{'status':'PASS','cases':len(rows),'drift_identities':drifts,'checks':CHECKS,'rows':rows})
 print(json.dumps({'accounts':'PASS','cases':len(rows),'drifts':drifts,'checks':CHECKS,'seconds':time.monotonic()-START}))
def obstruction():
 rows=[]
 for h in [2,3,4,6,8,10]:
  w=2**h-2;m=h+2;s=2*m;L=4*m;p=parameters(s,L,w,w,F(1));V=suffix(s,p,F(1));ratio=V/p['I']
  ck(p['m']==m);ck(V==closed(s,p,F(1)))
  owners=coordinate_owners(s,L,w,w,F(1),p)
  # Explicit all-integer bounds used in the proof, with no entropy approximation.
  ck(p['JC']/p['e']>=F(3*w,4));ck(p['JC']/p['e']<=w)
  ck((1-p['alpha'])*p['JB']/(p['alpha']*p['e'])+p['eta']/(p['alpha']*p['e'])<1)
  if h>=4:
   ck(2*m<=w);ck(p['I']<=3*w*p['alpha']*p['e']);ck(ratio>=F(m,4))
  rows.append({'h':h,'w':w,'m':m,'s':s,'L':L,'physical_dimension':s+L+2*w+1,'reserve_over_I':str(ratio),'reserve_over_mI':str(ratio/m),'per_coordinate_ratios':{name:str(owned/physical) for name,count,physical,owned in owners}})
 dump(ROOT/'out/ENVELOPE_OBSTRUCTION.json',{'status':'PASS','cases':rows,'checks':CHECKS,'asymptotic':'V_s/I(F_h) ~ m=h+2 ~ log2(w); V_s/I >=m/4 for every integer h>=4','scope':'Specific A046 cutoff envelope only; no unbounded actual bad debit or H/I claimed.'})
 print(json.dumps({'obstruction':'PASS','cases':len(rows),'checks':CHECKS,'seconds':time.monotonic()-START}))
def main():
 if 'accounts' in sys.argv:accounts();return
 if 'obstruction' in sys.argv:obstruction();return
 cases=[(s,1,R,T,'dictator',0) for s in [1,2] for R in [1,2] for T in [1,2]]+[(2,1,1,2,'bent',4),(2,1,1,2,'selector',4)]
 pilot='pilot' in sys.argv
 if pilot:cases=cases[:1]
 dest=ROOT/'out'/('PILOT.json' if pilot else 'PHYSICAL.json');rows=[];prior=0
 if 'resume' in sys.argv and dest.exists():
  old=json.loads(dest.read_text());rows=old['cases'];prior=old['checks'];ck([tuple(r['case']) for r in rows]==cases[:len(rows)])
 for case in cases[len(rows):]:
  if time.monotonic()-START>40:
   dump(dest,{'status':'CHECKPOINT','checks':prior+CHECKS,'helper_checks':a.CHECKS,'cases':rows,'seconds_batch':time.monotonic()-START});print('CHECKPOINT');return
  rows.append(physical(case));dump(dest,{'status':'RUNNING','checks':prior+CHECKS,'helper_checks':a.CHECKS,'cases':rows})
 dump(dest,{'status':'PASS','checks':prior+CHECKS,'helper_checks':a.CHECKS,'cases':rows,'seconds_batch':time.monotonic()-START})
 print(json.dumps({'physical':'PASS','roots':len(rows),'checks':prior+CHECKS,'helper_checks':a.CHECKS,'seconds':time.monotonic()-START}))
if __name__=='__main__':main()

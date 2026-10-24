import arithmetic as ar
from fractions import Fraction as F
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();CHECKS=0
KB=F(1781,480);KU=F(10063,2520)
def ck(p):
 global CHECKS
 assert p
 CHECKS+=1
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def resume_rows(path):
 global CHECKS
 if 'resume' in sys.argv and path.exists():
  old=json.loads(path.read_text(encoding='utf-8'));CHECKS=old['checks'];ar.CHECKS=old['helper_checks'];return old['rows']
 return []
def controls(L,R,T):
 B=[];C=[]
 for x in range(1<<(L+R+T)):
  W=x&((1<<L)-1)==(1<<L)-1;U=(x>>L)&((1<<R)-1)==(1<<R)-1;V=(x>>(L+R))&((1<<T)-1)==(1<<T)-1
  B.append(int(W and U and V));C.append(int(U or V))
 return B,C
def construct(j,L,R,T,g):
 B,C=controls(L,R,T);n=L+R+T;G=tuple(g[x>>n] if B[x&((1<<n)-1)] else 1 for x in range(len(B)*len(g)));H=tuple(g[x>>n] if C[x&((1<<n)-1)] else 1 for x in range(len(C)*len(g)))
 v=tuple(H[x>>j] if x&((1<<j)-1)==(1<<j)-1 else G[x>>j] for x in range(len(G)*(1<<j)))
 return v,G,H
def node(j,L,R,T,g):
 v,G,H=construct(j,L,R,T,g);P,ds,Hroot,TC,W=ar.spectrum(v);rho=F(1,2**(j-1));eta=F(1,2**(L+R+T));q=F(1,2**R);r=F(1,2**T);e=q+r-q*r-eta
 aa=1-F(sum(g),len(g));d=rho*aa*e/2;ck(ds[0]==d)
 N=len(G);WG=ar.fwht(G);WH=ar.fwht(H);delta=[F(y-x,N) for x,y in zip(WG,WH)];gg=[F(x,N) for x in WG]
 ck(gg[0]==1-aa*eta);ck(delta[0]==-aa*e)
 ck(sum(x*x for x in gg[1:])==2*aa*eta-aa*aa*eta*eta)
 ck(sum(x*y for x,y in zip(gg[1:],delta[1:]))==-aa*aa*eta*e)
 ck(sum(x*x for x in delta[1:])==2*aa*e-aa*aa*e*e)
 u=[x+rho*y/2 for x,y in zip(gg,delta)];vv=[-rho*y/2 for y in delta]
 qstar=sum(x*x+y*y for x,y in zip(u[1:],vv[1:]));bstar=sum(x*x for x in vv[1:])
 ck(u[0]==1-aa*eta-d);ck(vv[0]==d)
 ck(qstar==2*aa*eta-aa*aa*eta*eta-rho*aa*aa*eta*e+rho*rho*(aa*e-aa*aa*e*e/2))
 ck(bstar==rho*rho*aa*e*(2-aa*e)/4);ck(qstar<=2*aa*eta+rho*rho*aa*e)
 packet=[P[2*t]+P[2*t+1] for t in range(len(P)//2)];Bvec=ar.add((1,Hroot),(-1,ar.ent(packet)))
 direct={}
 for x,y in zip(u,vv):
  direct=ar.add((1,direct),(1,ar.ent([x*x,y*y])),(-1,ar.ent([x*x+y*y])))
 direct=ar.add((1,direct),(2*(1-rho)*d,{2:F(1)}));ck(direct==Bvec)
 ck(25*eta<=8*e*e)
 certified={}
 if d:
  if e<=F(1,8):
   gap=ar.add((1,Bvec),(-KU*d,{2:F(1)}));ck(ar.bounds(gap)[1]<0);certified['biased_bound_gap']=ar.packed(gap)
   if aa==1:
    gap=ar.add((1,Bvec),(-KB*d,{2:F(1)}));ck(ar.bounds(gap)[1]<0);certified['balanced_bound_gap']=ar.packed(gap)
 else:ck(not Bvec)
 result={'j':j,'L':L,'R':R,'T':T,'core':list(g),'a':str(aa),'e':str(e),'d':str(d),'q_star':str(qstar),'b_star':str(bstar),'erasure':ar.packed(Bvec),'certificates':certified,'dimension':len(ds)}
 return result,(P,ds,Hroot,v)
def basic(mode):
 maj=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
 if mode=='source':cases=[(j,g) for j in [1,2] for g in [(1,-1),maj]]
 else:cases=[(j,tuple(1-2*(mask>>x&1) for x in range(4))) for j in [1,2] for mask in range(16)]
 if 'pilot' in sys.argv:cases=cases[:1]
 name='PILOT' if 'pilot' in sys.argv else mode.upper();dest=ROOT/'out'/f'{name}.json';rows=resume_rows(dest)
 for j,g in cases[len(rows):]:
  if time.monotonic()-START>40:
   save(dest,{'status':'CHECKPOINT','checks':CHECKS,'helper_checks':ar.CHECKS,'rows':rows,'seconds':time.monotonic()-START});print('CHECKPOINT '+name+' '+str(len(rows)));return
  ar.spectrum.cache_clear();row,_=node(j,1,4,4,g);rows.append(row);save(dest,{'status':'RUNNING','checks':CHECKS,'helper_checks':ar.CHECKS,'rows':rows})
 save(dest,{'status':'PASS','checks':CHECKS,'helper_checks':ar.CHECKS,'nodes':len(rows),'seconds':time.monotonic()-START,'rows':rows})
 print(json.dumps({'mode':name,'status':'PASS','nodes':len(rows),'checks':CHECKS,'helper_checks':ar.CHECKS,'seconds':time.monotonic()-START}))
def interleaved():
 maj=tuple(1 if x.bit_count()>=2 else -1 for x in range(8));parity=tuple((-1)**x.bit_count() for x in range(8));point=tuple(-1 if x==0 else 1 for x in range(8))
 cases=[(j,g) for j in [1,2] for g in [maj,parity,point,tuple(-x for x in point)]];dest=ROOT/'out/INTERLEAVED.json';rows=resume_rows(dest)
 for j,g in cases[len(rows):]:
  if time.monotonic()-START>40:
   save(dest,{'status':'CHECKPOINT','checks':CHECKS,'helper_checks':ar.CHECKS,'rows':rows,'seconds':time.monotonic()-START});print('CHECKPOINT INTERLEAVED '+str(len(rows)));return
  ar.spectrum.cache_clear();parent,(P,ds,H,v)=node(j,1,4,4,g);children=[];parentface=account_node(j,g,parent,ds,v)
  pi=F(1,2**9)+F(1,2**j)*(F(1,8)-F(1,256)-F(1,512))
  for i in range(3):
   g0,g1=ar.halves(g,i);r0,(P0,d0,H0,v0)=node(j,1,4,4,g0);r1,(P1,d1,H1,v1)=node(j,1,4,4,g1);idx=j+9+i
   face0=account_node(j,g0,r0,d0,v0);face1=account_node(j,g1,r1,d1,v1)
   ck(ar.halves(v,idx)==(v0,v1));ck(ds[idx]==pi*ar.infs(g)[i])
   ck(sum(ds)==ds[idx]+(sum(d0)+sum(d1))/2)
   packet=[P[t]+P[t|(1<<idx)] for t in range(len(P)) if not(t>>idx&1)];HP=ar.ent(packet)
   B=ar.add((1,H),(-1,HP));JS=ar.add((1,HP),(-F(1,2),H0),(-F(1,2),H1))
   ck(not ar.add((1,H),(-F(1,2),H0),(-F(1,2),H1),(-1,B),(-1,JS)))
   ck(F(parent['d'])==(F(r0['d'])+F(r1['d']))/2)
   release=parentface-(face0+face1)/2;ck(release==F(1,2**j)*F(parent['e'])*ar.infs(g)[i]);ck(release<=ds[idx])
   children.append({'core_query':i,'query_influence':str(ds[idx]),'separator_face_release':str(release),'child0':r0,'child1':r1,'data_query_erasure':ar.packed(B),'data_query_JS':ar.packed(JS),'expected_child_terminal_entropy':ar.packed(ar.add((pi/2,ar.ent(ar.spectrum(g0)[0])),(pi/2,ar.ent(ar.spectrum(g1)[0]))))})
  rows.append({'parent':parent,'queries':children});save(ROOT/'out/INTERLEAVED.json',{'status':'RUNNING','checks':CHECKS,'helper_checks':ar.CHECKS,'rows':rows})
 save(ROOT/'out/INTERLEAVED.json',{'status':'PASS','parents':8,'child_occurrences':48,'checks':CHECKS,'helper_checks':ar.CHECKS,'seconds':time.monotonic()-START,'rows':rows})
 print(json.dumps({'mode':'INTERLEAVED','status':'PASS','checks':CHECKS,'helper_checks':ar.CHECKS,'seconds':time.monotonic()-START}))
def account_node(j,g,row,ds,v):
 aa=F(row['a']);eta=F(1,512);e=F(row['e']);alpha=F(1,2**j);pi=eta+alpha*e;JB=9*eta;JC=8*F(1,16)*F(15,16);Ig=sum(ar.infs(g))
 ck(sum(ds[:j])==aa*j*alpha*e);ck(sum(ds[j:j+9])==aa*((1-alpha)*JB+alpha*JC));ck(sum(ds[j+9:])==pi*Ig)
 v0,v1=ar.halves(v,0);face=sum(ar.infs(tuple(x*y for x,y in zip(v0,v1))))/2
 ck(face==alpha*(aa*(JB+JC+(j-1)*e)+e*Ig));row['separator_face_cost']=str(face);row['I_terminal']=str(pi*Ig)
 return face
def rational():
 initial=CHECKS;rows=0
 for j in range(1,9):
  rho=F(1,2**(j-1))
  for L in range(1,4):
   for R in range(4,9):
    for T in range(4,9):
     eta=F(1,2**(L+R+T));e=F(1,2**R)+F(1,2**T)-F(1,2**(R+T))-eta
     for aa in [F(0),F(1,64),F(1,8),F(1,2),F(1),F(3,2),F(2)]:
      d=rho*aa*e/2;qs=2*aa*eta-aa*aa*eta*eta-rho*aa*aa*eta*e+rho*rho*(aa*e-aa*aa*e*e/2);bs=rho*rho*aa*e*(2-aa*e)/4
      ck(e<=F(1,8));ck(25*eta<=8*e*e);ck(0<=bs<=qs);ck(qs<=2*aa*eta+rho*rho*aa*e);ck(qs+(1-aa*eta-d)**2+d*d==1-rho*(1-rho)*aa*e);rows+=1
 save(ROOT/'out/MOMENTS.json',{'status':'PASS','formal_rows':rows,'checks':CHECKS-initial})
 # All constants in the analytic extension: integers/Fractions only.
 lnlo=F(2,3)+F(2,81)+F(2,1215);ck(lnlo>F(9,13));ck(F(65,24)+F(1,100)<F(87,32));ck(87**20<2**13*56**20);ck(F(100,49)>2);ck(2+F(13,20)+F(26,63)+F(67,72)==KU);ck(KU<4);ck(2+F(2,3)+F(9,20)+F(19,32)==KB);ck(KB<4)
 initial=CHECKS;cases=drifts=0
 for s in range(1,7):
  for L in range(1,4):
   for R in range(1,7):
    for T in range(1,7):
     for Ig in [F(1),F(5,2)]:
      alpha=F(1,2**s);eta=F(1,2**(L+R+T));q=F(1,2**R);r=F(1,2**T);e=q+r-q*r-eta;JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);JD=JB+JC
      mm=0 if min(R,T)>=4 else (min(R,T)+1).bit_length()+2
      def W(j):
       M=min(j,mm);return F(1,2**j)*(M*JD+e*M*(M-1)/2+M*e*Ig)
      for j in range(1,s+1):ck(W(j)-W(j-1)/2==(F(1,2**j)*(JD+(j-1)*e+e*Ig) if j<=mm else 0));drifts+=1
      Is=s*alpha*e;Io=(1-alpha)*JB+alpha*JC;It=(eta+alpha*e)*Ig;ck(W(s)<=5*Io+2*Is+5*It);ck(W(s)<=5*(Is+Io+It));cases+=1
 save(ROOT/'out/RESERVE.json',{'status':'PASS','formal_cases':cases,'drift_identities':drifts,'checks':CHECKS-initial})
 save(ROOT/'out/RATIONAL_SUMMARY.json',{'status':'PASS','total_checks':CHECKS,'seconds':time.monotonic()-START,'formal_rows':rows,'reserve_cases':cases,'constants_checks':8})
 print(json.dumps({'mode':'RATIONAL','status':'PASS','checks':CHECKS,'moments':rows,'reserve_cases':cases,'seconds':time.monotonic()-START}))
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'source'
 if mode in ['source','biased']:basic(mode)
 elif mode=='interleaved':interleaved()
 elif mode=='rational':rational()
 else:raise ValueError(mode)

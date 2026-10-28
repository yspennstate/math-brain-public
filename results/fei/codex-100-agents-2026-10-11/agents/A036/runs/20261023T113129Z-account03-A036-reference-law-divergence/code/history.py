from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import sys,time,json
import exact as E
import channel as C
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
def ck(v):
 global N
 N+=1;assert v,N
 assert time.perf_counter()-start<55

def KL(p,q):
 weights=defaultdict(F)
 for a,b in zip(p,q):
  if a:ck(b>0);weights[a/b]+=a
 return E.total(E.scale(a,E.logpoint(z)) for z,a in weights.items())
def H(p):
 weights=defaultdict(int)
 for a in p:
  if a:weights[a]+=1
 return E.total(E.scale(n,E.phi(E.iv(a))) for a,n in weights.items())
def facts(t):
 p=E.law(t);I=sum(F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t)) for i in range(len(t).bit_length()-1))
 return p,I,H(p)
def step(t,q,i,zero=False):
 p=E.law(t);ts=[E.restrict(t,i,y) for y in [0,1]];ps=[E.law(a) for a in ts]
 pp=[p[z]+p[z|(1<<i)] for z in range(len(p)) if not z>>i&1]
 qq=[q[z]+q[z|(1<<i)] for z in range(len(q)) if not z>>i&1]
 ck(pp==[(a+b)/2 for a,b in zip(*ps)])
 joint=[[qq[z]*(ps[y][z]/(2*pp[z]) if pp[z] else F(1,2)) for z in range(len(pp))] for y in [0,1]];out=[sum(j) for j in joint];qc=[[a/out[y] for a in joint[y]] for y in [0,1]]
 ck(sum(out)==1);ck(all(sum(a)==1 for a in qc))
 if zero:
  for z in range(len(p)):
   zz=(z&((1<<i)-1))|((z>>(i+1))<<i)
   ck(q[z]*pp[zz]==p[z]*qq[zz])
  ck(out==[F(1,2),F(1,2)])
 Erel=E.sub(KL(p,q),KL(pp,qq));O=KL([F(1,2)]*2,out);old=E.scale(F(1,2),E.total(KL(a,b) for a,b in zip(ps,qc)))
 ck(E.overlaps(KL(p,q),E.add(E.add(Erel,O),old)))
 return ts,ps,qc,out,Erel,O

k=5 if '--pilot' in sys.argv else 10;d=F(1,2**k);g=[(-1)**(z&1)*(-1 if z in [2,3] else 1) for z in range(1<<k)];v=[g[z>>1]*(-1 if z==1 else 1) for z in range(1<<(k+1))];qv0=C.qfactor(v,F(1,8));corep=E.law(v)
t=[(-1)**((z>>1)&1) if not z&1 else v[z>>3] if z&4 else 1 for z in range(8*len(v))];p,I0,H0=facts(t);q=[F(0)]*len(t);q[:8]=p[:8]
for s in range(1,len(v)):
 for c in [0,1,4,5]:q[(s<<3)|c]=qv0[s]/16
ck(sum(q)==1);A0=KL(p,q);ck(E.overlaps(A0,E.scale(F(1,4),KL(corep,qv0))))
bs,bp,bq,bo,be,bout=step(t,q,2,True);aa,ap,aq,ao,ae,aout=step(bs[1],bq[1],1,True);release=E.add(E.add(be,bout),E.scale(F(1,2),E.add(ae,aout)));sigma1=E.iv(0);sigma2=E.iv(0);leaves=[(F(1,2),bs[0],bq[0])]
for a in [0,1]:
 eps=(-1)**a;tt,expected=C.lift(v,[1],eps,qv0,[F(1)]);ck(tt==aa[a]);ck(expected==aq[a]);tt,new=C.lift(v,[1],eps,C.qfactor(v,F(1,6)),[F(1)]);sigma1=E.add(sigma1,E.scale(F(1,4),E.sub(KL(ap[a],new),KL(ap[a],aq[a]))))
 ts,ps,old,outs,loss,out=step(tt,new,1);release=E.add(release,E.scale(F(1,4),E.add(loss,out)))
 for y in [0,1]:
  vy=E.restrict(v,0,y);child,rn=C.lift(vy,[1],eps,C.qfactor(vy,F(1,6)),[F(1)]);ck(child==ts[y]);ck(all((x==0)==(z==0) for x,z in zip(ps[y],rn)))
  sigma2=E.add(sigma2,E.scale(F(1,8),E.sub(KL(ps[y],rn),KL(ps[y],old[y]))));leaves.append((F(1,8),child,rn))
HH=E.iv(0);II=F(0);KK=E.iv(0)
for w,tt,rr in leaves:
 pp,ii,hh=facts(tt);HH=E.add(HH,E.scale(w,hh));II+=w*ii;KK=E.add(KK,E.scale(w,KL(pp,rr)))
ck(E.overlaps(E.add(A0,E.add(sigma1,sigma2)),E.add(release,KK)));S=E.sub(E.iv(4*II),HH);e=E.add(E.sub(H0,HH),E.iv(-4*(I0-II)));M=E.sub(E.iv(4*I0),E.add(H0,A0));net=E.add(E.add(A0,e),E.add(sigma1,sigma2));J=(max(F(0),net[0]),max(F(0),net[1]));remaining=E.sub(E.sub(S,J),E.iv(F(1,4)))
ck(sigma1[0]>0);ck(sigma2[0]>E.div(E.iv(F(1,4096)),E.LN2)[1]);ck(S[0]>F(15,8));ck(remaining[0]>F(13,8));ck(E.overlaps(E.sub(S,net),E.sub(M,E.add(sigma1,sigma2))))
if k>=10:ck(M[0]>1+(1+d)+F(7,8))
row={'k':k,'source_dimension':k+4,'actual_root_A0':E.enc(A0),'root_margin_M0':E.enc(M),'first_ACTUAL_positive_reset':E.enc(sigma1),'second_ACTUAL_positive_reset':E.enc(sigma2),'all_erasure_plus_outcome_KL':E.enc(release),'complete_terminal_KL':E.enc(KK),'complete_terminal_S':E.enc(S),'old_booking':'1/4','same_original_owner_remaining':E.enc(remaining),'terminal_count':len(leaves),'all_old_and_fresh_supports_match':True}
receipt={'status':'PASS','cases':1,'assertions':N,'channel_assertions':C.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'row':row}
(R/'out'/('HISTORY_PILOT.json' if '--pilot' in sys.argv else 'HISTORY.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in receipt.items() if k!='row'}))

from fractions import Fraction as F
from pathlib import Path
import time,sys,json
import exact as E
import validate as V
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(v):
 global C
 C+=1;assert v,C
 assert time.perf_counter()-start<55
def KL(p,q):return V.KL(p,q)
def core(fs):
 g=[1]
 for f in fs:g=[a*b for b in f for a in g]
 return g
def cq(fs,alpha):
 q=[F(1)]
 for f in fs:q=V.tensor(q,V.qfactor(f,alpha))
 return q
def root(fs):
 g=core(fs);q=cq(fs,F(1,8));t=[(-1)**((z>>1)&1) if not z&1 else (g[z>>3] if z&4 else 1) for z in range(8*len(g))]
 p=E.law(t);qq=[F(0)]*len(t);qq[:8]=p[:8]
 for s in range(1,len(q)):
  for c in [0,1,4,5]:qq[(s<<3)|c]=q[s]/16
 ck(sum(qq)==1);return t,qq
def fresh(fs,epsilon):
 g=core(fs);q=cq(fs,F(1,6));p=E.law([epsilon if not z&1 else g[z>>1] for z in range(2*len(g))]);qq=[F(0)]*len(p);qq[:2]=p[:2]
 for s in range(1,len(q)):qq[2*s]=qq[2*s+1]=q[s]/4
 ck(sum(qq)==1);return qq
rows=[]
for m,r in ([(1,2)] if '--pilot' in sys.argv else [(1,2),(1,3),(2,2),(2,3)]):
 for policy in [0,1]:
  fs=[V.point(r) for _ in range(m)];t,q=root(fs);p,ii,H,_=E.facts(t);A=KL(p,q);M=E.sub(E.iv(4*sum(ii)),E.add(H,A))
  bs,bp,bq,bo,be,bout=V.step(t,q,2);release=E.add(be,bout)
  aa,ap,aq,ao,ae,aout=V.step(bs[1],bq[1],1);release=E.add(release,E.scale(F(1,2),E.add(ae,aout)))
  leaves=[(F(1,2),bs[0],bq[0])];sigma1=E.iv(0);sigmalater=E.iv(0)
  for a in [0,1]:
   epsilon=(-1)**a;new=fresh(fs,epsilon);sigma1=E.add(sigma1,E.scale(F(1,4),E.sub(KL(ap[a],new),KL(ap[a],aq[a]))))
   active=[(F(1,4),aa[a],new,[f[:] for f in fs])]
   for generation in [0,1]:
    nxt=[]
    for weight,tab,ref,factors in active:
     j=(a+generation)%m if policy else 0
     offset=sum((len(f).bit_length()-1) for f in factors[:j]);coord=1+offset
     kids,pk,old,outs,loss,out=V.step(tab,ref,coord);release=E.add(release,E.scale(weight,E.add(loss,out)))
     local=E.iv(0)
     for y in [0,1]:
      ff=[f[:] for f in factors];ff[j]=E.restrict(ff[j],0,y);rn=fresh(ff,epsilon)
      inc=E.sub(KL(pk[y],rn),KL(pk[y],old[y]));local=E.add(local,E.scale(F(1,2),inc));nxt.append((weight/2,kids[y],rn,ff))
     ck(local[1]<0 or local[0]<=0<=local[1]);sigmalater=E.add(sigmalater,E.scale(weight,local))
    active=nxt
   leaves.extend((w,tt,qq) for w,tt,qq,_ in active)
  HH=E.iv(0);II=F(0);K=E.iv(0)
  for w,tt,qq in leaves:
   pp,iii,hh,_=E.facts(tt);HH=E.add(HH,E.scale(w,hh));II+=w*sum(iii);K=E.add(K,E.scale(w,KL(pp,qq)))
  ck(E.overlaps(E.add(A,E.add(sigma1,sigmalater)),E.add(release,K)))
  S=E.sub(E.iv(4*II),HH);e=E.add(E.sub(H,HH),E.iv(-4*(sum(ii)-II)));net=E.add(E.add(A,e),E.add(sigma1,sigmalater));J=(max(F(0),net[0]),max(F(0),net[1]));remaining=E.sub(E.sub(S,J),E.iv(F(1,4)))
  ck(S[0]>=1);ck(remaining[0]>=F(3,4));ck(E.overlaps(E.sub(S,net),E.sub(M,E.add(sigma1,sigmalater))))
  ck(sigmalater[1]<0);ck(sigma1[0]>0)
  rows.append({'m':m,'r':r,'policy':policy,'initial_source_KL':E.enc(A),'first_ACTUAL_positive_reset':E.enc(sigma1),'later_ACTUAL_signed_resets':E.enc(sigmalater),'all_erasure_and_outcome_KL':E.enc(release),'full_final_KL':E.enc(K),'full_S':E.enc(S),'same_owner_after_old_quarter':E.enc(remaining),'terminals':len(leaves)})
receipt={'status':'PASS','cases':len(rows),'assertions':C,'transport_assertions':V.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'rows':rows}
(R/'out'/('HISTORY_PILOT.json' if '--pilot' in sys.argv else 'HISTORY.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in receipt.items() if k!='rows'}))

from fractions import Fraction as F
from pathlib import Path
import json,time,sys
import exact as E
import validate as V
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(v,msg=''):
 global C
 C+=1;assert v,(C,msg);assert time.perf_counter()-start<55
def KL(p,q):return V.KL(p,q)
def core(fs):
 g=[1]
 for f in fs:g=V.tensor(g,f)
 return g
def cq(fs,betas):
 q=[F(1)]
 for f,b in zip(fs,betas):q=V.tensor(q,V.qfactor(f,1-b))
 return q
def fresh(fs,betas,epsilon):
 g=core(fs);q=cq(fs,betas);t=[epsilon if not z&1 else g[z>>1] for z in range(2*len(g))]
 p=E.law(t);qq=[F(0)]*len(p);qq[:2]=p[:2]
 for s in range(1,len(q)):qq[2*s]=qq[2*s+1]=q[s]/4
 ck(sum(qq)==1);return t,qq
def root(fs):
 g=core(fs);q=cq(fs,[F(7,8)]*len(fs));t=[(-1)**((z>>1)&1) if not z&1 else (g[z>>3] if z&4 else 1) for z in range(8*len(g))]
 p=E.law(t);qq=[F(0)]*len(t);qq[:8]=p[:8]
 for s in range(1,len(q)):
  for c in [0,1,4,5]:qq[(s<<3)|c]=q[s]/16
 ck(sum(qq)==1);return t,qq
def variance(f):return 1-F(sum(f),len(f))**2
def run(m,r,policy):
 fs=[V.point(r) for _ in range(m)];t,q=root(fs);p,ii,H,_=E.facts(t);A=KL(p,q);M=E.sub(E.iv(4*sum(ii)),E.add(H,A))
 bs,bp,bq,bo,be,bout=V.step(t,q,2);release=E.add(be,bout)
 aa,ap,aq,ao,ae,aout=V.step(bs[1],bq[1],1);release=E.add(release,E.scale(F(1,2),E.add(ae,aout)))
 leaves=[(F(1,2),bs[0],bq[0])];s1=E.iv(0);later=E.iv(0);charge=E.iv(0);transactions=[];positive=0;nodecount=0
 for a in [0,1]:
  epsilon=(-1)**a;betas=[F(5,6)]*m;tt,new=fresh(fs,betas,epsilon);ck(tt==aa[a]);s1=E.add(s1,E.scale(F(1,4),E.sub(KL(ap[a],new),KL(ap[a],aq[a]))))
  active=[(F(1,4),tt,new,[f[:] for f in fs],betas,0)]
  for generation in range(3):
   nxt=[]
   for w,tab,ref,factors,betas,hist in active:
    eligible=[j for j,f in enumerate(factors) if len(f)>=4 and abs(sum(f))!=len(f)]
    if not eligible or (policy==2 and a==1 and generation>=1):leaves.append((w,tab,ref));continue
    j=eligible[0] if policy==0 else eligible[(a+generation+hist)%len(eligible)]
    coord=1+sum(len(f).bit_length()-1 for f in factors[:j]);kids,pk,old,outs,loss,out=V.step(tab,ref,coord);release=E.add(release,E.scale(w,E.add(loss,out)));local=E.iv(0);same=E.iv(0);delta=E.iv(0);bound=E.iv(0)
    for y in [0,1]:
     ff=[f[:] for f in factors];ff[j]=E.restrict(ff[j],0,y);bb=betas[:]
     if policy==0:bb[j]=max(F(4,5),bb[j]*F(49,50))
     elif policy==1:bb[j]=F(4,5) if (y+a+generation)%2 else bb[j]
     else:bb[j]=max(F(4,5),bb[j]*F(99,100)) if y else bb[j]
     _,mid=fresh(ff,betas,epsilon);tt,rn=fresh(ff,bb,epsilon);ck(tt==kids[y]);ck(F(4,5)<=bb[j]<=betas[j]);ck(all(bb[k]==betas[k] for k in range(m) if k!=j))
     ds=E.sub(KL(pk[y],mid),KL(pk[y],old[y]));dd=E.sub(KL(pk[y],rn),KL(pk[y],mid));inc=E.sub(KL(pk[y],rn),KL(pk[y],old[y]));local=E.add(local,E.scale(F(1,2),inc));same=E.add(same,E.scale(F(1,2),ds));delta=E.add(delta,E.scale(F(1,2),dd))
     bd=E.scale(variance(ff[j])/2,E.logpoint(betas[j]/bb[j]));bound=E.add(bound,E.scale(F(1,2),bd))
     exactdiff=E.scale(F(1,2),E.sub(KL(E.law(ff[j]),V.qfactor(ff[j],1-bb[j])),KL(E.law(ff[j]),V.qfactor(ff[j],1-betas[j]))))
     ck(E.overlaps(dd,exactdiff),'profile lift identity');ck(dd[0]>=0 or dd[0]<=0<=dd[1]);ck(dd[1]<=bd[0] or bb[j]==betas[j] or len(ff[j])<=2 or variance(ff[j])==0)
     nxt.append((w/2,tt,rn,ff,bb,2*hist+y))
    ck(same[1]<0,'nonpositive same-profile step');ck(E.overlaps(local,E.add(same,delta)));ck(local[1]<bound[0] or bound==E.iv(0));nodecount+=1;positive+=local[0]>0
    later=E.add(later,E.scale(w,local));charge=E.add(charge,E.scale(w,bound));transactions.append({'reach':str(w),'factor':j,'generation':generation,'old_beta':str(betas[j]),'sigma':E.enc(local),'same_profile_sigma':E.enc(same),'profile_increment':E.enc(delta),'variance_increment_cap':E.enc(bound),'actual_outcomes':list(map(str,outs))})
   active=nxt
  leaves.extend((w,tt,qq) for w,tt,qq,_,_,_ in active)
 HH=E.iv(0);II=F(0);K=E.iv(0);terms=[]
 for w,tt,qq in leaves:
  pp,iii,hh,_=E.facts(tt);HH=E.add(HH,E.scale(w,hh));II+=w*sum(iii);kk=KL(pp,qq);K=E.add(K,E.scale(w,kk));terms.append({'reach':str(w),'H':E.enc(hh),'I':str(sum(iii)),'KL':E.enc(kk),'reference':list(map(str,qq))})
 ck(sum(w for w,_,_ in leaves)==1)
 cap=E.scale(sum(variance(f) for f in fs)/4,E.logpoint(F(25,24)));totalcap=E.scale(sum(variance(f) for f in fs)/4,E.logpoint(F(5,4)))
 ck(charge[1]<=cap[0]);ck(E.add(s1,later)[1]<totalcap[0]);ck(E.overlaps(E.add(A,E.add(s1,later)),E.add(release,K)))
 S=E.sub(E.iv(4*II),HH);e=E.add(E.sub(H,HH),E.iv(-4*(sum(ii)-II)));net=E.add(E.add(A,e),E.add(s1,later));J=(max(F(0),net[0]),max(F(0),net[1]));remaining=E.sub(E.sub(S,J),E.iv(F(1,4)))
 ck(S[0]>=1);ck(remaining[0]>=F(3,4));ck(E.overlaps(E.sub(S,net),E.sub(M,E.add(s1,later))));ck(s1[0]>0)
 return {'m':m,'r':r,'policy':policy,'node_count':nodecount,'positive_later_local_resets':positive,'A0':E.enc(A),'sigma1':E.enc(s1),'sigma_later':E.enc(later),'actual_profile_cap_sum':E.enc(charge),'original_variance_later_cap':E.enc(cap),'original_variance_combined_cap':E.enc(totalcap),'all_erasure_outcome_KL':E.enc(release),'full_terminal_KL':E.enc(K),'S':E.enc(S),'remaining_after_old_quarter':E.enc(remaining),'transactions':transactions,'terminals':terms}
if __name__=='__main__':
 specs=[(1,3)] if '--pilot' in sys.argv else [(1,3),(1,4),(2,2),(2,3)]
 rows=[]
 for m,r in specs:
  for policy in range(3):rows.append(run(m,r,policy))
  E.logpoint.cache_clear()
 ck(2*(F(1,3)+F(1,81)+F(1,1215))>F(9,13));ck(10**15<2**8*7**15)
 summary={'status':'PASS','cases':len(rows),'assertions':C,'transport_assertions':V.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'positive_later_local_resets':sum(x['positive_later_local_resets'] for x in rows),'rows':rows}
 (R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in summary.items() if k!='rows'}))

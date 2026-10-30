from fractions import Fraction as F
from pathlib import Path
import json,sys,time
import exact as E
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter();C=0
STRONG='--strong' in sys.argv
def ck(b):
 global C
 C+=1;assert b,C
 assert time.perf_counter()-START<55
def enc(a):return E.enc(a)
def ivlaw(q):return [E.iv(a) for a in q]
def sumv(ws):return E.total(ws)
def close(a,b):ck(E.overlaps(a,b))
def core(m,r):
 return [(-1)**sum(((z>>(j*r))&((1<<r)-1))==((1<<r)-1) for j in range(m)) for z in range(1<<(m*r))]
def fq(w,active=True,den=8):
 if not active or w==0:return [F(1)]+[F(0)]*((1<<w)-1)
 if w==1:return [F(0),F(1)]
 d=F(1,1<<w);p0=(1-2*d)**2;v=1-p0
 q=[p0]+[F(den-1,den)*4*d*d]*( (1<<w)-1)
 q[-1]+=v/den;ck(sum(q)==1);return q
def tensorq(m,r,fixed=None,fresh=False):
 den=6 if STRONG and fresh else 8
 qs=[fq(r if fixed is None else r-1, fixed!=0,den)]+[fq(r,True,den) for _ in range(m-1)]
 result=[F(1)]
 for q in qs:result=[a*b for b in q for a in result]
 ck(sum(result)==1);return result
def lift(tab,q):
 t=[(-1)**((u>>1)&1) if not u&1 else tab[u>>3] if u&4 else 1 for u in range(8*len(tab))]
 p=E.law(t);Q=[F(0)]*len(t)
 for s in range(8):Q[s]=p[s]
 for s in range(1,len(q)):
  for ctl in (0,1,4,5):Q[(s<<3)|ctl]=q[s]/16
 ck(sum(Q)==1);return t,ivlaw(Q)
def fresh(tab,q,ctl,child):
 p=E.law(tab)
 if ctl==0:
  if child==0:return ivlaw(p)
  v=[F(0)]*len(p)
  for s,a in enumerate(q):v[s<<1]=a
 else:
  v=[F(0)]*len(p);v[0]=p[0];v[1]=p[1]
  for s in range(1,len(q)):v[2*s]=v[2*s+1]=q[s]/4
 ck(sum(v)==1)
 ck(all(not pp or qq>0 for pp,qq in zip(p,v)))
 return ivlaw(v)
def var_remaining(m,r,bit):
 d=F(1,1<<r);first=F(0) if bit==0 else 4*(2*d)*(1-2*d)
 return first+(m-1)*4*d*(1-d)
def run(m,r):
 h=core(m,r);q=tensorq(m,r);p=E.law(h);ck(q[0]==p[0])
 t,Q=lift(h,q);P,inf,H,_=E.facts(t);A=E.kl(P,Q)
 close(A,E.scale(F(1,4),E.kl(p,ivlaw(q))))
 margin=E.sub(E.iv(4*sum(inf)),E.add(H,A));delta=F(1,1<<r)
 tau=F(sum(x==-1 for x in h),len(h));ck(margin[0]>1+2*tau+F(m,4)*delta)
 B,BQ,Ob,_,zb,Eb=E.step(t,Q,2)
 D,DQ,Od,_,zd,Ed=E.step(B[1],BQ[1],2)
 rows=[]
 for ctl in (0,1):
  pairs=[]
  for bit in (0,1):
   G,GQ,Og,outs,zg,Eg=E.step(D[bit],DQ[bit],ctl)
   qq=tensorq(m,r,bit,True)
   hc=E.restrict(h,0,bit);ck(E.law(hc)[0]==qq[0])
   kc=E.kl(E.law(hc),ivlaw(qq))
   RQ=[fresh(G[c],qq,ctl,c) for c in (0,1)]
   kfresh=sumv(E.scale(F(1,2),E.kl(E.law(g),rq)) for g,rq in zip(G,RQ))
   close(kfresh,E.scale(F(1,2),kc))
   pairs.append((G,GQ,RQ,Og,Eg,zg,kfresh))
  for selected in ('all','zero'):
   facts=[(F(1,2),B[0],BQ[0],BQ[0])]
   release=E.add(Eb,Ob);release=E.add(release,E.scale(F(1,2),E.add(Ed,Od)))
   freshbill=E.iv(0)
   for bit,pair in enumerate(pairs):
    G,GQ,RQ,Og,Eg,zg,kfresh=pair
    release=E.add(release,E.scale(F(1,4),E.add(Eg,Og)))
    use=selected=='all' or bit==0
    if use:freshbill=E.add(freshbill,E.scale(F(1,4),kfresh))
    for j in (0,1):facts.append((F(1,8),G[j],GQ[j],RQ[j] if use else GQ[j]))
   Hf=E.iv(0);If=F(0);Kold=E.iv(0);Knew=E.iv(0)
   for w,g,qold,qnew in facts:
    pp,ii,hh,_=E.facts(g);Hf=E.add(Hf,E.scale(w,hh));If+=w*sum(ii)
    Kold=E.add(Kold,E.scale(w,E.kl(pp,qold)));Knew=E.add(Knew,E.scale(w,E.kl(pp,qnew)))
   close(A,E.add(release,Kold))
   sigma=E.sub(Knew,Kold);ck(sigma[1]<=freshbill[1]+F(1,1<<75))
   variance=4*m*delta*(1-delta)
   ck((var_remaining(m,r,0)+var_remaining(m,r,1))/2<=variance)
   L=E.logpoint(F(6,5) if STRONG else F(8,7));upper=E.scale(variance/4,L)
   rate=F(11,40) if STRONG else F(1,5)
   ck(freshbill[1]<m*rate*delta);ck(sigma[1]<m*rate*delta)
   S=E.sub(E.iv(4*If),Hf);ck(S[0]>=1)
   edge=E.add(E.sub(H,Hf),E.iv(-4*(sum(inf)-If)))
   net=E.add(E.add(A,edge),sigma)
   J=(max(F(0),net[0]),max(F(0),net[1]))
   reserve=E.sub(E.sub(S,J),E.iv(F(1,4)));ck(reserve[0]>=F(3,4))
   close(E.sub(S,net),E.sub(margin,sigma))
   ck(E.sub(margin,sigma)[0]>1+2*tau+(F(m,40) if STRONG else F(m,20))*delta)
   row={'m':m,'r':r,'controller':'x' if ctl==0 else 'a','reset_pairs':selected,'root_A':enc(A),'root_inclusive_margin':enc(margin),'erasure_plus_outcome_KL':enc(release),'old_terminal_KL':enc(Kold),'new_terminal_KL':enc(Knew),'actual_signed_reset_sigma':enc(sigma),'complete_fresh_bill':enc(freshbill),'variance_bound':str(variance),'variance_KL_upper':enc(upper),'final_H':enc(Hf),'final_I':str(If),'actual_S':enc(S),'signed_net_after_reset':enc(net),'old_booking':'1/4','remaining_same_owner':enc(reserve),'source_zero_erased_rows':zb+zd+sum(x[5] for x in pairs),'full_terminal_count':len(facts)}
   rows.append(row)
   row['initial_denominator']=8;row['fresh_denominator']=6 if STRONG else 8
   (ROOT/'out'/f'{"STRONG_" if STRONG else ""}CASE_m{m}r{r}_{ctl}_{selected}.json').write_text(json.dumps(row,indent=2),encoding='utf-8')
 return rows
fixtures=([(2,3)] if STRONG else [(1,2)]) if '--pilot' in sys.argv else [(2,2),(2,3),(3,2)]
rows=[]
for m,r in fixtures:rows+=run(m,r)
ck(8**5<2*7**5)
if STRONG:ck(6**40<2**11*5**40)
summary={'status':'PASS','cases':len(rows),'assertions':C,'primitive_assertions':E.checks,'runtime_seconds':time.perf_counter()-START,'source_zero_rows':sum(x['source_zero_erased_rows'] for x in rows),'positive_signed_resets':sum(F(x['actual_signed_reset_sigma'][0])>0 for x in rows),'scope':'finite verification only; all-parameter result is analytic PROOF.md'}
(ROOT/'out'/(('STRONG_' if STRONG else '')+('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'))).write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary))

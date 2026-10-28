from pathlib import Path
import json,time,hashlib
from fractions import Fraction as F
from arithmetic import *
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0

def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime')

def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def CE(P,Q):
 ans=Z
 for p,q in zip(P,Q):
  if p:ck(q>0);ans=add(ans,scale(log(q),-p))
 return ans

def transport(f,Q,i):
 children=[restrict(f,i,b) for b in [0,1]];P=law(f);laws=[law(v) for v in children];N=len(laws[0]);q=[];qr=[];kernels=[];joint=[[],[]];refonly=0
 for x in range(N):
  lo=(x&((1<<i)-1))|((x>>i)<<(i+1));hi=lo|(1<<i);mass=P[lo]+P[hi];ref=Q[lo]+Q[hi]
  ck(laws[0][x]+laws[1][x]==2*mass)
  k=laws[0][x]/(2*mass) if mass else F(1,2)
  ck(0<=k<=1);refonly+=int(mass==0 and ref>0);q.append(mass);qr.append(ref);kernels.append(k);joint[0].append(ref*k);joint[1].append(ref*(1-k))
 z=[sum(v) for v in joint];ck(z[0]>0 and z[1]>0 and sum(z)==1);refs=[[t/z[b] for t in joint[b]] for b in [0,1]]
 E=Z
 for x in range(N):
  lo=(x&((1<<i)-1))|((x>>i)<<(i+1));hi=lo|(1<<i)
  if q[x]:E=add(E,scale(kl([P[lo]/q[x],P[hi]/q[x]],[Q[lo]/qr[x],Q[hi]/qr[x]]),q[x]))
 O=kl([F(1,2)]*2,z);K=mean(kl(laws[0],refs[0]),kl(laws[1],refs[1]));A=kl(P,Q);overlap(A,add(E,add(O,K)))
 ce=CE(P,Q);ces=[CE(laws[b],refs[b]) for b in [0,1]];drop=sub(ce,mean(*ces));inf=infl(f,i)
 margin=sub((4*inf,)*2,drop);term=mean(*[sub((4*influence(children[b]),)*2,ces[b]) for b in [0,1]])
 overlap(sub((4*influence(f),)*2,ce),add(margin,term))
 ck(influence(f)==inf+(influence(children[0])+influence(children[1]))/2)
 rec={'coordinate':i,'Inf':str(inf),'normalizers':[str(x) for x in z],'reference_only_rows':refonly,'E':fmt(E),'O':fmt(O),'Kmean':fmt(K),'CE_parent':fmt(ce),'CE_children':[fmt(x) for x in ces],'DCE':fmt(drop),'rate4_margin':fmt(margin),'terminal_bank':fmt(term)}
 return children,refs,rec

def erasure(f,i):
 P=law(f);B=Z
 for x in range(len(P)//2):
  lo=(x&((1<<i)-1))|((x>>i)<<(i+1));hi=lo|(1<<i)
  B=add(B,sub(add(entterm(P[lo]),entterm(P[hi])),entterm(P[lo]+P[hi])))
 return B

def snode(g,f,Q):
 ck(f==family(g));d=infl(f,0);B=erasure(f,0)
 if not d:
  ck(B==Z);v=CE(law(f),Q);out={'skipped':True,'B':fmt(B),'Inf':'0','terminal_bank':fmt(sub((4*influence(f),)*2,v)),'normalizer':'not queried','source_CE':fmt(v),'terminal_laws':[{'P':[str(x) for x in law(f)],'Q':[str(x) for x in Q],'I':str(influence(f)),'CE':fmt(v)}]}
  return out
 ck(B[1]<4*d)
 fs,qs,rec=transport(f,Q,0);rec.update({'skipped':False,'B':fmt(B),'core':list(g)})
 rec['terminal_laws']=[{'P':[str(x) for x in law(fs[b])],'Q':[str(x) for x in qs[b]],'I':str(influence(fs[b])),'CE':fmt(CE(law(fs[b]),qs[b]))} for b in [0,1]]
 return rec

g=(-1,-1,-1,1,1,1,1,1);f=family(g);P=law(f);Q=product(P);rootCE=CE(P,Q);I=influence(f);U=bank(g);ck(U==F(23,32));ck(I==F(71,64))
fs,qinh,first=transport(f,Q,4);gs=[restrict(g,0,b) for b in [0,1]];qs=[product(law(v)) for v in fs]
core_remainder=sub(sub(entropy(P),mean(*[entropy(law(v)) for v in fs])),scale(sub(entropy(law(g)),mean(*[entropy(law(v)) for v in gs])),F(7,16)));core_remainder=sub(core_remainder,(F(5,64),)*2)
reset=mean(*[sub(CE(law(fs[b]),qs[b]),CE(law(fs[b]),qinh[b])) for b in [0,1]])
CEchild=[CE(law(fs[b]),qs[b]) for b in [0,1]];rawbanks=[sub((4*influence(fs[b]),)*2,CEchild[b]) for b in [0,1]]
old=sub(sub((4*I,)*2,rootCE),(U,)*2);new=add(old,(F(27,64),)*2)
C=mean(sub(rawbanks[0],(F(7,16),)*2),rawbanks[1]);L=sub(add(sub(rootCE,mean(*CEchild)),(F(5,64),)*2),(4*infl(f,4),)*2)
overlap(sub(C,L),new);ck(old[1]<-F(21,50));ck(new[0]>F(1,800));ck(sub(C,core_remainder)[0]>F(5,16));ck(L[0]>F(7,20));ck(reset[0]>F(3,50))
sourceS=[snode(gs[b],fs[b],qs[b]) for b in [0,1]]
for rec in sourceS:ck(F(rec['rate4_margin'][1])<0);ck(F(rec['terminal_bank'][0])>0)
review={'status':'PASS','source_statement_hash':None,'Iroot':str(I),'Uroot':str(U),'old_root_bank':fmt(old),'new_root_bank':fmt(new),'Cnew':fmt(C),'complete_node_L':fmt(L),'R':fmt(core_remainder),'signed_reset':fmt(reset),'first_query':first,'child_raw_banks':[fmt(x) for x in rawbanks],'S_nodes':sourceS,'reserve_conservation':['23/32','5/64','27/64','7/32']}
(R/'out/REVIEW.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
policies=[]
for choices in [(0,0),(0,1),(1,0),(1,1)]:
 nodes=[];original_second_release=F(0);total_second_inf=F(0);weighted_term=Z;secondD=Z;Sprice=Z;allSgood=True
 for b,i in enumerate(choices):
  gb=gs[b];fb=fs[b];qb=qs[b];ti=infl(gb,i);original_second_release+=F(1,2)*F(5,16)*ti;total_second_inf+=F(1,2)*infl(fb,4+i)
  if ti:
   fcs,qcs,rec=transport(fb,qb,4+i);gcs=[restrict(gb,i,c) for c in [0,1]];secondD=add(secondD,scale(tuple(F(x) for x in rec['DCE']),F(1,2)));branches=[]
   for c in [0,1]:
    sr=snode(gcs[c],fcs[c],qcs[c]);branches.append(sr)
    if sr['skipped']:tb=tuple(F(x) for x in sr['terminal_bank']);sd=Z
    else:tb=tuple(F(x) for x in sr['terminal_bank']);sd=tuple(F(x) for x in sr['rate4_margin'])
    weighted_term=add(weighted_term,scale(tb,F(1,4)));Sprice=add(Sprice,scale(sd,F(1,4)))
   rec['S_children']=branches;rec['core']=list(gb);rec['core_ti']=str(ti);rec['original_U_release']=str(F(5,16)*ti);nodes.append(rec)
  else:
   sr=snode(gb,fb,qb);tb=tuple(F(x) for x in sr['terminal_bank']);sd=tuple(F(x) for x in sr['rate4_margin'])
   weighted_term=add(weighted_term,scale(tb,F(1,2)));Sprice=add(Sprice,scale(sd,F(1,2)));nodes.append({'skipped_irrelevant_core':True,'coordinate':i,'S':sr})
 held=F(7,32);deficit=original_second_release-held
 maximalret=U-F(5,64)-original_second_release
 source_ce_margin=sub((4*I,)*2,rootCE)
 # No remaining bad S liability, so under continued ORIGINAL release bookings,
 # maximal retirement is exactly leftover U. Everything else has already been booked.
 amended_source=add(old,(maximalret,)*2)
 if choices[0]==1:ck(deficit==F(1,64));ck(amended_source[1]<-F(7,500));ck(amended_source[0]>-F(3,200))
 else:ck(deficit==-F(9,64));ck(amended_source[0]>F(7,50))
 second_price=sub((4*total_second_inf,)*2,secondD)
 overlap(mean(*rawbanks),add(second_price,add(Sprice,weighted_term)))
 # Full signed continuation without an artificial second U-release debit:
 # same incoming R_b carried through both physical steps, no reset.
 policy={'choices':list(choices),'original_second_release':str(original_second_release),'held':str(held),'held_deficit':str(deficit),'max_retirement_if_all_original_releases_booked':str(maximalret),'root_bank_with_this_max_retirement':fmt(amended_source),'weighted_second_Inf':str(total_second_inf),'second_query_price4_margin':fmt(second_price),'S_price4_margin':fmt(Sprice),'full_final_terminal_bank':fmt(weighted_term),'mean_first_child_raw_bank':fmt(mean(*rawbanks)),'all_S_erasure_good':True,'nodes':nodes}
 # H is the original held reserve, never reinitialized: H0=7/16,H1=0.
 # At any second ACTIVE core query set descendant H=0, since every ensuing
 # S node was checked good. If the core query is irrelevant, skip it and
 # carry H unchanged to the S node, then retire it there. All terminal H=0.
 future_debit=add(neg(add(second_price,Sprice)),(held,held))
 total_debit=add(L,future_debit)
 final_margin=sub(weighted_term,total_debit)
 overlap(final_margin,new);ck(final_margin[0]>F(1,800));ck(future_debit[0]>0);ck(total_debit[0]>0)
 retired_drift=original_second_release-(F(7,32) if choices[0]==1 else 0)
 policy.update({'held_after_all_S':'0','effective_future_debit':fmt(future_debit),'previous_full_node_debit':fmt(L),'combined_previously_booked_and_future_debit':fmt(total_debit),'final_same_source_margin':fmt(final_margin),'second_query_retired_part_drift':str(retired_drift),'additional_withdrawal_1_over_1600_margin':fmt(sub(final_margin,(F(1,1600),)*2))})
 ck(sub(final_margin,(F(1,1600),)*2)[0]>F(1,1600))
 policies.append(policy)
 (R/'out'/('POLICY_'+''.join(map(str,choices))+'.json')).write_text(json.dumps(policy,indent=2)+'\n',encoding='utf-8')
# Immediate exact finite-to-universal guard: an arbitrary previously spent debit
# cannot be admitted just because this source has positive ~.0013 slack.
ck(new[1]<F(13,10000));ck(new[0]>F(12,10000));ck(sub(new,(F(1,64),)*2)[1]<0)
summary={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-start,'policies':[{k:p[k] for k in ['choices','original_second_release','held_deficit','root_bank_with_this_max_retirement','full_final_terminal_bank','second_query_price4_margin','S_price4_margin','effective_future_debit','previous_full_node_debit','final_same_source_margin','second_query_retired_part_drift']} for p in policies],'original_source_margin':fmt(new),'full_root_rate4_CE_margin':fmt(sub((4*I,)*2,rootCE)),'formal_status':'not attempted: prior identical algebra route runtime-unverified; exact Fraction certificates used'}
(R/'out/RESULT.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'PASS','checks':checks,'runtime_seconds':summary['runtime_seconds'],'source_margin':mid(new),'policy_diagnostics':[{'choices':p['choices'],'held_deficit':p['held_deficit'],'source_max':mid(tuple(F(x) for x in p['root_bank_with_this_max_retirement'])),'terminal':mid(tuple(F(x) for x in p['full_final_terminal_bank']))} for p in policies]},indent=2))

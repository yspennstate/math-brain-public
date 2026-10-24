from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import exact as E
R=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0;NODES=0;GHOSTS=0
def ck(x):
 global COUNT
 assert x
 COUNT+=1
 assert time.perf_counter()-START<55
def ge(v):ck(not v or E.bounds(v)[0]>=0)
def ent(p):return E.ent(p.values())
def ce(p,q):return E.add(ent(p),E.kl(p,q))
def save(n,o):(R/'out'/n).write_text(json.dumps(o,indent=2),encoding='utf-8')
def close(v):
 if not v:return
 a,b=E.bounds(v);ck(a<=0<=b and b-a<F(1,1<<70))
def spectrum(t,co):return E.spec(t,co)
def core(m,r):
 def f(z):
  h=1
  for j in range(m):
   if (z>>(j*r))&((1<<r)-1)==(1<<r)-1:h=-h
  return h
 return tuple(f(z) for z in range(1<<(m*r)))
def factorref(r):
 t=core(1,r);p,ii=spectrum(t,tuple(range(r)));v=1-p.get(0,F(0));full=(1<<r)-1
 q={s:w if not s else F(7,8)*w+(v/F(8) if s==full else 0) for s,w in p.items()}
 ck(sum(q.values())==1 and q[0]==p[0]);return p,q
def tensorref(m,r):
 pp,qq=factorref(r);q={0:F(1)}
 for j in range(m):q={s|(u<<(j*r)):w*v for s,w in q.items() for u,v in qq.items()}
 return q
def calibrate(p,q):
 a=p.get(0,F(0));b=q.get(0,F(0));ck(sum(q.values())==1)
 if a==1:return {0:F(1)},E.kl({0:F(1)},{0:b})
 ck(b<1)
 qc={s:(a if not s else (1-a)*w/(1-b)) for s,w in q.items() if s or a}
 ck(sum(qc.values())==1 and qc.get(0,F(0))==a)
 debit=E.kl({0:a,1:1-a},{0:b,1:1-b})
 close(E.add(E.kl(p,q),E.scale(E.kl(p,qc),-1),E.scale(debit,-1)))
 return qc,debit
def lift(t,q):
 full=tuple(1-2*((u>>1)&1) if not(u&1) else t[u>>3] if u&4 else 1 for u in range(8*len(t)))
 p,ii=spectrum(full,tuple(range(3+len(t).bit_length()-1)))
 # Actual controls at zero core; the six occupied atoms are copied.
 Q={s:w for s,w in p.items() if not (s>>3)}
 for s,w in q.items():
  if s:
   for c in (0,1,4,5):Q[(s<<3)|c]=w/16
 ck(sum(Q.values())==1)
 return full,p,ii,Q
def node(t,co,q,i):
 global NODES,GHOSTS
 NODES+=1
 p,ii=spectrum(t,co);j=co.index(i);cn=tuple(x for x in co if x!=i);mask=sum(1<<x for x in cn)
 pe=E.marginal(p,mask);qe=E.marginal(q,mask)
 kids=[E.restrict(t,j,b) for b in (0,1)];P=[spectrum(z,cn)[0] for z in kids]
 for s in qe:ck(pe.get(s,F(0))==(P[0].get(s,F(0))+P[1].get(s,F(0)))/2)
 ghost=sum(not pe.get(s,F(0)) for s,w in qe.items() if w);GHOSTS+=ghost
 joint=[{s:w*(P[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,w in qe.items()} for b in (0,1)]
 qb=[sum(x.values()) for x in joint];ck(sum(qb)==1 and min(qb)>0)
 Q=[{s:w/qb[b] for s,w in joint[b].items() if w} for b in (0,1)]
 for s,pv in p.items():
  u=s&mask;er=(pv/pe[u])/(q[s]/qe[u])
  for b in (0,1):
   if P[b].get(u,F(0)):ck(pv/q[s]==er*(F(1,2)/qb[b])*(P[b][u]/Q[b][u]))
 ck(sum(ii.values())==ii[i]+sum(sum(spectrum(k,cn)[1].values()) for k in kids)/2)
 erased=E.add(E.kl(p,q),E.scale(E.kl(pe,qe),-1))
 outcome=E.kl({0:F(1,2),1:F(1,2)},{0:qb[0],1:qb[1]})
 ge(erased);ge(outcome)
 return kids,cn,Q,ghost,E.add(erased,outcome)
def frontier(t,co,q,remaining,w):
 if not remaining:
  p,ii=spectrum(t,co);return [(w,ent(p),sum(ii.values()),E.kl(p,q))],{}
 i=remaining[0];kids,cn,Q,ghost,release=node(t,co,q,i)
 rows=[];total=E.scale(release,w)
 for b in (0,1):
  rr,ee=frontier(kids[b],cn,Q[b],remaining[1:],w/2);rows+=rr;total=E.add(total,ee)
 return rows,total
def run(label,t,qraw):
 k=len(t).bit_length()-1;p,ic=spectrum(t,tuple(range(k)));q,cal=calibrate(p,qraw)
 full,P,I,Q=lift(t,q);H=ent(P);A=E.kl(P,Q);CE=E.add(H,A)
 close(E.add(A,E.scale(E.kl(p,q),F(-1,4))))
 ge(E.add({2:4*sum(ic.values())},E.scale(ce(p,qraw),-1),cal))
 # Positive calibrated credit is used once, before physical transport.
 ge(E.add({2:F(3)},E.scale(ce(p,qraw),F(1,4)),E.scale(cal,F(-1,4)),E.scale(CE,-1)))
 tminus=F(sum(z==-1 for z in t),len(t));rootmargin=E.add({2:4*sum(I.values())},E.scale(CE,-1))
 ge(E.add(rootmargin,{2:-1-2*tminus}))
 co=tuple(range(k+3));kids,cn,Qs,_,b_release=node(full,co,Q,2)
 p0,i0=spectrum(kids[0],cn);base=[(F(1,2),ent(p0),sum(i0.values()),E.kl(p0,Qs[0]))]
 first_remaining=(3,) if k else ()
 one,one_release=frontier(kids[1],cn,Qs[1],first_remaining,F(1,2));frontier_one=base+one
 allrows,all_release=frontier(kids[1],cn,Qs[1],tuple(range(3,k+3)),F(1,2));frontier_all=base+allrows
 views=[]
 for name,rows,releases in [('first_data',frontier_one,one_release),('all_data',frontier_all,all_release)]:
  Hf={};If=F(0);KLf={}
  for w,h,i,kl in rows:
   Hf=E.add(Hf,E.scale(h,w));If+=w*i;KLf=E.add(KLf,E.scale(kl,w))
   ge(E.add({2:4*i-2},E.scale(h,-1)))
  S=E.add({2:4*If},E.scale(Hf,-1));edge=E.add(H,E.scale(Hf,-1),{2:-4*(sum(I.values())-If)})
  # SIGNED net transaction, no replacement by A+[edge]+.
  net=E.add(A,edge);lo,hi=E.bounds(net)
  ck(lo>0 or hi<0 or not net)
  sharp=net if lo>0 else {}
  reserve=E.add(S,E.scale(sharp,-1))
  ge(E.add(reserve,{2:-1}))
  ge(E.add(reserve,{2:F(-3,4)})) # old booking1/4 retained, at least3/4 left.
  close(E.add(S,E.scale(net,-1),E.scale(rootmargin,-1)))
  close(E.add(A,E.scale(b_release,-1),E.scale(releases,-1),E.scale(KLf,-1)))
  views.append({'frontier':name,'leaves':len(rows),'terminal_H':E.serial(Hf),'terminal_I':str(If),'terminal_KL':E.serial(KLf),'signed_transaction':E.serial(net),'same_owner_reserve':E.serial(reserve),'reserve_interval':list(map(str,E.bounds(reserve))),'old_booking':'1/4, no new bank','after_old_booking':'>=3/4'})
 out={'label':label,'dimension':k+3,'core_KL':E.serial(E.kl(p,q)),'root_KL':E.serial(A),'initial_calibration_credit':E.serial(cal),'root_CE':E.serial(CE),'root_I':str(sum(I.values())),'root_margin':E.serial(rootmargin),'histories':views}
 save('CASE_'+label+'.json',out);return out
fixtures=[(1,2)] if '--pilot' in sys.argv else [(1,2),(2,2),(2,3),(3,2)]
out=[]
for m,r in fixtures:out.append(run(f'm{m}_r{r}',core(m,r),tensorref(m,r)))
if '--pilot' not in sys.argv:
 out.append(run('parity3_ghost_calibration',tuple((-1)**z.bit_count() for z in range(8)),{s:F(1,8) for s in range(8)}))
 for sign in (1,-1):out.append(run('constant_'+str(sign),(sign,sign),{0:F(1,2),1:F(1,2)}))
 # Huge Boolean cases use proved tensor formulas; no truth table enumeration.
 for m,r in [(9,3),(64,2),(64,3),(256,4),(512,2)]:
  pp,qq=factorref(r);d=F(1,1<<r);mu=(1-2*d)**m;t=(1-mu)/2
  ceh=E.scale(ce(pp,qq),m);Ih=2*m*r*d
  ge(E.add({2:4*Ih-m*d},E.scale(ceh,-1)))
  rootprice=E.add({2:F(3)},E.scale(ceh,F(1,4)))
  I=1+t/2+Ih/4
  ge(E.add({2:4*I-1-2*t-F(m,4)*d},E.scale(rootprice,-1)))
  save(f'SYMBOLIC_m{m}_r{r}.json',{'actual_Boolean_dimension':m*r+3,'truth_table_constructed':False,'core_CE':E.serial(ceh),'root_CE_upper':E.serial(rootprice),'root_I':str(I),'root_margin_lower':str(1+2*t+F(m,4)*d),'same_rate':4,'all_data_history_after_old_booking_lower':'3/4','proof':'PROOF.md, tensor formulas'})
  if (m,r)==(512,2):
   # Full data frontier has S=2. Paying A alone is false here; signed
   # negative query credits are indispensable. No huge cube is built.
   A=E.scale(E.kl(pp,qq),F(m,4))
   ge(E.add(A,{2:F(-2)}));ck(256**16>2*245**16)
   save('SIGNED_NECESSITY.json',{'source_KL':E.serial(A),'source_KL_lower':'>2','final_actual_S4':'2','conservative_source_only_payment':'FAILS','signed_net_upper':'< -31','signed_liability':'0','same_owner_after_old_quarter':'7/4','integer_sign':'256^16>2*245^16','reference':'same nonmatching lifted Q, not a fresh source'})
ck(8**4<2*7**4)
result={'status':'PASS','physical_cases':len(out),'symbolic_cases':0 if '--pilot' in sys.argv else 5,'assertions':COUNT,'primitive_assertions':E.COUNT,'physical_nodes':NODES,'retained_reference_only_rows':GHOSTS,'runtime_seconds':time.perf_counter()-START,'root_reference':'calibrated correlation-preserving lift; NOT canonical singleton occupancy','formal_status':'analytic with exact checks; no Lean result from this checker'}
save('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json',result);print(json.dumps(result))

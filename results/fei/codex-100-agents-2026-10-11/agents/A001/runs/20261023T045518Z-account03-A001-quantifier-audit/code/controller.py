from common import *
import helpers
start=time.perf_counter();rows=[];positive_individual=0;strict_mean=0;naive_checked=set()
for mask in range(256):
 ctrl=tuple(1 if mask>>x&1 else -1 for x in range(8));pp=sum(F(1-c,2) for c in ctrl)/8;v=actual(2,3,ctrl);P=spectrum(v);Q=source(2,3,F(1),ctrl)
 q=tuple(sum(P[T*8:(T+1)*8]) for T in range(8));Rp=tuple(sum(Q[T*8:(T+1)*8]) for T in range(8));vac=F(1,4)+F(5,16)*pp
 ck(Rp==(vac,)+((1-vac)/7,)*7 and q[0]==vac)
 if pp not in naive_checked:
  naive=[F(sum(a*((-1)**((j&T).bit_count())) for j,a in enumerate(v)),len(v))**2 for T in range(len(v))];ck(naive==P);naive_checked.add(pp)
 for h in range(3):
  daughters,pd,r,B,rho=query(v,Q,h);ck(not rho)
  controls=[tuple(restrict(ctrl,h,b)) for b in (0,1)];Qs=[source(2,3,F(1),c) for c in controls]
  qc=[tuple(sum(t[T*4:(T+1)*4]) for T in range(8)) for t in pd];Rps=[tuple(sum(t[T*4:(T+1)*4]) for T in range(8)) for t in Qs]
  ck(tuple((a+b)/2 for a,b in zip(*qc))==q)
  Z=[add((1,CE(t,qq)),(-1,CE(t,r))) for t,qq in zip(pd,Qs)]
  K=[add((1,CE(t,r)),(-1,CE(qq,Rp)),(-1,entropy(t)),(1,entropy(qq))) for t,qq in zip(pd,qc)]
  for a in K:ck(not a or interval(a)[0]>=0)
  for a in Z:
   if a and interval(a)[0]>0:positive_individual+=1
  jensen=add(*[(F(1,2),CE(qq,rr)) for qq,rr in zip(qc,Rps)],(-1,CE(q,Rp)))
  ck(not jensen or interval(jensen)[1]<0)
  avg=add(*[(F(1,2),a) for a in Z]);ck(avg==add((1,jensen),*[(F(-1,2),a) for a in K]))
  ck(not avg or interval(avg)[1]<0)
  if avg:strict_mean+=1
  direct=add((1,B),*[(F(1,2),CE(t,qq)) for t,qq in zip(pd,Qs)],(-1,CE(P,Q)));ck(direct==avg)
  rows.append({'event_mask':mask,'encoder':h,'event_mean':str(pp),'mean_signed_reset':rec(avg),'Jensen_gap':rec(jensen),'mean_conditional_KL':rec(add(*[(F(1,2),a) for a in K]))})
  ck(time.perf_counter()-start<55)
out={'status':'PASS','exact_assertions':helpers.count,'case_count':len(rows),'naive_Walsh_event_means':len(naive_checked),'positive_individual_child_resets':positive_individual,'strict_negative_means':strict_mean,'elapsed_seconds':time.perf_counter()-start,'rows':rows}
(RUN/'out/CONTROLLER_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

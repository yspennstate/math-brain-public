from common import *
import helpers
start=time.perf_counter();rows=[];ends={0:0,1:0}
def uniform_block(q):
 v=q[0];return (v,)+((1-v)/(len(q)-1),)*(len(q)-1)
for mask in range(256):
 v=tuple(1 if mask>>x&1 else -1 for x in range(8));P=spectrum(v)
 for j in range(3):
  q=marginal(P,j);R=uniform_block(q);Q=[F(0)]*8
  for T in range(4):
   for b in (0,1):
    t=insert(T,j,b);Q[t]=R[T]*(P[t]/q[T] if q[T] else int(b==0))
  ck(sum(Q)==1)
  if q[0] in ends:ends[q[0]]+=1
  ch,pc,rc,B,rho=query(v,Q,j);ck(not rho)
  refs=[uniform_block(p) for p in pc];z=[add((1,CE(p,r)),(-1,CE(p,rc))) for p,r in zip(pc,refs)]
  avg=add(*[(F(1,2),a) for a in z]);ck(not avg or interval(avg)[1]<0)
  billchange=add((1,B),*[(F(1,2),CE(p,r)) for p,r in zip(pc,refs)],(-1,CE(P,Q)));ck(avg==billchange)
  rows.append({'truth_table':mask,'encoder':j,'data_vacuum':str(q[0]),'whole_liability_change':rec(avg)})
  ck(time.perf_counter()-start<55)
out={'status':'PASS','exact_assertions':helpers.count,'case_count':len(rows),'vacuum_endpoint_counts':ends,'elapsed_seconds':time.perf_counter()-start,'rows':rows}
(RUN/'out/BLOCK_AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

from pathlib import Path
import json,time,hashlib
p=Path(__file__).with_name('check_flat.py')
exec(compile(p.read_text(encoding='utf-8').split('cases=0;coords=0')[0],str(p),'exec'))
start=time.monotonic();checks=0;rows=[]
for m,K in [(4,4),(10,10)]:
 n=m+1;poly=tuple((1<<(2*j+1))|(1<<(2*j+2)) for j in range(m//2))
 f=truth(n,poly,1<<1);_,_,d,q,B=split(f,0);_,I,H=stats(f)
 eq(d,Q(1,1<<m));eq(q,m*d);eq(I,Q(m,2)+(m+1)*d)
 eq(sign(add(B,const(-K*d))),1)
 a=tuple(Q(x,len(f)) for x in fwht(f));ws=[]
 for T in range(len(f)):
  if T&1:continue
  W=(1-d-a[T]**2)*(d-a[T^1]**2)
  le(Q((K-2)**2,4)*d*d,W)
  ws.append(W)
 lo,hi=bounds(B)
 assert lo>K*d
 rows.append({'data_dimension':m,'K':K,'influence':str(I),'selector_d':str(d),'root_odd_face_q':str(q),'root_q_over_I':str(q/I),'erasure_log_vector':serialize(B),'erasure_lower':str(lo),'erasure_upper':str(hi),'ratio_lower':str(lo/d),'ratio_upper':str(hi/d),'minimum_fiber_W':str(min(ws)),'fibers_checked':len(ws)})
 if time.monotonic()-start>60:raise TimeoutError('frozen cap')
out={'status':'PASS','fixed_functions':2,'exact_assertions':checks,'rows':rows,'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Bad selected order, not an all-tree or FEI counterexample'}
save('OBSTRUCTION.json',out);print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

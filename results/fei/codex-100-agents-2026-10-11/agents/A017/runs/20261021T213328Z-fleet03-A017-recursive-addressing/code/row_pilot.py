from pathlib import Path
import itertools,json,time,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(a):
 a=list(a); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h): x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
  h*=2
 return a
def ratio(a):
 p=q=1
 for v in a:
  t=v*v;p*=(t+1)**(t+1)
  if t:q*=t**t
 return p,q
start=time.perf_counter(); out={};checks=0
for c in [0,2,-2]:
 best=None;hist={}
 for tail in itertools.product([-1,1],repeat=6):
  H=[1,c]+list(tail); A=[w-1 for w in walsh(H)]; p,q=ratio(A)
  assert sum(A)==0 and sum(x*x for x in A)==(48 if c==0 else 80)
  assert all(x%2==0 for x in A)
  checks+=3
  if best is None or p*best[1]>best[0]*q:best=(p,q,H,A)
 out[str(c)]={'P':str(best[0]),'Q':str(best[1]),'H':best[2],'A':best[3]}
p0,q0=int(out['0']['P']),int(out['0']['Q'])
for c in ['2','-2']:
 p,q=int(out[c]['P']),int(out[c]['Q']);out[c]['three_zero_rows_plus_this_row_paid']=p*p0**3 <= (q*q0**3<<128)
res={'status':'ROW_CENSUS_COMPLETE','cases':192,'assertions':checks,'rows':out,'elapsed_seconds':time.perf_counter()-start}
(R/'out/row_pilot.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');print(json.dumps(res))

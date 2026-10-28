from pathlib import Path
from itertools import product,islice
from collections import Counter
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 return a
def ratio(A):
 p=q=1
 for a in A:
  t=a*a;p*=(t+1)**(t+1)
  if t:q*=t**t
 return p,q
start=time.perf_counter();best={};count=0;digest=hashlib.sha256();pilot='--pilot' in sys.argv
it=product([-2,-1,0,1,2],repeat=7)
if pilot:it=islice(it,1000)
for tail in it:
 H=[1]+list(tail);k=sum(abs(v)!=1 for v in tail);a=sum(abs(v)==2 for v in tail)
 A=[v-1 for v in walsh(H)];p,q=ratio(A);key=(k,a)
 assert sum(A)==0 and sum(v*v for v in A)==48-8*k+32*a+8 # 8*sum H^2-8
 if key not in best or p*best[key][1]>best[key][0]*q:best[key]=(p,q,H,A)
 count+=1;digest.update(bytes([v+2 for v in tail]))
results=[]
if not pilot:
 for k in range(8):
  worst=None
  for alloc in product(range(k+1),repeat=4):
   if sum(alloc)!=k:continue
   p=q=1
   for a in alloc:
    x,y,_,_=best[(k,a)];p*=x;q*=y
   if worst is None or p*worst[1]>worst[0]*q:worst=(p,q,alloc)
  p,q,alloc=worst
  results.append({'intrusions':k,'allocation':alloc,'row_envelope_paid':p<=(q<<128),'P':str(p),'Q':str(q),'profiles':[best[(k,a)][2] for a in alloc]})
res={'status':'COMPLETE','pilot':pilot,'cases':count,'coverage_sha256':digest.hexdigest(),'elapsed_seconds':time.perf_counter()-start,'results':results,'row_maxima':[{'k':k,'a':a,'P':str(v[0]),'Q':str(v[1]),'H':v[2],'A':v[3]} for (k,a),v in sorted(best.items())]}
(R/'out'/('envelope_pilot.json' if pilot else 'envelope_certificate.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k not in ['row_maxima','results']}));print(json.dumps([{k:v for k,v in a.items() if k not in ['P','Q','profiles']} for a in results]))

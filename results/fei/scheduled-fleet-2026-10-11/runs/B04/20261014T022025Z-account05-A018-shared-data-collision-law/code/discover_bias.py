from pathlib import Path
import math,json,time,sys
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
def e(u):
 p=(1+math.sqrt(max(0,1-u*u)))/2
 return 0 if p==1 else -p*math.log2(p)-(1-p)*math.log2(1-p)
laws=[]
for a in range(1,26):
 for b in range(1,26):
  laws.append((a,b,((a/25,b/(a+b)),(-b/25,a/(a+b))), (b*e(a/25)+a*e(b/25))/(a+b)))
best=(-1e100,None);count=0;violations=0
for a,b,L,H in laws:
 for c,d,R,K in laws:
  excess=-H-K
  for u,p in L:
   for v,q in R:
    weight=1+u*v
    if weight>0:excess+=p*q*weight*(e((u+v)/weight)-math.log2(weight))
  count+=1
  if excess>best[0]:best=(excess,[a,b,c,d])
  if excess>1e-12:
   violations+=1
   if violations==1:(ROOT/'out/FIRST_REAL_DISCOVERY.json').write_text(json.dumps({'parameters_over_25':[a,b,c,d],'float_excess':excess,'not_a_proof':True,'not_a_Boolean_witness':True},indent=2)+'\n',encoding='utf8')
  assert time.perf_counter()-start<60
  if '--pilot' in sys.argv and count==100:break
 if '--pilot' in sys.argv and count==100:break
out={'status':'DISCOVERY_ONLY','pairs':count,'positive_float_candidates':violations,'maximum_float_excess':best[0],'maximizer_parameters_over_25':best[1],'elapsed_seconds':time.perf_counter()-start,'arithmetic':'float; no proof or Boolean realization inferred'}
(ROOT/'out'/('BIAS_PILOT.json' if '--pilot' in sys.argv else 'BIAS_DISCOVERY.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))

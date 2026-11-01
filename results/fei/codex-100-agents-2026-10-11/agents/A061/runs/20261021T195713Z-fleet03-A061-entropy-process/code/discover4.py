from discover import *
start=time.perf_counter();best=(-1,None);maxratio=(-1,None);records=[]
for mask in range(0,65536,2):
 a=[1 if mask>>s&1 else -1 for s in range(16)];v=check(a,0);v.update(n=4,mask=mask,i=0)
 if v['gap']>best[0]:best=(v['gap'],v)
 if v['d'] and v['D']/v['d']>maxratio[0]:maxratio=(v['D']/v['d'],v)
 if v['gap']>1e-9 and len(records)<10:records.append(v)
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime exceeded')
out=dict(count=32768,seconds=time.perf_counter()-start,max_gap=best[1],max_D_per_d=maxratio,first_failures=records,arithmetic='FLOAT DISCOVERY ONLY')
(R/'out'/'DISCOVERY_4.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

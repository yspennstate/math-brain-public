import random,json,pathlib,time
from finite_checks import graph,avalanche,recurrent
start=time.monotonic();rng=random.Random(3301);vs,adj,o=graph(2);found=None;count=0
for _ in range(30000):
 h=[rng.choice([1,2,3,3,3]) for x in vs]
 if not recurrent(h,adj):continue
 count+=1;u,w,f=avalanche(h,adj,o)
 for a,b in zip(w,w[1:]):
  if not b<=a:
   found={'heights':h,'vertices':vs,'earlier_wave':sorted(a),'later_wave':sorted(b)};break
 if found:break
saturated=[]
for r in range(1,13):
 vsr,ar,orr=graph(r);u,w,f=avalanche([3]*len(vsr),ar,orr)
 assert len(w)==r+1
 assert all({vsr[i] for i in a}=={x for x in vsr if max(map(abs,x))<=r-k} for k,a in enumerate(w))
 saturated.append({'r':r,'waves':len(w),'topplings':sum(u)})
out={'recurrent_5x5_states_tested':count,'wave_expansion_example':found,'saturated':saturated,'seconds':time.monotonic()-start}
pathlib.Path('further_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

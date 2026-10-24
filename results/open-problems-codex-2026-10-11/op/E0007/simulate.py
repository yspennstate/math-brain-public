import random,math,time,json,statistics
from pathlib import Path
start=time.time();L=24;V=L*L
nb=[(y*L+(x+1)%L,y*L+(x-1)%L,((y+1)%L)*L+x,((y-1)%L)*L+x) for y in range(L) for x in range(L)]
cases=[(6.,2.,2.8,1.),(2.8,1.,5.4,2.),(8.,4.,1.9,1.)];results=[]
for case_id,(b1,d1,b2,d2) in enumerate(cases):
 trajectories=[];rate=max(b1+d1,b2+d2)
 for rep in range(6):
  rng=random.Random(7007+100*case_id+rep);s=[1 if (u:=rng.random())<.45 else 2 if u<.9 else 0 for _ in range(V)]
  counts=[s.count(0),s.count(1),s.count(2)];t=0.;next_t=0;snaps=[];targets=[0,10,30,60];j=0
  while j<len(targets):
   nt=t+rng.expovariate(V*rate)
   while j<len(targets) and nt>targets[j]:
    snaps.append({'t':targets[j],'rho1':counts[1]/V,'rho2':counts[2]/V});j+=1
   if j==len(targets):break
   t=nt;i=rng.randrange(V);typ=s[i]
   if not typ:continue
   b,d=(b1,d1) if typ==1 else (b2,d2);u=rng.random()*rate
   if u<d:s[i]=0;counts[typ]-=1;counts[0]+=1
   elif u<d+b:
    k=nb[i][rng.randrange(4)]
    if s[k]==0:s[k]=typ;counts[typ]+=1;counts[0]-=1
  trajectories.append(snaps)
 means=[{'t':t,'rho1_mean':statistics.mean(tr[j]['rho1'] for tr in trajectories),'rho2_mean':statistics.mean(tr[j]['rho2'] for tr in trajectories),'rho1_range':[min(tr[j]['rho1'] for tr in trajectories),max(tr[j]['rho1'] for tr in trajectories)]} for j,t in enumerate(targets)]
 results.append({'beta1':b1,'delta1':d1,'beta2':b2,'delta2':d2,'ratio1':b1/d1,'ratio2':b2/d2,'summary':means,'trajectories':trajectories})
out={'L':L,'replicates':6,'initial_probabilities':[.1,.45,.45],'method':'exact uniformized continuous-time process on finite periodic square; total birth rates','seeds':'7007+100*case_id+rep','elapsed_seconds':time.time()-start,'scope':'finite-size and finite-time observations only; cannot establish infinite-volume exclusion','cases':results}
Path('simulation.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for r in results:print({k:v for k,v in r.items() if k!='trajectories'})
print('elapsed',out['elapsed_seconds'])

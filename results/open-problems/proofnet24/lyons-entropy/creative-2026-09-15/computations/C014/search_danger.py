import random,math,json
from phase_explore import danger
rng=random.Random(34014); found=0
for case in range(5000):
 d=[rng.uniform(.04,.96) for _ in range(3)];r=[rng.uniform(.01,.3) for _ in range(3)]
 pf=[]
 for i in range(17):
  co=-1+i/8
  z=danger(d,[r[0],r[1],r[2]*complex(co,math.sqrt(max(0,1-co*co)))])
  if z is not None:pf.append((co,z))
 if len(pf)!=17:continue
 ref=max(pf[0][1],pf[8][1],pf[-1][1]); best=max(pf,key=lambda z:z[1])
 if best[1]>ref+1e-6:
  print(json.dumps(dict(case=case,d=d,r=r,profile=pf,gap=best[1]-ref)),flush=True);found+=1
  if found>=8:break
print('COUNT',found)

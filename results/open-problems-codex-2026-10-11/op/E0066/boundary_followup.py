from pathlib import Path
import json,time,itertools
import numpy as np
from scipy.optimize import linprog
prefix=Path('experiments.py').read_text(encoding='utf-8-sig').split('# Hostile test:')[0]
exec(prefix)
started=time.monotonic();m=4;pairs,n,row,eq,rhs,ub,br=model(m)
perms=np.array(sorted(set(itertools.permutations([.5,.5,0.,0.]))));out=[]
for period in [5,6]:
 for chosen in itertools.combinations(range(1,6),period-1):
  for order in itertools.permutations(chosen):
   if time.monotonic()-started>180:break
   ids=(0,)+order;cycle=perms[list(ids)];A=list(eq);b=list(rhs)
   for t in range(period):
    for k in range(m):A.append(row(cycle[t],k));b.append(cycle[(t+1)%period,k])
   sol=linprog(np.zeros(n),A_ub=ub,b_ub=br,A_eq=A,b_eq=b,bounds=(0,1),method='highs',options={'time_limit':3})
   out.append({'period':period,'ids':ids,'status':int(sol.status)})
   if sol.success:
    Path('boundary_candidate.json').write_text(json.dumps({'cycle':cycle.tolist(),'pairs':pairs,'coefficients':sol.x.tolist()}),encoding='utf8')
summary={'cases':len(out),'statuses':{str(s):sum(x['status']==s for x in out) for s in range(5)},'seconds':time.monotonic()-started}
Path('boundary_followup.json').write_text(json.dumps({'summary':summary,'cases':out},indent=2),encoding='utf8');print(summary)

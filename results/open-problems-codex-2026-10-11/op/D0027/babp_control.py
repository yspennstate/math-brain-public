from pathlib import Path
from fractions import Fraction as F
import json
from tensor_checks import matrices
I=[[F(1),F(0)],[F(0),F(1)]];states=[(0,0),(0,1),(1,0),(1,1)];out=[]
for r in [F(1,2),F(2,3),F(3,4)]:
 p=r*r;q=1-p;A,B,K=matrices(q,r/2,(1+r)/2,'V')
 E=[]
 for i,j in states:
  E.append([(I[i][k]-A[i][k])*B[j][l]+B[i][k]*(I[j][l]-A[j][l]) for k,l in states])
 assert all(sum(row)==0 for row in E)
 assert all(E[i][j]>=0 for i in range(4) for j in range(4) if i!=j)
 assert all(E[i][j]==0 for i in range(4) for j in range(4) if (sum(states[i])-sum(states[j]))%2)
 assert E[0][3]==(1-r)**2/2 and E[3][0]==(1+r)**2/2
 assert E[1][2]==q/2 and E[2][1]==q/2
 out.append({'r':str(r),'q':str(q),'rates':[[str(x) for x in row] for row in E]})
Path('babp_positive_control.json').write_text(json.dumps({'status':'PASS','cases':out},indent=2),encoding='utf8');print('BABP positive control PASS',len(out),flush=True)

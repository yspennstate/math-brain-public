from fractions import Fraction as Q
from pathlib import Path
import json
def restrict(t,j,b):
 return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def H(t):
 w=[sum(t[x]*((-1)**((x&s).bit_count()%2)) for x in range(len(t))) for s in range(len(t))]
 p=[Q(v*v,len(t)**2) for v in w if v]
 assert sum(p)==1
 out=Q(0)
 for z in p:
  assert z.numerator==1 and z.denominator&(z.denominator-1)==0
  out+=z*(z.denominator.bit_length()-1)
 return out
rows=[]
for name,h in [('constant',(1,1)),('character',(1,-1))]:
 t=tuple((1 if (x&1)==0 else (1-2*((x>>1)&1))*h[x>>2]) for x in range(8))
 a,b=restrict(t,1,0),restrict(t,1,1)
 d=H(t)-(H(a)+H(b))/2
 inf=Q(sum(x!=y for x,y in zip(a,b)),len(a))
 assert H(t)==2 and inf==Q(1,2)
 assert d==(2 if name=='constant' else 0)
 rows.append({'seed':name,'truth':t,'H':str(H(t)),'child_entropies':[str(H(a)),str(H(b))],'tag_drop':str(d),'tag_influence':str(inf)})
p=Path(__file__).resolve().parents[1]/'out/tag_boundary.json'
p.write_text(json.dumps({'status':'PASS','cases':rows},indent=2)+'\n',encoding='utf-8',newline='\n')
print('tag boundary: 2 exact cases PASS')

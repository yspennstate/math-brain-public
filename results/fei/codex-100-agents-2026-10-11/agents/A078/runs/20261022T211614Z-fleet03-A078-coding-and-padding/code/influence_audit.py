from pathlib import Path
from fractions import Fraction as Q
import json
R=Path(__file__).resolve().parents[1]
rows=[]
for k in [2,4]:
 for m in [1,2]:
  for d in [1,2]:
   e=Q(1,2**d);n=k+m+1;v=[];w=[]
   for x in range(2**n):
    z=x%2**k;y=1-2*((x>>(k+m))&1)
    v.append(y*(-1)**sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,k,2)))
    w.append(y*(1-2*(x%2**(k+m)==0)))
   f=[v[x>>d] if x%2**d==0 else w[x>>d] if x%2**d==1 else 1 for x in range(2**(n+d))]
   edges=[Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n+d)]
   tiny=Q(2)**(1-k-m);b=Q(2)**(-k//2)
   parts={'shared':sum(edges[:d],Q(0)),'bent_bits':sum(edges[d:d+k],Q(0)),'padding_bits':sum(edges[d+k:d+k+m],Q(0)),'guard_y':edges[-1]}
   predicted={'shared':e*(2*d-1-b+tiny),'bent_bits':e*(Q(k,2)+k*tiny),'padding_bits':e*m*tiny,'guard_y':2*e}
   assert parts==predicted,(k,m,d,parts,predicted)
   assert sum(parts.values(),Q(0))==e*(Q(k,2)+2*d+1-b+(k+m+1)*tiny)
   rows.append({'k':k,'m':m,'d':d,'dimension':n+d,'influence_parts':{a:str(z) for a,z in parts.items()},'total_influence':str(sum(parts.values(),Q(0))),'every_coordinate':[str(x) for x in edges]})
(R/'out/PADDING_INFLUENCE.json').write_text(json.dumps({'status':'PASS','fixtures':rows,'arithmetic':'Fraction; direct directed-edge counts; analytic formulas checked independently'},indent=2),encoding='utf-8',newline='\n')
print('influence fixtures:',len(rows),'PASS')

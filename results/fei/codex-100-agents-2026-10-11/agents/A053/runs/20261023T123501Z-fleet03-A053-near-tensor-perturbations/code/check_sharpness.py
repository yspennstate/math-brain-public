from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
import json,time
import arithmetic as a
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-start>55:raise RuntimeError('55-second guard')
rows=[]
for k in (3,5,7,9):
 R=1<<k;n=R;m=R-1-k;p=Q(1,1<<n);d=Q(1,1<<m);t=Q(1,1<<(m//2));s=1<<m
 cp=(s+(1<<(m//2)))//2;cm=(s-(1<<(m//2)))//2
 groups=[(t-d-2*p,cp),(-t-d-2*p,cm),(d-2*p,s),(-2*p,(1<<n)-2*s)]
 ck(sum(c*v*v for v,c in groups)==1)
 ck(d==2*R*p);ck(t-d-2*p>t/2)
 beta=s*(d-2*p)**2;I=d-2*p
 ck(beta/I==(1-Q(1,R)))
 lower=(m-2)*(1-Q(1,R));ck(beta*(m-2)/I==lower)
 ck(3*Q(7*R-9,16)>=R)
 ck(s*(R+1)<=(1<<n))
 rows.append({'k':k,'n':n,'seed_dimension':m,'edit_count':R+1,'selector_influence':str(I),'occupied_off_anchor_mass':str(beta),'price_lower':str(lower),'price_lower_over_edit_count':str(lower/(R+1)),'root_FEI3':'analytic certified'})
 if k!=3:continue
 L=R-1
 basis=[]
 for j in range(1,R):
  if j&(j-1)==0:continue
  row=1<<(j-1)
  for bit in range(k):
   if j>>bit&1:row^=1<<((1<<bit)-1)
  basis.append(row)
 ck(len(basis)==m)
 code={0}
 for row in basis:code|={v^row for v in list(code)}
 ck(len(code)==s);ck(all(v==0 or v.bit_count()>=3 for v in code))
 def logical(x):return sum(((x&b).bit_count()%2)<<j for j,b in enumerate(basis))
 def bent(y):return -1 if sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m//2))%2 else 1
 seed=[bent(logical(x&((1<<L)-1))) for x in range(1<<n)]
 f=seed.copy();edits=[]
 for x in range(1<<n):
  if x==0 or ((x>>L)&1 and logical(x&((1<<L)-1))==0):f[x]*=-1;edits.append(x)
 ck(len(edits)==R+1);ck(sum(v<0 for v in f)%2==1)
 w=a.fwht(f);fw=a.fwht(seed);support=[i for i,v in enumerate(fw) if v]
 ck(set(support)==code)
 for x,y in combinations(support,2):ck((x^y).bit_count()>=3)
 logical_g=a.fwht([bent(y) for y in range(s)])
 signs={}
 for u in range(s):
  mask=0
  for j,row in enumerate(basis):
   if u>>j&1:mask^=row
  signs[mask]=Q(logical_g[u],s)
 for label,coef in enumerate(w):
  ck(coef!=0)
  pred=signs[label]-d-2*p if label in signs else (d-2*p if (label^(1<<L)) in signs else -2*p)
  ck(Q(coef,1<<n)==pred)
 infs=a.infs(f);ck(infs[L]==I)
 root=a.entropy([Q(v*v,(1<<n)**2) for v in w])
 children=[f[:1<<L],f[1<<L:]]
 hs=[a.entropy([Q(v*v,(1<<L)**2) for v in a.fwht(child)]) for child in children]
 Llo=root[0]-(hs[0][1]+hs[1][1])/2
 ck(Llo/I>=lower);ck(root[1]<=3*sum(infs))
 ck(a.infs(seed)[:L]==[Q(1,2)]*L)
 ck(sum(infs)>=Q(7*R-9,16))
 ck(Counter(Q(v*v,(1<<n)**2) for v in w)==Counter({v*v:sum(c for z,c in groups if z*z==v*v) for v,_ in groups}))
out={'status':'PASS','assertions':checks,'physical_k3_n8_full_spectrum_and_edges':'PASS','compressed_k':[3,5,7,9],'cases':rows,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Hamming-kernel basis and physical Walsh/edges; exact Fraction; rational entropy intervals only for actual n8 fixture'}
(RUN/'out/SHARPNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in out.items() if key!='cases'},indent=2))

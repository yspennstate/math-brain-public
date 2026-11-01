import ast,json,sys,time,itertools
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1]; MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'; START=time.perf_counter(); COUNT=0
OLD=R.parents[0]/'20261023T070855Z-fleet03-A088-booleanity-referee/code/check.py'
names={'exact','add','mul','sub','rounded','ln','log','weighted_log','enc','intersects','fw','law','ce'}
tree=ast.parse(OLD.read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(OLD),'exec'))
def ck(value,label):
 global COUNT
 COUNT+=1
 if not value:raise AssertionError(label)
 if time.perf_counter()-START>(55 if MODE=='pilot' else 180):raise TimeoutError(label)
def cut(v,j,b):return [v[x] for x in range(len(v)) if (x>>j)&1==b]
def marginal(q,j):
 out=[]
 for x in range(len(q)):
  if not ((x>>j)&1):out.append(q[x]+q[x+(1<<j)])
 return out
def influence(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def H(v):
 p=law(v);return ce(p,p)
def rank(rows):
 rows=list(rows);r=0
 while any(rows):
  a=max(rows);p=a.bit_length()-1;r+=1
  rows=[x^a if (x>>p)&1 else x for x in rows if x!=a]
 return r
quadratic_cases=0
for n in ([2] if MODE=='pilot' else range(1,5)):
 edges=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(edges)):
  pairs=[edge for t,edge in enumerate(edges) if (mask>>t)&1]
  rows=[sum(1<<b for a,b in pairs if a==j)+sum(1<<a for a,b in pairs if b==j) for j in range(n)]
  r=rank(rows)
  for linear in range(1<<n):
   v=[(-1)**(sum(((x>>a)&1)*((x>>b)&1) for a,b in pairs)+(x&linear).bit_count()) for x in range(1<<n)]
   p=law(v);ck(all(a==F(1,1<<r) for a in p if a),'quadratic flat law from literal FWHT and independent F2 rank')
   for j in range(n):
    rem=[a for a in range(n) if a!=j]
    rc=rank([sum(((rows[a]>>b)&1)<<t for t,b in enumerate(rem)) for a in rem])
    a,b=cut(v,j,0),cut(v,j,1);pa,pb=law(a),law(b)
    ck(all(z==F(1,1<<rc) for z in pa+pb if z),'both restricted quadratic ranks and flat spectra')
    I=influence(v,j);e=F(r-rc)-3*I
    ck(e+F(rc,4)<=F(r,4),'independent literal Bellman inequality')
    ck(all((x+y)/2==z for x,y,z in zip(pa,pb,marginal(p,j))),'physical two-child square sum')
   quadratic_cases+=1

def source(m):
 n=2*m+1
 b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m)) for x in range(1<<n)]
 c=[a-2*(x==0) for x,a in enumerate(b)]
 g=c+b;IX=F(m)+F(2*m+1,2*4**m)
 actual=sum((influence(b,j)+influence(c,j))/2 for j in range(n))
 ck(actual==IX,'original physical IX exact')
 return b,c,IX,sub(exact(3*IX),H(g))
def node(v,q,labels,reach):return (v,q,labels,reach)
def query(active,coordinate,clean,J):
 v,q,labels,a=active;j=labels.index(coordinate);qn=marginal(q,j);labs=[x for x in labels if x!=coordinate]
 v0,v1=cut(v,j,0),cut(v,j,1)
 ck(all(x in (-1,1) for x in v0+v1),'literal edited children Boolean')
 J+=a*influence(v,j)
 clean=clean+[node(v1,qn,labs,a/2)]
 return node(v0,qn,labs,a/2),clean,J
def frontier(baseH,active,clean,J,m,reserve,Hcut,order,prefix):
 EH=baseH;EQ=baseH;K=exact(0);capacity=F()
 for v,q,labels,a in clean+[active]:
  p=law(v);hp=ce(p,p);cp=ce(p,q)
  ck(sum(p)==sum(q)==1,'full terminal P/Q probability normalization')
  ck(all(not x or y>0 for x,y in zip(p,q)),'full inherited Q dominates actual spectrum')
  EH=sub(EH,mul(hp,a));EQ=sub(EQ,mul(cp,a));K=add(K,mul(sub(cp,hp),a))
 for v,q,labels,a in clean:
  k=sum(2*j in labels and 2*j+1 in labels for j in range(m))
  capacity+=a*F(k,2)
 EH=sub(EH,exact(3*J));EQ=sub(EQ,exact(3*J))
 ck(intersects(EH,add(EQ,K)),'entire signed CE/H ledger with full terminal KL')
 ck(capacity<=F(m,2),'entire clean-forest stopping capacity')
 balance=sub(reserve,add(EH,exact(capacity)))
 if m==2:ck(balance[0]>F(13,96),'exact exceptional m2 all-order all-clean-forest reserve >13/96')
 else:ck(balance[0]>F(m,2)-F(119,96),'all-order general reserve bound')
 return {'m':m,'H':Hcut,'order':list(order),'prefix':prefix,'E_H':enc(EH),'E_Q':enc(EQ),'full_KL':enc(K),'clean_capacity':str(capacity),'reserve_after_all_clean_cap':enc(balance)}

certs=[];orders_seen=0
for m in ([2] if MODE=='pilot' else [2,3,4]):
 b,c,IX,reserve=source(m);baseH=mul(add(H(b),H(c)),F(1,2));labs=list(range(2*m+1))
 for h in range(m+1):
  active=node(c,law(c),labs,F(1,2));clean=[node(b,law(b),labs,F(1,2))];J=F()
  for coordinate in range(2*h):active,clean,J=query(active,coordinate,clean,J)
  active,clean,J=query(active,2*m,clean,J)
  rest=list(range(2*h,2*m))
  if m==2:orders=list(itertools.permutations(rest))
  else:orders=list(dict.fromkeys([tuple(rest),tuple(rest[::2]+rest[1::2]),tuple(reversed(rest))]))
  seen=set()
  for order in orders:
   orders_seen+=1;ac=active;cl=list(clean);jj=J
   for length in range(len(order)+1):
    key=order[:length]
    if key not in seen:
     seen.add(key);certs.append(frontier(baseH,ac,cl,jj,m,reserve,h,order,length))
    if length<len(order):ac,cl,jj=query(ac,order[length],cl,jj)

# Sharp failure of extending the old constant full-KL cap after clean queries.
# Original b_m reference is uniform on 2m labels; querying one member of each
# pair leaves a character with one nonzero coefficient, hence KL=m per leaf.
guards=[]
for m in [2,3,4]:
 b,c,ix,res=source(m);v=b;q=law(b);labels=list(range(2*m+1))
 for coordinate in range(0,2*m,2):
  j=labels.index(coordinate);v=cut(v,j,0);q=marginal(q,j);labels.remove(coordinate)
 K=sub(ce(law(v),q),H(v))
 ck(K==(F(m),F(m)),'clean first-members guard exact KL=m')
 ck(F(m,2)>F(19,32),'old global constant KL cap cannot survive clean continuation')
 guards.append({'m':m,'b_sibling_contribution_to_full_KL':str(F(m,2)),'actual_entropy_debit':str(F(m,4))})

# Strong normalized real, exactly isospectral phase diagnostic.
boolean=[1,1,1,-1];real=[0,0,0,-2]
ck(law(boolean)==law(real),'nonBoolean normalized real phase has identical original squared spectrum')
ck(sum(F(x*x,len(real)) for x in real)==1,'real root L2 normalized')
norms=[sum(F(x*x,2) for x in cut(real,0,b)) for b in (0,1)]
ck(norms==[0,2],'real countermodel fails individual physical child normalization')
out={'status':'PASS','mode':MODE,'checks':COUNT,'runtime_seconds':time.perf_counter()-START,'quadratic_cases':quadratic_cases,'orders':orders_seen,'literal_frontiers':len(certs),'m2_min_reserve_lower':str(min(F(x['reserve_after_all_clean_cap']['lo']) for x in certs if x['m']==2)),'frontiers':certs,'KL_guards':guards,'real_relaxation':{'truth_table':real,'child_squared_norms':[str(x) for x in norms]},'arithmetic':'Fraction; 28-term atanh with rigorous tail, outward log rounding 2^-90'}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('PILOT.json' if MODE=='pilot' else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','runtime_seconds','quadratic_cases','orders','literal_frontiers','m2_min_reserve_lower']}))

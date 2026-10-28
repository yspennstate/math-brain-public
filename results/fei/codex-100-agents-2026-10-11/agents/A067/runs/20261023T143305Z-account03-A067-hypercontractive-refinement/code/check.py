from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast,json,time,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1];mode=sys.argv[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.monotonic()-start<(55 if mode=='pilot' else 180)
# Reuse only named immutable arithmetic helpers; never execute the older search.
helper=A/'runs/20261023T120754Z-account03-A067-hypercontractive-refinement/code/check.py'
names={'wal','sp','rest','marg','inf','TI','ln','lg','pt','add','mul','sub','overlaps','CE','enc'}
tree=ast.parse(helper.read_text(encoding='utf-8'));body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
exec(compile(ast.Module(body=body,type_ignores=[]),str(helper),'exec'));L2=ln(F(2))
def rank(n,edges):
 rows=[sum(1<<j for j in range(n) if j!=i and (min(i,j),max(i,j)) in edges) for i in range(n)];r=0
 for j in range(n):
  p=next((i for i in range(r,n) if rows[i]&(1<<j)),None)
  if p is None:continue
  rows[p],rows[r]=rows[r],rows[p]
  for i in range(n):
   if i!=r and rows[i]&(1<<j):rows[i]^=rows[r]
  r+=1
 return r
def cleanH(v):
 s=[x for x in sp(v) if x];ck(all(x==s[0] for x in s));ck(len(s)&(len(s)-1)==0);return F(len(s).bit_length()-1)
def seed(n,e):return tuple((-1)**sum(((x>>i)&1)*((x>>j)&1) for i,j in e) for x in range(1<<(n+1)))
edges4=[(i,j) for i in range(4) for j in range(i+1,4)];K4=set(edges4)
graphs=[(4,K4)] if mode=='pilot' else [(4,{e for j,e in enumerate(edges4) if mask&(1<<j)}) for mask in range(64) if rank(4,{e for j,e in enumerate(edges4) if mask&(1<<j)})==4]
if mode!='pilot':graphs +=[(6,{(0,1),(2,3),(4,5)}),(6,{(i,j) for i in range(6) for j in range(i+1,6)})]
states=edgescount=fronts=0;guard=None;rows=[]
for gi,(n,e) in enumerate(graphs):
 m=n//2;d=F(1,1<<n);aa=F(1,1<<m);rho=1+((1+aa)/(1-aa))**2
 b=seed(n,e);c=tuple(v-2*(x==0) for x,v in enumerate(b));qb,qc=sp(b),sp(c);ck(rank(n,e)==n);ck(TI(b)==m)
 ck(TI(c)==m+(n+1)*d);hg=CE(sp(b+c),sp(b+c));IX=(TI(b)+TI(c))/2;r2=sub(pt(2*IX),hg);ck(r2[0]>d/8);r4=sub(pt(4*IX),hg)
 allstates={0:(c,qc,list(range(n+1)))}
 for mask in range(1,1<<(n+1)):
  bit=(mask&-mask).bit_length()-1;pm=mask^(1<<bit);v,q,lab=allstates[pm];j=lab.index(bit)
  allstates[mask]=(rest(v,j,0),marg(q,j),[x for x in lab if x!=bit])
 for mask,(v,q,lab) in allstates.items():
  states+=1;p=sp(v);ck(sum(p)==sum(q)==1)
  for j,label in enumerate(lab):
   edgescount+=1;qr=marg(q,j);pr=marg(p,j)
   if label!=n:
    for x,qq in enumerate(q):ck(qr[(x&((1<<j)-1))|((x>>(j+1))<<j)]<=rho*qq)
   v1=rest(v,j,1);h1=cleanH(v1)
   for k in range(len(v1).bit_length()-1):ck(h1-(cleanH(rest(v1,k,0))+cleanH(rest(v1,k,1)))/2-4*inf(v1,k)<=0)
   if guard is None and n==4 and e==K4 and mask==1 and label==1:
    mm=sum(p[x]*qr[(x&((1<<j)-1))|((x>>(j+1))<<j)]!=q[x]*pr[(x&((1<<j)-1))|((x>>(j+1))<<j)] for x in range(len(p)))
    ck(mm>0);cc=CE(p,q);c0=CE(sp(rest(v,j,0)),qr);c1=CE(sp(v1),qr);debit=sub(sub(cc,mul(add(c0,c1),F(1,2))),pt(4*inf(v,j)));ck(debit[1]<0)
    guard={'mismatch_labels':mm,'physical_influence':str(inf(v,j)),'signed_source_debit':enc(debit)}
 hinit=mul(add(pt(n),CE(qc,qc)),F(1,2))
 for shift in range(n+1):
  order=list(range(n+1));order=order[shift:]+order[:shift];active=(c,qc,F(1,2),list(range(n+1)));leaves=[(b,qb,F(1,2))];J=F(0)
  for depth in range(n+2):
   v,q,a,lab=active;hs=cs=ks=pt(0)
   for vv,qq,rr in leaves+[(v,q,a)]:
    pp=sp(vv);hh=CE(pp,pp);cc=CE(pp,qq);hs=add(hs,mul(hh,rr));cs=add(cs,mul(cc,rr));ks=add(ks,mul(sub(cc,hh),rr))
   eh=sub(sub(hinit,hs),pt(4*J));eq=sub(sub(hinit,cs),pt(4*J));ck(eq[1]<F(203,96));ck(ks[1]<=1);ck(eh[1]<F(299,96));ck(overlaps(eh,add(eq,ks)))
   remain=sub(r4,eh);ck(remain[0]>2*m-F(299,96));ck(remain[0]>F(85,96));fronts+=1
   rows.append({'graph':gi,'n':n,'cyclic_shift':shift,'depth':depth,'actual_debit':enc(eh),'full_KL_before_clean':enc(ks),'remaining':enc(remain),'J':str(J)})
   if depth==n+1:break
   j=lab.index(order[depth]);qr=marg(q,j);J+=a*inf(v,j);leaves.append((rest(v,j,1),qr,a/2));active=(rest(v,j,0),qr,a/2,[x for x in lab if x!=order[depth]])
 # Adversarial phase: same flat magnitudes, wrong marked first jet.
 if gi==0:
  wrong=tuple(v*(-1)**(x&1) for x,v in enumerate(b));wc=tuple(v-2*(x==0) for x,v in enumerate(wrong));ck(TI(wc)!=m+(n+1)*d)
ck(guard is not None)
result={'status':'PASS','mode':mode,'checks':checks,'runtime_seconds':time.monotonic()-start,'graphs':len(graphs),'subset_states':states,'local_query_edges':edgescount,'cyclic_prefix_frontiers':fronts,'noncanonical_profile_guard':guard,'frontiers':rows}
(R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if mode=='pilot' else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='frontiers'}))

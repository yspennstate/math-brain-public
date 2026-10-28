from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,hashlib,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
SRC=Path(r'agents\A039\runs\20261014T055326Z-account05-A039-projection-under-restrictions\code\mixed.py')
s=importlib.util.spec_from_file_location('a039_mixed_readonly',SRC);M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
L=M.L;zero=(F(0),F(0));checks=0

def ck(v):
 global checks
 checks+=1
 assert v,checks

def enc(v):return [str(x) for x in v]
def overlap(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def save(o):
 (R/'out/CHECK_RESULTS.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8',newline='\n')
def scalar(m):
 d=F(1,2**(m-1));p0=(1-d)**2;rest=2*d-d*d
 hf=L.add((-p0,L.L(p0)),(-rest,L.L(d*d)))
 H=L.evalformal(hf);tc=L.evalformal(L.add((m,L.h(d)),(-1,hf)))
 sf=L.add((4*(1+(m-2)*d),L.L(F(2))),(-1,hf));S=L.evalformal(sf)
 ck(tc[1]<F(3,5));ck(S[0]>=2 if sf!={2:F(1)} else True)
 # m=2 gives the exact equality S=2, so inspect the formal difference.
 if m==2:ck(L.add((1,sf),(-2,L.L(F(2))))=={})
 return {'m':m,'TC':enc(tc),'twisted_S4':enc(S),'H':enc(H)}
def fixture(n):
 v=[-1 if j==0 else 1 for j in range(2**n)]
 return [-1 if not(t&1) and t&2 else (v[t>>3] if t&1 and t&4 else 1) for t in range(2**(n+3))]
def record_frontier(nodes,E,O,A,n,depth,order):
 facts=[M.info(t) for t,q,w,labels,y in nodes]
 H=M.sumiv(M.scale(w,f[2]) for f,(_,q,w,labels,y) in zip(facts,nodes))
 TC=M.sumiv(M.scale(w,f[3]) for f,(_,q,w,labels,y) in zip(facts,nodes))
 K=M.sumiv(M.scale(w,M.kl(f[0],q)) for f,(_,q,w,labels,y) in zip(facts,nodes))
 S=M.sumiv(M.scale(w,f[4]) for f,(_,q,w,labels,y) in zip(facts,nodes))
 overlap(A,M.plus(E,M.plus(O,K)))
 D=M.sub(M.plus(O,TC),A)
 overlap(D,M.sub(M.sub(TC,K),E))
 ck(D[1]<F(3,10));ck(TC[1]<F(3,10));ck(S[0]>=1)
 # Every twisted-lineage descendant retains at least 2; do not spend other lineage.
 for f,(_,q,w,labels,y) in zip(facts,nodes):
  if y==1:
   exact_gap=L.add((4*sum(f[1])-2,L.L(F(2))),(-1,L.ent(f[0])))
   ck(exact_gap=={} or f[4][0]>=2)
 debit=(max(F(0),D[0]),max(F(0),D[1]));remain=M.sub((F(3,4),F(3,4)),debit);ck(remain[0]>F(9,20))
 return {'n':n,'depth':depth,'order':order,'extra_conversion_D':enc(D),'mean_terminal_TC':enc(TC),'mean_terminal_H':enc(H),'mean_terminal_S4':enc(S),'mean_terminal_inherited_KL':enc(K),'root_A':enc(A),'erasure_E':enc(E),'outcome_O':enc(O),'unused_original_bank_after_prior_and_conversion':enc(remain),'terminal_count':len(nodes)}
def run(n,full):
 tab=fixture(n);p,d,*_=M.info(tab);Q,c=M.rootref(p,d);A=M.kl(p,Q)
 tabs,qs,E0,O0,rows=M.step(tab,Q,1);edges={}
 for y in range(2):
  for j in range(n):edges[y,j]=M.step(tabs[y],qs[y],2+j)
 rowsout=[]
 for j0 in range(n):
  for j1 in range(n):
   nodes=[];E=E0;O=O0
   for y,j in enumerate([j0,j1]):
    ts,rr,e,o,z=edges[y,j];E=M.plus(E,M.scale(F(1,2),e));O=M.plus(O,M.scale(F(1,2),o))
    labels=[0,2]+[3+k for k in range(n) if k!=j]
    for t,q in zip(ts,rr):nodes.append((t,q,F(1,4),labels,y))
   row=record_frontier(nodes,E,O,A,n,1,[j0,j1]);rowsout.append(row)
 if full:
  for direction in ['ascending','descending']:
   nodes=[(tabs[y],qs[y],F(1,2),[0,2]+list(range(3,n+3)),y) for y in range(2)];E=E0;O=O0
   for depth in range(1,n+1):
    nxt=[]
    for t,q,w,labels,y in nodes:
     data=[z for z in labels if z>=3];label=min(data) if direction=='ascending' else max(data);i=labels.index(label)
     ts,qq,e,o,z=M.step(t,q,i);E=M.plus(E,M.scale(w,e));O=M.plus(O,M.scale(w,o));ll=[z for z in labels if z!=label]
     for tt,qr in zip(ts,qq):nxt.append((tt,qr,w/2,ll,y))
    nodes=nxt;rowsout.append(record_frontier(nodes,E,O,A,n,depth,direction))
 return rowsout
start=time.perf_counter();pilot='--pilot' in sys.argv
scalars=[scalar(m) for m in range(2,13)]
# Exact tail: m(m+1/2)2^(1-m) <=17/32 for all m>=8, by ratio<1.
for m in range(8,33):
 ck(F(m*(2*m+1),2**m)<=F(17,32));ck((m+1)*(2*m+3)<2*m*(2*m+1))
rows=[]
for n in ([2] if pilot else [2,3,4]):
 rows.extend(run(n,n<=3));L.log2.cache_clear()
 save({'status':'RUNNING','rows':rows,'scalar_certificates':scalars})
 ck(time.perf_counter()-start<(60 if pilot else 1200))
result={'status':'PASS','checks':checks+M.checks,'own_checks':checks,'helper_checks':M.checks,'runtime_seconds':time.perf_counter()-start,'two_query_policies':sum(isinstance(x['order'],list) for x in rows),'continuation_frontiers':sum(isinstance(x['order'],str) for x in rows),'scalar_certificates':scalars,'rows':rows,'helper_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'independent_review':'PENDING','formal_status':'not established by this checker'}
save(result);print(json.dumps({k:v for k,v in result.items() if k not in ['rows','scalar_certificates']}))

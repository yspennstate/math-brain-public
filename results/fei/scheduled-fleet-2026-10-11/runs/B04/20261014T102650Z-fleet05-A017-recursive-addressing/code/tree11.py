"""A017-eleven-edit-tree-v1: exact retained-label/root/terminal integration."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,itertools,time,argparse,hashlib
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
sp=importlib.util.spec_from_file_location('rational',old);U=importlib.util.module_from_spec(sp);sp.loader.exec_module(U)
checks=nodes=leaves=0;digest=hashlib.sha256()
def req(ok,msg=''):
 global checks
 checks+=1
 if not ok:raise AssertionError((checks,msg))
def nonnegative(x,msg=''):req(x.interval()[0]>=0,msg)
def restrict(g,n,i,b):return [g[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))]
def configs(pilot=False):
 for n in [3] if pilot else [3,4,5,6]:
  for code in U.graph_codes(n)[:1 if pilot else 4]:
   for ell in [0,(1<<n)-1]:
    for rows in [[],[1],[1,2],[3,5]][:2 if pilot else 4]:
     K=[x for x in range(1<<n) if U.addr(rows,x)==0];sets={(),tuple(K[:min(10,len(K))]),tuple(K[:min(11,len(K))]),tuple(sorted(x^1 for x in K[:min(11,len(K))]))}
     for E in sorted(sets):yield n,rows,code|ell,E
def fixtures():
 E=(7,11,15,19,23,27,31)
 return [(5,[],U.poly_code(5,[(0,1),(1,2),(3,4)]),E),(5,[],U.poly_code(5,[(0,1)]),E)]

def tree(g,b,labels,ids,Q):
 global nodes,leaves
 n=len(ids);sp=U.spectrum(g,labels);inf=U.spectral_metrics(sp,n)[0];H=U.entropy(sp,n)
 active=[i for i in range(n) if any(labels[x]!=labels[x^(1<<i)] for x in range(1<<n))]
 polar=[i for i in range(n) if Q[ids[i]]&sum(1<<j for j in ids)]
 edits=sum(a!=c for a,c in zip(g,b));req(edits<=11)
 if not active and (not edits or (not polar and n>=6) or n==0):
  leaves+=1;req(len(set(labels))==1)
  nonnegative(U.LF(F(34,5)*sum(inf)).add(H,-1),'paid terminal including induced character')
  return F(0),sum(inf)
 if not active and n<=5:
  i=max(range(n),key=lambda j:inf[j])
 else:i=active[0] if active else polar[0]
 nodes+=1;B=U.erasure(sp,n,i)
 nonnegative(U.LF(4*inf[i]).add(B,-1),'K4 query good')
 result=[];decrement=U.LF().add(H)
 for bit in [0,1]:
  cg,cb,cl=[restrict(v,n,i,bit) for v in [g,b,labels]]
  decrement.add(U.entropy(U.spectrum(cg,cl),n-1),-F(1,2))
  result.append(tree(cg,cb,cl,ids[:i]+ids[i+1:],Q))
 nonnegative(U.LF((4+2/U.LN2[1])*inf[i]).add(decrement,-1),'entropy decrement')
 spent=inf[i]+sum(a for a,b in result)/2;terminal=sum(b for a,b in result)/2
 req(spent+terminal==sum(inf),'influence partition')
 return spent,terminal
def root(n,rows,code,E):
 ell,edges,Q=U.parameters(n,code);b=U.signs(n,ell,edges);g=b.copy()
 for x in E:g[x]*=-1
 labels=[U.addr(rows,x) for x in range(1<<n)];req(len({labels[x] for x in E})<=1)
 sp=U.spectrum(g,labels);bp=U.spectrum(b,labels)
 for z,w in sp.items():
  for s,amp in enumerate(w):req(amp==bp[z][s]-2*sum(b[x]*(-1)**U.parity(s&x) for x in E if labels[x]==z),'exact coherent correction')
 inf,pairs,C,dc=U.spectral_metrics(sp,n);pi,pp,pdc=U.physical(g,labels,n)
 req((inf,pairs,dc)==(pi,pp,pdc),'independent physical first/second derivatives')
 for i in range(n):
  active=any(row>>i&1 for row in rows);base=F(1,2) if active or Q[i] else F(ell>>i&1)
  change=0 if active else F(2,1<<n)*sum((-1)**((ell>>i&1)^U.parity(Q[i]&x)) for x in E if x^(1<<i) not in E)
  req(inf[i]==base+change,'crossing edge owner')
 H=U.entropy(sp,n);rank=U.rank(rows);basis=U.kernel(rows,n);fiberH=U.LF(2*rank)
 for z in set(labels):
  origin=labels.index(z);vals=[]
  for t in range(1<<len(basis)):
   x=origin
   for j,vec in enumerate(basis):
    if t>>j&1:x^=vec
   vals.append(g[x])
  fiberH.add(U.entropy({0:U.fwht(vals)},len(basis)),F(1,1<<rank))
 req(fiberH==H,'kernel-basis fiber entropy without relabeling influence')
 spent,terminal=tree(g,b,labels,list(range(n)),Q)
 req(spent+terminal==sum(inf))
 nonnegative(U.LF((4+2/U.LN2[1])*(spent+terminal)).add(H,-1),'full terminal-inclusive proof ledger')
 digest.update(json.dumps([n,rows,code,E,[str(v) for v in inf]],sort_keys=True).encode()+b'\n')
def leafconfigs(pilot=False):
 for n in [6] if pilot else [6,7,8]:
  for s in [1,10,11]:yield n,tuple(range(s))
def main():
 start=time.perf_counter();ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--plan',action='store_true');a=ap.parse_args()
 if a.plan:print(json.dumps(dict(pilot_roots=sum(1 for x in configs(True))+2,full_roots=sum(1 for x in configs())+2,pilot_leaves=sum(1 for x in leafconfigs(True)),full_leaves=sum(1 for x in leafconfigs()))));return
 roots=leafcases=0
 for c in list(configs(a.pilot))+fixtures():root(*c);roots+=1
 for n,E in leafconfigs(a.pilot):
  g=[-1 if x in E else 1 for x in range(1<<n)];sp={0:U.fwht(g)};H=U.entropy(sp,n);inf=U.spectral_metrics(sp,n)[0]
  worst=sum(min(t,1-t) for t in inf) # exact minimum over ALL characters, not a sampled phase
  nonnegative(U.LF(F(34,5)*worst).add(H,-1),'five-point terminal all characters')
  leafcases+=1
 result=dict(status='PASS',helper='A017-eleven-edit-tree-v1',pilot=a.pilot,roots=roots,queried_nodes=nodes,stopping_leaves=leaves,terminal_sets_all_characters=leafcases,K4_bad_queried_nodes=0,assertions=checks,utility_assertions=U.CHECKS,elapsed_seconds=time.perf_counter()-start,coverage_sha256=digest.hexdigest())
 (R/'out'/('tree11_pilot.json' if a.pilot else 'tree11_validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
if __name__=='__main__':main()

from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys,itertools
import exact as E
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;start=time.perf_counter()
checks=rows=eligible=liquidating=competitors=0
def ck(v,msg):
 global checks
 checks+=1
 if not v:raise AssertionError(msg)
def lc(v):return {2:Q(v)} if v else {}
def add(a,b,w=Q(1)):return E.add(a,b,w)
def sc(a,w):return add({},a,w)
@lru_cache(None)
def H(g):return E.entropy(E.walsh(g))
def I(g):return E.influence(E.walsh(g))
def cut(g,i,a):return E.slice_table(g,i,a)
def D(g,i):return add(H(g),add(H(cut(g,i,0)),H(cut(g,i,1))),-Q(1,2))
def sign(a):
 if not a:return 0
 lo,hi=E.bounds(a)
 if lo>=0:return 1
 if hi<=0:return -1
 raise AssertionError('unresolved exact sign')
def le(a,b,msg):ck(sign(add(b,a,-1))>=0,msg)
def biv(a):
 lo,hi=E.bounds(a);l,h=E.ln(Q(2));v=[lo/l,lo/h,hi/l,hi/h];return min(v),max(v)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def scale(a,b):return times(a,(b,b))
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def ivle(a,b,msg):ck(a[1]<=b[0],msg)
A=Q(6)
for n in range(0,(2 if pilot else 3)+1):
 for mask in range(1<<(1<<n)):
  g=tuple(1-2*((mask>>x)&1) for x in range(1<<n));ii=I(g)
  for j in range(n):
   rows+=1;cs=[cut(g,j,a) for a in (0,1)];hh=[H(c) for c in cs];jj=[I(c) for c in cs];p=E.influence(E.walsh(g),j);dd=D(g,j)
   ck(ii==p+sum(jj)/2,'physical influence conservation')
   ck(add(H(g),dd,-1)==sc(add(hh[0],hh[1]),Q(1,2)),'full child entropy')
   for u in (Q(0),Q(1,16)):
    cash=A*ii-u
    if sign(add(lc(cash),dd,-1))<0:continue
    eligible+=1;ex=add(dd,lc(u-A*p));ex={} if sign(ex)<=0 else ex
    if not ex:continue
    liquidating+=1
    pos=[a for a in (0,1) if jj[a]>0];ck(bool(pos),'positive liquidation has capacity')
    for a in (0,1):
     if jj[a]==0:ck(not hh[a],'zero influence child entropy zero')
    if len(pos)==2 and sign(add(sc(hh[0],jj[1]),sc(hh[1],jj[0]),-1))>0:pos.reverse()
    first=pos[0];cap=A*jj[first]/2
    if sign(add(lc(cap),ex,-1))>=0:
     opt=times(biv(ex),biv(sc(hh[first],1/(A*jj[first]))))
     opt_exact=sc(hh[first],ex.get(2,Q(0))/(A*jj[first])) if set(ex)<=set([2]) else None
    else:
     ck(len(pos)==2,'second capacity exists');second=pos[1]
     rem=add(ex,lc(cap),-1)
     opt=plus(biv(sc(hh[first],Q(1,2))),times(biv(rem),biv(sc(hh[second],1/(A*jj[second])))))
     opt_exact=add(sc(hh[first],Q(1,2)),sc(hh[second],rem.get(2,Q(0))/(A*jj[second]))) if set(rem)<=set([2]) else None
    for w0,w1 in itertools.product([Q(x,4) for x in range(5)],repeat=2):
     discarded=A*(w0*jj[0]+w1*jj[1])/2
     if sign(add(lc(discarded),ex,-1))<0:continue
     competitors+=1;frozen=add(sc(hh[0],w0/2),hh[1],w1/2)
     live=add(sc(hh[0],(1-w0)/2),hh[1],(1-w1)/2)
     ck(add(frozen,live)==sc(add(hh[0],hh[1]),Q(1,2)),'both frozen+live full children retained')
     if opt_exact is not None:le(opt_exact,frozen,'exact local optimum dual')
     else:ivle(opt,biv(frozen),'interval-certified local optimum dual')
  if time.perf_counter()-start>55:raise RuntimeError('frozen cap')
# Actual rate6 rare-tag seed; no shared-variable copies or large truth table.
m=8;N0=1<<m;c=Q(1,N0)
b=tuple((-1)**sum(((x>>(2*l))&1)*((x>>(2*l+1))&1) for l in range(4)) for x in range(N0))
C=tuple(int(x==N0-1) for x in range(N0));K=tuple(b[x]-C[x] for x in range(N0));g=tuple(K[x]+v*C[x] for v in (1,-1) for x in range(N0))
cs=[cut(g,m,a) for a in (0,1)];hh=[H(x) for x in cs];jj=[I(x) for x in cs];dd=D(g,m);p=E.influence(E.walsh(g),m);ex=add(dd,lc(-A*p));ev=biv(ex)
ck(p==c,'actual rare tag density');le(lc(7*c),dd,'seed D>=7c');le(lc(c),ex,'positive excess beyond rate6')
le(dd,lc(A*I(g)),'actual source query cash admissible')
res=[];precision=0
for N in range(1,(4 if pilot else 64)+1):
 ja=[x+N for x in jj];ha=[add(x,lc(2*N)) for x in hh]
 ck(all(ev[1]<A*x/2 for x in ja),'single outcome capacity')
 ratios=[biv(sc(ha[a],1/(A*ja[a]))) for a in (0,1)]
 which=0 if sign(add(sc(ha[0],ja[1]),sc(ha[1],ja[0]),-1))<=0 else 1
 opt=times(ev,ratios[which]);common=times(ev,biv(sc(add(ha[0],ha[1]),1/(A*sum(ja)))))
 residuals=[biv(add(hh[a],lc(-2*jj[a]))) for a in (0,1)];M=max(abs(z) for pair in residuals for z in pair)
 center=scale(ev,Q(1,3));err=ev[1]*M/(A*N)
 ck(opt[0]>=center[0]-err and opt[1]<=center[1]+err,'reservoir positive-limit error bound')
 ck(common[1]-opt[0]<=2*err,'entire outcome advantage O(1/N)')
 widths=range(0,13)
 for width in widths:
  precision+=1;B=1<<width
  # Certified conservative ceiling of mandatory discarded fraction.
  frac=scale(ev,Q(2)/(A*ja[which]));w=Q(-((-frac[1].numerator*B)//frac[1].denominator),B)
  ck(0<w<=1,'physical dyadic liquidation probability')
  frozen=biv(sc(ha[which],w/2))
  ck(A*w*ja[which]/2>=ev[1],'physical original capacity feasible')
  ck(frozen[0]>=Q(N,B),'physical entropy lower bound Ns/2^(b+1)')
  # Rounding loss, including the explicitly certified log enclosure width.
  error=Q(1,B)+(frac[1]-frac[0])
  ck(frozen[1]-opt[0]<=biv(sc(add(ha[0],ha[1]),error/2))[1]+Q(1,10**15),'finite coin rounding tail bound')
 res.append({'N':N,'optimal_frozen_bits':[str(z) for z in opt],'common_frozen_bits':[str(z) for z in common]})
# ALL-outcome adaptive distinct-touch identity on actual complete/early-stop trees.
tree_nodes=tree_leaves=0
def product_table(N):return tuple((-1)**sum(((x>>(2*j))&3)==3 for j in range(N)) for x in range(1<<(2*N)))
for N in (1,2,3):
 root=product_table(N)
 def visit(tab,labels,touched,depth):
  global tree_nodes,tree_leaves
  tree_nodes+=1
  untouched=N-len(touched)
  if not labels or (depth>=2 and sum(tab)>0 and depth%2==0):
   tree_leaves+=1;ck(H(tab)==lc(2*untouched),'all adaptive full-terminal product entropy')
   return Q(1),Q(untouched),H(tab)
  j=max(range(len(labels)),key=lambda k:(E.influence(E.walsh(tab),k),labels[k]))
  factor=labels[j]//2;nextlabels=labels[:j]+labels[j+1:]
  ch=[visit(cut(tab,j,a),nextlabels,touched|{factor},depth+1) for a in (0,1)]
  weight=(ch[0][0]+ch[1][0])/2;u=(ch[0][1]+ch[1][1])/2;h=sc(add(ch[0][2],ch[1][2]),Q(1,2))
  ck(h==lc(2*u),'full adaptive terminal law')
  return weight,u,h
 wt,uu,ht=visit(root,tuple(range(2*N)),set(),0);ck(wt==1,'all actual outcome leaves retained')
result={'status':'PASS','pilot':pilot,'assertions':checks,'coordinate_rows':rows,'eligible_received_states':eligible,'liquidating_states':liquidating,'feasible_grid_competitors':competitors,'reservoir_rows':res,'precision_guards':precision,'adaptive_tree_nodes':tree_nodes,'adaptive_tree_leaves':tree_leaves,'seed_excess_bits':[str(z) for z in ev],'seed_child_influences':[str(x) for x in jj],'seconds':time.perf_counter()-start}
(R/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['reservoir_rows','seed_excess_bits']}))

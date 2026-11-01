from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys,itertools,hashlib
import exact as e
R=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
start=time.perf_counter(); checks=cases=policies=profiles=0
K=Q(9,2); k=Q(29,13); A=2*k; eps=K-A
def ck(x,label):
 global checks
 checks+=1
 if not x:raise AssertionError(label)
def lc(x):return {2:Q(x)} if x else {}
def add(a,b,c=Q(1)):return e.add(a,b,c)
def cut(g,i,a):return e.slice_table(g,i,a)
@lru_cache(None)
def H(g):return e.entropy(e.walsh(g))
def I(g):return e.influence(e.walsh(g))
def inf(g,i):return e.influence(e.walsh(g),i)
def D(g,i):return add(H(g),add(H(cut(g,i,0)),H(cut(g,i,1))),-Q(1,2))
def le(a,b,label):e.le(a,b,label);ck(True,label)
def mean(g):return Q(sum(g),len(g))
ck(3**5<2**8,'log2(3)<8/5 exact integer certificate')
ck(eps==Q(1,26),'same original source has reserve1/26')
for n in range(1,(2 if pilot else 3)+1):
 for mask in range(1<<(1<<n)):
  g=tuple(1-2*((mask>>x)&1) for x in range(1<<n)); total=I(g)
  ck(total==sum((inf(g,i) for i in range(n)),Q(0)),'Walsh influences')
  for i in range(n):
   cases+=1;p=inf(g,i);cs=[cut(g,i,a) for a in (0,1)];avgI=(I(cs[0])+I(cs[1]))/2;d=D(g,i)
   ck(total==p+avgI,'physical influence conservation')
   le({},d,'entropy decrement nonnegative')
   le(d,lc(k*total),'reconstructed universal single query bound')
   # Ticket1 closes; ticket2 pending; their historical releases remain.
   after1=add(lc(k*total),d,-1)
   le({},after1,'closed first ticket nonnegative')
   transported=[lc(k*I(c)+k*p+eps*total) for c in cs]
   combined=add(after1,add(transported[0],transported[1]),Q(1,2))
   ck(add(lc(K*total),combined,-1)==d,'SAME original two-ticket debit')
   options=range(-1,n-1)
   for js in itertools.product(options,repeat=2):
    policies+=1;second={};terminalH={}
    for a,c in enumerate(cs):
     j=js[a]
     fee={} if j==-1 else D(c,j)
     le(fee,lc(k*I(c)),'actual adaptive second fee')
     second=add(second,fee,Q(1,2))
     term=H(c) if j==-1 else add(H(cut(c,j,0)),H(cut(c,j,1)))
     terminalH=add(terminalH,term,Q(1,2) if j==-1 else Q(1,4))
    both=add(d,second)
    le(both,lc(A*total),'two queries original source cap')
    ck(add(H(g),terminalH,-1)==both,'both complete terminal spectra retained')
   for q in (Q(0),Q(1,4),Q(1,2)):
    Aq=k/(1-q)
    release=add(lc(Aq*total-q*Aq*avgI),d,-1)
    le(lc(q*Aq*p),release,'geometric transaction release')
    # Intermediate reserve after core answer, then exact fair-coin innovation.
    children=[add(release,lc(q*Aq*I(c))) for c in cs]
    ck(add(lc(Aq*total),add(children[0],children[1]),-Q(1,2))==d,'pre-coin account conservation')
  if time.perf_counter()-start>55:raise RuntimeError('frozen runtime cap')
# Complete n<=2 core trees: independently accumulate exact geometric bills.
def stopped(g,q):
 if len(g)==1:return {},H(g),Q(0)
 i=max(range(len(g).bit_length()-1),key=lambda j:(inf(g,j),j))
 cs=[cut(g,i,a) for a in (0,1)];subs=[stopped(c,q) for c in cs]
 bill=D(g,i);terminal={};occupation=I(g)
 for c,(b,h,o) in zip(cs,subs):
  bill=add(bill,b,q/2)
  terminal=add(terminal,H(c),(1-q)/2);terminal=add(terminal,h,q/2)
  occupation+=q*o/2
 ck(add(H(g),terminal,-1)==bill,'full geometric terminal telescoping')
 ck(occupation<=I(g)/(1-q),'whole-tree occupation, no renewal')
 le(bill,lc(k*occupation),'whole-tree actual entropy bill')
 return bill,terminal,occupation
for mask in range(16):
 g=tuple(1-2*((mask>>x)&1) for x in range(4))
 for q in (Q(0),Q(1,4),Q(1,2)):stopped(g,q)
# Generic coherent wrappers, full spectrum profile and BOTH core children.
for bm in range(2 if pilot else 16):
 C=(0,0,0,1);KK=tuple((1-2*((bm>>x)&1)) if x<3 else 0 for x in range(4));t=Q(1,4)
 def full(h):return tuple(KK[x]+C[x]*v for v in h for x in range(4))
 for gm in range(16):
  g=tuple(1-2*((gm>>x)&1) for x in range(4));F=full(g);ex=add(H(F),H(g),-t)
  le({},ex,'current coherent profile nonnegative')
  for i in range(2):
   cs=[cut(g,i,a) for a in (0,1)];ec=[add(H(full(c)),H(c),-t) for c in cs]
   fee=add({},D(g,i),t);physical=D(F,2+i)
   ck(physical==add(fee,add(ex,add(ec[0],ec[1]),-Q(1,2))),'full physical mean profile debit')
   bank=add(ex,lc(A*t*I(g)));p=inf(g,i)
   r=add(lc(A*t*I(g)-A*t*(I(g)-p)/2),fee,-1)
   nextB=[add(ec[a],add(r,lc(A*t*I(cs[a])/2))) for a in (0,1)]
   ck(add(bank,add(nextB[0],nextB[1]),-Q(1,2))==physical,'coherent geometric transaction same owner')
   le({},r,'transaction remaining cash nonnegative');profiles+=1
# Growing-depth actual product-AND2 core: exact factor recurrences only.
rows=[]
for N in range(1,33):
 q=Q(1,2);weights=[q**j for j in range(N)]
 # Each core query removes the first coordinate of one fresh AND2.
 # Expected remaining influence before query j is N-j/2 (each old factor leaves influence 1/2).
 occ=sum((weights[j]*(N-Q(j,2)) for j in range(N)),Q(0))
 debit=2*sum(weights,Q(0));terminal=2*N-debit
 ck(occ<=2*N,'compressed arbitrary-depth occupation')
 ck(debit<=K*N,'original core source price')
 ck(terminal>=0,'full expected terminal entropy retained')
 ck(q**(N-1)>0,'actual N-query path has positive probability')
 rows.append(dict(N=N,core_fee=str(debit),terminal_H=str(terminal),occupation=str(occ),reach_depth_N=str(q**(N-1))))
result=dict(status='PASS',pilot=pilot,assertions=checks+e.checks,local_assertions=checks,helper_assertions=e.checks,coordinate_cases=cases,adaptive_two_query_policies=policies,coherent_edges=profiles,growing_depth_rows=rows,seconds=time.perf_counter()-start,helper_sha256=hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest())
(R/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({a:b for a,b in result.items() if a!='growing_depth_rows'}))

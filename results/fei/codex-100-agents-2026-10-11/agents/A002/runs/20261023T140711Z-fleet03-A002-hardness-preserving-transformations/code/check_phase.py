import sys,time,json,itertools
from pathlib import Path
from functools import lru_cache
import exactlib as E
from exactlib import Q,add,logq,ok,rankadd,fw
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); pilot='--pilot' in sys.argv
counts={'rank_fixtures':0,'phases':0,'candidate_pairs':0,'applicable_pairs':0,'strict_refinement_pairs':0}; example=None
@lru_cache(None)
def entinterval(v): return E.interval(dict(v))
@lru_cache(None)
def st(f):
 N=len(f); n=N.bit_length()-1; W=tuple(fw(f)); H=tuple(sorted(add(*[(1,logq(Q(w,N))) for w in W if w]).items()))
 cor=fw([w*w for w in W]); cost=tuple((N*N-z)//(2*N) for z in cor); m=tuple(min(c,N-c) for c in cost)
 basis={}; B=[]
 for v in sorted(range(1,N),key=lambda v:(m[v],v)):
  if rankadd(basis,v): B.append(v)
 aa=sum(m[v] for v in B); supp=[s for s,w in enumerate(W) if w]; wb={}
 for s in supp:rankadd(wb,s^supp[0])
 kb={}
 for v in range(N):
  if m[v]==0:rankadd(kb,v)
 beta=min((m[v] for v in range(N) if m[v]),default=N)
 return {'n':n,'N':N,'W':W,'H':H,'cost':cost,'m':m,'a':aa,'B':tuple(B),'r':len(wb),'wb':wb,'kb':kb,'s0':supp[0],'beta':beta}
def reduce(v,b):
 for j in sorted(b,reverse=True):
  if (v>>j)&1:v^=b[j]
 return v
def rankcheck(f):
 s=st(f);N=s['N'];n=s['n'];ok(s['r']+len(s['kb'])==n)
 for v in range(N):
  ok(s['cost'][v]==sum(f[x]!=f[x^v] for x in range(N)))
  for w in range(N):
   if s['m'][w]==0:ok(s['m'][v^w]==s['m'][v])
 counts['rank_fixtures']+=1
for n in range((1 if pilot else 3)+1):
 for v in range(1<<(1<<n)):rankcheck(tuple(1 if (v>>x)&1 else -1 for x in range(1<<n)))
mon=[s for s in range(16) if s.bit_count()>=2]
phases=range(16 if pilot else 2048)
roots=[tuple(-1 if x==j else 1 for x in range(16)) for j in range(16)]+[(1,)*16,tuple(-1 if x in (0,1) else 1 for x in range(16))]
if pilot:roots=roots[:2]+[roots[16]]
for idx in phases:
 P=tuple((-1)**sum(1 for j,m in enumerate(mon) if (idx>>j)&1 and (x&m)==m) for x in range(16));sp=st(P);rankcheck(P);counts['phases']+=1
 r=sp['r'];beta=sp['beta'];N=16
 # full affine rank is the quotient rank, not physical variable count
 for f in roots:
  counts['candidate_pairs']+=1;neg=sum(y<0 for y in f);sf=st(f)
  if sp['beta']<4*neg:continue
  counts['applicable_pairs']+=1; g=tuple(a*b for a,b in zip(f,P));sg=st(g)
  ok(sg['a']-sf['a']>=sp['a']-4*neg*r);ok(sg['a']-sf['a']>=r*(beta-4*neg))
  # executable independent quotient subset in an ACTUAL optimal product basis
  qb={};C=[]
  for v in sg['B']:
   if rankadd(qb,reduce(v,sp['kb'])):C.append(v)
  ok(len(C)==r);ok(sum(sp['m'][v] for v in C)>=sp['a']);ok(sum(sf['m'][v] for v in sg['B'])>=sf['a'])
  for v in sg['B']:
   if sp['m'][v]:ok(sg['m'][v]-sf['m'][v]>=sp['m'][v]-4*neg>=0)
   else:ok(sg['m'][v]==sf['m'][v])
  # direct coset norm conservation after one character shift
  before={};after={}
  for s in range(N):
   b=reduce(s,sp['wb']);before[b]=before.get(b,0)+sf['W'][s]**2
   b=reduce(s^sp['s0'],sp['wb']);after[b]=after.get(b,0)+sg['W'][s]**2
  ok(before==after)
  diff=tuple(sorted(add((1,dict(sg['H'])),(-1,dict(sf['H']))).items()));lo,hi=entinterval(diff);ok(hi<=r)
  for K in (0,4,8,20):ok(hi-Q(K*(sg['a']-sf['a']),N)<=r-Q(K*(sp['a']-4*neg*r),N))
  if sp['a']>r*beta:
   counts['strict_refinement_pairs']+=1
   if neg==1 and example is None:example={'phase_index':idx,'ANF_monomial_masks':[m for j,m in enumerate(mon) if (idx>>j)&1],'negative_point':f.index(-1),'rank':r,'beta':str(Q(beta,N)),'a_phase':str(Q(sp['a'],N)),'old_charge':str(Q(r*(beta-4*neg),N)),'new_charge':str(Q(sp['a']-4*neg*r,N)),'actual_influence_gain':str(Q(sg['a']-sf['a'],N)),'K20_new_deficit_upper':str(r-Q(20*(sp['a']-4*neg*r),N))}
if not pilot:ok(example is not None)
out={'status':'PASS','assertions':E.checks,'counts':counts,'strict_example':example,'elapsed_seconds':time.monotonic()-start,'pilot':pilot,'method':'integer Walsh autocorrelation, exact centered minimum bases and quotient subset, coset norms, rational entropy intervals'}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

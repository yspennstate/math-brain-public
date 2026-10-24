"""Structural independent certificate check of the posterior-median constrained optimum."""
import pathlib,json,time
from fractions import Fraction
from functools import cache
P=pathlib.Path(__file__).parent;start=time.monotonic();d=json.loads((P/'median_ties_certificate.json').read_text());rows={r['id']:r for r in d['rows']}
@cache
def expr(t):
 if t<2:return t
 if t==2:return 'u'
 return tuple(expr(c) for c in d['nodes'][t])
def norm(e):
 if not isinstance(e,tuple):return e
 cs=[norm(c) for c in e]
 if cs.count(0)>=2:return 0
 if cs.count(1)>=2:return 1
 if 0 in cs and 1 in cs:return next(c for c in cs if c!=0 and c!=1)
 return tuple(sorted(cs,key=repr))
@cache
def prob(e):
 if e=='u':return Fraction(1,2)
 if isinstance(e,int):return Fraction(e)
 a,b,c=map(prob,e);return a*b+a*c+b*c-2*a*b*c
def eligible_paths(e,p=()):
 if e=='u':yield p
 elif isinstance(e,tuple):
  qs=list(map(prob,e));med=sorted(qs)[1]
  for i,c in enumerate(e):
   if qs[i]==med:yield from eligible_paths(c,p+(i,))
def all_paths(e):
 if e=='u':return 1
 if isinstance(e,int):return 0
 return sum(all_paths(c) for c in e)
def substitute(e,p,b):
 if not p:return b
 cs=list(e);cs[p[0]]=substitute(cs[p[0]],p[1:],b);return tuple(cs)
canon={s:norm(expr(s)) for s in rows};errors=[];transitions=0
for s,r in rows.items():
 e=expr(s);m=all_paths(e);assert m==d['sizes'][s]
 expected={(norm(substitute(e,p,0)),norm(substitute(e,p,1))) for p in eligible_paths(e)}
 supplied={(canon[a],canon[b]) for a,b in r['moves']}
 if expected!=supplied:errors.append(('allowed moves',s))
 transitions+=len(supplied)
 if s<2:
  if r['weight']!=0:errors.append(('constant',s))
 else:
  scores=[]
  for a,b in r['moves']:
   assert d['sizes'][a]<m and d['sizes'][b]<m
   scores.append((1<<m)+(rows[a]['weight']<<(m-1-d['sizes'][a]))+(rows[b]['weight']<<(m-1-d['sizes'][b])))
  if r['weight']!=min(scores):errors.append(('Bellman',s))
assert not errors
root=d['root'];cost=Fraction(rows[root]['weight'],1<<d['sizes'][root]);assert cost==Fraction(257554309,16777216)
unrestricted=Fraction(15796051,1048576);gap=cost-unrestricted;assert gap==Fraction(4817493,16777216)>0
out=dict(states=len(rows),transition_pairs=transitions,errors=errors,cost=str(cost),unrestricted=str(unrestricted),gap=str(gap),seconds=time.monotonic()-start)
(P/'median_verification.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))

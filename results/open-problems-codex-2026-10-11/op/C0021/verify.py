"""Independent raw-state depth-two DP and structural audit of depth-three certificate."""
import json,pathlib,time
from functools import cache
from fractions import Fraction
P=pathlib.Path(__file__).parent;start=time.monotonic()
def maj(a,b,c):return int(a+b+c>=2)
def f(bits):return maj(*(maj(*bits[i:i+3]) for i in (0,3,6)))
@cache
def raw(s):
 lo=tuple(0 if x==2 else x for x in s);hi=tuple(1 if x==2 else x for x in s)
 if f(lo)==f(hi):return Fraction(0)
 return 1+min((raw(s[:i]+(0,)+s[i+1:])+raw(s[:i]+(1,)+s[i+1:]))/2 for i,x in enumerate(s) if x==2)
out={'raw_depth2':str(raw((2,)*9)),'raw_states':raw.cache_info().currsize}
assert raw((2,)*9)==Fraction(393,64)
data=json.loads((P/'depth3_certificate.json').read_text());rows={r['id']:r for r in data['rows']}
@cache
def expr(t):
 if t<2:return t
 if t==2:return 'u'
 return tuple(expr(c) for c in rows[t]['children'])
def simplify(e):
 if not isinstance(e,tuple):return e
 cs=[simplify(c) for c in e]
 if cs.count(0)>=2:return 0
 if cs.count(1)>=2:return 1
 if 0 in cs and 1 in cs:return next(c for c in cs if c!=0 and c!=1)
 return tuple(sorted(cs,key=repr))
def paths(e,p=()):
 if e=='u':yield p
 elif isinstance(e,tuple):
  for i,c in enumerate(e):yield from paths(c,p+(i,))
def setleaf(e,path,v):
 if not path:return v
 cs=list(e);cs[path[0]]=setleaf(cs[path[0]],path[1:],v);return tuple(cs)
canon={t:simplify(expr(t)) for t in rows}; errors=[];edges=0
for t,r in rows.items():
 e=expr(t);ps=list(paths(e))
 if len(ps)!=r['size']:errors.append(('size',t))
 expected={(simplify(setleaf(e,p,0)),simplify(setleaf(e,p,1))) for p in ps}
 supplied={(canon[a],canon[b]) for a,b in r['moves']}
 if expected!=supplied:errors.append(('moves',t))
 edges+=len(supplied)
 if t<2:
  if r['weight']!=0:errors.append(('constant',t))
 else:
  m=r['size'];scores=[]
  for a,b in r['moves']:
   assert rows[a]['size']<m and rows[b]['size']<m
   scores.append((1<<m)+(rows[a]['weight']<<(m-1-rows[a]['size']))+(rows[b]['weight']<<(m-1-rows[b]['size'])))
  if r['weight']!=min(scores):errors.append(('Bellman',t))
root=rows[data['root']];out.update(depth3=str(Fraction(root['weight'],1<<root['size'])),certificate_states=len(rows),transition_pairs=edges,errors=errors,seconds=time.monotonic()-start)
assert not errors
assert Fraction(root['weight'],1<<root['size'])==Fraction(15796051,1048576)
(P/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))

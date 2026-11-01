"""Find an optimal-policy reachable residual where every median query has positive regret."""
import pathlib,json,time
from functools import cache
from fractions import Fraction
from collections import deque
P=pathlib.Path(__file__).parent;start=time.monotonic();d=json.loads((P/'depth3_certificate.json').read_text());rs={r['id']:r for r in d['rows']}
@cache
def expr(t):
 if t<2:return t
 if t==2:return 'u'
 return tuple(sorted((expr(c) for c in rs[t]['children']),key=repr))
def norm(e):
 if not isinstance(e,tuple):return e
 cs=[norm(c) for c in e]
 if cs.count(0)>=2:return 0
 if cs.count(1)>=2:return 1
 if 0 in cs and 1 in cs:return next(c for c in cs if c!=0 and c!=1)
 return tuple(sorted(cs,key=repr))
@cache
def q(e):
 if e=='u':return Fraction(1,2)
 if isinstance(e,int):return Fraction(e)
 a,b,c=map(q,e);return a*b+a*c+b*c-2*a*b*c
def paths(e,p=(),median=False):
 if e=='u':yield p
 elif isinstance(e,tuple):
  qs=list(map(q,e));md=sorted(qs)[1]
  for i,c in enumerate(e):
   if not median or qs[i]==md:yield from paths(c,p+(i,),median)
def subst(e,p,b):
 if not p:return b
 cs=list(e);cs[p[0]]=subst(cs[p[0]],p[1:],b);return tuple(cs)
lookup={expr(s):s for s in rs}
def outcomes(e,p):return lookup[norm(subst(e,p,0))],lookup[norm(subst(e,p,1))]
def score(s,a,b):
 m=rs[s]['size'];return (1<<m)+(rs[a]['weight']<<(m-1-rs[a]['size']))+(rs[b]['weight']<<(m-1-rs[b]['size']))
queue=deque([(d['root'],0)]);seen=set();parent={d['root']:None};out=None
while queue:
 s,clock=queue.popleft()
 if s in seen or s<2:continue
 seen.add(s);e=expr(s)
 medpairs={outcomes(e,p) for p in paths(e,median=True)}
 assert medpairs and medpairs<=set(tuple(x) for x in rs[s]['moves'])
 medscore=min(score(s,a,b) for a,b in medpairs)
 best=rs[s]['weight'];opts=[tuple(ab) for ab in rs[s]['moves'] if score(s,*ab)==best]
 if medscore>best:
  chosen=opts[0];path=next(p for p in paths(e) if outcomes(e,p)==chosen)
  ancestry=[];node=e
  for i in path:
   qs=list(map(q,node));ancestry.append(dict(probabilities=list(map(str,qs)),chosen_index=i,chosen_probability=str(qs[i]),median=str(sorted(qs)[1]),is_median=qs[i]==sorted(qs)[1]));node=node[i]
  trace=[];u=s
  while parent[u] is not None:
   prev,a,b,bit=parent[u];trace.append(dict(from_state=prev,outcomes=[a,b],observed=bit,to_state=u));u=prev
  trace.reverse();den=1<<rs[s]['size']
  for edge in trace:
   prev=edge['from_state'];pair=tuple(edge['outcomes']);pe=expr(prev)
   assert pair in {outcomes(pe,p) for p in paths(pe,median=True)}
   assert score(prev,*pair)==rs[prev]['weight']
   assert edge['to_state']==pair[edge['observed']]
  out=dict(state_id=s,clock=clock,state=repr(e),remaining_leaves=rs[s]['size'],value=str(Fraction(best,den)),best_median_query_cost=str(Fraction(medscore,den)),positive_median_regret=str(Fraction(medscore-best,den)),chosen_optimal_path=path,ancestry=ancestry,optimal_trace=trace,states_inspected=len(seen),seconds=time.monotonic()-start)
  out['prefix_median_eligible']=True
  assert any(not r['is_median'] for r in ancestry)
  break
 # Until the first positive-regret state, keep the prefix itself median-eligible.
 for a,b in opts:
  if (a,b) not in medpairs:continue
  for bit,t in enumerate((a,b)):
   if t not in parent:parent[t]=(s,a,b,bit)
   queue.append((t,clock+1))
assert out is not None
(P/'median_witness.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))

from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,itertools,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parents[1]/'runs'/'20261014T094139Z-account05-A091-composition-referee'/'code'))
import check as a
import exact as e
ORIGINAL_FACTORS=e.factors
def bounded_factors(n):
 if n.bit_length()>32:raise RuntimeError('factor input exceeds frozen32-bit direct-spectrum guard')
 return ORIGINAL_FACTORS(n)
e.factors=bounded_factors
START=time.perf_counter(); MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
COUNTS={'states':0,'edges':0,'last_tag_edges':0,'generic_wrappers':0,'scalar_cases':0,'full_tree_leaves':0}
def watchdog():
 if time.perf_counter()-START>(55 if MODE=='pilot' else 900):
  (ROOT/'out'/'incomplete.json').write_text(json.dumps({'status':'INCOMPLETE_TIMEOUT','counts':COUNTS,'assertions':e.COUNT}),encoding='utf-8')
  raise RuntimeError('frozen runtime watchdog')
def H(t):return e.entropy(a.squares(t))
def mean(t):return Q(sum(t),len(t))
def restrict(t,state):
 return tuple(t[sum((state[j] if state[j]>=0 else ((x>>[i for i,v in enumerate(state) if v<0].index(j))&1))<<j for j in range(len(state)))] for x in range(1<<state.count(-1)))
def wrapper(k,c,g):return tuple(k[z]+c[z]*g[y] for y in range(len(g)) for z in range(len(k)))
def profile(k,c,g):
 t=mean(c);mu=mean(g)
 form=e.add((1,e.entropy(tuple((v+mu*w)**2 for v,w in zip(a.coeff(k),a.coeff(c))))),(-t,a.eta(mu*mu)),(1-mu*mu,e.entropy(a.squares(c))))
 return form,t
BENT=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
CMASK=tuple(int(x==15) for x in range(16));KMASK=tuple(b-c for b,c in zip(BENT,CMASK));B0=Q(7)
def maincore(mask,pilot=False):
 core=e.tab(mask,2)
 @lru_cache(None)
 def frame(s):
  k=restrict(KMASK,s[:4]);c=restrict(CMASK,s[:4]);g=restrict(core,s[4:6]);tag=s[6]
  h=tuple(v*w for w in ((1,-1) if tag<0 else ((-1)**tag,)) for v in g)
  f=wrapper(k,c,h);hf=H(f);hg=H(h);E,t=profile(k,c,h)
  return f,hf,hg,E,t,h
 states=list(itertools.product((-1,0,1),repeat=7))
 if pilot:states=states[:32]
 for s in states:
  watchdog();f,hf,hg,E,t,h=frame(s);COUNTS['states']+=1
  e.check(e.add((1,hf),(-t,hg)),E)
  e.nonnegative(E)
  e.nonnegative(e.add((1,a.const(s[:4].count(-1))),(1,e.entropy((t,1-t))),(-1,E)))
  mu=mean(h);marg=[Q(0)]*len(h)
  for freq,p in enumerate(a.squares(f)):marg[freq//(len(f)//len(h))]+=p
  expected=[t*p for p in a.squares(h)];expected[0]+=1-t;e.check(tuple(marg),tuple(expected))
  for i,v in enumerate(s):
   if v>=0:continue
   children=[frame(s[:i]+(b,)+s[i+1:]) for b in (0,1)]
   D=e.add((1,hf),*[(-Q(1,2),v[1]) for v in children]);e.nonnegative(D);e.nonnegative(e.add((1,a.const(2)),(-1,D)))
   if 4<=i<6:
    fee=e.add((t,hg),*[(-t/2,v[2]) for v in children])
    e.nonnegative(fee);e.nonnegative(e.add((1,a.const(2*t)),(-1,fee)))
   else:fee={}
   e.check(D,e.add((1,fee),(1,E),*[(-Q(1,2),v[3]) for v in children]))
   # Explicit original-resource innovations, not a descendant influence replacement.
   L=a.const(Q(10));B=e.add((1,L),(1,E))
   childB=[e.add((1,L),(-1,fee),(1,v[3])) for v in children]
   e.check(e.add((1,B),*[(-Q(1,2),v) for v in childB]),D)
   if i==6:
    q=mean(h[::1])**2 # current h balanced before final tag; use restricted G instead
    g=restrict(core,s[4:6]);q=mean(g)**2
    T=e.add((q,a.eta(t)),(t,a.eta(q)),(1,a.const(Q(9,2)*t*q)))
    e.nonnegative(e.add((1,T),(-1,D)));COUNTS['last_tag_edges']+=1
   COUNTS['edges']+=1
 frame.cache_clear();a.coeff.cache_clear();e.entropy.cache_clear();a.iv2.cache_clear()
def generic():
 for state in itertools.product((-1,0,1),repeat=4):
  # state0 means mask; +/-1 are arbitrary signs off it.
  c=tuple(int(v==0) for v in state);k=tuple(v for v in state)
  for mask in range(16):
   g=e.tab(mask,2);f=wrapper(k,c,g);E,t=profile(k,c,g)
   e.check(e.add((1,H(f)),(-t,H(g))),E);e.nonnegative(E)
   e.nonnegative(e.add((1,a.const(2)),(1,e.entropy((t,1-t))),(-1,E)))
   COUNTS['generic_wrappers']+=1
  watchdog()
def scalar():
 for m in range(4,257,4):
  c=Q(1,1<<m);b=2*m-4*m*c
  e.check(2*c*(m*(1<<m)-2*m+1)-b,2*c)
  e.check(b-2*c-m-(m+Q(3,2))*c>=Q(m,4),True) # h2(c)<=c*(m+3/2), proved analytically
  e.check(Q(3*m,4)-Q(15,32)-Q(m,2)>=Q(m,8),True)
  if m>=16:e.check(b-2*c-m-11>=Q(m,4),True)
  n=Q(7)
  for j in range(2,130):
   # Finite tail identity 2+sum_{n=2}^j 2^(1-n)(n+4)=9-(j+6)*2^(1-j).
   n-=Q(j+4,1<<(j-1));e.check(n,Q(j+6,1<<(j-1)))
  COUNTS['scalar_cases']+=1;watchdog()
def tree():
 # Two-tag AND2; old query first, next core query AFTER last tag on selected surviving branch.
 base=(1,1,1,-1);core=tuple(base[x&3]*base[x>>2] for x in range(16));h=tuple(v*w for w in (1,-1,-1,1) for v in core);f=wrapper(KMASK,CMASK,h)
 ie=sum(Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(4));e.check(4*ie,B0)
 oldchildren=[a.cut(f,4,b) for b in (0,1)];old=e.add((1,H(f)),*[(-Q(1,2),H(v)) for v in oldchildren]);e.check(old,a.const(Q(1,8)))
 Estart,t=profile(KMASK,CMASK,h);L=e.add((1,a.const(B0)),(-1,old),(-1,Estart));e.nonnegative(e.add((1,L),(-1,a.const(Q(1,2)))))
 leaves=[]
 def descend(k,c,g,tagbits,sign,L,prob,phase):
  watchdog()
  h=tuple(sign*v*((-1)**x.bit_count()) for x in range(1<<tagbits) for v in g)
  F=wrapper(k,c,h);E,t=profile(k,c,h);B=e.add((1,L),(1,E))
  e.nonnegative(e.add((1,L),(-1,a.const(Q(1,2)))))
  # Fixed actual policy: all tags, all ext, then one further core query (fee up to2).
  if tagbits:
   for z in (0,1):descend(k,c,g,tagbits-1,sign*((-1)**z),L,prob/2,phase)
  elif len(k)>1:
   for z in (0,1):descend(a.cut(k,0,z),a.cut(c,0,z),g,0,sign,L,prob/2,phase)
  elif len(g)>1 and phase==0:
   fee=e.add((t,H(g)),*[(-t/2,H(a.cut(g,1,z))) for z in (0,1)])
   LL=e.add((1,L),(-1,fee))
   for z in (0,1):descend(k,c,a.cut(g,1,z),0,sign,LL,prob/2,1)
  else:
   leaves.append((prob,e.add((1,H(F)),(-1,B))));COUNTS['full_tree_leaves']+=1
 for z in (0,1):descend(KMASK,CMASK,a.cut(core,0,z),2,1,L,Q(1,2),0)
 e.check(H(f),e.add((1,a.const(B0)),*leaves));e.check(sum(p for p,v in leaves),Q(1))
if MODE=='pilot':maincore(7,True)
else:
 for mask in range(16):
  maincore(mask)
  (ROOT/'out'/'checkpoint.json').write_text(json.dumps({'status':'RUNNING','last_complete_core_mask':mask,'assertions':e.COUNT,'counts':COUNTS,'runtime_seconds':time.perf_counter()-START}),encoding='utf-8')
 generic();scalar();tree()
out={'status':'PASS','mode':MODE,'assertions':e.COUNT,'counts':COUNTS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'exact Fraction prime-log identities and certified rational intervals; no floating signs','scope':'finite validation only; all-policy scope by PROOF.md local induction'}
(ROOT/'out'/('pilot.json' if MODE=='pilot' else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

"""Independent residual-formula Bellman DP and rollout policy; exact dyadic costs.
Interned IDs 0,1=constants, 2=one unknown bit. Every occurrence has disjoint bits.
The ID of a formula is a *type*, not a shared variable.
"""
import time,json,math,sys,pathlib,ctypes
from fractions import Fraction
from functools import cache
P=pathlib.Path(__file__).parent
nodes=[None,None,None]; sizes=[0,0,1]; probs=[0.,1.,.5]; heights=[0,0,0]; intern={}
start=time.monotonic(); limit=240
class Memory(ctypes.Structure):
 _fields_=[('cb',ctypes.c_ulong),('PageFaultCount',ctypes.c_ulong)]+[(n,ctypes.c_size_t) for n in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage']]
def memory():
 info=Memory();info.cb=ctypes.sizeof(info)
 ctypes.windll.psapi.GetProcessMemoryInfo(ctypes.c_void_p(-1),ctypes.byref(info),info.cb)
 return info.WorkingSetSize
def guard():
 if len(nodes)>400000 or time.monotonic()-start>limit: raise RuntimeError('bounded-job cap reached')
 if len(nodes)%1024==0 and memory()>850000000:raise RuntimeError('memory cap reached')
def norm(cs):
 cs=tuple(sorted(cs))
 if cs[1]==0: return 0
 if cs.count(1)>=2: return 1
 if 0 in cs and 1 in cs: return next(c for c in cs if c>1)
 if cs in intern: return intern[cs]
 guard(); i=len(nodes); intern[cs]=i; nodes.append(cs)
 sizes.append(sum(sizes[c] for c in cs)); heights.append(1+max(heights[c] for c in cs))
 a,b,c=(probs[x] for x in cs); probs.append(a*b+a*c+b*c-2*a*b*c)
 return i
def full(k): return 2 if k==0 else norm((full(k-1),)*3)
@cache
def moves(t):
 if t<2:return ()
 if t==2:return ((0,1),)
 out=set(); cs=nodes[t]
 for i,c in enumerate(cs):
  if i and c==cs[i-1]:continue
  for a,b in moves(c):out.add((norm(cs[:i]+(a,)+cs[i+1:]),norm(cs[:i]+(b,)+cs[i+1:])))
 return tuple(sorted(out))
def step(t,a,b,vals):
 m=sizes[t]
 return (1<<m)+(vals(a)<<(m-1-sizes[a]))+(vals(b)<<(m-1-sizes[b]))
@cache
def W(t):
 if t<2:return 0
 guard(); return min(step(t,a,b,W) for a,b in moves(t))
def value(t):return W(t)/(1<<sizes[t])
@cache
def optimal_moves(t):
 return tuple((a,b) for a,b in moves(t) if step(t,a,b,W)==W(t))
@cache
def lottery(cs):
 # Price = optimal standalone uniform conditional expected cost.
 @cache
 def go(s):
  if s.count(0)>=2 or s.count(1)>=2:return 0.
  return min(value(cs[i])+probs[cs[i]]*go(s[:i]+(1,)+s[i+1:])+(1-probs[cs[i]])*go(s[:i]+(0,)+s[i+1:]) for i,v in enumerate(s) if v==2)
 s=tuple(c if c<2 else 2 for c in cs)
 return go(s)
@cache
def R(t):
 if t<2:return 0.
 if heights[t]<=3:return value(t)
 return lottery(nodes[t])
@cache
def candidates(t,mode):
 if mode=='all':return moves(t)
 cs=nodes[t];out=set()
 for i,c in enumerate(cs):
  if i and c==cs[i-1]:continue
  for a,b in optimal_moves(c):out.add((norm(cs[:i]+(a,)+cs[i+1:]),norm(cs[:i]+(b,)+cs[i+1:])))
 return tuple(sorted(out))
@cache
def look(t,mode,depth):
 if depth==0 or t<2:return R(t)
 return min(1+(look(a,mode,depth-1)+look(b,mode,depth-1))/2 for a,b in candidates(t,mode))
@cache
def policy(t,mode,depth):
 if heights[t]<=3:return optimal_moves(t)[0]
 return min(candidates(t,mode),key=lambda ab:(1+(look(ab[0],mode,depth-1)+look(ab[1],mode,depth-1))/2,ab))
@cache
def E(t,mode,depth):
 if t<2:return 0
 if heights[t]<=3:return W(t)
 guard();a,b=policy(t,mode,depth);return step(t,a,b,lambda x:E(x,mode,depth))
def verify():
 # Check every generated optimal-state Bellman equality, exact integers.
 errs=0
 for t in range(len(nodes)):
  if heights[t]<=3:
   w=W(t)
   if t>=2 and w!=min(step(t,a,b,W) for a,b in moves(t)):errs+=1
 return errs
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'optimal';depth=int(sys.argv[2]) if len(sys.argv)>2 else 1
 rows=[]
 try:
  maxk=int(sys.argv[3]) if len(sys.argv)>3 else 4
  for k in range(1,maxk+1):
   t=full(k); w=W(t) if k<=3 else E(t,mode,depth);d=Fraction(w,1<<sizes[t])
   row=dict(k=k,cost=str(d),decimal=float(d),sigma_bound=1-math.log(float(d))/k/math.log(3),nodes=len(nodes),seconds=time.monotonic()-start,mode=mode,lookahead=depth)
   row['working_set_bytes']=memory()
   rows.append(row);print(row,flush=True);(P/f'compute_{mode}_{depth}.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
   if k==3:
    reachable=set()
    def visit(s):
     if s in reachable:return
     reachable.add(s)
     for a,b in moves(s):visit(a);visit(b)
    visit(t)
    cert=[dict(id=s,children=nodes[s],size=sizes[s],weight=W(s),moves=moves(s)) for s in sorted(reachable)]
    (P/'depth3_certificate.json').write_text(json.dumps(dict(root=t,rows=cert)),encoding='utf8')
  print('Bellman errors',verify(),flush=True)
 except RuntimeError as e: print(str(e), 'nodes',len(nodes),'seconds',time.monotonic()-start,flush=True)

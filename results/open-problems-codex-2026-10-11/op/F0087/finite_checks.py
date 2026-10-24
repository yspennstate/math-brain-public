import cmath,collections,json,pathlib,time
import numpy as np
P=pathlib.Path(__file__).parent

def matchings(W,H):
 N=W*H
 def rec(mask,edges):
  if mask==(1<<N)-1:yield frozenset(edges);return
  v=next(i for i in range(N) if not(mask>>i)&1);x,y=v%W,v//W
  for u in ([v+1] if x+1<W else [])+([v+W] if y+1<H else []):
   if not(mask>>u)&1:yield from rec(mask|(1<<v)|(1<<u),edges+[(v,u)])
 yield from rec(0,[])

def edge_data(a,b,W,H):
 x,y=a;xx,yy=b
 if xx<x or yy<y:
  s,e=edge_data(b,a,W,H);return -s,e
 if xx==x+1:
  s=1 if (x+y)%2==0 else -1
  e=tuple(sorted(((y-1)*W+x,y*W+x))) if 0<y<H else None
 else:
  s=1 if (x-1+y)%2==0 else -1
  e=tuple(sorted((y*W+x-1,y*W+x))) if 0<x<W else None
 return s,e

def heights(M,W,H):
 h={(0,0):0};q=collections.deque([(0,0)])
 while q:
  a=q.popleft();x,y=a
  for b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
   if 0<=b[0]<=W and 0<=b[1]<=H:
    s,e=edge_data(a,b,W,H);v=h[a]+s*(1-4*int(e in M))
    if b in h:assert h[b]==v,'height not closed'
    else:h[b]=v;q.append(b)
 return h

def matrix(W,H):
 black=[v for v in range(W*H) if (v%W+v//W)%2==0];white=[v for v in range(W*H) if v not in black]
 bi={v:i for i,v in enumerate(black)};wi={v:i for i,v in enumerate(white)}
 K=np.zeros((len(black),len(white)),complex)
 for b in black:
  x,y=b%W,b//W
  for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
   if 0<=xx<W and 0<=yy<H:K[bi[b],wi[yy*W+xx]]=1 if yy==y else 1j
 return K,bi,wi
out=[];start=time.time()
for W,H in [(2,2),(2,4),(4,4),(4,6),(6,6)]:
 Ms=list(matchings(W,H));hs=[heights(M,W,H) for M in Ms];ref=hs[0]
 assert all(all((h[v]-ref[v])%4==0 for v in h) for h in hs)
 K,bi,wi=matrix(W,H);base=np.linalg.det(K);assert abs(abs(base)-len(Ms))<1e-8
 # Two different dual paths with the same endpoints, both with interior crossed edges.
 a=(1,1);b=(W-1,H-1)
 paths=[[(x,1) for x in range(1,W)]+[(W-1,y) for y in range(2,H)],[(1,y) for y in range(1,H)]+[(x,H-1) for x in range(2,W)]]
 errors=[];period_errors=[]
 for alpha in [0,.37,np.pi/3,np.pi,.9*np.pi,1.4*np.pi,2*np.pi]:
  exact=sum(cmath.exp(1j*alpha*(h[b]-h[a])/4) for h in hs)/len(hs)
  for path in paths:
   D=0;T=K.copy()
   for v,z in zip(path,path[1:]):
    s,e=edge_data(v,z,W,H);D+=s/4
    if e is not None:
     u,w=e
     if u not in bi:u,w=w,u
     T[bi[u],wi[w]]*=cmath.exp(-1j*alpha*s)
   det=cmath.exp(1j*alpha*D)*np.linalg.det(T)/base
   errors.append(abs(exact-det))
  shift=sum(cmath.exp(1j*(alpha+2*np.pi)*(h[b]-h[a])/4) for h in hs)/len(hs)
  period_errors.append(abs(shift-cmath.exp(2j*np.pi*(ref[b]-ref[a])/4)*exact))
 row={'rectangle':[W,H],'tilings':len(Ms),'all_heights_closed':True,'all_height_differences_divisible_by_4':True,'max_twisted_determinant_error':max(errors),'max_charge_alias_error':max(period_errors),'endpoint_pi_checked_finite_only':True}
 out.append(row);print(json.dumps(row),flush=True)
(P/'finite_checks.json').write_text(json.dumps({'elapsed_seconds':time.time()-start,'results':out},indent=2),encoding='utf8')

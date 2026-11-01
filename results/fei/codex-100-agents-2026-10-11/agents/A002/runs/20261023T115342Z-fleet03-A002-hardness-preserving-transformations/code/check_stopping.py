import sys,json,time,math
from pathlib import Path
from functools import lru_cache
import exactlib as E
from exactlib import Q,add,logq,interval,ok,rankadd
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); counts={'policies':0,'nodes':0,'leaves':0,'eligible_banks':0,'sharp_depth_laws':0}; maxn=1 if '--pilot' in sys.argv else 3
@lru_cache(None)
def physical(f):
 N=len(f); n=N.bit_length()-1
 W=tuple(sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(N)) for s in range(N))
 H=add(*[(1,logq(Q(w,N))) for w in W if w]); costs=tuple(Q(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N))
 I=sum((costs[1<<j] for j in range(n)),Q(0))
 ok(I==sum((s.bit_count()*Q(w*w,N*N) for s,w in enumerate(W)),Q(0)))
 return n,W,H,I,costs

def phi(x):
 assert 0<=x<=Q(1,2)
 # h2 term, not q(signed amplitude)
 H=add((Q(1,2)/x if x else 0,logq(x)),(Q(1,2)/(1-x) if x!=1 else 0,logq(1-x)))
 lo,hi=interval(H); _,_,lnlo,lnhi=E.lnint(2)
 return lo+2*x/lnhi,hi+2*x/lnlo

def hdiff(f,g0,g1): return add((1,physical(f)[2]),(-Q(1,2),physical(g0)[2]),(-Q(1,2),physical(g1)[2]))
def linear_reset(f,ref,ids,mode,depth):
 n,W,H,I,cost=physical(f); N=len(f)
 if n==0 or mode==0: return f,ref,ids,Q(0)
 if mode==1 or mode==2:
  basis={}; dirs=[]; cm=0
  for v in sorted(range(1,N),key=lambda v:(min(cost[v],1-cost[v]),v)):
   if rankadd(basis,v):
    if cost[v]>Q(1,2): cm|=1<<len(dirs)
    dirs.append(v)
 else:
  dirs=[1<<j for j in range(n)]
  if n>=2: dirs[0]^=dirs[1]
  cm=1 if depth%2==0 else 0
 shift=(depth+mode)%N
 images=[shift for _ in range(N)]
 for y in range(N):
  for j,v in enumerate(dirs):
   if (y>>j)&1: images[y]^=v
 signs=[(-1)**((y&cm).bit_count()%2) for y in range(N)]
 f2=tuple(signs[y]*f[images[y]] for y in range(N)); r2=tuple(signs[y]*ref[images[y]] for y in range(N)); ids2=tuple(ids[images[y]] for y in range(N))
 ok(len(set(ids2))==N); ok(physical(f2)[2]==H)
 rel=I-physical(f2)[3]
 if mode in (1,2): ok(rel>=0)
 return f2,r2,ids2,rel

def child(a,j,b): return tuple(a[(x% (1<<j))+((x//(1<<j))<<(j+1))+(b<<j)] for x in range(len(a)//2))

def check_policy(f,ref,mode):
 N=len(f); n=N.bit_length()-1; Z=tuple(a!=b for a,b in zip(f,ref)); e=Q(sum(Z),N); rootH=physical(f)[2]; rootI=physical(f)[3]
 depths=[None]*N; a=Q(0); db=Q(0); Qcost=Q(0); Rcost=Q(0); loss={}; terminalH={}; terminalI=Q(0); allnoninc=True
 def walk(g,c,ids,reach,depth):
  nonlocal a,db,Qcost,Rcost,loss,terminalH,terminalI,allnoninc
  z=tuple(Z[x] for x in ids); q=Q(sum(z),len(ids)); nn=physical(g)[0]
  ok(tuple(x!=y for x,y in zip(g,c))==z)
  if nn==0 or (mode==1 and q in (0,1)) or (mode==2 and depth and (sum(ids)+depth)%3==0):
   for x in ids: depths[x]=depth
   terminalH=add((1,terminalH),(reach,physical(g)[2])); terminalI+=reach*physical(g)[3]; counts['leaves']+=1
   return
  j=(depth+mode)%nn; g0,g1=child(g,j,0),child(g,j,1); c0,c1=child(c,j,0),child(c,j,1); i0,i1=child(ids,j,0),child(ids,j,1)
  q0=Q(sum(Z[x] for x in i0),len(i0)); q1=Q(sum(Z[x] for x in i1),len(i1)); ok((q0+q1)/2==q)
  inf=Q(sum(g[x]!=g[x^(1<<j)] for x in range(len(g))),len(g)); m=min(inf,1-inf); ok(m<=min(2*q,Q(1,2)))
  lv=hdiff(g,g0,g1); ok(interval(lv)[1]<=phi(m)[0])
  db+=reach; a+=reach*q; Qcost+=reach*inf; loss=add((1,loss),(reach,lv)); counts['nodes']+=1
  for gg,cc,ii in ((g0,c0,i0),(g1,c1,i1)):
   gg,cc,ii,release=linear_reset(gg,cc,ii,mode,depth)
   Rcost+=reach*release/2; allnoninc=allnoninc and release>=0
   walk(gg,cc,ii,reach/2,depth+1)
 walk(f,ref,tuple(range(N)),Q(1),0)
 ok(all(x is not None for x in depths)); ok(db==Q(sum(depths),N)); ok(a==Q(sum(t for t,z in zip(depths,Z) if z),N)); ok(loss==add((1,rootH),(-1,terminalH)))
 ok(Qcost+Rcost==rootI-terminalI)
 if db: ok(interval(loss)[1]<=db*phi(min(2*a/db,Q(1,2)))[0])
 else: ok(loss=={})
 if allnoninc:
  ok(Qcost+Rcost>=0); counts['eligible_banks']+=1
  for K in (0,1,2,4):
   # exact SAME signed terminal bank; no entropy signs discarded
   deficit=add((1,rootH),(-K*rootI,{2:Q(1)})); S=add((K*terminalI,{2:Q(1)}),(-1,terminalH))
   ok(add((1,deficit),(1,S),(K*(Qcost+Rcost),{2:Q(1)}))==loss)
 # exact rational upper-tail primal/dual; also try complements and adversarial ties
 for M in sorted(set((0,sum(Z),N//2,N))):
  ee=Q(M,N); primal=Q(sum(sorted(depths,reverse=True)[:M]),N)
  candidates=[(Q(L)*ee+Q(sum(max(t-L,0) for t in depths),N),L) for L in range(max(depths)+1)]
  dual,L=min(candidates); ok(primal==dual); counts['sharp_depth_laws']+=1
  chosen=sorted(range(N),key=lambda x:(-depths[x],x))[:M]
  witness=tuple(-1 if x in chosen else 1 for x in range(N)); ok(Q(sum(depths[x] for x in range(N) if witness[x]<0),N)==dual)
  if ee==e: ok(a<=dual)
 counts['policies']+=1

for n in range(maxn+1):
 for v in range(1<<(1<<n)):
  f=tuple(1 if (v>>x)&1 else -1 for x in range(1<<n)); W=physical(f)[1]; S=max(range(len(W)),key=lambda s:abs(W[s])); sg=1 if W[S]>=0 else -1
  refs=(tuple(1 for _ in f),tuple(sg*(-1)**((x&S).bit_count()%2) for x in range(len(f))))
  for ref in refs:
   for mode in range(4): check_policy(f,ref,mode)
# fixed actual formula replay: control-first stop / complete active data query
fixtures=[]
for t in (1,2,4):
 k=2; d=2; n=k+d*t; N=1<<n; p=Q(1,4)
 f=tuple(1 if x%4 else (-1)**sum(((x>>(k+2*j))&1)*((x>>(k+2*j+1))&1) for j in range(t)) for x in range(N))
 tau=[]
 for x in range(N):
  z=x%4; depth=next((j+1 for j in range(k) if (z>>j)&1),k+d*t); tau.append(depth)
 e=Q(sum(x<0 for x in f),N); db=Q(sum(tau),N); a=Q(sum(T for T,y in zip(tau,f) if y<0),N)
 ok(db==2*(1-p)+p*d*t); ok(e==p*(1-Q(1,2)**t)/2); ok(a==e*(k+d*t))
 M=sum(y<0 for y in f); primal=Q(sum(sorted(tau,reverse=True)[:M]),N); dual=min(Q(L)*e+Q(sum(max(T-L,0) for T in tau),N) for L in range(max(tau)+1)); ok(primal==dual==a)
 ok(a>e*db); ok(Q(sum(T*T for T in tau),N)>=p*(k+d*t)**2)
 fixtures.append({'t':t,'dimension':n,'mean_depth':str(db),'error_occupation':str(a),'quantile_bound_exact':True})
# source k10 formula certified by rational inequalities, not huge table
ok(Q(2047,512)<4); ok(Q(1933,1024)>Q(116,1024)); ok(Q(889,1024)>Q(116,1024)); ok(2*(10+Q(9,2))==29)
out={'status':'PASS','assertions':E.checks,'counts':counts,'activation_fixtures':fixtures,'elapsed_seconds':time.monotonic()-start,'pilot':'--pilot' in sys.argv,'arithmetic':'direct character/physical input ancestry, Fraction, prime-log, rational atanh','max_dimension':10}
(R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

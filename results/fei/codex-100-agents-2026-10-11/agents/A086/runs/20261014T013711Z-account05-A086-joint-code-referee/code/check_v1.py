import arithmetic as ar
from arithmetic import F,fw,spec,add,scale,log,H,CE,KL,interval,L2,ck
from pathlib import Path
from itertools import product
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
def table(w,n): return [1 if w>>x&1 else -1 for x in range(1<<n)]
def refs(n,j):
 p=F(1+(j%2),3)
 return {T:p**T.bit_count()*(1-p)**(n-T.bit_count()) for T in range(1<<n)}
def cal(R,P,t):
 C=range(1<<t); v=1-sum(P.get(T,0) for T in C); z=sum(R[T] for T in R if T>=1<<t)
 out={T:P.get(T,F(0)) for T in C}
 if v:
  for T in R:
   if T>=1<<t: out[T]=v*R[T]/z
 return {T:m for T,m in out.items() if m}
def embed(T,t): return (T&((1<<t)-1))|((T>>t)<<(t+1))
def physical(t):
 return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range((len(t)-1).bit_length())]
def packet(A,B): return add(H({0:A,1:B}),scale(log(A+B),A+B)) if A+B else {}
def selector(t,G,Ht):
 mask=(1<<t)-1; n=t+3
 truth=[G[((x>>1)&mask)|(((x>>(t+1))&1)<<t)] if not x&1 else Ht[((x>>1)&mask)|(((x>>(t+2))&1)<<t)] for x in range(1<<n)]
 a,b=fw(G),fw(Ht); b={embed(T,t):m for T,m in b.items()}; P=spec(truth); q={}; expected={}; B={}; delta=F(0); bout=F(0)
 for T in set(a)|set(b):
  u,v=a.get(T,0),b.get(T,0); m=(u*u+v*v)/2; q[T]=m
  A,E=(u+v)**2/4,(u-v)**2/4
  if A: expected[T<<1]=A
  if E: expected[(T<<1)|1]=E
  B=add(B,packet(A,E))
  if T<1<<t: delta+=E
  else: bout+=m
 ck(P==expected); edge=physical(truth); d=edge[0]; fold=min(d,1-d)
 ck(sum(edge)==(sum(physical(G))+sum(physical(Ht)))/2+d)
 ck(d==sum(v for s,v in P.items() if s&1))
 if d>F(1,2):
  af=a; bf={T:-v for T,v in b.items()}
 else: af,bf=a,b
 delta=sum((af.get(T,0)-bf.get(T,0))**2/4 for T in range(1<<t))
 ck(delta<=min(fold,(1<<t)*fold*fold)); ck(bout<=2*fold)
 BC=add(*(packet((af.get(T,0)+bf.get(T,0))**2/4,(af.get(T,0)-bf.get(T,0))**2/4) for T in range(1<<t)))
 ck(interval(add(H({0:delta,1:1-delta}),scale(BC,-1)))[0]>=0)
 PG,PH=spec(G),spec(Ht); Delta=add(H(P),scale(add(H(PG),H(PH)),F(-1,2)))
 JS=add(Delta,scale(B,-1)); ck(interval(JS)[0]>=0)
 ck(interval(JS)[1]<=2*fold)
 if t==1:
  ck(interval(add({2:4*d},scale(B,-1)))[0]>=0)
  ck(interval(Delta)[1]<=4*d*L2[0]+2*d)
  meansG=[F(sum(G[s+(x<<t)] for x in range(2)),2) for s in range(2)]
  meansH=[F(sum(Ht[s+(x<<t)] for x in range(2)),2) for s in range(2)]
  c=[1 if meansG[s]+meansH[s]>=0 else -1 for s in range(2)]
  gp=[G[x]*c[x&1] for x in range(4)]; hp=[Ht[x]*c[x&1] for x in range(4)]
  tt=[v*c[(x>>1)&1] for x,v in enumerate(truth)]; pt=spec(tt)
  shift=0 if c[0]==c[1] else 2
  ck(pt=={s^shift:v for s,v in P.items()})
  e=[(1-c[s]*meansG[s])/2 for s in range(2)]; f=[(1-c[s]*meansH[s])/2 for s in range(2)]
  s=sum(e+f)/2; ck(0<=s<=1)
  ck(d>=s*(1-s) if s<=F(1,2) else d>=s/2)
 else:
  ck(interval(Delta)[1]<=(t+2)*fold*L2[0]+3*fold)
 for j in range(2 if t==1 else 1):
  RG,RH=refs(t+1,j),refs(t+1,j+1); CG,CH=cal(RG,PG,t),cal(RH,PH,t)
  ck(sum(CG.values())==sum(CH.values())==1)
  ck(interval(add(CE(PG,RG),scale(CE(PG,CG),-1)))[0]>=0)
  # Exact categorical KL, not only its sign.
  catP={T:PG.get(T,F(0)) for T in range(1<<t)}; catR={T:RG[T] for T in range(1<<t)}
  catP['private']=1-sum(catP.values()); catR['private']=1-sum(catR.values())
  ck(add(CE(PG,RG),scale(CE(PG,CG),-1))==KL(catP,catR))
  rr={T:v/2 for T,v in CG.items()}
  for T,v in CH.items():
   T=embed(T,t); rr[T]=rr.get(T,0)+v/2
  Q={s:rr[s>>1]*v/q[s>>1] for s,v in P.items()}
  for T,v in rr.items():
   if T not in q: Q[T<<1]=v
  ck(sum(Q.values())==1)
  ck(KL(P,Q)==scale(add(KL(PG,CG),KL(PH,CH)),F(1,2)))
  ck(CE(P,Q)==add(scale(add(CE(PG,CG),CE(PH,CH)),F(1,2)),Delta))
  # Whole sector-label chain: collision atoms + two private ownership sectors.
  sectors={('C',s):v for s,v in Q.items() if (s>>1)<1<<t}
  vG=1-sum(CG.get(T,0) for T in range(1<<t)); vH=1-sum(CH.get(T,0) for T in range(1<<t))
  sectors['G']=vG/2; sectors['H']=vH/2; chain=H(sectors)
  for CP,RCP,vj in [(PG,CG,vG),(PH,CH,vH)]:
   if vj:
    pp={T:v/vj for T,v in CP.items() if T>=1<<t}; rp={T:v/vj for T,v in RCP.items() if T>=1<<t}
    chain=add(chain,scale(CE(pp,rp),vj/2),{2:vj/2})
  ck(chain==CE(P,Q))
 return d,Delta
def shared(mode):
 t=1 if mode=='one' else 2; count=0
 words=list(product(range(16),repeat=2)) if t==1 else [(i,(37*j)%256) for i in range(256) for j in range(16)]
 for i,j in words: selector(t,table(i,t+1),table(j,t+1)); count+=1
 return {'shared_width':t,'Boolean_pairs':count,'reference_pairs':count*(2 if t==1 else 1)}
def hc(rows): return add(*(scale(log(p),-p*c) for p,c in rows if p))
def bent(k):
 return [(-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2)) for x in range(1<<k)]
def boundary():
 cases=0; finite=0; tensors=0; cert=[]
 for k in range(4,33,2):
  N=1<<k; delta=F(1,N); e=F(1,1<<(k//2)); plus=(N+(1<<(k//2)))//2; minus=N-plus
  Ag,Ah=(e-delta)**2,(e+delta)**2; rows=[(Ag,plus),(Ah,minus),(delta*delta,N)]
  HM=hc(rows); Hh=hc([((e-2*delta)**2,plus),((e+2*delta)**2,minus)])
  Delta=add(HM,scale(add({2:F(k)},Hh),F(-1,2)))
  B=add(scale(packet(Ag,delta*delta),plus),scale(packet(Ah,delta*delta),minus))
  ck(sum(p*c for p,c in rows)==1)
  for t in [k,k+1]:
   ck(interval(add(B,scale(add({2:F(k)},scale(log(F(16,9)),-1)),-delta)))[0]>=0)
   ck(interval(Delta)[1]<=(t+2)*delta*L2[0]+3*delta); cases+=1
  IM=F(k,2)+(k+1)*delta
  ck(interval(add({2:2*(IM+1)},scale(HM,-1)))[0]>0) # A094's balanced tagged root
  slack=add({2:2*k*delta+F(k,2)},scale(Hh,F(-1,2)))
  excess=add(Delta,{2:-2*delta})
  ck(interval(add(slack,scale(excess,-1)))[0]>0)
  lo,hi=interval(add({2:2*IM},scale(HM,-1))); ck(lo>0)
  cert.append({'k':k,'d':str(delta),'root_2I_minus_H_nats_lower':str(lo),'calibration_saving':'0','posterior_mismatch':'0'})
  if k in [4,6]:
   g=bent(k); h=g.copy(); h[0]*=-1; root=[g[x>>1] if not x&1 else h[x>>1] for x in range(1<<(k+1))]; PM=spec(root)
   ck(H(PM)==HM); ck(H(spec(h))==Hh); ck(sum(physical(g))==F(k,2)); ck(sum(physical(h))==F(k,2)+2*k*delta); ck(sum(physical(root))==IM); finite+=1
   for w in range(16):
    tq=table(w,2); pq=spec(tq); Iq=sum(physical(tq))
    for j in range(2):
     rq=refs(2,j); prodP={(s,T):v*m for s,v in PM.items() for T,m in pq.items()}; prodQ={(s,T):v*m for s,v in PM.items() for T,m in rq.items()}
     ck(H(prodP)==add(HM,H(pq))); ck(CE(prodP,prodQ)==add(HM,CE(pq,rq))); ck(KL(prodP,prodQ)==KL(pq,rq)); tensors+=1
 (RUN/'out/RESERVE_CERTIFICATES.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf8')
 return {'compressed_boundary_cases':cases,'direct_bent_cases':finite,'arbitrary_terminal_reference_cases':tensors,'root_2I_margin':'positive in all frozen cases; analytic continuation k>=6 in reconstruction'}
mode=sys.argv[1]; start=time.monotonic(); result=boundary() if mode=='boundary' else shared(mode)
result.update(assertions=ar.N,seconds=time.monotonic()-start)
(RUN/f'out/{mode.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8'); print(json.dumps(result))

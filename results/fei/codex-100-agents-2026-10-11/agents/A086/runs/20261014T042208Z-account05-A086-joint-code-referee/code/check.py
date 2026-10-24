import arithmetic as ar
from arithmetic import F,fw,spec,add,scale,log,H,CE,KL,interval,L2,ck
from pathlib import Path
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1]; rawln=ar.ln
@lru_cache(None)
def gridln(q):
 a,b=rawln(q); D=1<<80
 return F(a.numerator*D//a.denominator,D),F(-((-b.numerator*D)//b.denominator),D)
ar.ln=gridln
def edges(t): return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range((len(t)-1).bit_length())]
def fullref(n,j,P):
 u={T:F(1,1<<n) for T in range(1<<n)}
 if j==0: return u
 if j==1: return {T:v/2 for T,v in u.items()}
 return {T:(P.get(T,0)+v)/2 for T,v in u.items()}
def lift(m,r,g,a):
 p=F(1,1<<r); t=F(1,1<<m); mask=(1<<r)-1
 truth=[g[x>>r]*(-1 if (x&mask)==0 and (x>>r)==a else 1) for x in range(1<<(m+r))]
 A=fw(g); actual=fw(truth); predicted={}
 for T in range(1<<m):
  b=g[a]*(-1)**(T&a).bit_count()
  for U in range(1<<r):
   c=(A.get(T,0) if not U else 0)-2*p*t*b
   if c: predicted[U|(T<<r)]=c
 ck(actual==predicted); P={s:v*v for s,v in actual.items()}; PG=spec(g)
 q={T:sum(v for s,v in P.items() if s>>r==T) for T in range(1<<m)}
 q={T:v for T,v in q.items() if v}; B=add(H(P),scale(H(q),-1)); I=sum(edges(truth)); I0=sum(edges(g)); j=sum(g[a]!=g[a^(1<<i)] for i in range(m)); C=2*p*t*(m-j); E=2*p*t*j; Isel=2*r*p*t
 ck(I==I0+C-E+Isel); ck(sum(edges(truth)[:r])==Isel)
 V=4*p*(1-p)*t
 bound=add(H({0:V,1:1-V}),scale(log((1<<r)-1),V))
 ck(interval(add(bound,scale(B,-1)))[0]>=0)
 ck(interval(B)[1]<=m*V*L2[0]+4*Isel*L2[0])
 return PG,P,q,B,I0,C,E,Isel
def mixture(PG,P,q,B,r,m,weights,components,R):
 references=[R]+components[1:]; rr={T:sum(weights[j]*references[j].get(T,0) for j in range(len(weights))) for T in range(1<<m)}
 Q={s:rr[s>>r]*v/q[s>>r] for s,v in P.items()}
 for T,v in rr.items():
  if T not in q and v: Q[T<<r]=v
 ck(sum(Q.values())==weights[0]*sum(R.values())+sum(weights[1:]))
 joint={(j,T):weights[j]*v for j,cp in enumerate(components) for T,v in cp.items() if weights[j]*v}
 ck(sum(joint.values())==1)
 ck({T:sum(v for (j,S),v in joint.items() if S==T) for T in q}==q)
 postH=add(H(joint),scale(H(q),-1)); kap={}
 for T,v in q.items():
  pp={j:weights[j]*components[j].get(T,0)/v for j in range(len(weights)) if weights[j]*components[j].get(T,0)}
  rp={j:weights[j]*references[j].get(T,0)/rr[T] for j in range(len(weights))}
  kap=add(kap,scale(KL(pp,rp),v))
 ck(interval(kap)[0]>=0)
 c=CE(PG,R); hg=H(PG); compCE=add(*(scale(CE(components[j],references[j]),weights[j]) for j in range(len(weights))))
 exact=add(compCE,H(dict(enumerate(weights))),scale(postH,-1),scale(kap,-1),B)
 ck(CE(P,Q)==exact)
 ck(KL(P,Q)==add(scale(add(c,scale(hg,-1)),weights[0]),scale(kap,-1)))
 return Q,c,kap
def parity():
 roots=refs=0
 for m in range(1,4):
  for k in range(1,m+1):
   A=(1<<k)-1; g=[(-1)**(x&A).bit_count() for x in range(1<<m)]
   for a in range(1<<m):
    for r in range(1,4):
     PG,P,q,B,I0,C,E,Is=lift(m,r,g,a); p=F(1,1<<r); t=F(1,1<<m); rho=4*p*t
     uniform={T:t for T in range(1<<m)}
     ck(q=={T:(1-rho)*PG.get(T,0)+rho*t for T in range(1<<m)})
     for j in range(3):
      R=fullref(m,j,PG); Q,c,kap=mixture(PG,P,q,B,r,m,[1-rho,rho],[PG,uniform],R)
      ck(interval(add(c,{2:6*(C+E+Is)},scale(CE(P,Q),-1)))[0]>=0)
      K=F(8); margin=add({2:K*(I0+C-E+Is)},scale(CE(P,Q),-1)); rhs=add({2:K*I0+(K-6)*C-(K+6)*E+(K-6)*Is},scale(c,-1))
      ck(interval(add(margin,scale(rhs,-1)))[0]>=0); refs+=1
     roots+=1
     if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 # No factorization of the huge near-unit probability is needed for this exact shock.
 shock=[]
 for L in [8,32,256]:
  epsilon=F(1,1<<(L+4)); RA=1-15*epsilon; ck(RA>F(1,2)); ck(RA+15*epsilon==1)
  off=F(15,128); lower=off*(L+4); shock.append({'L':L,'source_cost_bits_upper':'1','root_CE_bits_lower':str(lower),'I':'33/16','C':'1/8','E':'1/8'})
 ck(F(975,32)>8*F(33,16)); (RUN/'out/SHOCK_CERTIFICATES.json').write_text(json.dumps(shock,indent=2)+'\n',encoding='utf8')
 return {'Boolean_roots':roots,'reference_cases':refs,'shock_cases':3}
def unequal():
 m=6; g=[-1 if x&7==0 else 1 for x in range(64)]; roots=refs=0
 for a in range(0,64,8):
  for r in range(1,5):
   PG,P,q,B,I0,C,E,Is=lift(m,r,g,a); rho=F(4,1<<(r+m)); weights=[1-4*rho,3*rho,rho]; uniform={T:F(1,64) for T in range(64)}; components=[PG,{0:F(1)},uniform]
   ck(sum(weights)==1); ck(min(weights)>0); ck(I0==F(3,4)); ck(C==E); ck(q=={T:(1-4*rho)*PG.get(T,0)+3*rho*(T==0)+rho/64 for T in range(64)})
   for j in range(3):
    R=fullref(m,j,PG); Q,c,kap=mixture(PG,P,q,B,r,m,weights,components,R)
    ck(interval(add(c,{2:72*Is},scale(CE(P,Q),-1)))[0]>=0)
    ck(KL(P,Q)==add(scale(KL(PG,R),1-4*rho),scale(kap,-1))); refs+=1
   roots+=1
   if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 return {'Boolean_roots':roots,'reference_cases':refs,'marginal_mixture_weights':'(1-4rho,3rho,rho)','selector_coefficient':72}
def tensor():
 g=[-1 if x&7==0 else 1 for x in range(64)]; PG,P,q,B,I0,C,E,Is=lift(6,1,g,0); rho=F(1,32); U={T:F(1,64) for T in range(64)}; Q,c,kap=mixture(PG,P,q,B,1,6,[1-4*rho,3*rho,rho],[PG,{0:F(1)},U],U); cases=0
 for w in range(16):
  t=[1 if w>>x&1 else -1 for x in range(4)]; pq=spec(t)
  for j in range(2):
   rq=fullref(2,j,pq); pp={(S,T):v*m for S,v in P.items() for T,m in pq.items()}; qq={(S,T):v*m for S,v in Q.items() for T,m in rq.items()}
   ck(CE(pp,qq)==add(CE(P,Q),CE(pq,rq))); ck(KL(pp,qq)==add(KL(P,Q),KL(pq,rq))); ck(sum(qq.values())==sum(Q.values())*sum(rq.values())); cases+=1
   if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 return {'arbitrary_terminal_reference_cases':cases}
mode=sys.argv[1]; start=time.monotonic(); result=globals()[mode](); result.update(assertions=ar.N,seconds=time.monotonic()-start)
(RUN/f'out/{mode.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8'); print(json.dumps(result))

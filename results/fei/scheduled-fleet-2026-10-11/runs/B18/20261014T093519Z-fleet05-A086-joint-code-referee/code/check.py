import arithmetic as ar
from arithmetic import F,fw,spec,ck,L2
from pathlib import Path
from functools import lru_cache
from math import comb
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
@lru_cache(None)
def ln(q):
 a,b=ar.ln(q); D=1<<80
 return F(a.numerator*D//a.denominator,D),F(-((-b.numerator*D)//b.denominator),D)
def ce(P,Q):
 groups={}
 for T,v in P.items():
  if v: groups[Q[T]]=groups.get(Q[T],0)+v
 lo=hi=F(0)
 for q,v in groups.items():
  a,b=ln(q); lo-=v*b; hi-=v*a
 return lo,hi
def entropy(P): return ce(P,P)
def edges(t): return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range((len(t)-1).bit_length())]
def insert(x,j,b): return (x&((1<<j)-1))|(b<<j)|((x>>j)<<(j+1))
def remove(x,j): return (x&((1<<j)-1))|((x>>(j+1))<<j)
def physical_children(t,j): return [[t[insert(x,j,b)] for x in range(len(t)//2)] for b in range(2)]
def inherit(P,Q,children,j,zero=None):
 m={}; r={}; M=sum(Q.values())
 for s,v in P.items(): m[remove(s,j)]=m.get(remove(s,j),0)+v
 for s,v in Q.items(): r[remove(s,j)]=r.get(remove(s,j),0)+v
 ck(sum(m.values())==1); ck(sum(r.values())==M)
 for T in set(m)|set(children[0])|set(children[1]): ck(m.get(T,0)==(children[0].get(T,0)+children[1].get(T,0))/2)
 raw=[{},{}]
 for T,v in r.items():
  pi=[children[b].get(T,0)/(2*m[T]) for b in range(2)] if m.get(T,0) else (zero(T) if zero else [F(1,2),F(1,2)])
  ck(sum(pi)==1)
  for b in range(2):
   if pi[b]*v: raw[b][T]=2*v*pi[b]
 Z=[sum(x.values()) for x in raw]; ck(sum(Z)==2*M); ck(min(Z)>0)
 R=[{T:M*v/Z[b] for T,v in raw[b].items()} for b in range(2)]
 for b in range(2):
  ck(sum(R[b].values())==M)
  for T,v in children[b].items(): ck(v/R[b][T]==(m[T]/r[T])*(Z[b]/M))
 # KL release is paid from the same model, not a renewed descendant bank.
 ck(Z[0]*Z[1]<=M*M)
 return R,Z
def edited(g,r,a):
 n=(len(g)-1).bit_length(); p=F(1,1<<r); t=F(1,len(g)); mask=(1<<r)-1
 truth=[g[x>>r]-2*g[a]*int((x&mask)==0 and x>>r==a) for x in range(1<<(n+r))]
 A=fw(g); actual=fw(truth); expected={}
 for T in range(len(g)):
  b=g[a]*(-1)**(T&a).bit_count()
  for U in range(1<<r):
   c=(A.get(T,0) if U==0 else 0)-2*p*t*b
   if c: expected[U|(T<<r)]=c
 ck(actual==expected); P={S:v*v for S,v in actual.items()}; PG=spec(g)
 q={T:sum(v for S,v in P.items() if S>>r==T) for T in range(len(g))}
 beta=6*p*t; j=sum(g[a]!=g[a^(1<<i)] for i in range(n)); C=2*p*t*(n-j); E=2*p*t*j; J=2*r*p*t
 I=sum(edges(truth)); I0=sum(edges(g)); ck(I==I0+C-E+J); ck(E<=I0/2)
 ck(all(q[T]<=2*PG.get(T,0)+beta*t for T in q)); ck(min(q.values())>0)
 return truth,PG,P,q,beta,C,E,J,I,I0
def envelope():
 roots=models=queries=0
 for n in range(1,4):
  for w in range((1<<(1<<n)) if n<3 else 32):
   g=[1 if w>>x&1 else -1 for x in range(1<<n)]
   for a in range(len(g)):
    for r in [1,2]:
     truth,PG,P,q,beta,C,E,J,I,I0=edited(g,r,a); t=F(1,len(g))
     for R in [PG,{T:v/2 for T,v in PG.items()},{T:t for T in range(len(g))}]:
      s=sum(R.values()); Rd={T:(R.get(T,0)+beta*t)/(1+beta) for T in q}; Q={S:Rd[S>>r]*v/q[S>>r] for S,v in P.items()}; M=(s+beta)/(1+beta)
      ck(sum(Q.values())==M); cp=ce(P,Q); c=ce(PG,R)
      ck(cp[1]<=2*c[0]+15*(C+E+J)*L2[0])
      if I0:
       C0=c[1]/(L2[0]*I0); K=4*C0+15; ck(cp[1]<=K*I*L2[0])
      if n<3:
       for coord in range(n+r):
        ts=physical_children(truth,coord); ps=[spec(v) for v in ts]; inherit(P,Q,ps,coord); queries+=1
      models+=1
     roots+=1
     if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 return {'actual_roots':roots,'supplied_models':models,'same_mass_single_queries':queries}
def weak_root(k):
 n=k+4; zstar=(1<<(k//2))-1
 g=[(-1)**sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,k,2))*(-1 if ((x>>k)&7)==0 else 1) for x in range(1<<n)]
 tr,PG,P,q,beta,C,E,J,I,I0=edited(g,1,zstar); t=F(1,1<<n); Q={S:t*v/q[S>>1] for S,v in P.items()}
 ck(I0==F(k,2)+F(3,4)); ck(I==I0-t); ck(C==t*(F(k,2)+1)); ck(E==t*(F(k,2)+3)); ck(sum(Q.values())==1)
 cp=ce(P,Q); ck(cp[1]<=4*I*L2[0]); ck(4*I*L2[0]-cp[1]>=(k-1-(k+12)*t)*L2[0])
 return tr,P,Q,t
def weak():
 orders=0
 for k in [2,4]:
  tr,P,Q,t=weak_root(k); dummy=k+4; selector=0
  for first in [dummy,selector]:
   second=selector if first==dummy else dummy-1; ts=physical_children(tr,first); ps=[spec(x) for x in ts]; R,Z=inherit(P,Q,ps,first)
   hp=entropy(P); hcs=[entropy(p) for p in ps]; delta_lo=hp[0]-(hcs[0][1]+hcs[1][1])/2
   ck(edges(tr)[first]==t); ck(delta_lo>(F(k,2)+5)*t*L2[1])
   whole_lo=ce(P,Q)[0]-sum(ce(ps[b],R[b])[1] for b in range(2))/2; ck(whole_lo>(F(k,2)+5)*t*L2[1])
   leaves=[]; finalI=F(0); finalHs=[]
   for b in range(2):
    cs=physical_children(ts[b],second); pp=[spec(x) for x in cs]; refs,z=inherit(ps[b],R[b],pp,second)
    for c in range(2):
     ck(sum(edges(cs[c]))>0); leaves.append((pp[c],refs[c])); finalI+=sum(edges(cs[c]))/4; finalHs.append(entropy(pp[c]))
   ck(sum(edges(tr))-finalI==2*t)
   PiHlo=hp[0]-sum(h[1] for h in finalHs)/4
   ck(PiHlo>(F(3*k,2)+9)*t*L2[1]); orders+=1
   if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 return {'actual_even_widths':[2,4],'two_query_orders':orders,'all_leaves_nonconstant':True}
def shock():
 certificates=[]; cases=0
 for n in range(2,11):
  N=1<<n; t=F(1,N); g=[-1 if x&1==0 else 1 for x in range(N)]; tr,PG,P,q,beta,C,E,J,I,I0=edited(g,1,0)
  R={T:F(1,2*(N-2)) for T in range(N) if T not in [0,1]}; R[1]=F(1,2); Rd={T:(1-2*t)*R.get(T,0)+2*t*t for T in range(N)}; Q={S:Rd[S>>1]*v/q[S>>1] for S,v in P.items()}
  ck(sum(Q.values())==1); ck(I==1+(n-1)*t); ck(ce(P,Q)[1]<=12*I*L2[0])
  ts=physical_children(tr,1); ps=[spec(x) for x in ts]; refs,Z=inherit(P,Q,ps,1)
  negative=0; positive=1; qA=1-2*t+2*t*t; RA=(1-2*t)/2+2*t*t; rv=t*t+RA*(1-t)**2/qA
  ck(Z[positive]==rv/qA); ck(Z[negative]==2-rv/qA); rn=(1-2*t)**2*rv/(2*qA-rv); ck(refs[negative][0]==rn); ck(rn<F(1,3)); ck(sum(edges(ts[negative]))==2*n*t)
  if n>=3: ck(ce(ps[negative],refs[negative])[0]>F(9,16)*L2[1])
  ck(entropy(ps[negative])[1]<4*(2*n*t)*L2[0])
  ck(ce(P,Q)[1]<=(1+10*(n+1)*t)*L2[0]); ck(1+10*(n+1)*t<=F(34,3)*(1-t))
  certificates.append({'n':n,'negative_vacuum':str(ps[negative][0]),'reference_vacuum':str(rn),'Z_positive':str(Z[positive]),'root_reference_mass':'1'}); cases+=1
  if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 # Reconstruct the source's all-n Bernstein certificate independently.
 coeff=[F(3),F(-18,4),F(51,16),F(-79,64),F(66,256),F(-24,1024)]
 bern=[sum(coeff[j]*F(comb(i,j),comb(5,j)) for j in range(i+1)) for i in range(6)]
 ck(bern==[F(3),F(21,10),F(243,160),F(145,128),F(557,640),F(11,16)]); ck(min(bern)>0)
 (RUN/'out/SHOCK_CERTIFICATES.json').write_text(json.dumps({'actual_cases':certificates,'Bernstein_coefficients':[str(x) for x in bern]},indent=2)+'\n',encoding='utf8')
 return {'actual_dimensions':list(range(2,11)),'actual_shock_cases':cases,'all_n_Bernstein_certificate':'PASS'}
def terminal():
 tr,P,Q,t=weak_root(2); j=6; ts=physical_children(tr,j); ps=[spec(x) for x in ts]; refs,Z=inherit(P,Q,ps,j); width=(len(tr)-1).bit_length(); cases=0
 # Core posterior on zero terminal fibers must preserve the original model/mass.
 m={}; r={}
 for S,v in P.items(): m[remove(S,j)]=m.get(remove(S,j),0)+v
 for S,v in Q.items(): r[remove(S,j)]=r.get(remove(S,j),0)+v
 def corepi(T): return [ps[b].get(T,0)/(2*m[T]) for b in range(2)] if m.get(T,0) else [F(1,2),F(1,2)]
 for w in range(16):
  h=[1 if w>>x&1 else -1 for x in range(4)]; ph=spec(h)
  for mass in [F(1),F(1,2)]:
   rh={T:mass/4 for T in range(4)}; prodP={S|(T<<width):v*z for S,v in P.items() for T,z in ph.items()}; prodQ={S|(T<<width):v*z for S,v in Q.items() for T,z in rh.items()}; childs=[{S|(T<<(width-1)):v*z for S,v in ps[b].items() for T,z in ph.items()} for b in range(2)]
   out,z=inherit(prodP,prodQ,childs,j,zero=lambda T:corepi(T&((1<<(width-1))-1)))
   for b in range(2):
    expected={S|(T<<(width-1)):v*q for S,v in refs[b].items() for T,q in rh.items()}; ck(out[b]==expected)
   cases+=1
   if time.monotonic()-start>55: raise RuntimeError('pilot cutoff')
 return {'terminal_reference_cases':cases,'normalized_and_subprobability_models':True,'zero_fiber_product_transport':'PASS'}
mode=sys.argv[1]; start=time.monotonic(); result=globals()[mode](); result.update(assertions=ar.N,seconds=time.monotonic()-start)
(RUN/f'out/{mode.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8'); print(json.dumps(result))

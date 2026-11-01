from pathlib import Path
from fractions import Fraction as Q
from math import comb
from functools import lru_cache
import time,json,hashlib
import arithmetic as M
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(t):
 global checks
 assert t; checks+=1
 if time.perf_counter()-start>58: raise RuntimeError('Frozen pilot guard reached')
M.log=lru_cache(None)(M.log)
@lru_cache(None)
def ent(ps): return M.entropy(ps)
def H(ps): return ent(tuple(sorted(p for p in ps if p)))
def Phi(a,b): return M.add(H((a,b)),M.mul(-1,H((a+b,))))
def sub(a,b): return M.add(a,M.mul(-1,b))
@lru_cache(None)
def spec(t):
 a=tuple(M.walsh(t));return a,tuple(x*x for x in a)
def slice_(t,i,bit): return tuple(t[x] for x in range(len(t)) if (x>>i&1)==bit)
def infl(t,i):return Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def inf(t): return sum((infl(t,i) for i in range(len(t).bit_length()-1)),Q(0))
def Bi(p,i):return M.add(*(Phi(p[x],p[x|(1<<i)]) for x in range(len(p)) if not x>>i&1))
def BB(p):return M.add(*(Bi(p,i) for i in range(len(p).bit_length()-1)))
def majority(n):return tuple(1 if n-2*x.bit_count()>0 else -1 for x in range(1<<n))
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
records=[]
for r in range(1,65):
 N=2*r;rho=Q(comb(N,r),1<<N)
 # Direct coefficient of the zero-level derivative, not A003's recurrence implementation.
 c={l+1:Q(sum((-1)**j*choose(l,j)*choose(N-l,r-j) for j in range(l+1)),1<<N) for l in range(0,N+1,2)}
 ck(c[1]==rho)
 even=Q(0);odd_product=Q(0);inner_energy=Q(0)
 for t in range(N):
  a=c[t+1] if t%2==0 else c[t]
  b=c[t+1] if t%2==0 else c[t+2]
  count=comb(N-1,t);inner_energy+=count*b*b
  if t%2==0: even+=count*a*a; ck(a==b)
  else:
   odd_product+=count*abs(a*b)
   ck(t*c[t]+(N-t)*c[t+2]==0)
   ck(count*abs(a*b)==comb(N-1,t-1)*a*a)
 ck(even==rho/2);ck(odd_product==rho/2);ck(inner_energy==rho)
 # Sum Phi <= 2 sum |a b|, whose RHS is exactly 2rho.
 ck(2*(even+odd_product)==2*rho)
 if r<=4:
  for bit in (0,1):
   t=slice_(majority(N+1),0,bit);a,p=spec(t)
   for s in range(len(t)):
    degree=s.bit_count();expected=c[degree] if degree%2 else (1 if bit==0 else -1)*c[degree+1]
    ck(a[s]==expected)
   ck(a[0]==(1 if bit==0 else -1)*rho)
   for i in range(N):
    ck(infl(t,i)==rho);ck(a[1<<i]==rho)
    value=Bi(p,i); ck(not value or M.bounds(sub({2:2*rho},value))[0]>=0)
    if r==1:ck(value=={2:Q(1)})
 records.append({'r':r,'rho':str(rho),'even_energy':str(even),'odd_product_sum':str(odd_product),'bound':str(2*rho)})
(R/'out'/'KRAWTCHOUK_CERTIFICATE.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('KRAWTCHOUK_PASS',checks,flush=True)
composed=0;tree_nodes=0
def conditioning(p):
 b=BB(p);dtc=sub(H(p),b);v=1-p[0]
 if not v:ck(not b and not dtc);return
 q=tuple(Q(0) if x==0 else p[x]/v for x in range(len(p)))
 t0=M.add(*(Phi(p[0],p[1<<i]) for i in range(len(p).bit_length()-1)))
 ck(b==M.add(M.mul(v,BB(q)),t0))
 ck(dtc==M.add(M.h2(v),M.mul(v,sub(H(q),BB(q))),M.mul(-1,t0)))
 ck(H(p)==M.add(M.h2(v),M.mul(v,H(q))))
for mask in range(16):
 outer=tuple(1 if mask>>x&1 else -1 for x in range(4))
 A=tuple(Q(outer[x<<1]+outer[(x<<1)|1],2) for x in range(2))
 D=tuple(Q(outer[x<<1]-outer[(x<<1)|1],2) for x in range(2))
 delta=sum(d*d for d in D)/2;Aa=M.walsh(A);Dd=M.walsh(D)
 for n in (3,5,7):
  for bit in (0,1):
   h=slice_(majority(n),0,bit);ha,hp=spec(h);mu=ha[0];rho=Q(comb(n-1,(n-1)//2),1<<(n-1))
   t=tuple(outer[((x>>(n-1))<<1)|(0 if h[x&((1<<(n-1))-1)]==1 else 1)] for x in range(1<<n))
   a,p=spec(t);conditioning(p)
   for i in range(n-1):
    gamma=ha[1<<i];ck(gamma==rho)
    collision=M.add(*(Phi((Aa[j]+mu*Dd[j])**2,gamma**2*Dd[j]**2) for j in range(2)))
    inherited=M.mul(delta,sub(Bi(hp,i),Phi(mu**2,gamma**2)))
    ck(Bi(p,i)==M.add(inherited,collision));ck(infl(t,i)==delta*rho)
    ck(inherited==M.mul(delta,sub(Bi(hp,i),{2:2*rho*rho})))
    ck(sum((Aa[j]+mu*Dd[j])**2 for j in range(2))==1-delta+mu*mu*delta)
    if delta:
     # Certify the sharper concavity bound; the analytic log majorant follows separately.
     bound=M.add({2:delta*(2*rho-2*rho*rho)},Phi(1-delta+rho*rho*delta,rho*rho*delta))
     margin=sub(bound,Bi(p,i));ck(not margin or M.bounds(margin)[0]>=0)
   composed+=1
(R/'out'/'COMPOSITION_RECEIPT.json').write_text(json.dumps({'cases':composed,'assertions_so_far':checks,'status':'PASS'},indent=2)+'\n',encoding='utf-8')
print('COMPOSITION_PASS',checks,flush=True)
def tree(t,labels,counts):
 global tree_nodes
 tree_nodes+=1;_,p=spec(t);conditioning(p);hh=H(p);ii=inf(t)
 available=[j for j,(block,pos) in enumerate(labels) if counts[block]<2]
 if not available:
  v=1-p[0]; conditional={} if not v else M.mul(v,H(tuple(Q(0) if x==0 else p[x]/v for x in range(len(p)))))
  # Fields are expected terminal H, terminal I, total erasure, total JS, terminal mixing, terminal conditional H.
  return hh,ii,{}, {},M.h2(v),conditional
 # A genuinely adaptive block order, depending on the actual remaining truth table.
 block=min(labels[j][0] for j in available) if t[0]>0 else max(labels[j][0] for j in available)
 i=next(j for j in available if labels[j][0]==block)
 child=[slice_(t,i,z) for z in (0,1)];cp=[spec(c)[1] for c in child]
 projected=tuple(p[x]+p[x|(1<<i)] for x in range(len(p)) if not x>>i&1)
 b=Bi(p,i);js=sub(H(projected),M.mul(Q(1,2),M.add(H(cp[0]),H(cp[1]))))
 ck(sub(hh,M.mul(Q(1,2),M.add(H(cp[0]),H(cp[1]))))==M.add(b,js))
 ck(ii==infl(t,i)+sum(inf(c) for c in child)/2)
 nc=list(counts);nc[block]+=1;nl=labels[:i]+labels[i+1:]
 children=[tree(c,nl,tuple(nc)) for c in child]
 out=[]
 for k in range(6):
  out.append(sum((q[k] for q in children),Q(0))/2 if k==1 else M.mul(Q(1,2),M.add(*(q[k] for q in children))))
 out[2]=M.add(out[2],b);out[3]=M.add(out[3],js)
 ck(hh==M.add(out[0],out[2],out[3]))
 ck(out[0]==M.add(out[4],out[5]))
 # Signed one-budget deficit; K=5 is simply an identity calibration, not a claimed bound.
 ck(sub({2:5*ii},hh)==M.add(sub({2:5*out[1]},out[0]),{2:5*(ii-out[1])},M.mul(-1,M.add(out[2],out[3]))))
 return tuple(out)
for mask in range(16):
 outer=tuple(1 if mask>>x&1 else -1 for x in range(4));maj=majority(3)
 t=tuple(outer[(0 if maj[x&7]==1 else 1)|((0 if maj[x>>3]==1 else 1)<<1)] for x in range(64))
 tree(t,tuple((j//3,j%3) for j in range(6)),(0,0))
# Constant cutoff algebra checks: independent integer/rational certificates, no enormous encoders instantiated.
constants=[]
for k in range(4,65,2):
 delta0=Q(1,1<<k);s=Q(1,1<<(k//2));MM=2*k*k*(1<<(2*k+4))+1
 ck(4*k<=1<<(k+1));ck(delta0*Q(6*k,Q(1))+delta0*Q(11,2)<=Q(59,512)*4*k)
 ck(Q(1,2)+2*s-12*delta0>=Q(1,4))
 margin=k*(Q(1,2)+2*s-12*delta0)-Q(6*k,MM)-Q(5*k,2*(MM-2))-delta0
 ck(margin>0);ck(MM>=128)
 constants.append({'k':k,'M':str(MM),'eligibility_margin_lower':str(margin)})
ck(M.ln_interval(Q(2))[0]>Q(2,3))
(R/'out'/'CONSTANT_CERTIFICATES.json').write_text(json.dumps(constants,indent=2)+'\n',encoding='utf-8')
result={'helper_version':'A004-Krawtchouk-review-v1','status':'PASS','assertions':checks,'Krawtchouk_r_cases':64,'physical_slice_cases':8,'composed_slice_cases':composed,'adaptive_trees':16,'adaptive_nodes':tree_nodes,'constant_calibrations':31,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction/integer Krawtchouk plus FWHT; exact prime-log identities and proved rational intervals','helper_sha256':hashlib.sha256((R/'code'/'arithmetic.py').read_bytes()).hexdigest()}
(R/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result),flush=True)

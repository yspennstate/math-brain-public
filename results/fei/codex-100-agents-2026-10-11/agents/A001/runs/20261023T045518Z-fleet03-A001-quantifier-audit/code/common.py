from helpers import *
import helpers

def CE(p,q):
 ck(len(p)==len(q) and sum(p)==sum(q)==1)
 ck(all(b>0 for a,b in zip(p,q) if a))
 return add(*[(-a,log(b)) for a,b in zip(p,q) if a])
def marginal(p,j):return tuple(p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2))
def query(v,Q,j):
 p=spectrum(v);ch=[transport(v,j,s) for s in (0,1)];pc=[spectrum(c) for c in ch];m=marginal(p,j);r=marginal(Q,j);B=erase(v,j)
 ck(tuple((a+b)/2 for a,b in zip(*pc))==m)
 rho=add((1,CE(p,Q)),(-1,entropy(p)),(-1,CE(m,r)),(1,entropy(m)))
 ck(not rho or interval(rho)[0]>=0)
 ck(add((1,B),*[(F(1,2),CE(t,r)) for t in pc])==add((1,CE(p,Q)),(-1,rho)))
 return ch,pc,r,B,rho
MAJ=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
def actual(k,r,ctrl=MAJ):
 return tuple(ctrl[x] if y==0 else (1 if y&((1<<k)-1)==0 else -1) for y in range(1<<r) for x in range(len(ctrl)))
def source(k,r,z,ctrl=MAJ,edited=True):
 s=F(1,1<<k);t=F(1,1<<r);mu=1-2*s;nc=len(ctrl);pg=spectrum(tuple(-1 if y&((1<<k)-1)==0 else 1 for y in range(1<<r)))
 V=tuple(mu*mu if T==0 else (1-mu*mu)/((1<<r)-1) for T in range(1<<r));R=tuple((1-z)*a+z*b for a,b in zip(pg,V));ck(sum(R)==1)
 if not edited:return tuple(R[T] if S==0 else F(0) for T in range(1<<r) for S in range(nc))
 psi=tuple(F(1-c,2) for c in ctrl);pp=sum(psi)/nc;e=2*pp*t;ck(0<=e<=s)
 ph=amplitudes(psi);gh=amplitudes(tuple(-1 if y&((1<<k)-1)==0 else 1 for y in range(1<<r)))
 p=tuple((gh[T]*(S==0)+2*t*ph[S])**2 for T in range(1<<r) for S in range(nc));ck(p==tuple(spectrum(actual(k,r,ctrl))))
 q=tuple(sum(p[T*nc:(T+1)*nc]) for T in range(1<<r));ck(q==tuple(a*a+2*e*a+2*e*t for a in gh))
 rp=tuple((1-e/s)*a+(e/s)*mu*(T==0)+2*e*t for T,a in enumerate(R));ck(sum(rp)==1 and min(rp)>0 and min(q)>=0)
 if z==0:ck(rp==q)
 Q=tuple((rp[T]*p[T*nc+S]/q[T] if q[T] else rp[T]*(S==0)) for T in range(1<<r) for S in range(nc));ck(sum(Q)==1)
 return Q

def rec(d):
 lo,hi=interval(d)
 return {'prime_log':enc(d),'interval':[str(lo),str(hi)],'millionth_enclosure':[(lo*10**6).__floor__(),(hi*10**6).__ceil__()]}

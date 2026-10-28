"""v1: exact ghost-singleton transfer and independent A097 review."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,hashlib
# Both paths are A079-owned; do not import the reviewed author's implementation.
OLD=Path(__file__).resolve().parents[2]/'20261023T034945Z-account03-A079-correlated-auxiliaries/code'
sys.path.insert(0,str(OLD))
import check as c
ROOT=Path(__file__).resolve().parents[1]
def save(n,x):(ROOT/'out'/n).write_text(json.dumps(c.dump(x),indent=2)+'\n',encoding='utf-8',newline='')
a,b=c.rows((-1,)*4);A,B=c.coeff(a),c.coeff(b);beta=sum(x*x for x in B)
C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B));E=sum(y**4 for y in B);Gamma=C-D*D/E
def labels(n,i):
 return tuple((t&((1<<i)-1))+((t>>i)<<(i+1)) for t in range(1<<(n-1)))
def cond_nonempty(p,r,i):
 ans={}
 for t in labels(len(p).bit_length()-1,i)[1:]:
  pp=(p[t],p[t+(1<<i)]);qq=(r[t],r[t+(1<<i)]);w=sum(pp)
  if w:ans=c.add((1,ans),(w,c.kl(tuple(v/w for v in pp),tuple(v/sum(qq) for v in qq))))
 return ans
def ghost(h,i,r,s,lam=None,target_kind=0):
 p=c.prob(h);n=len(h).bit_length()-1;m=c.mean(h);t=1-m*m
 c.ok(c.coeff(h)[1<<i]==0);c.ok(r[0]==m*m)
 q=c.coherent(a,b,h,r,s);v=c.truth(a,b,h,s);pv=c.prob(v);j=4+i
 star=cond_nonempty(p,r,i);rho=r[1<<i];theta=rho/t if t else F(0)
 if lam is None:lam=theta/2
 c.ok(F(0)<=theta<1 or t==0);c.ok(F(0)<=lam<1)
 rbar=c.marginal(r,i);cost=[];eta=[];records=[]
 for bit in (0,1):
  hh=c.restrict(h,i,bit);pp=c.prob(hh);rc=c.cal(rbar,m*m)
  target=c.profile(len(hh)-1,(target_kind+bit)%2) if len(hh)>1 else ()
  qnew,rnew=c.fresh(a,b,hh,rc,s,lam,target)
  true=c.prob(c.truth(a,b,hh,s));c.ok(all(x in (-1,1) for x in c.truth(a,b,hh,s)))
  cost.append(c.ce(true,qnew))
  eta.append(c.add((1,c.kl(c.tail(pp),c.tail(rnew))),(-1,c.kl(c.tail(pp),c.tail(rc)))) if t else {})
  records.append(dict(seed=hh,reference=qnew,spectrum=true,source_reference=rnew))
 L=c.log(1/(1-theta))
 pred=c.add((-beta,star),(-beta*t,L),(beta*t/2,eta[0]),(beta*t/2,eta[1]))
 actual=c.add((1,c.erasure(pv,j)),(F(1,2),cost[0]),(F(1,2),cost[1]),(-1,c.ce(pv,q)))
 c.ok(c.erasure(pv,j)==c.add((beta,c.erasure(p,i))));c.ok(actual==pred)
 bound=c.add((-beta,star),(-beta*t,L),(beta*t,c.log(1/(1-lam))))
 c.ok(c.sign(c.add((1,bound),(-1,actual)))>=0)
 if lam<=theta:c.ok(c.sign(actual)<=0)
 return dict(actual=actual,bound=bound,theta=theta,rho=rho,lambda_=lam,Dstar=star,terminals=records)
def main_domain(pilot):
 candidates=admitted=isospectral=0
 for n in ([2] if pilot else [2,3]):
  for code in range(1<<(1<<n)):
   if time.monotonic()>deadline:raise TimeoutError('frozen limit')
   h=tuple(1-2*((code>>x)&1) for x in range(1<<n));p=c.prob(h);m=c.mean(h)
   for i in range(n):
    for k in (0,1):
     r=c.cal(c.profile(1<<n,k),m*m)
     for s in (1,-1):
      candidates+=1
      if c.coeff(h)[1<<i]:continue
      ghost(h,i,r,s,target_kind=k);admitted+=1
      labs=labels(n,i);isospectral+=all(c.coeff(h)[t]*c.coeff(h)[t+(1<<i)]==0 for t in labs)
 return dict(candidates=candidates,admitted_zero_singleton=admitted,isospectral_cases=isospectral)
def review_phase():
 hs=[tuple(1-2*((code>>x)&1) for x in range(4)) for code in range(16)]
 hs += [tuple((-1 if x&4 else 1)*(-1 if x&3==0 else 1) for x in range(8)),tuple((-1)**x.bit_count() for x in range(8))]
 c.ok((beta,E,Gamma)==(F(3,8),F(21,512),F(9,3584)))
 cases=0
 for h in hs:
  n=len(h).bit_length()-1;p=c.prob(h);hc=c.coeff(h);m=c.mean(h)
  for i in range(n):
   labs=labels(n,i);u=[hc[t] for t in labs];v=[hc[t+(1<<i)] for t in labs];d=v[0]
   bins=[[t for t in range(1,len(labs)) if (u[t]*v[t]>=0)==pos] for pos in (True,False)]
   bins=[z for z in bins if z];cs=[sum(u[t]*v[t] for t in z) for z in bins]
   x=Gamma*d*d+E*sum(z*z for z in cs)
   for k in (0,1):
    r=c.cal(c.profile(len(h),k),m*m);rb=c.marginal(r,i)
    for s in (1,-1):
     pv=c.prob(c.truth(a,b,h,s));q=c.coherent(a,b,h,r,s);cost=[]
     for bit in (0,1):
      hh=c.restrict(h,i,bit);pp=c.prob(hh);rr=[F(0)]*len(pp);rr[0]=c.mean(hh)**2
      for block in bins:
       mass=sum(pp[t] for t in block);ref=sum(rb[t] for t in block)
       if mass:
        c.ok(ref>0)
        for t in block:rr[t]=mass*rb[t]/ref
      c.ok(sum(rr)==1);tailmass=beta*(1-rr[0]);eps=x/(tailmass+x) if tailmass*x else F(0)
      qq,_=c.fresh(a,b,hh,tuple(rr),s,eps,c.profile(len(hh)-1,k))
      cost.append(c.ce(c.prob(c.truth(a,b,hh,s)),qq))
     inc=c.add((1,c.erasure(pv,4+i)),(F(1,2),cost[0]),(F(1,2),cost[1]),(-1,c.ce(pv,q)))
     # Analytic Pinsker supplies stronger -x/ln2; rational -x is an exact finite guard.
     c.ok(c.sign(c.add((-1,inc),(-x,{2:F(1)})))>=0);cases+=1
 return dict(status='PASS',transactions=cases,beta=beta,E4=E,Gamma=Gamma)
def sharp():
 h=tuple((-1)**x.bit_count() for x in range(8));p=c.prob(h);fixtures=[]
 for rho in (F(0),F(1,128),F(1,64),F(1,32),F(1,2)):
  r=tuple((1-rho)*v+rho*(t==1) for t,v in enumerate(p))
  for lam in (rho,F(1,64)):
   for s in (1,-1):
    out=ghost(h,0,r,s,lam)
    # Use a genuinely disjoint singleton target for the exact sharp identity.
    q=c.coherent(a,b,h,r,s);hh=c.restrict(h,0,0);rc=c.cal(c.marginal(r,0),F(0))
    qq,_=c.fresh(a,b,hh,rc,s,lam,(F(1),F(0),F(0)))
    actual=c.add((1,c.ce(c.prob(c.truth(a,b,hh,s)),qq)),(-1,c.ce(c.prob(c.truth(a,b,h,s)),q)))
    exact=c.add((beta,c.log((1-rho)/(1-lam))))
    c.ok(actual==exact);c.ok(c.sign(actual)==((lam>rho)-(lam<rho)))
    fixtures.append(dict(rho=rho,lambda_=lam,sign=s,increment=actual,phase_energy=0,source_price=c.add((beta,c.log(1/(1-rho)))),full_new_reference=qq,child_spectrum=c.prob(c.truth(a,b,hh,s))))
 save('sharp_zero_phase.json',dict(status='PASS',seed=h,fixtures=fixtures,sharp_price='beta log2((1-rho)/(1-lambda)); zero iff lambda=rho',ghost_injection_is_exact_prepayment=True))
def main():
 global deadline
 start=time.monotonic();pilot='--pilot' in sys.argv;deadline=start+(55 if pilot else 120)
 domain=main_domain(pilot)
 if not pilot:save('review_A097.json',review_phase());sharp()
 out=dict(status='PASS',pilot=pilot,assertions=c.checks,seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inherited_helper_sha256=hashlib.sha256((OLD/'check.py').read_bytes()).hexdigest(),**domain)
 save('pilot.json' if pilot else 'validation.json',out);print(json.dumps(out))
if __name__=='__main__':main()

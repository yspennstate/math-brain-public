from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json, time, hashlib, sys
sys.dont_write_bytecode = True
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'out'
N=0
def ck(v):
 global N
 N+=1
 if not v: raise AssertionError(N)
def save(name,x):
 (OUT/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def walsh(f):
 a=list(f); h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [Q(x,len(a)) for x in a]
def law(f):return [x*x for x in walsh(f)]
def inf(f):
 n=(len(f)-1).bit_length()
 return sum((Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)),Q(0))
def project(p,keep):
 a=[Q(0)]*(1<<len(keep))
 for x,v in enumerate(p):a[sum(((x>>i)&1)<<j for j,i in enumerate(keep))]+=v
 return a
def restrict(f,state):
 free=[i for i,s in enumerate(state) if s==-1]
 return [f[sum((b if b!=-1 else (x>>free.index(i))&1)<<i for i,b in enumerate(state))] for x in range(1<<len(free))],free
@lru_cache(None)
def ln(x):
 x=Q(x); ck(x>0)
 z=(x-1)/(x+1); v=Q(0); zz=z*z; t=z
 for i in range(32):v+=2*t/(2*i+1);t*=zz
 err=2*abs(t)/(65*(1-zz))
 return v-err,v+err
@lru_cache(None)
def log(x):
 x=Q(x); e=0
 while x<1:x*=2;e-=1
 while x>=2:x/=2;e+=1
 a,b=ln(x);c,d=ln(Q(2))
 return Q(e)+a/d,Q(e)+b/c
def ce(p,q):
 lo=hi=Q(0)
 for a,b in zip(p,q):
  if a:
   ck(b>0);c,d=log(1/b);lo+=a*c;hi+=a*d
 return lo,hi
def full(core):
 # gate bit0, mask bits1,2, core above them
 return [1 if not(x&1) else (-1 if ((x>>1)&3)==0 else 1)*core[x>>3] for x in range(8*len(core))]
def fullref(qc):
 return [qc[x>>3]/16+Q(int((x>>1)==0),4) for x in range(8*len(qc))]
E=[(-1 if (x&1)==0 and ((x>>1)&3)==0 else 1)*(-1 if (x&1)==0 and ((x>>3)&3)==0 else 1) for x in range(32)]
PE=law(E)
def blocks(pilot):
 cert=[]; profiles=[]; ghosts=0
 states=list(product([-1,0,1],repeat=5))
 for state in states[:27] if pilot else states:
  g,free=restrict(E,state)
  essential=[i for i in range(len(free)) if any(g[x]!=g[x^(1<<i)] for x in range(len(g)))]
  clean=[g[sum(((x>>j)&1)<<i for j,i in enumerate(essential))] for x in range(1<<len(essential))]
  keep=[free[i] for i in essential];p=law(clean);r=project(PE,keep);ii=inf(clean)
  ck(sum(r)==sum(p)==1)
  den=len(clean)**2
  # CE <= 4I iff product R(t)^(den*P(t)) >= 2^(-4I*den).
  lhs=Q(1)
  for a,b in zip(p,r):
   if a:ck(b>0);ck((a*den).denominator==1);lhs*=b**int(a*den)
  exponent=4*ii*den;ck(exponent.denominator==1);ck(lhs*2**int(exponent)>=1)
  rawR=project(PE,free)
  if ii==0 and rawR[0]<1:ghosts+=1
  cert.append({'state':state,'keep':keep,'P':[str(x) for x in p],'R':[str(x) for x in r],'I':str(ii),'integer_log_certificate_ratio':str(lhs*2**int(exponent))})
  profiles.append((clean,r,state))
 save('BLOCK_CERTIFICATES.json',cert)
 return profiles,ghosts
def core_profiles(profiles,pilot):
 mu=Q(5,8)**5;rho=Q(1,32);p0=rho*(1-mu)/2
 count=negative=0
 for g,R,state in profiles:
  for flip in [1,-1]:
   g=[flip*x for x in g];P=law(g);nu=Q(sum(g),len(g));ig=inf(g)
   for kp in ([0] if pilot else [0,1,2]):
    r=Q(1,1<<kp);a=r*(1-nu)/2
    qc=[];formula=[]
    for x in range(2*(1<<kp)*len(g)):
     T=x>>(kp+1);u=x&1
     qc.append((1-2*p0)*Q(int(x==1),2)+Q(int(x==0),2)+rho*r*(R[T]+(1-2*mu)*int(T==0))/8)
     formula.append((1-2*a)*int(x==1)+r*r*(P[T]+(1-2*nu)*int(T==0))/4)
    ck(sum(qc)==sum(formula)==1);ck(min(qc)>0)
    negative+=int(1-2*a<0)
    for sigma in [1,-1]:
     core=[sigma if ((x>>1)&((1<<kp)-1))==0 and g[x>>(kp+1)]==-1 else (-1 if x&1 else 1) for x in range(len(qc))]
     pc=law(core);ck(pc==formula)
     cc=ce(pc,qc);cr=ce(P,R)
     ck(cc[1]<=2+2*r*(5+kp+4)+r*cr[0]/2)
     nonempty=[x for x in range(len(pc)) if x>>(kp+1)]
     direct=ce([pc[x] for x in nonempty],[qc[x] for x in nonempty])
     s=ce(P[1:],R[1:]);v=r*((1-nu*nu)*(5+kp+3))/2
     ck(direct[0]<=v+r*s[1]/2 and v+r*s[0]/2<=direct[1])
     f=full(core);pf=law(f);qf=fullref(qc);cf=ce(pf,qf);fi=4*inf(f)
     ck(sum(qf)==1);ck(fi==6+2*(kp-1)*a+r*ig-sigma*a)
     ck(cf[1]<=cc[0]/2+3)
     ck(fi-cf[1]>=2-r*(5+kp+7)+r*(ig-cr[0]/4))
     count+=1
   g=[flip*x for x in g]
 save('CORE_PROFILES.json',{'profiles':count,'negative_latent_coefficients':negative,'original_mu':str(mu),'original_p':str(p0)})
 return count
def literal_original():
 # Full original small table, used only to verify inherited reference formulas.
 k=1;rho=Q(1,2);mu=Q(5,8);p=rho*(1-mu)/2
 h=[(-1 if x&1 else 1) if ((x>>2)&1)==0 and E[x>>3]==-1 else (-1 if (x>>1)&1 else 1) for x in range(256)]
 ph=law(h);qh=[(v+int(i==1))/2 for i,v in enumerate(ph)]
 f=full(h);qf=fullref(qh);ck(sum(qf)==1)
 # q bit3 in full table; then expose a=1, clean four dead source bits.
 remaining=[0,1,2,4,5] # gate,mask,mask,u,padding
 proj=project(qf,remaining)
 for qb in [0,1]:
  state=[-1]*11;state[3]=qb;state[6]=1
  for i in range(7,11):state[i]=0
  leaf,free=restrict(f,state);ck(free==remaining)
  c=ce(law(leaf),proj);ck(c[0]>=0)
 # Positive-vacuum warning: no cleanup leaves a constant source with ghost mass.
 ck(project(PE,[1,2,3,4])[0]==Q(17,32))
 return 2
def posterior():
 # All outcomes, choices depend on both source and padding outcomes.
 leaves=[];rho=Q(1,8)
 def walk(state,depth):
  free=[i for i,x in enumerate(state) if x==-1]
  if depth==6 or not free or (depth>1 and sum(x==1 for x in state)%3==1):
   prob=Q(1,1<<sum(x!=-1 for x in state));kp=sum(state[i]==-1 for i in range(3))
   r=Q(0) if any(state[i]==1 for i in range(3)) else Q(1,1<<kp)
   leaves.append((prob,r,kp));return
  i=free[(sum((i+1)*(x+1) for i,x in enumerate(state))+depth)%len(free)]
  for b in [0,1]:s=state[:];s[i]=b;walk(s,depth+1)
 walk([-1]*8,0)
 ck(sum(w for w,r,k in leaves)==1);ck(sum(w*r for w,r,k in leaves)==rho);ck(sum(w*r*k for w,r,k in leaves)<=3*rho)
 ck(Q(11,8)-Q(17,32)==Q(27,32));ck(31**31>2**152)
 save('POSTERIOR.json',{'leaves':len(leaves),'E_r':str(sum(w*r for w,r,k in leaves)),'E_r_kprime':str(sum(w*r*k for w,r,k in leaves))})
 return len(leaves)
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv
 profiles,ghosts=blocks(pilot);n=core_profiles(profiles,pilot);lit=literal_original();leaves=posterior()
 result={'status':'PASS','assertions':N,'block_assignments':len(profiles),'core_profiles_both_signs':n,'constant_ghost_states':ghosts,'literal_original_leaves':lit,'adaptive_leaves':leaves,'seconds':time.perf_counter()-start,'pilot':pilot}
 save('PILOT.json' if pilot else 'CHECKS.json',result);print(json.dumps(result))
if __name__=='__main__':main()

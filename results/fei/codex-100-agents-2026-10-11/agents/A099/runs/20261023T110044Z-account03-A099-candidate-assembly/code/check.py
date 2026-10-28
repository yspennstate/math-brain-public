from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time,sys
import prior_exact as ex
R=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;CAP=50 if PILOT else 600
COUNT=0;ST=dict(transactions=0,positive_mixture_children=0,zero_singleton_positive_energy=0,matched_isospectral_queries=0)
def ck(v):
 global COUNT
 COUNT+=1
 assert v,COUNT
 assert time.monotonic()-START<CAP,'frozen wall cap'
def save(name,x):(R/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def coeff(f):
 a=list(map(F,f));s=1
 while s<len(a):
  for i in range(0,len(a),2*s):
   for j in range(i,i+s):a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return tuple(x/len(a) for x in a)
def insert(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def restrict(f,j,b):return tuple(f[insert(x,j,b)] for x in range(len(f)//2))
def margrow(q,j):return tuple(q[insert(x,j,0)]+q[insert(x,j,1)] for x in range(len(q)//2))
def flat(rows):return tuple(x for row in rows for x in row)
def calibration(p,q,bins):
 out=[F(0)]*len(p)
 for block in bins:
  a=sum(p[i] for i in block);b=sum(q[i] for i in block)
  if a:
   ck(b>0)
   for i in block:out[i]=a*q[i]/b
 return tuple(out)
def grouped(p,bins):return tuple(sum(p[i] for i in b) for b in bins)
@lru_cache(None)
def intervalprime(p):
 a,b=ex.log_bounds(p);D=2**80
 return F(a.numerator*D//a.denominator,D),F(-((-b.numerator*D)//b.denominator),D)
def bounds(e):
 a=b=F(0)
 for p,c in e.items():
  lo,hi=intervalprime(p);a+=c*(lo if c>=0 else hi);b+=c*(hi if c>=0 else lo)
 return a,b
LNLO,LNHI=ex.ln_bounds(F(2))
def natbounds(e):
 a,b=bounds(e);return min(a*LNLO,a*LNHI),max(b*LNLO,b*LNHI)
def nonpos(e):ck(not e or bounds(e)[1]<=0)
CTRL=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
AA=coeff(CTRL);BB=coeff(tuple(1-x*x for x in CTRL));BETA=sum(x*x for x in BB)
E4=sum(x**4 for x in BB);CC=sum(a*a*b*b for a,b in zip(AA,BB));DD=sum(a*b**3 for a,b in zip(AA,BB));GAMMA=CC-DD*DD/E4
ck((BETA,E4,GAMMA)==(F(3,8),F(21,512),F(9,3584)))
def wrap(hat,sigma,source=None):
 seed=tuple(x*x for x in hat) if source is None else source;m=hat[0]
 return tuple(((a+sigma*m*b)**2,)+tuple(b*b*x for x in seed[1:]) for a,b in zip(AA,BB))
def transaction(h,j,sigma,kind):
 hat=coeff(h);N=len(h);m=hat[0];d=hat[1<<j];p=tuple(x*x for x in hat)
 if kind==0:source=p
 else:
  tot=sum(range(2,N+1));source=(m*m,)+tuple((1-m*m)*i/tot for i in range(2,N+1))
 ck(sum(source)==1)
 par=flat(wrap(hat,sigma));qpar=flat(wrap(hat,sigma,source))
 qrows=tuple(margrow(row,j) for row in wrap(hat,sigma,source));q=flat(qrows)
 pmarg=flat(tuple(margrow(row,j) for row in wrap(hat,sigma)))
 hs=[restrict(h,j,b) for b in (0,1)];hats=[coeff(x) for x in hs];ps=[tuple(x*x for x in hh) for hh in hats]
 actual=[flat(wrap(hh,sigma)) for hh in hats];K=N//2
 ck(tuple((a+b)/2 for a,b in zip(*actual))==pmarg)
 # Direct pivotal edge fraction is independent of Fourier computation.
 influence=F(sum(h[x]!=h[x^(1<<j)] for x in range(N)),N)
 ck(influence==sum(p[t] for t in range(N) if t&(1<<j)))
 prod=[hat[insert(t,j,0)]*hat[insert(t,j,1)] for t in range(K)]
 signs=[tuple(t for t in range(1,K) if (prod[t]<0)==negative) for negative in (False,True)]
 cs=[sum(prod[t] for t in group) for group in signs]
 bins=[]
 for U in range(len(AA)):
  bins.append((U*K,))
  bins.extend(tuple(U*K+t for t in group) for group in signs if group)
 ck(sorted(i for b in bins for i in b)==list(range(len(q))))
 pblocks=[grouped(z,bins) for z in actual];qblocks=grouped(q,bins);mean=tuple((a+b)/2 for a,b in zip(*pblocks))
 rhos=[ex.kl(z,qblocks) for z in pblocks];rho=ex.sc(F(1,2),ex.add(*rhos))
 js=ex.add(ex.ent(mean),ex.sc(F(-1,2),ex.add(*(ex.ent(x) for x in pblocks))))
 ck(rho==ex.add(js,ex.kl(mean,qblocks)))
 discrepancy=sum((a-b)**2 for a,b in zip(mean,qblocks));halfdiff=sum(((a-b)/2)**2 for a,b in zip(*pblocks))
 direct=F(1,2)*sum(sum((a-b)**2 for a,b in zip(z,qblocks)) for z in pblocks)
 ck(direct==discrepancy+halfdiff)
 # Independently check A003's coarser vacuum/whole-tail discrepancy formula.
 coarse=[(U*K,) for U in range(len(AA))]+[tuple(U*K+t for U in range(len(AA)) for t in range(1,K))]
 pv=[grouped(z,coarse) for z in actual];qv=grouped(q,coarse)
 delta=source[1<<j]-d*d
 Fm=sum(b*b*(sigma*a+m*b)**2 for a,b in zip(AA,BB))
 vnorm=F(1,2)*sum(sum((a-b)**2 for a,b in zip(z,qv)) for z in pv)
 ck(vnorm==4*d*d*(Fm+BETA*BETA*m*m)+delta*delta*(E4+BETA*BETA))
 xd=GAMMA*d*d+(E4+BETA*BETA)*delta*delta/4
 ck(natbounds(rho)[0]>=2*xd or not rho and xd==0)
 x=GAMMA*d*d+E4*sum(c*c for c in cs)
 if d==0:
  V=sum(abs(a-b) for a,b in zip(*ps))/2;y=BETA*V*V/4
  ck(x==E4*V*V/8)
 else:y=x
 if not d and y:ST['zero_singleton_positive_energy']+=1
 ck(natbounds(rho)[0]>=2*y or (not rho and y==0))
 qcal=[calibration(z,q,bins) for z in actual]
 fresh=[];epss=[];costs=[]
 for b in (0,1):
  z=actual[b];cal=qcal[b];tail=BETA*(1-ps[b][0]);eps=y/(tail+y) if tail*y else F(0);epss.append(eps)
  opposite=ps[1-b];mass=1-opposite[0]
  target=tuple(v/mass for v in opposite[1:]) if mass else (F(1,K-1),)*(K-1)
  out=list(cal)
  for U,bhat in enumerate(BB):
   for t in range(1,K):out[U*K+t]=(1-eps)*cal[U*K+t]+eps*bhat*bhat*(1-ps[b][0])*target[t-1]
  out=tuple(out);ck(sum(out)==1)
  cost=ex.add(ex.ce(z,out),ex.sc(-1,ex.ce(z,cal)));costs.append(cost)
  if cost and bounds(cost)[0]>0:ST['positive_mixture_children']+=1
  ck(natbounds(cost)[1]<=y or not cost)
  ck(ex.add(ex.ce(z,q),ex.sc(-1,ex.ce(z,cal)))==rhos[b]);fresh.append(out)
 B=ex.add(ex.ent(par),ex.sc(-1,ex.ent(pmarg)))
 occ=ex.add(ex.kl(par,qpar),ex.sc(-1,ex.kl(pmarg,q)))
 net=ex.add(B,ex.sc(F(1,2),ex.add(*(ex.ce(z,s) for z,s in zip(actual,fresh)))),ex.sc(-1,ex.ce(par,qpar)))
 ck(net==ex.add(ex.sc(-1,occ),ex.sc(-1,rho),ex.sc(F(1,2),ex.add(*costs))))
 release=ex.add(net,occ);ck(natbounds(release)[1]<=-y or not release and y==0)
 if d==0 and x==0 and kind==0:
  ck(actual[0]==actual[1]==q)
  ck(not B and not occ and not rho and not net);ST['matched_isospectral_queries']+=1
 ST['transactions']+=1
 return {'energy':str(y),'old_energy':str(x),'eps':list(map(str,epss)),'net':net,'parent':par,'children':actual,'Qparent':qpar,'Qnew':fresh}
def controller_faces():
 cases=0
 for state in itertools.product((-1,0,1),repeat=4):
  free=[i for i,z in enumerate(state) if z==0];table=[]
  for x in range(2**len(free)):
   idx=sum((1 if z==-1 else 0)<<i for i,z in enumerate(state) if z)
   for k,i in enumerate(free):idx|=((x>>k)&1)<<i
   table.append(CTRL[idx])
  a=coeff(table);b=coeff(tuple(1-z*z for z in table));beta=sum(t*t for t in b)
  c=sum(u*u*v*v for u,v in zip(a,b));d=sum(u*v**3 for u,v in zip(a,b));e=sum(v**4 for v in b)
  ck(sum(x*y for x,y in zip(a,b))==0 and sum(x*x for x in a)+beta==1)
  ck(c*e>=d*d)
  cases+=1
 return cases
def main():
 n=2 if PILOT else 3;N=2**n
 for table in range(2**N):
  h=tuple(1 if table&(1<<x) else -1 for x in range(N))
  for j in range(n):
   for sigma in (-1,1):
    for source in (0,1):transaction(h,j,sigma,source)
 # Full physical witness is independently computed rather than factorized only.
 h=tuple((1 if not x&4 else -1)*(-1 if x&3==0 else 1) for x in range(8));w=transaction(h,0,1,0)
 full=tuple(CTRL[u]+(1-CTRL[u]**2)*h[t] for u in range(16) for t in range(8))
 phys=tuple(x*x for x in coeff(full));ck(phys==w['parent']==w['Qparent'])
 for b in (0,1):ck(tuple(x*x for x in coeff(restrict(full,0,b)))==w['children'][b])
 expected=ex.sc(F(3,8),ex.logq(F(5,8)));ck(w['net']==expected and w['energy']=='3/32' and w['eps']==['1/5','1/5'])
 save('POSITIVE_WITNESS.json',{'seed':'x3 times two-bit point defect; query0; target other child spectrum','energy':w['energy'],'old_energy':w['old_energy'],'eps':w['eps'],
  'full_signed_increment':'(3/8)log2(5/8)','net_lower':str(bounds(w['net'])[0]),'net_upper':str(bounds(w['net'])[1]),'arithmetic':'literal128-vertex Boolean FWHT + exact prime-log identity'})
 parity=tuple((-1)**x.bit_count() for x in range(8));w0=transaction(parity,0,1,0)
 ck(w0['energy']=='0' and not w0['net'])
 # Force an excluded target ghost; both full child costs are positive.
 ghost=ex.sc(F(3,8),ex.logq(F(64,63)));ck(bounds(ghost)[0]>0)
 save('ZERO_ENERGY_CONTROL.json',{'seed':'parity3, exact incoming spectrum','query_ledger':'EXACT_ZERO','without_reset':'PAID with no surplus use',
  'forced_mixture':'1/64 toward distinct singleton, both full child bills (3/8)log2(64/63)>0','lower':str(bounds(ghost)[0]),'FEI_counterexample':False})
 faces=controller_faces()
 result=dict(status='PASS',pilot=PILOT,n=n,Boolean_tables=2**N,exact_assertions=COUNT,seconds=time.monotonic()-START,controller_faces=faces,**ST)
 save('PILOT.json' if PILOT else 'EXACT_PHASE_AUDIT.json',result);print(json.dumps(result))
if __name__=='__main__':main()

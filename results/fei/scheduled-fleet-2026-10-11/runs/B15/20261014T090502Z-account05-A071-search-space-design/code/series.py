"""Independent centered-bit polynomial interpolation and formal logarithm series."""
import time
from fractions import Fraction as Q
import arithmetic as a
def trim(x):
 x=list(x)
 while x and not x[-1]:x.pop()
 return x
def plus(x,y):return trim([(x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0) for i in range(max(len(x),len(y)))])
def scale(x,c):return trim([v*c for v in x])
def minus(x,y):return plus(x,scale(y,-1))
def times(x,y):
 z=[Q(0)]*max(0,len(x)+len(y)-1)
 for i,u in enumerate(x):
  for j,v in enumerate(y):z[i+j]+=u*v
 return trim(z)
ONE=[Q(1)];P=[Q(0),Q(1)]
def ev(x,p):return sum(v*p**i for i,v in enumerate(x))
def clean(d):return {k:v for k,v in d.items() if v}
def la(x,y,c=Q(1)):
 z=x.copy()
 for k,v in y.items():z[k]=z.get(k,Q(0))+c*v
 return clean(z)
def lc(x,c):return clean({k:v*c for k,v in x.items()})
def logformal(x):
 out={}
 for num,sgn in [(x.numerator,1),(x.denominator,-1)]:
  prime=2
  while prime*prime<=num:
   while num%prime==0:out[str(prime)]=out.get(str(prime),Q(0))+sgn;num//=prime
   prime+=1
  if num>1:out[str(num)]=out.get(str(num),Q(0))+sgn
 return clean(out)
def ls(x,y,c=Q(1)):return [la(u,v,c) for u,v in zip(x,y)]
def lm(x,p):
 z=[{} for _ in range(3)]
 for i,d in enumerate(x):
  for j,v in enumerate(p[:3-i]):z[i+j]=la(z[i+j],d,v)
 return z
def ell(x):
 z=[{} for _ in range(3)]
 if not x:return z
 r=next(i for i,v in enumerate(x) if v)
 if r>2:return z
 u=x[r];a.ck(u>0);v=x[r+1] if r+1<len(x) else Q(0);w=x[r+2] if r+2<len(x) else Q(0)
 L=logformal(u);L=la(L,{'P':Q(r)})
 z[r]=lc(L,-u)
 if r<=1:z[r+1]=la(lc(L,-v),{'E':-v})
 if r==0:z[2]=la(lc(L,-w),{'E':-w-v*v/(2*u)})
 return z
def outer(kind):
 ps=[P]*6
 if kind=='plus':ps=[[]]+[P]*5
 if kind=='minus':ps=[ONE]+[P]*5
 c=[[Q(v)] for v in a.J]
 for j,p in enumerate(ps):
  for x in range(64):
   if not x>>j&1:
    u,v=c[x],c[x|1<<j];c[x]=plus(u,times(p,minus(v,u)));c[x|1<<j]=minus(v,u)
 masses=[]
 for x,u in enumerate(c):
  w=times(u,u)
  for j,p in enumerate(ps):
   if x>>j&1:w=times(w,times(p,minus(ONE,p)))
  masses.append(w)
 a.ck(sum_poly(masses)==ONE)
 qs=[]
 for j in range(6):
  q=[]
  for x in range(64):
   if x>>j&1 or a.J[x]==a.J[x|1<<j]:continue
   w=ONE
   for k,p in enumerate(ps):
    if k!=j:w=times(w,p if x>>k&1 else minus(ONE,p))
   q=plus(q,w)
  qs.append(q)
 C=[{} for _ in range(3)]
 for w in masses:C=ls(C,ell(w))
 for q,p in zip(qs,ps):
  v=scale(times(p,minus(ONE,p)),Q(4));h=ls(ell(v),ell(minus(ONE,v)))
  C=ls(C,lm(h,q),Q(-1))
 return C,qs,masses
def sum_poly(xs):
 z=[]
 for x in xs:z=plus(z,x)
 return z
def val(d):
 z=(Q(0),Q(0))
 for k,v in d.items():
  a.ck(k!='P')
  x=a.lg(Q(int(k))) if k!='E' else (Q(a.NAT,a.LN2[1]),Q(a.NAT,a.LN2[0]))
  z=a.add(z,a.mul(x,v))
 return z
def run():
 t=time.perf_counter();data={k:outer(k) for k in ('parent','plus','minus')}
 Cp,qp,_=data['parent'];C0,_,_=data['plus'];C1,q1,_=data['minus']
 D=ls(ls(Cp,lm(C0,[Q(1),Q(-1)]),Q(-1)),lm(C1,P),Q(-1))
 a.ck(D==[{}, {}, {'2':Q(32),'E':Q(16)}])
 a.ck(C1==[{}, {}, {'2':Q(64),'E':Q(-32)}])
 a.ck(qp[0]==list(map(Q,[0,4,-14,18,-10,2])))
 a.ck(sum_poly(q1[1:])==list(map(Q,[0,16,-42,36,-10])))
 # Reconstruct leading core entropy from its exact multiplicity formula.
 eh=ell([Q(1),Q(-4),Q(4)])
 big=ell([Q(0),Q(0),Q(4)])
 small=ell([Q(0),Q(0),Q(4,9)])
 hlead=la(la(eh[1],big[2],Q(3,4)),small[2],Q(9,4))
 ilead={'3':Q(2),'P':Q(-2),'2':Q(-8,3)}
 slead=la(lc(ilead,Q(4)),hlead,Q(-1))
 a.ck(slead=={'3':Q(6),'2':Q(-8,3),'E':Q(-4)})
 ecoeff=la(D[2],slead,Q(-4));mcoeff=la(lc(slead,Q(16)),C1[2],Q(-1))
 a.ck(ecoeff=={'2':Q(128,3),'3':Q(-24),'E':Q(32)})
 a.ck(mcoeff=={'3':Q(96),'2':Q(-320,3),'E':Q(-32)})
 a.ck(val(ecoeff)[0]>Q(5079,100));a.ck(val(mcoeff)[1]<Q(-6765,10000))
 # Polynomial values compared with independently centered-bit numerical path, no source import.
 import search
 for kind,p0 in [('parent',Q(3,64)),('plus',Q(0)),('minus',Q(1))]:
  C,qs,masses=data[kind]
  a.ck([ev(q,Q(3,64)) for q in qs]==search.outer(p0)[1])
  Hp=a.entropy_prob([ev(w,Q(3,64)) for w in masses])
  correction=Hp
  for q,p in zip(qs,[p0]+[Q(3,64)]*5):correction=a.sub(correction,a.mul(a.h2(4*p*(1-p)),ev(q,Q(3,64))))
  a.ck(correction==search.outer(p0)[0])
 out={'method':'centered-bit polynomial interpolation; formal prime logarithms, exact rational coefficients; all p-log-p cancellations checked symbolically','D_series':D,'negative_C_series':C1,'core_S4_leading':slead,'excess_limit':ecoeff,'negative_endpoint_limit':mcoeff,'excess_interval':val(ecoeff),'endpoint_interval':val(mcoeff),'full_mass_polynomials':{k:v[2] for k,v in data.items()},'pivot_polynomials':{k:v[1] for k,v in data.items()},'checks':a.checks,'seconds':time.perf_counter()-t}
 a.save('INDEPENDENT_SERIES.json',out);print('independent series checks',a.checks,'seconds',out['seconds'])
if __name__=='__main__':run()

import sympy as s
from fractions import Fraction as F
from itertools import product
import json

eps,t,r=s.symbols('eps t r',real=True)
K0=s.Matrix([[s.Rational(9,40),s.Rational(1,10),s.Rational(1,40)],
             [s.Rational(1,10),s.Rational(2,25),s.Rational(1,10)],
             [s.Rational(1,40),s.Rational(1,10),s.Rational(9,40)]])
A=s.Matrix([[0,-s.Rational(2,5),-1],[-s.Rational(2,5),-s.Rational(8,25),-s.Rational(2,5)],[-1,-s.Rational(2,5),0]])
K=K0+eps*s.eye(3);xs=list(product([0,1],repeat=3));checks=0
def check(x):
 global checks
 assert x;checks+=1
def atoms(M):
 return [s.expand((-1)**(3-sum(x))*(M-s.diag(*[1-i for i in x])).det()) for x in xs]
p=atoms(K);pt=atoms(K+t*A)
v=[s.diff(z,t).subs(t,0) for z in pt];a=[s.diff(z,t,2).subs(t,0) for z in pt]
check(s.simplify(sum(p)-1)==0);check(s.simplify(sum(v))==0);check(s.simplify(sum(a))==0)
check(K0.charpoly().as_expr().factor()==s.Symbol('lambda')*(5*s.Symbol('lambda')-1)*(100*s.Symbol('lambda')-33)/500)
check(K0*A==A*K0)
check(s.simplify(p[-1]-eps*(eps+s.Rational(1,5))*(eps+s.Rational(33,100)))==0)
check(s.simplify(a[-1]+s.Rational(66,25)*eps)==0)
for z in p[:-1]:check(z.subs(eps,0)>0)

# Exact affine heat intertwining, including first and second jets.
Kr=s.eye(3)/2+r*(K-s.eye(3)/2)
pr=atoms(Kr+r*t*A)
for k in range(3):
 jet=[s.diff(z,t,k).subs(t,0) for z in pr]
 original=[s.diff(z,t,k).subs(t,0) for z in pt]
 for i,x in enumerate(xs):
  noise=0
  for j,y in enumerate(xs):
   noise+=original[j]*s.prod((1+r)/2 if x[b]==y[b] else (1-r)/2 for b in range(3))
  check(s.expand(jet[i]-noise)==0)

# Build Q and the complete noise forcing as rational plus log rational terms.
E=F(1,10**12)
def rat(z):
 z=s.cancel(z.subs(eps,s.Rational(E.numerator,E.denominator)))
 return F(int(s.numer(z)),int(s.denom(z)))
pp=list(map(rat,p));vv=list(map(rat,v));aa=list(map(rat,a))
qrat=sum(vv[i]**2/pp[i] for i in range(8));qlogs=list(zip(aa,pp))
drat=F(0);dlogs=[]
for i,x in enumerate(xs):
 for b in range(3):
  if x[b]:continue
  y=list(x);y[b]=1;j=xs.index(tuple(y));u,w=pp[i],pp[j]
  drat+=F(1,2)*((u+w)*(vv[i]/u-vv[j]/w)**2+aa[i]*(1-w/u)+aa[j]*(1-u/w))
  dlogs.append((F(1,2)*(aa[i]-aa[j]),u/w))

def log_small(q,N=100):
 z=(q-1)/(q+1);value=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
 err=2*abs(z)**(2*N+1)/(F(2*N+1)*(1-z*z))
 return value-err,value+err
L2=log_small(F(2))
def log_bounds(q):
 k=0
 while q<1:q*=2;k-=1
 while q>2:q/=2;k+=1
 lo,hi=log_small(q)
 if k>=0:return lo+k*L2[0],hi+k*L2[1]
 return lo+k*L2[1],hi+k*L2[0]
def enclose(base,terms):
 lo=hi=base
 for c,q in terms:
  a,b=log_bounds(q)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
qb=enclose(qrat,qlogs);db=enclose(drat,dlogs)
check(qb[0]>0);check(db[1]<0)
check(F(2812,1000)<qb[0] and qb[1]<F(2813,1000))
check(-F(7336,1000)<db[0] and db[1]<-F(7335,1000))

# Singular coefficient in dQ/ds: only p_111 vanishes.
ps=atoms(s.eye(3)/2+r*(K-s.eye(3)/2)+t*A)
asfull=s.diff(ps[-1],t,2).subs(t,0)
ads=s.simplify(-s.diff(asfull,r).subs(r,1))
check(ads.subs(eps,0)==-s.Rational(33,25))

out={'status':'PASS','exact_assertions':checks,'epsilon':'1/1000000000000',
     'curvature_interval':[float(qb[0]),float(qb[1])],
     'forcing_interval':[float(db[0]),float(db[1])],
     'forcing_log_epsilon_coefficient':'33/25'}
print(json.dumps(out,indent=2))
open('computations/X073/results.json','w').write(json.dumps(out,indent=2)+'\n')

"""Exact exploratory moment relaxation; output is not a theorem by itself."""
import itertools
import sympy as s
from memory_guard import install
install()
A,B,C,a,b,k,l=s.symbols('A B C a b k l')
d,e,f,h=s.symbols('d e f h')
x,y,X,Y=s.symbols('x y X Y')
mom={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(1,1):0,(0,2):1,(4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
def pairs(expr):
 out=0
 for (i,j,u,v),cc in s.Poly(s.expand(expr),x,y,X,Y).terms():out+=cc*mom.get((i,j),s.Symbol('m%d%d'%(i,j)))*mom.get((u,v),s.Symbol('m%d%d'%(u,v)))
 return s.expand(out)
ss=a+b;v=a*a+b*b
FM=a*(A+C)+b*(B+C)
hd=s.Rational(8,5)-s.Rational(4,5)*ss+FM
K=a*a*A+b*b*B+2*a*b*C-v/5-a*a*(d*d+e*e)-2*a*b*(e*e+f*f)-b*b*(f*f+h*h)
Z=pairs((s.Rational(1,5)+a*x*X+b*y*Y)*((x-X)**2+(y-Y)**2)*(a*(x-X)**2+b*(y-Y)**2))/2
Y5=4*(ss-v)-2*Z
mass=(4-ss+l)/2
T=s.expand(2*(ss-v)+2*(k+2)*K/k+(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*hd)-Y5)
base=T.subs({d:0,e:0,f:0,h:0});cubic=s.factor(T-base)
print('cubic=',cubic,flush=True)
from prior15.moment_polytope import vertices
vs=[tuple(s.Rational(x.numerator,x.denominator)for x in v)for v in vertices(True)]
print('vertices',len(vs),flush=True)
# Parametrize the triangle a>=b>=0, a+b<=1 by a=t/(1+r), b=tr/(1+r).
t,r,z=s.symbols('t r z')
for mode in ('no_lower','trace_endpoint'):
 expr=s.cancel((k*k*(base-a*a*C/3)).subs(l,0 if mode=='no_lower'else k-4).subs({a:t/(1+r),b:t*r/(1+r)})*(1+r)**2)
 expr=s.expand(expr.subs(k,5+z))
 bad=[];minimum=None
 for point in sorted(vs):
  pp=s.Poly(expr.subs(dict(zip([A,B,C],point))),z)
  for zz in range(3):
   pt=s.Poly(pp.nth(zz),t);cs=[pt.nth(0),pt.nth(0)+pt.nth(1)/2,pt.nth(0)+pt.nth(1)+pt.nth(2)]
   for j,cc in enumerate(cs):
    # exact quadratic minimum in r on [0,1]
    p=s.Poly(cc,r);vals=[cc.subs(r,0),cc.subs(r,1)]
    if p.degree()==2 and p.nth(2)>0:
     crit=-p.nth(1)/(2*p.nth(2))
     if 0<crit<1:vals.append(cc.subs(r,crit))
    mn=min(vals);minimum=mn if minimum is None else min(minimum,mn)
    if mn<0:bad.append((point,zz,j,mn))
 print(mode,'minimum',minimum,'bad',len(bad),'first',bad[:5],flush=True)

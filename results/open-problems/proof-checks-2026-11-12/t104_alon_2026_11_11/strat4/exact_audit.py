"""Independent exact checks of the pair expansions and analytic bounds."""
import sympy as s
xi,yi,xj,yj=s.symbols('xi yi xj yj')
a,b,A,B,C,d,e,f,h=s.symbols('a b A B C d e f h')
known={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(0,2):1,(1,1):0,(4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
def pair_sum(expr):
    out=0
    for (i,j,k,l),v in s.Poly(s.expand(expr),xi,yi,xj,yj).terms():
        out+=v*known.get((i,j),s.Symbol(f'm{i}{j}'))*known.get((k,l),s.Symbol(f'm{k}{l}'))/2
    return s.expand(out)
du=xi-xj;dw=yi-yj
identities=[(du**2,5),(dw**2,5),(du**4,5*A+3),(dw**4,5*B+3),(du**2*dw**2,5*C+1),
(xi*xj*du**2,-1),(xi*xj*dw**2,0),(yi*yj*du**2,0),(yi*yj*dw**2,-1),
(xi*xj*du**4,3*d*d-4*A),(yi*yj*dw**4,3*h*h-4*B),(xi*xj*dw**4,3*f*f),(yi*yj*du**4,3*e*e),
(xi*xj*du**2*dw**2,d*f+2*e*e-2*C),(yi*yj*du**2*dw**2,h*e+2*f*f-2*C)]
for expr,expected in identities:assert s.expand(pair_sum(expr)-expected)==0
lam=(2+a+b)/4;su=a+b;k2=a*a+b*b
F=a*(A+C)+b*(B+C)
K=a*a*A+b*b*B+2*a*b*C-k2/5-a*a*(d*d+e*e)-2*a*b*(e*e+f*f)-b*b*(f*f+h*h)
S5=pair_sum((lam/5+a*xi*xj+b*yi*yj)*(2-du*du-dw*dw)*(a*du*du+b*dw*dw))
X1=2*(lam*su-k2);X2=s.Rational(10,3)*K;X3=(1-lam)/9*(-2*su+10*F)
T=s.expand(X1+X2+X3-2*S5)
Cub=s.Rational(8,3)*a*a*d*d+s.Rational(8,3)*b*b*h*h+s.Rational(2,3)*a*(a+5*b)*e*e+s.Rational(2,3)*b*(b+5*a)*f*f+2*su*(a*d*f+b*h*e)
reduced=(14+2*su)/9*(F-su/5)+s.Rational(4,3)*k2-s.Rational(14,3)*(a*a*A+b*b*B)-4*(k2+a*b/3)*C+Cub
assert s.expand(T-reduced)==0
sq=s.Rational(8,3)*a*a*(d+3*su*f/(8*a))**2+s.Rational(8,3)*b*b*(h+3*su*e/(8*b))**2+(7*b-a)*(b+9*a)*f*f/24+(7*a-b)*(a+9*b)*e*e/24
assert s.factor(Cub-sq)==0
r=s.symbols('r')
assert s.expand(s.Rational(14,3)*a*F-(s.Rational(14,3)*(a*a*A+b*b*B)+4*(k2+a*b/3)*C)-s.Rational(14,3)*b*(a-b)*B-s.Rational(2,3)*(a-b)*(a+6*b)*C)==0
# Equal-gap invariant identity.
g,Kv,N,J=s.symbols('g K N J')
Teq=s.factor(T.subs({a:g,b:g}))
assert s.expand(Teq-g/s.Integer(45)*(70*(A+B+2*C)-28+g*(112-190*(A+B+2*C)+30*(d*d+3*e*e+3*f*f+h*h)+90*((d+f)**2+(e+h)**2))))==0
print('PROVED: all 15 pair-sum identities checked by exact symbolic ordered sums.')
print('PROVED: closed T, cubic square completion, and equal-gap invariant formula checked.')
print('PROVED: quartic upper bound has nonnegative remainder (a>=b>=0).')
# Exact rational matrix verification of both disconnected reductions.
H=s.eye(5)-s.ones(5)/5

def evaluate(L,Pi,lam):
 G=lam*H-L
 X1=2*(lam*s.trace(G)-s.trace(G*G))
 X2=s.Rational(10,3)*sum(Pi[i,j]*G[i,j]**2 for i in range(5) for j in range(5))
 X3=(1-lam)/3*(2*s.trace(G)-s.Rational(10,3)*sum(Pi[i,i]*G[i,i] for i in range(5)))
 Y=2*sum(-L[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for i in range(5) for j in range(i+1,5))
 return s.factor(X1+X2+X3-Y)
for n in [3,4]:
 for k in range(1,31):
  v=s.Matrix([k,1,-k-1] if n==3 else [k,1,2,-k-3]);v2=(v.T*v)[0]
  R=v*v.T/v2;q=sum(v[i]**4 for i in range(n))/v2**2;m=sum(v[i]**3 for i in range(n))**2/v2**3
  b0=s.Rational(1,10);la=(2+b0)/3
  L=s.zeros(5);Pi=s.zeros(5)
  Ln=la*(s.eye(n)-s.ones(n)/n)-b0*R
  Pn=s.eye(n)-s.ones(n)/n-R
  L[:n,:n]=Ln;Pi[:n,:n]=Pn
  if n==3:
   L[3:5,3:5]=la*(s.eye(2)-s.ones(2)/2);Pi[3:5,3:5]=s.eye(2)-s.ones(2)/2
   expect=(10+196*b0-314*b0*b0+648*b0*b0*m)/243
  else:
   expect=(20+(276*q-73)*b0+(161-708*q+432*m)*b0*b0)/162
  assert evaluate(L,Pi,la)==expect
print('PROVED: disconnected T formulas rechecked on 60 exact rational matrices (corroboration).')
p=s.symbols('p');P=(2+b)/(9*b)
assert s.factor(10+196*b-314*b*b+648*b*b*9*P*P*(s.Rational(1,2)-P)+2*(b-1)*(143*b*b-3*b-32)/b)==0
print('PROVED: the 3+2 component weight-bound substitution checked exactly.')
# Rational point l=32/5: a rigorous witness below the C5 quotient.
W=s.zeros(5)
for i,j,z0 in [(0,1,s.Rational(110,789)),(0,3,s.Rational(110,789)),(0,2,s.Rational(272,789)),(1,3,s.Rational(99,263))]:W[i,j]=W[j,i]=z0
L=s.diag(*[sum(W.row(i)) for i in range(5)])-W
la=s.Rational(704,789);aa=la;bb=s.Rational(178,263);G=la*H-L
Pi=H-((aa+bb)*G-G*G)/(aa*bb)
assert Pi*Pi==Pi and L*Pi==la*Pi
X1=2*(la*s.trace(G)-s.trace(G*G))
X2=s.Rational(10,3)*sum(Pi[i,j]*G[i,j]**2 for i in range(5) for j in range(5))
X3=(1-la)/3*(2*s.trace(G)-s.Rational(10,3)*sum(Pi[i,i]*G[i,i] for i in range(5)))
assert evaluate(L,Pi,la)/(X1+X2+X3)==s.Rational(55411,2732767)<s.Rational(1,40)
print('PROVED: rational l=32/5 graph has quotient 55411/2732767 < 1/40.')

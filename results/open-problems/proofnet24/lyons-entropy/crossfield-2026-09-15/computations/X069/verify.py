import sympy as s
import json
from pathlib import Path
r,q,z,w,X,Y,R,S,D,k=s.symbols('r q z w X Y R S D k',positive=True)
a=1-r*r;b=1-q*q;c=1-r*r*q*q
U=s.Matrix([[2*(2*c-b)/(a*c),2/c-2*k],[2/c-2*k,2*(2*c-a)/(b*c)]])
T=s.Matrix([[R+q*D,S-q*k],[R-r*k,S+r*D]])
V=s.Matrix([[4*(1+r*R+r*q*D),2*(q*R+r*S-D-r*q*k)],[2*(q*R+r*S-D-r*q*k),4*(1+q*S+r*q*D)]])
x1,x2,y1,y2=s.symbols('x1 x2 y1 y2',real=True)
x=s.Matrix([x1,x2]);y=s.Matrix([y1,y2]);v=x.col_join(y)
Q=U.row_join(-2*T).col_join((-2*T.T).row_join(V))
checks=0

def check(expr):
 global checks
 assert s.factor(expr)==0, expr
 checks+=1
check((v.T*Q*v)[0]-((T.T*x-2*y).T*(T.T*x-2*y))[0]-(x.T*(U-T*T.T)*x)[0]-(y.T*(V-4*s.eye(2))*y)[0])
for n in range(1,51):
 check(s.Rational(1,2*n+1)-s.Rational(1,2*n)+s.Rational(1,2*n*(2*n+1)))
 check(s.integrate(s.Symbol('h')**(2*n-1)*(1-s.Symbol('h')),(s.Symbol('h'),0,1))-s.Rational(1,2*n*(2*n+1)))
# Generic rotation identities, retaining independent formal logarithms.
W=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
t,d,l,m=s.symbols('t d l m',real=True)
rot=(W*T.T*W).subs({R:(t+d)/2,S:(t-d)/2,D:(l-m)/2,k:(l+m)/2})
B=s.Matrix([[t-(r+q)*m/2,(r-q)*m/2],[d-(r-q)*l/2,(r+q)*l/2]])
for e in rot-B:check(e)
# Verify rational hyperbolic identities through independent r,q.
zform=(1+r*q)/s.sqrt(a*b);wform=(1-r*q)/s.sqrt(a*b)
st=(r+q)/s.sqrt(a*b);sd=(r-q)/s.sqrt(a*b)
Ur=W*U*W
expected=s.Matrix([[zform*wform+2+zform/wform+wform/zform-1/(zform*wform)-2*k,st*sd*(1-1/(zform*wform))],[st*sd*(1-1/(zform*wform)),zform*wform-1/(zform*wform)+2*k]])
for e in Ur-expected:check(e)
# Balanced identity, with formal log and inverse hyperbolic variable.
L,A=s.symbols('L A',real=True)
h=(W*(U-T*T.T)*W).subs({q:r,R:A/2,S:A/2,D:L/2,k:L/2})
zbal=(1+r*r)/(1-r*r)
expect=s.diag(2*zbal+2-L-A*A,zbal-1/zbal+L-r*r*L*L)
for e in h-expect:check(e)
check(4-X/2+X*X/12-s.Rational(13,4)-(X-3)**2/12)
check(z-1/z-((z-1)/(z+1))*(z-1)**2/z-4*(z-1)/(z+1))
# Integral tails and bracket are exact scalar algebra.
check(X+Y-X*Y-(1-(1-X)*(1-Y)))
# Rational instances of the sharp bracket bounds.
for xx in [s.Rational(0),s.Rational(1,7),s.Rational(4,5),s.Rational(99,100)]:
 for yy in [s.Rational(0),s.Rational(2,9),s.Rational(7,8),s.Rational(999,1000)]:
  for n in [1,2,3,11]:
   value=xx**n+yy**n-(xx*yy)**n
   assert 0<=value<=1
   checks+=1
# Essential deterministic numerical check of the reduced identity only.
import numpy as np
from probe import Q as numeric_Q
maxerr=0.0
for rr,ss in [(0.,0.),(.2,.05),(.5,.5),(.91,.23),(.98,.97),(.1,.9)]:
 qq=numeric_Q(rr,ss); TT=-qq[:2,2:]/2
 tv=np.arctanh(rr)+np.arctanh(ss);dv=np.arctanh(rr)-np.arctanh(ss)
 zz=np.cosh(tv);ww=np.cosh(dv);ll=np.log(zz);mm=np.log(ww)
 al=np.sinh(tv)/(zz+ww);be=np.sinh(dv)/(zz+ww)
 BB=np.array([[tv-al*mm,be*mm],[dv-be*ll,al*ll]])
 UU=np.array([[zz*ww+2+zz/ww+ww/zz-1/(zz*ww)-ll-mm,np.sinh(tv)*np.sinh(dv)*(1-1/(zz*ww))],[np.sinh(tv)*np.sinh(dv)*(1-1/(zz*ww)),zz*ww-1/(zz*ww)+ll+mm]])
 WW=np.array([[1,1],[1,-1]])/np.sqrt(2)
 err=np.max(np.abs(WW@(qq[:2,:2]-TT@TT.T)@WW-(UU-BB.T@BB)))
 maxerr=max(maxerr,float(err))
 assert err<1e-9
out={'status':'PASS','exact_assertions':checks,'numerical_reduced_identity_max_error':maxerr,'unrestricted_U_ge_TT':'UNPROVED','three_site_six_mode_comparison':'UNPROVED'}
Path('computations/X069/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

"""Exact determinant check of X042's fixed flag and the entire phase polynomial."""
import itertools, json
from pathlib import Path
import sympy as S
import mpmath as mp

x=S.symbols('x', real=True)
eps=S.Rational(1,65536)
a=S.Rational(1,25)
b=S.Integer(0)
v=S.Matrix([1,1,1])/S.sqrt(3)
V0=S.Matrix([[1/S.sqrt(2),1/S.sqrt(6)],[-1/S.sqrt(2),1/S.sqrt(6)],[0,-2/S.sqrt(6)]])
V=S.zeros(4,2);V[1:4,:]=V0
w=S.Matrix([S.sqrt(1-eps),0,0,0])-S.sqrt(eps)*S.Matrix([0,*v])
W=w.col_join(S.Matrix([1]))/S.sqrt(2)
Vhat=V.col_join(S.zeros(1,2))
M=S.Matrix([[S.Rational(1,2)+a,b+S.I*x],[b-S.I*x,S.Rational(1,2)-a]])
K=w*w.T/2+V*M*V.T
Q=W*W.T+Vhat*M*Vhat.T

def zero(z):
 return S.simplify(S.expand(z))==0

def atom(K, subset):
 n=K.rows;cols=[]; eye=S.eye(n)
 for i in range(n):cols.append(K[:,i] if i in subset else eye[:,i]-K[:,i])
 return S.simplify(S.Matrix.hstack(*cols).det(method='domain-ge'))

def law(K):
 return {T:atom(K,T) for k in range(K.rows+1) for T in itertools.combinations(range(K.rows),k)}

checks=0
def check(test):
 global checks
 assert test
 checks+=1

check(V0.T*V0==S.eye(2));check(V0.T*v==S.zeros(2,1))
check(zero((W.T*W)[0]-1));check(W.T*Vhat==S.zeros(1,2))
check(Q[:4,:4]==K)
p=law(K);q=law(Q)
d=S.Rational(1,4)-a*a-x*x;c=S.Rational(1,2)-d
si=[S.simplify(S.Rational(3,2)*(V0*S.re(M)*V0.T)[i,i]-S.Rational(1,2)) for i in range(3)]
A=[S.Rational(2,3)*(c+s) for s in si]
Ap=[S.Rational(2,3)*(c-s) for s in si]
B=d/3
p0={():d,(0,1,2):S.Integer(0)}
p1={():S.Integer(0),(0,1,2):d}
for i in range(3):
 p0[(i,)]=A[i];p1[(i,)]=B
 T=tuple(j for j in range(3) if j!=i)
 p0[T]=B;p1[T]=Ap[i]
check(zero(sum(p.values())-1));check(zero(sum(q.values())-1))
check(zero(sum(p0.values())-1));check(zero(sum(p1.values())-1))
for T,prob in q.items():
 physical=tuple(i for i in T if i<4)
 Y=tuple(i-1 for i in physical if i>0)
 if 4 in T:
  expected=S.Integer(0) if 0 in T else p0[Y]/2
 elif 0 in T:
  expected=(1-eps)*p0[Y]/2
 else:
  expected=eps*p1[Y]/2
 check(zero(prob-expected))
for T,prob in p.items():
 check(zero(prob-q[T]-q[tuple(sorted((*T,4)))]))
for t in [S.Rational(-1,10),S.Integer(0),S.Rational(1,10)]:
 check(all(S.simplify(z.subs(x,t)).is_nonnegative is True for z in p.values()))
 check(sum(not zero(z.subs(x,t)) for z in p.values())==15)
Mlo=M.subs(x,-S.Rational(1,10));Mhi=M.subs(x,S.Rational(1,10))
check(Mlo*Mhi-Mhi*Mlo!=S.zeros(2))

# Independent exact differentiation of the homogeneous entropy perspective.
D=S.symbols('D', positive=True); ss,ee=S.symbols('s e', real=True, positive=True)
AA=S.Rational(2,3)*(S.Rational(1,2)-D+ss);BB=D/3
AAp=S.Rational(2,3)*(S.Rational(1,2)-D-ss)
phi=lambda y,z:(y+z)*S.log(y+z)-y*S.log(y)-z*S.log(z)
first=phi(AA,ee*BB);second=phi(BB,ee*AAp)
check(zero(S.diff(first,D,2)+ee*(1+2*ss)**2/(81*AA*BB*(AA+ee*BB))))
check(zero(S.diff(second,D,2)+ee*(1-2*ss)**2/(81*BB*AAp*(BB+ee*AAp))))
check(S.Rational(3,2)*S.Rational(121,100)*(S.Rational(125,12)+S.Rational(125,6))==S.Rational(1815,32))
check(S.Rational(19,6)-S.Rational(1815,8)/100==S.Rational(431,480))
check(S.Rational(4,3)**3*S.Rational(24,25)**2>1)

mp.mp.dps=60
em=mp.mpf(1)/65536
sm=[mp.mpf(str(S.N(s,65))) for s in si]
am=mp.mpf(1)/25
phim=lambda y,z:(y+z)*mp.log(y+z)-y*mp.log(y)-z*mp.log(z)
def cm(t):
 dd=mp.mpf(1)/4-am*am-t*t;cc=mp.mpf(1)/2-dd
 return sum(phim(2*(cc+s)/3,em*dd/3)+phim(dd/3,em*2*(cc-s)/3) for s in sm)/2
values={str(t):mp.nstr(mp.diff(cm,t,2),30) for t in [-mp.mpf('0.1'),mp.mpf(0),mp.mpf('0.1')]}
result={"status":"PASS","exact_assertions":checks,"epsilon":str(eps),"a":str(a),"b":str(b),"conditional_curvature_decimal_checks":values,"proved_curvature_lower_bound":str(S.Rational(431,480)*eps),"notes":"Determinant identities checked symbolically for the entire phase variable; decimal curvatures supplement, and do not prove, the analytic interval bound."}
Path(__file__).with_name('verified_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

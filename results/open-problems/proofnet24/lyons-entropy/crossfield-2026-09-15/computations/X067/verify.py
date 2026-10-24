"""Exact checks of the X067 conditional transport identity and log witness."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=0
def check(value):
    global checks
    assert value
    checks+=1

K=s.Matrix([[s.Rational(1,5),s.Rational(1,10),(1+s.I)/20],
            [s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],
            [(1-s.I)/20,s.Rational(1,10),s.Rational(4,5)]])
a=K[0,0]; b=1-a; q=a*b; v=K[1:,0]; C=K[1:,1:]; U=v*v.conjugate().T
J=[C+U/b,C-U/a]
for mat in [K,s.eye(3)-K]:
    for i in range(1,4): check(s.det(mat[:i,:i])>0)

def atoms(M):
    n=M.rows
    return [s.factor((-1)**(n-mask.bit_count())*s.det(M-s.diag(*[
        0 if mask>>i&1 else 1 for i in range(n)]))) for mask in range(2**n)]

def jets(M,E):
    t=s.Symbol('t',real=True)
    p=atoms(M+t*E)
    return [[s.simplify(s.diff(x,t,r).subs(t,0)) for x in p] for r in range(3)]

p=atoms(K)
pc=[atoms(j) for j in J]
check(p==[s.Rational(x,2000) for x in [102,38,208,52,518,142,772,168]])
for bit in [0,1]:
    pi=[b,a][bit]
    for m in range(4):check(pc[bit][m]==p[2*m+bit]/pi)

# A nontrivial exact rational-complex moving-pivot velocity.
d=s.Rational(2,7); z=(2+3*s.I)/11; x=s.re(z)
B=s.Matrix([[s.Rational(3,13),(1+2*s.I)/17],[(1-2*s.I)/17,-s.Rational(4,19)]])
A=s.zeros(3);A[0,0]=d;A[1:,0]=z*v;A[0,1:]=s.conjugate(z)*v.conjugate().T;A[1:,1:]=B
E=[B+(2*x/b+d/b**2)*U,B+(-2*x/a+d/a**2)*U]
t=s.Symbol('t',real=True)
Kt=K+t*A;at=a+t*d;vt=(1+t*z)*v;Ct=C+t*B
Jt=[Ct+vt*vt.conjugate().T/(1-at),Ct-vt*vt.conjugate().T/at]
C2=[2/b*abs(z+d/b)**2*U,-2/a*abs(z-d/a)**2*U]
for bit in [0,1]:
    check(s.simplify(Jt[bit].diff(t).subs(t,0)-E[bit])==s.zeros(2))
    check(s.simplify(Jt[bit].diff(t,2).subs(t,0)-C2[bit])==s.zeros(2))
    pjt=atoms(Jt[bit]); pj=jets(J[bit],E[bit]); pu=jets(J[bit],C2[bit])
    for m in range(4):
        check(s.simplify(pjt[m].diff(t,2).subs(t,0)-pj[2][m]-pu[1][m])==0)

# Keep all joint logarithms formal: equality is coefficientwise exact.
logs=s.symbols('l0:8',real=True);la,lb=s.symbols('la lb',real=True)
clogs=[[logs[2*m+bit]-[lb,la][bit] for m in range(4)] for bit in [0,1]]
def grad(M,E,ls):
    pp,dp,ddp=jets(M,E)
    return -sum(dp[i]*ls[i] for i in range(len(pp)))
def curv(M,E,ls):
    pp,dp,ddp=jets(M,E)
    check(sum(dp)==0);check(sum(ddp)==0)
    return sum(dp[i]**2/pp[i]+ddp[i]*ls[i] for i in range(len(pp)))
LU=grad(J[1],U,clogs[1])-grad(J[0],U,clogs[0])
LB=grad(J[1],B,clogs[1])-grad(J[0],B,clogs[0])
direct=curv(K,A,logs)
rhs=d*d/q+a*curv(J[1],E[1],clogs[1])+b*curv(J[0],E[0],clogs[0])+2*abs(z)**2*LU-2*d*LB
check(s.expand(direct-rhs)==0)
check(s.expand(LU-q*sum((pc[0][m]-pc[1][m])*(clogs[0][m]-clogs[1][m]) for m in range(4)))==0)

# The full moving-pivot witness, with formal independent face logarithms.
l0,l1,c2,c3=s.symbols('l0 l1 c2 c3',real=True)
tau=l1-l0; kap=l1/a+l0/b; m0=b*l0+a*l1
ell1=c3+s.Rational(31,40)*l1-s.Rational(129,160)*l0
ell2=c2+s.Rational(11,20)*l1-s.Rational(49,80)*l0
Lmat=s.diag(c3,c2)+l1*J[1].adjugate()-l0*J[0].adjugate()
check(s.expand(Lmat[0,0]-ell1)==0);check(s.expand(Lmat[1,1]-ell2)==0)
Bw=s.diag(ell2,-ell1)
check(s.expand(s.trace(Lmat*Bw))==0)
Aw=s.zeros(3);Aw[0,0]=-100;Aw[1:,0]=v;Aw[0,1:]=v.conjugate().T;Aw[1:,1:]=Bw
M=s.diag(l0,c2,c3)+tau*K
r=-ell1/100+ell2/200
LUw=ell1/100+ell2/200-tau/1000+kap/10000
frozen=-m0*ell1*ell2-LUw+(-100*kap-2*tau)*r
check(s.expand(s.trace(M*Aw.adjugate())-frozen)==0)
check(s.expand(s.det(Aw)-(100*ell1*ell2-r))==0)
check(s.expand(s.trace(Lmat*U)-LUw)==0)

# Elementary rational intervals for every logarithm used by the witness.
class I:
    def __init__(self,lo,hi=None):self.lo=F(lo);self.hi=F(lo if hi is None else hi)
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-o if isinstance(o,I) else self+I(-o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o)
        assert not o.lo<=0<=o.hi
        return self*I(1/o.hi,1/o.lo)

def log_interval(r,n=16):
    r=F(r);assert r>=1
    w=(r-1)/(r+1)
    lo=2*sum((w**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*w**(2*n+1)/(F(2*n+1)*(1-w*w))
    return I(lo,lo+tail)

L0=log_interval(F(13468,9843));L1=log_interval(F(923,798))
C2=log_interval(F(4921,3621));C3=log_interval(F(76,51))
T=L1-L0;Kap=5*L1+F(5,4)*L0;M0=F(4,5)*L0+F(1,5)*L1
Ell1=C3+F(31,40)*L1-F(129,160)*L0
Ell2=C2+F(11,20)*L1-F(49,80)*L0
R=-Ell1/100+Ell2/200
Luw=Ell1/100+Ell2/200-T/1000+Kap/10000
Frozen=-M0*Ell1*Ell2-Luw+(-100*Kap-2*T)*R
Det=100*Ell1*Ell2-R
check(Ell1.lo>F(2588,10000));check(Ell1.hi<F(2590,10000))
check(Ell2.lo>F(1947,10000));check(Ell2.hi<F(1948,10000))
check(R.hi<0);check(Luw.lo>0)
check(Frozen.lo>F(4,25));check(Det.lo>5)
# Mixed diagonal signs and positive determinant certify inertia (1,2).
check(Ell2.lo>0);check((-Ell1).hi<0)
check((100*Ell1-F(1,200)).lo>25) # A_{13} principal determinant >25.

# A second witness: even the conditional secant is indefinite.
Ks=s.Matrix([[s.Rational(1,2),s.Rational(1,10),0],
             [s.Rational(1,10),s.Rational(11,50),s.Rational(1,10)],
             [0,s.Rational(1,10),s.Rational(4,5)]])
for mat in [Ks,s.eye(3)-Ks]:
    for i in range(1,4):check(s.det(mat[:i,:i])>0)
cs2,cs3=s.symbols('cs2 cs3',real=True)
ts=l1-l0;ks=2*(l0+l1);ms=(l0+l1)/2
g1=cs3+s.Rational(4,5)*ts
g2=cs2+s.Rational(1,5)*l1-s.Rational(6,25)*l0
hs=-ts/10
Gs=s.Matrix([[g1,hs],[hs,g2]])
Bs=s.Matrix([[-g2+2*hs,-g1],[-g1,g1]])
As=s.zeros(3);As[0,0]=100;As[0,1]=As[1,0]=s.Rational(1,10);As[1:,1:]=Bs
Ms=s.diag(l0,cs2,cs3)+ts*Ks
vs=Ks[1:,0];Us=vs*vs.T;Cs=Ks[1:,1:]
Js=[Cs+2*Us,Cs-2*Us];pcs=[atoms(j) for j in Js]
check(pcs[0]==[s.Rational(x,500) for x in [71,29,309,91]])
check(pcs[1]==[s.Rational(x,20) for x in [3,1,13,3]])
check(s.simplify(Gs-(Ms[1:,1:].adjugate()-ks*Us.adjugate()))==s.zeros(2))
check(s.expand(s.trace(Gs*Bs))==0)
fs=ms*s.det(Bs)-g1/100+(100*ks-2*ts)*g1/100
check(s.expand(s.trace(Ms*As.adjugate())-fs)==0)
check(s.expand(s.det(As)-(100*s.det(Bs)-g1/100))==0)
check(s.expand(s.det(Gs)-(s.det(Ms[1:,1:])-ks*g1/100))==0)

S0=log_interval(F(8961,6461));S1=log_interval(F(13,9))
S2=log_interval(F(927,923));S3=log_interval(F(87,71))
Ts=S1-S0;Ks0=2*(S0+S1);Ms0=(S0+S1)/2
G1=S3+F(4,5)*Ts;G2=S2+F(1,5)*S1-F(6,25)*S0;Hs=-Ts/10
B11=-G2+2*Hs;DetB=B11*G1-G1*G1
DetGs=G1*G2-Hs*Hs
Fs=Ms0*DetB-G1/100+(100*Ks0-2*Ts)*G1/100
DetAs=100*DetB-G1/100
check(DetGs.hi<-F(1,10000));check(B11.hi<0);check(G1.lo>0)
check(DetAs.hi<-5);check(Fs.lo>F(3,10))

out={"status":"PASS","exact_assertions":checks,
     "witness":{"ell1_interval":[float(Ell1.lo),float(Ell1.hi)],
                "ell2_interval":[float(Ell2.lo),float(Ell2.hi)],
                "det_A_rational_lower_bound":5,
                "tr_M_adj_A_rational_lower_bound":"4/25",
                "tr_M_adj_A_interval":[float(Frozen.lo),float(Frozen.hi)],
                "curvature_rational_lower_bound":62500},
     "indefinite_secant_witness":{
         "det_G_rational_upper_bound":"-1/10000",
         "det_A_rational_upper_bound":-5,
         "tr_M_adj_A_rational_lower_bound":"3/10",
         "tr_M_adj_A_interval":[float(Fs.lo),float(Fs.hi)],
         "curvature_rational_lower_bound":40000},
     "note":"All signs use rational series bounds, not the displayed decimals."}
(HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

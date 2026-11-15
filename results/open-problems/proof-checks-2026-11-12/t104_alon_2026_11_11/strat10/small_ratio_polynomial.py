"""PROVED: homogeneous polynomial lower bound on a small-ratio strip."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from fractions import Fraction as F

def construct(rho):
    rho=F(rho);rho=QQ(rho.numerator,rho.denominator)
    rr,*gen=ring('z0,z1,z2,z3,x0,x1,x2',QQ);z,x=gen[:4],gen[4:]
    U=[sum(((5-j)if i<j else -j)*z[j-1]for j in range(1,5))for i in range(5)]
    span=U[0]-U[4]
    W=[sum((U[4]-U[j+1])*x[j]for j in range(3))]+[span*x[j]for j in range(3)]+[sum((U[j+1]-U[0])*x[j]for j in range(3))]
    t=sum(ui**2 for ui in U);n=sum(wi**2 for wi in W)
    A=sum(ui**4 for ui in U);B=sum(wi**4 for wi in W);C=sum(ui**2*wi**2 for ui,wi in zip(U,W))
    d=sum(ui**3 for ui in U);e=sum(ui**2*wi for ui,wi in zip(U,W));f=sum(ui*wi**2 for ui,wi in zip(U,W));h=sum(wi**3 for wi in W)
    D0=-20*U[0]*U[4]-t;kk=7*t-5*(U[0]+U[4])**2
    Lu=(11*(A*n+t*C)-2*t*t*n)/8
    Lw=(11*(t*B+C*n)-2*t*n*n)/8
    P=QQ(83,64)*t**3*n**2-QQ(75,16)*A*t*n*n-QQ(59,16)*C*t*t*n+3*d*d*n*n+e*e*t*n+2*d*f*t*n
    Q=QQ(5,16)*(A*t*n*n+B*t**3)-QQ(11,8)*C*t*t*n-QQ(33,160)*t**3*n*n+4*e*e*t*n+4*f*f*t*t+2*d*f*t*n+2*e*h*t*t
    R=QQ(83,64)*t**3*n*n-QQ(75,16)*B*t**3-QQ(193,48)*C*t*t*n
    p0=QQ(9,80)*D0**2*t*n*n+2*D0*Lu*n+4*P
    p1=-QQ(9,40)*D0*kk*t*n*n+2*(D0*t*Lw-kk*Lu*n)+4*Q
    p2=QQ(9,80)*kk**2*t*n*n-2*kk*t*Lw+4*R
    return rr,(p0,p0+rho*p1/2,p0+rho*p1+rho*rho*p2)

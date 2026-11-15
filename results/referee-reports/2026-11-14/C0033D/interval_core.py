"""Exact atom polynomials and outward interval Hessian/criterion certificates.

The determinant polynomials and LDL scheme follow C0033B/interval3.py and
C0033C/interval_audit.py; the probability-coordinate solve is new here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from fractions import Fraction
import sympy as sp
import mpmath as mp
iv=mp.iv
x=sp.symbols('x0:9')
a,b,c,xr,xi,yr,yi,zr,zi=x
expr=[]
for s in range(8):
    u,v,w=[x[i]-(0 if s>>i&1 else 1) for i in range(3)]
    det=u*v*w-u*(zr*zr+zi*zi)-v*(yr*yr+yi*yi)-w*(xr*xr+xi*xi)+2*((xr*zr-xi*zi)*yr+(xr*zi+xi*zr)*yi)
    expr.append(sp.expand((-1)**(3-s.bit_count())*det))
poly=sp.lambdify(x,expr,'math')
grad=sp.lambdify(x,[[sp.diff(p,z) for z in x] for p in expr],'math')
hess=sp.lambdify(x,[[[sp.diff(p,z,w) for w in x] for z in x] for p in expr],'math')

def endpoint(t):
    sign,man,e,_=t
    return Fraction((-1)**sign*man)*Fraction(2)**e

def bounds(z,digits=35):
    scale=10**digits;lo=endpoint(z._mpi_[0])*scale;hi=endpoint(z._mpi_[1])*scale
    return [str(Fraction(lo.numerator//lo.denominator,scale)),str(Fraction(-((-hi.numerator)//hi.denominator),scale))]

def pos(z):return z._mpi_[0][0]==0 and z._mpi_[0][1]!=0
def neg(z):return z._mpi_[1][0]==1 and z._mpi_[1][1]!=0
def rat(s):
    q=Fraction(s);return iv.mpf(q.numerator)/q.denominator
def interval(lo,hi):
    l=rat(lo);h=rat(hi)
    return iv.mpf([l.a,h.b])

def ldl(m):
    n=len(m);l=[[iv.mpf(int(i==j)) for j in range(n)] for i in range(n)];d=[]
    for i in range(n):
        pivot=m[i][i]-sum(l[i][k]**2*d[k] for k in range(i))
        if not pos(pivot):raise ArithmeticError(('LDL pivot',i,bounds(pivot)))
        d.append(pivot)
        for j in range(i+1,n):l[j][i]=(m[j][i]-sum(l[j][k]*l[i][k]*d[k] for k in range(i)))/pivot
    return l,d

def solve(l,d,z):
    n=len(z);v=[]
    for i in range(n):v.append(z[i]-sum(l[i][j]*v[j] for j in range(i)))
    v=[v[i]/d[i] for i in range(n)];out=[iv.mpf(0) for _ in range(n)]
    for i in reversed(range(n)):out[i]=v[i]-sum(l[j][i]*out[j] for j in range(i+1,n))
    return out

def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def inv3(a):
    d=det3(a).real
    if not pos(d):raise ArithmeticError('det R not certified positive')
    ans=[]
    for i in range(3):
        row=[]
        for j in range(3):
            ii=[k for k in range(3) if k!=j];jj=[k for k in range(3) if k!=i]
            row.append((-1)**(i+j)*(a[ii[0]][jj[0]]*a[ii[1]][jj[1]]-a[ii[0]][jj[1]]*a[ii[1]][jj[0]])/d)
        ans.append(row)
    return ans,d

def matrix(xx):
    q=[[iv.mpc(0) for j in range(3)] for i in range(3)]
    for i in range(3):q[i][i]=iv.mpc(xx[i])
    for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):
        q[i][j]=iv.mpc(xx[3+2*k],xx[4+2*k]);q[j][i]=iv.mpc(q[i][j].real,-q[i][j].imag)
    return q

def R_matrix(q,p):
    ell=[iv.log(p[2]*p[4]/(p[0]*p[6])),iv.log(p[1]*p[4]/(p[0]*p[5])),iv.log(p[1]*p[2]/(p[0]*p[3]))]
    gamma=iv.log(p[7]*p[1]*p[2]*p[4]/(p[0]*p[3]*p[5]*p[6]))
    return [[iv.mpc(ell[i] if i==j else 0)-gamma*q[i][j] for j in range(3)] for i in range(3)],gamma

def full_certificate(xx,criterion_too=True):
    p=list(map(iv.mpf,poly(*xx)));g=grad(*xx);hh=hess(*xx)
    if not all(map(pos,p)):raise ArithmeticError('atom positivity')
    f=[[sum(iv.mpf(g[s][i])*iv.mpf(g[s][j])/p[s] for s in range(8)) for j in range(9)] for i in range(9)]
    nh=[[f[i][j]+sum(iv.log(p[s])*iv.mpf(hh[s][i][j]) for s in range(8)) for j in range(9)] for i in range(9)]
    _,piv=ldl(nh)
    out=dict(atoms=[bounds(z) for z in p],negative_hessian_pivots=[bounds(z) for z in piv])
    if not criterion_too:return out
    q=matrix(xx);R,gamma=R_matrix(q,p);ri,d=inv3(R)
    rm=[R[0][0].real,(R[0][0]*R[1][1]-R[0][1]*R[1][0]).real,d]
    if not all(map(pos,rm)):raise ArithmeticError('R leading minors')
    bas=[]
    for i in range(9):
        e=[[iv.mpc(0) for _ in range(3)] for _ in range(3)]
        if i<3:e[i][i]=iv.mpc(1)
        else:
            ii,jj=((0,1),(0,2),(1,2))[(i-3)//2]
            e[ii][jj]=iv.mpc(1,0) if (i-3)%2==0 else iv.mpc(0,1)
            e[jj][ii]=iv.mpc(e[ii][jj].real,-e[ii][jj].imag)
        bas.append(e)
    rb=[matmul(ri,e) for e in bas];z=[tr(e).real for e in rb]
    J=[[f[i][j]+d*tr(matmul(rb[i],rb[j])).real for j in range(9)] for i in range(9)]
    lj,dj=ldl(J);v=solve(lj,dj,z);theta=d*sum(z[i]*v[i] for i in range(9))
    if not pos(1-theta):raise ArithmeticError('margin not certified positive')
    # Seven nonempty atom gradients, as Hermitian matrices C_s.
    C=[]
    for s in range(1,8):
        e=[[iv.mpc(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):e[i][i]=iv.mpc(g[s][i])
        for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):
            e[i][j]=iv.mpc(g[s][3+2*k]/2,g[s][4+2*k]/2);e[j][i]=iv.mpc(e[i][j].real,-e[i][j].imag)
        C.append(e)
    rc=[matmul(R,c) for c in C];bb=[tr(e).real for e in rc]
    M=[[tr(matmul(rc[i],rc[j])).real+d*((p[i+1] if i==j else 0)-p[i+1]*p[j+1]) for j in range(7)] for i in range(7)]
    lm,dm=ldl(M);vv=solve(lm,dm,bb);theta7=3-sum(bb[i]*vv[i] for i in range(7))
    if not pos(1-theta7):raise ArithmeticError('seven-variable margin')
    difference=theta-theta7
    if not endpoint(difference._mpi_[0])<=0<=endpoint(difference._mpi_[1]):
        raise ArithmeticError('independent criterion intervals do not overlap')
    out.update(R_leading_minors=[bounds(z) for z in rm],theta=bounds(theta),margin=bounds(1-theta),
               theta_seven=bounds(theta7),difference=bounds(difference),gamma=bounds(gamma))
    return out

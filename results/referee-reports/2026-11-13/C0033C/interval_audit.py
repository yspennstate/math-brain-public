"""Rational-input, outward-rounded audit of C0033B (17) and the full Hessian.

No binary matrix inverse enters the certificate. All atom polynomials and their
first two derivatives are exact integer polynomials; mpmath.iv rounds outwards.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,itertools,resource,time
from pathlib import Path
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp
iv=mp.iv;iv.dps=100
x=sp.symbols('x0:9');a,b,c,xr,xi,yr,yi,zr,zi=x
expr=[]
for s in range(8):
    d=[x[i]-(0 if s>>i&1 else 1) for i in range(3)]
    det=d[0]*d[1]*d[2]-d[0]*(zr*zr+zi*zi)-d[1]*(yr*yr+yi*yi)-d[2]*(xr*xr+xi*xi)+2*((xr*zr-xi*zi)*yr+(xr*zi+xi*zr)*yi)
    expr.append(sp.expand((-1)**(3-s.bit_count())*det))
poly=sp.lambdify(x,expr,'math')
grad=sp.lambdify(x,[[sp.diff(p,z) for z in x] for p in expr],'math')
hess=sp.lambdify(x,[[[sp.diff(p,z,w) for w in x] for z in x] for p in expr],'math')
def exact(t):
    sign,man,e,bc=t
    return Fraction((-1)**sign*man)*Fraction(2)**e

def bounds(z,digits=30):
    scale=10**digits;lo=exact(z._mpi_[0])*scale;hi=exact(z._mpi_[1])*scale
    return [str(Fraction(lo.numerator//lo.denominator,scale)),str(Fraction(-((-hi.numerator)//hi.denominator),scale))]

def pos(z):return z._mpi_[0][0]==0 and z._mpi_[0][1]!=0

def ldl(m):
    n=len(m);l=[[iv.mpf(int(i==j)) for j in range(n)] for i in range(n)];d=[]
    for i in range(n):
        pivot=m[i][i]-sum(l[i][k]**2*d[k] for k in range(i));assert pos(pivot),(i,pivot)
        d.append(pivot)
        for j in range(i+1,n):l[j][i]=(m[j][i]-sum(l[j][k]*l[i][k]*d[k] for k in range(i)))/pivot
    return l,d

def solve_ldl(l,d,z):
    n=len(z);v=[]
    for i in range(n):v.append(z[i]-sum(l[i][j]*v[j] for j in range(i)))
    v=[v[i]/d[i] for i in range(n)];out=[iv.mpf(0) for _ in range(n)]
    for i in reversed(range(n)):out[i]=v[i]-sum(l[j][i]*out[j] for j in range(i+1,n))
    return out

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def tr(a):return sum(a[i][i] for i in range(len(a)))
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def inv3(a):
    d=det3(a).real;assert pos(d)
    out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            ii=[k for k in range(3) if k!=j];jj=[k for k in range(3) if k!=i]
            row.append((-1)**(i+j)*(a[ii[0]][jj[0]]*a[ii[1]][jj[1]]-a[ii[0]][jj[1]]*a[ii[1]][jj[0]])/d)
        out.append(row)
    return out,d

def main():
    start=time.monotonic();q=np.load('data/scalar_witness.npz')['Q']
    coords=[q[i,i].real for i in range(3)]+[t for i,j in ((0,1),(0,2),(1,2)) for t in (q[i,j].real,q[i,j].imag)]
    # Exact rational rounding; resulting kernel is the object certified below.
    numer=[round(float(z)*10**12) for z in coords];den=10**12
    rat=[sp.Rational(z,den) for z in numer];xx=[iv.mpf(z)/den for z in numer]
    Path('data/scalar_witness_rational.json').write_text(json.dumps(dict(denominator=den,numerators=numer,coordinate_order=['q11','q22','q33','Re q12','Im q12','Re q13','Im q13','Re q23','Im q23']),indent=2)+'\n')
    qq=sp.Matrix([[rat[0],rat[3]+sp.I*rat[4],rat[5]+sp.I*rat[6]],[rat[3]-sp.I*rat[4],rat[1],rat[7]+sp.I*rat[8]],[rat[5]-sp.I*rat[6],rat[7]-sp.I*rat[8],rat[2]]])
    # Sylvester's criterion with exact rationals.
    principal={}
    for name,m in [('Q',qq),('I-Q',sp.eye(3)-qq)]:
        minors=[sp.factor(m[:k,:k].det()) for k in range(1,4)];assert all(z>0 for z in minors)
        principal[name]=list(map(str,minors))
    pp=list(map(iv.mpf,poly(*xx)));gg=grad(*xx);hh=hess(*xx);assert all(map(pos,pp))
    fisher=[[sum(iv.mpf(gg[s][i])*iv.mpf(gg[s][j])/pp[s] for s in range(8)) for j in range(9)] for i in range(9)]
    nh=[[fisher[i][j]+sum(iv.log(pp[s])*iv.mpf(hh[s][i][j]) for s in range(8)) for j in range(9)] for i in range(9)]
    _,piv=ldl(nh)
    ell=[iv.log(pp[2]*pp[4]/(pp[0]*pp[6])),iv.log(pp[1]*pp[4]/(pp[0]*pp[5])),iv.log(pp[1]*pp[2]/(pp[0]*pp[3]))]
    gamma=iv.log(pp[7]*pp[1]*pp[2]*pp[4]/(pp[0]*pp[3]*pp[5]*pp[6]))
    qiv=[[iv.mpc(0) for j in range(3)] for i in range(3)]
    for i in range(3):qiv[i][i]=iv.mpc(xx[i])
    for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):qiv[i][j]=iv.mpc(xx[3+2*k],xx[4+2*k]);qiv[j][i]=iv.mpc(qiv[i][j].real,-qiv[i][j].imag)
    r=[[iv.mpc(ell[i] if i==j else 0)-gamma*qiv[i][j] for j in range(3)] for i in range(3)]
    ri,d=inv3(r)
    # R>0: leading minors, all computed with outward rounding.
    rmin=[r[0][0].real,(r[0][0]*r[1][1]-r[0][1]*r[1][0]).real,d];assert all(map(pos,rmin))
    bas=[]
    for i in range(9):
        e=[[iv.mpc(0) for j in range(3)] for k in range(3)]
        if i<3:e[i][i]=iv.mpc(1)
        else:
            ii,jj=((0,1),(0,2),(1,2))[(i-3)//2];e[ii][jj]=(iv.mpc(1,0) if (i-3)%2==0 else iv.mpc(0,1));e[jj][ii]=iv.mpc(e[ii][jj].real,-e[ii][jj].imag)
        bas.append(e)
    rb=[matmul(ri,e) for e in bas]
    z=[tr(m).real for m in rb]
    jmat=[[fisher[i][j]+d*tr(matmul(rb[i],rb[j])).real for j in range(9)] for i in range(9)]
    lj,dj=ldl(jmat);sol=solve_ldl(lj,dj,z)
    ratio=d*sum(z[i]*sol[i] for i in range(9));assert pos(1-ratio)
    out=dict(precision_decimal=100,exact_leading_minors=principal,atoms=[bounds(z) for z in pp],R_leading_minors=[bounds(z) for z in rmin],negative_hessian_pivots=[bounds(z) for z in piv],criterion_17=bounds(ratio),criterion_gap=bounds(1-ratio),seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/interval_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

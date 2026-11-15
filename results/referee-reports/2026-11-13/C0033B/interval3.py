"""Outward-rounded interval LDL certificate on a full Hermitian 3x3 box.

Uses mpmath.iv interval arithmetic and polynomial probability derivatives.
The box is only a local certificate, not a cover of all positive contractions.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sympy as sp,mpmath as mp,json
from fractions import Fraction
iv=mp.iv;iv.dps=60
x=sp.symbols('x0:9');a,b,c,xr,xi,yr,yi,zr,zi=x
expr=[]
for s in range(8):
 d=[x[i]-(0 if s>>i&1 else 1) for i in range(3)]
 p=d[0]*d[1]*d[2]-d[0]*(zr*zr+zi*zi)-d[1]*(yr*yr+yi*yi)-d[2]*(xr*xr+xi*xi)+2*((xr*zr-xi*zi)*yr+(xr*zi+xi*zr)*yi)
 expr.append(sp.expand((-1)**(3-s.bit_count())*p))
poly=sp.lambdify(x,expr,'math');grad=sp.lambdify(x,[[sp.diff(p,z) for z in x] for p in expr],'math');hess=sp.lambdify(x,[[[sp.diff(p,z,w) for w in x] for z in x] for p in expr],'math')
# Endpoints constructed in interval arithmetic from exact rational fractions.
center=[iv.mpf(2)/5,iv.mpf(1)/2,iv.mpf(3)/5,iv.mpf(1)/16,iv.mpf(0),iv.mpf(1)/20,iv.mpf(0),iv.mpf(1)/24,iv.mpf(1)/32]
eps=iv.mpf(1)/10**4
box=[iv.mpf([z.a-eps,z.b+eps]) for z in center]
p=list(map(iv.mpf,poly(*box)));g=grad(*box);hh=hess(*box)
def lower(z):return mp.mpf(z.a._mpi_[0])
def upper(z):return mp.mpf(z.b._mpi_[1])
def exact_mpf(t):
 sign,man,exponent,bc=t
 return Fraction((-1)**sign*man)*(Fraction(2)**exponent)
def pair(z):
 scale=10**20;lo=exact_mpf(z._mpi_[0])*scale;hi=exact_mpf(z._mpi_[1])*scale
 return [str(lo.numerator//lo.denominator)+'/100000000000000000000',str(-((-hi.numerator)//hi.denominator))+'/100000000000000000000']
def positive(z):return lower(z)>0
# Gershgorin verifies 0<Q<I for every element of this box.
off=[iv.sqrt(box[i]**2+box[i+1]**2) for i in (3,5,7)]
margins=[box[0]-off[0]-off[1],box[1]-off[0]-off[2],box[2]-off[1]-off[2],1-box[0]-off[0]-off[1],1-box[1]-off[0]-off[2],1-box[2]-off[1]-off[2]]
assert all(map(positive,margins));assert all(map(positive,p))
m=[[sum(iv.mpf(g[s][i])*iv.mpf(g[s][j])/p[s]+iv.log(p[s])*iv.mpf(hh[s][i][j]) for s in range(8)) for j in range(9)] for i in range(9)]
l=[[iv.mpf(0) for j in range(9)] for i in range(9)];d=[]
for i in range(9):
 pivot=m[i][i]-sum(l[i][k]**2*d[k] for k in range(i));assert positive(pivot),(i,pivot)
 d.append(pivot);l[i][i]=iv.mpf(1)
 for j in range(i+1,9):l[j][i]=(m[j][i]-sum(l[j][k]*l[i][k]*d[k] for k in range(i)))/pivot
out=dict(precision_decimal=60,radius='1/10000',coordinate_order=['q11','q22','q33','Re q12','Im q12','Re q13','Im q13','Re q23','Im q23'],center=['2/5','1/2','3/5','1/16','0','1/20','0','1/24','1/32'],box=[pair(z) for z in box],gershgorin_margins=[pair(z) for z in margins],atoms=[pair(z) for z in p],ldl_pivots=[pair(z) for z in d],result='positive definite negative entropy Hessian throughout the full nine-dimensional box')
Path('data/interval3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

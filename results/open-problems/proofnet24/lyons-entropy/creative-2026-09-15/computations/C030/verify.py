#!/usr/bin/env python3
"""Exact certificate for C030's new noisy Fourier coupling and dilation defect.

Standard library only. Field elements are a+b*sqrt(-3), with rational a,b.
No numerical optimization or unretained data is used.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

ZERO=(F(0),F(0)); ONE=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scale(x,c): return (x[0]*c,x[1]*c)
def div(x,y): return scale(mul(x,conj(y)),1/(y[0]**2+3*y[1]**2))
def det(M):
    n=len(M)
    if not n: return ONE
    M=[r[:] for r in M]; out=ONE
    for k in range(n):
        pivot=next((i for i in range(k,n) if M[i][k]!=ZERO),None)
        if pivot is None: return ZERO
        if pivot!=k: M[k],M[pivot]=M[pivot],M[k]; out=neg(out)
        d=M[k][k]; out=mul(out,d)
        for i in range(k+1,n):
            q=div(M[i][k],d)
            for j in range(k+1,n): M[i][j]=sub(M[i][j],mul(q,M[k][j]))
            M[i][k]=ZERO
    return out

N=6; FULL=(1<<N)-1
def elems(mask): return [i for i in range(N) if mask>>i&1]
def mask(items): return sum(1<<i for i in items)
def subsets(bits): return [m for m in range(1<<N) if m&~bits==0]
def atom_law(K):
    p=[]
    for S in range(1<<N):
        ids=elems(S); value=det([[K[i][j] for j in ids] for i in ids])
        assert value[1]==0
        p.append(value[0])
    # Boolean inclusion-exclusion, converting inclusion moments to atom masses.
    for i in range(N):
        for S in range(1<<N):
            if not S>>i&1: p[S]-=p[S|(1<<i)]
    assert sum(p)==1 and min(p)>=0
    return p

# All Fourier powers, zeta=(1+sqrt(-3))/2.
zeta=(F(1,2),F(1,2)); powers=[ONE]
for k in range(1,6): powers.append(mul(powers[-1],zeta))
assert mul(powers[-1],zeta)==ONE
def fourier_projector(cols):
    return [[scale(sum_field(powers[((i-j)*k)%6] for k in cols),F(1,6))
             for j in range(N)] for i in range(N)]
def sum_field(items):
    result=ZERO
    for x in items: result=add(result,x)
    return result
PW=fourier_projector([0,1]); B=fourier_projector([2]); C=fourier_projector([3])
d=[F(1,2)]+[F(3,4)]*5
s=[v*v for v in d]; a=[(1-v)/2 for v in s]
def kernel(lam,mu):
    return [[add((a[i],F(0)) if i==j else ZERO,
                 scale(add(PW[i][j],add(scale(B[i][j],lam),scale(C[i][j],mu))),d[i]*d[j]))
             for j in range(N)] for i in range(N)]

# C004's exact positive Fourier seed, reconstructed from its eight orbit rows.
orbits=[((0,1),(2,3),1),((0,1),(2,4),1),((0,1),(3,4),1),
        ((0,1),(2,5),1),((0,2),(3,5),7),((0,2),(1,3),1),
        ((0,2),(1,4),7),((0,3),(1,4),4)]
seed={}
for AA,BB,numerator in orbits:
    for sign in [-1,1]:
        for shift in range(6):
            A=mask((sign*j+shift)%6 for j in AA)
            Bmask=mask((sign*j+shift)%6 for j in BB)
            for key in [(A,Bmask),(Bmask,A)]:
                value=F(numerator,216)
                if key in seed: assert seed[key]==value
                seed[key]=value
assert len(seed)==90 and sum(seed.values())==1 and min(seed.values())==F(1,216)

# Push every seed diamond through a single shared monotone binary channel.
weights={}
for (S,Bmask),w in seed.items():
    J=FULL^(S|Bmask); i,j=elems(J)
    for A in subsets(FULL^J):
        value=w*s[i]*s[j]
        for k in elems(FULL^J):
            prob=a[k]+(s[k] if S>>k&1 else 0)
            value*=prob if A>>k&1 else 1-prob
        weights[A,J]=weights.get((A,J),F(0))+value
assert len(weights)==240
lower=F(2401,268435456)
assert min(weights.values())>=lower

laws={(lam,mu):atom_law(kernel(F(lam),F(mu))) for lam,mu in [(0,0),(1,0),(0,1),(1,1)]}
contrast=[laws[0,0][S]+laws[1,1][S]-laws[1,0][S]-laws[0,1][S] for S in range(64)]
represented=[F(0)]*64
for (S,J),w in weights.items():
    i,j=elems(J)
    represented[S]+=w; represented[S|J]+=w
    represented[S|(1<<i)]-=w; represented[S|(1<<j)]-=w
assert represented==contrast

# The added pair has a fixed exterior-square law, independent of the coupling.
pair_masses={}
for (S,J),w in weights.items(): pair_masses[J]=pair_masses.get(J,F(0))+w
for J,total in pair_masses.items():
    i,j=elems(J)
    expected=s[i]*s[j]*F(2*(1-powers[(j-i)%6][0]),36)
    assert total==expected
assert sum(weights.values())==F(33,128)
gram_diag=F(49,96); gram_cross=F(-5,96)
assert gram_diag**2-gram_cross**2==F(33,128)

# Rational outward bounds for logarithms. The atanh series has a geometric
# positive tail after scaling the input to [1,2], so every claimed sign is exact.
def core_log_bounds(x,terms=32):
    assert 1<=x<=2
    z=(x-1)/(x+1); partial=sum((2*z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    remainder=2*z**(2*terms+1)/F(2*terms+1)/(1-z*z)
    return partial,partial+remainder
LOG2=core_log_bounds(F(2))
def log_bounds(x):
    assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>2: x/=2; k+=1
    lo,hi=core_log_bounds(x)
    if k>=0: return lo+k*LOG2[0],hi+k*LOG2[1]
    return lo+k*LOG2[1],hi+k*LOG2[0]
def combine_log(coeff,x,bounds):
    lo,hi=log_bounds(x)
    if coeff<0: lo,hi=hi,lo
    return bounds[0]+coeff*lo,bounds[1]+coeff*hi

# New noisy family at lambda=1/3, mu=2/3, with slopes (+1,-1).
lam=F(1,3); mu=F(2,3)
p=[(1-lam)*(1-mu)*laws[0,0][S]+lam*(1-mu)*laws[1,0][S]
   +(1-lam)*mu*laws[0,1][S]+lam*mu*laws[1,1][S] for S in range(64)]
assert p==atom_law(kernel(lam,mu)) and min(p)>0
# Differentiate the four mixture coefficients with lambda'=1, mu'=-1.
dp=[(mu-lam)*laws[0,0][S]+(1+lam-mu)*laws[1,0][S]
    +(-1+lam-mu)*laws[0,1][S]+(mu-lam)*laws[1,1][S] for S in range(64)]
assert sum(dp)==0
fisher=sum((v*v/q for v,q in zip(dp,p)),F(0))
hessian=(-fisher,-fisher)
for b,q in zip(contrast,p): hessian=combine_log(2*b,q,hessian)
assert hessian[1]<0

# Exact conditional-entropy curvature of the canonical pure projection dilation.
def cond_bounds(t):
    lo,hi=log_bounds(1+1/(4*t*t))
    correction=2/(F(1,4)+t*t)
    return 4*lo-correction,4*hi-correction
c_quarter=cond_bounds(F(1,4)); c_third=cond_bounds(F(1,3))
assert c_quarter[0]>0 and c_third[1]<F(-7,13)
short_log5=sum((2*F(2,3)**(2*k+1)/F(2*k+1) for k in range(4)),F(0))
assert short_log5>F(8,5)
assert sum((F(5,4)**k/F(__import__('math').factorial(k)) for k in range(4)),F(0))>F(13,4)

# A second exact defect: opposite spectral slopes on two sites, then keep one.
# Conditional entropy equals all of the lifted entropy's varying part.
lo,hi=log_bounds(F(3,5))
mixed_defect=(F(-64,15)+4*lo,F(-64,15)+4*hi)
assert mixed_defect[1]<0

def outward_decimal(interval,digits=12):
    unit=10**digits
    lo=interval[0].numerator*unit//interval[0].denominator
    hi=-((-interval[1].numerator*unit)//interval[1].denominator)
    return [str(F(lo,unit)),str(F(hi,unit))]
result={
    'status':'PASS',
    'source_projection_diamonds':len(seed),
    'new_noisy_diamonds':len(weights),
    'exact_new_atom_contrast_equations':len(contrast),
    'new_coupling_mass':str(sum(weights.values())),
    'minimum_new_weight':str(min(weights.values())),
    'proved_common_weight_lower_bound':str(lower),
    'nonorthogonal_update_gram':{'diagonal':str(gram_diag),'off_diagonal':str(gram_cross)},
    'new_family_hessian_rational_outward_interval':outward_decimal(hessian),
    'canonical_defect_curvature_t_1_4':outward_decimal(c_quarter),
    'canonical_defect_curvature_t_1_3':outward_decimal(c_third),
    'log5_four_term_lower_bound':str(short_log5),
    'mixed_lift_defect_curvature_t_1_4':outward_decimal(mixed_defect)
}
out=Path(__file__).with_name('verification_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

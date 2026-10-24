#!/usr/bin/env python3
"""Check tensor and one-suspension behavior of the mask-56242 SMR witness.

Direct truth-table evaluation is used for the base and the twofold tensor.
The large-t table uses the proved activation recurrence and exact tensor
formulas; only logarithms are evaluated in floating point.
"""
from fractions import Fraction
from math import log2


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def caps(p):
    a = list(p)
    n = len(a).bit_length()-1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def xr(x, y):
    return 0.0 if x == 0 else float(x)*log2(float(y/x))


def T(a, b):
    return xr(a, a+b)+xr(b, a+b)


def restrict(v, i, bit):
    n = len(v).bit_length()-1
    out=[]
    for z in range(1 << (n-1)):
        lo=z & ((1 << i)-1)
        hi=z >> i
        out.append(v[lo | (bit << i) | (hi << (i+1))])
    return tuple(out)


def basic(v):
    h=fwht(v)
    p=[x*x for x in h]
    c=caps(p)
    U=sum(xr(x,y) for x,y in zip(p,c))
    I=sum(s.bit_count()*float(x) for s,x in enumerate(p))
    n=len(v).bit_length()-1
    B=0.0
    for i in range(n):
        bit=1 << i
        for s in range(len(p)):
            if not s & bit:
                B += T(p[s],p[s|bit])
    return U,I,B,h,p


def stats(v):
    U,I,B,h,p=basic(v)
    n=len(v).bit_length()-1
    G=n*U
    for i in range(n):
        G -= .5*basic(restrict(v,i,0))[0]
        G -= .5*basic(restrict(v,i,1))[0]
    return dict(U=U,I=I,B=B,G=G,M=G-B,h=h,p=p)


def activate(v):
    return tuple(v)+tuple(1 for _ in v)


def tensor(v,w):
    return tuple(a*b for b in w for a in v)


def R(m):
    # Formal one-bit child with spectrum (m^2,1-m^2); the activation
    # correction depends only on m, so this computes it exactly as a scalar.
    p=[m*m,1-m*m]
    Uq=sum(xr(x,y) for x,y in zip(p,caps(p)))
    pa=[(1+m)**2/4,(1-m*m)/4,(1-m)**2/4,(1-m*m)/4]
    Ua=sum(xr(x,y) for x,y in zip(pa,caps(pa)))
    return Ua-.5*Uq


def threshold(s,eta):
    return (s['M']+(1+eta)*s['U'])/s['I']


mask=56242
q=tuple(1 if mask&(1<<i) else -1 for i in range(16))
f=activate(q)
sf=stats(f)
m=float(sf['h'][0])
n=len(f).bit_length()-1
means=[]
for i in range(n):
    means.append((sum(restrict(f,i,0))/len(restrict(f,i,0)),
                  sum(restrict(f,i,1))/len(restrict(f,i,1))))
singleton=[float(sf['p'][1<<i]) for i in range(n)]


def tensor_activation_threshold(t,eta):
    mt=m**t
    dr=0.0
    corr=0.0
    for (mm,mp),pi in zip(means,singleton):
        mm*=m**(t-1); mp*=m**(t-1)
        dr += t*(R(mt)-.5*(R(mm)+R(mp)))
        pit=pi*m**(2*t-2)
        corr += t*(-.5*T(mt*mt,pit)
                   +.25*T((1+mt)**2,pit)+.25*T((1-mt)**2,pit))
    bz=(1-mt*mt)/2+.25*T((1+mt)**2,(1-mt)**2)
    a0=dr+(2+eta)*R(mt)-bz-corr
    j=(1-mt)/2
    nf=sf['M']+(1+eta)*sf['U']
    return (.5*t*nf+a0)/(.5*t*sf['I']+j), dr, corr, a0, j


eta=.25
cF=threshold(sf,eta)
print('status=PASS')
print(f'mask={mask}')
print('seed=fair_activation_of_mask_56242')
print(f'mean_F={m:.17g}')
print(f'I_F={sf["I"]:.17g}')
print(f'c_F_eta_1_4={cF:.15f}')

# Exact additivity check by direct twofold truth-table reconstruction.
f2=tensor(f,f)
sf2=stats(f2)
for key in ('U','I','B','G','M'):
    err=abs(sf2[key]-2*sf[key])
    assert err < 2e-12, (key,err)
print('direct_tensor_additivity_checks=5')
print('direct_tensor_max_error=' + format(max(abs(sf2[k]-2*sf[k]) for k in ('U','I','B','G','M')),'.3e'))

# Direct check of the recurrence at t=2.
af2=stats(activate(f2))
ct2_direct=threshold(af2,eta)
ct2_formula=tensor_activation_threshold(2,eta)[0]
assert abs(ct2_direct-ct2_formula) < 2e-12
print(f't2_direct_threshold={ct2_direct:.15f}')
print(f't2_formula_threshold={ct2_formula:.15f}')
print(f't2_formula_error={abs(ct2_direct-ct2_formula):.3e}')

for t in (1,2,3,4,8,16,32,64,128):
    ct,dr,corr,a0,j=tensor_activation_threshold(t,eta)
    print(f't={t} c_t={ct:.15f} excess={ct-cF:.15e} DR={dr:.6e} C={corr:.6e}')

limit=1+eta-cF/2
assert limit > 0
print(f'node_limit_at_cF={limit:.15f}')
print(f'asymptotic_t_times_excess={2*limit/sf["I"]:.15f}')
ct128=tensor_activation_threshold(128,eta)[0]
assert ct128 > cF
print('large_t_strict_excess=PASS')

for t in (2,3,4,5,6,8):
    c0=tensor_activation_threshold(t,0.0)[0]
    c1=tensor_activation_threshold(t,1.0)[0]
    f0=threshold(sf,0.0)
    f1=threshold(sf,1.0)
    print(f'affine_t={t} D0={c0-f0:.15e} D1={(c1-c0)-(f1-f0):.15e}')


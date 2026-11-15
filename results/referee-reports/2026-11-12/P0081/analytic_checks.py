"""Independent checks of the Yule representation and equilibrium algebra."""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
from scipy.special import zeta
from scipy.stats import norm
import mpmath as mp

mp.mp.dps = 40
print('zeta(2) =', mp.zeta(2))
print('zeta(4) =', mp.zeta(4))
print('C4 limiting Var((1+u)/2) = pi^2/32 - 1/4 =', mp.pi**2/32-mp.mpf(1)/4)
print('C4 moment-matched symmetric Beta b =', 1/(8*(mp.pi**2/32-mp.mpf(1)/4))-mp.mpf(1)/2)
R,T=8191,1000
log_delta=(math.log(2)+R*math.log(2*T)-math.lgamma(R+1))/math.log(10)
print(f'Line finite-volume failure bound per target at T=1000: log10(delta_8191)={log_delta:.2f}')
print('Triangle uniform-equilibrium tangent eigenvalue at alpha=11/10: 3*alpha/4-1 = -7/40 < 0')
def density_m4(s):
    if abs(s)<mp.mpf('1e-15'): return mp.mpf(1)/6-s*s/60
    return (s*mp.coth(s/2)-2)/(4*mp.sinh(s/2)**2)
norm_integral=2*mp.quad(density_m4,[0,1,5,20,mp.inf])
var_integral=mp.quad(lambda s:mp.tanh(s/4)**2*density_m4(s)/2,[0,1,5,20,mp.inf])
print('Independent quadrature of C4 charge density: mass =',norm_integral,'Var(p) =',var_integral)
assert abs(var_integral-(mp.pi**2/32-mp.mpf(1)/4))<mp.mpf('1e-25')

for L in [4,6,10]:
    count=0
    for support in product((0,1),repeat=L):
        if not any(support) or any(support[i]==support[i-1]==0 for i in range(L)):
            continue
        if all(support): continue
        start=next(i for i in range(L) if support[i] and not support[i-1])
        x=[F(0)]*L
        good=True
        i=start
        while True:
            block=[]
            while support[i]:
                block.append(i); i=(i+1)%L
                if i==start: break
            k=len(block)
            if k!=1 and k%2: good=False;break
            s=F(2) if k==1 else F(2*k+2,k+2)
            d=0 if k==1 else 2*s/k
            for j,e in enumerate(block,1):
                x[e]=F(j//2)*d if j%2==0 else s-F(j//2)*d
            i=(i+1)%L  # skip the single zero
            if i==start:break
        if not good: continue
        sv=[x[v-1]+x[v] for v in range(L)]
        grad=[1/sv[e]+1/sv[(e+1)%L]-1 for e in range(L)]
        assert sum(x)==L and all(s>0 for s in sv)
        assert all(x[e]*grad[e]==0 for e in range(L))
        if any(x[e] not in (0,2) for e in range(L)):
            assert max(grad[e] for e in range(L) if not x[e])>=F(1,2*L)
        count+=1
    print(f'C{L}: {count} boundary equilibria from admissible supports (including 2 segment endpoints); algebra exact')

rng=np.random.default_rng(550341)
for L in [4,6,10,20,50,100,400]:
    # Generate the exact terminal law directly, using independent logistic pairs.
    # A batch avoids large memory even for L=400.
    n=200000
    out=[]
    for first in range(0,n,1000):
        zz=rng.logistic(size=(min(1000,n-first),L//2)).sum(axis=1)/math.sqrt(L)
        out.append(zz)
    zz=np.concatenate(out)
    print(f'exact-law MC L={L}: var(Z)={zz.var(ddof=1):.7f}, '
          f'excess={np.mean((zz-zz.mean())**4)/zz.var()**2-3:.6f}, '
          f'theory excess={12/(5*L):.6f}, '
          f'P(|Z|>2sqrt(c))={np.mean(abs(zz)>2*math.sqrt(float(zeta(2,1)))):.6f}')

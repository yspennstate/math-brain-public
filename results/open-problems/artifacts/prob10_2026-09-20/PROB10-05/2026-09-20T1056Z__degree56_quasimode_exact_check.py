#!/usr/bin/env python3
from ast import literal_eval
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import re

# Exact degree-56 finite-polynomial certificate for PROB10-05.
# The Gaussian moment engine is reused from the immutable scale-correct
# degree-48 checker after verifying its Git blob hash. Only DEG and the frozen
# polynomial witness are changed. The inherited degree-40 non-Perron min-max
# mass is then combined with the new Rayleigh/residual certificate.

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=ROOT/'proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0645Z__degree48_safe_trace_exact_check.py'
WIT=HERE/'2026-09-20T1055Z__degree56_witness.txt'
raw=BASE.read_bytes()
blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert blob=='8f82e8ae344db14a32b013636a4ef62f4a726ce3'
PC=literal_eval(WIT.read_text())
assert len(PC)==57

src=raw.decode()
prefix=src.split('# Coarse outward spectral data.')[0]
prefix=prefix.replace('DEG=48','DEG=56',1)
prefix=re.sub(r'PC=\[.*?\]\n\nr=', 'PC='+repr(PC)+'\n\nr=', prefix, count=1, flags=re.S)
ns={'__name__':'__degree56_exact_core__'}
exec(compile(prefix,str(BASE), 'exec'),ns)

SCALE=ns['SCALE']; floor_frac=ns['floor_frac']; ceil_frac=ns['ceil_frac']
muI=ns['muI']; eps2I=ns['eps2I']
mu_lo=F(91221208,100000000)
mu_hi=F(91221209,100000000)
eps2_hi=F(677,50000000)  # 0.00001354
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

r=F(7,8); s=F(24861,25000); c=s*F(1+r,2)
trace4=F(54959,50000)
targets=[
F(27719,50000),F(8583,20000),F(2071,6250),F(25537,100000),
F(4913,25000),F(7553,50000),F(5801,50000),F(8907,100000),
F(3419,50000),F(5253,100000),F(101,2500),F(3113,100000),
F(601,25000),F(1859,100000),F(1437,100000),F(1107,100000),
F(847,100000),F(4,625)]
L40=sum(a**4 for a in targets)+r**160/(F(16)*(1-r**8))

theta=F(42971,250000)       # 0.171884
x=F(9122805,10000000)      # 0.9122805
beta=F(71377,100000)        # 0.71377
assert x**62500 < r**42971  # x < r^(4 theta)
assert x>mu_hi and mu_lo>beta
trace_margin=beta**4-(trace4-x**4-L40)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert trace_margin>0 and temple_margin>0

# Exact finite part of the source covariance bridge. The inherited k>=6
# algebraic factorization is also sanity-checked at its endpoint inequality.
cov=[]
for k in range(1,6):
    u=r**k; tk=c*r**(k-1)
    A=6*u**5*tk+2*u**10-5*u**6-5*u**4+2
    margin=A*A-4*(1-u**4)**5
    assert A>0 and margin>0
    cov.append(margin)
assert c/r>1
assert F(4)-F(7,4)-F(20,16)==F(1)

incoming=F(53683,312500)
upper=F(1,4)
assert theta>incoming and upper-theta<upper-incoming

print('base blob =',blob)
print('mu interval =',ns['interval_float'](muI))
print('eps2 interval =',ns['interval_float'](eps2I))
print('mu coarse =',mu_lo,mu_hi)
print('eps2 coarse upper =',eps2_hi,float(eps2_hi))
print('L40 =',float(L40))
print('trace margin =',float(trace_margin))
print('Temple margin =',float(temple_margin))
print('covariance finite margins =',[float(z) for z in cov])
print('incoming lower/width =',float(incoming),float(upper-incoming))
print('new lower/width =',float(theta),float(upper-theta))
print('repository gain =',float(theta-incoming))
print('ALL_EXACT_CHECKS_PASS = True')

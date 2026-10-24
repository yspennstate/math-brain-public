#!/usr/bin/env python3
from ast import literal_eval
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import re

# PROB10-05 exact checker for the redesigned Lamperti comparator r=22/25.
# The finite Gaussian-moment engine is reused from an immutable verified base
# after checking its Git blob hash.  We then reparameterize the engine to the
# new (r,s), recompute the degree-56 witness Rayleigh quotient/residual, prove
# the all-lag covariance bridge, certify an HGR four-cycle trace cap, and finish
# with an exact trace-separation/Kato-Temple contradiction.

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT/'proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0645Z__degree48_safe_trace_exact_check.py'
WIT = HERE/'2026-09-20T1055Z__degree56_witness.txt'

raw = BASE.read_bytes()
base_blob = sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert base_blob == '8f82e8ae344db14a32b013636a4ef62f4a726ce3'
wraw = WIT.read_bytes()
wit_blob = sha1(b'blob '+str(len(wraw)).encode()+b'\0'+wraw).hexdigest()
assert wit_blob == '8c2448736bb1ea40eeb50babdde1b459711232f9'
PC = literal_eval(wraw.decode())
assert len(PC) == 57

# Reuse only the exact moment-engine prefix; replace every parameter before it
# is executed.  No old spectral bound is imported.
src = raw.decode()
prefix = src.split('# Coarse outward spectral data.')[0]
prefix = prefix.replace('DEG=48', 'DEG=56', 1)
prefix = re.sub(r'PC=\[.*?\]\n\nr=', 'PC='+repr(PC)+'\n\nr=', prefix,
                count=1, flags=re.S)
prefix = prefix.replace('r=F(7,8)', 'r=F(22,25)', 1)
prefix = prefix.replace('s=F(24861,25000)', 's=F(936901,940000)', 1)
ns = {'__name__':'__mesh22_25_exact_core__'}
exec(compile(prefix, str(BASE), 'exec'), ns)

SCALE = ns['SCALE']
floor_frac = ns['floor_frac']
ceil_frac = ns['ceil_frac']
interval_float = ns['interval_float']
muI = ns['muI']
eps2I = ns['eps2I']
r = ns['r']; s = ns['s']; c = ns['c']
PI = ns['PI']
sqrt_bounds = ns['sqrt_bounds']
atan_point_bounds = ns['atan_point_bounds']

assert r == F(22,25)
assert c == F(936901,1000000)
assert s == F(936901,940000)

# Outward coarsenings of the recomputed new-operator finite-polynomial data.
mu_lo = F(9155053441, 10_000_000_000)
mu_hi = F(9155053442, 10_000_000_000)
eps2_hi = F(270154, 10_000_000_000)
assert muI[0] > floor_frac(mu_lo*SCALE)
assert muI[1] < ceil_frac(mu_hi*SCALE)
assert eps2I[0] > 0
assert eps2I[1] < ceil_frac(eps2_hi*SCALE)

# ---------------------------------------------------------------------------
# Exact all-lag Lamperti covariance bridge.
# R(u)=(-2u^10+5u^6+5u^4+2(1-u^4)^(5/2)-2)/(6u^5).
# For k=1,2, R(r^k)<c r^(k-1) is isolated and squared exactly.
radical_margins=[]
for k in (1,2):
    u = r**k
    cap = c*r**(k-1)
    A = 6*u**5*cap + 2*u**10 - 5*u**6 - 5*u**4 + 2
    margin = A*A - 4*(1-u**4)**5
    assert A > 0 and margin > 0
    radical_margins.append(margin)

# For k>=3 Taylor's theorem gives
# (1-z)^(5/2) <= 1-(5/2)z+(15/8)z^2, hence
# R(u) <= 5u/6+5u^3/8-u^5/3.
# g(q)=5/6+5q/8-q^2/3 is increasing on q<=r^6, so k=3 is worst.
deriv_margin = F(5,8) - F(2,3)*r**6
tail_endpoint = r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin > 0
assert tail_endpoint < c

# ---------------------------------------------------------------------------
# HGR/Gebelein upper bound for the softened Gaussian four-cycle trace.
a = (r+r**3)/(1+r**4)
b = 2*r*r/(1+r**4)
v = (1+a)/(1+r)
g = (1+b+2*a)/(2*(1+r))
h = (a+b)/(1+r)
varV = s*v + (1-s)
rho_adj = s*g/varV
rho_opp = s*h/varV
assert 0 < rho_opp < rho_adj < 1
kappa = 2*rho_adj/(1+rho_opp)
assert 0 < kappa < 1

def asin_bounds_pos(rho):
    rho = F(rho)
    slo, shi = sqrt_bounds(1-rho*rho)
    tlo, thi = slo/rho, shi/rho
    atan_lo = atan_point_bounds(tlo)[0]
    atan_hi = atan_point_bounds(thi)[1]
    return PI[0]/2-atan_hi, PI[1]/2-atan_lo

asin_adj = asin_bounds_pos(rho_adj)
asin_opp = asin_bounds_pos(rho_opp)
qadj_lo = 2*asin_adj[0]/PI[1]
qadj_hi = 2*asin_adj[1]/PI[0]
qopp_lo = 2*asin_opp[0]/PI[1]
qopp_hi = 2*asin_opp[1]/PI[0]
assert 0 < qadj_lo <= qadj_hi < 1
assert 0 < qopp_lo <= qopp_hi < 1

# Let A=sgn(V0)sgn(V2), B=sgn(V1)sgn(V3).  The maximal correlation
# between the two Gaussian opposite-pair blocks is kappa, so
# E[AB] <= qopp^2+kappa(1-qopp^2).
m4_hi = kappa + (1-kappa)*qopp_hi*qopp_hi
p4_hi = (1 + 4*qadj_hi + 2*qopp_hi + m4_hi)/16
trace_hi = p4_hi/(1-r**4)
trace_cap = F(115053,100000)
assert trace_hi < trace_cap

# ---------------------------------------------------------------------------
# Exact spectral separation and Kato-Temple synthesis.
theta = F(43013,250000)       # 0.172052
x = F(366313,400000)          # 0.9157825
beta = F(408877,500000)       # 0.817754
# 4 theta = 43013/62500; x < r^(4 theta) iff x^62500 < r^43013.
assert x**62500 < r**43013
assert x > mu_hi > mu_lo > beta
spectral_tail_margin = beta**4 - (trace_cap-x**4)
temple_margin = (x-mu_hi)*(mu_lo-beta) - eps2_hi
assert spectral_tail_margin > 0
assert temple_margin > 0

incoming = F(42971,250000)
upper = F(1,4)
assert theta > incoming
assert upper-theta < upper-incoming

print('base blob =', base_blob)
print('witness blob =', wit_blob)
print('r,c,s =', r, c, s)
print('mu interval =', interval_float(muI))
print('eps2 interval =', interval_float(eps2I))
print('mu coarse =', mu_lo, mu_hi)
print('eps2 coarse upper =', eps2_hi, float(eps2_hi))
print('covariance squared margins k=1,2 =', [float(z) for z in radical_margins])
print('tail derivative margin =', float(deriv_margin))
print('tail endpoint upper =', float(tail_endpoint))
print('tail endpoint c-margin =', float(c-tail_endpoint))
print('rho_adj,rho_opp,kappa =', float(rho_adj), float(rho_opp), float(kappa))
print('trace HGR upper <', float(trace_hi))
print('trace cap/margin =', float(trace_cap), float(trace_cap-trace_hi))
print('theta,x,beta =', float(theta), float(x), float(beta))
print('spectral-tail margin =', float(spectral_tail_margin))
print('Temple margin =', float(temple_margin))
print('incoming lower/width =', float(incoming), float(upper-incoming))
print('new lower/width =', float(theta), float(upper-theta))
print('repository gain =', float(theta-incoming))
print('ALL_EXACT_CHECKS_PASS = True')

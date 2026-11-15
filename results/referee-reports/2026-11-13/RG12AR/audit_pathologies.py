"""Two independent stress tests: log-periodic negative tails and infinite log drift."""
import math
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp

signal.alarm(240)
resource.setrlimit(resource.RLIMIT_CPU, (220, 230))
mp.mp.dps = 70
started = time.monotonic()
rho = mp.mpf(2)/5

def T(p):
    # Remainder <= rho**400 < 2e-159.
    return mp.fsum((1-rho)*rho**j/(1+mp.mpf(p)/16**j) for j in range(400))

print('lacunary scaling: a regularly varying T with T(16p)/T(p)->rho would require T(4p)/T(p)->sqrt(rho)')
print('required sqrt(rho)', mp.nstr(mp.sqrt(rho), 30))
for n in [4, 8, 16, 32]:
    p = 16**n
    a, b, c = T(p), T(4*p), T(16*p)
    print('n', n, 'T(4p)/T(p)', mp.nstr(b/a, 30), 'T(16p)/T(4p)', mp.nstr(c/b, 30), 'T(16p)/T(p)', mp.nstr(c/a, 30))

# Independent bilateral limit. Its left and right omitted tails are <1e-75.
def phase(x):
    return (1-rho)*mp.fsum(rho**ell/(1+mp.mpf(x)/mp.power(16, ell)) for ell in range(-200, 401))
print('bilateral limit F(4)/F(1)', mp.nstr(phase(4)/phase(1), 40))
print('bilateral limit rho*F(1)/F(4)', mp.nstr(rho*phase(1)/phase(4), 40))
def rational_phase_interval(x):
    rr = F(2, 5)
    lo = (1-rr)*sum((rr**ell/(1+F(x)/F(16)**ell) for ell in range(-60, 101)), F(0))
    rem_right = rr**101
    rem_left = (1-rr)/x*(16*rr)**(-61)/(1-F(1)/(16*rr))
    return lo, lo+rem_right+rem_left

f1lo, f1hi = rational_phase_interval(1)
f4lo, f4hi = rational_phase_interval(4)
ratio1lo, ratio1hi = f4lo/f1hi, f4hi/f1lo
ratio2lo, ratio2hi = F(2, 5)*f1lo/f4hi, F(2, 5)*f1hi/f4lo
assert ratio1hi < ratio2lo
print('exact rational intervals disjoint:', ratio1hi < ratio2lo,
      'widths', float(ratio1hi-ratio1lo), float(ratio2hi-ratio2lo))
print('T(16p)-rho*T(p)-(1-rho)/(1+16p) at p=7:', mp.nstr(T(112)-rho*T(7)-(1-rho)/113, 4))

# Another bona fide critical q: b_{2**(j*j)}=1/(zeta(2)*j*j), j>=1.
# At p=1, K(1,m+1)=b_m exactly, since nu(m)=b_m/h(m+1).
# Hence E_1 log h(P_1) >= sum_{j<=J} b_j log h(2**(j*j)+1).
def logh_big(n):
    x = mp.mpf(n)
    if n < 10000:
        return mp.log(2/mp.sqrt(mp.pi))+mp.loggamma(x+mp.mpf('.5'))-mp.loggamma(x)
    v = mp.log(2/mp.sqrt(mp.pi))+mp.log(x)/2
    for k in range(1, 17):
        v += mp.bernoulli(2*k)/(2*k*(2*k-1))*(mp.power(2, 1-2*k)-2)/x**(2*k-1)
    return v

fZ = mp.fsum(1/(mp.zeta(2)*j*j*(mp.mpf(2)**(j*j)+1)) for j in range(1, 31))
Z = 1/(1-fZ)
print('infinite-log-moment critical example Z', mp.nstr(Z, 35))
print('critical equations satisfied exactly by Z=1/(1-sum b_m/(m+1)), sum b_m=1')
print('asymptotic contribution per support atom', mp.nstr(3*mp.log(2)/mp.pi**2, 30))
partial = mp.mpf(0)
for j in range(1, 81):
    contribution = logh_big(2**(j*j)+1)/(mp.zeta(2)*j*j)
    partial += contribution
    if j in [5, 10, 20, 40, 80]:
        print('J', j, 'partial E_1 log h(P_1)', mp.nstr(partial, 20), 'last contribution', mp.nstr(contribution, 20))
print('At p=1, the truncated increment L is identically zero for this example.')
print('seconds', round(time.monotonic()-started, 3), 'peak_rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

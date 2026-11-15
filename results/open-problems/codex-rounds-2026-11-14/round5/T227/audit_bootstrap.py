"""Second derivation: binomial exponentials, literal interval gradients,
exact sign Chernoff bound, and high-precision nearly balanced trajectories.
No other script is imported.
"""
import json
import math
import os
import resource
import time
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
scale = 10**32

def down(x): return Q(math.floor(x*scale), scale)
def up(x): return Q(math.ceil(x*scale), scale)

def exp_binomial(x):
    n = 2**40
    assert 0 <= x < n
    # log(1+x/n)<=x/n<=-log(1-x/n). Bound both limits
    # with rational arithmetic and outward rounding at every squaring.
    lo, hi = down(1+x/n), up(1/(1-x/n))
    for _ in range(40):
        lo, hi = down(lo*lo), up(hi*hi)
    return lo, hi

def tanh_point(x):
    lo, hi = exp_binomial(2*x)
    return down((lo-1)/(lo+1)), up((hi-1)/(hi+1))

class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        if not isinstance(other, I): other = I(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __mul__(self, other):
        if not isinstance(other, I): other = I(other)
        ends = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(ends), max(ends))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = Q(other)
        assert other > 0
        return I(self.lo/other, self.hi/other)
    def pair(self): return [float(self.lo), float(self.hi)]
    def absmax(self): return max(abs(self.lo), abs(self.hi))

assert tanh_point(Q('1.97'))[0] > Q('.961')
assert tanh_point(Q('2.03'))[1] < Q('.967')
assert tanh_point(Q('1.97'))[0] > Q('.96')
assert tanh_point(Q('2.03'))[1] < Q('.97')
# Direct signed endpoint extrema, independent of the midpoint expansion
# in the main proof. Positive sign fraction lies in [.49,.51].
ztube = (Q('.51')*Q('1.001')*Q('.967')
         -Q('.49')*Q('.999')*Q('.961')+Q('.2')*Q('.967'))
assert ztube < Q('.217')
metric = []
S = Q(11, 10)*Q(1, 50)*Q(40, 39)
for n in (1, 2, 5):
    m = n*n
    a, u = I('7.9', '8.1'), I('.961', '.967')
    v, q = I('-.217', '.217'), I(1-Q('.217')**2, 1)
    r, B = I(0, 1-Q('.961')**2), I(-Q('1.201')/n, Q('1.201')/n)
    ga = [v/m for _ in range(m)]
    gB = [[a*q*u/(m*n) for _ in range(m)] for _ in range(m)]
    gc = [r*sum((a*q*B for _ in range(m)), I(0))/(m*n) for _ in range(m)]
    gs = ga+[g for row in gB for g in row]+gc
    # Ordinary interval multiplication permits unequal factors, including
    # opposite signs. This is a cross-gradient calculation, not a norm.
    cross = m*sum((g*g for g in gs), I(0))
    assert cross.lo > 50 and cross.hi < 63
    da = m*S*max(g.absmax() for g in ga)
    dw = n*m*S*max(g.absmax() for row in gB for g in row)
    dc = m*S*max(g.absmax() for g in gc)
    assert da < Q('.09') and dw < Q('.2') and dc < Q('.029')
    metric.append(dict(width=m, cross=cross.pair(), movements=list(map(float, (da, dw, dc)))))

u0lo = tanh_point(Q('1.999'))[0]
u0hi = tanh_point(Q('2.001'))[1]
z0 = Q('.51')*Q('1.001')*u0hi-Q('.49')*Q('.999')*u0lo
assert Q('7.99')*u0lo*(1-z0*z0) > 7
# Density 500, output interval length 2s, inverse derivative m²/7.
assert 500*Q(2, 7) < 143
assert (2*Q('1.001')*Q('8.01'))**2 < 320
assert Q('.33')*S < Q('.0075')
assert Q('7.9')*(1-Q('.225')**2)*Q('.96') > Q('7.2')
assert Q('8.1')*Q('.97') < Q('7.86')
assert 40**12 < Q(200000**4, 50) <= 40**13

# Exact Chernoff bound for m=200000 signs: for K~Bin(m,1/2),
# use z=51/49 and P(K>=102000)<=((1+z)/2)^m/z^102000.
# Include both tails and all rows. Integer powers, no exponential series.
m = 200000
row_chernoff = Q(2*m*50**m, 51**102000*49**98000)
assert row_chernoff < Q('2e-12')
exp40lo, _ = exp_binomial(Q(40))
assert exp40lo > 2*10**17
independent_prob = row_chernoff+2/exp40lo+Q(143, m*m)
assert independent_prob < Q('4e-9')

def tanh_decimal(x):
    e = (2*x).exp()
    return (e-1)/(e+1)

def decimal_state(x, m):
    dm, root = D(m), D(m).sqrt()
    a, B, c = x[:m], x[m:m+m*m], x[m+m*m:]
    u = [tanh_decimal(cj) for cj in c]
    z = [sum((B[i*m+j]*u[j] for j in range(m)), D(0))/root for i in range(m)]
    v = [tanh_decimal(zi) for zi in z]
    q = [1-vi*vi for vi in v]
    F = sum((a[i]*v[i] for i in range(m)), D(0))/dm
    ga = [vi/dm for vi in v]
    gB = [a[i]*q[i]*u[j]/(dm*root) for i in range(m) for j in range(m)]
    gc = [(1-u[j]*u[j])*sum((a[i]*q[i]*B[i*m+j] for i in range(m)), D(0))/(dm*root) for j in range(m)]
    return F, ga+gB+gc

precision_audits = []
for precision in (80, 110):
    with localcontext() as ctx:
        ctx.prec = precision
        m = 4
        base = [D(8)]*m+[D('-0.5') if j < 2 else D('0.5') for i in range(m) for j in range(m)]+[D(2)]*m
        assert decimal_state(base, m)[0] == 0
        for perturbation in ('1e-20', '1e-30'):
            for direction in (-1, 1):
                x0 = base[:]
                x0[m] += direction*D(perturbation)
                for hs in ('.9', '1', '1.1'):
                    h = D(hs)
                    x, rows, signed = x0[:], [], D(0)
                    initial = decimal_state(x, m)[0]
                    assert 0 < abs(initial) < D('1e-19')
                    for t in range(40):
                        f, grad = decimal_state(x, m)
                        assert all(D('7.9') < ai < D('8.1') for ai in x[:m])
                        assert all(D('1.97') < ci < D('2.03') for ci in x[m+m*m:])
                        assert max(abs((bi-b0)*2) for bi, b0 in zip(x[m:m+m*m], x0[m:m+m*m])) < D('.2')
                        shift_error = max(abs((bi-b0)*2+D('7.53')*signed) for bi, b0 in zip(x[m:m+m*m], x0[m:m+m*m]))
                        assert shift_error < D('.0075')
                        rows.append(dict(t=t, F=str(f), common_shift_error=str(shift_error)))
                        if abs(f) >= D('.02'):
                            assert abs(f) < D('1.38')
                            break
                        y = [xi-D(m)*h*f*gi for xi, gi in zip(x, grad)]
                        fy = decimal_state(y, m)[0]
                        assert 40 < abs(fy/f) < 69 and fy*f < 0
                        signed += h*f
                        x = y
                    else:
                        raise AssertionError('Near-zero trajectory did not escape')
                    precision_audits.append(dict(precision=precision, perturbation=perturbation,
                                                direction=direction, h=hs, initial=str(initial),
                                                exit_t=t, exit_F=str(f), rows=rows))

# Precision doubling cross-check: initial residuals, exit times and exit
# values must agree, including the 30-digit perturbation.
for lo in precision_audits:
    if lo['precision'] != 80: continue
    hi = next(a for a in precision_audits if a['precision'] == 110
              and all(a[k] == lo[k] for k in ('perturbation', 'direction', 'h')))
    assert lo['exit_t'] == hi['exit_t']
    assert abs(D(lo['exit_F'])-D(hi['exit_F'])) < D('1e-40')

summary = dict(status='PASS', method='binomial exponentials, literal interval gradients, exact Chernoff, Decimal trajectories',
               independent_tube_z_upper=float(ztube), literal_metric=metric,
               exact_row_chernoff_at_200000=float(row_chernoff),
               independent_failure_bound_at_200000=float(independent_prob),
               arbitrary_precision_trajectories=len(precision_audits),
               longest_near_zero_exit=max(a['exit_t'] for a in precision_audits),
               smallest_initial_residual=min(abs(D(a['initial'])) for a in precision_audits).__str__(),
               nice=os.getpriority(os.PRIO_PROCESS, 0),
               max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               seconds=time.monotonic()-started)
assert summary['max_rss_bytes'] < 1_000_000_000
with open('bootstrap_audit.json', 'w') as f:
    json.dump(dict(summary=summary, precision_audits=precision_audits), f, indent=2)
print(json.dumps(summary, indent=2))

"""Independent recheck of the round-5 deterministic and probability constants."""
import json
import math
import os
import resource
import time
from decimal import Decimal, localcontext
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
start = time.monotonic()
assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def exp_bounds(x):
    # Exact rational series, with a different degree from the old scripts.
    term = total = Q(1)
    for k in range(1, 73):
        term *= x/k
        total += term
    assert 0 <= x < 74
    return total, total + term*x/73/(1-x/74)

def tanh_bounds(x):
    l, u = exp_bounds(2*x)
    return (l-1)/(l+1), (u-1)/(u+1)

assert tanh_bounds(Q('1.97'))[0] > Q('.96')
assert tanh_bounds(Q('2.03'))[1] < Q('.97')
z0 = Q('.965')*Q('.021') + Q('.005')*Q('1.001')
z = z0 + Q('.2')*Q('.97')
dlo = Q('7.9')*(1-Q('.225')**2)*Q('.96')
dhi = Q('8.1')*Q('.97')
cup = (1-Q('.96')**2)*Q('8.1')*Q('1.201')
klo = dlo*dlo-Q('.225')**2-cup*cup
khi = dhi*dhi+Q('.225')**2+cup*cup
s = Q('1.1')*Q('.02')*Q(40,39)
assert z < Q('.225') and klo > 50 and khi < 63
assert Q('.9')*klo-1 > 40 and Q('1.1')*khi-1 < 69
assert Q('7.99')-s*Q('.225') > Q('7.9')
assert Q('8.01')+s*Q('.225') < Q('8.1')
assert s*dhi < Q('.2')
assert Q('1.999')-s*cup > Q('1.97')
assert Q('2.001')+s*cup < Q('2.03')
assert dlo > Q('7.2') and dhi < Q('7.86')
assert Q('.33')*s < Q('.0075')
derivative = Q('7.99')*Q('.96')*(1-z0*z0)
assert derivative > 7
assert (2*Q('1.001')*Q('8.01'))**2 < 320
m = 200000
prob = Q(2*m+2)/exp_bounds(Q(40))[0] + Q(143,m*m)
assert prob < Q('4e-9')
assert 40**12 < Q(m**4,50) <= 40**13

# Second derivation of the transcendental and tube bounds: Decimal exp
# is an audit only. The exact rational checks above are the certificate.
with localcontext() as ctx:
    ctx.prec = 70
    def th(x):
        e = (2*Decimal(x)).exp()
        return (e-1)/(e+1)
    ul, uh = th('1.97'), th('2.03')
    # Signed endpoints, not the midpoint formula used in the proof.
    z_alt = (Decimal('.51')*Decimal('1.001')*uh
             -Decimal('.49')*Decimal('.999')*ul + Decimal('.2')*uh)
    assert z_alt < Decimal('.225')
    alt_Dlo = Decimal('7.9')*(1-z_alt*z_alt)*ul
    alt_Dhi = Decimal('8.1')*uh
    alt_C = (1-ul*ul)*Decimal('8.1')*Decimal('1.201')
    alt_klo = alt_Dlo**2-z_alt**2-alt_C**2
    alt_khi = alt_Dhi**2+z_alt**2+alt_C**2
    assert alt_klo > 50 and alt_khi < 63

def fg(x, m):
    root = math.sqrt(m)
    a, B, c = x[:m], x[m:m+m*m], x[m+m*m:]
    u = list(map(math.tanh,c))
    z = [math.fsum(B[i*m+j]*u[j] for j in range(m))/root for i in range(m)]
    v = list(map(math.tanh,z))
    aq = [a[i]/math.cosh(z[i])**2 for i in range(m)]
    f = math.fsum(ai*vi for ai,vi in zip(a,v))/m
    g = ([vi/m for vi in v]
         +[aq[i]*u[j]/(m*root) for i in range(m) for j in range(m)]
         +[math.fsum(aq[i]*B[i*m+j] for i in range(m))/(m*root*math.cosh(c[j])**2) for j in range(m)])
    return f, g

audits = []
fd = 0.
for m in (4, 16):
    root = math.sqrt(m)
    for kind in ('circulant', 'imbalanced_columns'):
        x0 = ([7.99+.02*(i%3)/2 for i in range(m)]
              +[(-1 if ((j-i if kind=='circulant' else j)%m)<m//2 else 1)
                *(1.0001+.0002*((i+2*j)%4))/root for i in range(m) for j in range(m)]
              +[1.999+.002*(j%3)/2 for j in range(m)])
        f0, g0 = fg(x0,m)
        assert 1e-10 < abs(f0) < .02
        if m == 4:
            for k, g in enumerate(g0):
                xp, xm = x0[:], x0[:]
                xp[k] += 1e-6
                xm[k] -= 1e-6
                fd = max(fd, abs((fg(xp,m)[0]-fg(xm,m)[0])/2e-6-g))
        for h in (.9,1.,1.1):
            x, prev, signed = x0[:], None, 0.
            for t in range(20):
                f,g = fg(x,m)
                assert 50 < m*math.fsum(gi*gi for gi in g) < 63
                assert min(x[:m]) > 7.9 and max(x[:m]) < 8.1
                assert min(x[m+m*m:]) > 1.97 and max(x[m+m*m:]) < 2.03
                movement = [(b-b0)*root for b,b0 in zip(x[m:m+m*m],x0[m:m+m*m])]
                assert max(map(abs,movement)) < .2
                assert max(abs(w+7.53*signed) for w in movement) < .0075
                if prev is not None:
                    assert f*prev < 0 and 40 < abs(f/prev) < 69
                if abs(f) >= .02:
                    assert abs(f) < 1.38
                    break
                prev = f
                signed += h*f
                x = [xi-m*h*f*gi for xi,gi in zip(x,g)]
            else:
                raise AssertionError('escape failed')
            audits.append(dict(width=m,kind=kind,h=h,initial=f0,exit_t=t,exit_F=f))
assert fd < 1e-7
summary = dict(status='PASS',z0=float(z0),z_tube=float(z),
               cross=[float(klo),float(khi)],
               alternate_cross=[float(alt_klo),float(alt_khi)],
               total_h_abs_F=float(s),movements=[float(s*Q('.225')),float(s*dhi),float(s*cup)],
               common_shift_error=float(s*Q('.33')),density_derivative=float(derivative),
               failure_upper=float(prob),time_bound=13,trajectories=len(audits),
               finite_difference_error=fd,nice=os.getpriority(os.PRIO_PROCESS,0),
               rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               seconds=time.monotonic()-start)
assert summary['rss_bytes'] < 1_000_000_000
with open('escape_recheck.json','w') as out:
    json.dump(dict(summary=summary,audits=audits),out,indent=2)
print(json.dumps(summary,indent=2))

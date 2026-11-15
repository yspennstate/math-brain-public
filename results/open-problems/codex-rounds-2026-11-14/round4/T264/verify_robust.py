"""Standard-library audits of the open-set theorem; no optimizer is used.

Checks competitors and arbitrary feasible perturbations, the pointwise mass
inequality, the explicit uniform error, sphere integration, and a counterexample
to dropping the nonzero third-coordinate hypothesis.
"""
import json
import math
import os
from pathlib import Path
import random
import resource
import signal
import sys
import time

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
# Memory rlimits are rejected in this environment. Working arrays are bounded
# to a few thousand scalars; the final assertion checks peak resident memory.
signal.alarm(90)
started = time.monotonic()
rng = random.Random(26404)
ROOT = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
pi = math.pi


def dot(u,v):
    return math.fsum(a*b for a,b in zip(u,v))


def scale(c,u):
    return tuple(c*t for t in u)


def unit(d):
    w = [rng.gauss(0,1) for _ in range(d)]
    r = math.sqrt(dot(w,w))
    return tuple(t/r for t in w)


def relu(t):
    return max(0.,t)


def evaluate(atoms,x):
    return math.fsum(c*relu(dot(u,x)) for c,u in atoms)


def risk(atoms,d):
    def kernel(u,v):
        co = max(-1.,min(1.,dot(u,v)))
        beta = math.acos(co)
        return (math.sin(beta)+(pi-beta)*co)/(2*pi*d)
    return math.fsum(c*t*kernel(u,v) for c,u in atoms for t,v in atoms)


def competitor(theta,z,tau):
    d = len(z)
    a,b = math.cos(theta/2),math.sin(theta/2)
    e1 = (1.,)+(0.,)*(d-1)
    v = (b,-a)+(0.,)*(d-2)
    h = a*z[1]-b*z[0]
    assert h > 0
    r = (tau-relu(z[0])/a)/h
    return [(1/a,e1),(-1/(a*b),v),(r,scale(-1,v))]


def perturb(theta,z,atoms,t=.015):
    """Add an independently chosen ridge, cancel all its training responses."""
    d = len(z)
    a,b = math.cos(theta/2),math.sin(theta/2)
    X1 = (a,b)+(0.,)*(d-2)
    X2 = (a,-b)+(0.,)*(d-2)
    w = unit(d)
    v1,v2 = relu(dot(w,X1)),relu(dot(w,X2))
    alpha = -v1/a
    beta = (v1-v2)/math.sin(theta)
    h = a*z[1]-b*z[0]
    gamma = -(relu(dot(w,z))+alpha*relu(z[0]))/h
    shifts = (alpha,beta,gamma)
    return [(c+t*r,u) for (c,u),r in zip(atoms,shifts)]+[(t,w)]


def bounds(theta,delta,H):
    a,b = math.cos(theta/2),math.sin(theta/2)
    K = 2+2*(H+2)/delta
    U = 2*theta/math.sin(theta)+K*theta
    # Independent stable form of U-theta/b from equation (18).
    gap = K*theta+(theta/b)*(2*math.sin(theta/4)**2)/a
    assert abs(gap-(U-theta/b)) < 3e-14*max(1,U)
    E = 2*math.sqrt(U*gap)
    eta = (1+1/delta)*E+theta*H/delta+U-2
    return K,U,E,eta


def test_localization():
    worst = 0.
    count = 0
    # Include wrong-sign, off-plane, inactive, and kink directions explicitly.
    for d in (2,3,7):
        for theta in (1e-6,.02,.3):
            a,b = math.cos(theta/2),math.sin(theta/2)
            X1 = (a,b)+(0.,)*(d-2)
            X2 = (a,-b)+(0.,)*(d-2)
            directions = [unit(d) for _ in range(1000)]
            directions += [(0.,1.)+(0.,)*(d-2), (0.,-1.)+(0.,)*(d-2),
                           (-1.,0.)+(0.,)*(d-2), (b,a)+(0.,)*(d-2),
                           (b,-a)+(0.,)*(d-2)]
            if d >= 3:
                directions.append((0.,0.,1.)+(0.,)*(d-3))
            for u in directions:
                # Direct response subtraction is independent of proof's cases.
                g = (relu(dot(u,X1))-relu(dot(u,X2)))/math.sin(theta)
                for t in (-1,1):
                    distance2 = math.fsum((val-(t if k==1 else 0.))**2
                                          for k,val in enumerate(u))
                    rhs = 4*(1-a*t*g)
                    worst = max(worst,distance2-rhs)
                    assert distance2 <= rhs+2e-9, (d,theta,t,u,distance2,rhs)
                    count += 1
    print(f'PASS: localization inequality, {count} signed directions; max violation {worst:.3g}')


def test_competitors():
    rows = []
    max_interp = 0.
    max_uniform_ratio = 0.
    for d in (2,3,7):
        for delta in (.1,.5,.9):
            H = 2.5
            for theta in (delta/2,delta*.01,delta*1e-5):
                a,b = math.cos(theta/2),math.sin(theta/2)
                X1 = (a,b)+(0.,)*(d-2)
                X2 = (a,-b)+(0.,)*(d-2)
                for label in (-H,0.,H):
                    # q at the cap boundary; both signs of first coordinate,
                    # and genuine out-of-plane coordinates in dimensions >=3.
                    z = list(unit(d))
                    other = math.sqrt(math.fsum(v*v for k,v in enumerate(z) if k!=1))
                    z = tuple(delta if k==1 else v*math.sqrt(1-delta*delta)/other
                              for k,v in enumerate(z))
                    base = competitor(theta,z,label)
                    atoms = perturb(theta,z,base)
                    K,U,E,eta = bounds(theta,delta,H)
                    cost = math.fsum(abs(c) for c,u in atoms)
                    assert cost <= 2/math.sin(theta)+K+1e-9
                    for sign in (1,-1):
                        # Reflection plus output sign covers both cap signs.
                        zz = tuple(sign*v if k==1 else v for k,v in enumerate(z))
                        aa = [(sign*c,tuple(sign*v if k==1 else v for k,v in enumerate(u)))
                              for c,u in atoms]
                        yy = sign*label
                        interp = max(abs(evaluate(aa,x)-y) for x,y in
                                     ((X1,1.),(X2,-1.),(zz,yy)))
                        max_interp = max(max_interp,interp)
                        assert interp < 3e-9, (d,delta,theta,label,sign,interp)
                        tests = [unit(d) for _ in range(48)]+[zz,X1,X2]
                        tests += [(0.,1.)+(0.,)*(d-2),(0.,-1.)+(0.,)*(d-2)]
                        actual = max(abs(theta*evaluate(aa,x)+2*sign*relu(-sign*x[1]))
                                     for x in tests)
                        max_uniform_ratio = max(max_uniform_ratio,actual/eta)
                        assert actual <= eta+1e-10
                        scaled = [(theta*c,u) for c,u in aa]
                        rr = risk(scaled,d)
                        lo = max(0.,math.sqrt(2/d)-eta)**2
                        hi = (math.sqrt(2/d)+eta)**2
                        assert lo-1e-10 <= rr <= hi+1e-10
                        if theta == delta*1e-5:
                            assert abs(rr-2/d) < 2e-4
                        rows.append({'d':d,'delta':delta,'theta':theta,
                                     'label':yy,'third_sign':sign,
                                     'cost_above_2_over_s':cost-2/math.sin(theta),
                                     'K':K,'uniform_sample_error':actual,
                                     'uniform_proved_bound':eta,'theta2_risk':rr})
    print(f'PASS: {len(rows)} feasible perturbed networks in d=2,3,7, both caps, labels -2.5,0,2.5')
    print(f'Maximum interpolation error {max_interp:.3g}; sampled error/proved bound {max_uniform_ratio:.3g}')
    for d in (2,3,7):
        row = next(r for r in rows if r['d']==d and r['delta']==.5
                   and r['theta']==.5e-5 and r['label']==2.5 and r['third_sign']==1)
        print(f"d={d} theta={row['theta']:g}: theta^2 R={row['theta2_risk']:.12g}, limit={2/d:.12g}")
    return rows


def test_surface():
    theta=.02
    z=(.2,.7,math.sqrt(.47))
    atoms=perturb(theta,z,competitor(theta,z,-1.),t=.05)
    atoms=[(theta*c,u) for c,u in atoms]
    nz,np=160,768
    def terms():
        for j in range(nz):
            alt=-1+2*(j+.5)/nz
            rad=math.sqrt(1-alt*alt)
            for k in range(np):
                ph=2*pi*(k+.5)/np
                x=(rad*math.cos(ph),rad*math.sin(ph),alt)
                yield evaluate(atoms,x)**2
    direct=math.fsum(terms())/(nz*np)
    exact=risk(atoms,3)
    assert abs(direct/exact-1)<1e-4, (direct,exact)
    print(f'PASS: out-of-plane S^2 integration scaled risk={direct:.12g}, kernel={exact:.12g}')
    return {'direct_scaled_risk':direct,'kernel_scaled_risk':exact}


def test_counterexample():
    # This third point stays near -e1, while its second coordinate tends to zero.
    rows=[]
    for theta in (.05,.005,.00005):
        a,b=math.cos(theta/2),math.sin(theta/2)
        s=math.sin(theta)
        atoms=[(1/s,(b,a)),(-1/s,(b,-a))]
        z=(-math.cos(3*theta/2),math.sin(3*theta/2))
        assert abs(evaluate(atoms,z)-1)<1e-11
        rr=risk([(theta*c,u) for c,u in atoms],2)
        if theta==.00005:
            assert abs(rr-.5)<1e-7
        rows.append({'theta':theta,'third_second_coordinate':z[1],
                     'third_label':1,'theta2_risk_d2':rr})
    # For theta in (0,pi/2), this is the unique two-point minimum. It already
    # interpolates the third observation, so is also a three-point minimum.
    print(f"PASS: dropping fixed delta fails: theta^2 R2={rows[-1]['theta2_risk_d2']:.12g}, expected 1/2, not 1")
    return rows


def test_tail_constants():
    result=[]
    # Independently normalize sin^m by integration-by-parts recurrence.
    integrals={0:pi,1:2.}
    for m in range(2,7):
        integrals[m]=(m-1)*integrals[m-2]/m
    for d in range(2,8):
        cd=math.gamma(d/2)/(math.sqrt(pi)*math.gamma((d-1)/2))
        assert abs(cd*integrals[d-2]-1)<2e-15
        alpha=(d-1)/2
        D=cd/(2*(d-1))*(2/d)**alpha
        if d==2:
            assert abs(D-1/(2*pi))<1e-15
        if d==3:
            assert abs(D-1/12)<1e-15
        if d==5:
            assert abs(D-3/200)<1e-15
        result.append({'d':d,'alpha':alpha,'tail_liminf_lower_bound':D})
        print(f'd={d}: alpha={alpha:g}, tail liminf lower bound={D:.12g}')
    # Check the logarithmic endpoint divergence independently through dyadic
    # shells: theta^(d-2) R^alpha dtheta has asymptotic density 1/theta.
    for d in (2,3,5):
        r=(d-1)/2
        for theta in (1e-3,1e-5):
            shell_density=theta**(d-2)*(theta**-2)**r*theta
            assert abs(shell_density-1)<1e-12
    print('PASS: angular normalizers, lower-tail constants, endpoint exponent')
    return result


test_localization()
data={'feasible_networks':test_competitors(),
      'surface_check':test_surface(),
      'equatorial_counterexample':test_counterexample(),
      'tail_constants':test_tail_constants()}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes=rss if sys.platform=='darwin' else 1024*rss
assert rss_bytes<1_000_000_000
data['resources']={'seconds':time.monotonic()-started,'peak_rss_bytes':rss_bytes,
                   'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1}
(ROOT/'verification_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('All assertions passed.')
print('Resources:',data['resources'])

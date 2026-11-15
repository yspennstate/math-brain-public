"""Independent piecewise-antiderivative check of the round-3 formulas."""
import math
import os
import resource
import signal
import time

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
signal.alarm(45)
start = time.monotonic()
pi = math.pi


def dot(u, v):
    return math.fsum(x*y for x, y in zip(u, v))


def value(atoms, x):
    return math.fsum(c*max(0., dot(z, x)) for c, z in atoms)


def integrate_circle(atoms):
    cuts = {0., 2*pi}
    for _, z in atoms:
        ph = math.atan2(z[1], z[0])
        cuts.update(((ph-pi/2) % (2*pi), (ph+pi/2) % (2*pi)))
    cuts = sorted(cuts)
    integrals = []
    for left, right in zip(cuts, cuts[1:]):
        mid = (left+right)/2
        active = [(c,z) for c,z in atoms
                  if dot(z, (math.cos(mid),math.sin(mid))) > 0]
        A = math.fsum(c*z[0] for c,z in active)
        B = math.fsum(c*z[1] for c,z in active)
        cc = (right-left)/2 + (math.sin(2*right)-math.sin(2*left))/4
        ss = (right-left)/2 - (math.sin(2*right)-math.sin(2*left))/4
        cross = math.sin(right)**2-math.sin(left)**2
        integrals.append(A*A*cc+B*B*ss+A*B*cross)
    return math.fsum(integrals)/(2*pi)


def main():
    maxerr = 0.
    for theta in (1e-5, .001, .1, .7, 1.047):
        a,b = math.cos(theta/2),math.sin(theta/2)
        s = math.sin(theta)
        v = (b,-a)
        for tau in (1,-1):
            if tau == 1:
                W = ((1-b)/a,1.)
                L = math.hypot(*W)
                C = (1-b)/(a*b)
                atoms = [(1.,W),(-C,v)]
                beta = math.acos(-math.sqrt((1-b)/2))
                risk = (L*L+C*C)/4-L*C*(math.sin(beta)+(pi-beta)*math.cos(beta))/(2*pi)
                cost = L+C
                lam = (1/s+L/2,-1/s,L/2-1/a)
            else:
                C,D = a/b,(1+b)/a
                atoms = [(1.,(a,b)),(-C,v),(-D,(-b,a))]
                risk = (1+C*C+D*D)/4-(C+D)/(2*pi)
                cost = 1+C+D
                lam = (1+1/s,-1/s,-1/a)
            y = (1.,-1.,float(tau))
            X = ((a,b),(a,-b),(0.,1.))
            assert max(abs(value(atoms,x)-t) for x,t in zip(X,y)) < 2e-10
            assert abs(dot(lam,y)/cost-1) < 1e-12
            independent = integrate_circle(atoms)
            err = abs(independent/risk-1)
            maxerr = max(maxerr,err)
            assert err < 2e-10, (theta,tau,independent,risk)
            if theta == 1e-5:
                assert abs(theta*theta*independent-1) < 2e-5
            print(f'theta={theta:g} tau={tau:+d} cost={cost:.12g} theta^2*R2={theta*theta*independent:.12g}')
    print(f'PASS: piecewise antiderivatives vs earlier exact risk; max relative error {maxerr:.3g}')
    print('PASS: interpolation, separate cost/dual values, limit 2/d (d=2)')
    print('Resources:', {'seconds':time.monotonic()-start,
          'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'nice':os.getpriority(os.PRIO_PROCESS,0)})


if __name__ == '__main__':
    main()

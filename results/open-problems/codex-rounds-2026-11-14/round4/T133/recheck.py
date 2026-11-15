#!/usr/bin/env python3
"""Independent small-interval check by scalar Neumann quadrature."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import math, resource, signal, time
import mpmath as mp
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (120,120))
mp.mp.dps = 40
start = time.monotonic()

def coeff(g,u,t):
    d=mp.pi-g; T=d-u
    a=lambda s: mp.sin(g)/(2*mp.pi*(mp.cos(s-u)+mp.cos(g)))
    b=lambda s: a(-s)
    e=lambda s: (mp.sin(T)/(2*mp.pi*(mp.cos(s)-mp.cos(T)))
        -mp.sin(mp.pi*T/d)/(2*d*(mp.cos(mp.pi*s/d)-mp.cos(mp.pi*T/d))))
    av=[mp.diff(a,t,j) for j in range(4)]
    bv=[mp.diff(b,t,j) for j in range(4)]
    ev=[mp.diff(e,t,j) for j in range(4)]
    W=av[0]*bv[1]-av[1]*bv[0]
    x=(ev[0]*bv[1]-ev[1]*bv[0])/W
    y=(av[0]*ev[1]-av[1]*ev[0])/W
    C=x*av[2]+y*bv[2]-ev[2]; D=x*av[3]+y*bv[3]-ev[3]
    x2=(C*bv[1]/2-D*bv[0]/6)/W
    y2=(D*av[0]/6-C*av[1]/2)/W
    return tuple(map(float,(x,y,x2,y2,C,W)))

def functional(B,g,u,t,x,y):
    # Composite two-point Gauss rule, scalar Neumann iteration.
    n=96; w=2*B/n
    s=[-B+(2*j+1+v/math.sqrt(3))*w for j in range(n//2) for v in (-1,1)]
    k=lambda z: math.sin(2*g)/(2*math.pi*(math.cosh(z)-math.cos(2*g)))
    M=[[w*k(v-z) for z in s] for v in s]
    rho=[1.]*n
    for it in range(80):
        new=[1+sum(v*r for v,r in zip(row,rho)) for row in M]
        if max(abs(a-b) for a,b in zip(new,rho))<2e-16:
            rho=new; break
        rho=new
    import cmath
    d=math.pi-g; T=d-u; h=math.pi/d
    A=lambda z: math.sin(g)/(2*math.pi*(cmath.cosh(z)+math.cos(g)))
    L=lambda z: (math.sin(T)/(2*math.pi*(cmath.cosh(z)-math.cos(T)))
        -math.sin(h*T)/(2*d*(cmath.cosh(h*z)-math.cos(h*T))))
    return w*sum((x*A(z+1j*(t-u))+y*A(z+1j*(t+u))-L(z+1j*t))*r
                 for z,r in zip(s,rho)).real

if __name__=='__main__':
    for g,fu,ft in ((.4,.3,-.4),(math.pi/2,.5,0),(2.4,.3,-.2)):
        d=math.pi-g; u=fu*d; t=ft*(d-u)
        x,y,x2,y2,C,W=coeff(g,u,t)
        # Finite differences of the independently integrated functional.
        errors=[]
        for B in (.008,.004):
            xx=x+B*B*x2; yy=y+B*B*y2
            h=B*1e-3; ht=1e-5
            db=(functional(B+h,g,u,t,xx,yy)-functional(B-h,g,u,t,xx,yy))/(2*h)
            dt=(functional(B,g,u,t+ht,xx,yy)-functional(B,g,u,t-ht,xx,yy))/(2*ht)
            errors.append((db,dt))
        assert abs(errors[-1][0])<abs(errors[0][0])/5+1e-11
        assert abs(errors[-1][1])<abs(errors[0][1])/5+1e-11
        print('gamma=%.8g C=%.10g W=%.10g residuals=%s'%(g,C,W,errors))
    # Exact independent free-fermion identity.
    x,y,x2,y2,C,W=coeff(mp.pi/2,mp.pi/4,mp.mpf(0))
    assert abs(x-(.5-1/(2*math.sqrt(2))))<1e-15
    assert abs(x2-1/(4*math.sqrt(2)))<1e-15
    print('PASS exact free-fermion base and quadratic coefficient')
    print('elapsed_seconds',time.monotonic()-start,'peak_rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'nice',os.getpriority(os.PRIO_PROCESS,0))

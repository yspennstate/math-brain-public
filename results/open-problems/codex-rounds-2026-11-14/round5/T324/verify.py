"""Consistency checks for the noisy-group proof. Standard library, one thread.

These floating-point checks are not numerical certificates. All output stays
beside this script; the proof does not rely on the simulations.
"""
import json
import math
import os
from pathlib import Path
import random
import resource
import sys
import time

ROOT = Path(__file__).resolve().parent
K = 2 + 2/(-math.expm1(-0.5))


def velocity(beta, positions):
    # Remove exp(beta) using a different expression for 1-cos(d).
    out = []
    for theta in positions:
        weights = [math.exp(-2*beta*math.sin((phi-theta)/2)**2)
                   for phi in positions]
        out.append(math.fsum(z*math.sin(phi-theta)
                            for z,phi in zip(weights,positions))/math.fsum(weights))
    return out


def gap(y, na):
    return math.fsum(y[na:])/(len(y)-na)-math.fsum(y[:na])/na


def width(y, na):
    return max(max(y[:na])-min(y[:na]), max(y[na:])-min(y[na:]))


def initial(na, nb, w, x=1.2):
    y = []
    for n, center in ((na,0),(nb,x)):
        y += [center+(i/(n-1)-0.5)*w if n>1 else center for i in range(n)]
    return y


def atom_drift(beta,s,p):
    e = math.exp(-2*beta*math.sin(s/2)**2)
    q = 1-p
    return math.sin(s)*(q*e/(p+q*e)+p*e/(q+p*e))


def simpson(f,a,b,n=16384):
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*math.fsum(f(a+i*h) for i in range(1,n,2))
                +2*math.fsum(f(a+i*h) for i in range(2,n,2)))


def heun(beta,y,dt,noise):
    before = velocity(beta,y)
    pred = [z+dt*v+dw for z,v,dw in zip(y,before,noise)]
    after = velocity(beta,pred)
    return [z+0.5*dt*(v+w)+dw for z,v,w,dw in zip(y,before,after,noise)]


def center_covariances():
    rng = random.Random(32405)
    rows = []
    for na,nb in ((1,1),(2,3),(3,7),(10,10)):
        chi = 1/na+1/nb
        coeff = [-1/na]*na+[1/nb]*nb
        generator_value = math.fsum(c*c for c in coeff)
        assert abs(generator_value-chi)<1e-14
        samples = 20000
        total = total2 = cross = residual2 = 0.0
        for _ in range(samples):
            zs = [rng.gauss(0,1) for _ in coeff]
            center = math.fsum(c*z for c,z in zip(coeff,zs))
            # One within-group Brownian residual; identically zero for a singleton.
            residual = zs[0]-math.fsum(zs[:na])/na
            total += center
            total2 += center*center
            cross += center*residual
            residual2 += residual*residual
        variance = total2/samples-(total/samples)**2
        assert abs(variance/chi-1)<0.05
        covariance = cross/samples
        assert abs(covariance) < 0.04*math.sqrt(chi)
        rows.append(dict(na=na,nb=nb,chi=chi,empirical_variance=variance,
                         relative_error=abs(variance/chi-1),
                         center_residual_covariance=covariance))
    return rows


def residual_checks():
    rng = random.Random(32406)
    rows = []
    for na,nb in ((2,3),(3,7),(1,4)):
        p, q = na/(na+nb), nb/(na+nb)
        for beta in (20,80,320):
            for s in (0.4,1.2,2.8):
                for width_factor in (0.05,0.5,1.0):
                    w0=width_factor/beta
                    y=[]
                    for n,c in ((na,0.0),(nb,s)):
                        raw=[rng.uniform(-0.5,0.5) for _ in range(n)]
                        average=math.fsum(raw)/n
                        y += [c+w0*(z-average) for z in raw]
                    w=width(y,na)
                    actual_gap=gap(y,na)
                    velocities=velocity(beta,y)
                    drift=gap(velocities,na)
                    h=atom_drift(beta,actual_gap,p)
                    eps=max(p/q,q/p)*math.exp(
                        -beta*(math.cos(w)-math.cos(actual_gap-2*w)))
                    # This bound retains finite-parameter factors before
                    # replacing them by the unspecified constant in (9).
                    rel=max(math.exp(4*beta*w)*(1+2*w/math.sin(actual_gap))-1,
                            1-math.exp(-4*beta*w)*(1-2*w/math.sin(actual_gap)))
                    bound=math.exp(1/8)*beta*(w**3+eps*w*w)+h*rel
                    residual=abs(drift+h)
                    assert residual<=bound+2e-15
                    lower=math.sin(actual_gap)*math.exp(
                        -beta*(1-math.cos(actual_gap)))
                    eps_over_h_bound=max(p/q,q/p)/math.sin(actual_gap)*math.exp(2.5)
                    assert h>=lower*(1-1e-12)
                    assert eps/h<=eps_over_h_bound*(1+1e-12)
                    rows.append(dict(na=na,nb=nb,beta=beta,gap=s,width=w,
                                     absolute_residual=residual,bound=bound,
                                     residual_over_bound=residual/bound))
    return rows


def block_response_checks():
    # Kicked equations have an exact exponential flow between jumps. This is
    # a pathwise check, including adapted damping and sign-changing differences.
    rng=random.Random(32407)
    worst=0.0
    for trial in range(20):
        u=0.01
        d0=0.02*(-1 if trial%2 else 1)
        d=d0
        t=0.0
        dt=0.01
        for block in range(30):
            raw=[0.0]
            for _ in range(100):
                raw.append(raw[-1]+rng.gauss(0,math.sqrt(dt)))
            maximum=max(map(abs,raw))
            path=[z*u/maximum for z in raw]
            for j in range(100):
                coefficient=-0.5-0.5*math.sin(20*d)**2
                d=d*math.exp(coefficient*dt)+(path[j+1]-path[j])
                t+=dt
                envelope=abs(d0)*math.exp(-t/2)+K*u
                assert abs(d)<=envelope+1e-14
                worst=max(worst,abs(d)/envelope)
    return dict(K=K,worst_fraction_of_envelope=worst,trials=20,blocks=30)


def high_beta_paths():
    beta,nu,dt,na,nb,T=500,1e-9,0.01,2,3,20
    barw=1/(3*math.sqrt(beta))
    w0,u=0.002,0.0005
    eps=max(na/nb,nb/na)*math.exp(
        -beta*(math.cos(barw)-math.cos(0.2)))
    sufficient=-1+(beta+0.5)*barw**2+(beta+2)*eps
    assert sufficient < -0.5
    assert w0+K*u<barw
    M=na*(na-1)//2+nb*(nb-1)//2
    bound=4*M*math.ceil(T)*math.exp(-u*u/(8*nu))
    rng=random.Random(32408)
    max_width=max_grid_pair=0.0
    exits=0
    for trial in range(12):
        y=initial(na,nb,w0)
        brown=[0.0]*(na+nb)
        for j in range(round(T/dt)):
            if j%round(1/dt)==0:
                block_origin=list(brown)
            increments=[math.sqrt(2*nu*dt)*rng.gauss(0,1) for _ in y]
            brown=[z+dz for z,dz in zip(brown,increments)]
            y=heun(beta,y,dt,increments)
            t=(j+1)*dt
            observed=width(y,na)
            max_width=max(max_width,observed)
            for group in (range(na),range(na,na+nb)):
                for i in group:
                    for k in group:
                        max_grid_pair=max(max_grid_pair,abs(
                            (brown[i]-block_origin[i])-(brown[k]-block_origin[k])))
            assert observed <= w0*math.exp(-t/2)+K*u
            if not 0.4<gap(y,na)<1.6:
                exits+=1
                break
    assert exits==0
    return dict(beta=beta,nu=nu,dt=dt,T=T,trials=12,
                sufficient_derivative_bound=sufficient,
                predicted_failure_bound=bound,max_width=max_width,
                max_grid_pair_increment=max_grid_pair,u=u)


def merging_paths():
    rng=random.Random(32409)
    na,nb=2,3
    p=na/(na+nb)
    rows=[]
    for beta in (10,14):
        nu=math.exp(-1.4*beta)
        dt=0.02
        scalar=simpson(lambda s:1/atom_drift(beta,s,p),0.4,1.2)
        for trial in range(4):
            fine=initial(na,nb,0.05/beta)
            coarse=list(fine)
            coarse_pending=[0.0]*len(fine)
            fine_hit=coarse_hit=None
            t=0.0
            for j in range(100000):
                inc=[math.sqrt(2*nu*dt)*rng.gauss(0,1) for _ in fine]
                if fine_hit is None:
                    before=gap(fine,na)
                    nxt=heun(beta,fine,dt,inc)
                    after=gap(nxt,na)
                    if after<=0.4:
                        fine_hit=t+dt*(before-0.4)/(before-after)
                    fine=nxt
                coarse_pending=[z+dz for z,dz in zip(coarse_pending,inc)]
                if j%2==1:
                    if coarse_hit is None:
                        before=gap(coarse,na)
                        nxt=heun(beta,coarse,2*dt,coarse_pending)
                        after=gap(nxt,na)
                        if after<=0.4:
                            coarse_hit=t-dt+2*dt*(before-0.4)/(before-after)
                        coarse=nxt
                    coarse_pending=[0.0]*len(fine)
                t+=dt
                if fine_hit is not None and coarse_hit is not None:
                    break
            assert fine_hit is not None and coarse_hit is not None
            mesh_error=abs(fine_hit/coarse_hit-1)
            assert mesh_error<2e-4
            # Only a moderate-beta consistency check of very weak noise.
            assert abs(fine_hit/scalar-1)<0.05
            rows.append(dict(beta=beta,nu=nu,trial=trial,
                             fine_hitting=fine_hit,coarse_hitting=coarse_hit,
                             scalar_hitting=scalar,token_over_scalar=fine_hit/scalar,
                             coupled_mesh_error=mesh_error))
    return rows


def parameter_audit():
    rows=[]
    for x in (0.001,0.2,1.2,2.8,3.13):
        ax=2*math.sin(x/2)**2
        for margin in (0.0001,0.1,2.0):
            r0=ax*(1+margin)
            aL=(ax+min(r0,2))/2
            L=math.acos(1-aL)
            kappa=(aL/3+min(r0/2,1))/2
            H=(ax+r0)/2
            gamma=(r0-H)/4
            assert x<L<math.pi
            assert 2*kappa<r0 and 3*kappa>aL and kappa<1
            assert ax<H and H+2*gamma<r0
            rows.append(dict(x=x,r0=r0,L=L,kappa=kappa,H=H,gamma=gamma))
    return rows


def independent_exit_audit():
    # Independent Ito calculation for exp(D^2/(16 nu)).
    maximum = -float('inf')
    error = 0.0
    for coefficient in (-1.0,-0.75,-0.5):
        for i in range(1001):
            z=i/10
            nu=0.01
            d=math.sqrt(z*nu)
            f=math.exp(d*d/(16*nu))
            first=d*f/(8*nu)
            second=(1/(8*nu)+d*d/(64*nu*nu))*f
            direct=coefficient*d*first+2*nu*second
            algebra=(0.25+(coefficient/8+1/32)*z)*math.exp(z/16)
            error=max(error,abs(direct-algebra))
            assert direct<=0.25+1e-12
            assert abs(direct-algebra)<=1e-10
            maximum=max(maximum,direct)
    return dict(maximum_LF=maximum,max_algebra_error=error,
                exponent_denominator=16)


def main():
    started=time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    assert os.getpriority(os.PRIO_PROCESS,0)>=15
    for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
        assert os.environ.get(key)=='1'
    results={}
    for name,check in (
        ('center_covariances',center_covariances),
        ('drift_residuals',residual_checks),
        ('block_response',block_response_checks),
        ('parameter_choices',parameter_audit),
        ('independent_exit',independent_exit_audit),
        ('high_beta_widths',high_beta_paths),
        ('merging_paths',merging_paths)):
        results[name]=check()
        print(name+': passed',flush=True)
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    assert peak<1024
    results['resources']=dict(elapsed_seconds=time.monotonic()-started,
                              peak_rss_mib=peak,
                              effective_nice=os.getpriority(os.PRIO_PROCESS,0))
    (ROOT/'verification.json').write_text(json.dumps(results,indent=2)+'\n')
    print('K:',K)
    print('Maximum center variance relative sampling error:',
          max(z['relative_error'] for z in results['center_covariances']))
    print('Maximum exact drift residual / explicit bound:',
          max(z['residual_over_bound'] for z in results['drift_residuals']))
    print('High-beta width check:',json.dumps(results['high_beta_widths']))
    for row in results['merging_paths']:
        print('Merging:',json.dumps(row))
    print('All checks passed:',json.dumps(results['resources']),flush=True)


if __name__=='__main__':
    main()

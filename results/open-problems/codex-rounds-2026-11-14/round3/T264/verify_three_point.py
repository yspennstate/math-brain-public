#!/usr/bin/env python3
"""Standard-library checks: continuous atom pricing and direct risk integration.

Run under nice -n 15 with OMP_NUM_THREADS=1. Writes verification_data.json.
"""
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(90)
resource.setrlimit(resource.RLIMIT_CPU, (75,75))
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
pi = math.pi
TAU = 2*pi


def dot(u,v):
    return math.fsum(x*y for x,y in zip(u,v))


def relu(t):
    return max(t,0.0)


def evaluate(atoms,x):
    return math.fsum(c*relu(dot(z,x)) for c,z in atoms)


def risk_circle(atoms, steps=65536):
    return math.fsum(evaluate(atoms,(math.cos(TAU*(j+.5)/steps),
                                   math.sin(TAU*(j+.5)/steps)))**2
                     for j in range(steps))/steps


def kernel(u,v,d):
    # Gaussian polar integral, used only in the formula side of comparisons.
    beta=math.acos(max(-1.0,min(1.0,dot(u,v))))
    return (math.sin(beta)+(pi-beta)*math.cos(beta))/(2*pi*d)


def risk_atoms(atoms,d):
    return math.fsum(c*t*kernel(u,v,d)
                     for c,u in atoms for t,v in atoms)


def solve3(matrix,rhs):
    # Recover multipliers from three linear equations independently of formulas.
    aug=[list(row)+[value] for row,value in zip(matrix,rhs)]
    for k in range(3):
        p=max(range(k,3),key=lambda j:abs(aug[j][k]))
        aug[k],aug[p]=aug[p],aug[k]
        scale=aug[k][k]
        assert abs(scale)>1e-12
        aug[k]=[v/scale for v in aug[k]]
        for j in range(3):
            if j!=k:
                factor=aug[j][k]
                aug[j]=[v-factor*w for v,w in zip(aug[j],aug[k])]
    return tuple(row[-1] for row in aug)


def price(X,lam):
    # Exact continuous pricing: activation boundaries and every arc's stationary
    # directions. This does not use the proposed atoms or the case analysis.
    breaks={0.0,TAU}
    for x in X:
        angle=math.atan2(x[1],x[0])
        for shift in (-pi/2,pi/2):
            breaks.add((angle+shift)%TAU)
    breaks=sorted(breaks)
    candidates=list(breaks)
    for lo,hi in zip(breaks,breaks[1:]):
        mid=(lo+hi)/2
        z=(math.cos(mid),math.sin(mid))
        active=[i for i,x in enumerate(X) if dot(x,z)>0]
        slope=tuple(math.fsum(lam[i]*X[i][k] for i in active)
                    for k in range(2))
        angle=math.atan2(slope[1],slope[0])%TAU
        for stationary in (angle,(angle+pi)%TAU):
            if lo<=stationary<=hi:
                candidates.append(stationary)
    def val(phi):
        z=(math.cos(phi),math.sin(phi))
        return math.fsum(t*relu(dot(x,z)) for t,x in zip(lam,X))
    vals=[(abs(val(phi)),phi,val(phi)) for phi in candidates]
    return max(vals),len(candidates)


def construct(theta,tau):
    a,b=math.cos(theta/2),math.sin(theta/2)
    s=2*a*b
    X=((a,b),(a,-b),(0.0,1.0))
    v=(b,-a)
    if tau==1:
        W=((1-b)/a,1.0)
        L=math.hypot(*W)
        C=(1-b)/(a*b)
        r=tuple(t/L for t in W)
        atoms=((L,r),(-C,v))
        lam=(1/s+L/2,-1/s,L/2-1/a)
        # Interior exposed r: gradient equals r. Negative exposed v: value=-1.
        matrix=[tuple(x[k] for x in X) for k in range(2)]
        matrix.append(tuple(relu(dot(x,v)) for x in X))
        recovered=solve3(matrix,(r[0],r[1],-1))
    else:
        C,D=a/b,(1+b)/a
        atoms=((1.0,X[0]),(-C,v),(-D,(-b,a)))
        lam=(1+1/s,-1/s,-1/a)
        matrix=[tuple(relu(dot(x,z)) for x in X) for c,z in atoms]
        recovered=solve3(matrix,(1,-1,-1))
    return X,atoms,lam,recovered


data={'earlier_checks':[],'three_point_checks':[]}
# Earlier result: independently integrate actual network at acute and obtuse angles.
for th in (.001,.04,.7,pi/2,2.2,3.13):
    a,b=math.cos(th/2),math.sin(th/2)
    X=((a,b),(a,-b))
    if th<=pi/2:
        atoms=((1/math.sin(th),(b,a)),(-1/math.sin(th),(b,-a)))
        exact=(pi-math.sin(th)+th*math.cos(th))/(2*pi*math.sin(th)**2)
    else:
        atoms=((1.0,X[0]),(-1.0,X[1]))
        exact=(pi-math.sin(th)-(pi-th)*math.cos(th))/(2*pi)
    direct=risk_circle(atoms)
    relative=abs(direct/exact-1)
    assert relative<2e-8,(th,direct,exact,relative)
    data['earlier_checks'].append({'theta':th,'risk_circle':direct,
                                   'earlier_formula':exact,'relative_error':relative})
print('PASS: earlier exact two-point risk, independent scalar integration')

max_price_error=0.0
max_risk_error=0.0
for theta in (1e-4,.002,.03,.2,.6,1.0,pi/3-1e-6):
    for tau in (1,-1):
        X,atoms,lam,recovered=construct(theta,tau)
        y=(1,-1,tau)
        interp=max(abs(evaluate(atoms,x)-v) for x,v in zip(X,y))
        assert interp<2e-10,(theta,tau,interp)
        recovered_error=max(abs(x-y)/max(1,abs(y)) for x,y in zip(recovered,lam))
        assert recovered_error<1e-9
        cost=math.fsum(abs(c) for c,z in atoms)
        dual=dot(lam,y)
        assert abs(cost/dual-1)<1e-12
        priced,count=price(X,lam)
        pricing_error=abs(priced[0]-1)
        max_price_error=max(max_price_error,pricing_error)
        assert pricing_error<1e-10,(theta,tau,priced)
        direct=risk_circle(atoms)
        exact=risk_atoms(atoms,2)
        relative=abs(direct/exact-1)
        max_risk_error=max(max_risk_error,relative)
        assert relative<3e-8,(theta,tau,direct,exact,relative)
        # Separate closed formulas, including the antipodal atom cancellation.
        a,b=math.cos(theta/2),math.sin(theta/2)
        if tau==-1:
            C,D=a/b,(1+b)/a
            closed=(1+C*C+D*D)/4-(C+D)/(2*pi)
        else:
            L=math.sqrt(2/(1+b)); C=(1-b)/(a*b)
            beta=math.acos(-math.sqrt((1-b)/2))
            closed=(L*L+C*C)/4-L*C*(math.sin(beta)+(pi-beta)*math.cos(beta))/(2*pi)
        assert abs(closed/exact-1)<3e-12
        odd_vector=tuple(math.fsum(c*z[k] for c,z in atoms) for k in range(2))
        odd=sum(t*t for t in odd_vector)/8
        assert odd<=exact*(1+1e-12)
        if tau==1:
            assert abs(odd*8*b*b-1)<2e-12
        if theta==1e-4:
            assert abs(theta*theta*direct-1)<3e-4
            assert abs(theta*theta*odd-.5)<3e-4
        # Uniform convergence sampled on a disk; analytic bound in PROOF.md.
        uniform=max(abs(theta*evaluate(atoms,(math.cos(TAU*j/4096),math.sin(TAU*j/4096)))
                        +2*relu(-math.sin(TAU*j/4096))) for j in range(4096))
        if theta==1e-4:
            assert uniform<5e-4
        row={'theta':theta,'tau':tau,'cost':cost,'dual_value':dual,
             'interpolation_error':interp,'recovered_dual_error':recovered_error,
             'continuous_price':priced[0],'pricing_candidates':count,
             'risk_direct_d2':direct,'risk_formula_d2':closed,
             'risk_relative_error':relative,'theta_squared_risk_d2':theta*theta*direct,
             'theta_squared_odd_risk_d2':theta*theta*odd,
             'sampled_uniform_limit_error':uniform}
        data['three_point_checks'].append(row)
        if theta in (1e-4,.03,.2,1.0):
            print(f'theta={theta:g} tau={tau:+d} Q={cost:.12g} theta^2*R2={theta*theta*direct:.12g} theta^2*oddR2={theta*theta*odd:.12g}')
print(f'PASS: interpolation, recovered multipliers, primal=dual, continuous pricing (max error {max_price_error:.3g})')
print(f'PASS: independent circle risk vs closed and kernel formulas (max relative error {max_risk_error:.3g})')

# Independent S^2 surface integral: coordinate z is uniform and angle is uniform.
X,atoms,_,_=construct(.2,-1)
Nz,Nphi=256,2048
def sphere_terms():
    for j in range(Nz):
        altitude=-1+2*(j+.5)/Nz
        rad=math.sqrt(1-altitude*altitude)
        for k in range(Nphi):
            ph=TAU*(k+.5)/Nphi
            yield evaluate(atoms,(rad*math.cos(ph),rad*math.sin(ph)))**2
sphere_direct=math.fsum(sphere_terms())/(Nz*Nphi)
sphere_exact=risk_atoms(atoms,3)
assert abs(sphere_direct/sphere_exact-1)<3e-5
print(f'PASS: S^2 direct surface integral {sphere_direct:.12g}, formula {sphere_exact:.12g}')
data['sphere3']={'direct':sphere_direct,'formula':sphere_exact}

# Try to falsify the stated domain: blindly extending f+ beyond theta=pi/3 fails.
X,atoms,_,_=construct(1.2,1)
outside_error=abs(evaluate(atoms,X[1])+1)
assert outside_error>.1
print(f'PASS: out-of-domain theta=1.2 candidate fails interpolation by {outside_error:.12g}; restriction is necessary for this formula')
data['out_of_domain_interpolation_error']=outside_error

rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes=rss if sys.platform=='darwin' else 1024*rss
assert rss_bytes<1_000_000_000
stats={'elapsed_seconds':time.monotonic()-started,'peak_rss_bytes':rss_bytes,
       'nice':os.getpriority(os.PRIO_PROCESS,0),'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS']}
data['resources']=stats
(ROOT/'verification_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('All assertions passed.')
print('Resources:',stats)

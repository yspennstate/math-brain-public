"""Finite checks for the collision law. No diffusion simulation.
Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit_collision.py
"""
from fractions import Fraction as F
import math
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
print("nice", os.getpriority(os.PRIO_PROCESS, 0))

def ball(j):
    return math.pi**(j/2)/math.gamma(1+j/2)

def simpson(f, n=4096):
    h = math.pi/(2*n)
    return h/3*(f(0)+f(math.pi/2)+sum(
        (4 if k%2 else 2)*f(k*h) for k in range(1,n)))

flux_error = moment_error = 0.0
for d in range(2,13):
    projected = ball(d-1)/(d*ball(d))
    sphere_ratio = math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d-1)/2))
    raw = simpson(lambda t: math.cos(t)*math.sin(t)**(d-2))
    angular = sphere_ratio*raw
    flux_error = max(flux_error, abs(projected-angular))
    assert abs(projected-angular) < 3e-12
    assert abs(2*angular-2*projected) < 6e-12
    # Uniform impact point in the (d-1)-ball gives E radius^2=(d-1)/(d+1).
    projected_mu2 = 1-(d-1)/(d+1)
    angular_mu2 = simpson(
        lambda t: math.cos(t)**3*math.sin(t)**(d-2))/raw
    moment_error = max(moment_error,abs(projected_mu2-angular_mu2))
    assert abs(projected_mu2-angular_mu2) < 3e-12
    assert math.isclose(4*projected_mu2,8/(d+1),rel_tol=2e-14)
print("single-hemisphere flux d=2..12: projection vs angular max error %.3g" % flux_error)
print("cosine-law E[mu^2]=2/(d+1): impact-ball vs angular max error %.3g" % moment_error)
assert math.isclose(ball(1)/(2*ball(2)),1/math.pi,rel_tol=1e-14)
assert math.isclose(ball(2)/(3*ball(3)),1/4,rel_tol=1e-14)
print("d=2 flux 1/pi; d=3 flux 1/4; whole-sphere absolute flux is twice these")

# Two independent all-vacancy normalizations: exposed area / vacant volume,
# and derivative at zero of the exact conditional sausage void probability.
rate_error = derivative_error = 0.0
for d in range(2,9):
    for lam,r in ((0.03,0.2),(0.23,0.7),(1.1,1.0)):
        p0=math.exp(-lam*ball(d)*r**d)
        area=lam*d*ball(d)*r**(d-1)*p0
        c=ball(d-1)/(d*ball(d))
        area_rate=c*area/p0
        shadow_rate=lam*ball(d-1)*r**(d-1)
        rate_error=max(rate_error,abs(area_rate/shadow_rate-1))
        assert math.isclose(area_rate,shadow_rate,rel_tol=3e-14)
        h=1e-7/shadow_rate
        derivative=-math.expm1(-shadow_rate*h)/h
        derivative_error=max(derivative_error,abs(derivative/shadow_rate-1))
        assert abs(derivative/shadow_rate-1)<6e-8
        for ratio in (1.0,1.2,10.0,1e6):
            theta=p0/ratio
            T=(1+math.log(ratio))/shadow_rate
            survival_bound=math.exp(math.log(ratio)-shadow_rate*T)
            lower1=(1-survival_bound)/T
            lower2=(1-math.exp(-1))*shadow_rate/(1+math.log(ratio))
            assert math.isclose(survival_bound,math.exp(-1),rel_tol=4e-14)
            assert math.isclose(lower1,lower2,rel_tol=4e-14)
            upper=shadow_rate*p0/theta
            assert 0<lower2<=upper
print("all-vacancy rate: exposed area vs shadow max relative error %.3g" % rate_error)
print("independent first-flight derivative max relative error %.3g" % derivative_error)
print("positive lower-bound substitution and upper/lower consistency PASS")

# Exact finite-time Campbell check on periodic point processes with a uniform
# time phase. This includes a nonergodic mixture and unequal flight lengths.
def phase_average(gaps,T,power):
    cycle=sum(gaps,F(0))
    epochs=[]
    e=F(0)
    for gap in gaps:
        epochs.append(e)
        e+=gap
    cuts={F(0),cycle}
    for e in epochs:
        cuts.add(e%cycle)
        cuts.add((e-T)%cycle)
    cuts=sorted(cuts)
    average=F(0)
    for left,right in zip(cuts,cuts[1:]):
        phase=(left+right)/2
        count=F(0)
        for e,gap in zip(epochs,gaps):
            # This bounded range contains every event for the chosen T.
            for k in range(-2,25):
                if 0<e+k*cycle-phase<=T:
                    count+=gap**power
        average+=(right-left)*count/cycle
    return average

types=((F(2,5),(F(1),F(3))),
       (F(3,5),(F(1,2),F(1,2),F(1,2),F(3,2))))
gamma=F(0)
palm_length_numerator=F(0)
volume_weighted_event_mean=F(0)
volume_waiting=F(0)
for weight,gaps in types:
    cycle=sum(gaps,F(0))
    intensity=F(len(gaps),1)/cycle
    gamma+=weight*intensity
    palm_length_numerator+=weight*intensity*cycle/len(gaps)
    volume_weighted_event_mean+=weight*cycle/len(gaps)
    volume_waiting+=weight*sum((x*x for x in gaps),F(0))/(2*cycle)
    for T in (F(1,7),F(5,4),F(17,3)):
        for power in (0,1,2):
            actual=phase_average(gaps,T,power)
            expected=T*sum((gap**power for gap in gaps),F(0))/cycle
            assert actual==expected,(gaps,T,power,actual,expected)
palm_length=palm_length_numerator/gamma
assert gamma==1
assert palm_length==1/gamma
assert volume_weighted_event_mean==F(5,4)
assert volume_waiting==F(4,5)
print("exact rational marked Campbell tests: two periodic laws, 3 windows, 3 marks PASS")
print("nonergodic mixture: rate=%s; Palm mean flight=%s; product=%s" %
      (gamma,palm_length,gamma*palm_length))
print("different samplings: volume-weighted event mean=5/4; forward waiting mean=4/5")

# Independent face-slab proof of the surface-count squeeze limit.
for d in range(2,13):
    for q in (0.5,0.1,0.001):
        outer=(1+q)**d
        inner=(1-q)**d
        assert inner<=1<=outer
        assert outer-1<=d*q*(1+q)**(d-1)*(1+1e-13)
        assert 1-inner<=d*q*(1+1e-13)
print("inner/outer spatial count squeeze: face-slab checks PASS")
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform!="darwin":
    rss*=1024
assert rss<1024**3
elapsed=time.monotonic()-started
assert elapsed<20*60
print("peak resident bytes",rss)
print("PASS; elapsed %.3f seconds" % elapsed)

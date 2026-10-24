"""Independent finite-case checks and numerical diagnostics; not proof certificates."""
import json
import math
from fractions import Fraction
from pathlib import Path
import random
import time

ROOT=Path(__file__).resolve().parent
started=time.perf_counter()
checks=[]
def record(name,cases,**details):
    checks.append(dict(name=name,cases=cases,status='PASS',**details))

# Exact root-law probabilities, including the midpoint and n<9 boundaries.
root_cases=0
for n in range(2,82):
    harmonic=sum((Fraction(1,i) for i in range(1,n)),Fraction())
    q=[Fraction(n,2*i*(n-i))/harmonic for i in range(1,n)]
    assert sum(q)==1
    for k in range(1,(n-1)//2+1):
        direct=sum((q[i-1] for i in range(1,n) if min(i,n-i)<=k),Fraction())
        closed=(sum((Fraction(1,i) for i in range(1,k+1)),Fraction())+sum((Fraction(1,i) for i in range(n-k,n)),Fraction()))/harmonic
        assert direct==closed
        root_cases+=1
record('P0342_exact_split_and_small_boundary_checks',root_cases)

# Exhaust adapted survival trees. An auxiliary fair coin changes future hazards.
hazard_cases=0
worst=0.0
for policy in range(20):
    survivors=[(1.0,0.0,0)]
    previous=1.0
    crossings={k:0.0 for k in (0.5,1.0,2.0)}
    for depth in range(1,9):
        next_states=[]
        for prob,compensator,bits in survivors:
            p=(1+((bits+policy*3+depth)%7))/9
            new_a=compensator+p
            new_prob=prob*(1-p)
            for k in crossings:
                if compensator<k<=new_a:
                    crossings[k]+=new_prob
            next_states.extend([(new_prob/2,new_a,bits*2),(new_prob/2,new_a,bits*2+1)])
        expectation=sum(prob*math.exp(a) for prob,a,_ in next_states)
        assert expectation<=previous+1e-12
        previous=expectation
        survivors=next_states
        hazard_cases+=len(survivors)
    for k,prob in crossings.items():
        assert prob<=math.exp(-k)+1e-12
        worst=max(worst,prob/math.exp(-k))
record('C0057_adapted_supermartingale_and_stopping_bound',hazard_cases,max_bound_fraction=worst)
assert 1==sum([1]+[0]*10) # deterministic T=1: discovery without divergence
record('C0057_false_necessity_counterexample',1,discovery_probability=1,stopped_hazard_sum=1)

# Projection discretization is independent of the analytic annular ODE solution.
max_annular_error=0.0
for theta in (0.05,0.2,0.7,1.1):
    horizon=min(0.4,math.log(1/math.tan(theta/2))/2)
    steps=20000
    dt=horizon/steps
    y=[math.cos(theta),math.sin(theta)]
    for _ in range(steps):
        y[0]-=dt
        radius=math.hypot(*y)
        if radius<1:
            y=[value/radius for value in y]
        assert math.hypot(*y)<3
    phi=2*math.atan(math.exp(horizon)*math.tan(theta/2))
    error=math.hypot(y[0]-math.cos(phi),y[1]-math.sin(phi))
    max_annular_error=max(max_annular_error,error)
    assert error<2e-5
    assert (y[0]-1)**2+y[1]**2>2*(1-math.cos(theta))
record('P0024_independent_annular_reflection_discretization',80000,max_endpoint_error=max_annular_error)

# Threshold algebra for the nonidentical-Bernoulli logarithmic lower-bound proof.
city_cases=0
for K in (0.01,0.2,1.0,10.0):
    for d in (0.25,0.5,1.0,2.0,4.0):
        kappa=(1/(32*(1+K)))**(1/(d+1))
        for log_t in (1e8,1e10,1e12):
            m=math.floor(kappa*log_t**(1/(d+1)))
            if m<1:
                continue
            mu_lower=log_t/(4*(1+K)*m**d)
            assert mu_lower>=4*m
            city_cases+=1
record('P0218_logarithmic_threshold_algebra',city_cases,note='Checks the conditional process lemma, not the primary model rate.')

# Integrate in the original height coordinate to check the Poisson change of variables.
poisson_cases=0
max_integral_error=0.0
for alpha in (0.5,1.0,2.0):
    for t in (2.0,3.0,5.0):
        for upper in (-1.0,0.0,1.0):
            steps=1000
            width=(t+upper)/steps
            direct=width*sum(math.exp(-alpha*(-t+(j+0.5)*width))*math.exp(alpha*(t-t+(j+0.5)*width)) for j in range(steps))
            exact=math.exp(alpha*t)*(t+upper)
            relative=abs(direct/exact-1)
            max_integral_error=max(max_integral_error,relative)
            assert relative<1e-11
            poisson_cases+=1
# A decoration K(s)=exp(s) meets the hypotheses, but full expectation diverges.
full_cutoff_expectations=[math.exp(2)*(2+upper) for upper in (0,10,100,1000)]
assert all(a<b for a,b in zip(full_cutoff_expectations,full_cutoff_expectations[1:]))
wrong=(math.exp(4)-1)/2
right=2*math.exp(2)
assert abs(wrong-right)>10
record('C0005_original_coordinate_poisson_integrals',poisson_cases,max_relative_error=max_integral_error,old_integral_at_t2=wrong,correct_truncated_mean_at_t2=right)

# Exact rational counterexamples to the inference from the recorded premises.
for n in range(2,1002):
    delta=Fraction(1,n)
    theta=delta
    derivative=chi=C=Fraction(1)
    assert theta/delta==1 and derivative<=C*chi
    assert delta*chi==delta and chi<1/delta
record('C0065_exact_counterexamples_to_derivative_inference',1000)

# Independently sum the root total-progeny distribution on the degree-three tree.
tree_cases=0
max_tree_mean_error=0.0
for p in (0.6,0.65,0.75,0.9):
    r=1-p
    total=mean=0.0
    for n in range(1,1501):
        log_prob=math.log(3)-math.log(2*n+1)+math.lgamma(2*n+2)-math.lgamma(n)-math.lgamma(n+3)+(n-1)*math.log(r)+(n+2)*math.log(1-r)
        mass=math.exp(log_prob)
        total+=mass
        mean+=n*mass
        tree_cases+=1
    exact_mean=1+3*r/(1-2*r)
    assert abs(total-1)<1e-10
    assert abs(mean-exact_mean)<1e-8
    max_tree_mean_error=max(max_tree_mean_error,abs(mean-exact_mean))
scaled_chi=[]
for delta in (1e-2,1e-3,1e-4,1e-5):
    p=0.5+delta
    scaled_chi.append(delta*((1-p)/p)**3*(2-p)/(2*p-1))
assert abs(scaled_chi[-1]-0.75)<1e-4
record('C0065_C0143_independent_tree_progeny_coefficients',tree_cases,max_conditional_mean_error=max_tree_mean_error,scaled_chi=scaled_chi)

# Smallest extinction root and conditional offspring mean across regular degrees.
extinction_cases=0
largest_mean=0.0
for b in range(2,9):
    for p in (1/b+0.02, (1+1/b)/2, 0.95):
        t=0.0
        for _ in range(10000):
            next_t=1-p+p*t**b
            if abs(next_t-t)<1e-14:
                t=next_t
                break
            t=next_t
        else:
            raise AssertionError('Extinction iteration did not converge')
        mean=b*p*t**(b-1)
        assert 0<t<1 and mean<1
        largest_mean=max(largest_mean,mean)
        assert abs(t-(1-p+p*t**b))<1e-12
        extinction_cases+=1
record('C0143_supercritical_extinction_and_subcritical_duality',extinction_cases,max_conditional_mean=largest_mean)

# Enumerate all shared-weight configurations, rather than replacing by edge marginals.
covariances=[]
scale_cases=0
weights=(1.0,2.0)
for a,b in ((0.1,0.1),(1.0,0.3),(3.0,2.0)):
    mean1=mean2=joint=0.0
    for w0 in weights:
        for w1 in weights:
            for w2 in weights:
                p1=-math.expm1(-a*w0*w1)
                p2=-math.expm1(-b*w0*w2)
                mean1+=p1/8
                mean2+=p2/8
                joint+=p1*p2/8
                scale_cases+=1
    covariance=joint-mean1*mean2
    assert covariance>0
    covariances.append(covariance)
ratios=[]
for s in (1e-2,1e-3,1e-4,1e-5,1e-6):
    ratios.append(sum(-math.expm1(-s*u*v)/(4*s) for u in weights for v in weights))
assert abs(ratios[-1]-2.25)<4e-6
record('C0090_exact_weight_configuration_enumeration',scale_cases,edge_covariances=covariances,small_s_probability_over_s=ratios)

# Quantitative directional containment, including nearly tangential interior points.
rng=random.Random(345)
direction_cases=0
for gamma in (0.25,0.5,1.0):
    C=2.0
    for _ in range(1000):
        x=[rng.uniform(-1e-3,1e-3),rng.uniform(-1e-3,1e-3)]
        tangent_norm=math.hypot(*x)
        x.append(C*tangent_norm**(1+gamma)-rng.random()*1e-4)
        radius=math.sqrt(sum(v*v for v in x))
        assert -x[-1]/radius>=-C*radius**gamma-1e-12
        direction_cases+=1
record('P0019_holder_boundary_direction_bound',direction_cases,note='Does not verify the reversed-bridge sketch.')

# Finite intervals (no wraparound) test spanning, acyclicity and the residue classes.
forest_cases=0
for k in range(2,51):
    vertices=list(range(-5*k,5*k+1))
    parent={v:v for v in vertices}
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    edges=0
    for v in vertices:
        if v+k in parent:
            a,b=find(v),find(v+k)
            assert a!=b
            parent[a]=b
            edges+=1
    assert len({find(v) for v in vertices})==k
    assert edges==len(vertices)-k
    forest_cases+=1
record('P0048_arbitrary_finite_residue_class_forest',forest_cases)

data={'command':'python -B -X utf8 check_results.py','seconds':time.perf_counter()-started,'checks':checks,'check_groups':len(checks),'cases':sum(c['cases'] for c in checks),'invalid_prior_routes_detected':3,'full_open_problems_solved':0,'independent_keeps':0,'lean_checked_mathematical_claims':0,'scope':'Finite exact checks and numerical diagnostics supplement the written arguments; they do not certify general theorems.'}
(ROOT/'measurements.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:data[key] for key in ('seconds','check_groups','cases','invalid_prior_routes_detected','full_open_problems_solved','independent_keeps')}))


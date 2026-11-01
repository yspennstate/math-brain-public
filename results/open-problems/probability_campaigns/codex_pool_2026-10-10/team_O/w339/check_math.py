"""Small independent controls for the saved mathematical claims; not a test bank."""
import itertools
import json
import math
import random
import time
from collections import deque
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
report = {'command':'python -X utf8 ~/brain_workers/w339/check_math.py',
          'scope':'local proof controls and numerical diagnostics; no independent audit', 'checks':{}}
started=time.perf_counter()

def save(name, values):
    report['checks'][name]=values
    ROOT.joinpath('measurements.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(name,json.dumps(values),flush=True)

def simpson(f,lo,hi,n=4096):
    h=(hi-lo)/n
    return h*(f(lo)+f(hi)+4*sum(f(lo+h*i) for i in range(1,n,2))+2*sum(f(lo+h*i) for i in range(2,n,2)))/3

# P0267: check the exact Ito constants separately from the archived argument.
c_squared=F(1,2)
bes_dimension=4
cubic_drift=(F(3-bes_dimension,2))/c_squared
diffusion_squared=1/c_squared
assert cubic_drift==-1 and diffusion_squared==2
assert 2*cubic_drift+diffusion_squared==0
assert (2*F(2,3)-1)*(2+1)==1
assert 2-2*1==0  # time-change exponent minus two multiplier exponents
max_error=0.0
for r,S in itertools.product((.3,1.,2.),(.2,1.,3.)):
    k=r*r/(2*S)
    quadrature=simpson(lambda v:math.exp(-k*(1-v))/(2*S),0,1)
    formula=-math.expm1(-k)/(r*r)
    err=abs(quadrature-formula)/formula
    assert err<1e-9
    max_error=max(max_error,err)
log_tail={str(n):-2*math.log(n)-n*n/(4*((math.exp(2)-1)/2)) for n in (1,10,100)}
save('P0267',{'ito_cubic_drift':str(cubic_drift),'ito_diffusion_squared':str(diffusion_squared),
              'critical_energy_coefficient':0,'quadrature_cases':9,'max_relative_error':max_error,
              'squared_maximum_tail_coefficient_logs_T1_a1overn':log_tail,
              'note':'log coefficients remain finite when ordinary floating point underflows; divergence uses the analytic tail limit'})

# C0031: no random matrix theorem is simulated or inferred here.
sv=[]
for n in (100,1000,10000,1000000):
    m=math.floor(n/math.log(n))
    value=m*math.log(n)/n
    assert m/n<1 and 0<value<=1
    sv.append({'n':n,'small_fraction':m/n,'minimum':1/n,'normalized_negative_log':value})
save('C0031',{'diagonal_controls':sv,'limit_negative_log':1,
              'full_sequence_promotion':'not established; almost-sure subsequence proved analytically'})

# C0134: a controlled infinite-stack example, with a provable martingale bound.
rng=random.Random(339)
n=100000
right=sum(rng.random()<.6 for _ in range(n))
speed=(2*right-n)/n
assert abs(speed-.2)<.02
save('C0134',{'constant_cookie_probability':.6,'steps':n,'observed_speed':speed,
              'proved_liminf_lower_bound':.2,'total_cookie_drift':'infinity',
              'finite_delta_ballisticity_criterion':'unproved'})

# P0092: survival recursion of the dependency tree; criticality included.
reset=[]
for b,r in ((2,.6),(3,.8),(2,.5),(2,.25)):
    p=1.
    m=b*(1-r)
    levels=10000 if m==1 else 100
    for level in range(1,levels+1):
        p=(1-r) if p==1 else (1-r)*(-math.expm1(b*math.log1p(-p)))
        if m<1:
            assert p<=m**level+1e-13
    if m==1: assert 0<p<.001
    if m>1: assert abs(p-2/3)<1e-10
    reset.append({'b':b,'reset_probability':r,'dependency_mean':m,'level':levels,'survival_to_level':p})
save('P0092',{'dependency_controls':reset,'critical_claim':'a.s. extinction by generating-function proof; numeric recursion is a control only'})

# P0439: compute response tails directly and also by independent convolution.
def erlang_c(lam,mu,c):
    L=lam/mu
    if c<=L: raise ValueError('unstable')
    term=1.
    denom=term
    for j in range(1,c):
        term*=L/j
        denom+=term
    term*=L/c
    aterm=term/(1-L/c)
    return aterm/(denom+aterm)

def response_tail(lam,mu,c,t):
    C=erlang_c(lam,mu,c)
    a=c*mu-lam
    if abs(a-mu)<1e-12:
        return math.exp(-mu*t)*(1+C*mu*t)
    return math.exp(-mu*t)+C*mu*(math.exp(-mu*t)-math.exp(-a*t))/(a-mu)

qerr=0.
qcases=0
for lam,t in itertools.product((.5,2.,7.),(2.,4.)):
    for c in (math.floor(lam)+1,math.floor(lam)+2):
        C=erlang_c(lam,1,c)
        a=c-lam
        direct=(1-C)*math.exp(-t)+C*(math.exp(-a*t)+simpson(lambda w:a*math.exp(-a*w)*math.exp(-(t-w)),0,t))
        formula=response_tail(lam,1,c,t)
        assert abs(direct-formula)<1e-10
        assert formula>math.exp(-t)
        qerr=max(qerr,abs(direct-formula))
        qcases+=1
tails={c:response_tail(2,1,c,4) for c in range(3,26)}
minimum=next(c for c,tail in tails.items() if tail<=.03)
waiting_only_min=next(c for c in tails if erlang_c(2,1,c)*math.exp(-(c-2)*4)<=.03)
assert minimum==4 and waiting_only_min==3
assert tails[25]-math.exp(-4)<1e-15
bound=F(99,100)*F(1,10)
selector_checks=0
for a0,a1 in itertools.product(range(101),repeat=2):
    success=F(99,100)*F(a0,100)+F(1,100)*F(a1,100)
    if success>=F(99,100):
        cost=F(99,100)*F(a0,100)*F(1,10)+F(1,100)*F(a1,100)*100
        assert cost>=bound
        selector_checks+=1
save('P0439',{'convolution_cases':qcases,'max_convolution_error':qerr,
              'arrival_rate':2,'service_rate':1,'deadline':4,'target_miss_probability':.03,
              'waiting_only_staffing_count_before':waiting_only_min,'response_staffing_count_after':minimum,
              'response_tail_c3':tails[3],'response_tail_c4':tails[4],
              'service_floor':math.exp(-4),'quantile_capacity_integral':str(bound),
              'two_size_selector_controls':selector_checks,
              'scope':'minimum among stable FCFS M/M/c staffing choices only'})

# C0040: exact rational adjoint-density identity on periodic environments.
adjoint_checks=0
drift_examples=[]
for ps in ((F(3,4),),(F(4,5),F(2,3)),(F(3,4),F(4,5),F(2,3)),(F(2,5),F(9,10))):
    size=len(ps)
    rho=[(1-p)/p for p in ps]
    cycle_product=math.prod(rho)
    assert cycle_product<1
    Ss=[]
    for i in range(size):
        numerator=F(1)
        product=F(1)
        for k in range(1,size):
            product*=rho[(i+k-1)%size]
            numerator+=product
        Ss.append(numerator/(1-cycle_product))
    H=[(1+rho[i])*Ss[(i+1)%size] for i in range(size)]
    Z=sum(H)/size
    for i in range(size):
        assert H[i]==ps[(i-1)%size]*H[(i-1)%size]+(1-ps[(i+1)%size])*H[(i+1)%size]
        adjoint_checks+=1
    drift=sum((2*ps[i]-1)*H[i] for i in range(size))/(size*Z)
    assert drift==1/Z
    drift_examples.append({'period':size,'Z':str(Z),'mean_drift':str(drift)})
save('C0040',{'rational_adjoint_identities':adjoint_checks,'periodic_examples':drift_examples,
              'literature_forward_half':'Drewitz-Ramirez Corollary 2.15 checked directly; converse only in cached open question'})

# C0079: exhaustive open-subgraph checks, with independently computed pivotals.
def distance(edges,mask,u,v,vertices):
    adj=[[] for _ in range(vertices)]
    for i,(a,b) in enumerate(edges):
        if mask>>i&1:
            adj[a].append(b); adj[b].append(a)
    todo=deque([(u,0)])
    seen={u}
    while todo:
        a,d=todo.popleft()
        if a==v:return d
        for b in adj[a]:
            if b not in seen:seen.add(b);todo.append((b,d+1))
    return None

graphs=[(2,[(0,1)]),(3,[(0,1),(1,2),(0,2)]),
        (4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(3,0)]),
        (4,list(itertools.combinations(range(4),2)))]
graph_checks=0
for vertices,edges in graphs:
    for mask in range(1<<len(edges)):
        for u,v in itertools.combinations(range(vertices),2):
            d=distance(edges,mask,u,v,vertices)
            if d is None:continue
            piv=sum(bool(mask>>i&1) and distance(edges,mask&~(1<<i),u,v,vertices) is None for i in range(len(edges)))
            assert d>=piv
            graph_checks+=1
assert distance([(0,1)],1,0,1,2)==1
save('C0079',{'connected_subgraph_endpoint_controls':graph_checks,
              'old_plus_one_counterexample':{'distance':1,'bond_pivotal_count':1},
              'correct_tail_direction':'pivotal-tail event is contained in intrinsic-tail event'})

# C0122: fixed-seed Gaussian controls. The proofs do not rest on these estimates.
gaussian=[]
rng=random.Random(12339)
samples=50000
for rho in (.1,.5,.95):
    values=[]
    for _ in range(samples):
        z=rng.gauss(0,1)
        y=rho*z+math.sqrt(1-rho*rho)*rng.gauss(0,1)
        chosen_x=z if y>=0 else -z
        values.append(abs(z)-chosen_x)
    empirical=sum(values)/samples
    variance=sum((d-empirical)**2 for d in values)/(samples-1)
    stderr=math.sqrt(variance/samples)
    target=(1-rho)*math.sqrt(2/math.pi)
    assert abs(empirical-target)<6*stderr
    gaussian.append({'rho':rho,'observed_mean_deficit':empirical,'predicted':target,'standard_error':stderr})
rho=math.exp(-4)
overlaps=[]
for _ in range(samples):
    z=rng.gauss(0,1)
    y=rho*z+math.sqrt(1-rho*rho)*rng.gauss(0,1)
    overlaps.append(1 if z*y>0 else -1)
signed_mean=sum(overlaps)/samples
assert abs(signed_mean-2/math.pi*math.asin(rho))<.03
assert sum(x*x for x in overlaps)/samples==1
save('C0122',{'samples_per_control':samples,'deficit_controls':gaussian,
              'signed_overlap_time':4,'mean':signed_mean,'predicted_mean':2/math.pi*math.asin(rho),
              'second_moment':1,'positive_tail_probability':sum(x==1 for x in overlaps)/samples,
              'short_noise_original_problem':'not settled'})

# P0011: simulate the finite contact mechanism exactly, not Brownian paths.
contacts=[(.1,'A','C'),(1.,'A','B'),(9.,'C','B'),(10.,'B','D')]
def epidemic(lifetimes):
    infection={'A':0.}
    for t,u,v in contacts:
        u_infectious=u in infection and t<infection[u]+lifetimes[u]
        v_infectious=v in infection and t<infection[v]+lifetimes[v]
        if u_infectious and v not in infection:infection[v]=t
        elif v_infectious and u not in infection:infection[u]=t
    return infection

sir_controls=0
for a,c,b in itertools.product((.46,.54),(11.6,12.4),(1.9,2.1)):
    lifetimes={'A':a,'C':c,'B':b,'D':1}
    baseline=epidemic(lifetimes)
    longer=epidemic({v:3*l for v,l in lifetimes.items()})
    assert baseline['D']==10 and 'D' not in longer
    assert baseline['B']==9 and longer['B']==1
    sir_controls+=1
box_probability=math.prod(math.exp(-lo)-math.exp(-hi) for lo,hi in ((.45,.55),(11.5,12.5),(1.8,2.2)))
assert box_probability>0
save('P0011',{'contact_schedule_controls':sir_controls,'baseline_infected_count':4,
              'longer_lifetime_infected_count':3,'exponential_lifetime_box_probability':box_probability,
              'Brownian_contact_realization':'not proved'})

# P0037: exhaustive monotone-event pairs; probabilities compared as integers.
def monotone_events(m):
    result=[]
    for table in range(1<<(1<<m)):
        valid=True
        for mask in range(1<<m):
            if not (table>>mask&1):continue
            for bit in range(m):
                if not mask>>bit&1 and not (table>>(mask|(1<<bit))&1):
                    valid=False;break
            if not valid:break
        if valid:result.append(table)
    return result

def minimal_witnesses(table,m):
    return [mask for mask in range(1<<m) if table>>mask&1 and
            all(not(table>>(mask&~(1<<bit))&1) for bit in range(m) if mask>>bit&1)]

pair_checks=0
enum=[]
for m in (2,3,4):
    events=monotone_events(m)
    assert len(events)=={2:6,3:20,4:168}[m]
    full=(1<<m)-1
    trees=[full&~(1<<j) for j in range(m)]
    witnesses={table:minimal_witnesses(table,m) for table in events}
    support={table:[bool(table>>tree&1) for tree in trees] for table in events}
    profiles=[[1]*m,list(range(1,m+1)),[2**j for j in range(m)],[0]+list(range(2,m+1))]
    for A,B in itertools.product(events,repeat=2):
        unions=[a|b for a in witnesses[A] for b in witnesses[B] if not a&b]
        box=[any(not(union&~tree) for union in unions) for tree in trees]
        for weights in profiles:
            total=sum(weights)
            pa=sum(w*yes for w,yes in zip(weights,support[A]))
            pb=sum(w*yes for w,yes in zip(weights,support[B]))
            pbox=sum(w*yes for w,yes in zip(weights,box))
            assert pbox*total<=pa*pb
            pair_checks+=1
    enum.append({'ground_set_size':m,'monotone_events':len(events),'omission_profiles':profiles,
                 'event_pair_weight_checks':len(events)**2*len(profiles)})
# Nonincreasing B, triangle: P(A box B)=1/3 > (2/3)(1/3).
assert F(1,3)>F(2,3)*F(1,3)
save('P0037',{'exact_event_pair_weight_checks':pair_checks,'enumeration':enum,
              'violations':0,'nonincreasing_negative_control':{'disjoint_probability':'1/3','product':'2/9'},
              'scope':'co-singleton laws; weighted connected unicyclic graphs; not arbitrary UST'})

report['elapsed_seconds']=time.perf_counter()-started
report['completed']=True
ROOT.joinpath('measurements.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',round(report['elapsed_seconds'],3),flush=True)

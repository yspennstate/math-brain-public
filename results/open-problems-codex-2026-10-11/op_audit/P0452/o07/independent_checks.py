"""Independent finite checks; none substitutes for the asymptotic proof."""
import itertools
import math
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import zeta, gammainc, gammaincc

BASE = Path(__file__).resolve().parent
results = {}

def components(n, edges):
    roots = list(range(n))
    def find(x):
        while roots[x] != x:
            x = roots[x]
        return x
    for a, b in edges:
        a, b = find(a), find(b)
        roots[a] = b
    labels = [find(x) for x in range(n)]
    return labels, [labels.count(x) for x in set(labels)]

def mass(sizes, k):
    return sum(x for x in sizes if x >= k)

# Graph sensitivity: no access to claimant's code.
n = 5
pairs = list(itertools.combinations(range(n), 2))
count = 0
for mask in range(1 << len(pairs)):
    edges = {e for j,e in enumerate(pairs) if mask & (1 << j)}
    _, sizes = components(n, edges)
    for e in pairs:
        _, other = components(n, edges ^ {e})
        for k in range(1, n+2):
            assert abs(mass(sizes,k)-mass(other,k)) <= 2*(k-1)
            count += 1
results['one_edge_sensitivity_cases'] = count

# Exact history enumeration, including rejected arrivals in counters.
n = 4
pairs = list(itertools.combinations(range(n),2))
prefixes = checks = 0
for budgets in itertools.product(range(1,4),repeat=n):
    for order in itertools.permutations(pairs):
        deg = [0]*n
        seen, accepted = set(), set()
        for step in range(7):
            labels, _ = components(n,accepted)
            active = [v for v in range(n) if deg[v]<budgets[v]]
            for a,b in itertools.combinations(active,2):
                if labels[a]!=labels[b]:
                    assert (a,b) not in seen
                    checks += 1
            prefixes += 1
            if step < 6:
                a,b=order[step]
                if deg[a]<budgets[a] and deg[b]<budgets[b]:
                    accepted.add((a,b))
                deg[a]+=1
                deg[b]+=1
                seen.add((a,b))
        expected = set()
        for a,b in pairs:
            ra = 1+sum(order.index(e)<order.index((a,b)) for e in pairs if a in e and e!=(a,b))
            rb = 1+sum(order.index(e)<order.index((a,b)) for e in pairs if b in e and e!=(a,b))
            if ra<=budgets[a] and rb<=budgets[b]: expected.add((a,b))
        assert expected == accepted
results['arrival_prefixes'] = prefixes
results['active_cross_pair_tests'] = checks

# Fresh-child motif integral, independently evaluated in its stable shifted form.
motif = []
for d,t in itertools.product([2,3,7,25],[0.25,1,3,6,15]):
    val,err=quad(lambda w: math.exp(-t-w)*w**(d-1)/math.factorial(d-1),0,np.inf,epsabs=1e-13)
    exact=math.exp(-t)
    assert abs(val-exact)<1e-10
    motif.append(dict(d=d,t=t,value=val,exact=exact,error=err))
results['motif_integrals'] = motif

# Exhaust finite final-component mass partitions.
partition_cases = 0
for total in range(3,20):
    for breaks in range(1 << (total-1)):
        blocks=[]
        start=0
        for i in range(1,total):
            if breaks & (1 << (i-1)):
                blocks.append(i-start); start=i
        blocks.append(total-start)
        for eta in range(1,total//3+1):
            if max(blocks)>=total-eta: continue
            # The same dichotomy, tested without guessing a subset.
            candidate=next((x for x in blocks if eta<=x<=total-eta),None)
            if candidate is None:
                assert max(blocks)<eta
                candidate=0
                for b in blocks:
                    candidate+=b
                    if candidate>=eta: break
            assert eta<=candidate<=total-eta
            partition_cases+=1
results['partition_cases'] = partition_cases

# Heavy-tail first moment without second moment: D=1+M, p(M)=M^-5/2 / zeta(5/2).
tail_rows=[]
normalizer=float(zeta(2.5,1))
mean_m=float(zeta(1.5,1))/normalizer
for B,a,b in [(10,.05,30),(100,.01,250),(1000,.001,2000)]:
    ms=np.arange(1,B+1,dtype=float)
    weights=ms**(-1.5)/normalizer
    kept=weights*(gammainc(ms+1,b)-gammainc(ms+1,a))
    epsilon=mean_m-float(kept.sum())
    tail_rows.append(dict(B=B,a=a,b=b,epsilon=epsilon))
assert tail_rows[-1]['epsilon']<1
results['infinite_variance_compact_tail'] = tail_rows

# Finite discretization of EXACT slot kernel; return Schur complement and reversal.
# This case has supercritical direct reproduction. A separate stress script
# checks subcritical direct reproduction with a supercritical return kernel.
m=np.array([1.,2.,5.,8.])
x=np.array([.3,1.,3.,8.])
p=np.array([.12,.38,.30,.20])
H=np.minimum(x[:,None],x[None,:])/x[:,None]
M=m[:,None]*H*p[None,:]
full_radius=float(max(np.linalg.eigvals(M).real))
K=np.array([2,3]); O=np.array([0,1])
epsilon=float(np.sum(m[O]*p[O]))
direct=M[np.ix_(K,K)]
bridge=M[np.ix_(K,O)]
outside=M[np.ix_(O,O)]
back=M[np.ix_(O,K)]
R=direct+bridge@np.linalg.inv(np.eye(len(O))-outside)@back
alpha=m/x
pi=p/alpha
symmetry_error=float(np.max(np.abs(pi[K,None]*R-R.T*pi[K][None,:])))
assert epsilon<1 and symmetry_error<1e-12
trunc=[]
RN=direct.copy()
power=np.eye(len(O))
for N in range(13):
    if N>0:
        RN+=bridge@power@back
        power=power@outside
    loss_density=(R-RN)/p[K][None,:]
    bound=max(m[K])*epsilon**(N+1)/(1-epsilon)
    assert np.min(loss_density)>-1e-12
    assert np.max(loss_density)<=bound+1e-10
    assert np.max(np.abs(pi[K,None]*RN-RN.T*pi[K][None,:]))<1e-12
    trunc.append(dict(N=N,radius=float(max(np.linalg.eigvals(RN).real)),max_loss=float(loss_density.max()),bound=bound))
results['return_kernel'] = dict(full_radius=full_radius,direct_radius=float(max(np.linalg.eigvals(direct).real)),return_radius=float(max(np.linalg.eigvals(R).real)),epsilon=epsilon,symmetry_error=symmetry_error,truncations=trunc)

# For this finite slot process, compute minimal extinction fixed points under cutoffs.
cutoff_rows=[]
for t in [.1,.5,1,2,4,8,100]:
    ht=np.minimum(np.minimum(x[:,None],x[None,:]),t)/x[:,None]
    q=np.zeros(len(m))
    for iteration in range(20000):
        nq=(1-ht@(p*(1-q)))**m
        if np.max(np.abs(nq-q))<1e-13: break
        q=nq
    cutoff_rows.append(dict(t=t,iterations=iteration,q=nq.tolist()))
assert all(np.max(np.array(b['q'])-np.array(a['q']))<1e-10 for a,b in zip(cutoff_rows,cutoff_rows[1:]))
results['slot_fixed_points'] = cutoff_rows

# Rational check of path integrals from historical Section 7.
path_integrals=[]
for ell in range(3,8):
    integral=Fraction(0)
    for order in itertools.permutations(range(ell)):
        ranks={v:i for i,v in enumerate(order)}
        coeff=[0]*ell
        for i in range(ell-1):
            coeff[max(ranks[i],ranks[i+1])]+=1
        denom=1
        for j in range(ell): denom*=sum(coeff[j:])
        integral+=Fraction(1,denom)
    bound=1.25*(1/math.sqrt(2))**(ell-3)
    assert float(integral)<=bound+1e-12
    path_integrals.append(dict(ell=ell,exact=str(integral),bound=bound))
results['path_integrals'] = path_integrals

(BASE/'independent_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in results.items() if k in ['one_edge_sensitivity_cases','arrival_prefixes','active_cross_pair_tests','partition_cases','infinite_variance_compact_tail','return_kernel','path_integrals']},indent=2))

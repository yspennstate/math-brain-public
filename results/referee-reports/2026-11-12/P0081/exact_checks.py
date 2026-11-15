"""Independent rational checks; no author code is imported."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import exp, factorial


def check(name, edges, sigma, steps=7):
    nv = max(max(e) for e in edges) + 1
    inc = [[i for i, e in enumerate(edges) if v in e] for v in range(nv)]
    assert all(sum(sigma[e] for e in row) == 0 for row in inc)
    h = [F(0)]
    h2 = [F(0)]
    for k in range(1, steps + 2):
        h.append(h[-1] + F(1, k))
        h2.append(h2[-1] + F(1, k*k))
    law = {tuple([1]*len(edges)): F(1)}
    expected_bracket = F(0)
    poisson_em = poisson_m2 = poisson_q = 0.0
    integrated_rates=F(0)
    t = .25
    print(name, 'edges=', edges, 'sigma=', sigma)
    for k in range(steps+1):
        em = sum(p*sum(s*h[n-1] for s,n in zip(sigma,state)) for state,p in law.items())
        em2 = sum(p*sum(s*h[n-1] for s,n in zip(sigma,state))**2 for state,p in law.items())
        assert em == 0 and em2 == expected_bracket
        optional=sum(p*sum(s*s*h2[n-1] for s,n in zip(sigma,state)) for state,p in law.items())
        assert optional == em2
        rate_mean=sum(p*sum(sum(F(sigma[e]**2,state[e]*sum(state[f] for f in row))
                                   for e in row) for row in inc) for state,p in law.items())
        integrated_rates+=rate_mean
        weight = exp(-nv*t)*(nv*t)**k/factorial(k)
        poisson_em += weight*float(em)
        poisson_m2 += weight*float(em2)
        # Conditional on K(t)=k, k+1 gaps have mean t/(k+1).
        # The embedded choices are independent of these waiting times.
        poisson_q += weight*t/(k+1)*float(integrated_rates)
        print(f'  rings={k}, states={len(law)}, E[M]={em}, E[M^2]=E[bracket]={float(em2):.12g}')
        if k == steps:
            break
        new = defaultdict(F)
        for state,p in law.items():
            drift = F(0)
            q = F(0)
            for row in inc:
                sv = sum(state[e] for e in row)
                drift += sum(F(sigma[e], sv) for e in row)
                q += sum(F(sigma[e]**2, sv*state[e]) for e in row)
                for e in row:
                    ns = list(state)
                    ns[e] += 1
                    new[tuple(ns)] += p*F(state[e], nv*sv)
            assert drift == 0
            expected_bracket += p*q/nv
        law = new
        assert sum(law.values()) == 1
    # For a unit jump bound |M|<=K, the omitted Poisson second moment
    # is bounded by sum_{k>steps} k^2 P(K=k), computed without cancellation.
    remainder = sum(k*k*exp(-nv*t)*(nv*t)**k/factorial(k) for k in range(steps+1,100))
    poisson_tail=sum(exp(-nv*t)*(nv*t)**k/factorial(k) for k in range(steps+1,100))
    print(f'  continuous t={t}: Poisson mixture E[M]={poisson_em:g}, '
          f'E[M^2]=E[optional]={poisson_m2:.12g}; omitted M^2 bound={remainder:.3g}; '
          f'independently integrated E[predictable bracket]={poisson_q:.12g}, '
          f'omitted bracket bound={nv*t*poisson_tail:.3g}')


cycle = [(0,1),(1,2),(2,3),(3,0)]
check('C4', cycle, [1,-1,1,-1], 14)
check('K4 (contains triangles)', [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],
      [1,-1,0,0,-1,1], 12)

state=(2,1,1,1)
sigma=(1,-1,0,0)
drift=sum(F(sum(sigma[e] for e,ends in enumerate(cycle) if v in ends),
            sum(state[e] for e,ends in enumerate(cycle) if v in ends)) for v in range(4))
print('C4 nonkernel sigma=(1,-1,0,0), state=(2,1,1,1): generator M =', drift)


def synchronous_drift(n):
    # Dual cycle: every comparison vertex acts once, using OLD counts.
    sig=(1,-1,1,-1)
    def hh(k): return sum((F(1,j) for j in range(1,k)),F(0))
    before=sum(s*hh(k) for s,k in zip(sig,n))
    out=F(0)
    for choices in product((0,1), repeat=4):
        p=F(1); nn=list(n)
        for v,c in enumerate(choices):
            e=(v-1)%4 if c == 0 else v
            p*=F(n[e],n[v-1]+n[v]); nn[e]+=1
        out+=p*(sum(s*hh(k) for s,k in zip(sig,nn))-before)
    return out

for state in [(1,1,1,1),(3,2,1,2),(3,1,3,1)]:
    print('Synchronous harmonic charge drift at',state,'=',synchronous_drift(state))
print('Initial continuous embedded event: M=+/-1 with equal probabilities.')
hist=defaultdict(int)
for choices in product((0,1), repeat=4):
    nn=[1]*4
    for v,c in enumerate(choices): nn[(v-1)%4 if c==0 else v]+=1
    h=lambda n: sum((F(1,j) for j in range(1,n)), F(0))
    hist[sum(s*h(n) for s,n in zip((1,-1,1,-1),nn))]+=1
print('Initial synchronous round charge multiplicities out of 16:', sorted(hist.items()))
print('Initial synchronous E[M^2]=',sum(m*m*k for m,k in hist.items())/16)

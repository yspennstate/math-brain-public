"""Independent finite arithmetic and seeded simulator checks; writes only locally."""
import itertools, json, math, random
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parent
out = {}

# Exact hypergeometric exponential moment at lambda=log(2), all boundary cases.
count = 0
for N in range(1, 21):
    for C in range(N + 1):
        for m in range(N + 1):
            lhs = sum((F(math.comb(C, x) * math.comb(N-C, m-x), math.comb(N, m)) * F(1, 2)**x
                       for x in range(max(0, m-(N-C)), min(C,m)+1)), F(0))
            rhs = (1-F(C,2*N))**m
            assert lhs <= rhs, (N,C,m,lhs,rhs)
            count += 1
out['exact_hypergeometric_mgf_cases'] = count

def partitions_set(n):
    blocks = []
    def visit(v):
        if v == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for block in blocks:
            block.append(v)
            yield from visit(v+1)
            block.pop()
        blocks.append([v])
        yield from visit(v+1)
        blocks.pop()
    yield from visit(0)

# Enumerate every graph and every partition for n<=5. Whenever the current
# cut condition holds, verify its claimed adaptive-partition crossing bound.
graphs = goodgraphs = partitionchecks = 0
for n in range(2,6):
    edges = list(itertools.combinations(range(n),2))
    N = len(edges)
    cuts = [sum(1<<e for e,(u,v) in enumerate(edges) if ((A>>u)&1)!=((A>>v)&1))
            for A in range(1, (1<<n)-1)]
    part = list(partitions_set(n))
    for mask in range(1<<N):
        graphs += 1
        m = mask.bit_count()
        if not m: continue
        if any(2*N*(mask&cut).bit_count() < m*cut.bit_count() for cut in cuts): continue
        goodgraphs += 1
        for blocks in part:
            label = {v:i for i,block in enumerate(blocks) for v in block}
            cross = sum(1 for e,(u,v) in enumerate(edges) if (mask>>e)&1 and label[u]!=label[v])
            assert 2*n*cross >= m*(len(blocks)-1)
            partitionchecks += 1
out.update(graphs=graphs, good_graphs=goodgraphs, adaptive_partition_checks=partitionchecks)

# Direct exact drift, including the threshold boundary a=1.
drifts = 0
for n in (2, 10, 100):
    for B in (4,12,20):
        for m in (B*n+1, B*n+2, B*n*10):
            a = F(B*n,m-1)
            for z in range(n):
                for p in (F(z,2*n),F(1)):
                    drift = F(B*n*z,m*(m-1)) - p*a*a/2
                    assert drift <= 0
                    drifts += 1
out['exact_drift_checks'] = drifts

# Exact one-bin count law checked by deterministic quadrature; full process
# law follows from the written regenerative first-event proof, not this test.
def integrand(t,b,h,z):
    return b*((1-b*t)*z+b*t)*math.exp(b*(h-t)*(z-1))
maxerr = 0.0
for b,h,z in itertools.product((.1,.5,1.0),(.3,.7,1.0),(0.0,.2,.8,1.0)):
    steps=2000
    v=integrand(0,b,h,z)+integrand(h,b,h,z)
    v+=sum((4 if j%2 else 2)*integrand(h*j/steps,b,h,z) for j in range(1,steps))
    pgf=1-b*h+(h/(3*steps))*v
    maxerr=max(maxerr,abs(pgf-math.exp(b*h*(z-1))))
assert maxerr<1e-11
out['count_pgf_max_quadrature_error'] = maxerr

# Seeded process simulation: first retained low offer plus independent phantom
# points. Count disjoint interval increments and marks at the b=1 boundary.
rng=random.Random(22120261011)
results=[]
samples=100000
for b in (.1,.5,1.0):
    s1=s2=s11=s22=s12=marks=marksum=0.0
    hist=[0]*7
    for _ in range(samples):
        T,W=rng.random(),rng.random()
        events=[]
        if W<=b:
            if rng.random()<=1-b*T: events.append((T,W/b))
            t=T
            while True:
                t+=rng.expovariate(b)
                if t>1: break
                events.append((t,rng.random()))
        x=sum(t<=.5 for t,w in events)
        y=len(events)-x
        s1+=x; s2+=y; s11+=x*x; s22+=y*y; s12+=x*y
        marks+=len(events); marksum+=sum(w for t,w in events)
        hist[min(len(events),6)]+=1
    row=dict(b=b, samples=samples, first_mean=s1/samples, second_mean=s2/samples,
             first_variance=s11/samples-(s1/samples)**2,
             second_variance=s22/samples-(s2/samples)**2,
             increment_covariance=s12/samples-s1*s2/samples**2,
             mark_mean=marksum/marks, count_histogram=hist)
    assert abs(row['first_mean']-b/2)<.012
    assert abs(row['second_mean']-b/2)<.012
    assert abs(row['increment_covariance'])<.012
    results.append(row)
out['simulator_monte_carlo'] = results
(root/'second_checks.json').write_text(json.dumps(out,indent=2)+'\n', encoding='utf-8')
print(json.dumps(out,indent=2))

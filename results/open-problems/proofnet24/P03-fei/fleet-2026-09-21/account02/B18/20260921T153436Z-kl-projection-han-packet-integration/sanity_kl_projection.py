import itertools, json, math, random

def H(ps):
    return -sum(p*math.log2(p) for p in ps if p > 0.0)

def marginal(mu, n, B):
    B = tuple(B)
    out = {bits: 0.0 for bits in itertools.product((0,1), repeat=len(B))}
    for s,p in enumerate(mu):
        bits = tuple((s >> i) & 1 for i in B)
        out[bits] += p
    return [out[bits] for bits in itertools.product((0,1), repeat=len(B))]

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def tc(mu, n, B):
    return sum(
        h2(sum(mu[s] for s in range(1<<n) if (s>>i)&1))
        for i in B
    ) - H(marginal(mu,n,B))

def mutual_info(mu,n,i,B):
    return h2(sum(mu[s] for s in range(1<<n) if (s>>i)&1)) + H(marginal(mu,n,B)) - H(marginal(mu,n,tuple(B)+(i,)))

def check(mu,n):
    Hn=H(mu)
    T=tc(mu,n,range(n))
    max_proj=0.0
    hq=[0.0]
    Tq=[0.0]
    Aq=[0.0]
    for q in range(1,n+1):
        Bs=list(itertools.combinations(range(n),q))
        hbar=sum(H(marginal(mu,n,B)) for B in Bs)/len(Bs)
        tbar=sum(tc(mu,n,B) for B in Bs)/len(Bs)
        a=hbar-(q/n)*Hn
        max_proj=max(max_proj,abs(a-((q/n)*T-tbar)))
        hq.append(hbar); Tq.append(tbar); Aq.append(a)
    m=[]
    for q in range(n):
        vals=[]
        for i in range(n):
            others=[j for j in range(n) if j!=i]
            for B in itertools.combinations(others,q):
                vals.append(mutual_info(mu,n,i,B))
        m.append(sum(vals)/len(vals))
    max_slope=abs(T-sum(m))
    for q in range(1,n):
        lo=sum(m[:q])/q
        hi=sum(m[q:])/(n-q)
        max_slope=max(max_slope,abs(Aq[q]-q*(n-q)/n*(hi-lo)))
    mono=all(m[q] <= m[q+1] + 1e-12 for q in range(n-1))
    return {"n":n,"T":T,"max_projection_identity_error":max_proj,
            "max_slope_identity_error":max_slope,"m_monotone":mono}

rng=random.Random(20260921)
rows=[]
for n in range(2,6):
    xs=[rng.random()+0.01 for _ in range(1<<n)]
    z=sum(xs); mu=[x/z for x in xs]
    rows.append(check(mu,n))

# Two exact-structure stress tests.
n=4
rows.append({"case":"uniform-product-bent-spectrum-proxy", **check([1/(1<<n)]*(1<<n),n)})
# one-point-defect Fourier-square law: empty coefficient (1-2^(1-n))^2,
# every nonempty coefficient square 2^(2-2n).
n=8
mu=[(1-2**(1-n))**2] + [2**(2-2*n)]*((1<<n)-1)
rows.append({"case":"one-point-defect-spectrum", **check(mu,n)})

print(json.dumps(rows, indent=2, sort_keys=True))

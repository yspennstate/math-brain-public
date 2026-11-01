from fractions import Fraction as F
from itertools import product, permutations

CHECKS = 0

def ck(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def rising(a, n):
    r = F(1)
    for t in range(n):
        r *= a + t
    return r

def nu(x, a):
    n = len(x)
    s = sum(x)
    return rising(a, s) * rising(a, n-s) / rising(2*a, n)

def q1_heatbath(x, v, a):
    n = len(x)
    s_other = sum(x) - x[v]
    return (a + s_other) / (F(n-1) + 2*a)

def heatbath_transition(x, y, v, a):
    if any(x[u] != y[u] for u in range(len(x)) if u != v):
        return F(0)
    q = q1_heatbath(x, v, a)
    return q if y[v] == 1 else 1-q

def split_formula(a, i, j):
    return 2 * rising(a, i) * rising(a, j) / rising(2*a, i+j)

def beta_int(i,j):
    # B(i,j) for positive integers
    import math
    return F(math.factorial(i-1)*math.factorial(j-1), math.factorial(i+j-1))

def no_split2(x):
    n=len(x); s=sum(x)
    return F(s*(s-1)+(n-s)*(n-s-1), n*(n-1))

# 1. Exact normalization and fixed-site Gibbs detailed balance/invariance.
for N in range(2, 8):
    a = F(1,N)
    states = list(product((0,1), repeat=N))
    total = sum(nu(x,a) for x in states)
    ck(total == 1, f'nu normalization N={N}: {total}')
    for v in range(N):
        # detailed balance for the only nontrivial flip edge at v
        for x in states:
            y=list(x); y[v]=1-x[v]; y=tuple(y)
            lhs = nu(x,a)*heatbath_transition(x,y,v,a)
            rhs = nu(y,a)*heatbath_transition(y,x,v,a)
            ck(lhs == rhs, f'detailed balance N={N} v={v} x={x}')
        # invariance checked state by state
        for y in states:
            incoming = sum(nu(x,a)*heatbath_transition(x,y,v,a) for x in states)
            ck(incoming == nu(y,a), f'invariance N={N} v={v} y={y}')

# 2. Predictive split identity by exact ordered-injection enumeration.
for N in range(2, 8):
    a = F(1,N)
    states = list(product((0,1), repeat=N))
    for b in range(2, min(5,N)+1):
        tuples = list(permutations(range(N), b))
        den = F(len(tuples))
        for i in range(1,b):
            j=b-i
            direct=F(0)
            for x in states:
                good=0
                for tup in tuples:
                    pat=[x[u] for u in tup]
                    if (all(z==1 for z in pat[:i]) and all(z==0 for z in pat[i:])) or \
                       (all(z==0 for z in pat[:i]) and all(z==1 for z in pat[i:])):
                        good += 1
                direct += nu(x,a)*F(good, len(tuples))
            form=split_formula(a,i,j)
            ck(direct == form, f'predictive N={N} i={i} j={j}: {direct} vs {form}')
            # exact tangent product identity
            lhs = form / (a*beta_int(i,j))
            prod = F(1)
            for r in range(1,i): prod *= 1 + a/F(r)
            for r in range(1,j): prod *= 1 + a/F(r)
            for r in range(1,b): prod /= 1 + 2*a/F(r)
            ck(lhs == prod, f'tangent product N={N} i={i} j={j}')

# 3. Boundary compactification: p_alpha / alpha -> B(i,j), checked exactly along alpha=1/N.
for i in range(1,6):
    for j in range(1,6):
        B=beta_int(i,j)
        # exact finite-N errors shrink monotonically after a coarse start for these cases
        errs=[]
        for N in (10,20,40,80,160):
            a=F(1,N)
            errs.append(abs(split_formula(a,i,j)/a - B))
        for u,v in zip(errs, errs[1:]):
            ck(v < u or v == 0, f'boundary error not decreasing i={i} j={j}: {errs}')
        ck(errs[-1] < F(1,50), f'boundary error still large i={i} j={j}: {errs[-1]}')

# 4. Critical scales for C027: Delta=alpha=1/N, L=N^3.
for N in range(2,501):
    Delta=F(1,N); L=N**3
    ck(L*Delta*Delta == N, f'finite-pool scale N={N}')
    # O(Delta^2) simultaneous-split and kernel-error bookkeeping only needs Delta->0.
    ck(Delta > 0 and Delta <= F(1,2), f'Delta range N={N}')

# 5. N=4 exact root witness and prior binary-class separation.
N=4; a=F(1,4)
p13=split_formula(a,1,3)
p22=split_formula(a,2,2)
ratio=p13/p22
ck(p13 == F(3,56), f'p13={p13}')
ck(p22 == F(5,168), f'p22={p22}')
ck(ratio == F(9,5), f'ratio={ratio}')
prior_binary = [
    F(2,1), F(7,5), F(2699,1365), F(2273,1153), F(61381,43765),
    F(166094447739,85563797248), F(33,17), F(5,3), F(597,359), F(18,11)
]
for q in prior_binary:
    ck(ratio != q, f'collision with prior binary witness {q}')

# 6. Finite mechanism witness: heat-bath is not the Moran fixed-victim kernel even at same (N,alpha).
x=(1,0,0,0); v=0
hb=q1_heatbath(x,v,a)
# C023/C021 fixed-victim Moran stay-1 probability at this x,v with the same alpha.
moran_stay_1 = (F(1)+a)/(F(N)+2*a)
ck(hb == F(1,14), f'heatbath witness {hb}')
ck(moran_stay_1 == F(5,18), f'moran witness {moran_stay_1}')
ck(hb != moran_stay_1, 'heatbath and Moran kernels coincide unexpectedly')

# 7. Tree-visible temporal witness at N=4 for C027 finite locus pool L=N^3.
states=list(product((0,1), repeat=N))
sbar=sum(nu(x,a)*no_split2(x) for x in states)
hsame=F(0)
for x in states:
    gx=no_split2(x)
    Kg=F(0)
    for vv in range(N):
        q=q1_heatbath(x,vv,a)
        for bit,pr in ((1,q),(0,1-q)):
            y=list(x); y[vv]=bit; y=tuple(y)
            Kg += F(1,N)*pr*no_split2(y)
    hsame += nu(x,a)*gx*Kg
L=N**3
two_step=(1-F(1,L))*sbar*sbar + F(1,L)*hsame
temporal_ratio=two_step/(sbar*sbar)
ck(sbar == F(5,6), f'sbar={sbar}')
ck(hsame == F(5263,7056), f'hsame={hsame}')
ck(two_step == F(313963,451584), f'two_step={two_step}')
ck(temporal_ratio == F(313963,313600), f'temporal ratio={temporal_ratio}')
ck(temporal_ratio != 1, 'finite-locus temporal dependence vanished')
ck(temporal_ratio != F(37,36), 'collides with archived C023 temporal witness')

print('R11 C027 exact self-check')
print(f'CHECKS={CHECKS}')
print('N4 alpha=1/4 root particular-support probabilities:')
print(f'  p(1|3)={p13}')
print(f'  p(2|2)={p22}')
print(f'  ratio={ratio} = {float(ratio):.12f}')
print('Same-alpha mechanism witness at x=(1,0,0,0), victim=1-site:')
print(f'  Gibbs heat-bath P(new bit=1)={hb}')
print(f'  Moran fixed-victim P(new bit=1)={moran_stay_1}')
print('N4 two-label finite-pool temporal witness:')
print(f'  P(no split one query)={sbar}')
print(f'  same-locus two-query no-split moment={hsame}')
print(f'  unconditional two-query survival={two_step}')
print(f'  survival ratio={temporal_ratio} = {float(temporal_ratio):.12f}')
print('Critical scales: Delta_N=alpha_N=1/N, L_N=N^3, so L_N Delta_N^2=N -> infinity.')
print('ALL_EXACT_CHECKS_PASS')

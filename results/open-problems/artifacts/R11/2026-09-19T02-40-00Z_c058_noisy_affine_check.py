from fractions import Fraction
from itertools import combinations, product
from math import comb

ASSERTS = 0

def check(cond, msg):
    global ASSERTS
    ASSERTS += 1
    if not cond:
        raise AssertionError(msg)

def is_prime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True

def least_prime_ge(n):
    q=n
    while not is_prime(q): q+=1
    return q

def ceil_log2_int(n):
    # least L with 2^L >= n
    L=0; p=1
    while p<n:
        p*=2; L+=1
    return L

def rho_for_N(N):
    return Fraction(1, max(2, ceil_log2_int(N+1)))

def base_bits(q,j,a,b,labels):
    return tuple(1 if ((a*r+b) % q) < j else 0 for r in labels)

def noisy_pattern_prob_given_y(q,j,rho,y,z):
    x=Fraction(j,q)
    p=Fraction(1)
    for yi,zi in zip(y,z):
        p *= rho*(1 if zi==yi else 0) + (1-rho)*(x if zi else 1-x)
    return p

def avg_pattern_prob(q,j,rho,labels,z):
    s=Fraction(0)
    for a in range(q):
        for b in range(q):
            y=base_bits(q,j,a,b,labels)
            s += noisy_pattern_prob_given_y(q,j,rho,y,z)
    return s/Fraction(q*q)

def split_prob_mark(q,j,rho,A,B):
    labels=tuple(sorted(set(A)|set(B)))
    z1=tuple(1 if r in A else 0 for r in labels)
    z2=tuple(1 if r in B else 0 for r in labels)
    return avg_pattern_prob(q,j,rho,labels,z1)+avg_pattern_prob(q,j,rho,labels,z2)

def mark_intensity(q,j):
    x=Fraction(j,q)
    return Fraction(1, 2*(q-1)) / (x*(1-x))

def split_rate(q,rho,A,B):
    return sum(mark_intensity(q,j)*split_prob_mark(q,j,rho,A,B) for j in range(1,q))

def iid_split_mark(q,j,i,jj):
    x=Fraction(j,q)
    return x**i*(1-x)**jj + x**jj*(1-x)**i

def iid_grid_rate(q,i,jj):
    return sum(mark_intensity(q,j)*iid_split_mark(q,j,i,jj) for j in range(1,q))

def beta_int(i,j):
    # (i-1)!(j-1)!/(i+j-1)!
    from math import factorial
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def centered_moment_base(q,j,labels):
    x=Fraction(j,q)
    s=Fraction(0)
    for a in range(q):
        for b in range(q):
            y=base_bits(q,j,a,b,labels)
            p=Fraction(1)
            for yi in y:
                p *= Fraction(yi)-x
            s += p
    return s/Fraction(q*q)

def centered_moment_noisy_direct(q,j,rho,labels):
    x=Fraction(j,q)
    s=Fraction(0)
    k=len(labels)
    for z in product((0,1), repeat=k):
        pz=avg_pattern_prob(q,j,rho,labels,z)
        mon=Fraction(1)
        for zi in z:
            mon *= Fraction(zi)-x
        s += pz*mon
    return s

# 1. Prime / parameter sanity.
for N in range(2,40):
    q=least_prime_ge(N)
    check(is_prime(q) and q>=N, f'least prime failed N={N}')
    check(Fraction(0)<rho_for_N(N)<=Fraction(1,2), f'rho range N={N}')

# 2. Affine F_q values are exactly pairwise uniform on distinct labels.
for q in [3,5,7,11]:
    labels=list(range(min(q,7)))
    for r,s in combinations(labels,2):
        counts={(u,v):0 for u in range(q) for v in range(q)}
        for a in range(q):
            for b in range(q):
                counts[((a*r+b)%q,(a*s+b)%q)] += 1
        for u in range(q):
            for v in range(q):
                check(counts[(u,v)]==1, f'pair uniform q={q}, r={r},s={s},u={u},v={v}')

# 3. Thresholded affine bits have exact Bernoulli(x) one- and two-point marginals.
for q in [5,7,11]:
    labels=list(range(min(q,6)))
    for j in range(1,q):
        x=Fraction(j,q)
        for r in labels:
            p=avg_pattern_prob(q,j,Fraction(1),[r],(1,))
            check(p==x, f'one marginal q={q},j={j},r={r}')
        for r,s in combinations(labels,2):
            for z in product((0,1), repeat=2):
                p=avg_pattern_prob(q,j,Fraction(1),[r,s],z)
                target=(x if z[0] else 1-x)*(x if z[1] else 1-x)
                check(p==target, f'two marginal q={q},j={j},r={r},s={s},z={z}')

# 4. Noise-operator attenuation identity E prod(Z-x)=rho^r E prod(Y-x), independently enumerated.
for q in [5,7]:
    labels=list(range(min(q,5)))
    for j in range(1,q):
        for rho in [Fraction(1,2), Fraction(1,3), Fraction(1,4)]:
            for r in range(1,min(5,len(labels))+1):
                for S in combinations(labels,r):
                    lhs=centered_moment_noisy_direct(q,j,rho,S)
                    rhs=(rho**r)*centered_moment_base(q,j,S)
                    check(lhs==rhs, f'attenuation q={q},j={j},rho={rho},S={S}: {lhs}!={rhs}')

# 5. Universal centered-moment bound for base pairwise law on tested instances.
for q in [5,7,11]:
    labels=list(range(min(q,6)))
    for j in range(1,q):
        x=Fraction(j,q)
        M=max(x,1-x)
        for r in range(2,min(6,len(labels))+1):
            for S in combinations(labels,r):
                mom=abs(centered_moment_base(q,j,S))
                bound=x*(1-x)*(M**(r-2))
                check(mom<=bound, f'moment bound q={q},j={j},S={S}: {mom}>{bound}')

# 6. Split-probability error bound on many exact cases.
for q in [5,7]:
    labels=list(range(min(q,5)))
    for j in range(1,q):
        x=Fraction(j,q)
        for rho in [Fraction(1,2), Fraction(1,3), Fraction(1,4)]:
            for k in range(2,len(labels)+1):
                subset=labels[:k]
                for i in range(1,k):
                    A=set(subset[:i]); B=set(subset[i:])
                    got=split_prob_mark(q,j,rho,A,B)
                    target=x**i*(1-x)**(k-i)+x**(k-i)*(1-x)**i
                    bound=2*x*(1-x)*sum(Fraction(comb(k,r))*rho**r for r in range(3,k+1))
                    check(abs(got-target)<=bound, f'split bound q={q},j={j},rho={rho},k={k},i={i}')

# 7. Pair normalized rate is exactly one for the C058 mark intensities.
for N in range(2,16):
    q=least_prime_ge(N); rho=rho_for_N(N)
    if N>=2:
        got=split_rate(q,rho,{0},{1})
        check(got==1, f'pair rate N={N},q={q},rho={rho}: {got}')

# 8. Grid iid rates converge toward beta; verify exact symmetry formula and monotone-sized errors on sample q.
for q in [5,7,11,17,31]:
    for i in range(1,5):
        for jj in range(1,5):
            # symmetric-grid simplification
            direct=iid_grid_rate(q,i,jj)
            simple=sum((Fraction(u,q)**(i-1))*((1-Fraction(u,q))**(jj-1)) for u in range(1,q))/Fraction(q-1)
            check(direct==simple, f'grid symmetry q={q},i={i},j={jj}')
            # loose rigorous Riemann bound for polynomial on [0,1]: <= degree/(q-1) when degree>0, exact if degree=0
            target=beta_int(i,jj)
            deg=i+jj-2
            if deg==0:
                check(direct==target, 'pair beta exact')
            else:
                check(abs(direct-target)<=Fraction(deg, q-1), f'Riemann bound q={q},i={i},j={jj}')

# 9. C058 finite witness at N=6: q=7, rho=1/3.
N=6; q=least_prime_ge(N); rho=rho_for_N(N)
check(q==7 and rho==Fraction(1,3), f'C058 params q={q},rho={rho}')
vals={}
seen=set()
for subset in combinations(range(N),4):
    a,b,c,d=subset
    for A,B in [({a,b},{c,d}),({a,c},{b,d}),({a,d},{b,c})]:
        key=tuple(sorted([tuple(sorted(A)),tuple(sorted(B))]))
        if key in seen: continue
        seen.add(key)
        v=split_rate(q,rho,set(A),set(B))
        vals.setdefault(v,[]).append(key)
check(len(seen)==45, f'expected 45 balanced splits, got {len(seen)}')
expected={Fraction(533,2835):27, Fraction(709,3780):18}
check({v:len(L) for v,L in vals.items()}==expected, f'witness multiset { {v:len(L) for v,L in vals.items()} }')
check(Fraction(533,2835)-Fraction(709,3780)==Fraction(1,2268), 'witness gap')
check(split_rate(q,rho,{0},{1})==1, 'pair normalization witness')
check(split_rate(q,rho,{0},{1,2,3})==Fraction(1769,5670), '1|3 witness')

# 10. Distinct from unrefreshed affine C055 at same N/q under normalized rates.
vals_pure={}
seen=set()
for subset in combinations(range(N),4):
    a,b,c,d=subset
    for A,B in [({a,b},{c,d}),({a,c},{b,d}),({a,d},{b,c})]:
        key=tuple(sorted([tuple(sorted(A)),tuple(sorted(B))]))
        if key in seen: continue
        seen.add(key)
        v=split_rate(q,Fraction(1),set(A),set(B))
        vals_pure.setdefault(v,0); vals_pure[v]+=1
check(vals_pure=={Fraction(8,45):27, Fraction(3,20):18}, f'pure witness {vals_pure}')
check(set(vals_pure)!=set(vals), 'C058 must differ from pure affine C055')

print(f'ASSERTIONS={ASSERTS}')
print('C058_N6_Q7_RHO=1/3')
print('C058_BALANCED_RATE_A=533/2835 count=27')
print('C058_BALANCED_RATE_B=709/3780 count=18')
print('C058_BALANCED_GAP=1/2268')
print('C058_PAIR_RATE=1')
print('C058_1v3_RATE=1769/5670')
print('C055_PURE_AFFINE_BALANCED=8/45 count=27; 3/20 count=18')
print('ALL_EXACT_CHECKS_PASS')

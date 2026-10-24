from fractions import Fraction as F
from itertools import combinations

# Exact checker for the finite core used in
# 2026-09-20T103000Z__C0036_open_S3_neighborhood.md

# D_3 coordinates r^i s^j, with s r s = r^{-1}.
G = [(i,j) for j in (0,1) for i in range(3)]
idx = {g:k for k,g in enumerate(G)}

def mul(g,h):
    i,j = g; k,l = h
    return ((i + (-1 if j else 1)*k) % 3, (j+l) % 2)

def inv(g):
    for h in G:
        if mul(g,h)==(0,0) and mul(h,g)==(0,0):
            return h
    raise RuntimeError

def act_subset(a,mask):
    out=0
    for g in G:
        if (mask >> idx[g]) & 1:
            out |= 1 << idx[mul(a,g)]
    return out

# 16 left-translation subset orbits.
seen=set(); orbits=[]
for m in range(64):
    if m in seen: continue
    orb={act_subset(a,m) for a in G}
    seen |= orb
    orbits.append(sorted(orb))
assert len(orbits)==16
orbit_id={m:i for i,o in enumerate(orbits) for m in o}

# Orbit poset and its 76 upper ideals.
le=[[False]*16 for _ in range(16)]
for i,o in enumerate(orbits):
    for j,p in enumerate(orbits):
        le[i][j]=any((m & ~n)==0 for m in o for n in p)
upper=[]
for b in range(1<<16):
    ok=True
    for i in range(16):
        if (b>>i)&1:
            for j in range(16):
                if le[i][j] and not ((b>>j)&1):
                    ok=False; break
        if not ok: break
    if ok: upper.append(b)
assert len(upper)==76

def det(M):
    n=len(M)
    if n==0: return F(1)
    A=[row[:] for row in M]
    ans=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; ans=-ans
        piv=A[c][c]; ans*=piv
        for j in range(c,n): A[c][j]/=piv
        for r in range(c+1,n):
            fac=A[r][c]
            if fac:
                for j in range(c,n): A[r][j]-=fac*A[c][j]
    return ans

def conv_matrix(u,v,x0,x1,x2):
    q={(0,0):u,(1,0):v,(2,0):v,(0,1):x0,(1,1):x1,(2,1):x2}
    Q=[[F(0) for _ in range(6)] for _ in range(6)]
    for a,g in enumerate(G):
        gi=inv(g)
        for b,h in enumerate(G): Q[a][b]=q[mul(gi,h)]
    return Q

Q=conv_matrix(F(1,2),F(1,20),F(1,30),-F(1,60),F(1,30))
Iminus=[[((F(1) if i==j else F(0))-Q[i][j]) for j in range(6)] for i in range(6)]
assert det(Q)==F(143,10000)
assert det(Iminus)==F(567,40000)

def principal(M,mask):
    ids=[i for i in range(6) if (mask>>i)&1]
    return [[M[i][j] for j in ids] for i in ids]

def exact_probs(M):
    inc=[det(principal(M,m)) for m in range(64)]
    out=[F(0)]*64
    for s in range(64):
        rem=63^s; a=rem; tot=F(0)
        while True:
            tot += (-1 if a.bit_count()%2 else 1)*inc[s|a]
            if a==0: break
            a=(a-1)&rem
        out[s]=tot
    assert sum(out)==1 and min(out)>=0
    return out

def bern_probs(t):
    return [t**m.bit_count()*(1-t)**(6-m.bit_count()) for m in range(64)]

def event_prob(probs,b):
    return sum(probs[s] for s in range(64) if (b>>orbit_id[s])&1)

def coeffs(b):
    U=[s for s in range(64) if (b>>orbit_id[s])&1]
    c=[]
    for T in range(64):
        z=0
        for S in U:
            if (S & ~T)==0:
                z += -1 if ((T^S).bit_count()%2) else 1
        c.append(z)
    return c

weights=[]
for b in upper:
    c=coeffs(b)
    weights.append(sum(abs(c[t])*t.bit_count() for t in range(64)))
assert max(weights)==480

pbar=F(49267,100000)
rlow=F(50805,100000)
assert pbar**6 > F(143,10000)
assert (1-rlow)**6 > F(567,40000)

pq=exact_probs(Q)
pl=bern_probs(pbar)
pu=bern_probs(rlow)
low=[]; up=[]
for b in upper:
    low.append((b,event_prob(pq,b)-event_prob(pl,b)))
    up.append((b,event_prob(pu,b)-event_prob(pq,b)))

# Structural equality events in orbit-ideal bit encoding.
forced_low={0,32768,65535}       # empty, {full configuration}, whole space
forced_up={0,65534,65535}        # empty, nonempty, whole space
min_low=min(v for b,v in low if b not in forced_low)
min_up=min(v for b,v in up if b not in forced_up)

assert min_low==F(509351537331256502398728569,200000000000000000000000000000)
assert min_up==F(185372629975314782364961,64000000000000000000000000)
assert min_low > F(25467,10000000)   # > 0.0025467
assert min_up > F(28964,10000000)    # > 0.0028964

EPS=F(4,1000000)
assert min_low - 500*EPS > 0
assert min_up - 504*EPS > 0

print('subset_orbits',len(orbits))
print('invariant_upper_sets',len(upper))
print('max_event_Lipschitz_weight',max(weights))
print('det_Q',det(Q))
print('det_I_minus_Q',det(Iminus))
print('min_lower_rational_margin',min_low,float(min_low))
print('min_upper_rational_margin',min_up,float(min_up))
print('radius',EPS,float(EPS))
print('lower_margin_after_radius',min_low-500*EPS,float(min_low-500*EPS))
print('upper_margin_after_radius',min_up-504*EPS,float(min_up-504*EPS))
print('ALL_EXACT_OPEN_NEIGHBORHOOD_CHECKS_PASS')

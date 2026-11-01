from fractions import Fraction
from functools import lru_cache
from collections import Counter, defaultdict, deque

# Exact state model for recursive 3-majority.
def norm(ch):
    p = sum(c == '+' for c in ch)
    m = sum(c == '-' for c in ch)
    if p >= 2:
        return '+'
    if m >= 2:
        return '-'
    return tuple(sorted(ch, key=repr))

@lru_cache(None)
def queries(t):
    if t == 'u':
        return (('+', '-'),)
    if t in ('+', '-'):
        return ()
    out = set()
    for i, c in enumerate(t):
        if i and t[i] == t[i-1]:
            continue
        for cp, cm in queries(c):
            out.add((norm(t[:i] + (cp,) + t[i+1:]),
                     norm(t[:i] + (cm,) + t[i+1:])))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def V(t):
    if t in ('+', '-'):
        return Fraction(0)
    return min(Fraction(1) + (V(a) + V(b))/2 for a,b in queries(t))

@lru_cache(None)
def P(t):
    if t == '+':
        return Fraction(1)
    if t == '-':
        return Fraction(0)
    if t == 'u':
        return Fraction(1,2)
    a,b,c = map(P,t)
    return a*b + a*c + b*c - 2*a*b*c

def full(k):
    return 'u' if k == 0 else norm((full(k-1),)*3)

def opt_moves(t):
    if t in ('+', '-'):
        return ()
    best = V(t)
    return tuple((a,b) for a,b in queries(t)
                 if Fraction(1) + (V(a)+V(b))/2 == best)

# Fixed-policy derivatives/skews for the unique optimal policy on depth-3 reachable states.
@lru_cache(None)
def K(t):
    if t in ('+', '-'):
        return Fraction(0)
    oms = opt_moves(t)
    assert len(oms) == 1
    a,b = oms[0]
    return V(a)-V(b) + (K(a)+K(b))/2

@lru_cache(None)
def H(t):
    if t in ('+', '-'):
        return Fraction(0)
    oms = opt_moves(t)
    assert len(oms) == 1
    a,b = oms[0]
    return 2*P(t)-1 + (H(a)+H(b))/2

def flip(t):
    if t == '+': return '-'
    if t == '-': return '+'
    if t == 'u': return 'u'
    return norm(tuple(flip(c) for c in t))

def opt_reachable(root):
    seen = {root}
    q = deque([root])
    while q:
        s = q.popleft()
        if s in ('+', '-'):
            continue
        for a,b in opt_moves(s):
            for z in (a,b):
                if z not in seen:
                    seen.add(z)
                    q.append(z)
    return seen

# Outer-majority wrapper preserving the third residual child after the root is decided.
def wnorm(ch):
    return tuple(sorted(ch, key=repr))

def root_sign(w):
    p = sum(c == '+' for c in w)
    m = sum(c == '-' for c in w)
    if p >= 2: return '+'
    if m >= 2: return '-'
    return None

@lru_cache(None)
def wqueries(w):
    if root_sign(w) is not None:
        return ()
    out = set()
    for i,c in enumerate(w):
        if c in ('+', '-'):
            continue
        if i and w[i] == w[i-1]:
            continue
        for cp,cm in queries(c):
            out.add((wnorm(w[:i] + (cp,) + w[i+1:]),
                     wnorm(w[:i] + (cm,) + w[i+1:])))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def WV(w):
    if root_sign(w) is not None:
        return Fraction(0)
    return min(Fraction(1)+(WV(a)+WV(b))/2 for a,b in wqueries(w))

def wopt(w):
    if root_sign(w) is not None:
        return ()
    best = WV(w)
    return tuple((a,b) for a,b in wqueries(w)
                 if Fraction(1)+(WV(a)+WV(b))/2 == best)

def residual_child(w):
    r = root_sign(w)
    assert r is not None
    others = [c for c in w if c != r]
    if len(others) == 1:
        return others[0]
    if len(others) == 0:
        return r
    raise AssertionError(('invalid terminal wrapper',w))

def terminal_distribution(h):
    start = wnorm((full(h),)*3)
    frontier = {start: Fraction(1)}
    terminals = defaultdict(Fraction)
    nonterminal_seen = set()
    while frontier:
        nxt = defaultdict(Fraction)
        for w,pr in frontier.items():
            if root_sign(w) is not None:
                terminals[w] += pr
                continue
            nonterminal_seen.add(w)
            oms = wopt(w)
            assert len(oms) == 1
            a,b = oms[0]
            nxt[a] += pr/2
            nxt[b] += pr/2
        frontier = nxt
    ev = Fraction(0)
    eu = Fraction(0)
    erm = Fraction(0)
    for w,pr in terminals.items():
        r = Fraction(1 if root_sign(w) == '+' else -1)
        s = residual_child(w)
        m = 2*P(s)-1
        ev += pr*V(s)
        eu += pr*(1-m*m)
        erm += pr*r*m
    return WV(start), dict(terminals), ev, eu, erm, nonterminal_seen

# Known exact costs.
D1,D2,D3 = V(full(1)),V(full(2)),V(full(3))
assert D1 == Fraction(5,2)
assert D2 == Fraction(393,64)
assert D3 == Fraction(15796051,1048576)
print('D1,D2,D3',D1,D2,D3)

# B7: test whether (posterior, remaining value) is a closed scale-free state.
R3 = opt_reachable(full(3))
non = [s for s in R3 if s not in ('+','-')]
assert len(R3) == 499 and len(non) == 497
assert Counter(len(opt_moves(s)) for s in non) == Counter({1:497})

groups = defaultdict(list)
for s in non:
    groups[(P(s),V(s))].append(s)
coll = [(key,ss) for key,ss in groups.items() if len(ss)>1]
assert len(coll) == 6
assert all(len(ss)==2 and flip(ss[0])==ss[1] for _,ss in coll)
assert len({(P(s),V(s),K(s)) for s in non}) == 497
assert len({(P(s),V(s),H(s)) for s in non}) == 497
print('depth3_optimal_reachable',len(R3),'nonterminal',len(non),'unique_optimal_moves',497)
print('pV_collision_groups',len(coll),'all_size2_sign_pairs',True)
print('pVK_injective',True,'pVH_injective',True)

S = norm((
    norm(('-', norm(('u','u','u')), norm(('u','u','u')))),
    norm((norm(('+','u','u')), norm(('+','u','u')), norm(('u','u','u')))),
    norm((norm(('+','u','u')), norm(('-','u','u')), norm(('u','u','u')))),
))
J = flip(S)
assert (P(S),V(S),K(S),H(S)) == (Fraction(1,2),Fraction(2335,256),Fraction(31,2048),Fraction(19,256))
assert (P(J),V(J),K(J),H(J)) == (Fraction(1,2),Fraction(2335,256),-Fraction(31,2048),-Fraction(19,256))
sa,sb = opt_moves(S)[0]
ja,jb = opt_moves(J)[0]
assert (P(sa),V(sa),P(sb),V(sb)) == (Fraction(153,256),Fraction(33369,4096),Fraction(103,256),Fraction(33159,4096))
assert (P(ja),V(ja),P(jb),V(jb)) == (Fraction(153,256),Fraction(33159,4096),Fraction(103,256),Fraction(33369,4096))
print('collision_example_pV',P(S),V(S),'K_pair',K(S),K(J),'H_pair',H(S),H(J))
print('collision_example_S_successors',P(sa),V(sa),P(sb),V(sb))
print('collision_example_J_successors',P(ja),V(ja),P(jb),V(jb))

# B13: natural odd magnitudes are not monotone along the optimal depth-3 policy.
def compare_abs(F,s):
    cur = abs(F(s))
    a,b = opt_moves(s)[0]
    nxt = (abs(F(a))+abs(F(b)))/2
    return 'increase' if nxt>cur else 'decrease' if nxt<cur else 'equal'
ck = Counter(compare_abs(K,s) for s in non)
ch = Counter(compare_abs(H,s) for s in non)
assert ck == Counter({'decrease':320,'increase':174,'equal':3})
assert ch == Counter({'decrease':302,'increase':194,'equal':1})
print('absK_next_average_counts',dict(ck))
print('absH_next_average_counts',dict(ch))

# B30: solve one scale exactly, preserving terminal residual child.
expected = {
 0:(Fraction(5,2), Fraction(1,2), Fraction(1,2), Fraction(-1,2)),
 1:(Fraction(393,64), Fraction(87,64), Fraction(39,64), Fraction(-1,2)),
 2:(Fraction(15796051,1048576), Fraction(3539117,1048576), Fraction(158023,262144), Fraction(-1,2)),
}
for h in range(3):
    cost,terms,ev,eu,erm,seen = terminal_distribution(h)
    assert (cost,ev,eu,erm) == expected[h]
    print('h',h,'outer_cost',cost,'terminal_types',len(terms),'nonterminal_states',len(seen),
          'E_residual_V',ev,'residual_ratio',ev/V(full(h)),'E_uncertainty',eu,'E_r_m',erm)

cost,terms,ev,eu,erm,seen = terminal_distribution(2)
ratios=[]
for w,pr in terms.items():
    s = residual_child(w)
    m = 2*P(s)-1
    U = 1-m*m
    if U:
        ratios.append(V(s)/(D2*U))
assert max(ratios) == 1
print('h2_terminal_support_max_V_over_D2U',max(ratios))

# Exact obstruction to the tempting global domination V_h(s) <= D_h U(s).
sdag = norm(('-', norm(('-','u','u')), norm(('-','u','u'))))
p = P(sdag); U = 4*p*(1-p); v = V(sdag)
assert p == Fraction(1,16)
assert U == Fraction(15,64)
assert v == Fraction(15,8)
assert v/D2 == Fraction(40,131)
assert (v/D2)/U == Fraction(512,393) > 1
print('global_uncertainty_domination_counterexample','p',p,'U',U,'V',v,'V_over_D2',v/D2,'ratio_to_U',(v/D2)/U)

print('ALL_EXACT_LIMIT_STATE_UNCERTAINTY_CHECKS_PASS')

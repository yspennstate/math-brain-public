from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import defaultdict, deque

# P13 / C0021 exact self-check for methods B8, B20, B29.
# All finite mathematical comparisons use fractions.Fraction.


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
    for i,c in enumerate(t):
        if i and t[i] == t[i-1]:
            continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]), norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def V(t):
    if t in ('+', '-'):
        return Fraction(0)
    return min(Fraction(1)+(V(a)+V(b))/2 for a,b in queries(t))

@lru_cache(None)
def q(t):
    if t == '+': return Fraction(1)
    if t == '-': return Fraction(0)
    if t == 'u': return Fraction(1,2)
    a,b,c = (q(x) for x in t)
    return a*b+a*c+b*c-2*a*b*c

def full(h):
    return 'u' if h == 0 else norm((full(h-1),)*3)

def rank(t):
    if t in ('+','-'): return 0
    if t == 'u': return 1
    return sum(rank(x) for x in t)

def canonical_levels(max_h):
    levels=[{'+','-','u'}]
    for _ in range(max_h):
        prev=sorted(levels[-1], key=repr)
        out={'+','-'}
        for a,b,c in combinations_with_replacement(prev,3):
            out.add(norm((a,b,c)))
        levels.append(out)
    return levels

def min_regret(h):
    root=full(h)
    A={root:Fraction(0)}
    front={root}
    while front:
        cand={}
        for s in front:
            if s in ('+','-'): continue
            vs=V(s)
            for a,b in queries(s):
                r=Fraction(1)+(V(a)+V(b))/2-vs
                assert r >= 0
                zval=A[s]+r
                for z in (a,b):
                    if z not in cand or zval < cand[z]: cand[z]=zval
        new=set()
        for z,zval in cand.items():
            if z not in A or zval < A[z]:
                A[z]=zval; new.add(z)
        front=new
    return A

def canon3(t): return tuple(sorted(t,key=repr))

def terminal_residual(t):
    plus=[i for i,s in enumerate(t) if s=='+']
    minus=[i for i,s in enumerate(t) if s=='-']
    if len(plus)>=2:
        pair=plus[:2]; j=next(i for i in range(3) if i not in pair); return '+',t[j]
    if len(minus)>=2:
        pair=minus[:2]; j=next(i for i in range(3) if i not in pair); return '-',t[j]
    return None

levels=canonical_levels(3)
assert [len(levels[h]) for h in range(4)] == [3,6,46,17206]
D=[V(full(h)) for h in range(4)]
assert D == [Fraction(1),Fraction(5,2),Fraction(393,64),Fraction(15796051,1048576)]
A={h:min_regret(h) for h in (1,2,3)}
W={h:{s:V(s)-A[h][s] for s in A[h]} for h in (1,2,3)}

# ---------------- B8: exact dominating finite abstraction at h=3 ----------------
h=3
Dh=D[h]
# 2 posterior bins (<1/2, >=1/2) and 2 normalized-W bins (<1/2, >=1/2), plus intrinsic unresolved rank.
def abstract_class(s):
    if s=='+': return ('T+',)
    if s=='-': return ('T-',)
    qb = 0 if q(s) < Fraction(1,2) else 1
    wb = 0 if W[3][s] < Dh/2 else 1
    return ('N', rank(s), qb, wb)

classes=defaultdict(list)
for s in A[3]: classes[abstract_class(s)].append(s)
assert len(classes)==68

# Union of concrete actions in each abstract class. Terminal reward is max normalized W.
abs_actions=defaultdict(set)
abs_reward={}
for c,states in classes.items():
    if c[0].startswith('T'):
        abs_reward[c]=Fraction(0)
        continue
    abs_reward[c]=max(W[3][s]/Dh for s in states)
    for s in states:
        if s in ('+','-'): continue
        for a,b in queries(s):
            abs_actions[c].add(tuple(sorted((abstract_class(a),abstract_class(b)),key=repr)))

for c,states in classes.items():
    abs_reward[c]=max(W[3][s]/Dh for s in states)

def acanon3(t): return tuple(sorted(t,key=repr))

def aterminal(t):
    plus=[i for i,c in enumerate(t) if c==('T+',)]
    minus=[i for i,c in enumerate(t) if c==('T-',)]
    if len(plus)>=2:
        pair=plus[:2]; j=next(i for i in range(3) if i not in pair); return t[j]
    if len(minus)>=2:
        pair=minus[:2]; j=next(i for i in range(3) if i not in pair); return t[j]
    return None

@lru_cache(None)
def AB(t):
    residual=aterminal(t)
    if residual is not None:
        return abs_reward[residual]
    vals=[]
    for i,c in enumerate(t):
        if c in (('T+',),('T-',)): continue
        if i and t[i]==t[i-1]: continue
        for ca,cb in abs_actions[c]:
            vals.append((AB(acanon3(t[:i]+(ca,)+t[i+1:]))+AB(acanon3(t[:i]+(cb,)+t[i+1:])))/2)
    assert vals
    return max(vals)

aroot=acanon3((abstract_class(full(3)),)*3)
abs_beta3=AB(aroot)
assert abs_beta3 == Fraction(2251662374670021,2251799813685248)
rho3=Fraction(165736792,236940765)
assert abs_beta3 > rho3

# ---------------- B20: trace exact h=2 optimizer; posterior signatures are not Markov. ----------------
h=2
A2=A[2]; W2=W[2]
@lru_cache(None)
def B2(t):
    term=terminal_residual(t)
    if term is not None:
        return W2[term[1]]
    vals=[]
    for i,s in enumerate(t):
        if s in ('+','-'): continue
        if i and t[i]==t[i-1]: continue
        for a,b in queries(s):
            tp=canon3(t[:i]+(a,)+t[i+1:]); tm=canon3(t[:i]+(b,)+t[i+1:])
            vals.append(((B2(tp)+B2(tm))/2, i, a, b, tp, tm))
    return max(x[0] for x in vals)

def optimal_actions2(t):
    term=terminal_residual(t)
    if term is not None: return []
    target=B2(t); out=[]
    for i,s in enumerate(t):
        if s in ('+','-'): continue
        if i and t[i]==t[i-1]: continue
        for a,b in queries(s):
            tp=canon3(t[:i]+(a,)+t[i+1:]); tm=canon3(t[:i]+(b,)+t[i+1:])
            if (B2(tp)+B2(tm))/2 == target:
                out.append((i,a,b,tp,tm))
    return out

root2=canon3((full(2),)*3)
raw2=B2(root2)
assert raw2 == Fraction(57542829,16777216)
assert raw2/D[2] == Fraction(19180943,34340864)

reach={root2}; dq=deque([root2])
while dq:
    t=dq.popleft()
    for _,a,b,tp,tm in optimal_actions2(t):
        for z in (tp,tm):
            if z not in reach:
                reach.add(z); dq.append(z)
assert len(reach)==1046

def posterior_sig(t): return tuple(sorted((q(s) for s in t)))
def action_profile(t,act):
    i,a,b,_,_=act
    return (q(t[i]), tuple(sorted((q(a),q(b)))))
ps=defaultdict(set)
for t in reach:
    if terminal_residual(t) is not None: continue
    for act in optimal_actions2(t): ps[posterior_sig(t)].add(action_profile(t,act))
posterior_collision_count=sum(1 for sig,acts in ps.items() if len(acts)>1)
assert posterior_collision_count==240

S_A=canon3(('-', norm(('+','-',norm(('u','u','u')))), full(2)))
S_B=canon3(('-', norm(('+','-',norm(('+','-','u')))), full(2)))
assert S_A in reach and S_B in reach
assert posterior_sig(S_A)==posterior_sig(S_B)==(Fraction(0),Fraction(1,2),Fraction(1,2))
profA={action_profile(S_A,a) for a in optimal_actions2(S_A)}
profB={action_profile(S_B,a) for a in optimal_actions2(S_B)}
assert (Fraction(1,2),(Fraction(1,4),Fraction(3,4))) in profA
assert (Fraction(1,2),(Fraction(0),Fraction(1))) in profB

qv=defaultdict(list)
for s in A2:qv[(q(s),V(s))].append(s)
assert len(qv)==43
pair=qv[(Fraction(1,2),Fraction(5,2))]
assert len(pair)==2
wv=sorted((W2[s],A2[s],repr(s)) for s in pair)
assert [(x[0],x[1]) for x in wv]==[(Fraction(15,8),Fraction(5,8)),(Fraction(5,2),Fraction(0))]

qw=defaultdict(list)
for s in A[3]: qw[(q(s),W[3][s])].append(s)
qW_collision_classes=[v for v in qw.values() if len(v)>1]
assert len(qW_collision_classes)==212
assert max(map(len,qW_collision_classes))==2

S1=norm((
    norm(('+', norm(('u','u','u')), norm(('u','u','u')))),
    norm((norm(('-','u','u')), norm(('-','u','u')), norm(('u','u','u')))),
    full(2)
))
S2=norm((
    norm(('-', norm(('u','u','u')), norm(('u','u','u')))),
    norm((norm(('+','u','u')), norm(('+','u','u')), norm(('u','u','u')))),
    full(2)
))
assert q(S1)==q(S2)==Fraction(1,2)
assert W[3][S1]==W[3][S2]==Fraction(178035,16384)

def trans_profiles3(s):
    out=[]
    for a,b in queries(s):
        out.append((tuple(sorted((q(a),q(b)))), (W[3][a],W[3][b])))
    return out
p1=[x for x in trans_profiles3(S1) if x[0]==(Fraction(7,16),Fraction(9,16))]
p2=[x for x in trans_profiles3(S2) if x[0]==(Fraction(7,16),Fraction(9,16))]
assert p1 and p2
target=(Fraction(19673,2048),Fraction(169239,16384))
assert any(set(ws)==set(target) for _,ws in p1)
assert any(set(ws)==set(target) for _,ws in p2)

# ---------------- B29: compactified Hölder supersolution candidate ----------------
# P_h=(D_h-W_h)/D_h. Verify exact finite inequality
# P_h >= (3/4)|m|^(3/2), equivalently 16 P_h^2 >= 9 |m|^3, for all canonical states h<=3.
expected_min_c2={
    1:Fraction(32,25),
    2:Fraction(18386944,22841291),
    3:Fraction(147634018423616307200,227725810949378078473),
}
min_rows=[]
for h in (1,2,3):
    best=None; witness=None
    for s in A[h]:
        if s in ('+','-'): continue
        m=abs(2*q(s)-1)
        P=(D[h]-W[h][s])/D[h]
        assert P >= 0
        assert 16*P*P >= 9*m*m*m
        if m>0:
            c2=P*P/(m*m*m)
            if best is None or c2<best:
                best=c2; witness=s
    assert best==expected_min_c2[h]
    min_rows.append((h,best,q(witness),W[h][witness],repr(witness)))
# terminal states also satisfy the inequality (P=|m|=1).
for h in (1,2,3):
    for s in ('+','-'):
        P=(D[h]-W[h][s])/D[h]
        m=abs(2*q(s)-1)
        assert 16*P*P >= 9*m*m*m

# Root-adjacent family identities: after one '+' leaf, |m|=2^{-h}, A=0, V=D_h-1, P=1/D_h.
def one_plus_state(h):
    s=full(h)
    def rec(t,depth):
        if depth==0: return '+'
        ch=list(t); ch[0]=rec(ch[0],depth-1)
        return norm(tuple(ch))
    return rec(s,h)
for h in (1,2,3):
    s=one_plus_state(h)
    assert abs(2*q(s)-1)==Fraction(1,2**h)
    assert A[h][s]==0
    assert V(s)==D[h]-1
    assert (D[h]-W[h][s])/D[h]==Fraction(1,1)/D[h]

# A one-edge proof of the Hölder barrier fails already at h=1.
s0=norm(('+','-','u'))
assert q(s0)==Fraction(1,2) and V(s0)==1 and A[1][s0]==0
B_s=V(s0)-D[1]
B_terminal=-D[1]+Fraction(3,4)*D[1]
edge_increase=B_terminal-B_s
assert edge_increase==Fraction(7,8)
a,b=queries(s0)[0]
reg=1+(V(a)+V(b))/2-V(s0)
assert reg==0

print('C0021 B8/B20/B29 exact self-check')
print('D', *D)
print('B8_child_states', len(A[3]))
print('B8_abstract_classes', len(classes))
print('B8_abstract_outer_DP_states', AB.cache_info().currsize)
print('B8_abstract_upper_beta3', abs_beta3)
print('B8_abstract_upper_beta3_decimal', float(abs_beta3))
print('B8_previous_rho3', rho3, float(rho3))
print('B20_exact_beta2', raw2/D[2])
print('B20_optimal_reachable_outer_states', len(reach))
print('B20_posterior_signature_policy_collisions', posterior_collision_count)
print('B20_explicit_collision_signature', posterior_sig(S_A))
print('B20_state_A_optimal_profiles', sorted(profA,key=repr))
print('B20_state_B_optimal_profiles', sorted(profB,key=repr))
print('B20_h2_qV_classes', len(qv))
print('B20_h2_qV_collision_WA', [(x[0],x[1]) for x in wv])
print('B20_h3_qW_collision_classes', len(qW_collision_classes))
print('B20_h3_qW_max_collision_size', max(map(len,qW_collision_classes)))
print('B20_h3_explicit_collision_parent_qW', q(S1), W[3][S1])
for h,best,qq,ww,wit in min_rows:
    print('B29_h',h,'min_P2_over_abs_m3',best,'witness_q',qq,'witness_W',ww,'witness',wit)
print('B29_local_zero_regret_edge_increase', edge_increase)
print('ALL_EXACT_B8_B20_B29_CHECKS_PASS')

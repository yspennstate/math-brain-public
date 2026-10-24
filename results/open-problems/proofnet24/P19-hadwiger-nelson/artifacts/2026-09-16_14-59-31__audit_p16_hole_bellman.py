from collections import deque
from functools import lru_cache

Q = frozenset(range(5))
p = (0,1,2,4,3)
q = (1,2,3,0,4)
e = (2,1,2,3,4)
letters = [('p',p),('q',q),('e',e)]
gens = [('p',p),('q',q)]


def apply_map_subset(S, m):
    return frozenset(m[x] for x in S)


def compose_after(u, g):
    # tuple for word u followed by generator g: x -> g(u(x))
    return tuple(g[u[x]] for x in range(5))

# 1) Exact subset BFS reset threshold.
start = Q
D = {start: 0}
parent = {start: None}
move = {}
dq = deque([start])
terminal = None
while dq:
    S = dq.popleft()
    if len(S) == 1:
        terminal = S
        break
    for name,m in letters:
        T = apply_map_subset(S,m)
        if T not in D:
            D[T] = D[S]+1
            parent[T] = S
            move[T] = name
            dq.append(T)
assert terminal is not None
rt = D[terminal]
word=[]
cur=terminal
while parent[cur] is not None:
    word.append(move[cur])
    cur=parent[cur]
word=word[::-1]
assert rt == 14, rt

# verify no singleton reached at <=13 and displayed word resets.
S=Q
for a in word:
    m=dict(letters)[a]
    S=apply_map_subset(S,m)
assert len(S)==1
assert min(v for s,v in D.items() if len(s)==1)==14

# 2) Positive-generator Cayley graph of G=<p,q> and distances/shortest words.
idp=tuple(range(5))
gdist={idp:0}
gword={idp:()}
gdq=deque([idp])
while gdq:
    u=gdq.popleft()
    for name,g in gens:
        v=compose_after(u,g)
        if v not in gdist:
            gdist[v]=gdist[u]+1
            gword[v]=gword[u]+(name,)
            gdq.append(v)
assert len(gdist)==120, len(gdist)

# 3) Bellman values on canonical hole states: 0 in H, 2 not in H.
states=[frozenset(H) for mask in range(1<<5)
        for H in [{i for i in range(5) if mask>>i &1}]
        if 0 in H and 2 not in H]
by_size={k:[] for k in range(1,5)}
for H in states:
    by_size[len(H)].append(H)
Hstar=frozenset({0,1,3,4})
F={Hstar:0}
choice={}
for h in [3,2,1]:
    for H in by_size[h]:
        best=None
        bestu=None
        bestHp=None
        for u,du in gdist.items():
            Hu=frozenset(u[x] for x in H)
            if 0 in Hu or 2 in Hu:
                continue
            Hp=Hu | {0}
            if Hp not in F:
                continue
            val=du+F[Hp]
            if best is None or val<best:
                best=val; bestu=u; bestHp=Hp
        if best is not None:
            F[H]=best; choice[H]=(bestu,bestHp)

expected={
    frozenset({0}):10,
    frozenset({0,1}):10,
    frozenset({0,3}):7,
    frozenset({0,4}):6,
    frozenset({0,1,3}):5,
    frozenset({0,1,4}):5,
    frozenset({0,3,4}):6,
    Hstar:0,
}
assert F==expected, (F, expected)
assert rt == 4 + F[frozenset({0})]

# 4) Final stage set-transport costs among p,q.
target=frozenset({1,3,4})
three=[frozenset({0,1,3}),frozenset({0,1,4}),frozenset({0,3,4})]
transport={}
for H in three:
    best=None; bestword=None
    for u,du in gdist.items():
        if frozenset(u[x] for x in H)==target:
            if best is None or du<best:
                best=du; bestword=gword[u]
    transport[H]=(best,bestword)
assert [transport[H][0] for H in three]==[5,5,6], transport

# Verify the report's explicit words using q=1,p=0 notation.
reported={
    frozenset({0,1,3}):('q','q','q','p','q'),
    frozenset({0,1,4}):('q','p','q','p','q'),
    frozenset({0,3,4}):('q','q','p','q','p','q'),
}
for H,w in reported.items():
    S=H
    for name in w:
        S=apply_map_subset(S, dict(gens)[name])
    assert S==target, (H,w,S)
    assert len(w)==transport[H][0]

print('peer_report', 'hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T11-05-00Z__report.md')
print('peer_blob', '3ce4f8146fcafa2fa4cffee23e8a504237309d9f')
print('group_size', len(gdist))
print('reset_threshold', rt)
print('one_shortest_reset_word', ''.join(word))
print('bellman_values')
for H in sorted(F, key=lambda h:(len(h),tuple(sorted(h)))):
    print(' ', tuple(sorted(H)), F[H])
print('final_stage_transport_costs')
for H in three:
    cost,w=transport[H]
    print(' ', tuple(sorted(H)), '->', tuple(sorted(target)), 'cost', cost, 'word', ''.join(w))
print('ALL_CHECKS_PASSED')

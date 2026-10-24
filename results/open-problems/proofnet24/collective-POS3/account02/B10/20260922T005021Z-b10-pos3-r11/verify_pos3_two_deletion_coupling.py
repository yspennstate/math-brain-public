from itertools import combinations
from fractions import Fraction

N = 7
COVERS = {(0,1),(1,3),(0,5),(4,5),(3,6),(4,6)}
X, Y = 4, 2
S, T = 5, 6

def transitive_closure(n, rel):
    R = set(rel)
    changed = True
    while changed:
        changed = False
        add = set()
        for a,b in R:
            for c,d in R:
                if b == c and (a,d) not in R:
                    add.add((a,d))
        if add:
            R |= add
            changed = True
    return R

R = transitive_closure(N, COVERS)

def lt(a,b):
    return (a,b) in R

def incomparable(a,b):
    return a != b and not lt(a,b) and not lt(b,a)

def linear_extensions(vertices):
    V = tuple(sorted(vertices))
    pred = {v:{u for u in V if lt(u,v)} for v in V}
    out = []
    def rec(prefix, remaining):
        if not remaining:
            out.append(tuple(prefix))
            return
        Srem = set(remaining)
        mins = [v for v in remaining if pred[v].isdisjoint(Srem)]
        for v in mins:
            rec(prefix+[v], tuple(w for w in remaining if w != v))
    rec([], V)
    return out

LE = linear_extensions(range(N))
E = len(LE)

def before_count(a,b, exts=LE):
    return sum(L.index(a) < L.index(b) for L in exts)

width = 0
witness = None
for r in range(1,N+1):
    for A in combinations(range(N), r):
        if all(incomparable(a,b) for a,b in combinations(A,2)):
            if r > width:
                width = r
                witness = A

P_y_x = {z for z in range(N) if lt(z,Y) and incomparable(z,X)}
S_x_y = {z for z in range(N) if lt(X,z) and incomparable(z,Y)}
Mminus = {z for z in P_y_x if not any(lt(z,w) for w in P_y_x)}
Mplus = {z for z in S_x_y if not any(lt(w,z) for w in S_x_y)}

assert width == 3
assert E == 91
assert P_y_x == set()
assert S_x_y == {5,6}
assert Mminus == set()
assert Mplus == {5,6}

pair_counts = {
    "x<y": before_count(X,Y),
    "y<s": before_count(Y,S),
    "y<t": before_count(Y,T),
    "s<t": before_count(S,T),
    "1<2": before_count(1,2),
}
assert pair_counts == {"x<y":62, "y<s":62, "y<t":74, "s<t":63, "1<2":55}

Q = [v for v in range(N) if v not in (X,Y)]
LEQ = linear_extensions(Q)

def interval_for(z, tau):
    pos = {v:i+1 for i,v in enumerate(tau)}
    m = len(tau)
    lower = max([pos[a] for a in tau if lt(a,z)] or [0])
    upper = min([pos[b]-1 for b in tau if lt(z,b)] or [m])
    assert 0 <= lower <= upper <= m
    return lower, upper

sum_T = sum_xy = sum_yx = sum_delta = 0
pos_delta = neg_delta = 0
routed = {S:0,T:0}
for tau in LEQ:
    Lx,Rx = interval_for(X,tau)
    Ly,Ry = interval_for(Y,tau)
    Ix = list(range(Lx,Rx+1))
    Iy = list(range(Ly,Ry+1))
    inter = set(Ix) & set(Iy)
    less = sum(i < j for i in Ix for j in Iy)
    greater = sum(i > j for i in Ix for j in Iy)
    Ttau = len(Ix)*len(Iy)+len(inter)
    Nxy = less + len(inter)
    Nyx = greater + len(inter)
    delta = less-greater
    assert Ttau == Nxy+Nyx

    H = (Ly+Ry)-(Lx+Rx)
    if H > 0:
        strip = sum(1 <= j-i <= H for i in Ix for j in Iy)
        assert delta == strip and delta > 0
        assert Ly <= Lx
        assert Ry > Rx
        pos = {v:k+1 for k,v in enumerate(tau)}
        x_only_succ = [z for z in tau if lt(X,z) and not lt(Y,z)]
        earliest = min(x_only_succ, key=lambda z:pos[z])
        assert pos[earliest] == Rx+1
        assert earliest in (S,T)
        routed[earliest] += delta
        pos_delta += delta
    elif H < 0:
        strip = -sum(H <= j-i <= -1 for i in Ix for j in Iy)
        assert delta == strip and delta < 0
        neg_delta += -delta
    else:
        assert delta == 0

    sum_T += Ttau
    sum_xy += Nxy
    sum_yx += Nyx
    sum_delta += delta

assert sum_T == E
assert sum_xy == pair_counts["x<y"]
assert sum_yx == E-pair_counts["x<y"]
assert sum_delta == sum_xy-sum_yx == 33
assert pos_delta - neg_delta == 33
assert sum(routed.values()) == pos_delta

p = Fraction(sum_xy, E)
p_from_delta = Fraction(1,2) + Fraction(sum_delta, 2*sum_T)
assert p == p_from_delta == Fraction(62,91)

def predecessor_blockers(a,b):
    return {z for z in range(N) if lt(z,b) and incomparable(z,a)}
def max_elements(Sset):
    return {z for z in Sset if not any(lt(z,w) for w in Sset)}
for blocker in (S,T):
    assert X in max_elements(predecessor_blockers(Y,blocker))

print("POS3_TWO_DELETION_COUPLING_CHECK_PASS")
print("n =", N, "width =", width, "width_witness =", witness, "extensions =", E)
print("transitive_relations =", sorted(R))
print("canonical_positive_blockers =", sorted(Mplus), "canonical_negative_blockers =", sorted(Mminus))
for k,v in pair_counts.items():
    print(k, "=", v, "/", E, "=", Fraction(v,E))
print("Q_extensions =", len(LEQ))
print("fiber_sums: T =", sum_T, "N_xy =", sum_xy, "N_yx =", sum_yx, "Delta =", sum_delta)
print("positive_delta =", pos_delta, "negative_delta =", neg_delta, "routed =", routed)
print("p_xy_from_delta =", p_from_delta)

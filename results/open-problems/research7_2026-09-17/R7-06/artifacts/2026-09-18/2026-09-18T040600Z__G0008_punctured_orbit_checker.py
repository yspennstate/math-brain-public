import itertools
import sympy as sp

p = sp.symbols("p")
q = 1-p

# Around the deleted central vertex y, order the four neighbours cyclically as
# 0=x, 1=u, 2=z, 3=d.  Vertex 4 is y and only yu,yd are restored when
# reconstructing the two-edge slit graph H.

def canon(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))

def partitions(xs):
    if not xs:
        yield []
        return
    x = xs[0]
    for rest in partitions(xs[1:]):
        yield [{x}] + [set(b) for b in rest]
        for i in range(len(rest)):
            rr = [set(b) for b in rest]
            rr[i].add(x)
            yield rr

parts = {canon(z) for z in partitions([0,1,2,3])}
# Alternating opposite-pair partition cannot occur as two disjoint clusters in
# a planar graph with these terminals in cyclic order.
cross = canon([{0,2},{1,3}])
parts = parts - {cross}
assert len(parts) == 14

def dsu_class(pt, ou, od):
    parent = list(range(5))
    def f(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a,b):
        a,b = f(a),f(b)
        if a != b:
            parent[b] = a
    for block in pt:
        block = list(block)
        for v in block[1:]:
            union(block[0],v)
    if ou:
        union(4,1)
    if od:
        union(4,3)
    xy = f(0) == f(4)
    xz = f(0) == f(2)
    yz = f(4) == f(2)
    if xy and xz:
        return "c"
    if xy:
        return "a"
    if yz:
        return "ap"
    if xz:
        return "b"
    return "s"

def B(pt):
    pr = {k:0 for k in ["c","a","ap","b","s"]}
    for ou,od in itertools.product([0,1], repeat=2):
        w = (p if ou else q)*(p if od else q)
        pr[dsu_class(pt,ou,od)] += w
    return sp.expand(pr["a"] - q*pr["b"] + p*pr["s"])

actions = [(sgn,k) for sgn in [1,-1] for k in range(4)]
def trans(pt, act):
    sgn,k = act
    return canon([{(sgn*i+k)%4 for i in b} for b in pt])
def orbit(pt):
    return {trans(pt,a) for a in actions} & parts

orbits=[]
seen=set()
for pt in sorted(parts):
    if pt not in seen:
        O=orbit(pt)
        orbits.append(O)
        seen |= O

def typ(O):
    pt = next(iter(O))
    sizes = sorted(map(len,pt), reverse=True)
    if sizes == [1,1,1,1]:
        return "sigma"
    if sizes == [2,1,1]:
        pair = [b for b in pt if len(b)==2][0]
        a,b = sorted(pair)
        return "beta" if (a-b)%2 == 0 else "alpha"
    if sizes == [2,2]:
        return "gamma"
    if sizes == [3,1]:
        return "delta"
    if sizes == [4]:
        return "epsilon"
    raise AssertionError(sizes)

sums={}
for O in orbits:
    sums[typ(O)] = sp.factor(sum(B(pt) for pt in O))

expected={
    "sigma": p,
    "alpha": 2*p*(1+2*q),
    "beta": p-q,
    "gamma": 2*p*q*(1+q),
    "delta": 1-q**2-2*q**3,
    "epsilon": -q**3,
}
for k,v in expected.items():
    assert sp.expand(sums[k]-v) == 0

print("NONCROSSING_PARTITIONS", len(parts))
for k in ["sigma","alpha","beta","gamma","delta","epsilon"]:
    print(k, "=", sp.expand(sums[k]))

half={k:sp.simplify(v.subs(p,sp.Rational(1,2))) for k,v in expected.items()}
print("AT_P_HALF", half)
assert half == {
    "sigma":sp.Rational(1,2),
    "alpha":sp.Integer(2),
    "beta":sp.Integer(0),
    "gamma":sp.Rational(3,4),
    "delta":sp.Rational(1,2),
    "epsilon":sp.Rational(-1,8),
}

# For critical self-duality, condition the horizontal edge xy closed and restore
# the other three star edges.  If m_x is the number of {u,z,d} in x's K-cluster,
# then the conditional failure probability is 2^{-m_x}.  These are its D4-orbit
# sums.
def mx(pt):
    for b in pt:
        if 0 in b:
            return len(set(b) & {1,2,3})
weights={}
for O in orbits:
    weights[typ(O)] = sum(sp.Rational(1,2)**mx(pt) for pt in O)
print("DUAL_ORBIT_WEIGHTS", weights)
assert weights == {
    "sigma":1,
    "alpha":3,
    "beta":sp.Rational(3,2),
    "gamma":1,
    "delta":sp.Rational(7,4),
    "epsilon":sp.Rational(1,8),
}

S,A,B,G,D,E = sp.symbols("S A B G D E", nonnegative=True)
norm = S+4*A+2*B+2*G+4*D+E
dual = S+3*A+sp.Rational(3,2)*B+G+sp.Rational(7,4)*D+sp.Rational(1,8)*E
relation = sp.expand(8*(dual-sp.Rational(1,2)*norm))
assert relation == 4*S+8*A+4*B-2*D-3*E
print("DUAL_RELATION", relation, "= 0")

Bcrit = sp.Rational(1,2)*S+2*A+sp.Rational(3,4)*G+sp.Rational(1,2)*D-sp.Rational(1,8)*E
Esub = (4*S+8*A+4*B-2*D)/3
Bcrit2 = sp.expand(Bcrit.subs(E,Esub))
assert Bcrit2 == S/sp.Integer(3)+5*A/sp.Integer(3)-B/sp.Integer(6)+3*G/sp.Integer(4)+7*D/sp.Integer(12)
print("BCRIT_AFTER_DUAL", Bcrit2)

# Let T=P_K(x<->z)=B+2D+E.  Planarity plus FKG imply E >= T^2:
# the events x<->z and u<->d have the same probability T, and their intersection
# forces all four terminals into one cluster.
T = sp.symbols("T", nonnegative=True)
sol = sp.solve([
    sp.Eq(norm,1),
    sp.Eq(4*S+8*A+4*B-2*D-3*E,0),
    sp.Eq(B+2*D+E,T),
],[S,A,B], dict=True)[0]
for key in [S,A,B]:
    print(str(key)+" =", sp.factor(sol[key]))
bcT = sp.factor(Bcrit.subs(sol))
print("8Bcrit =", sp.expand(8*bcT))

# A>=0 gives G <= 1/2-3E/8-T/2-5D/4 and, after dropping G,D,
# T <= 1-3E/4.  With E>=T^2 this gives T<=2/3.
Gmax = sp.Rational(1,2)-3*E/sp.Integer(8)-T/sp.Integer(2)-5*D/sp.Integer(4)
lb = sp.expand((8*bcT).subs(G,Gmax))
print("LOWER_BOUND_BEFORE_FKG", lb)
assert lb == 3+sp.Rational(15,4)*E-7*T+sp.Rational(13,2)*D
quad = sp.factor(3+sp.Rational(15,4)*T**2-7*T)
print("LOWER_BOUND_AFTER_FKG", quad)
assert sp.expand(quad-sp.Rational(15,4)*(T-sp.Rational(2,3))*(T-sp.Rational(6,5))) == 0
print("ALL_EXACT_CHECKS_PASS")

from fractions import Fraction
from itertools import combinations

def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
    return True

def weighted_derivatives(n, edges, weights):
    m = len(edges)
    P = Fraction(0)
    P_i = [Fraction(0) for _ in range(m)]
    P_ij = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for mask in range(1 << m):
        if not is_forest(n, edges, mask):
            continue
        w = Fraction(1)
        chosen = []
        for i in range(m):
            if (mask >> i) & 1:
                w *= weights[i]
                chosen.append(i)
        P += w
        for i in chosen:
            P_i[i] += w / weights[i]
        for i, j in combinations(chosen, 2):
            x = w / (weights[i] * weights[j])
            P_ij[i][j] += x
            P_ij[j][i] += x
    return P, P_i, P_ij

def two_terminal_masses(n, edges, s, t):
    D = C = 0
    for mask in range(1 << len(edges)):
        if not is_forest(n, edges, mask):
            continue
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                parent[rv] = ru
        if find(s) == find(t):
            C += 1
        else:
            D += 1
    return D, C

def build_lift(host_n, host_edges, doubled):
    edges = []
    representative = {}
    next_vertex = host_n
    for i, (u, v) in enumerate(host_edges):
        if i not in doubled:
            representative[i] = len(edges)
            edges.append((u, v))
            continue
        representative[i] = len(edges)
        edges.append((u, v))
        for _ in range(3):
            w = next_vertex
            next_vertex += 1
            edges.extend([(u, w), (w, v)])
    return next_vertex, edges, representative

# K3 rank-degree candidate: h(y,z)=y^2+3yz+3z^2.
f = Fraction(7)
fy, fz = Fraction(5), Fraction(9)
fyy, fyz, fzz = Fraction(2), Fraction(3), Fraction(6)
Hyy = fyy/f - (fy/f)**2
Hyz = fyz/f - (fy/f)*(fz/f)
Hzz = fzz/f - (fz/f)**2
det = Hyy*Hzz - Hyz**2
assert (Hyy, Hyz, Hzz, det) == (
    Fraction(-11,49), Fraction(-24,49),
    Fraction(-39,49), Fraction(-3,49)
)
assert det < 0

theta = []
next_vertex = 2
for _ in range(3):
    w = next_vertex
    next_vertex += 1
    theta.extend([(0,w),(w,1)])
theta_D, theta_C = two_terminal_masses(next_vertex, theta, 0, 1)
direct_theta_D, direct_theta_C = two_terminal_masses(
    next_vertex, [(0,1)] + theta, 0, 1
)
assert (theta_D, theta_C) == (27,27)
assert (direct_theta_D, direct_theta_C) == (27,54)

# Triangle host with two weight-2 edges; replace each by direct+theta_3.
host_edges = [(0,1),(0,2),(1,2)]
host_weights = [Fraction(2), Fraction(2), Fraction(1)]
P, P_i, P_ij = weighted_derivatives(3, host_edges, host_weights)
lift_n, lift_edges, rep = build_lift(3, host_edges, {0,1})
LP, LP_i, LP_ij = weighted_derivatives(
    lift_n, lift_edges, [Fraction(1)] * len(lift_edges)
)
scale = Fraction(27**2)
assert LP == scale * P
for i in range(3):
    assert LP_i[rep[i]] == scale * P_i[i]
for i, j in combinations(range(3), 2):
    assert LP_ij[rep[i]][rep[j]] == scale * P_ij[i][j]
    gap = P_i[i]*P_i[j] - P*P_ij[i][j]
    lift_gap = LP_i[rep[i]]*LP_i[rep[j]] - LP*LP_ij[rep[i]][rep[j]]
    assert lift_gap == scale**2 * gap

print("K3_RANK_HOMOG_HESSLOG", Hyy, Hyz, Hzz, "DET", det)
print("K3_RANK_HOMOG_STATUS=NOT_LOG_CONCAVE")
print("THETA3_MASSES", theta_D, theta_C, "ACTIVITY", Fraction(theta_C, theta_D))
print("DIRECT_PLUS_THETA3_MASSES", direct_theta_D, direct_theta_C,
      "ACTIVITY", Fraction(direct_theta_C, direct_theta_D))
print("WEIGHT2_HOST", "P", P, "P_i", P_i)
print("LIFT", "vertices", lift_n, "edges", len(lift_edges),
      "P", LP, "scale", scale)
for i, j in combinations(range(3), 2):
    gap = P_i[i]*P_i[j] - P*P_ij[i][j]
    lift_gap = LP_i[rep[i]]*LP_i[rep[j]] - LP*LP_ij[rep[i]][rep[j]]
    print("PAIR", i, j, "HOST_GAP", gap, "LIFT_GAP", lift_gap,
          "RATIO", Fraction(lift_gap, gap) if gap else "NA")
print("STATUS=ALL_EXACT_CHECKS_PASS")

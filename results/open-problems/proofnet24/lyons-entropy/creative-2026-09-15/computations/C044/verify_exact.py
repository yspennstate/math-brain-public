"""C044 conditional bridge induction. Exact rational arithmetic, standard library.

No diamond feasibility solver is used: all transports are ordinary one-rank
inclusion flows whose Hall conditions are proved in the accompanying report.
"""
from collections import defaultdict, deque
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def det(a):
    a = [list(map(Q, row)) for row in a]
    out = Q(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[j], a[k] = a[k], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for k in range(j+1, len(a)):
            t = a[k][j]/p
            for l in range(j+1, len(a)):
                a[k][l] -= t*a[j][l]
    return out


def combine(a, x, b, y):
    return [a*xx+b*yy for xx, yy in zip(x, y)]


def householder(h):
    d = dot(h, h)
    return [[Q(int(i == j))-2*Q(h[i]*h[j], d)
             for j in range(len(h))] for i in range(len(h))]


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def law(columns, sites):
    """Projection law; columns may be nonnormalized rational orthogonal vectors."""
    gram = det([[dot(x, y) for y in columns] for x in columns])
    assert gram > 0
    ans = {s: det([[c[i] for c in columns] for i in s])**2/gram
           for s in combinations(sites, len(columns))}
    assert sum(ans.values()) == 1
    return ans


def inclusion_flow(left, right):
    """Exact Edmonds--Karp (same standard construction used by C038/C040)."""
    assert all(z >= 0 for z in list(left.values())+list(right.values()))
    mass = sum(left.values())
    assert mass == sum(right.values())
    ls, rs = list(left), list(right)
    sink = len(ls)+len(rs)+1
    cap = [[Q(0) for _ in range(sink+1)] for _ in range(sink+1)]
    adj = [[] for _ in range(sink+1)]

    def arc(i, j, v):
        cap[i][j] = v
        adj[i].append(j)
        adj[j].append(i)

    for i, s in enumerate(ls):
        arc(0, 1+i, left[s])
    for j, t in enumerate(rs):
        arc(1+len(ls)+j, sink, right[t])
    for i, s in enumerate(ls):
        for j, t in enumerate(rs):
            if set(s) <= set(t):
                arc(1+i, 1+len(ls)+j, 2*mass)
    sent = Q(0)
    while True:
        prev = [None]*(sink+1)
        prev[0] = 0
        queue = deque([0])
        while queue and prev[sink] is None:
            i = queue.popleft()
            for j in adj[i]:
                if prev[j] is None and cap[i][j] > 0:
                    prev[j] = i
                    queue.append(j)
        if prev[sink] is None:
            break
        v = 2*mass
        j = sink
        while j:
            v = min(v, cap[prev[j]][j])
            j = prev[j]
        j = sink
        while j:
            i = prev[j]
            cap[i][j] -= v
            cap[j][i] += v
            j = i
        sent += v
    assert sent == mass, (sent, mass)
    result = {(s, t): cap[1+len(ls)+j][1+i]
              for i, s in enumerate(ls) for j, t in enumerate(rs)
              if set(s) <= set(t) and cap[1+len(ls)+j][1+i]}
    assert all(v > 0 for v in result.values())
    assert {s: sum(v for (a, _), v in result.items() if a == s)
            for s in left} == left
    assert {t: sum(v for (_, b), v in result.items() if b == t)
            for t in right} == right
    return result


def transport_diamonds(flow):
    """Pair B inside triple T gives bottom T minus B and top T."""
    return {(tuple(sorted(set(t)-set(b))), t): v
            for (b, t), v in flow.items()}


def marginals(x, sites, rank):
    bottom = {s: Q(0) for s in combinations(sites, rank)}
    top = {s: Q(0) for s in combinations(sites, rank+2)}
    middle = {s: Q(0) for s in combinations(sites, rank+1)}
    added = {s: Q(0) for s in combinations(sites, 2)}
    for (s, t), v in x.items():
        assert v > 0 and set(s) < set(t) and len(t) == len(s)+2
        j = tuple(sorted(set(t)-set(s)))
        bottom[s] += v
        top[t] += v
        added[j] += v
        for i in j:
            middle[tuple(sorted(s+(i,)))] += v
    return bottom, top, middle, added


def hall_data(hg, cg, hk, ck):
    pairs, triples = list(hg), list(cg)
    ratios = [(Q(1), {"kind": "mass"})]
    ratios += [(hg[s]/hk[s], {"kind": "pair", "set": s})
               for s in pairs if hk[s]]
    ratios += [(cg[s]/ck[s], {"kind": "triple", "set": s})
               for s in triples if ck[s]]
    slacks = []
    for mask in range(1, (1 << len(pairs))-1):
        family = [s for j, s in enumerate(pairs) if mask >> j & 1]
        shadow = [t for t in triples if any(set(s) <= set(t) for s in family)]
        sg = sum(cg[t] for t in shadow)-sum(hg[s] for s in family)
        sk = sum(ck[t] for t in shadow)-sum(hk[s] for s in family)
        assert sg > 0 and sk >= 0
        slacks.append((sg, sk))
        if sk:
            ratios.append((sg/sk, {"kind": "Hall", "family": family}))
    threshold, witness = min(ratios, key=lambda z: z[0])
    return threshold, witness, slacks


def tables(table):
    return [{"set": list(s), "mass": str(v)} for s, v in sorted(table.items())]


def flow_table(flow):
    return [{"left": list(s), "right": list(t), "mass": str(v)}
            for (s, t), v in sorted(flow.items())]


def build(epsilon, filename, require_bound=False):
    sites = tuple(range(5))
    full = tuple(range(6))
    e = 5
    # C038's two-reflection rational orthogonal seed, now used at a positive
    # update coordinate. Columns are A, f, v, k, z0.
    seed = matmul(householder([1, 2, 3, 4, 5]),
                  householder([2, -1, 3, -2, 1]))
    av, f, v, k, z0 = [list(c) for c in zip(*seed)]
    assert all(dot(x, y) == int(i == j)
               for i, x in enumerate([av, f, v, k, z0])
               for j, y in enumerate([av, f, v, k, z0]))
    ct, st = Q(3, 5), Q(4, 5)
    cp = (1-epsilon**2)/(1+epsilon**2)
    sp = 2*epsilon/(1+epsilon**2)
    a, b, c = (cp*ct)**2, (sp*ct)**2, st**2
    lam = b/(1-a)
    x = combine(sp, f, cp*st, k)
    g = combine(cp*st, f, -sp, k)
    assert dot(x, x) == dot(g, g) == 1-a and dot(x, g) == 0
    hg, cg = law([g, v], sites), law([z0, g, v], sites)
    hk, ck = law([k, v], sites), law([z0, k, v], sites)
    zmin = min(t**2 for t in z0)
    hmin, cmin = min(hg.values()), min(cg.values())
    eta = min(cmin, zmin*hmin)
    assert 0 < lam and eta > 0
    if require_bound:
        assert lam < eta
    threshold, witness, slacks = hall_data(hg, cg, hk, ck)
    assert eta <= threshold and lam < threshold
    assert all(sg >= zmin*hmin for sg, sk in slacks)
    residual_h = {s: (b+c)*hg[s]-b*hk[s] for s in hg}
    residual_c = {s: (b+c)*cg[s]-b*ck[s] for s in cg}
    accelerated = [[cp**2, -cp*sp/st], [-cp*sp/st, sp**2]]
    assert det(accelerated) == -a*b/(c*(a+b)) < 0
    for residual, fixed in ((residual_h, []), (residual_c, [z0])):
        for subset, weight in residual.items():
            afamp = det([[col[i] for col in fixed+[f, v]] for i in subset])
            akamp = det([[col[i] for col in fixed+[k, v]] for i in subset])
            assert weight/c == cp**2*afamp**2+sp**2*akamp**2-2*cp*sp/st*afamp*akamp
    assert all(z > 0 for z in list(residual_h.values())+list(residual_c.values()))
    assert all(sg-lam*sk > 0 for sg, sk in slacks)
    absence_flow = inclusion_flow(residual_h, residual_c)
    presence_flow = inclusion_flow(law([f, v], sites), law([av, f, v], sites))
    bridge_flow = inclusion_flow(law([av, f], sites), law([av, f, v], sites))
    out = defaultdict(Q)
    # Modified deletion face: complement a rank-one transport within F.
    for (s, t), wt in transport_diamonds(absence_flow).items():
        bottom = tuple(j for j in sites if j not in t)
        top = tuple(j for j in sites if j not in s)
        out[bottom, top] += wt
    # Certified contraction face, with the new coordinate inserted everywhere.
    for (s, t), wt in transport_diamonds(presence_flow).items():
        out[tuple(sorted(s+(e,))), tuple(sorted(t+(e,)))] += a*wt
    # One common bridge cover; its two middle vertices are its two endpoints,
    # with e inserted at the lower endpoint only.
    for (s, t), wt in bridge_flow.items():
        out[s, tuple(sorted(t+(e,)))] += b*wt
    assert sum(out.values()) == 1
    w = [cp*st*z+sp*y for z, y in zip(k, f)]+[cp*ct]
    u = [sp*st*z-cp*y for z, y in zip(k, f)]+[sp*ct]
    z = [-ct*y for y in k]+[st]
    av6, v6, z06 = av+[Q(0)], v+[Q(0)], z0+[Q(0)]
    columns = [av6, w, u, v6, z, z06]
    assert all(dot(x, y) == int(i == j) for i, x in enumerate(columns)
               for j, y in enumerate(columns))
    bottom, top, middle, added = marginals(out, full, 2)
    want_bottom = law(columns[:2], full)
    want_top = law(columns[:4], full)
    mu_u, mu_v = law(columns[:3], full), law(columns[:2]+[v6], full)
    want_middle = {s: mu_u[s]+mu_v[s] for s in middle}
    want_added = law([u, v6], full)
    assert bottom == want_bottom and top == want_top
    assert middle == want_middle and added == want_added
    assert min(bottom.values()) > 0 and min(top.values()) > 0
    assert min(added.values()) > 0
    masses = [[sum(columns[j][i]**2 for j in idx) for idx in
               [(0, 1), (2, 3), (4, 5)]] for i in full]
    assert all(t > 0 for row in masses for t in row)
    # Conditional identity and naive bridge mismatch checked at every atom.
    ax, af = law([av, x], sites), law([av, f], sites)
    axv, afv = law([av, x, v], sites), law([av, f, v], sites)
    assert ax != af and axv != afv
    for s in combinations(sites, 2):
        assert want_bottom[s] == (b+c)*ax[s]
    for s in combinations(sites, 1):
        assert want_bottom[s+(e,)] == a*law([av], sites)[s]
    for s in combinations(sites, 4):
        assert want_top[s] == c*law([av, f, k, v], sites)[s]
    for s in combinations(sites, 3):
        assert want_top[s+(e,)] == (a+b)*afv[s]
        assert want_middle[s] == c*law([av, f, k], sites)[s]+(b+c)*axv[s]
    for s in combinations(sites, 2):
        assert want_middle[s+(e,)] == (a+b)*af[s]+a*law([av, v], sites)[s]
    mismatch = next(s for s in ax if ax[s] != af[s])
    certificate = {
        "seed_columns_A_f_v_k_z0": [[str(z) for z in col] for col in
                                    [av, f, v, k, z0]],
        "frame_columns_A_w_u_v_z_z0": [[str(z) for z in col] for col in columns],
        "epsilon": str(epsilon), "new_coordinate": e,
        "coordinate_color_masses_W_U_Z": [[str(z) for z in row] for row in masses],
        "parameters": {key: str(val) for key, val in
                       {"a": a, "b": b, "c": c, "lambda": lam,
                        "eta": eta, "sharp_threshold": threshold,
                        "zmin": zmin, "hmin": hmin, "cmin": cmin}.items()},
        "sharp_threshold_witness": witness,
        "minimum_residual_Hall_slack": str(min((b+c)*(sg-lam*sk) for sg, sk in slacks)),
        "naive_bridge_mismatch": {"set": list(mismatch),
                                   "mu_Ax": str(ax[mismatch]), "mu_Af": str(af[mismatch])},
        "absence_modified_pair_marginal": tables(residual_h),
        "absence_modified_triple_marginal": tables(residual_c),
        "absence_flow": flow_table(absence_flow),
        "presence_flow": flow_table(presence_flow),
        "bridge_flow": flow_table(bridge_flow),
        "diamonds": [{"bottom": list(s), "top": list(t), "mass": str(wt)}
                     for (s, t), wt in sorted(out.items())],
        "bottom": tables(bottom), "top": tables(top),
        "aggregate_middle": tables(middle), "added_pair": tables(added),
    }
    (HERE/filename).write_text(json.dumps(certificate, indent=2)+"\n")
    summary = {
        "status": "PASS", "arithmetic": "exact rational",
        "hall_families": len(slacks), "projection_marginal_equations": 65,
        "positive_diamonds": len(out),
        "absence_atoms": len(absence_flow), "presence_atoms": len(presence_flow),
        "bridge_atoms": len(bridge_flow),
        "all_18_coordinate_color_masses_positive": True,
        "all_15_bottom_top_and_added_pair_atoms_positive": True,
        "lambda_float_for_display": float(lam), "eta_float_for_display": float(eta),
        "threshold_float_for_display": float(threshold),
        "canonical_faces_have_nonzero_bridge_mismatch": True,
        "accelerated_residual_operator_has_negative_determinant": True,
        "simple_bound_passes": lam < eta,
    }
    return summary


def obstruction():
    seed = matmul(householder([1, 2, 3, 4, 5]),
                  householder([2, -1, 3, -2, 1]))
    av, f, v, k, z0 = [list(c) for c in zip(*seed)]
    sites = tuple(range(5))
    epsilon = Q(1, 5)
    cp = (1-epsilon**2)/(1+epsilon**2)
    sp = 2*epsilon/(1+epsilon**2)
    a, b, c = (cp*Q(3, 5))**2, (sp*Q(3, 5))**2, Q(4, 5)**2
    g = combine(cp*Q(4, 5), f, -sp, k)
    hg, hk = law([g, v], sites), law([k, v], sites)
    pair = (0, 2)
    residual = (b+c)*hg[pair]-b*hk[pair]
    assert residual < 0
    data = {"epsilon": str(epsilon), "pair": list(pair),
            "a": str(a), "b": str(b), "c": str(c),
            "negative_residual_pair_mass": str(residual),
            "meaning": "The fixed canonical bridge cannot be completed by any deletion-face diamond coupling.",
            "not_claimed": "No obstruction to another bridge or the full projection diamond is asserted."}
    (HERE/"canonical_bridge_obstruction.json").write_text(json.dumps(data, indent=2)+"\n")
    return data


def main():
    results = {
        "simple_bound_example": build(Q(1, 10000), "small_parameter_certificate.json", True),
        "positive_coordinate_example": build(Q(1, 10), "positive_coordinate_certificate.json"),
        "canonical_bridge_obstruction": obstruction(),
    }
    (HERE/"verified_output.json").write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

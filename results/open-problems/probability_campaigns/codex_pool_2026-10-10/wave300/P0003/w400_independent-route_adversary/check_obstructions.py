"""Bounded exact diagnostics; no SAW scaling simulation or formal proof receipt."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def on_segment(a, b, p):
    return orient(a, b, p) == 0 and all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def intersects(a, b, c, d):
    oa, ob, oc, od = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
    if oa*ob < 0 and oc*od < 0:
        return True
    return any((o == 0 and on_segment(u, v, p)) for o, u, v, p in
               [(oa, a, b, c), (ob, a, b, d), (oc, c, d, a), (od, c, d, b)])


def simple(points):
    if any(a == b for a, b in zip(points, points[1:])):
        return False
    edges = list(zip(points, points[1:]))
    return all(not intersects(*edges[i], *edges[j])
               for i, j in combinations(range(len(edges)), 2) if j > i+1)


def all_paths(graph, a, b, forbidden=frozenset()):
    stack, found = [(a,)], []
    while stack:
        path = stack.pop()
        if path[-1] == b:
            found.append(path)
        else:
            for v in graph[path[-1]]:
                if v not in path and v not in forbidden:
                    stack.append(path+(v,))
        assert len(stack)+len(found) <= 1000, "compute path cap"
    return sorted(found)


def main():
    gate = json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    assert gate['allow'] is True, "fresh gate did not allow this run"
    assert 0 <= time.time()-gate['checked_unix'] <= 120, "gate expired"
    started, cpu_started = time.monotonic(), time.process_time()
    graph = {i: set() for i in range(10)}
    for cycle in [(0, 1, 2, 3, 4, 5), (2, 6, 7, 8, 9, 3)]:
        for a, b in zip(cycle, cycle[1:]+cycle[:1]):
            graph[a].add(b); graph[b].add(a)
    paths = all_paths(graph, 0, 8)
    expected = sorted([(0,1,2,6,7,8), (0,1,2,3,9,8),
                       (0,5,4,3,9,8), (0,5,4,3,2,6,7,8)])
    assert paths == expected
    deleted = all_paths(graph, 0, 8, frozenset({6}))
    assert deleted == [p for p in expected if 6 not in p]
    finite = []
    for x in [F(1,4), F(1,2), F(3,4)]:
        z = sum(x**(len(p)-1) for p in paths)
        za = sum(x**(len(p)-1) for p in deleted)
        avoid = za/z
        assert avoid == F(2)/(3+x*x)
        uniform_given_length_5 = [p for p in paths if len(p)-1 == 5]
        assert len(uniform_given_length_5) == 3
        assert all(x**5/sum(x**5 for _ in uniform_given_length_5) == F(1,3)
                   for _ in uniform_given_length_5)
        first_branch = sum(x**(len(p)-1) for p in paths if p[1] == 1)/z
        assert first_branch == F(2)/(3+x*x)
        finite.append({'x':str(x),'paths':len(paths),'survivors':len(deleted),
                       'avoidance_ratio':str(avoid),'prob_first_branch_1':str(first_branch),
                       'naive_uniform_first_branch':'1/2'})
    geometry, conditioning = [], []
    slit = ((F(0), F(-1)), (F(0), F(0)))
    limit = [(-2,0), (0,0), (2,0)]
    assert any(intersects(a,b,*slit) for a,b in zip(limit,limit[1:]))
    for n in [2, 4, 8, 16, 32]:
        plus, minus = [(-2,0),(0,F(1,n)),(2,0)], [(-2,0),(0,F(-1,n)),(2,0)]
        assert simple(plus) and simple(minus)
        assert not any(intersects(a,b,*slit) for a,b in zip(plus,plus[1:]))
        assert any(intersects(a,b,*slit) for a,b in zip(minus,minus[1:]))
        eps = F(1,n)
        loop = [(-2,0),(0,0),(0,1),(1,1),(1,0),(eps,0),(eps,-eps),(2-eps,-eps),(2,0)]
        assert simple(loop)
        geometry.append({'n':n,'uniform_slit_curve_error':str(eps),
                         'finite_mixture_avoidance':'1/2','limiting_avoidance':'0',
                         'simple_approximating_loop':True})
        length_atoms = [F(k,n) for k in range(1,n+1)]
        assert length_atoms.count(F(1,2)) == 1
        atom_mass = F(1,n)
        plus_joint_mean, minus_joint_mean = atom_mass, -atom_mass
        assert plus_joint_mean/atom_mass == 1 and minus_joint_mean/atom_mass == -1
        conditioning.append({'n':n,'identical_length_marginals':True,
                             'conditioning_atom_probability':str(atom_mass),
                             'total_variation_to_zero_feature_base':str(atom_mass),
                             'conditional_features':[1,-1]})
    probe_matrix = [[F(-1,2), F(-3,4), F(1,4)],
                    [F(1,2), F(-3,4), F(1,4)],
                    [F(-3,4), F(-9,16), F(9,16)]]
    a,b,c = probe_matrix
    determinant = a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    assert determinant == F(9,32)
    inverse = [[F(-1),F(1),F(0)], [F(-5,3),F(-1,3),F(8,9)],
               [F(-3),F(1),F(8,3)]]
    assert [[sum(inverse[i][k]*probe_matrix[k][j] for k in range(3))
             for j in range(3)] for i in range(3)] == [[F(i==j) for j in range(3)] for i in range(3)]
    normalized = [-F(4,3)*row[1]+F(1,2)*row[2] for row in probe_matrix]
    assert normalized == [F(9,8),F(9,8),F(33,32)]
    exponent_cases = []
    for n in [128,256,512,1024]:
        raw = [e/n for e in normalized]
        assert max(raw) < F(1,100) and max(normalized) > F(1,100)
        exponent_cases.append({'n':n,'alpha':str(F(1,n)),
                               'max_raw_relative_drift':str(max(raw)),
                               'max_drift_divided_by_alpha':str(max(normalized)),
                               'actual_variance_rate':'0','required_sle_variance_rate':'8/3'})
    elapsed, cpu = time.monotonic()-started, time.process_time()-cpu_started
    assert cpu < 2 and elapsed < 10, "fresh compute budget exceeded"
    result = {'status':'PASS','formal_proof':False,'elapsed_seconds':elapsed,
              'process_cpu_seconds':cpu,'finite_graph':finite,
              'slit_and_simple_limit':geometry,'rare_length_conditioning':conditioning,
              'three_probe_matrix_determinant':str(determinant),
              'three_probe_inverse_verified':True,'degenerate_exponent':exponent_cases,
              'limitations':'Finite exact diagnostics certify these explicit examples only; no critical SAW scaling convergence is tested.'}
    (ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','finite_fugacity_cases':len(finite),
                      'slit_cases':len(geometry),'rare_length_cases':len(conditioning),
                      'exponent_cases':len(exponent_cases),
                      'elapsed_seconds':elapsed,'process_cpu_seconds':cpu}))


if __name__ == '__main__':
    main()

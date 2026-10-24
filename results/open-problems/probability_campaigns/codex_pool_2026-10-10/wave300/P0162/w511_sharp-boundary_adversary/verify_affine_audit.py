"""Independent exact Walsh checks of every affine subspace up to ambient n=4."""
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from verify_boundary import walsh, entropy, influence, binary

base = Path(__file__).resolve().parent
gate = json.loads((base/"AFFINE_AUDIT_GATE.json").read_text(encoding="utf-8"))
start = time.perf_counter()
cases = 0
max_error = 0.0
counts = {}
for n in range(1, gate["max_ambient_dimension"]+1):
    universe = range(1 << n)
    all_u = {frozenset([0])}
    frontier = all_u.copy()
    while frontier:
        following = set()
        for u in frontier:
            for vector in universe:
                if vector not in u:
                    enlarged = frozenset(set(u) | {x ^ vector for x in u})
                    if enlarged not in all_u:
                        following.add(enlarged)
        all_u |= following
        frontier = following
    counts[n] = 0
    for u in all_u:
        r = len(u).bit_length()-1
        p = Fraction(1, 1 << r)
        active = 0
        for vector in u:
            active |= vector
        m = active.bit_count()
        assert m >= r
        v_space = [t for t in universe if all((t & vector).bit_count()%2 == 0 for vector in u)]
        cosets = {frozenset(a ^ v for v in v_space) for a in universe}
        for a_set in cosets:
            assert time.perf_counter()-start < gate["max_wall_seconds"]
            a = min(a_set)
            f = [-1 if t in a_set else 1 for t in universe]
            wf = walsh(f)
            for index, coefficient in enumerate(wf):
                expected = (1-2*p if index == 0 else
                    -2*p*((-1)**((index & a).bit_count()%2)) if index in u else 0)
                assert Fraction(coefficient, len(wf)) == expected
            assert influence(wf) == 2*p*m
            for bit in range(n):
                assert influence(wf, bit) == (2*p if active & (1 << bit) else 0)
            q = (1-2*p)**2
            empty_term = -float(q)*math.log2(float(q)) if q else 0.0
            expected_h = empty_term + float(8*p*(1-p)*(r-1))
            err = abs(entropy(wf)-expected_h)
            max_error = max(max_error, err)
            assert err < 1e-12
            if r:
                mass = 4*p*(1-p)
                h_q = math.log2((1 << r)-1)
                assert abs(entropy(wf)-binary(float(mass))-float(mass)*h_q) < 1e-12
                assert entropy(wf) <= 4*float(influence(wf))+1e-12
                if r >= 2:
                    assert entropy(wf)/float(influence(wf)) < 4
                    fixed_max = expected_h/float(2*p*r)
                    assert abs(entropy(wf)/float(influence(wf))-(r/m)*fixed_max) < 1e-12
            cases += 1
            counts[n] += 1
            assert cases <= gate["max_constructed_affine_cases"]

for r in range(2, 5):
    count = 1 << r
    wf = walsh([-1] + [1]*(count-1))
    p = Fraction(1,count)
    marginal = influence(wf,0)
    joint = Fraction(sum(v*v for index,v in enumerate(wf) if index & 3 == 3), count*count)
    assert marginal == 2*p and joint == p
    assert binary(float(marginal))/float(marginal) >= r-1
    if r>=3:
        assert joint > marginal*marginal

result = {"command":"python -X utf8 verify_affine_audit.py", "cases":cases,
          "passed":cases, "counts_by_ambient_dimension":counts,
          "max_entropy_formula_error":max_error,
          "wall_seconds":time.perf_counter()-start, "gate":gate,
          "claims":"w510 C001-C004 corroborated; independent written proof audit in AUDIT_W510.md",
          "formal_verification":False}
(base/"affine_audit_measurements.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

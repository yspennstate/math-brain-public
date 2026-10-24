"""Exact bounded sanity checks. No transcendental inequality relies on floats."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import time

start = time.perf_counter()
assertions = 0

def check(test):
    global assertions
    assert test
    assertions += 1

def walsh(values):
    a = values.copy()
    width = 1
    while width < len(a):
        for j in range(0, len(a), 2 * width):
            for k in range(width):
                u, v = a[j+k], a[j+k+width]
                a[j+k], a[j+k+width] = u+v, u-v
        width *= 2
    return a

def audit(values, n):
    size = 1 << n
    raw = walsh(values)
    p = [Q(a*a, size*size) for a in raw]
    check(sum(p) == 1)
    influence = sum(s.bit_count()*v for s, v in enumerate(p))
    physical = sum(Q(sum(values[x] != values[x^(1<<i)] for x in range(size)), size)
                   for i in range(n))
    check(influence == physical)
    if n:
        check(all(a % 2 == 0 for a in raw))
        check(all(v == 0 or v >= Q(4, size*size) for v in p))
    # Every coefficient of the formal logarithm atom has exactly this area:
    # 2 integral_0^infty d*p*exp(-2dt) dt = p for d>0.
    for s, v in enumerate(p):
        if s:
            d = s.bit_count()
            check(2 * d * v * Q(1, 2*d) == v)
    # The mass/degree polynomials of the unnormalized heat law at rational r.
    for r in [Q(1,4), Q(1,2), Q(3,4), Q(1)]:
        q = [v*r**s.bit_count() for s,v in enumerate(p)]
        check(sum(q) <= 1)
        check(sum(q) >= p[0])
        check(sum(s.bit_count()*v for s,v in enumerate(q)) <= influence)
    return p, influence

functions = 0
for n in range(4):
    size = 1 << n
    for mask in range(1 << size):
        audit([1 if mask >> x & 1 else -1 for x in range(size)], n)
        functions += 1

rows = []
for n in range(2,9):
    size = 1 << n
    values = [1]*size
    values[0] = -1
    p, influence = audit(values, n)
    check(p[0] == Q(size-2,size)**2)
    check(all(v == Q(4,size*size) for v in p[1:]))
    check(influence == Q(2*n,size))
    for r in [Q(1,4), Q(1,2), Q(3,4), Q(1)]:
        weighted = sum(s.bit_count()*v*r**s.bit_count() for s,v in enumerate(p))
        closed = Q(4,size*size)*n*r*(1+r)**(n-1)
        check(weighted == closed)
        check(weighted/influence == r*((1+r)/2)**(n-1))
    # Formal coefficient multiplying ln(2) in integral J / I.
    nonempty_mass = sum(p[1:])
    area = Q(2*n-2,2) * nonempty_mass/influence
    closed_area = 2*(1-Q(1,n))*(1-Q(1,size))
    check(area == closed_area)
    check(area <= 2)
    rows.append({"n":n,"influence":str(influence),"area_over_I_coefficient_of_ln2":str(area)})

# A separate O(n) binomial formula reconstruction, not using Walsh transforms.
for n in range(2,9):
    check(sum(comb(n,d)*d for d in range(1,n+1)) == n*2**(n-1))

result = {"status":"PASS", "exhaustive_boolean_functions":functions,
          "point_defect_dimensions":[2,3,4,5,6,7,8], "assertions":assertions,
          "arithmetic":"integer and Fraction; logarithm atoms symbolic",
          "runtime_seconds":time.perf_counter()-start,
          "point_defect_rows":rows,
          "limits":"Does not certify the open universal integral bound; continuum obstruction is an analytic proof."}
out = Path(__file__).resolve().parents[1]/"out"
out.mkdir(exist_ok=True)
(out/"CHECK.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

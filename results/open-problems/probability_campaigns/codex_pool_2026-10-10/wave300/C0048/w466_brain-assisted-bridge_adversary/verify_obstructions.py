"""Bounded independent scalar checks; numerical results are not a lattice proof."""
from decimal import Decimal, localcontext
from pathlib import Path
import json
import math
import time
from fractions import Fraction
from itertools import product

root = Path(__file__).resolve().parent
gate = json.loads((root / 'compute_gate.json').read_text(encoding='utf-8'))
started = time.perf_counter()
with localcontext() as ctx:
    ctx.prec = 65
    ln2 = Decimal(2).ln()
    ln3 = Decimal(3).ln()
    gap = ln3 - Decimal(19) * ln2 / Decimal(12)
    allowance_lower = Decimal(4) * ln2 / Decimal(9)
    J = 4 * ln2
    def F(xs):
        return sum(x*x.ln() - J*x*x/2 for x in xs)
    u = [Decimal(1)/3]*3
    o = [Decimal(2)/3, Decimal(1)/6, Decimal(1)/6]
    s = [Decimal(1)/2, Decimal(1)/4, Decimal(1)/4]
    equality_residual = abs(F(u)-F(o))
    gap_residual = abs((F(s)-F(u))-gap)
    assert equality_residual < Decimal('1e-60')
    assert gap_residual < Decimal('1e-60')
    assert 3**12 > 2**19  # exact positive-gap witness
    assert gap > 0 and allowance_lower > gap
    assert 4-6*ln2 < 0
    quantitative = {'gap':str(gap),'allowance_lower':str(allowance_lower),
        'allowance_lower_over_gap':str(allowance_lower/gap),
        'ordered_disordered_residual':str(equality_residual),
        'gap_formula_residual':str(gap_residual),
        'exact_positive_gap_witness':{'3^12':3**12,'2^19':2**19}}

cases = 0
max_excess = 0.0
for eps in (1.0, 0.1, 0.01, 0.001):
    for x in (-1000.0, -10.0, -1.0, -0.01, 0.0, 0.01, 1.0, 10.0, 1000.0):
        # Stable expression for P_eps-P; avoids exponential overflow.
        error = eps*math.log1p(math.exp(-abs(x)/eps))
        max_excess = max(max_excess, error-eps*math.log(2))
        assert 0 <= error <= eps*math.log(2)+1e-15
        cases += 1
        assert cases <= gate['max_arithmetic_cases']
        assert time.perf_counter()-started < gate['arithmetic_deadline_seconds']

def component_count(N, bits, wired):
    parents = list(range(N+1))
    def find(a):
        while parents[a] != a:
            a = parents[a]
        return a
    def join(a,b):
        parents[find(a)] = find(b)
    if wired:
        join(0,N)
    for e, opened in enumerate(bits):
        if opened:
            join(e,e+1)
    return len({find(v) for v in range(N+1)})

exact_cycle_cases = 0
cycle_results = []
for p,q in ((Fraction(1,2),3),(Fraction(2,3),2),(Fraction(1,3),5)):
    a = p/(p+q*(1-p))
    for N in range(3,7):
        partition = [Fraction(0),Fraction(0)]
        open_mass = [Fraction(0),Fraction(0)]
        for bits in product((0,1), repeat=N):
            opened = sum(bits)
            weight0 = p**opened*(1-p)**(N-opened)
            for mode in (0,1):
                weight = weight0*q**component_count(N,bits,bool(mode))
                partition[mode] += weight
                if bits[N//2]:
                    open_mass[mode] += weight
            exact_cycle_cases += 1
            assert exact_cycle_cases+cases <= gate['max_arithmetic_cases']
            assert time.perf_counter()-started < gate['arithmetic_deadline_seconds']
        free = open_mass[0]/partition[0]
        wired = open_mass[1]/partition[1]
        expected = (q-1)*(1-a)*a**N/(1+(q-1)*a**N)
        assert free == a and wired-free == expected and expected > 0
        cycle_results.append({'p':str(p),'q':q,'N':N,'exact_gap':str(expected)})

result = {'gate_id':gate['gate_id'],'status':'PASS',
    'quantitative_obstruction':quantitative,'softplus_cases':cases,
    'softplus_max_excess_over_bound':max_excess,
    'exact_cycle_configurations':exact_cycle_cases,
    'exact_cycle_comparisons':cycle_results,
    'seconds':time.perf_counter()-started,
    'interpretation':'Scalar checks confirm the explicit obstruction formulas. They do not prove or disprove C0048, and are not an independent referee or formal proof.'}
(root/'measurement_arithmetic.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))

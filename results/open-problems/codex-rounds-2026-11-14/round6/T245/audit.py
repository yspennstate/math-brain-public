"""A manufactured audit of factorials, nontermination, and the Cauchy tail.

OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
The frozen coefficients are a test of the linear memory equation, not an
asserted endpoint trajectory of the training problem.
"""
import json
import math
import os
from pathlib import Path
import re
import resource
import sys
import time
from fractions import Fraction as F

sys.dont_write_bytecode = True
import verify as v


def main():
    start = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    final, degree = F(7, 10), 16
    rr, nn = v.coefficients(v.Z, (F(1), F(0)), (F(1), F(1)), F(1), degree)
    # Constant K=0, R(z)=z r1, N(z)=N0.
    # J_q=-tau^(q+1) L^q N0/(q+1)!, L(D)=r1^T D+D r1.
    jets, power = [], nn[0]
    for q in range(degree+1):
        jets.append(v.sc(power, -final**(q+1)/F(math.factorial(q+1))))
        assert jets[-1][0] == -final**(q+1)*(-2)**q/F(math.factorial(q+1))
        assert jets[-1][0] != 0
        power = v.add(v.mm(v.tr(rr[1]), power), v.mm(power, rr[1]))
    # Independently solve J_11_dot=-2z J_11-1 at fixed z.
    # General complex-disk bound for these frozen coefficients: K*=0,V=1,G=sqrt(2).
    rho = 2.
    r_bound = rho*math.sqrt(2.)
    n_bound = 4.
    m_bound = float(final)*n_bound*math.exp(2*float(final)*r_bound)
    rows = []
    for m in (0, 2, 4, 8, 12, 16):
        largest = 0.
        for j in range(257):
            z = j/256
            actual = -float(final) if z == 0 else math.expm1(-2*z*float(final))/(2*z)
            predicted = float(v.evaluate(jets[:m+1], F(j, 256))[0])
            largest = max(largest, abs(actual-predicted))
        bound = m_bound*rho**(-m)/(rho-1)
        assert largest <= bound+1e-15
        rows.append(dict(degree=m, scalar_field_error=largest, cauchy_bound=bound))
    # Recompute every reported ratio from the saved data, not from printed ratios.
    data = json.loads(Path('verification_data.json').read_text())
    ratios = []
    for case in data['discrete']:
        values = [row['full_state_error'] for row in case['rows']]
        recomputed = [a/b for a, b in zip(values, values[1:])]
        assert all(3.7 < ratio < 4.2 for ratio in recomputed)
        ratios.append(dict(t=case['t'], ratios=recomputed))
    coarse = Path('recheck_output.txt').read_text()
    refined = json.loads(Path('recheck_data.json').read_text())
    assert '1.8548329727002821e-07' in coarse
    sensitivity_ratio = 1.8548329727002821e-7/refined['maximum_sensitivity_error']
    assert 3.9 < sensitivity_ratio < 4.1
    for path in Path('.').glob('*.md'):
        content = path.read_text()
        assert content.count('\\[') == content.count('\\]'), path
        assert not any(ord(char) < 32 and char not in '\n\t\r' for char in content), path
    report = Path('REPORT.md').read_text()
    assert report.startswith('VERDICT: PARTIAL ')
    for target in re.findall(r'\]\(([^)]+)\)', report):
        if not target.startswith(('https://', 'http://')):
            assert Path(target).is_file(), target
    assert Path('verification_output.txt').read_text().rstrip().endswith('All checks passed.')
    assert Path('recheck_refined_output.txt').read_text().rstrip().endswith('Independent recheck passed.')
    result = dict(frozen_generator_rows=rows, all_coefficients_nonzero_through=degree,
                  manufactured_formula='j_q,11=-tau^(q+1)*(-2)^q/(q+1)!',
                  discrete_error_ratios_recomputed=ratios,
                  independent_recheck_refinement_ratio=sensitivity_ratio,
                  seconds=time.monotonic()-start,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  priority=os.getpriority(os.PRIO_PROCESS, 0))
    assert result['seconds'] < 1200 and result['peak_rss_bytes'] < 1_000_000_000
    Path('audit_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('Audit passed.')


if __name__ == '__main__':
    main()

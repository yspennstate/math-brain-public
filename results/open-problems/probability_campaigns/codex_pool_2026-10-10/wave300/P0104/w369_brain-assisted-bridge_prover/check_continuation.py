"""Bounded exact checks of L6--L7; these are not an independent proof audit."""
import itertools
import json
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = time.perf_counter()
gate = json.loads((ROOT / 'CONTINUATION_COMPUTE_GATE.json').read_text(encoding='utf-8'))


def expectation(leaves, values):
    return sum((leaf['p'] * value for leaf, value in zip(leaves, values)), F(0))


def check_tree(name, leaves):
    steps = len(leaves[0]['d'])
    assert steps <= gate['max_steps_per_case']
    assert len(leaves) <= gate['max_leaf_paths_per_case']
    checks = {}
    checks['probability_mass'] = sum((leaf['p'] for leaf in leaves), F(0)) == 1
    checks['positive_probabilities'] = all(leaf['p'] > 0 for leaf in leaves)
    checks['common_depth'] = all(len(leaf['d']) == steps == len(leaf['signals']) for leaf in leaves)
    variances = []
    adapted = True
    conditional_mean_zero = True
    for index in range(steps):
        groups = defaultdict(list)
        current_values = defaultdict(set)
        for number, leaf in enumerate(leaves):
            groups[tuple(leaf['signals'][:index])].append(number)
            current_values[tuple(leaf['signals'][:index+1])].add(leaf['d'][index])
        adapted = adapted and all(len(values) == 1 for values in current_values.values())
        variance_at_step = {}
        for prefix, numbers in groups.items():
            mass = sum((leaves[number]['p'] for number in numbers), F(0))
            mean_sum = sum((leaves[number]['p'] * leaves[number]['d'][index] for number in numbers), F(0))
            conditional_mean_zero = conditional_mean_zero and mean_sum == 0
            variance_at_step[prefix] = sum((leaves[number]['p'] * leaves[number]['d'][index] ** 2 for number in numbers), F(0)) / mass
        variances.append(variance_at_step)
    checks['adapted_differences'] = adapted
    checks['martingale_conditional_means'] = conditional_mean_zero

    terminal = []
    square_function = []
    predictable = []
    compensator_square = []
    predictable_increment_squares = []
    maximal_fourth = []
    cross_paths = []
    cubic_by_step = [[] for _ in range(steps)]
    fourth_paths = []
    for leaf in leaves:
        previous = F(0)
        maximum = F(0)
        cross = F(0)
        jump_fourth = F(0)
        q = F(0)
        v_total = F(0)
        v_squares = F(0)
        for index, difference in enumerate(leaf['d']):
            cross += previous ** 2 * difference ** 2
            cubic_by_step[index].append(previous * difference ** 3)
            jump_fourth += difference ** 4
            q += difference ** 2
            value = variances[index][tuple(leaf['signals'][:index])]
            v_total += value
            v_squares += value ** 2
            previous += difference
            maximum = max(maximum, abs(previous))
        terminal.append(previous)
        square_function.append(q)
        predictable.append(v_total)
        compensator_square.append((q-v_total) ** 2)
        predictable_increment_squares.append(v_squares)
        maximal_fourth.append(maximum ** 4)
        cross_paths.append(cross)
        fourth_paths.append(jump_fourth)

    mean = expectation(leaves, terminal)
    second = expectation(leaves, [value ** 2 for value in terminal])
    fourth = expectation(leaves, [value ** 4 for value in terminal])
    q_mean = expectation(leaves, square_function)
    q_second = expectation(leaves, [value ** 2 for value in square_function])
    v_mean = expectation(leaves, predictable)
    v_second = expectation(leaves, [value ** 2 for value in predictable])
    cross = expectation(leaves, cross_paths)
    cubic_terms = [expectation(leaves, values) for values in cubic_by_step]
    cubic = sum(cubic_terms, F(0))
    absolute_cubic = sum((abs(value) for value in cubic_terms), F(0))
    jump_fourth = expectation(leaves, fourth_paths)
    compensator_second = expectation(leaves, compensator_square)
    predictable_squares = expectation(leaves, predictable_increment_squares)
    checks.update({
        'terminal_mean_zero': mean == 0,
        'second_moment_identity': second == q_mean == v_mean,
        'fourth_moment_identity_with_cubic': fourth == 6*cross + 4*cubic + jump_fourth,
        'maximal_fourth_bound': expectation(leaves, maximal_fourth) <= F(4,3) ** 4 * fourth,
        'terminal_fourth_by_square_function': fourth <= 81*q_second,
        'square_function_by_terminal_fourth': q_second <= 81*fourth,
        'absolute_cross_bound': cross <= 16*q_second,
        'absolute_cubic_bound': absolute_cubic <= 4*q_second,
        'jump_fourth_bound': jump_fourth <= q_second,
        'exact_compensator_identity': compensator_second == jump_fourth-predictable_squares,
    })
    return {
        'case': name,
        'steps': steps,
        'leaf_paths': len(leaves),
        'checks': checks,
        'moments': {key: str(value) for key, value in {
            'variance': second,
            'terminal_fourth': fourth,
            'square_function_mean': q_mean,
            'square_function_second': q_second,
            'predictable_variation_second': v_second,
            'cross_sum': cross,
            'cubic_sum': cubic,
            'absolute_cubic_sum': absolute_cubic,
            'jump_fourth_sum': jump_fourth,
            'compensator_second': compensator_second,
        }.items()},
    }


cases = []
cases.append(check_tree('zero_martingale', [{'p': F(1,2), 'signals': [sign], 'd': [F(0)]} for sign in [-1,1]]))
walk = [{'p': F(1,16), 'signals': list(signs), 'd': [F(sign) for sign in signs]} for signs in itertools.product([-1,1], repeat=4)]
cases.append(check_tree('four_independent_sign_increments', walk))
for orientation in [1,-1]:
    skew = []
    for sign in [-1,1]:
        for branch, branch_probability in [(-1,F(2,3)), (2,F(1,3))]:
            skew.append({'p': F(1,2)*branch_probability, 'signals': [sign,branch], 'd': [F(sign),F(orientation*sign*branch)]})
    cases.append(check_tree('adapted_positive_cubic' if orientation == 1 else 'adapted_negative_cubic', skew))
for magnitude in [2,4,16,256]:
    p = F(1,magnitude ** 2)
    rare = []
    for indicator, mass in [(0,1-p),(1,p)]:
        for sign in [-1,1]:
            rare.append({'p': mass/2, 'signals': [indicator,sign], 'd': [F(0),F(indicator*sign*magnitude)]})
    cases.append(check_tree(f'revealed_rare_volatility_p_1_over_{magnitude ** 2}', rare))
assert len(cases) <= gate['max_cases']
rare_rows = cases[-4:]
obstruction_verified = all(row['moments']['variance'] == '1' and row['moments']['square_function_mean'] == '1' and row['moments']['square_function_second'] == str(magnitude ** 2) for row,magnitude in zip(rare_rows,[2,4,16,256]))
elapsed = time.perf_counter()-START
passed = sum(sum(row['checks'].values()) for row in cases) + int(obstruction_verified)
total = sum(len(row['checks']) for row in cases) + 1
result = {
    'command': 'python -X utf8 ~/brain_workers/w369/check_continuation.py',
    'gate': 'CONTINUATION_COMPUTE_GATE.json',
    'cases': len(cases),
    'checks_passed': passed,
    'checks_failed': total-passed,
    'rare_volatility_obstruction_verified': obstruction_verified,
    'elapsed_seconds': elapsed,
    'within_elapsed_gate': elapsed <= gate['max_elapsed_seconds'],
    'independent_mathematical_review': False,
    'formal_proof_receipt': None,
    'scope': 'Exact finite-support support for the hand proof; no estimate on lattice passage times',
    'rows': cases,
}
(ROOT / 'CONTINUATION_MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key: result[key] for key in ['cases','checks_passed','checks_failed','elapsed_seconds','within_elapsed_gate','rare_volatility_obstruction_verified']}))
assert passed == total and result['within_elapsed_gate']

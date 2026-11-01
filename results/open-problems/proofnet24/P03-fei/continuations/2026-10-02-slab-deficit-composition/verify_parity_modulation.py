"""Exact character-shift and influence-budget checks; no FEI constant fitted.

Enumerates every monotone Boolean truth table through five variables and
every output character. Integer Walsh numerators, direct physical flips,
and integer variance budgets establish the tested identities exactly.
Run: python verify_parity_modulation.py
"""
from pathlib import Path
import json
import numpy as np


def walsh_rows(rows):
    out = np.array(rows, dtype=np.int64, copy=True)
    width = out.shape[-1]
    half = 1
    while half < width:
        shaped = out.reshape(*out.shape[:-1], -1, 2 * half)
        left = shaped[..., :half].copy()
        right = shaped[..., half:].copy()
        shaped[..., :half] = left + right
        shaped[..., half:] = left - right
        half *= 2
    return out


monotone = [0, 1]
counts = []
function_count = modulation_count = 0
for n in range(1, 6):
    lower_width = 1 << (n - 1)
    monotone = [lo | (hi << lower_width)
                for lo in monotone for hi in monotone if lo & ~hi == 0]
    width = 1 << n
    indices = np.arange(width)
    characters = np.array([
        [1 if (s & x).bit_count() % 2 == 0 else -1 for x in range(width)]
        for s in range(width)], dtype=np.int64)
    permutations = np.array([indices ^ t for t in range(width)])
    for mask in monotone:
        truth = np.array([1 if mask & (1 << x) else -1
                          for x in range(width)], dtype=np.int64)
        coeff = walsh_rows(truth)
        changed = np.array([np.count_nonzero(truth != truth[indices ^ (1 << i)])
                            for i in range(n)], dtype=np.int64)
        assert np.count_nonzero(2 * changed > width) <= 1
        for i in range(n):
            for j in range(i):
                assert int(changed[i] + changed[j]) <= width
        mean_numerator = int(truth.sum())
        variance_numerator = width * width - mean_numerator * mean_numerator
        assert int(np.square(coeff[1:]).sum()) == variance_numerator
        budget_numerator = width * int(changed.sum()) - variance_numerator
        assert budget_numerator >= 0
        modulated = characters * truth[None, :]
        shifted = walsh_rows(modulated)
        # This permutation of all squared coefficients includes the empty atom.
        assert np.array_equal(np.square(shifted), np.square(coeff[permutations]))
        actual_changed = np.array([
            np.count_nonzero(modulated != modulated[:, indices ^ (1 << i)], axis=1)
            for i in range(n)], dtype=np.int64).T
        predicted = np.array([
            [width - int(changed[i]) if t & (1 << i) else int(changed[i])
             for i in range(n)] for t in range(width)], dtype=np.int64)
        assert np.array_equal(actual_changed, predicted)
        assert np.all(width * actual_changed.sum(axis=1) >= budget_numerator)
        function_count += 1
        modulation_count += width
    counts.append({'n': n, 'monotone_functions': len(monotone),
                   'characters_per_function': width})

# The scope counterexample: a two-bit parity modulated by itself is constant.
parity = np.array([1, -1, -1, 1], dtype=np.int64)
assert np.all(parity * parity == 1)
assert sum(np.count_nonzero(parity != parity[np.arange(4) ^ (1 << i)])
           for i in range(2)) == 8

result = {
    'status': 'PASS', 'arithmetic': 'exact int64 Walsh and physical flip counts',
    'monotone_functions': function_count, 'character_modulations': modulation_count,
    'counts': counts, 'includes_empty_spectral_atom': True,
    'scope_counterexample_checked': True,
    'limitations': 'Finite identities only; no universal FEI constant inferred.'}
Path(__file__).with_name('parity_modulation_checks.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))

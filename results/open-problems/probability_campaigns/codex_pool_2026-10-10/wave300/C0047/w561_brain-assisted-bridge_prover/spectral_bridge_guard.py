"""Read-only guard for the sufficient C0047 adjacency spectral criterion.

This checks an implication's prerequisites, not the parent conjecture. Numeric
inputs must be mathematically certified upper bounds; this module cannot certify
their provenance. It does not alter recall controls or any store.
"""
from fractions import Fraction


def assess(*, pc_upper=None, spectral_upper=None, degree=None,
           spectral_definition=None, hypotheses_confirmed=False):
    required = ('infinite countable vertex-transitive graph of bounded degree',
                'independent Bernoulli bond percolation',
                'certified critical-parameter and spectral upper bounds')
    if not hypotheses_confirmed:
        return {'status': 'MISSING_HYPOTHESES', 'required': required}
    if pc_upper is None or spectral_upper is None:
        return {'status': 'MISSING_BOUND', 'required': required}
    pc, spectral = Fraction(pc_upper), Fraction(spectral_upper)
    if not 0 <= pc <= 1 or spectral <= 0:
        raise ValueError('pc upper bound must be in [0,1], spectral upper bound positive')
    if spectral_definition == 'normalized_random_walk':
        if not isinstance(degree, int) or isinstance(degree, bool) or degree < 1:
            return {'status': 'MISSING_DEGREE', 'required': required}
        adjacency_upper = degree * spectral
    elif spectral_definition == 'adjacency_operator':
        adjacency_upper = spectral
    else:
        return {'status': 'MISSING_NORMALIZATION', 'required': required}
    product = pc * adjacency_upper
    return {
        'status': 'SUFFICIENT_CRITERION_MET' if product < 1 else 'NOT_CERTIFIED',
        'pc_times_adjacency_upper': str(product),
        'criterion': 'pc * ||A||_2->2 < 1',
        'required': required,
        'limitation': 'Failure of this sufficient criterion does not refute pc < pu.',
    }

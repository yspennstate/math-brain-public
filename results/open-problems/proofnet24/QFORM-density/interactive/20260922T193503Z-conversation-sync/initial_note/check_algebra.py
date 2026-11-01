"""Finite algebraic checks for PROOF_NOTE.md; not a proof of the general target."""
from pathlib import Path
import json
import sympy as s

def main() -> None:
    I = s.eye(3)
    U = I.col_join(I) / s.sqrt(2)
    lam = s.diag(2, 2, -2)
    D = s.eye(6) / 10
    A = D + U * lam * U.T
    assert s.simplify(U.T * U - I) == s.zeros(3)
    leverage = [s.simplify((U.row(i) * U.row(i).T)[0]) for i in range(6)]
    assert leverage == [s.Rational(1, 2)] * 6
    eigenvalues = A.eigenvals()
    expected = {s.Rational(21, 10): 2, s.Rational(-19, 10): 1, s.Rational(1, 10): 3}
    assert eigenvalues == expected
    B = s.prod((1-c) ** (-(1-c)/2) for c in leverage)
    Delta = abs(lam.det())
    bound = s.simplify(s.Rational(3) * B**s.Rational(2,3) * Delta**(-s.Rational(1,3)))
    assert bound == 3

    # Verify the explicit tail integral at finitely many integer ranks.
    t = s.symbols('t', positive=True)
    K = s.symbols('K', positive=True)
    for rank in range(3, 13):
        t0 = K ** s.Rational(2, rank)
        integral = 2 * (t0 + K * s.integrate(t**(-s.Rational(rank,2)), (t, t0, s.oo)))
        desired = 2*s.Rational(rank, rank-2)*K**s.Rational(2,rank)
        assert s.simplify(integral - desired) == 0

    c = s.symbols('c', positive=True)
    derivative = s.diff(c + (1-c)*s.log(1-c), c)
    assert s.simplify(derivative + s.log(1-c)) == 0
    # The sign -log(1-c)>=0 for 0<c<1 is used analytically in the note.
    eps, tt, ell = s.symbols('eps tt ell', real=True)
    real_inverse = s.simplify(s.re(1/(eps-s.I*tt*ell)))
    assert s.simplify(real_inverse - eps/(eps**2+tt**2*ell**2)) == 0

    result = {
        'status': 'PASS',
        'scope': 'Exact six-dimensional example, ranks 3 through 12 tail constants, two scalar identities only.',
        'universal_conjecture_verified': False,
        'analytic_theorem_requires_proof_review': True,
        'example_leverages': [str(c) for c in leverage],
        'example_eigenvalues_with_multiplicity': {str(k): int(v) for k,v in eigenvalues.items()},
        'example_density_bound': str(bound),
        'tail_integral_ranks_checked': list(range(3,13)),
    }
    text = json.dumps(result, indent=2)+'\n'
    Path(__file__).with_name('algebra_checks.json').write_text(text)
    print(text)

if __name__ == '__main__':
    main()

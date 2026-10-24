#!/usr/bin/env python3
import sympy as sp

a = sp.symbols('a', positive=True)
q = sp.Rational


def s0(x):
    return sp.factor(sp.cancel(sp.simplify(x)))


def check_curve(b, p, regime_name):
    c = s0((1-b)/2)
    d = s0(1-b)

    # Branch A: [0,c], [c,b], [d,b].
    # Branch B: [0,b], [c,d], [c,b].
    A = [(sp.Integer(0),c),(c,b),(d,b)]
    B = [(sp.Integer(0),b),(c,d),(c,b)]

    def width(I): return s0(I[1]-I[0])
    def center(I): return s0((I[0]+I[1])/2)

    Aw = [width(I) for I in A]
    Bw = [width(I) for I in B]
    Ac = [center(I) for I in A]
    Bc = [center(I) for I in B]

    # Exact one-uniform line identities. In A, [c,b] is the wide interval;
    # in B, [0,b] is the wide interval.
    assert s0(Aw[1] - Aw[0] - Aw[2]) == 0
    assert s0(Bw[0] - Bw[1] - Bw[2]) == 0
    assert s0(sum(Ac) - 1) == 0
    assert s0(sum(Bc) - 1) == 0

    # Exchangeabilized branch densities on the three consecutive cells
    # (0,c), (c,d), (d,b). Endpoints are null.
    densA = [
        1/(3*c),
        1/(3*(b-c)),
        (1/(b-c) + 1/(b-d))/3,
    ]
    densB = [
        1/(3*b),
        (1/b + 1/(d-c) + 1/(b-c))/3,
        (1/b + 1/(b-c))/3,
    ]
    mix = [s0(p*densA[i] + (1-p)*densB[i]) for i in range(3)]

    # Boundary fixed-mean layer extreme: layer mean 2/3, hence marginal mean 1/3.
    alpha = s0((b-q(2,3))/(b-a))
    beta  = s0((q(2,3)-a)/(b-a))
    target_low = s0(alpha/a + beta/b)
    target_high = s0(beta/b)

    if regime_name == 'C1':
        # c=a/2, d=a, so first two cells must equal target_low.
        assert s0(c-a/2) == 0
        assert s0(d-a) == 0
        assert s0(mix[0]-target_low) == 0
        assert s0(mix[1]-target_low) == 0
        assert s0(mix[2]-target_high) == 0
    elif regime_name == 'C2':
        # c=a, d=2a, so last two cells must equal target_high.
        assert s0(c-a) == 0
        assert s0(d-2*a) == 0
        assert s0(mix[0]-target_low) == 0
        assert s0(mix[1]-target_high) == 0
        assert s0(mix[2]-target_high) == 0
    else:
        raise ValueError(regime_name)

    # Normalization and mean follow from the target mixture, but verify algebraically.
    assert s0(alpha+beta-1) == 0
    assert s0(alpha*a/2 + beta*b/2 - q(1,3)) == 0

    return {
        'b': s0(b), 'c': s0(c), 'd': s0(d), 'p': s0(p),
        'alpha': s0(alpha), 'beta': s0(beta),
        'low': target_low, 'high': target_high,
        'mix': mix,
    }

# C1: b=1-a, 0<a<1/3. Then p=(1-a)/(2-3a) is strictly in (0,1).
C1 = check_curve(1-a, (1-a)/(2-3*a), 'C1')
# C2: b=1-2a, 0<a<1/6. Then p=(1-4a)/(1-3*a) is strictly in (0,1).
C2 = check_curve(1-2*a, (1-4*a)/(1-3*a), 'C2')

# Check the stated weight ranges by exact sign reductions on the declared domains.
# C1: p>0 and 1-p=(1-2a)/(2-3a)>0 for 0<a<1/3.
assert s0(1-C1['p'] - (1-2*a)/(2-3*a)) == 0
# C2: p>0 and 1-p=a/(1-3a)>0 for 0<a<1/6.
assert s0(1-C2['p'] - a/(1-3*a)) == 0

# Common b -> 2/3 boundary. C1 reaches it at a=1/3; C2 at a=1/6.
# Both target extremes degenerate to U[0,2/3], density 3/2.
assert s0(C1['high'].subs(a,q(1,3)) - q(3,2)) == 0
assert s0(C2['high'].subs(a,q(1,6)) - q(3,2)) == 0
assert s0(C1['low'].subs(a,q(1,3)) - q(3,2)) == 0
assert s0(C2['low'].subs(a,q(1,6)) - q(3,2)) == 0

print('C1', C1)
print('C2', C2)
print('C1_WEIGHT_COMPLEMENT', s0(1-C1['p']))
print('C2_WEIGHT_COMPLEMENT', s0(1-C2['p']))
print('COMMON_B23_TARGET_DENSITY', q(3,2))
print('ALL SYMBOLIC CHECKS PASSED')

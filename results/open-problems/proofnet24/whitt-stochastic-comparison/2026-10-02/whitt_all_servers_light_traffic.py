"""Exact checks of the all-server hyperexponential light-traffic formula.

Only Python's standard library is used. The finite capacity c+1 chain
supplies exact Taylor coefficients through order c+1; the accompanying
proof justifies matching those coefficients to the infinite queue.
"""
from fractions import Fraction as F
from math import factorial
import json


def compositions(total, k):
    if k == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, k - 1):
                yield (first,) + rest


def phase_taylor(c, probs, means):
    k = len(probs)
    states = [(n, counts) for n in range(c + 1)
              for counts in compositions(n, k)]
    states += [(c + 1, counts) for counts in compositions(c, k)]
    index = {state: j for j, state in enumerate(states)}
    size = len(states)
    Q0 = [[F(0) for _ in states] for _ in states]
    Q1 = [[F(0) for _ in states] for _ in states]

    def jump(Q, source, target, rate):
        Q[source][index[target]] += rate
        Q[source][source] -= rate

    for j, (n, counts) in enumerate(states):
        if n < c:
            for mark, p in enumerate(probs):
                dest = list(counts)
                dest[mark] += 1
                jump(Q1, j, (n + 1, tuple(dest)), p)
        elif n == c:
            jump(Q1, j, (c + 1, counts), F(1))
        for finished, count in enumerate(counts):
            if not count:
                continue
            after = list(counts)
            after[finished] -= 1
            rate = count / means[finished]
            if n <= c:
                jump(Q0, j, (n - 1, tuple(after)), rate)
            else:
                for replacement, p in enumerate(probs):
                    dest = after.copy()
                    dest[replacement] += 1
                    jump(Q0, j, (c, tuple(dest)), rate * p)
    assert all(sum(row, F(0)) == 0 for row in Q0 + Q1)
    current = [F(1)] + [F(0)] * (size - 1)
    coefficients = [F(0)]
    for degree in range(1, c + 2):
        rhs = [-sum((current[i] * Q1[i][j] for i in range(size)), F(0))
               for j in range(size)]
        following = [F(0)] * size
        for j in range(size - 1, 0, -1):
            following[j] = (rhs[j] - sum(
                (following[i] * Q0[i][j] for i in range(j + 1, size)), F(0)
            )) / Q0[j][j]
        following[0] = -sum(following[1:], F(0))
        assert all(sum((following[i] * Q0[i][j] for i in range(size)), F(0))
                   == rhs[j] for j in range(size))
        assert sum(following, F(0)) == 0
        coefficients.append(sum((following[j] for j, (n, _) in
                                 enumerate(states) if n >= c), F(0)))
        current = following
    return coefficients


def general_coefficient(c, probs, means):
    m = sum((p * a for p, a in zip(probs, means)), F(0))
    size_biased = [p * a / m for p, a in zip(probs, means)]
    n = c + 1
    expected_T = F(0)
    for counts in compositions(n, len(probs)):
        probability = F(factorial(n))
        for count, p in zip(counts, size_biased):
            probability *= p ** count / factorial(count)
        total_rate = sum((count / a for count, a in zip(counts, means)), F(0))
        odds = [(1 / a) / (total_rate - 1 / a) if count else F(0)
                for count, a in zip(counts, means)]
        sum_odds = sum((count * r for count, r in zip(counts, odds)), F(0))
        sum_squares = sum((count * r * r for count, r in zip(counts, odds)), F(0))
        T = (sum_odds * sum_odds - sum_squares) / n
        assert F(1, c) <= T <= F(2, c + 1)
        expected_T += probability * T
    K = m ** n * expected_T / factorial(c)
    next_coefficient = K - m ** n / factorial(c)
    excess_over_exponential = K - m ** n / (factorial(c) * c)
    return m, next_coefficient, excess_over_exponential


if __name__ == '__main__':
    cases = [([F(2, 3), F(1, 3)], [F(1, 2), F(2)]),
             ([F(3, 7), F(4, 7)], [F(1, 5), F(8, 5)]),
             ([F(1, 6), F(1, 3), F(1, 2)], [F(1, 4), F(1), F(3)]),
             ([F(1, 3), F(2, 3)], [F(7, 4), F(7, 4)])]
    output = []
    for case, (probs, means) in enumerate(cases):
        for c in range(2, 11 if len(probs) == 2 else 7):
            coeff = phase_taylor(c, probs, means)
            m, predicted, excess = general_coefficient(c, probs, means)
            assert all(x == 0 for x in coeff[:c])
            assert coeff[c] == m ** c / factorial(c)
            assert coeff[c + 1] == predicted
            assert (excess > 0) == (len(set(means)) > 1)
            output.append({'case': case, 'servers': c, 'next_coefficient': str(predicted),
                           'excess_over_exponential': str(excess)})
    print(json.dumps({'checks': 'all exact Fraction identities and inequalities passed',
                      'cases': output}, indent=2))

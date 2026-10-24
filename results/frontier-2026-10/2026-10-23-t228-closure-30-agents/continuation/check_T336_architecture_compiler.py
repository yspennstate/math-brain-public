#!/usr/bin/env python3
"""Exact rational wiring check for the stated scratch-token compiler.

This finite check supplements, and does not replace, the mathematical proof.
The full-width LN denominator is rational for the selected rank-one example.
Source-token selected LN differences are zero identically, without evaluating
their possibly irrational common denominator.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math

D, N, EPS = 72, 3, F(1, 18)
FEATURE, LABEL, POS0, POSQ, POSS, BALANCE = range(6)
XC, XQ, UPLUS, UMINUS, SPECIAL_PLUS, SPECIAL_MINUS, Z = range(6, 13)
GATES = list(range(13, 26))
MEAN = 26


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def linear(coefficients, row):
    return sum((F(value) * row[index] for index, value in coefficients.items()), F(0))


def attention(state, heads):
    output = [row[:] for row in state]
    for query, key, values in heads:
        for i in range(N):
            qi = [linear(form, state[i]) for form in query]
            for j in range(N):
                kj = [linear(form, state[j]) for form in key]
                score = max(F(0), sum((a * b for a, b in zip(qi, kj)), F(0)))
                for destination, value in values.items():
                    output[i][destination] += score * linear(value, state[j]) / N
    return output


def affine(state, destination, coefficients):
    return attention(state, [([{POSS: 1}], [{POSS: 1}],
                              {destination: {k: N * F(v) for k, v in coefficients.items()}})])


def multiply(state, destination, a, b):
    return attention(state, [([{a: 1}], [{b: 1}], {destination: {POSS: N}}),
                             ([{a: -1}], [{b: 1}], {destination: {POSS: -N}})])


def gather(state):
    return attention(state, [([{POSS: 1}], [{POS0: 1}], {XC: {FEATURE: N}}),
                             ([{POSS: 1}], [{POSQ: 1}], {XQ: {FEATURE: N}})])


def sqrt_exact(value):
    p, q = math.isqrt(value.numerator), math.isqrt(value.denominator)
    require(p * p == value.numerator and q * q == value.denominator,
            "Selected exact test has a non-rational denominator")
    return F(p, q)


def full_ln_difference_ffn(state):
    output = [row[:] for row in state]
    for i, row in enumerate(state):
        mean = sum(row, F(0)) / D
        variance = sum(((x - mean) ** 2 for x in row), F(0)) / D + EPS
        require(variance > 0, "Invalid normalization variance")
        difference = row[SPECIAL_PLUS] - row[SPECIAL_MINUS]
        # Exactly the two-ReLU FFN selecting LN_+ - LN_-.  When the
        # numerator is zero, both normalized coordinates are identical.
        selected = F(0) if difference == 0 else difference / sqrt_exact(variance)
        output[i][Z] += max(F(0), selected) - max(F(0), -selected)
    return output


def clip_scratch(state, coefficient, variance, A=F(3), V=F(5)):
    output = [row[:] for row in state]
    for old, row in zip(state, output):
        p, a, v = old[POSS], old[coefficient], old[variance]
        row[coefficient] += max(F(0), -A * p - a) - max(F(0), a - A * p)
        row[variance] += max(F(0), p - v) - max(F(0), v - V * p)
    return output


def run(label, coefficient_bias=F(0)):
    state = [[F(0) for _ in range(D)] for _ in range(N)]
    state[0][FEATURE], state[0][LABEL], state[0][POS0] = F(3, 4), F(label), F(1)
    state[1][FEATURE], state[1][POSQ] = F(-2), F(1)
    state[2][POSS], state[2][BALANCE] = F(1), F(-1)
    original_sources = [row[:] for row in state[:2]]
    state = gather(state)
    state = affine(state, GATES[0], {XC: 1})
    # D=72, eps=1/18, s=1 yield lambda^2=(4+D eps)/2=4.
    writes = {index: {index: -N} for index in [XC, XQ, *GATES]}
    writes.update({UPLUS: {GATES[0]: 2 * N}, UMINUS: {GATES[0]: -2 * N},
                   SPECIAL_PLUS: {POSS: N}, SPECIAL_MINUS: {POSS: -N}})
    state = attention(state, [([{POSS: 1}], [{POSS: 1}], writes)])
    nonzero = {index: value for index, value in enumerate(state[2]) if value}
    require(nonzero == {POSS: F(1), BALANCE: F(-1), UPLUS: F(3, 2),
                        UMINUS: F(-3, 2), SPECIAL_PLUS: F(1), SPECIAL_MINUS: F(-1)},
            "Scratch clearing inventory is wrong")
    state = full_ln_difference_ffn(state)
    require(state[:2] == original_sources, "LN residual changed a source token")
    require(state[2][Z] == F(24, 5), "Normalized scalar mismatch")
    state = gather(state)
    state = multiply(state, GATES[1], XC, XC)
    state = affine(state, GATES[2], {GATES[1]: 1, POSS: 1})
    state = affine(state, GATES[3], {POSS: 1})
    state = multiply(state, GATES[4], Z, Z)
    state = affine(state, GATES[5], {GATES[4]: F(1, 36)})
    state = multiply(state, GATES[6], GATES[3], XQ)
    state = affine(state, GATES[7], {GATES[6]: 1})
    state = multiply(state, GATES[8], GATES[5], GATES[7])
    state = multiply(state, GATES[9], XC, GATES[8])
    state = affine(state, GATES[10], {GATES[9]: 1, POSS: coefficient_bias})
    state = multiply(state, GATES[11], XQ, GATES[8])
    state = affine(state, GATES[12], {GATES[11]: 1, POSS: 1})
    coefficient, variance = GATES[10], GATES[12]
    require(state[2][GATES[5]] == F(16, 25), "Reciprocal mismatch")
    require(state[2][coefficient] == F(-24, 25) + coefficient_bias, "Coefficient mismatch")
    require(state[2][variance] == F(89, 25), "Variance mismatch")
    state = clip_scratch(state, coefficient, variance)
    state = attention(state, [([{coefficient: 1}], [{POS0: 1}], {MEAN: {LABEL: N}}),
                             ([{coefficient: -1}], [{POS0: 1}], {MEAN: {LABEL: -N}})])
    require(state[:2] == original_sources, "A source token was changed")
    require(state[2][MEAN] == (F(-24, 25) + coefficient_bias) * label,
            "Final exact label readout mismatch")
    return {"label": str(label), "bias": str(coefficient_bias),
            "mean": str(state[2][MEAN]), "variance": str(state[2][variance]),
            "source_tokens_exactly_unchanged": True}


def main():
    cases = [run(label, bias) for label in [F(0), F(-7, 3), F(10 ** 100), F(-(10 ** 100))]
             for bias in [F(0), F(1, 2), F(-1, 2)]]
    result = {"status": "PASS", "arithmetic": "Python Fraction; all comparisons exact",
              "scope": "Finite rank-one wiring check; not a replacement for the general proof",
              "width": D, "token_count": N, "epsilon": str(EPS),
              "cases": cases}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))
    print("Exact cases:", len(cases))


if __name__ == "__main__":
    main()

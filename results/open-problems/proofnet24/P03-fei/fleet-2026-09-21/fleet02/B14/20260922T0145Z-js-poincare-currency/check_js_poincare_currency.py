#!/usr/bin/env python3
"""Self-check for the sharp physical restriction JS/Poincare-currency bound.

For every nonconstant Boolean f through n<=4 and every coordinate i with Q_i>0,
compute the restriction Jensen-Shannon term JS_i and the exact Poincare currency
Q_i=(Inf_i-(q_1-q_0)^2)/4. Check JS_i <= 16 Q_i. This is only a regression
check; REPORT.md contains the all-dimensional analytic proof.
"""
import math


def fwht(a):
    a = [float(x) for x in a]
    h = 1
    n = len(a)
    while h < n:
        for j in range(0, n, 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def entropy(p):
    return -sum(x*math.log2(x) for x in p if x > 0.0)


def split(vals, n, i):
    m = 1 << (n-1)
    f0, f1 = [], []
    for y in range(m):
        lo = y & ((1 << i)-1)
        hi = y >> i
        z = lo | (hi << (i+1))
        f0.append(vals[z])
        f1.append(vals[z | (1 << i)])
    return f0, f1


cases = 0
positive = 0
max_ratio = -1.0
max_case = None
tol = 2e-12
for n in range(1, 5):
    N = 1 << n
    for tt in range(1, (1 << N)-1):
        vals = [1.0 if ((tt >> x) & 1) else -1.0 for x in range(N)]
        for i in range(n):
            f0, f1 = split(vals, n, i)
            h0, h1 = fwht(f0), fwht(f1)
            mu0 = [x*x for x in h0]
            mu1 = [x*x for x in h1]
            mix = [(x+y)/2 for x, y in zip(mu0, mu1)]
            js = entropy(mix) - 0.5*(entropy(mu0)+entropy(mu1))
            b = [(x-y)/2 for x, y in zip(h0, h1)]
            varb = sum(x*x for x in b[1:])
            Q = varb/4.0
            cases += 1
            if Q > 1e-15:
                positive += 1
                ratio = js/Q
                if ratio > max_ratio:
                    max_ratio = ratio
                    max_case = (n, tt, i, js, Q)
                assert js <= 16.0*Q + tol, (n, tt, i, js, Q, ratio)

# Two-input OR/AND geometry gives equality.
vals = [-1.0, 1.0, 1.0, 1.0]
f0, f1 = split(vals, 2, 0)
h0, h1 = fwht(f0), fwht(f1)
mu0 = [x*x for x in h0]
mu1 = [x*x for x in h1]
mix = [(x+y)/2 for x, y in zip(mu0, mu1)]
js = entropy(mix) - 0.5*(entropy(mu0)+entropy(mu1))
b = [(x-y)/2 for x, y in zip(h0, h1)]
Q = sum(x*x for x in b[1:])/4.0
assert abs(js-16*Q) < 1e-12

print("PASS")
print("coordinate_cases", cases)
print("positive_currency_cases", positive)
print("max_JS_over_Q", format(max_ratio, ".17g"))
print("max_case_n_tt_i_JS_Q", max_case)
print("AND2_JS", format(js, ".17g"))
print("AND2_Q", format(Q, ".17g"))
print("AND2_ratio", format(js/Q, ".17g"))

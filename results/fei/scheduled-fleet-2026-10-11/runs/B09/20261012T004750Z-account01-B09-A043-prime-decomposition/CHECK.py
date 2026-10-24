#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product

getcontext().prec = 90
LN2 = Decimal(2).ln()


def points(n):
    return list(product((0, 1), repeat=n))


def index(bits):
    return sum(b << i for i, b in enumerate(bits))


def table_from_code(n, code):
    return tuple(1 if (code >> j) & 1 else -1 for j in range(1 << n))


def essential(table, n):
    for i in range(n):
        found = False
        for x in points(n):
            y = list(x)
            y[i] ^= 1
            if table[index(x)] != table[index(tuple(y))]:
                found = True
                break
        if not found:
            return False
    return True


def canalizing(table, n):
    for i in range(n):
        for a in (0, 1):
            vals = {table[index(x)] for x in points(n) if x[i] == a}
            if len(vals) == 1:
                return True
    return False


def set_partitions(n):
    out = []

    def rec(i, blocks):
        if i == n:
            if 2 <= len(blocks) < n:
                out.append(tuple(tuple(b) for b in blocks))
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()

    rec(0, [])
    return out


ESSENTIAL_TABLES = {
    n: [table_from_code(n, c) for c in range(1 << (1 << n))
        if essential(table_from_code(n, c), n)]
    for n in range(1, 5)
}


def compose_table(n, blocks, children, outer):
    vals = [0] * (1 << n)
    for x in points(n):
        y = []
        for block, child in zip(blocks, children):
            local = tuple(x[j] for j in block)
            y.append(1 if child[index(local)] == 1 else 0)
        vals[index(x)] = outer[index(tuple(y))]
    return tuple(vals)


def decomposable_tables(n):
    result = set()
    witnesses = {}
    for blocks in set_partitions(n):
        k = len(blocks)
        child_lists = [ESSENTIAL_TABLES[len(b)] for b in blocks]
        for children in product(*child_lists):
            for outer in ESSENTIAL_TABLES[k]:
                f = compose_table(n, blocks, children, outer)
                result.add(f)
                witnesses.setdefault(f, blocks)
    return result, witnesses


def walsh_masses(table, n):
    den = 1 << n
    masses = []
    for mask in range(1 << n):
        total = 0
        for x in points(n):
            parity = sum(x[i] for i in range(n) if (mask >> i) & 1) & 1
            total += table[index(x)] * (-1 if parity else 1)
        masses.append(Fraction(total * total, den * den))
    return masses


def entropy(probs):
    ans = Decimal(0)
    for p in probs:
        if p:
            x = Decimal(p.numerator) / Decimal(p.denominator)
            ans -= x * x.ln() / LN2
    return ans


def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def outer_biased_masses(outer, ps):
    k = len(ps)
    masses = []
    for mask in range(1 << k):
        raw = Fraction(0)
        denom = Fraction(1)
        for y in points(k):
            prob = Fraction(1)
            centered = Fraction(1)
            for i, bit in enumerate(y):
                p = ps[i]
                prob *= p if bit else (1 - p)
                if (mask >> i) & 1:
                    centered *= Fraction(bit) - p
            raw += prob * outer[index(y)] * centered
        for i in range(k):
            if (mask >> i) & 1:
                denom *= ps[i] * (1 - ps[i])
        masses.append(raw * raw / denom)
    return masses


def popcount(x):
    return x.bit_count()


passed = 0


def check(cond):
    global passed
    assert cond
    passed += 1


# Exhaustive factorability and the prime/non-canalizing restriction.
prime_counts = {}
decomp_counts = {}
canalizing_prime_counts = {}
for n in (3, 4):
    decomposable, witnesses = decomposable_tables(n)
    essential_set = set(ESSENTIAL_TABLES[n])
    primes = essential_set - decomposable
    bad = [f for f in primes if canalizing(f, n)]
    prime_counts[n] = len(primes)
    decomp_counts[n] = len(essential_set & decomposable)
    canalizing_prime_counts[n] = len(bad)
    check(len(essential_set) == len(primes) + len(essential_set & decomposable))
    check(len(bad) == 0)
    for f in essential_set & decomposable:
        blocks = witnesses[f]
        check(2 <= len(blocks) < n)

# Exact composition spectrum for all two-input outer gates and all nonconstant
# two-bit children: 16*14*14 = 3136 genuine Boolean compositions.
all_outer = [table_from_code(2, c) for c in range(16)]
all_children = [table_from_code(2, c) for c in range(16)
                if len(set(table_from_code(2, c))) == 2]
composition_cases = 0
max_entropy_error = Decimal(0)

for outer in all_outer:
    for g1 in all_children:
        for g2 in all_children:
            composition_cases += 1
            p1 = Fraction(sum(1 for z in g1 if z == 1), 4)
            p2 = Fraction(sum(1 for z in g2 if z == 1), 4)
            v1 = 4 * p1 * (1 - p1)
            v2 = 4 * p2 * (1 - p2)
            m1 = walsh_masses(g1, 2)
            m2 = walsh_masses(g2, 2)
            q1 = [Fraction(0)] + [m1[s] / v1 for s in range(1, 4)]
            q2 = [Fraction(0)] + [m2[s] / v2 for s in range(1, 4)]
            om = outer_biased_masses(outer, (p1, p2))

            comp = compose_table(4, ((0, 1), (2, 3)), (g1, g2), outer)
            direct = walsh_masses(comp, 4)
            predicted = []
            for mask in range(16):
                s1 = mask & 3
                s2 = (mask >> 2) & 3
                t = (1 if s1 else 0) | (2 if s2 else 0)
                factor1 = q1[s1] if s1 else Fraction(1)
                factor2 = q2[s2] if s2 else Fraction(1)
                predicted.append(om[t] * factor1 * factor2)
            check(direct == predicted)
            check(sum(direct) == 1)

            alpha1 = om[1] + om[3]
            alpha2 = om[2] + om[3]
            I1 = sum(Fraction(popcount(s)) * m1[s] for s in range(4))
            I2 = sum(Fraction(popcount(s)) * m2[s] for s in range(4))
            Idirect = sum(Fraction(popcount(s)) * direct[s] for s in range(16))
            check(Idirect == alpha1 * I1 / v1 + alpha2 * I2 / v2)

            Hdirect = entropy(direct)
            Hformula = entropy(om) + dec(alpha1) * entropy(q1) + dec(alpha2) * entropy(q2)
            err = abs(Hdirect - Hformula)
            max_entropy_error = max(max_entropy_error, err)
            check(err < Decimal("1e-75"))

print("Arithmetic: fractions.Fraction plus Decimal(90) for logarithms")
print("Random seed: NONE")
print("Prime convention: essential gates, no factorization with 2<=k<n")
for n in (3, 4):
    print(f"n={n}: essential={len(ESSENTIAL_TABLES[n])}, decomposable={decomp_counts[n]}, prime={prime_counts[n]}, canalizing_primes={canalizing_prime_counts[n]}")
print(f"Composition cases checked: {composition_cases}")
print(f"Maximum entropy-chain error: {max_entropy_error}")
print(f"Assertions passed: {passed}")
print("Assertions failed: 0")

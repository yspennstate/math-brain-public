from itertools import permutations

P = list(permutations(range(4)))
IDX = {p: i for i, p in enumerate(P)}
ID = tuple(range(4))


def one_line(s):
    return tuple(int(ch) - 1 for ch in s)


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def inv(p):
    out = [0] * 4
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


# Drury's last displayed formula: 3u(f) is four positive evaluations minus one.
c = [0] * 24
for s in ("2134", "3214", "1432", "4321"):
    c[IDX[one_line(s)]] += 1
c[IDX[one_line("1234")]] -= 1
assert sum(c) == 3

orbit = {}
for r1 in P:
    for r2 in P:
        r2i = inv(r2)
        cp = [0] * 24
        for si, s in enumerate(P):
            if c[si]:
                t = compose(compose(r1, s), r2i)
                cp[IDX[t]] += c[si]
        orbit.setdefault(tuple(cp), 0)
        orbit[tuple(cp)] += 1

id_index = IDX[ID]
id_coeff_counts = {}
for key in orbit:
    id_coeff_counts[key[id_index]] = id_coeff_counts.get(key[id_index], 0) + 1

print("ordered_left_right_pairs", 24 * 24)
print("distinct_exceptional_functionals", len(orbit))
print("multiplicity_set", sorted(set(orbit.values())))
print("identity_coefficient_counts", dict(sorted(id_coeff_counts.items())))
print("u_of_constant_one", sum(c), "/ 3 = 1")
print("PASS")

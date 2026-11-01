from collections import Counter

# Three-edge graphic-matroid local types on distinguished edges e,f,g.
# Weights are nonnegative integer multiplicities of outside-forest states.
types = {
    "f_loop_eg_parallel": (2, ["", "e", "g"]),
    "e_loop_fg_parallel": (2, ["", "f", "g"]),
    "g_loop_ef_free": (3, ["", "e", "f", "ef"]),
    "triangle_U23": (1, ["", "e", "f", "g", "ef", "eg", "fg"]),
}

w = Counter()
for weight, independent_sets in types.values():
    for s in independent_sets:
        w["".join(sorted(s))] += weight

expected = {"": 8, "e": 6, "f": 6, "g": 5, "ef": 4, "eg": 1, "fg": 1, "efg": 0}
for key, value in expected.items():
    assert w[key] == value, (key, w[key], value)

Z = sum(w.values())
Ze = w["e"] + w["ef"] + w["eg"] + w["efg"]
Zf = w["f"] + w["ef"] + w["fg"] + w["efg"]
Zg = w["g"] + w["eg"] + w["fg"] + w["efg"]
Zef = w["ef"] + w["efg"]
Zeg = w["eg"] + w["efg"]
Zfg = w["fg"] + w["efg"]

def delta(a, b, ab):
    return a * b - Z * ab

Delta_ef = delta(Ze, Zf, Zef)
Delta_eg = delta(Ze, Zg, Zeg)
Delta_fg = delta(Zf, Zg, Zfg)
assert (Z, Ze, Zf, Zg, Zef, Zeg, Zfg) == (31, 11, 11, 7, 4, 1, 1)
assert (Delta_ef, Delta_eg, Delta_fg) == (-3, 46, 46)

# Deletion/contraction strata with respect to g.
A = w[""] + w["e"] + w["f"] + w["ef"]
Ae = w["e"] + w["ef"]
Af = w["f"] + w["ef"]
Aef = w["ef"]
D0 = Ae * Af - A * Aef

B = w["g"] + w["eg"] + w["fg"] + w["efg"]
Be = w["eg"] + w["efg"]
Bf = w["fg"] + w["efg"]
Bef = w["efg"]
D1 = Be * Bf - B * Bef
assert (A, Ae, Af, Aef, D0) == (24, 10, 10, 4, 4)
assert (B, Be, Bf, Bef, D1) == (7, 1, 1, 0, 1)

# Reconnection cells for the pair e,f after deleting e,f.
# The no-g states contribute n10=2,n01=2 and four safe n11 states.
# The g-present states contribute n00=4 and one overlap-Q state.
n00, n10, n01, n11, q = 4, 2, 2, 5, 1
N = n00 + n10 + n01 + n11
rayleigh_from_cells = n10 * n01 - n00 * n11 + N * q
assert (N, n00, n10, n01, n11, q) == (13, 4, 2, 2, 5, 1)
assert n11 - q == 4
assert rayleigh_from_cells == Delta_ef == -3

print("LOCAL_CONE_WITNESS_PASS")
print("selected_state_counts", dict(sorted(expected.items())))
print("Z,Ze,Zf,Zg,Zef,Zeg,Zfg", Z, Ze, Zf, Zg, Zef, Zeg, Zfg)
print("Delta_ef,Delta_eg,Delta_fg", Delta_ef, Delta_eg, Delta_fg)
print("g0_A,Ae,Af,Aef,D0", A, Ae, Af, Aef, D0)
print("g1_B,Be,Bf,Bef,D1", B, Be, Bf, Bef, D1)
print("R1_N,n00,n10,n01,n11,q,Delta", N, n00, n10, n01, n11, q, rayleigh_from_cells)

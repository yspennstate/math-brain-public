from tower_recompute import PM, T, dual, G, compose, LEAF
M, D = G(PM(3)), G(dual(PM(3)))
tops = {"T26": G(T(2, 6)), "T35": G(T(3, 5)), "dT25": G(dual(T(2, 5))), "dT43": G(dual(T(4, 3))), "Q2": G(dual(T(2, 2))),
        "T27": G(T(2, 7)), "T36": G(T(3, 6)), "T44": G(T(4, 4)), "T28": G(T(2, 8)), "none": None}
for base in ("D", "M"):
    st = LEAF
    st, _ = compose(st, *(D if base == "D" else M))
    best = None
    for k in range(1, 21):
        st, rM = compose(st, *(M if base == "D" else D))
        row = []
        for name, g in tops.items():
            r = rM if g is None else compose(st, *g)[1]
            row.append((r, name))
        r, name = max(row)
        if best is None or r > best[0]:
            best = (r, k, name)
        print(f"{base},{'M' if base=='D' else 'D'}^{k:<2d} best top {name:5s} {r:.13f}   plain {rM:.13f}", flush=True)
    print("BEST", best)

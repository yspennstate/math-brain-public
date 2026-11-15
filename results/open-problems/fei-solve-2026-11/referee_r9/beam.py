import json
from tower_recompute import PM, T, dual, G, compose, LEAF
gates = {"M": G(PM(3)), "D": G(dual(PM(3))), "P": G(PM(4)), "Pd": G(dual(PM(4))),
         "Q2": G(dual(T(2, 2))), "T26": G(T(2, 6)), "T35": G(T(3, 5)), "dT25": G(dual(T(2, 5))),
         "dT43": G(dual(T(4, 3)))}
beam = [((), LEAF, 0.0)]
best = (0.0, ())
WIDTH = 120
for depth in range(1, 17):
    cand = []
    for word, st, _ in beam:
        for name, (t, m) in gates.items():
            st2, r = compose(st, t, m)
            cand.append((word + (name,), st2, r))
            if r > best[0]:
                best = (r, word + (name,))
    cand.sort(key=lambda x: -x[2])
    beam, seen = [], set()
    for c in cand:  # keep diversity: dedupe on rounded state
        key = tuple(round(v, 9) for v in c[1])
        if key in seen:
            continue
        seen.add(key)
        beam.append(c)
        if len(beam) >= WIDTH:
            break
    print(f"depth {depth:2d} beam top {beam[0][2]:.14f} {','.join(beam[0][0])}  best so far {best[0]:.14f}", flush=True)
json.dump({"best": best[0], "word": list(best[1])}, open("beam_best.json", "w"))

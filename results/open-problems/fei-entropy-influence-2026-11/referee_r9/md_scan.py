import itertools
from tower_recompute import PM, dual, G, run
M, D = G(PM(3)), G(dual(PM(3)))
best = []
for h in range(1, 9):
    for w in itertools.product("MD", repeat=h):
        r, st = run([M if c == "M" else D for c in w])
        best.append((r, "".join(w)))
best.sort(reverse=True)
for r, w in best[:6]:
    print(f"{w:10s} {r:.15f}")
hit = [x for x in best if abs(x[0] - 4.505226154110238) < 1e-9]
print("match 4.505226154110238:", hit)

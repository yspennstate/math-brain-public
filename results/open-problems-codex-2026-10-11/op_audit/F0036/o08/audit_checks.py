import itertools, random, math, json
from pathlib import Path

root = Path(__file__).resolve().parent
scalar_checks = 0
for l, f, g, r in itertools.product(range(-4, 5), repeat=4):
    if l <= f < g <= r:
        assert l < r
        scalar_checks += 1

# Independent exhaustive path enumeration in random finite planar arrow graphs.
# Integer coordinates have parity equal to the layer index. No paths are killed.
rng = random.Random(8036)
cases = 200
contacts_total = 0
for case in range(cases):
    layers = [{-2, 0, 2}]
    arrows = {}
    for t in range(4):
        nxt = set()
        for x in sorted(layers[t]):
            choices = rng.choice([(-1,), (1,), (-1, 1)])
            arrows[t, x] = tuple(x + d for d in choices)
            nxt.update(arrows[t, x])
        layers.append(nxt)
    paths = [(x,) for x in sorted(layers[0])]
    for t in range(4):
        paths = [p + (y,) for p in paths for y in arrows[t, p[-1]]]
    contacts = set()
    for p, q in itertools.product(paths, repeat=2):
        for t in (2, 3):
            if p[t] == q[t] and all(p[v] < q[v] for v in range(1, t)):
                contacts.add((p[t], t))
    # Reverse occupied edges. All paths survive to layer 4, giving an incoming
    # reversed segment for each contact. Greedy outward predecessors bound all
    # reversed branches; separation until layer 1 is the tested relevance test.
    preds = {}
    for (t, x), ys in arrows.items():
        for y in ys:
            preds.setdefault((t + 1, y), []).append(x)
    forks = set()
    for t in (2, 3):
        for x in layers[t]:
            l = r = x
            separated = True
            for v in range(t, 1, -1):
                l = min(preds[v, l])
                r = max(preds[v, r])
                if l >= r:
                    separated = False
                    break
            if separated:
                forks.add((x, t))
    assert contacts == forks, (case, contacts, forks)
    contacts_total += len(contacts)

# Gaussian reflection/union estimate used in localization.
gaussian_checks = 0
for h in (0.01, 0.1, 1, 10, 100):
    for ratio in (0.001, 0.1, 0.5, 1, 2, 5, 10):
        d = ratio * math.sqrt(h)
        union_bound = 2 * math.erfc(d / math.sqrt(2*h))
        claimed = 4 * math.exp(-d*d/(2*h))
        assert union_bound <= claimed + 1e-15
        gaussian_checks += 1

def psi(v):
    return math.exp(-v)/math.sqrt(math.pi*v) + 1 + math.erf(math.sqrt(v))
psi_checks = 0
for v in (1e-8, 1e-5, 0.01, 0.1, 1, 10, 100):
    assert psi(v) <= 1/math.sqrt(math.pi*v) + 2
    psi_checks += 1
R, s, a, b, U = 2.0, 0.5, 1.0, 2.0, 3.0
n = 10000
integral = 4*R*(b-a)/n*sum(psi(U-(a+(j+0.5)*(b-a)/n))*psi(a+(j+0.5)*(b-a)/n-s) for j in range(n))
bound = 4*R*(b-a)*(1/math.sqrt(math.pi*(U-b))+2)*(1/math.sqrt(math.pi*(a-s))+2)
assert integral <= bound
result = {'scalar_order_checks': scalar_checks, 'finite_reversal_cases': cases,
          'finite_contacts': contacts_total, 'finite_reversal_mismatches': 0,
          'gaussian_bound_checks': gaussian_checks, 'psi_bound_checks': psi_checks,
          'sample_stationary_integral_midpoint': integral, 'sample_stationary_upper_bound': bound,
          'scope': 'Finite geometry and scalar computations only; not a stochastic Brownian-net proof.'}
(root/'audit_checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))

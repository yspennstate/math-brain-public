"""Exact Fraction checks of the half-turn form and minimized-variance identities."""
import json
import os
import signal
import time
from fractions import Fraction as F
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))


def timeout(signum, frame):
    raise TimeoutError("240-second computation limit")


signal.signal(signal.SIGALRM, timeout)
signal.alarm(240)
start = time.monotonic()
weights = list(map(F, ("0.01", "0.03", "0.1", "0.3", "1", "3", "10", "30", "100")))
count = 0
for n in (4, 6, 8, 10, 12, 20, 30):
    m = n//2
    for w in weights:
        edges = [(i, (i+1) % n, F(1)) for i in range(n)] + [(0, m, w)]
        degrees = [F(0)] * n
        for i, j, c in edges:
            degrees[i] += c
            degrees[j] += c

        def energy(u, v):
            return sum(c*(u[i]-u[j])*(v[i]-v[j]) for i, j, c in edges)

        def dot(u, v):
            return sum(degrees[i]*u[i]*v[i] for i in range(n))

        def variance(u):
            center = sum(degrees[i]*u[i] for i in range(n))/sum(degrees)
            return sum(degrees[i]*(u[i]-center)**2 for i in range(n))

        f = [F((7*i*i+3*i) % 19-9, i % 3+1) for i in range(n)]
        even = [(f[i]+f[(i+m) % n])/2 for i in range(n)]
        odd = [(f[i]-f[(i+m) % n])/2 for i in range(n)]
        one = [F(1)] * n
        assert energy(even, odd) == 0
        assert dot(even, odd) == 0
        assert sum(odd) == dot(one, odd) == 0
        assert energy(f, f) == energy(even, even)+energy(odd, odd)
        assert variance(f) == variance(even)+dot(odd, odd)
        g = [v-even[0] for v in even]
        assert g[0] == g[m] == 0
        assert variance(even) <= 2*sum(v*v for v in g)
        arcs = sum((g[(i+1) % n]-g[i])**2 for i in range(n))
        assert arcs == energy(even, even)
        s = odd[0]
        assert odd[m] == -s
        assert dot(odd, odd) == 2*sum(v*v for v in odd)+2*w*s*s
        cycle_energy = sum((odd[(i+1) % n]-odd[i])**2 for i in range(n))
        assert energy(odd, odd) == cycle_energy+4*w*s*s
        count += 1

result = dict(exact_fraction_form_cases=count, checks_per_case=11,
              seconds=round(time.monotonic()-start, 3), passed=True)
Path(__file__).with_name("referee_forms.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))

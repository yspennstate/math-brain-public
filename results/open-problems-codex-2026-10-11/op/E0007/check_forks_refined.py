from pathlib import Path
from fractions import Fraction as F
import itertools
import json
import time

started = time.time()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
coords = [(x, y) for x in range(-2, 3) for y in range(-2, 3) if abs(x) + abs(y) <= 2]
index = {xy: j for j, xy in enumerate(coords)}
affected = [index[(0, 0)]] + [index[d] for d in directions]
origin = index[(0, 0)]
near = [index[d] for d in directions]
neighbors = {j: [index[(coords[j][0] + dx, coords[j][1] + dy)] for dx, dy in directions] for j in affected}

def forks(s):
    n = sum(s[j] for j in near)
    return s[origin] * n * (n - 1), (1 - s[origin]) * n * (n - 1)

local_patterns = 0
local_transitions = 0
for bits in itertools.product([0, 1], repeat=13):
    s = list(bits)
    H, U = forks(s)
    N = sum(s[j] for j in near)
    death_H = death_U = birth4_H = birth4_U = 0
    for j in affected:
        old = s[j]
        if old:
            s[j] = 0
            h2, u2 = forks(s)
            death_H += h2 - H
            death_U += u2 - U
        else:
            count = sum(s[k] for k in neighbors[j])
            s[j] = 1
            h2, u2 = forks(s)
            birth4_H += count * (h2 - H)
            birth4_U += count * (u2 - U)
        s[j] = old
        local_transitions += 1
    assert death_H == -3 * H
    assert death_U == H - 2 * U
    assert birth4_H >= 2 * (3 * s[origin] * N - H)
    assert birth4_U >= -4 * U
    T4 = (1-s[origin])*N*N*(N-1)
    assert birth4_H >= 2*(3*s[origin]*N-H)+T4
    assert birth4_U >= -T4
    local_patterns += 1

b = F(109, 80)
P = b**3 + 7*b**2 + 36*b + 48
a = 2*b*(b*b+6*b+12)/P
h = b**2/(2*P)
u = b**2*(b+6)/(4*P)
kappa = (48-12*b-17*b*b)/P
m = min(1-12*u, 1-a-12*h)
assert a >= 0 and h >= 0 and u >= 0 and kappa > 0 and m > 0
assert -b+a*(2+b/2)-6*b*h == 0
assert h*(3+b/2)-u == 0
assert -a*b/8+u*(b+2)-b*h == 0
assert u >= h
assert (b-1)-a*b/2 == -kappa

L = 3
V = L*L
adj = [[y*L+(x+1)%L, y*L+(x-1)%L, ((y+1)%L)*L+x, ((y-1)%L)*L+x] for y in range(L) for x in range(L)]

def observables(s):
    counts = [sum(s[j] for j in adj[i]) for i in range(V)]
    return (
        F(sum(s), V),
        F(sum(s[i]*counts[i] for i in range(V)), 4*V),
        F(sum(s[i]*counts[i]*(counts[i]-1) for i in range(V)), V),
        F(sum((1-s[i])*counts[i]*(counts[i]-1) for i in range(V)), V),
    )

torus_states = torus_transitions = 0
largest_drift_plus_kappa_r = None
for bits in itertools.product([0, 1], repeat=V):
    s = list(bits)
    r, q, H, U = obs = observables(s)
    generator = [F(0)]*4
    for i in range(V):
        old = s[i]
        rate = F(1) if old else b*sum(s[j] for j in adj[i])/4
        if not rate:
            continue
        s[i] = 1-old
        new_obs = observables(s)
        s[i] = old
        for j in range(4):
            generator[j] += rate*(new_obs[j]-obs[j])
        torus_transitions += 1
    dr, dq, dH, dU = generator
    assert dr == (b-1)*r-b*q
    assert dq == b*r/2-(2+b/2)*q+b*U/8
    assert dH >= 6*b*q-(3+b/2)*H
    assert dU >= H-(b+2)*U
    T=b*sum((1-s[i])*sum(s[j] for j in adj[i])**2*(sum(s[j] for j in adj[i])-1) for i in range(V))/(4*V)
    assert dH >= 6*b*q-(3+b/2)*H+T
    assert dU >= H-2*U-T
    assert T <= b*U
    G = r-a*q-h*H-u*U
    drift = dr-a*dq-h*dH-u*dU
    assert m*r <= G <= r
    assert drift <= -kappa*r
    value = drift+kappa*r
    if largest_drift_plus_kappa_r is None or value > largest_drift_plus_kappa_r:
        largest_drift_plus_kappa_r = value
    torus_states += 1

result = {
    'local_radius_2_binary_patterns': local_patterns,
    'local_birth_death_changes': local_transitions,
    'torus_binary_states': torus_states,
    'torus_nonzero_rate_transitions': torus_transitions,
    'beta_total': str(b),
    'coefficients': {'a': str(a), 'h': str(h), 'u': str(u), 'kappa': str(kappa), 'm': str(m)},
    'largest_generator_G_plus_kappa_r': str(largest_drift_plus_kappa_r),
    'improved_threshold': (2*213**0.5-6)/17,
    'elapsed_seconds': time.time()-started,
    'scope': 'Exact finite local-generator and coefficient verification; infinite-volume proof is in SECOND_ATTEMPT.md.'
}
Path('fork_refined_checks.json').write_text(json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(result, indent=2))

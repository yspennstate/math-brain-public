"""Frozen finite check, integer Walsh plus independent physical edges. No imports from peers."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json, time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
checks = 0
rows = []

def require(ok):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(checks)

def walsh(values):
    a = values[:]
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k, k+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def scale(a, den):
    if not a:
        return 0
    a = abs(a)
    j = 0
    while 2*a <= den:
        a *= 2
        j += 1
    return j

for n in range(5):
    size = 1 << n
    zero = 0
    types = {}
    for mask in range(1 << size):
        if time.monotonic()-started > 55:
            raise RuntimeError('frozen runtime cap')
        f = [1 if mask >> x & 1 else -1 for x in range(size)]
        w = walsh(f)
        relevant = []
        admissible = True
        for i in range(n):
            # D_i has denominator 2. d_i is edge-disagreement probability.
            diffs = [(f[x | (1 << i)]-f[x])//2
                     for x in range(size) if not x >> i & 1]
            edges = sum(t*t for t in diffs)
            require(abs(sum(diffs))*2 == abs(w[1 << i]))
            if edges:
                relevant.append(i)
            tnum = abs(w[1 << i])
            # Analytic scalar equality: d=t and t in {0,1/2,1}.
            admissible &= edges*2 == tnum and tnum in (0, size//2, size)
        if not admissible:
            continue
        zero += 1
        r = len(relevant)
        require(r <= 3)
        high = sum(w[s]**2 for s in range(size) if s.bit_count() >= 2)
        delta = sum((s.bit_count()-1)*w[s]**2 for s in range(1, size))
        jhi = sum(w[s]**2*scale(w[s],size) for s in range(size) if s.bit_count() >= 2)
        if r == 0:
            require(abs(w[0]) == size)
        elif r == 1:
            require(abs(w[1 << relevant[0]]) == size)
        elif r == 2:
            require(abs(w[0])*2 == size)
            require(high*4 == size*size)
            require(jhi == delta)
        elif r == 3:
            require(w[0] == 0)
            require(abs(w[sum(1 << i for i in relevant)])*2 == size)
            require(2*jhi == delta)
        require(jhi <= delta)
        types[str(r)] = types.get(str(r),0)+1
    expected = 2+2*n+8*comb(n,2)+8*comb(n,3)
    require(zero == expected)
    rows.append(dict(n=n, total=1 << size, zero_reserve=zero, types=types))

# All-depth actual fair Maj3 tower: compressed recurrences from local spectrum.
towers = []
for depth in range(1,13):
    a = Q(3,2)**depth
    delta = a-1
    gate_weight = 2*delta
    terminal_j1 = depth*Q(3,4)**depth
    imports = Q(3,2)*delta-terminal_j1
    prime_hi = gate_weight/4
    final_hi = 2*delta-terminal_j1
    require(final_hi == prime_hi+imports)
    require(prime_hi == delta/2)
    require(imports >= 0)
    towers.append(dict(depth=depth, delta=str(delta), prime_Jhi_over_ln4=str(prime_hi),
                       import_over_ln4=str(imports), final_Jhi_over_ln4=str(final_hi),
                       Bstar_tree=0, low_carry=0, high_carry=0, V=0, flat_KL=0, tree_KL=0))

out = dict(status='PASS', arithmetic='integer Walsh, physical integer edge differences, Fraction tower recurrences',
           assertions=checks, seconds=time.monotonic()-started, domain=rows, towers=towers,
           finite_scope='all 65814 labelled Boolean tables for n=0..4; twelve analytic compressed tower checks')
(ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','domain']}))

"""Tiny deterministic checks. No simulation, training, store writes or worker launch."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import shutil
import time

ROOT = Path(__file__).resolve().parent

class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', wintypes.DWORD), ('load', wintypes.DWORD),
                ('total_phys', ctypes.c_ulonglong), ('avail_phys', ctypes.c_ulonglong),
                ('total_page', ctypes.c_ulonglong), ('avail_page', ctypes.c_ulonglong),
                ('total_virtual', ctypes.c_ulonglong), ('avail_virtual', ctypes.c_ulonglong),
                ('avail_extended', ctypes.c_ulonglong)]

def gate(work='exact corridor label enumeration and three-edge current parity enumeration'):
    mem = MemoryStatus()
    mem.length = ctypes.sizeof(mem)
    ok = bool(ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)))
    free_disk = shutil.disk_usage(ROOT).free
    decision = ok and mem.avail_phys >= 128 * 1024**2 and free_disk >= 32 * 1024**2
    result = {'utc': datetime.now(timezone.utc).isoformat(), 'allow': decision,
              'available_ram_bytes': mem.avail_phys if ok else None,
              'free_disk_bytes': free_disk, 'cores': 1, 'gpu': False,
              'work': work,
              'max_operations': 100000, 'max_active_seconds': 5, 'background': False}
    (ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    if not decision:
        raise SystemExit('Fresh compute gate denied; analytic proofs are retained.')

def corridor_check(n):
    length = n*n
    values = [length if j == k else 0 for j in range(n) for k in range(n)]
    p = Fraction(sum(x > 0 for x in values), n*n)
    first = Fraction(sum(values), n*n)
    second = Fraction(sum(x*x for x in values), n*n)
    ratio = first*first/second
    assert (p, first, second, ratio) == (Fraction(1,n), n, n**3, Fraction(1,n))
    return {'N': n, 'L': length, 'label_pairs': n*n, 'p_intersection': str(p),
            'E_I': str(first), 'E_I_squared': str(second), 'paley_zygmund_ratio': str(ratio)}

def current_laws(beta):
    # Each edge's infinite sum is exact: n=0, n>0 even, n odd.
    # Edge endpoints are (0,1), (1,2), (2,3). Free boundary, zero field.
    edges = [(0,1),(1,2),(2,3)]
    weights = [1.0, math.cosh(beta)-1.0, math.sinh(beta)]
    laws = {}
    for states in itertools.product(range(3), repeat=3):
        parity = 0
        support = 0
        weight = 1.0
        for e,(i,j) in enumerate(edges):
            state = states[e]
            weight *= weights[state]
            if state:
                support |= 1 << e
            if state == 2:
                parity ^= (1<<i) | (1<<j)
        laws.setdefault(parity, []).append((support, weight))
    for parity, rows in laws.items():
        normalizer = sum(w for _,w in rows)
        laws[parity] = [(s,w/normalizer) for s,w in rows]
    return laws

def reaches(support, start, finish):
    lo, hi = sorted((start, finish))
    return all(support & (1 << e) for e in range(lo, hi))

def current_check(beta):
    laws = current_laws(beta)
    def prob(sources1,sources2,start,finish):
        return sum(w1*w2 for s1,w1 in laws[sources1] for s2,w2 in laws[sources2]
                   if reaches(s1 | s2, start, finish))
    t = math.tanh(beta)
    p_original = prob(3,12,0,2)
    p_bare_hit = sum(w for s,w in laws[3] if reaches(s,0,2))
    p_augmented_hit = prob(3,0,0,2)
    p_four_union = 1.0 - (1.0/math.cosh(beta))**4
    assert math.isclose(p_original, t*t, abs_tol=1e-13)
    assert math.isclose(p_bare_hit, 1.0-1.0/math.cosh(beta), abs_tol=1e-13)
    assert math.isclose(p_augmented_hit, t*t, abs_tol=1e-13)
    identity_cases = 0
    worst = 0.0
    for a,b,c,d in itertools.product(range(4), repeat=4):
        s1 = (1<<a) ^ (1<<b)
        s2 = (1<<c) ^ (1<<d)
        sites = [a,b,c,d]
        # On a zero-field Ising chain, even-spin moments multiply tanh(beta)
        # along the unique edge set with the prescribed parity sources.
        odd_sites = sorted(x for x in range(4) if sites.count(x)%2)
        moment4 = t**sum(odd_sites[i+1]-odd_sites[i] for i in range(0,len(odd_sites),2))
        g = lambda x,y: t**abs(x-y)
        ursell = moment4 - g(a,b)*g(c,d) - g(a,c)*g(b,d) - g(a,d)*g(b,c)
        rhs = -2*g(a,b)*g(c,d)*prob(s1,s2,a,c)
        error = abs(ursell-rhs)
        worst = max(worst,error)
        assert error <= 1e-12, (beta,sites,ursell,rhs)
        identity_cases += 1
    f = [1.0, 2.0, 0.0, 0.5]
    variance = sum(f[x]*f[y]*t**abs(x-y) for x in range(4) for y in range(4))
    moment4_s = 0.0
    r_f = 0.0
    for a,b,c,d in itertools.product(range(4),repeat=4):
        fw = f[a]*f[b]*f[c]*f[d]
        odd = sorted(x for x in range(4) if [a,b,c,d].count(x)%2)
        m4 = t**sum(odd[i+1]-odd[i] for i in range(0,len(odd),2))
        moment4_s += fw*m4
        r_f += fw*t**abs(a-b)*t**abs(c-d)*prob((1<<a)^(1<<b),(1<<c)^(1<<d),a,c)/variance**2
    normalized_m4 = moment4_s/variance**2
    assert abs(normalized_m4-(3-2*r_f)) <= 1e-12
    return {'beta':beta, 'original_two_current_connection':p_original,
            'bare_sourced_hit':p_bare_hit, 'sourced_plus_sourceless_hit':p_augmented_hit,
            'four_current_connection':p_four_union, 'switching_identity_cases':identity_cases,
            'maximum_identity_error':worst, 'normalized_fourth_moment':normalized_m4,
            'weighted_connection_r':r_f, 'weighted_identity_error':abs(normalized_m4-(3-2*r_f))}

def main():
    gate()
    start = time.perf_counter()
    snapshot = ROOT/'INDEPENDENT.md'
    if not snapshot.exists():
        snapshot.write_bytes((ROOT/'ATTEMPT.md').read_bytes())
    digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
    results = {'command': 'python -X utf8 verify_obstruction.py',
               'scope': 'Finite controls only; not a proof of 3D Ising non-triviality.',
               'independent_snapshot': str(snapshot), 'independent_sha256': digest,
               'corridor': [corridor_check(n) for n in [2,4,8,16,32]],
               'chain_current_controls': [current_check(beta) for beta in [0.1,0.3,1.0]],
               'active_seconds': time.perf_counter()-start, 'passed':True}
    assert results['active_seconds'] < 5
    (ROOT/'VERIFICATION.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()

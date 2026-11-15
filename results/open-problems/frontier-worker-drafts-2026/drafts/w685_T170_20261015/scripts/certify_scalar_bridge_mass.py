"""Exact length-series certificate for irreducible positive height bridges."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import json, time, ctypes, hashlib

ROOT = Path(__file__).resolve().parents[1]

def walk_count(n, ell):
    if ell == 1:
        return int(n == 1)
    if n < ell or (n - ell) % 2:
        return 0
    m = n - 2
    total = 0
    for k in range(-n // ell - 2, n // ell + 3):
        u = (n + ell - 4) // 2 + k * ell
        v = u + 1
        total += (comb(m, u) if 0 <= u <= m else 0)
        total -= (comb(m, v) if 0 <= v <= m else 0)
    assert total >= 0
    return total

def direct_counts(n, ell):
    if ell == 1:
        return int(n == 1)
    v = [0] * (ell + 1)
    v[1] = 1
    for _ in range(n - 2):
        w = [0] * (ell + 1)
        for i in range(1, ell):
            w[i] = v[i-1] + v[i+1]
        v = w
    return v[ell-1]

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
    start = time.monotonic()
    point_path = ROOT/'logs/height_bridge_tail_certificate.json'
    point = json.loads(point_path.read_text(encoding='utf-8'))
    get = lambda key: Q(int(point[key]['n']), int(point[key]['d']))
    a, z, d = get('s') + 1, get('z'), 21
    t = Q(7, 5)
    r = d * (z + t**4/z) / (a*t)
    assert r < Q(9, 10)
    K, scale = 400, 10**40
    R = a.numerator * z.denominator
    bnum = d * a.denominator
    apow = [1] * (K+1)
    zpow = [1] * (K+1)
    qpow = [1] * (K+1)
    rpow = [1] * (K+1)
    for n in range(1, K+1):
        apow[n] = apow[n-1] * bnum
        zpow[n] = zpow[n-1] * z.numerator
        qpow[n] = qpow[n-1] * z.denominator
        rpow[n] = rpow[n-1] * R
    for n in range(2, 31):
        for ell in range(2, n+1):
            assert walk_count(n, ell) == direct_counts(n, ell)
    A, B = [0]*(K+1), [0]*(K+1)
    lo_units = 0
    short_units = {}
    for n in range(1, K+1):
        A[n] = apow[n] * sum(walk_count(n, ell) * zpow[ell] * qpow[n-ell]
                               for ell in range(1, n+1) if (n-ell)%2 == 0)
        B[n] = A[n] - sum(B[j]*A[n-j] for j in range(1, n))
        assert B[n] >= 0
        lo_units += B[n]*scale//rpow[n]
        if n in (9, 11, 13, 15, 17, 19, 21, 25, 31, 51, 101, 201, 400):
            short_units[str(n)] = str(lo_units)
    tail = t * Q(9,10)**(K+1) / Q(1,10)
    lower = Q(lo_units, scale)
    upper = lower + Q(K, scale) + tail
    # Independent finite profile enumeration checks the renewal coefficients.
    from height_profiles import profiles
    words = profiles(15)
    for n in range(1, 16):
        numerator = sum(apow[n]*zpow[h]*qpow[n-h] for word,h in words if len(word)==n)
        assert numerator == B[n]
    out = dict(at=datetime.now(timezone.utc).isoformat(), d=d, K=K,
               point_sha256=hashlib.sha256(point_path.read_bytes()).hexdigest(),
               a={'n':str(a.numerator),'d':str(a.denominator)},
               z={'n':str(z.numerator),'d':str(z.denominator)},
               method='integer reflection counts and A=B+BA coefficient recurrence; no floating operations',
               scale=str(scale), lower_units=str(lo_units),
               total_lower={'n':str(lower.numerator),'d':str(lower.denominator)},
               total_upper={'n':str(upper.numerator),'d':str(upper.denominator)},
               partial_lower_units=short_units, partial_rounding_upper_units=K,
               omitted_tail={'n':str(tail.numerator),'d':str(tail.denominator)},
               finite_checks='reflection versus direct killed walk n<=30; renewal versus exhaustive profiles n<=15',
               seconds=time.monotonic()-start,
               scope='scalar bridge mass only; mathematical renewal justification and FPP operator require separate review')
    (ROOT/'logs/scalar_bridge_mass_certificate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS exact scalar bridge mass',float(lower),float(upper),'K',K,'seconds',out['seconds'],flush=True)

if __name__ == '__main__':
    main()

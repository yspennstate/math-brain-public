"""Independent replay of T170-LEAD-ROLLING-D12-001 v1, written from the proof text (sections 1 and 3) only.
Reconstructs every h[a,b,c] (c >= 2) by the stated ceiling recursion, sweeping anti-diagonals b+c within each
a-slice, and checks every base-row inequality at c = 1 against A0. int64 is safe: |h| <= S is asserted per value,
rates <= R, so every numerator is below (1 + R + C) S < 2^56."""
import hashlib, json, sys, time
import numpy as np

try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

BASE = sys.argv[1]
raw = open(BASE, 'rb').read()
print('base sha256', hashlib.sha256(raw).hexdigest())
d = json.loads(raw.decode('utf-8'))
C, S, A0 = d['cap'], d['scale'], d['alpha0_units']
m = d['dimension'] - 1
assert (C, S, A0, m) == (512, 2**40, 109131241376, 11), (C, S, A0, m)
vals = d['base_bias']; assert len(vals) == C * C and all(isinstance(v, int) for v in vals)

# sigma(n) = 2m n - 2 f(n), f(n) = sum_{j<n} popcount(j)
f = [0] * (2 * C + 2)
for n in range(1, len(f)):
    f[n] = f[n - 1] + bin(n - 1).count('1')
sig = np.zeros(C + 2, dtype=np.int64)
for n in range(1, C + 1):
    sig[n] = 2 * m * n - 2 * f[n]
assert (sig[1:C + 1] > 0).all()
# all-split inequality behind the internal-edge bound, every split with a+b <= 2C
for a in range(1, 2 * C):
    for b in range(1, 2 * C + 1 - a):
        assert f[a] + f[b] + min(a, b) <= f[a + b], (a, b)
R = (6 * m + 3) * C
print('sigma(1), sigma(C):', int(sig[1]), int(sig[C]), ' R =', R)

H = np.zeros((C + 2, C + 2), dtype=np.int64)          # H[a,b], 1-indexed, zero padding
H[1:C + 1, 1:C + 1] = np.array(vals, dtype=np.int64).reshape(C, C)
assert np.abs(H).max() <= S

P = np.zeros((C + 2, C + 2), dtype=np.int64)          # h[a+1, b, c]
X = np.zeros((C + 2, C + 2), dtype=np.int64)          # h[a, b, c]
maxreq, argreq, minslack, maxden, maxabs, ninterior = None, None, None, 0, 0, 0
t0 = time.time()
for a in range(C, 0, -1):
    ra = int(sig[a]) if a < C else 0
    X[:] = 0
    X[1:C + 1, 1] = H[a, 1:C + 1]                      # h[a,b,1] = H[a,b]
    for k in range(2 * C, 2, -1):                      # anti-diagonal b + c = k, c >= 2
        lo, hi = max(1, k - C), min(C, k - 2)
        if lo > hi:
            continue
        bs = np.arange(lo, hi + 1, dtype=np.int64); cs = k - bs
        rb = np.where(bs < C, sig[bs] + np.maximum(a - bs, 0), 0)
        rc = np.where(cs < C, sig[cs] + np.maximum(bs - cs, 0), 0)
        num = S + ra * P[bs, cs] + rb * X[bs + 1, cs] + rc * X[bs, cs + 1] + cs * (H[bs, cs] - A0)
        den = ra + rb + rc + cs
        v = -((-num) // den)                           # ceiling, valid for negative numerators
        sl = v * den - num
        assert (sl >= 0).all() and (sl < den).all()
        X[bs, cs] = v
        ms = int(sl.min()); minslack = ms if minslack is None else min(minslack, ms)
        maxden = max(maxden, int(den.max())); maxabs = max(maxabs, int(np.abs(v).max()))
        ninterior += len(bs)
    # base rows (a, b, 1): S + L h <= A0 * 1, front child (b,1,1) = H[b,1]
    b = np.arange(1, C + 1, dtype=np.int64)
    rb1 = np.where(b < C, sig[b] + np.maximum(a - b, 0), 0)
    rc1 = int(sig[1]) + np.maximum(b - 1, 0)           # c = 1 < C
    h0 = H[a, b]
    req = (S + (ra * (H[a + 1, b] - h0) if a < C else 0) + rb1 * (H[a, b + 1] - h0)
           + rc1 * (X[b, 2] - h0) + (H[b, 1] - h0))
    i = int(np.argmax(req))
    if maxreq is None or int(req[i]) > maxreq:
        maxreq, argreq = int(req[i]), (a, i + 1, 1)
    maxden = max(maxden, int((ra + rb1 + rc1 + 1).max()))
    P, X = X, P
    if a % 64 == 0:
        print(f'  a={a} done, {time.time() - t0:.0f}s', flush=True)

assert maxabs <= S, maxabs
out = dict(interior=ninterior, expected_interior=C * C * (C - 1), min_interior_slack=minslack,
           max_base_requirement=maxreq, A0=A0, base_margin_units=A0 - maxreq, worst_base_row=argreq,
           max_total_rate=maxden, R=R, max_abs_h=maxabs, S=S, secs=round(time.time() - t0))
print(json.dumps(out))
assert ninterior == C * C * (C - 1) and maxreq <= A0 and maxden <= R
print('REPLAY PASS')

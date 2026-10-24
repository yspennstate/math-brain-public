import numpy as np
n = 4; N = 1 << n
def wht(t):
    a = np.array(t, float); h = 1
    while h < N:
        b = a.reshape(-1, 2*h); x = b[:, :h].copy(); y = b[:, h:].copy(); b[:, :h] = x+y; b[:, h:] = x-y; h *= 2
    return a/N
pc = [bin(s).count('1') for s in range(N)]
def HI(t):
    F = wht(t); P = F*F; nz = P > 1e-15
    return float(-(P[nz]*np.log2(P[nz])).sum()), float((P*np.array(pc)).sum())
def comp(t, i, up):
    t = list(t)
    for x in range(N):
        if (x >> i) & 1: continue
        a, b = t[x], t[x | (1 << i)]
        if (up and a == -1 and b == 1) or ((not up) and a == 1 and b == -1): t[x], t[x | (1 << i)] = b, a
    return t
found = 0
for code in range(1 << N):
    t = [1 - 2*((code >> x) & 1) for x in range(N)]
    H0, I0 = HI(t)
    for i in range(n):
        tu, td = comp(t, i, True), comp(t, i, False)
        (Hu, Iu), (Hd, Id) = HI(tu), HI(td)
        if min((H0-Hu) - 8*(I0-Iu), (H0-Hd) - 8*(I0-Id)) > 0.5:
            F = wht(t)
            print(f"f code {code}: TRUE set {[x for x in range(N) if t[x] == -1]}, coord {i}; H={H0:.3f} I={I0:.3f} -> up H={Hu:.3f} I={Iu:.3f}, down H={Hd:.3f} I={Id:.3f}")
            print("   nonzero coefficients:", {s: round(F[s], 4) for s in range(N) if abs(F[s]) > 1e-12})
            found += 1
            break
    if found >= 3: break

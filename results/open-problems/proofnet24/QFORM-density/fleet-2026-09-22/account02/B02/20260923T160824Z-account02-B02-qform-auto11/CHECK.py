import math
import numpy as np

rng = np.random.default_rng(160824)
min_ratio = 1.0
count = 0
for _ in range(5000):
    m, n = 5, 6
    u = rng.normal(size=m); u /= np.linalg.norm(u)
    v = rng.normal(size=n); v /= np.linalg.norm(v)
    E = rng.normal(size=(m, n))
    E = (np.eye(m) - np.outer(u, u)) @ E @ (np.eye(n) - np.outer(v, v))
    ef = np.linalg.norm(E)
    eps = float(rng.uniform(0.0, 1/8))
    if ef > 1e-12:
        E *= math.sqrt(eps) / ef
    S = math.sqrt(1-eps) * np.outer(u, v) + E
    T = float(np.sum(S*S))
    row = np.sum(S*S, axis=1)
    col = np.sum(S*S, axis=0)
    i, j = int(np.argmax(row)), int(np.argmax(col))
    if row[i] > T/2 and col[j] > T/2:
        count += 1
        min_ratio = min(min_ratio, float(S[i,j]**2/T))

print("C_DIFFUSE", 3*math.exp(1/3))
print("C_E2", 3*math.exp(1/3)*2**(1/6))
print("C_MINOR", 3*6**(1/3))
print("C_PARTNER_864", 3*6**(1/3)*864**(1/6))
print("C_SCALAR_DIFFUSE", 3*math.exp(2/3))
print("C_SCALAR_PARTNER_864", 3*math.exp(2/3)*864**(1/6))
print("C_D5_THRESHOLD", 5*math.sqrt(2)*math.e)
print("ENDPOINT_MARGIN", 5/24-math.sqrt(2)/7)
print("HEAVY_CASES", count)
print("MIN_SIJ2_OVER_T", min_ratio)
print("TARGET_1_OVER_36", 1/36)
print("STATUS", "PASS" if (5/24 > math.sqrt(2)/7 and min_ratio > 1/36) else "FAIL")

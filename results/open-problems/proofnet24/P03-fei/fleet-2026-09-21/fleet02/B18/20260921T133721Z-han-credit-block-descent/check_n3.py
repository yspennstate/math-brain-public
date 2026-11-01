from itertools import product
from math import comb, log, log2

def Hdist(xs):
    return -sum(x*log2(x) for x in xs if x > 0)

def walsh_data(values, n):
    pts = list(product([0,1], repeat=n))
    coeff = []
    for mask in range(1 << n):
        s = 0.0
        for x in pts:
            parity = sum(((mask >> i) & 1) * x[i] for i in range(n)) & 1
            s += values[x] * (-1 if parity else 1)
        coeff.append(s / (1 << n))
    p = [a*a for a in coeff]
    H = Hdist(p)
    I = sum(mask.bit_count() * p[mask] for mask in range(1 << n))
    return p, H, I

n = 3
pts = list(product([0,1], repeat=n))
f = {x: (-1 if x == (1,1,1) else 1) for x in pts}
p, H, I = walsh_data(f, n)
r = H / I

def marginal_entropy(coords):
    mass = {}
    for mask, z in enumerate(p):
        key = tuple((mask >> i) & 1 for i in coords)
        mass[key] = mass.get(key, 0.0) + z
    return Hdist(mass.values())

pairs = [(0,1), (0,2), (1,2)]
q = 2
h_q = sum(marginal_entropy(B) for B in pairs) / len(pairs)
A_q = h_q - (q/n) * H

eps = []
for B in pairs:
    i = ({0,1,2} - set(B)).pop()
    by_B = {}
    for mask, z in enumerate(p):
        key = tuple((mask >> j) & 1 for j in B)
        xi = (mask >> i) & 1
        by_B.setdefault(key, [0.0,0.0])[xi] += z
    eps.append(sum(min(row) for row in by_B.values()))
eps_q = sum(eps)/len(eps)

sum_R = 0.0
child_ratios = []
for i in range(n):
    H_children = []
    for val in [0,1]:
        rem = [j for j in range(n) if j != i]
        g = {}
        for y in product([0,1], repeat=n-1):
            x = [0]*n
            x[i] = val
            for j, coord in enumerate(rem):
                x[coord] = y[j]
            g[y] = f[tuple(x)]
        _, Hc, Ic = walsh_data(g, n-1)
        H_children.append(Hc)
        if Ic > 0:
            child_ratios.append(Hc/Ic)
    Delta = H - sum(H_children)/2
    B = H - marginal_entropy(tuple(j for j in range(n) if j != i))
    sum_R += Delta - B

cstar = 2/log(2)
k = n-q
N = comb(n,k)
v = comb(n-1,k)
Gamma_exact = (sum_R - N*A_q)/(v*I)
Gamma_upper = (n/(q*I))*(cstar*(n-q)*eps_q - A_q)
best_child_ratio = max(child_ratios)

print(f"H={H:.15f}")
print(f"I={I:.15f}")
print(f"r={r:.15f}")
print(f"h_q={h_q:.15f}")
print(f"eps_q={eps_q:.15f}")
print(f"A_q={A_q:.15f}")
print(f"sum_R={sum_R:.15f}")
print(f"Gamma_exact={Gamma_exact:.15f}")
print(f"Gamma_upper={Gamma_upper:.15f}")
print(f"best_child_ratio={best_child_ratio:.15f}")
print(f"r_minus_best_child={r-best_child_ratio:.15f}")

assert abs(Gamma_exact - (r-best_child_ratio)) < 1e-12
assert Gamma_exact <= Gamma_upper + 1e-12

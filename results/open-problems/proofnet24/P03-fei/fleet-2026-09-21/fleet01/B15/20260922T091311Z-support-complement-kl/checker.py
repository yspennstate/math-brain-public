from itertools import combinations
from math import log2, sqrt, prod

C_CENTER = 6.521851214


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x) - (1-x)*log2(1-x)


def fwht(vals):
    a = [int(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def essential(vals, n):
    N = 1 << n
    for i in range(n):
        if not any(vals[x] != vals[x ^ (1 << i)] for x in range(N)):
            return False
    return True


def decomposable(vals, n):
    coords = tuple(range(n))
    for size in range(2, n):
        for Atup in combinations(coords, size):
            A = tuple(Atup)
            Aset = set(A)
            B = tuple(i for i in coords if i not in Aset)
            rows = set()
            for aa in range(1 << len(A)):
                row = []
                for bb in range(1 << len(B)):
                    idx = 0
                    for j, i in enumerate(A):
                        idx |= ((aa >> j) & 1) << i
                    for j, i in enumerate(B):
                        idx |= ((bb >> j) & 1) << i
                    row.append(vals[idx])
                rows.add(tuple(row))
                if len(rows) > 2:
                    break
            if len(rows) <= 2:
                return True
    return False


def solve_c(r):
    mu = sum(r)
    if abs(mu - 1.0) < 1e-13:
        return None
    def g(c):
        z = 1.0
        for ri in r:
            z *= 1.0 - c*ri
        return 1.0 - z - c
    if abs(g(1.0)) < 1e-13:
        return 1.0
    lo, hi = 1e-15, 1.0
    for _ in range(180):
        mid = (lo + hi)/2.0
        if g(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2.0


def q_law(r, c):
    k = len(r)
    N = 1 << k
    q = [0.0]*N
    if c is None:
        for i, ri in enumerate(r):
            q[1 << i] = ri
        return q
    t = [c*ri for ri in r]
    for S in range(1, N):
        z = 1.0
        for i, ti in enumerate(t):
            z *= ti if ((S >> i) & 1) else (1.0-ti)
        q[S] = z/c
    return q


def parity_credit(r, c):
    active = [ri for ri in r if ri > 1e-14]
    if c is None or c >= 1.0 - 1e-13 or len(active) < 2:
        return 0.0
    t = [c*ri for ri in active]
    d2 = prod(x*(1.0-x) for x in t)/(c*c)
    qE = prod(t)/c
    s2 = 1.0-qE
    eta = (s2 - sqrt(max(0.0, s2*s2 - 4.0*d2)))/2.0
    return -2.0*log2(1.0-eta/2.0)


def one_function(vals, n):
    N = 1 << n
    W = fwht(vals)
    den = float(N*N)
    p = [(w*w)/den for w in W]
    r = [sum(p[S] for S in range(N) if (S >> i) & 1) for i in range(n)]
    I = sum(r)
    c = solve_c(r)
    q = q_law(r, c)
    Hmax = (sum(h2(c*ri) for ri in r)-h2(c))/c
    zeta = sum(q[S] for S in range(1, N) if p[S] == 0.0)
    support_credit = -log2(1.0-zeta) if zeta < 1.0 else float('inf')
    parity = parity_credit(r, c)
    credit = max(support_credit, parity)
    Binf = C_CENTER*(I-1.0)-Hmax
    return {
        'r': tuple(r), 'I': I, 'c': c, 'Hmax': Hmax,
        'zeta': zeta, 'support_credit': support_credit,
        'parity_credit': parity, 'lower_residual': Binf+credit,
    }


def enumerate_balanced(n):
    N = 1 << n
    prime = 0
    minrec = None
    for neg in combinations(range(N), N//2):
        vals = [1]*N
        for i in neg:
            vals[i] = -1
        if not essential(vals, n):
            continue
        if decomposable(vals, n):
            continue
        prime += 1
        rec = one_function(vals, n)
        if minrec is None or rec['lower_residual'] < minrec['lower_residual']:
            minrec = rec
    return prime, minrec

if __name__ == '__main__':
    print('C_CENTER', C_CENTER)
    W = [0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]
    p = [(w*w)/256.0 for w in W]
    r = [sum(p[S] for S in range(16) if (S >> i) & 1) for i in range(4)]
    c = solve_c(r)
    q = q_law(r,c)
    H = -sum(x*log2(x) for x in p if x > 0)
    Hmax = (sum(h2(c*ri) for ri in r)-h2(c))/c
    K = Hmax-H
    zeta = sum(q[S] for S in range(1,16) if p[S] == 0.0)
    print('named_witness_r', r)
    print('named_witness_c', format(c,'.15f'))
    print('named_witness_Kocc', format(K,'.15f'))
    print('named_witness_support_credit', format(-log2(1-zeta),'.15f'))
    print('named_witness_parity_credit', format(parity_credit(r,c),'.15f'))
    for n in (3,4):
        count, rec = enumerate_balanced(n)
        print('n', n, 'balanced_essential_prime_truth_tables', count)
        print('min_lower_residual', format(rec['lower_residual'],'.15f'))
        print('worst_r', rec['r'])
        print('worst_c', format(rec['c'],'.15f'))
        print('worst_Hmax', format(rec['Hmax'],'.15f'))
        print('worst_zeta', format(rec['zeta'],'.15f'))
        print('worst_support_credit', format(rec['support_credit'],'.15f'))
        print('worst_parity_credit', format(rec['parity_credit'],'.15f'))
    print('PASS diagnostic only; not an interval certificate')

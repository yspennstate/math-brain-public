from fractions import Fraction
from functools import lru_cache
from itertools import product

# Eight Boolean sign classes modulo global negation, represented with first coordinate +1.
SIGNS = [(1,) + x for x in product((-1, 1), repeat=3)]

# Positive rational coordinate weights lambda_j=a_j/16 with sum lambda_j=1.
WEIGHTS = []
for a in range(1, 14):
    for b in range(1, 15-a):
        for c in range(1, 16-a-b):
            d = 16-a-b-c
            if d >= 1:
                WEIGHTS.append((a,b,c,d))
assert len(WEIGHTS) == 455


def set_partitions(n):
    out = []
    blocks = []
    def rec(i):
        if i == n:
            out.append(tuple(tuple(b) for b in blocks))
            return
        for b in blocks:
            b.append(i)
            rec(i+1)
            b.pop()
        blocks.append([i])
        rec(i+1)
        blocks.pop()
    rec(0)
    return out


PARTITIONS = set_partitions(8)
assert len(PARTITIONS) == 4140


def orientation_options(block):
    # Global reversal inside one block is absorbed by r_B -> -r_B.
    k = len(block)
    for tail in product((-1,1), repeat=k-1):
        sig = (1,) + tail
        yield tuple(sig[j]*(block[j]+1) for j in range(k))


def oriented_vectors(key):
    out = []
    for z in key:
        sg = 1 if z > 0 else -1
        idx = abs(z)-1
        s = SIGNS[idx]
        out.append(tuple(sg*x for x in s))
    return out


@lru_cache(None)
def block_lb(key, a):
    """Exact lower bound on r^T Lambda r for one oriented witness block.

    Lambda=diag(a_j/16).  If <r,t_i> >= 1 for all i in the block, then for
    every nonempty U,
        <r, sum_{i in U} t_i> >= |U|.
    Weighted Cauchy gives
        r^T Lambda r >= |U|^2 / (v_U^T Lambda^{-1} v_U).
    The maximum over U is returned.  If some v_U=0, the block constraints are
    themselves infeasible, which certifies the full configuration.
    """
    vecs = oriented_vectors(key)
    k = len(vecs)
    P = a[0]*a[1]*a[2]*a[3]
    best_n, best_d = 0, 1
    for mask in range(1, 1 << k):
        q = mask.bit_count()
        v = [0,0,0,0]
        for i,t in enumerate(vecs):
            if (mask >> i) & 1:
                for j in range(4):
                    v[j] += t[j]
        if v == [0,0,0,0]:
            return None
        # v^T Lambda^{-1}v = 16 * sum_j v_j^2/a_j.
        den_num = 16 * sum(v[j]*v[j]*(P//a[j]) for j in range(4))
        n = q*q*P
        d = den_num
        if n*best_d > best_n*d:
            best_n, best_d = n, d
    return Fraction(best_n, best_d)


def config_cert(keys):
    # Every accepted certificate is exact rational arithmetic.
    for a in WEIGHTS:
        total = Fraction(0,1)
        infeasible = False
        for key in keys:
            lb = block_lb(key, a)
            if lb is None:
                infeasible = True
                break
            total += lb
            if total >= Fraction(1,3):
                return ('weight', a, total)
        if infeasible:
            return ('infeasible', a, None)
    return None


count = 0
infeasible_count = 0
exact_equal = 0
worst_cert = None
for part in PARTITIONS:
    opts = [tuple(orientation_options(block)) for block in part]
    for keys in product(*opts):
        count += 1
        cert = config_cert(keys)
        if cert is None:
            raise AssertionError(f'UNCERTIFIED configuration: {part} {keys}')
        if cert[0] == 'infeasible':
            infeasible_count += 1
        else:
            total = cert[2]
            if total == Fraction(1,3):
                exact_equal += 1
            if worst_cert is None or total < worst_cert:
                worst_cert = total

assert count == 75905

# Sharp lower-bound matrix A=Q/sqrt(3).  Each column has norm exactly one.
Q = [
    [0, 1,-1,-1],
    [1, 0,-1, 1],
    [1,-1, 0,-1],
    [1, 1, 1, 0],
]
for j in range(4):
    assert sum(Q[i][j]*Q[i][j] for i in range(4)) == 3
# For every Boolean signing eps, max_i |Q_i dot eps|=3, so disc(Q/sqrt(3))=sqrt(3).
for eps in product((-1,1), repeat=4):
    vals = [abs(sum(Q[i][j]*eps[j] for j in range(4))) for i in range(4)]
    assert max(vals) == 3, (eps, vals)

print('R13 n=4 exact cover checker')
print('set_partitions=', len(PARTITIONS))
print('weight_vectors=', len(WEIGHTS))
print('oriented_configurations=', count)
print('infeasible_by_zero_sum=', infeasible_count)
print('certificates_equal_1/3=', exact_equal)
print('smallest_selected_certificate=', worst_cert)
print('sharp_Q_column_square_sums=', [sum(Q[i][j]**2 for i in range(4)) for j in range(4)])
print('ALL_EXACT_CHECKS_PASS')

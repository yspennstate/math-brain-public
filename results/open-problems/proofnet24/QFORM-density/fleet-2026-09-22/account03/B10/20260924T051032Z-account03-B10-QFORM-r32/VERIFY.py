import math, random

SEED = 20260924051032
TARGET = 1000
MAX_ATTEMPTS = 300000


def rand_unit3(rng):
    v = [rng.gauss(0.0, 1.0) for _ in range(3)]
    n = math.sqrt(sum(x*x for x in v))
    return [x/n for x in v]


def orthogonal_columns(rng):
    q1 = rand_unit3(rng)
    while True:
        v = [rng.gauss(0.0, 1.0) for _ in range(3)]
        a = sum(v[i]*q1[i] for i in range(3))
        v = [v[i]-a*q1[i] for i in range(3)]
        n = math.sqrt(sum(x*x for x in v))
        if n > 1e-10:
            q2 = [x/n for x in v]
            break
    q3 = [
        q1[1]*q2[2]-q1[2]*q2[1],
        q1[2]*q2[0]-q1[0]*q2[2],
        q1[0]*q2[1]-q1[1]*q2[0],
    ]
    return [q1,q2,q3]


def spectral_matrix(Q, lam):
    return [[sum(Q[k][i]*lam[k]*Q[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


rng = random.Random(SEED)
accepted = 0
attempts = 0
min_abs_d = float("inf")
min_gap = float("inf")
min_delta = float("inf")
max_identity_error = 0.0

while accepted < TARGET and attempts < MAX_ATTEMPTS:
    attempts += 1
    signs = [1.0,1.0,-1.0] if rng.random() < 0.5 else [1.0,-1.0,-1.0]
    rng.shuffle(signs)
    lam = [signs[i]*(1.0+19.0*rng.random()) for i in range(3)]
    Q = orthogonal_columns(rng)
    M = spectral_matrix(Q, lam)
    alpha = M[0][0]
    if abs(alpha) >= 1.0/16.0:
        continue

    m1,m2 = M[1][0],M[2][0]
    s = math.hypot(m1,m2)
    if s < 1e-12:
        continue
    v = (m1/s,m2/s)
    q = (-v[1],v[0])
    N = ((M[1][1],M[1][2]),(M[2][1],M[2][2]))

    def bil(a,b):
        return (a[0]*(N[0][0]*b[0]+N[0][1]*b[1])
                + a[1]*(N[1][0]*b[0]+N[1][1]*b[1]))

    k = bil(v,q)
    d = bil(q,q)
    delta = alpha*alpha+s*s-1.0
    gap = delta*(d*d-1.0) - (1.0-alpha*alpha)*k*k

    q3 = (0.0,q[0],q[1])
    M2 = [[sum(M[i][j]*M[j][k0] for j in range(3))
           for k0 in range(3)] for i in range(3)]
    ee = M2[0][0]-1.0
    eq = sum((M2[0][j]-(1.0 if j == 0 else 0.0))*q3[j]
             for j in range(3))
    qq = sum(q3[i]*sum((M2[i][j]-(1.0 if i == j else 0.0))*q3[j]
                       for j in range(3)) for i in range(3))
    det_block = ee*qq-eq*eq
    max_identity_error = max(max_identity_error, abs(det_block-gap))

    if delta < -1e-8 or gap < -1e-7 or abs(d) < 1.0-1e-8:
        raise AssertionError((alpha,s,k,d,delta,gap,lam))

    accepted += 1
    min_abs_d = min(min_abs_d,abs(d))
    min_gap = min(min_gap,gap)
    min_delta = min(min_delta,delta)

print("seed", SEED)
print("accepted", accepted)
print("attempts", attempts)
print("min_abs_d", "%.15g" % min_abs_d)
print("min_delta", "%.15g" % min_delta)
print("min_psd_gap", "%.15g" % min_gap)
print("max_identity_error", "%.15g" % max_identity_error)
print("status PASS")

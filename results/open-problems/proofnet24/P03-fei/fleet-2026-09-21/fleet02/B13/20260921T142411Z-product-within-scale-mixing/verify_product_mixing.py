from __future__ import annotations
import collections
import json
import math

def masks(n):
    return range(1 << n)

def walsh_p(n, values):
    out = {}
    N = 1 << n
    for S in masks(n):
        c = 0.0
        for x, fx in enumerate(values):
            c += fx * (-1.0 if ((S & x).bit_count() & 1) else 1.0)
        c /= N
        if abs(c) > 1e-15:
            out[S] = c * c
    return out

def majority_values(n):
    vals = []
    for x in masks(n):
        total = sum(1 if ((x >> i) & 1) else -1 for i in range(n))
        vals.append(1 if total > 0 else -1)
    return vals

def one_point_values(n):
    # -1 only at x=0, +1 elsewhere.
    return [-1] + [1] * ((1 << n) - 1)

def product_p(p1, n1, p2, n2):
    return {a | (b << n1): pa * pb
            for a, pa in p1.items() for b, pb in p2.items()}

def fixed_packet(prefix, n, p, s):
    a = prefix.bit_count()
    E = 0.0
    R = 0.0
    raw = []
    for B, pb in p.items():
        if (B & prefix) != prefix:
            continue
        d = B.bit_count() - a
        E += pb * (s ** d)
        if d <= 0:
            continue
        base = pb * (s ** (d - 1))
        R += d * base
        if base == 0.0:
            continue
        rem = B & ~prefix
        for i in range(n):
            if (rem >> i) & 1:
                raw.append((i, B, base))
    if R == 0.0:
        return E, R, 0.0, []
    pi = collections.defaultdict(float)
    pB = collections.defaultdict(float)
    joint = []
    for i, B, w in raw:
        q = w / R
        joint.append((i, B, q))
        pi[i] += q
        pB[B] += q
    I = 0.0
    for i, B, q in joint:
        if q:
            I += q * math.log2(q / (pi[i] * pB[B]))
    return E, R, I, joint

def product_cross_mi(A1, n1, p1, A2, n2, p2, s):
    p = product_p(p1, n1, p2, n2)
    A = A1 | (A2 << n1)
    E, R, I, joint = fixed_packet(A, n1+n2, p, s)
    if R == 0.0:
        return E, R, I, 0.0, 0.0
    pL = collections.defaultdict(float)
    pT = collections.defaultdict(float)
    pK = collections.defaultdict(float)
    joint_LT = collections.defaultdict(float)
    joint_LK = collections.defaultdict(float)
    for i, B, q in joint:
        L = 0 if i < n1 else 1
        B1 = B & ((1 << n1)-1)
        B2 = B >> n1
        T = (B1, B2)
        K = (B1.bit_count(), B2.bit_count())
        pL[L] += q
        pT[T] += q
        pK[K] += q
        joint_LT[(L,T)] += q
        joint_LK[(L,K)] += q
    def mi(joint_map, pY):
        z = 0.0
        for (L,Y), q in joint_map.items():
            if q:
                z += q * math.log2(q / (pL[L] * pY[Y]))
        return z
    return E, R, I, mi(joint_LT, pT), mi(joint_LK, pK)

def partition_sum(n, p, s):
    total = 0.0
    for A in masks(n):
        E, _, _, _ = fixed_packet(A, n, p, s)
        total += ((1-s) ** A.bit_count()) * E
    return total

def simpson_cwithin(n, p, steps=1201):
    assert steps % 2 == 1
    vals = []
    for t in range(steps):
        s = t/(steps-1)
        cur = 0.0
        for A in masks(n):
            _, R, I, _ = fixed_packet(A, n, p, s)
            cur += ((1-s) ** A.bit_count()) * R * I
        vals.append(cur)
    h = 1.0/(steps-1)
    return (h/3.0) * (vals[0] + vals[-1]
                      + 4.0*sum(vals[1:-1:2])
                      + 2.0*sum(vals[2:-2:2]))

def influence(n,p):
    return sum(B.bit_count()*w for B,w in p.items())

def size_entropy(n,p):
    pk = collections.defaultdict(float)
    for B,w in p.items():
        pk[B.bit_count()] += w
    return -sum(w*math.log2(w) for w in pk.values() if w)

def main():
    maj3 = walsh_p(3, majority_values(3))
    defect3 = walsh_p(3, one_point_values(3))
    cases = [("maj3",3,maj3),("defect3",3,defect3)]
    max_factor_error = 0.0
    max_size_markov_error = 0.0
    max_partition_error = 0.0
    checks = 0

    # Pointwise fixed-scale decomposition for all prefix pairs on a 9-point scale grid.
    for name1,n1,p1 in cases:
        for name2,n2,p2 in cases:
            for q in range(9):
                s = q/8.0
                max_partition_error = max(max_partition_error,
                    abs(partition_sum(n1,p1,s)-1.0),
                    abs(partition_sum(n2,p2,s)-1.0))
                for A1 in masks(n1):
                    E1,R1,I1,_ = fixed_packet(A1,n1,p1,s)
                    for A2 in masks(n2):
                        E2,R2,I2,_ = fixed_packet(A2,n2,p2,s)
                        _,R,I,ILT,ILK = product_cross_mi(A1,n1,p1,A2,n2,p2,s)
                        lhs = R*I
                        rhs = R*ILT + R1*E2*I1 + E1*R2*I2
                        max_factor_error=max(max_factor_error,abs(lhs-rhs))
                        max_size_markov_error=max(max_size_markov_error,abs(ILT-ILK))
                        checks += 1

    # A strict nonadditivity witness: Maj_3 times Maj_3.
    maj6 = product_p(maj3,3,maj3,3)
    cw3 = simpson_cwithin(3,maj3)
    cw6 = simpson_cwithin(6,maj6)
    cross = cw6 - 2*cw3
    HKvec = 2*size_entropy(3,maj3)

    # A second stress case with a biased Boolean factor.
    def6 = product_p(defect3,3,defect3,3)
    cwd3 = simpson_cwithin(3,defect3)
    cwd6 = simpson_cwithin(6,def6)
    cross_def = cwd6 - 2*cwd3
    HKvec_def = 2*size_entropy(3,defect3)

    out = {
        "status":"PASS",
        "pointwise_prefix_pair_checks":checks,
        "max_fixed_scale_factorization_error":max_factor_error,
        "max_factor_label_size_markov_error":max_size_markov_error,
        "max_partition_of_unity_error":max_partition_error,
        "majority3": {
            "I": influence(3,maj3),
            "H_K": size_entropy(3,maj3),
            "C_within": cw3
        },
        "majority3_x_majority3": {
            "I": influence(6,maj6),
            "C_within": cw6,
            "C_mix_by_difference": cross,
            "H_K_vector": HKvec,
            "strict_nonadditivity": cross > 1e-6,
            "mix_le_size_entropy": cross <= HKvec + 2e-5
        },
        "defect3_x_defect3": {
            "I": influence(6,def6),
            "C_mix_by_difference": cross_def,
            "H_K_vector": HKvec_def,
            "mix_le_size_entropy": cross_def <= HKvec_def + 2e-5
        }
    }
    assert max_factor_error < 2e-12
    assert max_size_markov_error < 2e-12
    assert max_partition_error < 2e-12
    assert cross > 1e-6 and cross <= HKvec + 2e-5
    assert cross_def >= -2e-5 and cross_def <= HKvec_def + 2e-5
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()

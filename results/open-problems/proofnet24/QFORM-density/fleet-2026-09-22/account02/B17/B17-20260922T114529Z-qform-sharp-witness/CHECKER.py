import math

def sylvester(n):
    H = [[1]]
    while len(H) < n:
        H = [row + row for row in H] + [row + [-x for x in row] for row in H]
    return H

def transpose(A):
    return [list(c) for c in zip(*A)]

def matmul(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)]
            for row in A]

out = {"status": "PASS", "orders": {}, "constants": {}}
for n in (4, 8, 16, 32):
    H = sylvester(n)
    H3 = [[row[j] for j in range(3)] for row in H]
    G = matmul(transpose(H3), H3)
    assert G == [[n if i == j else 0 for j in range(3)] for i in range(3)]

    HD = [[row[0], row[1], -row[2]] for row in H3]
    M = matmul(HD, transpose(H3))
    M2 = matmul(M, M)
    M3 = matmul(M2, M)
    assert M3 == [[n*n*x for x in row] for row in M]

    dets = []
    for i in range(n):
        for j in range(i+1, n):
            dets.append(M[i][i]*M[j][j] - M[i][j]*M[j][i])
    assert max(dets) <= 0

    patterns = {}
    for row in H3:
        key = (row[1], row[2])
        patterns[key] = patterns.get(key, 0) + 1
    assert len(patterns) == 4 and set(patterns.values()) == {n//4}

    out["orders"][str(n)] = {
        "max_pair_det_numerator": max(dets),
        "min_pair_det_numerator": min(dets),
        "four_pattern_count_each": n//4
    }

vals = {
    "rot45_2_plus_ln2": 2 + math.log(2),
    "diagonal_pi": math.pi,
    "block_m2_2pi_minus_7over3": 2*math.pi - 7/3,
    "diffuse_limit_3sqrt2": 3*math.sqrt(2)
}
assert vals["diffuse_limit_3sqrt2"] > vals["block_m2_2pi_minus_7over3"]
assert vals["block_m2_2pi_minus_7over3"] > vals["diagonal_pi"]
assert vals["diagonal_pi"] > vals["rot45_2_plus_ln2"]
out["constants"] = vals

print(out)

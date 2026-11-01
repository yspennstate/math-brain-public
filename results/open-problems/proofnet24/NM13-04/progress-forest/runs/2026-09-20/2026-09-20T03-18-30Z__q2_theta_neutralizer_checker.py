#!/usr/bin/env python3
"""
Exact checker for NM13-04 / T07 split-5 Q2 transparent neutralizer.

Claims checked:
1. For Q2 = (K5 join independent-set-of-size 2) - 01, exact forest
   terminal counts are D_Q=6942, C_Q=13884, so terminal activity is 2.
2. For B_l = theta graph with r=3(2^l-1) internally-disjoint length-l
   paths in parallel, terminal activity is exactly 3.
3. The series composition A_l = Q2 o B_l is transparent:
   D_A = C_A = 41652*(2^l-1)^(3(2^l-1)).
4. For l=2, brute force on B_2 independently gives
   D=19683, C=59049 and hence D_A=C_A=819836316.

Only finite identities are checked here. PF-Rayleigh of Q2 is supplied by
the preceding split-5 port-field theorem; I-Rayleigh/PF of B_l is supplied
by the series-parallel theorem and PF series closure by NM13-08.
"""


def count_forest_terminal_states(nv, edges, s, t):
    m = len(edges)
    D = 0
    C = 0
    for mask in range(1 << m):
        parent = list(range(nv))
        rank = [0] * nv

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                if rank[ru] < rank[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                if rank[ru] == rank[rv]:
                    rank[ru] += 1

        if ok:
            if find(s) == find(t):
                C += 1
            else:
                D += 1
    return D, C


# Q2: clique terminals 0..4, independent vertices 5,6; port 01 deleted.
q2_edges = [
    (i, j)
    for i in range(5)
    for j in range(i + 1, 5)
    if (i, j) != (0, 1)
]
q2_edges += [(x, i) for x in (5, 6) for i in range(5)]
assert len(q2_edges) == 19

D_Q, C_Q = count_forest_terminal_states(7, q2_edges, 0, 1)
assert D_Q == 6942
assert C_Q == 13884
assert C_Q == 2 * D_Q

# Independent brute force for B_2: 9 length-2 paths in parallel.
b2_edges = [(0, 2 + j) for j in range(9)] + [(1, 2 + j) for j in range(9)]
D_B2, C_B2 = count_forest_terminal_states(11, b2_edges, 0, 1)
assert D_B2 == 3**9
assert C_B2 == 9 * 3**8
assert C_B2 == 3 * D_B2


def theta3_activity_counts(ell):
    q = 2**ell - 1
    r = 3 * q
    # One length-ell path: D=q, C=1. In parallel:
    # disconnected iff every branch disconnects.
    D = q**r
    # t_parallel = sum_i t_i = r/q = 3.
    C = 3 * D
    return q, r, D, C


def series_counts(D1, C1, D2, C2):
    # Outer terminals connect iff both pieces connect.
    C = C1 * C2
    # Otherwise at least one piece disconnects.
    D = D1 * D2 + D1 * C2 + C1 * D2
    return D, C


for ell in range(2, 9):
    q, r, D_B, C_B = theta3_activity_counts(ell)
    assert r == 3 * (2**ell - 1)
    assert C_B == 3 * D_B
    D_A, C_A = series_counts(D_Q, C_Q, D_B, C_B)
    closed = 41652 * q**r
    assert D_A == closed
    assert C_A == closed

D_A2, C_A2 = series_counts(D_Q, C_Q, D_B2, C_B2)
assert D_A2 == C_A2 == 819836316

print("Q2 edges =", len(q2_edges))
print("Q2 D,C =", D_Q, C_Q, "activity =", f"{C_Q}/{D_Q}=2")
print("B2 D,C =", D_B2, C_B2, "activity =", f"{C_B2}/{D_B2}=3")
print("A2 D,C =", D_A2, C_A2, "transparent =", D_A2 == C_A2)
for ell in range(2, 7):
    q, r, D_B, C_B = theta3_activity_counts(ell)
    D_A, C_A = series_counts(D_Q, C_Q, D_B, C_B)
    v_A = 8 + r * (ell - 1)
    e_A = 19 + r * ell
    print(
        f"ell={ell}: q={q}, r={r}, "
        f"|V(A_l)|={v_A}, |E(A_l)|={e_A}, "
        f"D_A=C_A={D_A}"
    )
print("ALL_EXACT_CHECKS_PASS")

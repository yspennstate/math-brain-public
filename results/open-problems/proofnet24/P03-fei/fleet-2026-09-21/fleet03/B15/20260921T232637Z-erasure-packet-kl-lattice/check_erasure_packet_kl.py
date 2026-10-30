#!/usr/bin/env python3
import json
import math


def walsh_int(vals):
    a = list(vals)
    n = len(a)
    h = 1
    while h < n:
        for base in range(0, n, 2*h):
            for j in range(base, base+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def coordinate_metrics(W, n, i):
    N = 1 << n
    NN = N*N
    bit = 1 << i
    A = sum(W[s]*W[s] for s in range(N) if s & bit)
    if not (0 < 2*A < NN):
        return None
    alpha = A / NN

    saturated = True
    L = 0.0
    D = 0.0
    packet = {}
    for t in range(N):
        if t & bit:
            continue
        u2 = W[t]*W[t]
        v2 = W[t | bit]*W[t | bit]
        m2 = u2 + v2
        if v2*NN != A*m2:
            saturated = False
        if v2:
            L += (v2/NN) * math.log2(m2/v2)
            P = v2/A
            M = m2/NN
            D += P * math.log2(P/M)
            key = abs(W[t | bit])
            packet.setdefault(key, []).append((u2, v2, m2))

    rhs = alpha * (math.log2(1/alpha) - D)

    packet_rhs = 0.0
    for key, rows in packet.items():
        beta_num = sum(v2 for _, v2, _ in rows)
        gamma_num = sum(m2 for _, _, m2 in rows)
        beta = beta_num/NN
        gamma = gamma_num/NN
        k = len(rows)
        # P(.|packet) is uniform because all |v| are equal.
        Din = 0.0
        for _, _, m2 in rows:
            U = 1.0/k
            Q = m2/gamma_num
            Din += U * math.log2(U/Q)
        packet_rhs += beta * (math.log2(gamma/beta) - Din)

    denom = alpha*math.log2(1/alpha)
    return {
        "alpha": alpha,
        "saturated": saturated,
        "D": D,
        "L": L,
        "credit_fraction": alpha*D/denom,
        "L_over_alpha": L/alpha,
        "identity_error": abs(L-rhs),
        "packet_error": abs(L-packet_rhs),
    }


def main():
    summary = []
    global_max_identity = 0.0
    global_max_packet = 0.0
    for n in range(1,5):
        N = 1 << n
        cases = 0
        saturations = 0
        min_credit = None
        min_credit_mask = None
        min_credit_coordinate = None
        min_credit_alpha = None
        max_Lalpha = None
        max_Lalpha_mask = None
        max_Lalpha_coordinate = None
        max_Lalpha_alpha = None
        for mask in range(1 << N):
            vals = [1 if ((mask >> x) & 1) else -1 for x in range(N)]
            W = walsh_int(vals)
            for i in range(n):
                row = coordinate_metrics(W, n, i)
                if row is None:
                    continue
                cases += 1
                saturations += int(row["saturated"])
                cf = row["credit_fraction"]
                if min_credit is None or cf < min_credit:
                    min_credit = cf
                    min_credit_mask = mask
                    min_credit_coordinate = i
                    min_credit_alpha = row["alpha"]
                la = row["L_over_alpha"]
                if max_Lalpha is None or la > max_Lalpha:
                    max_Lalpha = la
                    max_Lalpha_mask = mask
                    max_Lalpha_coordinate = i
                    max_Lalpha_alpha = row["alpha"]
                global_max_identity = max(global_max_identity, row["identity_error"])
                global_max_packet = max(global_max_packet, row["packet_error"])
        summary.append({
            "n": n,
            "active_coordinates_with_0_lt_alpha_lt_half": cases,
            "exact_P_equals_M_saturations": saturations,
            "min_credit_fraction": min_credit,
            "min_credit_witness_truth_mask": min_credit_mask,
            "min_credit_witness_coordinate": min_credit_coordinate,
            "min_credit_witness_alpha": min_credit_alpha,
            "max_L_over_alpha": max_Lalpha,
            "max_L_over_alpha_witness_truth_mask": max_Lalpha_mask,
            "max_L_over_alpha_witness_coordinate": max_Lalpha_coordinate,
            "max_L_over_alpha_witness_alpha": max_Lalpha_alpha,
        })
    print(json.dumps({
        "scope": "all Boolean truth tables through n=4; only coordinates with 0<Inf_i<1/2",
        "summaries": summary,
        "global_max_identity_error": global_max_identity,
        "global_max_source_magnitude_packet_error": global_max_packet,
        "interpretation": "finite falsification evidence only; exact non-saturation is proved algebraically in REPORT.md"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

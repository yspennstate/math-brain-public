#!/usr/bin/env python3
"""Exact verifier for the PROB10-02 k=10 equivariant lookahead certificate.

Floating relative-value iteration is used only to DISCOVER a policy/potential.
The final Bellman inequalities are checked after rounding by integer arithmetic.
The stochastic model always reveals actual iid source bits; it never replaces the
match array by independent Bernoulli entries.
"""

from collections import deque
import hashlib
import numpy as np

K = 10
RHO_NUM = 15_625_627
RHO_DEN = 20_000_000          # rho = 0.78128135
H_SCALE = 1_000_000_000
TOL = 2e-14
MAXIT = 260


def discover_and_verify():
    k = K
    p, q, Q = RHO_NUM, RHO_DEN, H_SCALE
    rho = p / q
    M = 1 << k
    arr = np.arange(M, dtype=np.int64)
    mask = M - 1
    sh0 = ((arr << 1) & mask).astype(np.int64)
    sh1 = (sh0 | 1).astype(np.int64)
    head = (arr >> (k - 1)) & 1
    eq = head[:, None] == head[None, :]

    # Discovery only: relative value iteration for reward - rho*(average consumption).
    h = np.zeros((M, M), dtype=np.float64)
    g = 0.0
    err = None
    for it in range(MAXIT):
        hx = 0.5 * (h[sh0, :] + h[sh1, :]) - rho / 2
        hy = 0.5 * (h[:, sh0] + h[:, sh1]) - rho / 2
        hm = (
            h[np.ix_(sh0, sh0)]
            + h[np.ix_(sh0, sh1)]
            + h[np.ix_(sh1, sh0)]
            + h[np.ix_(sh1, sh1)]
        ) / 4 + (1 - rho)
        nh = np.where(eq, hm, np.maximum(hx, hy))
        g = float(nh[0, 0])
        nh -= g
        err = float(np.max(np.abs(nh - h)))
        h = nh
        if err < TOL:
            break
    else:
        raise RuntimeError("relative value iteration did not converge")

    # Enforce exact swap symmetry before selecting actions.
    h = (h + h.T) / 2
    hx = 0.5 * (h[sh0, :] + h[sh1, :]) - rho / 2 - h
    hy = 0.5 * (h[:, sh0] + h[:, sh1]) - rho / 2 - h

    ii = np.arange(M)[:, None]
    jj = np.arange(M)[None, :]
    pref_x = np.zeros((M, M), dtype=bool)
    rep = (ii < jj) & (~eq)
    pref_x[rep] = hx[rep] >= hy[rep]
    rev = (ii > jj) & (~eq)
    pref_x[rev] = ~pref_x.T[rev]
    assert np.all(pref_x[~eq] == (~pref_x.T[~eq]))

    # The certificate begins here. hq is integer-valued and all residual checks
    # below are exact integer arithmetic.
    hq = np.rint(h * Q).astype(np.int64)

    sum4 = (
        hq[np.ix_(sh0, sh0)]
        + hq[np.ix_(sh0, sh1)]
        + hq[np.ix_(sh1, sh0)]
        + hq[np.ix_(sh1, sh1)]
    )
    # Equal-head action: reward=1, average consumption=1.
    # Residual denominator is 4*q*Q.
    num_eq = 4 * Q * (q - p) + q * (sum4 - 4 * hq)

    sx = hq[sh0, :] + hq[sh1, :]
    sy = hq[:, sh0] + hq[:, sh1]
    chosen_sum = np.where(pref_x, sx, sy)
    # Mismatch action: reward=0, average consumption=1/2.
    # Residual denominator is 2*q*Q.
    num_mis = -p * Q + q * (chosen_sum - 2 * hq)

    min_eq = int(num_eq[eq].min())
    min_mis = int(num_mis[~eq].min())
    assert min_eq > 0
    assert min_mis > 0

    eq_arg = int(np.argmin(np.where(eq, num_eq, np.iinfo(np.int64).max)))
    mis_arg = int(np.argmin(np.where(~eq, num_mis, np.iinfo(np.int64).max)))
    eq_state = (eq_arg // M, eq_arg % M)
    mis_state = (mis_arg // M, mis_arg % M)

    hmin = int(hq.min())
    hmax = int(hq.max())
    hosc = hmax - hmin
    h_hash = hashlib.sha256(hq.tobytes()).hexdigest()
    policy_hash = hashlib.sha256(pref_x.tobytes()).hexdigest()

    # Attack 3: unordered aligned-pair counts do NOT quotient this certificate.
    # Find two mismatch states with identical (head pair, n00,n01,n10,n11)
    # but opposite strict preferred actions.
    def bit_tuple(v):
        return tuple((v >> (k - 1 - i)) & 1 for i in range(k))

    seen = {}
    obstruction = None
    for x in range(M):
        bx = bit_tuple(x)
        for y in range(M):
            by = bit_tuple(y)
            if bx[0] == by[0]:
                continue
            counts = [0, 0, 0, 0]
            for a, b in zip(bx, by):
                counts[2 * a + b] += 1
            stat = (bx[0], by[0], *counts)
            action = "X" if pref_x[x, y] else "Y"
            old = seen.get(stat)
            if old is not None and old[2] != action:
                obstruction = (old, (x, y, action), stat)
                break
            seen[stat] = (x, y, action)
        if obstruction is not None:
            break
    assert obstruction is not None

    (x1, y1, a1), (x2, y2, a2), stat = obstruction
    nx1 = -p * Q + q * (int(sx[x1, y1]) - 2 * int(hq[x1, y1]))
    ny1 = -p * Q + q * (int(sy[x1, y1]) - 2 * int(hq[x1, y1]))
    nx2 = -p * Q + q * (int(sx[x2, y2]) - 2 * int(hq[x2, y2]))
    ny2 = -p * Q + q * (int(sy[x2, y2]) - 2 * int(hq[x2, y2]))
    assert (a1, a2) == ("X", "Y")
    assert nx1 > ny1 and ny2 > nx2

    return {
        "iterations": it + 1,
        "float_gain": g,
        "float_last_change": err,
        "min_eq_num": min_eq,
        "min_mis_num": min_mis,
        "eq_state": eq_state,
        "mis_state": mis_state,
        "hmin": hmin,
        "hmax": hmax,
        "hosc": hosc,
        "h_hash": h_hash,
        "policy_hash": policy_hash,
        "obstruction": obstruction,
        "obstruction_nums": (nx1, ny1, nx2, ny2),
    }


def successors(k, state, action):
    M = 1 << k
    mask = M - 1
    x, y = state
    shift = lambda v, b: ((v << 1) & mask) | b
    if action == "M":
        return [(shift(x, bx), shift(y, by)) for bx in (0, 1) for by in (0, 1)]
    if action == "X":
        return [(shift(x, b), y) for b in (0, 1)]
    return [(x, shift(y, b)) for b in (0, 1)]


def exhaustive_k2_atom_sanity():
    """Finite sanity check only; the report contains the all-k proof.

    Exhaust all 2^8 deterministic mismatch policies for k=2 and check that
    (00,00) is reachable from every state within 5k steps. This does not replace
    the analytic synchronizing-tail proof.
    """
    k = 2
    M = 1 << k
    states = [(x, y) for x in range(M) for y in range(M)]
    mismatch = [s for s in states if ((s[0] >> 1) & 1) != ((s[1] >> 1) & 1)]
    target = (0, 0)
    worst = 0
    worst_policy = None
    worst_state = None

    for mask in range(1 << len(mismatch)):
        index = {s: i for i, s in enumerate(mismatch)}
        policy = {}
        for s in states:
            if s in index:
                policy[s] = "X" if ((mask >> index[s]) & 1) else "Y"
            else:
                policy[s] = "M"

        rev = {s: [] for s in states}
        for s in states:
            for t in successors(k, s, policy[s]):
                rev[t].append(s)

        dist = {target: 0}
        q = deque([target])
        while q:
            t = q.popleft()
            for s in rev[t]:
                if s not in dist:
                    dist[s] = dist[t] + 1
                    q.append(s)
        assert len(dist) == len(states)
        md = max(dist.values())
        assert md <= 5 * k
        if md > worst:
            worst = md
            worst_policy = mask
            worst_state = max(dist, key=dist.get)

    return worst, worst_policy, worst_state


if __name__ == "__main__":
    out = discover_and_verify()
    worst, worst_policy, worst_state = exhaustive_k2_atom_sanity()

    print("PROB10-02 R17 equivariant lookahead exact checker")
    print(f"k={K}")
    print(f"rho={RHO_NUM}/{RHO_DEN}={RHO_NUM / RHO_DEN:.8f}")
    print(f"iterations={out['iterations']}")
    print(f"float_gain={out['float_gain']:.17g}")
    print(f"float_last_change={out['float_last_change']:.17g}")
    print(f"min_eq_numerator={out['min_eq_num']} denominator={4*RHO_DEN*H_SCALE}")
    print(f"min_mismatch_numerator={out['min_mis_num']} denominator={2*RHO_DEN*H_SCALE}")
    print(f"min_eq_state={out['eq_state']} min_mismatch_state={out['mis_state']}")
    print(f"potential_min={out['hmin']} potential_max={out['hmax']} scale={H_SCALE}")
    print(f"potential_oscillation={out['hosc']}/{H_SCALE}")
    print(f"potential_sha256={out['h_hash']}")
    print(f"policy_sha256={out['policy_hash']}")

    o1, o2, stat = out["obstruction"]
    nx1, ny1, nx2, ny2 = out["obstruction_nums"]
    print("pair_count_quotient_obstruction:")
    print(f"  statistic={stat}")
    print(f"  state1={o1} bits=({o1[0]:010b},{o1[1]:010b}) action_nums=(X:{nx1},Y:{ny1})")
    print(f"  state2={o2} bits=({o2[0]:010b},{o2[1]:010b}) action_nums=(X:{nx2},Y:{ny2})")
    print(f"k2_all_256_policies_atom_reachability_worst_distance={worst}")
    print(f"k2_worst_policy_mask={worst_policy} worst_state={worst_state}")
    print("ALL_EXACT_CHECKS_PASS")

from collections import deque
from fractions import Fraction
from itertools import product


def transition(state, w, u, v):
    """Exact correlated width-w strip transition from the P13/R17 carry recursion."""
    m = 2 * w
    x = state[:m]
    g = state[m:]
    d = [0] * (m + 1)
    for i in range(1, m + 1):
        d[i] = (1 - g[i - 1]) * int(bool(d[i - 1] or (x[i - 1] == v)))
    gp = [0] * m
    for i in range(m - 1):
        gp[i] = g[i + 1] + d[i + 2] - d[i + 1]
        assert gp[i] in (0, 1)
    gp[-1] = (1 - d[m]) * int(u == v)
    return tuple(x[1:] + (u,) + tuple(gp))


def reachable(w):
    m = 2 * w
    seeds = [tuple((a,) * m + (0,) * m) for a in (0, 1)]
    seen = set(seeds)
    q = deque(seeds)
    while q:
        s = q.popleft()
        for u, v in product((0, 1), repeat=2):
            t = transition(s, w, u, v)
            if t not in seen:
                seen.add(t)
                q.append(t)
    return seen


def apply_reset(state, w, a):
    m = 2 * w
    s = state
    for _ in range(m):
        s = transition(s, w, a, 1 - a)
    return s


def survival_prob(m, N):
    """Exact P(tau_m>N) for avoiding A^m and B^m in a 4-letter iid stream.

    A=(0,1), B=(1,0).  The other two source-pair letters are neutral.
    runs[r] aggregates the two signs A/B and current run length r.
    """
    neutral = Fraction(1, 1)
    runs = [Fraction(0, 1) for _ in range(m)]
    for _ in range(N):
        run_total = sum(runs[1:], Fraction(0, 1))
        total = neutral + run_total
        newneutral = total * Fraction(1, 2)
        newruns = [Fraction(0, 1) for _ in range(m)]
        newruns[1] = neutral * Fraction(1, 2) + run_total * Fraction(1, 4)
        for r in range(1, m - 1):
            newruns[r + 1] = runs[r] * Fraction(1, 4)
        neutral, runs = newneutral, newruns
    return neutral + sum(runs[1:], Fraction(0, 1))


def expected_wait_by_linear_recurrence(m):
    """Solve the exact run-length equations for E tau_m."""
    # E0=2+E1.  For 1<=r<m,
    # Er=1+E1/4+E0/2+E_{r+1}/4, with Em=0.
    # Hence E1=A*(2+3E1/4), A=sum_{j=0}^{m-2}4^{-j}.
    A = sum((Fraction(1, 4) ** j for j in range(m - 1)), Fraction(0, 1))
    E1 = (2 * A) / (1 - Fraction(3, 4) * A)
    E0 = 2 + E1
    return E0


print("P13 T02 overlapping-reset finite-to-infinite checker")

# Re-check the inherited 2w reachable-state reset on all reachable states for w<=4.
for w in range(1, 5):
    R = reachable(w)
    m = 2 * w
    for a in (0, 1):
        images = {apply_reset(s, w, a) for s in R}
        assert len(images) == 1
        target = next(iter(images))
        assert target == tuple((a,) * m + (0,) * m)
    print(f"reset_check w={w} m={m} reachable={len(R)} targets_unique=2 PASS")

# Verify the new overlapping-pattern waiting-time constant and strict gains.
for w in range(1, 6):
    m = 2 * w
    E = expected_wait_by_linear_recurrence(m)
    closed = Fraction(2 * (4 ** m - 1), 3)
    assert E == closed
    old = Fraction(w * 4 ** m, 1)
    assert closed < old

    N = 2 * m
    newtail = survival_prob(m, N)
    q = Fraction(2, 4 ** m)
    oldtail = (1 - q) ** 2
    assert newtail < oldtail

    print(
        f"w={w} m={m} E_tau={E} old_additive={old} "
        f"old/new={float(old/E):.12f} "
        f"tail_N={N}:{newtail} old_block_tail={oldtail} "
        f"strict_tail_gain={oldtail-newtail}"
    )

print("ALL_EXACT_CHECKS_PASS")

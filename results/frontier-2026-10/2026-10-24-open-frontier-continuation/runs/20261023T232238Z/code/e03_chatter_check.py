"""Exact rational checks for the frozen nonorthogonal Euler chatter example.

This is a deterministic endpoint calculation, not a finite-width simulation.
"""

from fractions import Fraction as Q


def fmt(x):
    return str(x)


def matvec(k, r):
    return (k[0][0] * r[0] + k[0][1] * r[1],
            k[1][0] * r[0] + k[1][1] * r[1])


def mean_matrix(mats):
    n = len(mats)
    return tuple(tuple(sum(k[i][j] for k in mats) / n for j in range(2))
                 for i in range(2))


def run(gamma, phase, nsteps=20):
    rho, z, r = Q(1, 2), Q(1), (Q(-1), Q(1))
    A, B = z * r[0], z * r[1]
    c, d = rho * B, -A - rho * B
    theta = c / (c + d)
    x, y, x0, y0 = phase, Q(10), phase, Q(10)
    active = []
    lam = []
    pre = []
    sec = []
    output_increment = (Q(0), Q(0))

    for n in range(nsteps):
        s = Q(int(x > 0))
        dx = gamma * (c + A * s)
        dy = gamma * (B + rho * A * s)
        x_next, y_next = x + dx, y + dy
        assert y > 0 and y_next > 0
        assert -gamma * d < x <= gamma * c
        assert -gamma * d < x_next <= gamma * c
        lamb = min(Q(1), x / (gamma * d)) if s else max(Q(0), x_next / (gamma * c))
        kpre = ((s, rho * s), (rho * s, Q(1)))
        ksec = ((s * lamb, rho * lamb), (rho * s, Q(1)))
        dp = (z * (max(x_next, Q(0)) - max(x, Q(0))), z * (y_next - y))
        assert dp == tuple(gamma * t for t in matvec(ksec, r))
        assert y_next - rho * x_next == y0 - rho * x0 + gamma * B * (1 - rho**2) * (n + 1)
        output_increment = tuple(output_increment[j] + dp[j] for j in range(2))
        active.append(s)
        lam.append(lamb)
        pre.append(kpre)
        sec.append(ksec)
        x, y = x_next, y_next

    assert abs(sum(active) - theta * nsteps) < 1
    assert sum(active) - theta * nsteps == -(x - x0) / (gamma * (c + d))
    kpre_avg, ksec_avg = mean_matrix(pre), mean_matrix(sec)
    mean_output_velocity = tuple(t / (nsteps * gamma) for t in output_increment)
    assert mean_output_velocity == matvec(ksec_avg, r)
    assert mean_output_velocity == (Q(0), Q(3, 4))
    print(f"gamma={fmt(gamma)} x0={fmt(x0)} n={nsteps}")
    print(f"  first four (active, secant fraction)={list(zip(active[:4], lam[:4]))}")
    print(f"  theta={fmt(theta)} phi={fmt(sum(lam) / nsteps)} occupation_error={fmt(sum(active)-theta*nsteps)}")
    print(f"  avg_pre={kpre_avg} avg_sec={ksec_avg}")
    print(f"  avg_pre*r={matvec(kpre_avg, r)} avg_sec*r={matvec(ksec_avg, r)}")
    print(f"  exact_mean_output_velocity={mean_output_velocity} final_x={fmt(x)}")


for gamma in (Q(1), Q(1, 10)):
    run(gamma, Q(0))
    run(gamma, gamma / 4)

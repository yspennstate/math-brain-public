from fractions import Fraction as F


rho = F(1, 2)
z = F(1)
r1, r2 = F(-1), F(1)
a, b = -z * r1, z * r2
c, d = rho * b, a - rho * b
kappa = (1 - rho * rho) * b
Cstar = Dstar = F(3, 4)


def ceil(q):
    return -((-q.numerator) // q.denominator)


def step(v, gamma):
    x, y = v
    rx = r1 if x > 0 else F(0)
    ry = r2 if y > 0 else F(0)
    return x + gamma * z * (rx + rho * ry), y + gamma * z * (rho * rx + ry)


def mixed_step(v, gamma, rr1, rr2):
    x, y = v
    rx = rr1 if x > 0 else F(0)
    ry = rr2 if y > 0 else F(0)
    return x + gamma * (rx + rho * ry), y + gamma * (rho * rx + ry)


dead = sliding = exact_axis = 0
for gamma in (F(1), F(1, 3)):
    for i in range(-20, 21):
        for j in range(-20, 21):
            v = (F(i, 4), F(j, 4))
            x0, y0 = v
            if x0 == 0 or y0 == 0:
                exact_axis += 1
            if y0 <= 0:
                n = 0 if x0 <= 0 else ceil(x0 / (gamma * a))
                for _ in range(n):
                    v = step(v, gamma)
                assert v[0] <= 0 and v[1] <= 0
                assert step(v, gamma) == v
                dead += 1
            else:
                if x0 > gamma * c:
                    e = ceil((x0 - gamma * c) / (gamma * d))
                elif x0 < -gamma * d:
                    e = ceil((-gamma * d - x0) / (gamma * c))
                else:
                    e = 0
                for _ in range(e):
                    assert v[1] > 0
                    assert not (-gamma * d <= v[0] <= gamma * c)
                    v = step(v, gamma)
                assert -gamma * d <= v[0] <= gamma * c
                eta = v[1] - rho * v[0]
                extra = max(0, (rho * gamma * Dstar - eta) // (gamma * kappa) + 1)
                for _ in range(extra):
                    assert v[1] > 0
                    v = step(v, gamma)
                eta = v[1] - rho * v[0]
                assert -gamma * Dstar < v[0] < gamma * Cstar
                assert eta > rho * gamma * Dstar
                x_capture = v[0]
                occupation = F(0)
                theta = c / (c + d)
                for _ in range(30):
                    old_eta = v[1] - rho * v[0]
                    occupation += gamma * ((1 if v[0] > 0 else 0) - theta)
                    v = step(v, gamma)
                    assert v[1] > 0
                    assert -gamma * Dstar < v[0] < gamma * Cstar
                    assert v[1] - rho * v[0] == old_eta + gamma * kappa
                assert occupation == -(v[0] - x_capture) / (c + d)
                assert abs(occupation) <= gamma
                sliding += 1

print(f"exact-rational cases: {dead + sliding}")
print(f"dead: {dead}; certified sliding: {sliding}; initial axis cases: {exact_axis}")
print(f"coefficients: c={c}, d={d}, kappa={kappa}, Cstar=Dstar={Cstar}")


# A prescribed rational residual changes cones after the initial double cone.
# Running-minimum reflection releases the positive-z normal, then recaptures it.
phases = ((F(1), F(-1), F(1)), (F(1), F(-1, 4), F(1)),
          (F(1), F(-2), F(1)))


def reflected(t):
    i1 = i2 = F(0)
    elapsed = F(0)
    minima = [F(0)]
    for duration, rr1, rr2 in phases:
        used = min(duration, max(F(0), t - elapsed))
        if used:
            i1 += used * rr1
            i2 += used * rr2
            minima.append(i1 + rho * i2)
        elapsed += duration
        if elapsed >= t:
            break
    w = i1 + rho * i2
    u = w - min(minima)
    v = rho * u + (1 - rho * rho) * i2
    return u, v


times = (F(0), F(1), F(2), F(13, 6), F(3))
states = tuple(reflected(t) for t in times)
assert states == ((F(0), F(0)), (F(0), F(3, 4)),
                  (F(1, 4), F(13, 8)), (F(0), F(13, 8)),
                  (F(0), F(9, 4)))
actions = ((F(0), F(3, 4)), (F(1, 4), F(7, 8)),
           (F(-3, 2), F(0)), (F(0), F(3, 4)))
for j, action in enumerate(actions):
    dt = times[j + 1] - times[j]
    increment = tuple(states[j + 1][k] - states[j][k] for k in (0, 1))
    assert increment == tuple(dt * action[k] for k in (0, 1))
print("reflected checkpoints:", list(zip(times, states)))
print("Schur/full-G action segments:", actions)


# Outside the double ratio cone, the finite selector can depend on gamma.
rr1, rr2 = F(-3), F(1)
aa, bb = -rr1, rr2
cc, dd = rho * bb, aa - rho * bb
kk = (1 - rho * rho) * bb
D = F(3)
general_dead = general_support = 0
for gamma in (F(1), F(1, 2)):
    for i in range(-20, 21):
        for j in range(-20, 21):
            v = (F(i, 4), F(j, 4))
            if v[1] <= 0:
                count = 0 if v[0] <= 0 else ceil(v[0] / (gamma * aa))
                for _ in range(count):
                    v = mixed_step(v, gamma, rr1, rr2)
                assert v[0] <= 0 and v[1] <= 0
                general_dead += 1
                continue
            eta0 = v[1] - rho * v[0]
            K = 0 if v[0] > -gamma * D else ((-gamma * D - v[0]) // (gamma * cc) + 1)
            M = max(0, (rho * gamma * D - eta0) // (gamma * kk) + 1)
            N = max(K, M)
            for n in range(N + 1):
                if v[1] <= 0:
                    count = 0 if v[0] <= 0 else ceil(v[0] / (gamma * aa))
                    for _ in range(count):
                        v = mixed_step(v, gamma, rr1, rr2)
                    assert v[0] <= 0 and v[1] <= 0
                    assert mixed_step(v, gamma, rr1, rr2) == v
                    general_dead += 1
                    break
                if n == K:
                    assert v[0] > -gamma * D
                if n == N:
                    assert v[0] > -gamma * D
                    assert v[1] - rho * v[0] > rho * gamma * D
                    for _ in range(30):
                        v = mixed_step(v, gamma, rr1, rr2)
                        assert v[0] > -gamma * D and v[1] > 0
                    general_support += 1
                    break
                v = mixed_step(v, gamma, rr1, rr2)

coarse = mixed_step((F(11, 10), F(3, 10)), F(1), rr1, rr2)
fine = (F(11, 10), F(3, 10))
fine_path = []
for _ in range(3):
    fine = mixed_step(fine, F(1, 2), rr1, rr2)
    fine_path.append(fine)
assert coarse == (F(-7, 5), F(-1, 5))
assert fine_path == [(F(-3, 20), F(1, 20)),
                     (F(1, 10), F(11, 20)), (F(-23, 20), F(3, 10))]
print(f"all-mixed exact-rational cases: {general_dead + general_support}; dead: {general_dead}; certified support: {general_support}")
print(f"all-mixed strict example: gamma=1 -> {coarse}; gamma=1/2 -> {fine_path}")

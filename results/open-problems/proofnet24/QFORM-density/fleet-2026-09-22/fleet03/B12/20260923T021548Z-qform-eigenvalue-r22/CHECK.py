import math

C_PAIR = 9.2 + math.log(10000.0)
C_TAIL = 9.0 * math.sqrt(3.0) * math.e / 2.0
C_TRIPLE = 6.0 * math.sqrt(math.pi)


def T(B, tau):
    return 4.0 * math.sqrt(B / tau)


def T_closed(B, tau, k):
    Bstar = 16.0 / tau
    return Bstar ** (1.0 - 2.0 ** (-k)) * B ** (2.0 ** (-k))


for tau in [1.0, 0.5, 1.0 / 64.0]:
    for B in [0.1, 1.0, 10.0, 16.0 / tau, 100.0, 1e6]:
        x = B
        for k in range(1, 21):
            x = T(x, tau)
            assert abs(x - T_closed(B, tau, k)) <= 1e-10 * max(1.0, abs(x))
            assert x <= max(B, 16.0 / tau) + 1e-9 * max(1.0, B, 16.0 / tau)

# The determinant-pair normalized envelope is decreasing for x>=1.
for j in range(100001):
    x = 1.0 + 999.0 * j / 100000.0
    deriv = (1.0 - 9.2 - math.log(10000.0 * x)) / (x * x)
    assert deriv < 0.0

print({
    "C_pair": C_PAIR,
    "C_tail": C_TAIL,
    "C_triple": C_TRIPLE,
    "scalar_fixed_point_tau_1": 16.0,
    "pair_exit_dominates_scalar_fixed_point_tau_1": C_PAIR > 16.0,
    "tau1_g1_collective_tail_chain_constant": max(C_TAIL, 16.0),
    "tau1_sigma1_protected_triple_chain_constant": max(C_TRIPLE, 16.0),
    "status": "PASS",
})

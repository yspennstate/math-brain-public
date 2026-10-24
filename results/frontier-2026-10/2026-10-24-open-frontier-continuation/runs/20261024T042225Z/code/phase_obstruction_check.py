"""Exact-Fraction checks for the prescribed polynomial return example."""

from fractions import Fraction as F


A = F(1, 2)
X0, Y0 = F(1, 4), F(-3, 8)
ETA = Y0 + A * X0


def one_gate_x(n: int, length: F) -> F:
    return X0 + F(n) - F(n * (n - 1), 1) / length


def literal_path(n_width: int, phase: F):
    length = F(n_width) + phase
    x, y = X0, Y0
    history = [(x, y)]
    for n in range(n_width + 5):
        first, second = x > 0, y > 0
        r1, r2 = 1 - F(2 * n, 1) / length, F(1)
        x, y = (
            x + (r1 if first else 0) - A * (r2 if second else 0),
            y - A * (r1 if first else 0) + (r2 if second else 0),
        )
        history.append((x, y))
    return length, history


def check(n_width: int, phase: F):
    length, history = literal_path(n_width, phase)
    for n in range(n_width + 2):
        x, y = history[n]
        assert x == one_gate_x(n, length)
        assert y == ETA - A * x
        assert x > 0 and y < 0
    x, y = history[n_width + 2]
    assert x == one_gate_x(n_width + 2, length)
    assert y == ETA - A * x
    assert x < 0
    if phase == 0:
        assert history[n_width + 1][0] == F(1, 4)
        assert x == -F(3, 4) - F(2, n_width)
        assert y == F(1, 8) + F(1, n_width)
        assert y > 0
        assert all(xx < 0 and yy > 0 for xx, yy in history[n_width + 2 :])
        sector = "single-2"
    else:
        assert phase == F(1, 2)
        assert history[n_width + 1][0] == F(3, 4) + F(1, 4) / length
        assert x == -F(1, 4) - F(3, 4) / length
        assert y == -F(1, 8) + F(3, 8) / length
        assert y < 0
        assert all((xx, yy) == (x, y) for xx, yy in history[n_width + 2 :])
        sector = "dead"
    incoming = history[n_width + 1]
    print(
        f"N={n_width:3d} phase={phase!s:>3s} L={length!s:>7s} "
        f"incoming={incoming!s:>25s} exit={(x, y)!s:>25s} sector={sector}"
    )


if __name__ == "__main__":
    assert ETA == -F(1, 4)
    for n_width in (3, 4, 10, 100):
        for phase in (F(0), F(1, 2)):
            check(n_width, phase)
    print("PASS: exact one-gate formula, first crossing, exit signs, and persistence")

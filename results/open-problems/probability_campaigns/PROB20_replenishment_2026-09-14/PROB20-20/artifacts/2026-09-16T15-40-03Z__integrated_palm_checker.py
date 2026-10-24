from fractions import Fraction


def g(x, lam, nu):
    """Residual cloud-mass fraction lower envelope."""
    return (lam - nu - x) / (lam - x)


def right_sum(lam, nu, c, N):
    """Exact right Riemann sum for the decreasing function g on [0,c]."""
    total = Fraction(0, 1)
    for r in range(1, N + 1):
        total += g(c * Fraction(r, N), lam, nu)
    return c * total / N


def enumerate_paths_to_threshold(threshold, max_part):
    """Ordered positive-integer increments, stopped at first threshold crossing."""
    out = []

    def rec(path, total):
        if total >= threshold:
            out.append(tuple(path))
            return
        for z in range(1, max_part + 1):
            rec(path + [z], total + z)

    rec([], 0)
    return out


def check_case(name, lam, nu, c, n, threshold, max_part, N=8):
    R = right_sum(lam, nu, c, N)
    old_rectangle = c * g(c, lam, nu)
    paths = enumerate_paths_to_threshold(threshold, max_part)

    min_slack = None
    min_path = None
    min_lhs = None

    for path in paths:
        y = Fraction(max(path), n)
        removed = 0
        sum_g = Fraction(0, 1)
        for z in path:
            if removed >= threshold:
                break
            x = Fraction(removed, n)
            sum_g += g(x, lam, nu)
            removed += z

        lhs = y * sum_g
        slack = lhs - R
        if min_slack is None or slack < min_slack:
            min_slack = slack
            min_path = path
            min_lhs = lhs

    # Finite exact falsification checks for the strengthened path inequality
    # y * sum_j g(x_j) >= integral_0^c g >= right Riemann sum R.
    assert min_slack is not None and min_slack >= 0
    # The integrated bound should strictly dominate the old terminal rectangle
    # c*g(c) in the three nonconstant test cases.
    assert R > old_rectangle

    return {
        "name": name,
        "lam": lam,
        "nu": nu,
        "c": c,
        "n": n,
        "threshold": threshold,
        "max_part": max_part,
        "N": N,
        "count": len(paths),
        "R": R,
        "old_rectangle": old_rectangle,
        "min_slack": min_slack,
        "min_path": min_path,
        "min_lhs": min_lhs,
    }


def fstr(q):
    return f"{q.numerator}/{q.denominator}"


def dstr(q):
    return f"{float(q):.15g}"


def main():
    cases = [
        ("A", Fraction(2), Fraction(1), Fraction(3, 4), 12, 9, 8),
        ("B", Fraction(3, 2), Fraction(1, 2), Fraction(2, 3), 12, 8, 8),
        ("C", Fraction(5, 2), Fraction(3, 2), Fraction(1, 2), 12, 6, 8),
    ]

    print("PROB20-20 integrated Palm path checker")
    print("All arithmetic below is exact Fraction arithmetic; decimals are display only.")

    for args in cases:
        r = check_case(*args)
        print(
            f"{r['name']} lambda={fstr(r['lam'])} nu={fstr(r['nu'])} "
            f"c={fstr(r['c'])} n={r['n']} threshold={r['threshold']} "
            f"max_part={r['max_part']} paths={r['count']} "
            f"R_{r['N']}={fstr(r['R'])} R_decimal={dstr(r['R'])} "
            f"old_rectangle={fstr(r['old_rectangle'])} "
            f"old_decimal={dstr(r['old_rectangle'])}"
        )
        print(
            f"{r['name']} min_lhs={fstr(r['min_lhs'])} "
            f"min_lhs_decimal={dstr(r['min_lhs'])} "
            f"min_slack={fstr(r['min_slack'])} "
            f"min_slack_decimal={dstr(r['min_slack'])} "
            f"minimizer={r['min_path']}"
        )

    print("PASS")


if __name__ == "__main__":
    main()

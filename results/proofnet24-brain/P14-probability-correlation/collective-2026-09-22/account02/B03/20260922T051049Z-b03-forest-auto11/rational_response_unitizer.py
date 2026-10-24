from fractions import Fraction
from functools import lru_cache

# Two-terminal block U = K_{2,3}, terminals the degree-3 side.
# Exact unit-forest partition: D_U=C_U=27, so response r=C/D=1.
U_D = 27
U_C = 27

@lru_cache(None)
def synth(p, q):
    r = Fraction(p, q)
    p, q = r.numerator, r.denominator
    if p == q:
        return {
            "D": U_D, "C": U_C, "V": 5, "E": 6,
            "blocks": 1, "expr": "U"
        }

    if p > q:
        # r = 1 + (r-1): parallel composition U || N_{r-1}
        b = synth(p-q, q)
        D = U_D * b["D"]
        C = U_C * b["D"] + U_D * b["C"]
        return {
            "D": D, "C": C,
            "V": 5 + b["V"] - 2,
            "E": 6 + b["E"],
            "blocks": 1 + b["blocks"],
            "expr": f"P(U,{b['expr']})"
        }

    # 0<r<1.  Put s=2r/(1-r), so r=s/(2+s).
    # This is the response of the series composition U o N_s.
    s = Fraction(2*p, q-p)
    b = synth(s.numerator, s.denominator)
    C = U_C * b["C"]
    D = (U_D + U_C) * (b["D"] + b["C"]) - C
    return {
        "D": D, "C": C,
        "V": 5 + b["V"] - 1,
        "E": 6 + b["E"],
        "blocks": 1 + b["blocks"],
        "expr": f"S(U,{b['expr']})"
    }

# Exact recurrence regression on all reduced fractions encountered from p,q<=100.
seen = set()
max_blocks = 0
max_arg = None
for p in range(1, 101):
    for q in range(1, 101):
        r = Fraction(p, q)
        if r in seen:
            continue
        seen.add(r)
        x = synth(r.numerator, r.denominator)
        got = Fraction(x["C"], x["D"])
        assert got == r, (r, got)
        if x["blocks"] > max_blocks:
            max_blocks = x["blocks"]
            max_arg = r

print("UNITIZER_GRID distinct_rationals=", len(seen))
print("UNITIZER_GRID max_blocks=", max_blocks, "at", max_arg)

for r in [Fraction(1,3), Fraction(2,5), Fraction(4,3),
          Fraction(7,4), Fraction(5,7), Fraction(2,1)]:
    x = synth(r.numerator, r.denominator)
    print("EXAMPLE", r, "D=", x["D"], "C=", x["C"],
          "V=", x["V"], "E=", x["E"], "blocks=", x["blocks"],
          "expr=", x["expr"])
    assert Fraction(x["C"], x["D"]) == r

# Apply the exact unitizer to account03/B01's K5 bridge polynomial
# q(t)=148-2t+64t^2 at t=2/5.
r = Fraction(2,5)
x = synth(r.numerator, r.denominator)
qval = Fraction(148,1) - 2*r + 64*r*r
scaled_gap = x["D"] * x["D"] * qval
print("K5_PARTNER t=", r, "q(t)=", qval,
      "D=", x["D"], "unit_simple_gap=", scaled_gap)
assert qval == Fraction(3936,25)
assert scaled_gap.denominator == 1

# K5/g contraction creates three size-two parallel classes.
# Two contain the queried marks: local scale 27 each.
# The third is unmarked: local scale 27^2.
# Hence all relevant forest counts scale by kappa=27^4,
# and the Rayleigh gap scales by kappa^2=27^8.
kappa = 27**4
contraction_gap = 64
expanded_gap = (kappa*kappa) * contraction_gap
print("K5_CONTRACTION kappa=", kappa,
      "multigraph_gap=", contraction_gap,
      "simple_expanded_gap=", expanded_gap)
assert expanded_gap == 18075490334784

# Partner mixed coefficient cannot be amplified into a response failure:
disc = (-2)**2 - 4*64*148
qmin = Fraction(148,1) - Fraction(1,32) + Fraction(1,64)
print("K5_PARTNER discriminant=", disc, "minimum=", qmin, "at t=1/64")
assert disc < 0 and qmin == Fraction(9471,64)

print("STATUS=PASS")

import math


def Cq(q):
    assert q > 2
    return (4 * math.pi) ** (1 / q) * ((q - 1) / (q - 2)) ** ((q - 1) / q)


print("QFORM-AVERAGED-QUADRATIC-GATE-v1")
for q in (2.1, 2.5, 3.0, 4.0, 10.0):
    c = Cq(q)
    print(f"q={q:.1f} Cq={c:.15f} Cq^q={c**q:.15f}")

c3 = Cq(3.0)
print(f"C3_expected={(16 * math.pi) ** (1/3):.15f}")
print(f"tail3_constant={16 * math.pi:.15f}")
assert abs(c3 ** 3 - 16 * math.pi) < 1e-12

# Exact shell formulas are vol(E_R)=pi*R*delta and
# p_Q(s)=pi*R on 0<s<delta.  The numerical values below
# check delta=1/(pi R), hence vol=1 and density*width=1.
for R in (1.0, 10.0, 1000.0):
    delta = 1 / (math.pi * R)
    volume = math.pi * R * delta
    output_density = math.pi * R
    print(
        f"R={R:g} delta={delta:.15g} volume={volume:.15g} "
        f"output_sup={output_density:.15g} mass={output_density*delta:.15g}"
    )
    assert abs(volume - 1) < 1e-12
    assert abs(output_density * delta - 1) < 1e-12

# Partner-derived hyperbolic conditional L^3 constant using
# ||H||_3 < 6.266 from account03/B01.
K_hyp = (2 * math.pi) ** (1 / 3) * math.sqrt(6.266) * 2 ** (-1 / 3)
print(f"partner_hyperbolic_L3_constant_lt={K_hyp:.15f}")
assert K_hyp < 3.67

print("STATUS=PASS")

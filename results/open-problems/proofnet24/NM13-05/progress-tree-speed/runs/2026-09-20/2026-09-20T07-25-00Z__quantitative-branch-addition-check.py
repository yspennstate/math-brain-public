from fractions import Fraction as Q


def A(l):
    return Q(6) * l / ((Q(3) - l) * (Q(9) - l)) - Q(4) * l / (Q(16) - l)


def t_upper(l):
    return (Q(9) - l) / (Q(2) * (Q(6) - l))


def t_lower(l):
    return Q(12) * (Q(15) - Q(4) * l) / (Q(5) * (Q(12) - l) * (Q(4) - l))


def theta(p, t):
    return p * t / (Q(1) - p + p * t)


def K(th):
    return (Q(3) + th) / (th * (Q(1) - th))


def F(l, th):
    aa = A(l)
    return Q(3) + th - aa * th * (Q(1) - th)


def vertex(l):
    aa = A(l)
    return (aa - Q(1)) / (Q(2) * aa)


def ppoly_num(l):
    return Q(29) * l * l - Q(328) * l + Q(720)


def qlower(l):
    return Q(2) * l * l - Q(15) * l + Q(24)


def fmt(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)


Llow = Q(1131, 400)
plow = Q(1, 3)
tu = t_upper(Llow)
thU = theta(plow, tu)
Alow = A(Llow)
Flow = F(Llow, thU)
vlow = vertex(Llow)
marglow = Q(2) * Flow / (Q(3) + thU + Llow) ** 2

Lhigh = Q(283, 100)
phigh = Q(2, 3)
tl = t_lower(Lhigh)
thL = theta(phigh, tl)
Ahigh = A(Lhigh)
Fhigh = F(Lhigh, thL)
vhigh = vertex(Lhigh)
marghi = Q(2) * Fhigh / (Q(4) + Lhigh) ** 2

Lq1 = Q(356, 125)
pq1 = Q(1, 4)
tu1 = t_upper(Lq1)
th1 = theta(pq1, tu1)
F1 = F(Lq1, th1)
m1 = Q(2) * F1 / (Q(3) + th1 + Lq1) ** 2

Lq2 = Q(713, 250)
pq2 = Q(3, 4)
tl2 = t_lower(Lq2)
th2 = theta(pq2, tl2)
F2 = F(Lq2, th2)
m2 = Q(2) * F2 / (Q(4) + Lq2) ** 2

lines = []
lines.append("NM13-05 T06 quantitative branch-addition exact checker")
lines.append(f"upper-ratio polynomial at max endpoint 2.852: P={fmt(ppoly_num(Lq2))} > 0")
lines.append(f"A3 derivative uniform lower bound inherited/proved: {fmt(Q(467,10816))} > 0")
lines.append(f"lower-ratio derivative numerator q(14/5)={fmt(qlower(Q(14,5)))} < 0")
lines.append(f"lower-ratio derivative numerator q(283/100)={fmt(qlower(Lhigh))} < 0")
lines.append("")
lines.append("LOW-MODERATE p<=1/3")
lines.append(f"L={fmt(Llow)}")
lines.append(f"t_upper(L)={fmt(tu)}")
lines.append(f"theta_upper={fmt(thU)}")
lines.append(f"A3(L)={fmt(Alow)}")
lines.append(f"old static gap 15-A3(L)={fmt(Q(15)-Alow)} < 0")
lines.append(f"old frontier bracket: 15-A3(1413/500)={fmt(Q(15)-A(Q(1413,500)))} > 0")
lines.append(f"old frontier bracket: 15-A3(2827/1000)={fmt(Q(15)-A(Q(2827,1000)))} < 0")
lines.append(f"quadratic vertex={fmt(vlow)}, theta_upper={fmt(thU)}, theta_upper<vertex={thU<vlow}")
lines.append(f"G_lower=F(theta_upper)={fmt(Flow)} > 0")
lines.append(f"-ell' uniform lower bound={fmt(marglow)} ~ {float(marglow):.12g}")
lines.append("")
lines.append("HIGH-MODERATE p>=2/3")
lines.append(f"L={fmt(Lhigh)}")
lines.append(f"t_lower(L)={fmt(tl)}")
lines.append(f"theta_lower={fmt(thL)}")
lines.append(f"A3(L)={fmt(Ahigh)}")
lines.append(f"old static gap 611/40-A3(L)={fmt(Q(611,40)-Ahigh)} < 0")
lines.append(f"old frontier bracket: 611/40-A3(2829/1000)={fmt(Q(611,40)-A(Q(2829,1000)))} > 0")
lines.append(f"quadratic vertex={fmt(vhigh)}, theta_lower={fmt(thL)}, theta_lower>vertex={thL>vhigh}")
lines.append(f"G_lower=F(theta_lower)={fmt(Fhigh)} > 0")
lines.append(f"-ell' uniform lower bound on new upper strip={fmt(marghi)} ~ {float(marghi):.12g}")
lines.append("")
lines.append("PREVIOUS HEADLINE TAILS IMPROVED")
lines.append(f"p<=1/4, L={fmt(Lq1)}, t_upper={fmt(tu1)}, theta_upper={fmt(th1)}")
lines.append(f"old static gap 52/3-A3(L)={fmt(Q(52,3)-A(Lq1))} < 0")
lines.append(f"G_lower={fmt(F1)}, -ell' lower bound={fmt(m1)} ~ {float(m1):.12g}")
lines.append(f"p>=3/4, L={fmt(Lq2)}, t_lower={fmt(tl2)}, theta_lower={fmt(th2)}")
lines.append(f"old static K(12/17)-A3(L)={fmt(K(Q(12,17))-A(Lq2))} < 0")
lines.append(f"G_lower={fmt(F2)}, -ell' lower bound={fmt(m2)} ~ {float(m2):.12g}")

assert ppoly_num(Lq2) > 0
assert Q(467, 10816) > 0
assert qlower(Q(14, 5)) < 0 and qlower(Lhigh) < 0
assert Q(15) - Alow < 0
assert Q(15) - A(Q(1413, 500)) > 0
assert Q(15) - A(Q(2827, 1000)) < 0
assert thU < vlow and Flow > 0 and marglow > 0
assert Q(611, 40) - Ahigh < 0
assert Q(611, 40) - A(Q(2829, 1000)) > 0
assert thL > vhigh and Fhigh > 0 and marghi > 0
assert Q(52, 3) - A(Lq1) < 0 and F1 > 0 and m1 > 0
assert K(Q(12, 17)) - A(Lq2) < 0 and F2 > 0 and m2 > 0

lines.append("ALL_EXACT_CHECKS_PASS")
print("\n".join(lines))

from decimal import Decimal, getcontext
getcontext().prec = 60

E = Decimal(1).exp()

def F(eps, delta):
    one = Decimal(1)
    a = (-eps).exp() / ((one-eps) ** (one-eps))
    b = eps.exp() / ((one+eps) ** (one+eps))
    q = one/(Decimal(2)*delta)
    return Decimal(3)*(a**q + b**q)

cases = [
    (Decimal(5)/Decimal(7), Decimal(1)/Decimal(14), Decimal(1)/Decimal(7)),
    (Decimal(5)/Decimal(8), Decimal(1)/Decimal(18), Decimal(3)/Decimal(16)),
]
for eps, delta, c in cases:
    val = F(eps, delta)
    print('eps=', eps, 'delta=', delta, 'c=', c)
    print('F=', val, '<1?', val < 1)
    print('delta/c=', delta/c)

sqrt_e = E.sqrt()
print('42 sqrt(e)=', Decimal(42)*sqrt_e)
print('32 sqrt(e)=', Decimal(32)*sqrt_e)
print('improvement ratio 32/54=', Decimal(32)/Decimal(54))
print('improvement percent=', Decimal(100)*(Decimal(1)-Decimal(32)/Decimal(54)))

# Exact simplification for eps=5/7, delta=1/14:
exact_clean = Decimal(3) * ((Decimal(49)/Decimal(4)) / (E**5) + (E**5)*(Decimal(7)/Decimal(12))**12)
print('clean exact-expression evaluation=', exact_clean)
assert abs(exact_clean - F(Decimal(5)/Decimal(7), Decimal(1)/Decimal(14))) < Decimal('1e-50')
assert F(Decimal(5)/Decimal(7), Decimal(1)/Decimal(14)) < 1
assert F(Decimal(5)/Decimal(8), Decimal(1)/Decimal(18)) < 1
assert (Decimal(1)/Decimal(14))/(Decimal(1)/Decimal(7)) == Decimal(1)/Decimal(2)
assert (Decimal(1)/Decimal(18))/(Decimal(3)/Decimal(16)) == Decimal(8)/Decimal(27)

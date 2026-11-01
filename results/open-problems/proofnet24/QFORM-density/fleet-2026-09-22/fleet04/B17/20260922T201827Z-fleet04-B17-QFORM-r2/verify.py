from decimal import Decimal, getcontext

getcontext().prec = 50
a = Decimal(57) / Decimal(32)
b = Decimal(3) / Decimal(4)
c = Decimal(15) / Decimal(4)
u = a.sqrt()
v = b.sqrt()
gamma = c - 2*u*v
kappa = (2*u + v)**2

assert gamma > 0
assert abs(kappa - (Decimal(63)/Decimal(8) + (Decimal(171)/Decimal(8)).sqrt())) < Decimal("1e-45")

# Four-row Hadamard exact identity.
hadamard = Decimal(4) * (
    a*(Decimal(1)/2)**2
    + c*(Decimal(1)/2)*(Decimal(1)/4)
    + b*(Decimal(1)/4)**2
)
assert hadamard == Decimal(123)/Decimal(32)
assert abs(hadamard - (kappa/4 + gamma/2)) < Decimal("1e-45")

print("gamma =", gamma)
print("kappa =", kappa)
print("kappa/20 =", kappa/20)
print("hadamard =", hadamard)
print("PASS QFORM-EDGEWORTH-FRAME-DEFICIT-SHARP-v1")

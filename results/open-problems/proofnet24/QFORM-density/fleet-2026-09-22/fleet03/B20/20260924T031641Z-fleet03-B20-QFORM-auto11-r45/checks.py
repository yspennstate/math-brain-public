from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
sqrt2 = D(2).sqrt()
sqrt3 = D(3).sqrt()
gamma0 = D(28159) / (D(4194304) * sqrt2)
tau = D(2) ** D(-16)
b0 = D(1) / (D(64) * sqrt3)
delta = tau / b0
Gamma = gamma0 / sqrt3 * (D(1) - delta) ** 2
CE3 = D("8.4530212255281768747")
epsilon = D(2) ** D(-12)
bound = CE3 * Gamma ** (-D(1)/D(3)) * epsilon ** (-D(1)/D(3))

assert gamma0 > D("0.00474725242887306016")
assert delta == sqrt3 / D(1024)
assert Gamma > D("0.00273156333189110832")
assert bound < D(968)
assert D(1) / D(442368) > D("0.00000226056134259259")
assert D(1) / D(128) == D("0.0078125")

print("gamma0 =", gamma0)
print("tau =", tau)
print("b0 =", b0)
print("delta =", delta)
print("Gamma =", Gamma)
print("E3 paid density bound =", bound)
print("diffuse selected-bank N-energy lower bound =", D(1)/D(442368))
print("heavy hub arm lower bound =", D(1)/D(128))

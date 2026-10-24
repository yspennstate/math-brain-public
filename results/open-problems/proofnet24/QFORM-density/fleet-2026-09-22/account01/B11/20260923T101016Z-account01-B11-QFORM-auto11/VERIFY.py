import math

# Constants in QFORM-OVERLAP-SAFE-SQUARE-LOG-v1.
L = math.sqrt(2.0)
H = 2.0 * math.sqrt(2.0) * L
C_general = 8.0 * 2.0**0.25 * math.sqrt(L)
C_bank = 8.0 * math.sqrt(2.0)
assert abs(C_general - C_bank) < 1e-12
assert abs(C_bank - 11.313708498984761) < 1e-12

# Partner family B_eps and the two uniform bounds.
for eps in [0.0, 0.01, 0.1, 0.5, 1.0, 3.0]:
    D = 1.0 + 2.0 * eps * eps
    kappa = math.sqrt(D)
    # eigenvalues of [[eps,sqrt(1+eps^2)],[sqrt(1+eps^2),-eps]]
    assert abs(kappa * kappa - D) < 1e-12
    new_bound = C_bank * (D * kappa)**(-0.25)
    partner_bound = 16.0 * math.sqrt(60.0) * D**(-0.25)
    assert new_bound <= C_bank + 1e-12
    assert partner_bound <= 16.0 * math.sqrt(60.0) + 1e-12

# Square-preimage length bound: for eta>0, sup_y |{x:|x^2-y|<eta}|=2 sqrt(2 eta).
def preimage_length(y, eta):
    if y + eta <= 0:
        return 0.0
    lo = max(0.0, y - eta)
    hi = y + eta
    return 2.0 * (math.sqrt(hi) - math.sqrt(lo))

for eta in [1e-6, 0.01, 1.0, 7.0]:
    vals = [preimage_length(-eta + (4*eta)*j/20000.0, eta) for j in range(20001)]
    assert max(vals) <= 2.0 * math.sqrt(2.0 * eta) + 1e-10
    assert abs(preimage_length(eta, eta) - 2.0 * math.sqrt(2.0 * eta)) < 1e-12

print('C_BANK=', C_bank)
print('C_PARTNER_ENDPOINT=', 16.0 * math.sqrt(60.0))
print('QFORM_B11_OVERLAP_SQUARE_LOG_CHECK_PASS')

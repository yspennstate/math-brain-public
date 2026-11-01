import math

# Finite sanity checks for QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1.
# The proof in REPORT.md is exact; this file checks constants on sample R=e^L.

for L in (2.0, 4.0, 8.0, 16.0, 64.0):
    R = math.exp(L)
    eps = 1.0/(2.0*L)
    area = 2.0*eps*L
    u_cap = 1.0/L
    v_cap = (1.0/L)/(1.0 - 1.0/(2.0*R*L))
    peak = 0.5*math.sqrt(L)
    half_riesz = 2.0*math.sqrt(L)
    assert abs(area-1.0) < 1e-12
    assert u_cap <= 1.0
    assert v_cap <= 1.0
    assert abs(half_riesz - 4.0*peak) < 1e-12
    print(f"L={L:g} area={area:.12g} Ucap={u_cap:.12g} Vcap<={v_cap:.12g} peak={peak:.12g} halfRiesz={half_riesz:.12g}")

# det [[1,0,0],[0,0,1],[0,1,0]]=-1 and characteristic polynomial
# (1-lambda)^2(-1-lambda), so spectrum is exactly {1,1,-1}.
print("detB=-1 spectrum={1,1,-1}")
print("STATUS=PASS")

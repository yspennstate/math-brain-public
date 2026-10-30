from math import sqrt

# Deterministic arithmetic checks for QFORM-TARGETSPECTRUM-FRESH-TRANSLATE-CAPS-FAIL-v1.
# No external packages.

def det_shifted(a, b, lam):
    # det([[a,b,0],[b,0,0],[0,0,1]] - lam I)
    return (1.0-lam)*((a-lam)*(-lam)-b*b)

for a in (1e-6, 1e-3, 0.1, 0.9):
    b = sqrt(1.0+a)
    logR = 4.0*b/(a**1.5)
    jac = sqrt(a)/(2.0*b)
    parameter_area = (a/2.0)*logR
    image_area = jac*parameter_area
    assert abs(image_area-1.0) < 1e-12
    for lam in (1.0+a, -1.0, 1.0):
        assert abs(det_shifted(a,b,lam)) < 1e-12
    lower = a/2.0
    upper = 5.0*a/4.0
    assert abs((upper-lower)-3.0*a/4.0) < 1e-15
    forced_peak = 1.0/(upper-lower)
    assert abs(forced_peak-4.0/(3.0*a)) < max(1e-12, 1e-12*forced_peak)
    print(f"a={a:g} b={b:.15g} area={image_area:.15g} support=[{lower:.15g},{upper:.15g}] forced_peak={forced_peak:.15g}")

print("STATUS=PASS")

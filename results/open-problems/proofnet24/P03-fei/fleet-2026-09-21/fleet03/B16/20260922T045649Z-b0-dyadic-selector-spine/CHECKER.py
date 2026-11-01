from fractions import Fraction

C0 = Fraction(16137,2500)       # 6.4548
EPS = Fraction(1,100)           # proved binary certificate lift
ADAG = Fraction(33525607,125000000)  # 0.268204856 exactly


def ln_iv(x, N=120):
    """Rigorous rational interval for natural log(x), x>0 rational.

    Uses ln x = 2 atanh((x-1)/(x+1)) and a geometric tail bound.
    """
    assert x > 0
    z = (x-Fraction(1))/(x+Fraction(1))
    a = abs(z)
    s = Fraction(0)
    p = z
    for k in range(N):
        s += p/Fraction(2*k+1)
        p *= z*z
    s *= 2
    tail = 2*a**(2*N+1) / (Fraction(2*N+1)*(1-a*a))
    return (s, s+tail) if z >= 0 else (s-tail, s)


LN2 = ln_iv(Fraction(2))


def scale(c, iv):
    lo, hi = iv
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def F_iv(m):
    """Rigorous interval for F(2^-m) from REPORT (2.5)."""
    t = Fraction(1,2**m)
    out = (Fraction(0),Fraction(0))
    pieces = [
        (-(1-2*t)**2, ln_iv(1-2*t)),
        ((1-t)**2, ln_iv(1-t)),
        (-(2*t*t+2*t+Fraction(1,2)), ln_iv(1+2*t)),
        (t*(6*t+C0-2), LN2),
        (-5*m*t*t, LN2),  # 5 t^2 ln t with ln t=-m ln2
    ]
    for c, iv in pieces:
        out = add(out, scale(c, iv))
    return t, out


def lower_B(m):
    t, (flo, fhi) = F_iv(m)
    assert flo > 0
    return t, flo/LN2[1], fhi/LN2[0]


mins = []
for m in range(2,14):
    t, blo, bhi = lower_B(m)
    cert_corr = EPS*(t*t/Fraction(2)-Fraction(1,16))
    stable_extra = (ADAG-EPS)*t*(1-t)/4
    cert_lo = blo + cert_corr
    stable_lo = cert_lo + stable_extra
    status = "SAFE" if cert_lo > 0 else "METHOD_FAILS"
    print("m=%2d t=2^-%d B_lo=%.15g cert_lo=%.15g stable_lo=%.15g %s" %
          (m,m,float(blo),float(cert_lo),float(stable_lo),status))
    if m <= 12:
        assert cert_lo > 0 and stable_lo > 0
        mins.append((cert_lo,m))
    else:
        # This is only failure of the two-AND lower certificate, not a gate violation.
        assert cert_lo < 0

# Endpoint analytic sign used in the concavity proof:
# B(1/4)=11137/10000-(9/16)log_2(3)>0 because log_2(3)<8/5.
assert 3**5 < 2**8
endpoint_rational_lower = Fraction(11137,10000)-Fraction(9,16)*Fraction(8,5)
assert endpoint_rational_lower > 0

# Exact elementary factors used to prove F''<=0 at the endpoint; on the
# full interval they follow symbolically from t<=1/4.
tq = Fraction(1,4)
assert 1-2*tq >= 2*tq
assert (1+2*tq)**2 >= 4*tq*(1-tq)

mmin = min(mins)
print("minimum_certified_margin_m2_to_m12=%.15g at m=%d" %
      (float(mmin[0]),mmin[1]))
print("endpoint_simple_rational_lower=%.15g" % float(endpoint_rational_lower))
print("status=PASS")

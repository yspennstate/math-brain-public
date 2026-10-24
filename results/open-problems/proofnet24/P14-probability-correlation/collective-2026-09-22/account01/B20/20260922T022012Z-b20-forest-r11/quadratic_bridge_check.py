import sympy as sp

A,B,Ae,Af,Aef,Be,Bf,Bef,t = sp.symbols(
    "A B Ae Af Aef Be Bf Bef t"
)

d0 = sp.expand(Ae*Af - A*Aef)
d1 = sp.expand(Be*Bf - B*Bef)
m  = sp.expand(Ae*Bf + Af*Be - Aef*B - Bef*A)

ce = sp.expand(Ae*B - A*Be)
cf = sp.expand(Af*B - A*Bf)

delta = sp.expand(
    (Ae+t*Be)*(Af+t*Bf)
    - (Aef+t*Bef)*(A+t*B)
)

print("DELTA_COEFFS", sp.Poly(delta, t).all_coeffs())
print("DELTA_MINUS_QUADRATIC",
      sp.expand(delta - (d0 + m*t + d1*t**2)))
print("AB_IDENTITY",
      sp.expand(A*B*m - (B**2*d0 + A**2*d1 - ce*cf)))

assert sp.expand(delta - (d0 + m*t + d1*t**2)) == 0
assert sp.expand(A*B*m - (B**2*d0 + A**2*d1 - ce*cf)) == 0

print("PASS")

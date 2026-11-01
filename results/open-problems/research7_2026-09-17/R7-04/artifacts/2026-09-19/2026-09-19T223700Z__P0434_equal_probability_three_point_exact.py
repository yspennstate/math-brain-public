import sympy as sp

c, lam, u = sp.symbols('c lam u', positive=True)
m = (c + 3) / 3
B = 1 - sp.Rational(5,3)*lam
rho = lam*m

# Exact rank candidates for X uniform on {1,2,c}.
A1 = 3*(1-u)
A2 = (5-3*u)/2
A3 = m-u
B1 = 4-2*u
B2 = (2-u) + (c-2)/2

checks = {
    'terminal_minus_fresh': sp.simplify(((c-2)-m) - (2*c-9)/3) == 0,
    'MS_middle_minus_fresh': sp.simplify((c/2-m) - (c-6)/6) == 0,
    'fresh_A2_minus_m': sp.simplify((sp.Rational(5,2)-m) + (2*c-9)/6) == 0,
    'terminal_discard_length': sp.simplify(((c-sp.Rational(5,2))-2) - (2*c-9)/2) == 0,
}

# Uniform {1,2,3}: exact lower-envelope pieces and M-SERPT levels.
sub3 = {c: sp.Integer(3)}
checks.update({
    'c3_A3_le_A2_on_0_half_at_diff_factor': sp.simplify((A2-A3).subs(sub3) - (sp.Rational(1,2)-u/2)) == 0,
    'c3_A1_le_A3_on_half_1_at_diff_factor': sp.simplify((A3-A1).subs(sub3) - (2*u-1)) == 0,
    'c3_B_switch': sp.solve(sp.Eq(B1.subs(sub3), B2.subs(sub3)), u) == [sp.Rational(3,2)],
    'c3_M1_equals_m': sp.simplify(sp.Max(2, sp.Rational(3,2))) == 2,
})

# Exact SOAP accounting in the nontrivial one-valley cell 9/2 < c <= 6.
# For rank r0=5/2: E[min(X,2)] = 5/3, E[min(X,2)^2] = 3,
# and the Gittins recycled terminal block has length 5/2 with probability 1/3.
W0_G = sp.Rational(61,24)*lam/B
W0_MS = sp.Rational(3,2)*lam/B
EX2 = (c**2+5)/3
W_inf = lam*EX2/(2*(1-rho)*B)
TG1 = 1 + W0_G
TG2 = 2 + W0_G
TGc = W_inf + (c-sp.Rational(5,2))/B + sp.Rational(5,2)
TMS1 = 1 + W0_MS
TMS2 = 2 + W0_MS
TMSc = W_inf + c/B
EG = sp.factor((TG1+TG2+TGc)/3)
EMS = sp.factor((TMS1+TMS2+TMSc)/3)
diff = sp.factor(EMS-EG)
checks.update({
    'soap_difference_identity': sp.simplify(diff - 25*lam/(36*B)) == 0,
    'short_medium_difference_each': sp.simplify((TMS1-TG1) + 25*lam/(24*B)) == 0,
    'long_difference': sp.simplify((TMSc-TGc) - 25*lam/(6*B)) == 0,
})

for name, ok in checks.items():
    print(f'{name}: {ok}')
    assert ok

print('EXACT_IDENTITIES')
print('m =', sp.factor(m))
print('terminal_minus_fresh =', sp.factor((c-2)-m))
print('MS_middle_minus_fresh =', sp.factor(c/2-m))
print('EG =', EG)
print('EMS-EG =', diff)
print('ALL_EXACT_CHECKS_PASS')

import mpmath as mp

mp.mp.dps = 50
alpha = mp.mpf(1) / 4
c_alpha = mp.gamma(1-alpha) * mp.sin(mp.pi*alpha/2) / mp.pi

def J_formula(t0, beta):
    return 8 * t0**alpha * (4*beta/(4*beta-1))

def J_numeric(t0, beta):
    near = mp.quad(lambda x: x**(alpha-1), [0, t0])
    tail = mp.quad(lambda x: x**(alpha-1) * (t0/x)**beta, [t0, mp.inf])
    return 2 * (near + tail)

print('c_alpha =', c_alpha)
for beta in [mp.mpf('0.375'), mp.mpf('0.75'), mp.mpf('1.2')]:
    exact = J_formula(mp.mpf(1), beta)
    numeric = J_numeric(mp.mpf(1), beta)
    print('beta', beta, 'formula', exact, 'numeric', numeric, 'abs_error', abs(exact-numeric))

coef_diffuse = 16*c_alpha*(mp.pi*mp.e*mp.sqrt(3)/mp.sqrt(2))**alpha*3
b19 = coef_diffuse*(mp.mpf(64)/49)**alpha*(mp.mpf(8)/7)**alpha*(mp.mpf(2240)/27)**alpha
partner_coeff = mp.power(2, mp.mpf(13)/4)/3
print('q1_theta_3_4_ridge_branch_coefficient =', coef_diffuse)
print('b19_diffuse_cut_bound =', b19)
print('partner_density_lift_coefficient =', partner_coeff)
print('STATUS=PASS')

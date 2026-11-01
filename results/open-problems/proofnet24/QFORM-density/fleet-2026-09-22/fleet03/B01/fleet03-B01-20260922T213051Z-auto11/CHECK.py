import mpmath as mp
mp.mp.dps=60
alpha=mp.mpf(1)/4
C_R=(mp.pi*mp.e/2)**alpha/(4*mp.gamma(alpha)*mp.cos(mp.pi/8))*mp.beta(mp.mpf(1)/16,mp.mpf(1)/16)
C_star=3*2**(mp.mpf(4)/3)*mp.e**(-mp.mpf(2)/3)*C_R**(mp.mpf(2)/3)
y=mp.e**(-1/alpha)
max_log=y**alpha*mp.log(1/y)
target=1/(alpha*mp.e)
H=C_R
A=2*mp.sqrt(2)
B=(4*2**(mp.mpf(1)/4)/mp.e)*H
rstar=(2*A/B)**(mp.mpf(2)/3)
f=A/rstar+B*mp.sqrt(rstar)
print('C_R =', mp.nstr(C_R,50))
print('C_star =', mp.nstr(C_star,50))
print('log_ineq_max =', mp.nstr(max_log,50))
print('log_ineq_target =', mp.nstr(target,50))
print('rstar_normalized =', mp.nstr(rstar,50))
print('f_normalized =', mp.nstr(f,50))
assert abs(max_log-target) < mp.mpf('1e-50')
assert abs(f-C_star) < mp.mpf('1e-50')
assert C_star < mp.mpf('8.799')
print('STATUS=QFORM_PAIRLOG_FRACTIONAL_RIESZ_CHECK_PASS')

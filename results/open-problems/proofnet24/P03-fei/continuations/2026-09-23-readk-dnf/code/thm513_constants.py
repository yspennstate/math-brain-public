# Recompute every numerical constant used in the proof of Theorem thm:thr-strong from the inequalities stated there
# (independent of the case-B audit, which checks the inequalities on instances).  Prints each constant and the value
# claimed in the text, and asserts the claimed value is on the safe side.
import math
out = []
def chk(name, value, claimed, direction):          # direction '<=' means value <= claimed must hold
    ok = value <= claimed + 1e-12 if direction == '<=' else value >= claimed - 1e-12
    out.append((name, value, claimed, direction, ok))
eps_max = 0.1
# (a) the other inputs: case |D| != t-1
Lp_lo = (2 / 3) * math.log(10)                          # L' > (2/3) ln 10
chk('(2/3) ln 10 > 1.53', Lp_lo, 1.53, '>=')
chk('rho_{j0} bound < 0.65', math.sqrt(2 / (math.pi * Lp_lo)), 0.65, '<=')
chk('ln(1-x) >= -1.5x at x=1/2 (margin)', math.log(0.5) + 0.75, 0.0, '>=')
Lp_max = 2 / (math.pi * (1 - eps_max) ** 2)
chk('L\' <= 2/(pi rho^2) < 0.79', Lp_max, 0.79, '<=')
root_lo = (1 - math.sqrt(1 - 4 * eps_max)) / 2
root_hi = (1 + math.sqrt(1 - 4 * eps_max)) / 2
chk('lower root of L(1-L)=0.1 < 0.113', root_lo, 0.113, '<=')
chk('upper root of L(1-L)=0.1 exceeds 0.79', root_hi, 0.79, '>=')
chk('L\' <= 1.128 eps  (1/(1-0.113))', 1 / (1 - root_lo), 1.128, '<=')
chk('Lambda\' <= 4.51 eps', 4 * 1 / (1 - root_lo), 4.51, '<=')
Lam = 4.51 * eps_max
chk('Lambda\' <= 0.451', Lam, 0.451, '<=')
# (b) J lower bounds
rhoU = 0.5 * (1 - root_lo)
chk('(1-q)(1-L\') > 0.44', rhoU, 0.44, '>=')
chk('0.44*0.56 >= eps(1-eps) at eps=0.1', 0.44 * 0.56, eps_max * (1 - eps_max), '>=')
chk('eps(1-eps) >= 0.9 eps', 1 - eps_max, 0.9, '>=')
chk('1-L\' >= 0.887', 1 - root_lo, 0.887, '>=')
# down-types: rho in [0.887q, 0.56], q <= 1/2
worst = min(min(0.887 * q * (1 - 0.887 * q), 0.56 * 0.44) / q for q in [k / 10000 for k in range(1, 5001)])
chk('rho(1-rho) >= 0.49 q for down-types', worst, 0.49, '>=')
# (c) sets containing j0
U_lo = eps_max * (1 - eps_max)   # U_d = eps(1-eps); ratio Lambda'/U_d uses eps(1-eps) >= 0.9 eps
chk('Lambda\' <= 5.02 U_d', 4.51 / 0.9, 5.02, '<=')
chk('ln 5.02 <= 1.62', math.log(5.02), 1.62, '<=')
chk('sum U^k/e <= 0.41 U (U <= 0.09)', 1 / (math.e * (1 - 0.09)), 0.41, '<=')
chk('I(d) <= Lambda\'/4 <= 1.26 U_d', 1.128 / 0.9, 1.26, '<=')
chk('0.41 + 1.62*1.26 <= 2.5', 0.41 + 1.62 * 1.26, 2.5, '<=')
# (d) sets avoiding j0
e1 = math.exp(Lam)
chk('e^{Lambda\'} <= 1.57', e1, 1.571, '<=')
chk('(1/2) e^{Lambda_D} <= 0.79', e1 / 2, 0.79, '<=')
xmax = 2 * 1.128 * eps_max
chk('2 L_U <= 0.23', xmax, 0.23, '<=')
chk('x(1+2ln(1/x)) <= 0.91 at x=0.23 (increasing below e^{-1/2})', 0.23 * (1 + 2 * math.log(1 / 0.23)), 0.91, '<=')
chk('q(1+2ln(1/q)) <= 1.2 at q=1/2', 0.5 * (1 + 2 * math.log(2)), 1.2, '<=')
chk('lambda=4L_U^2 <= 1/e', xmax ** 2, 1 / math.e, '<=')
U1 = 2 * (1 / math.e + 1) * 1.57 * 4.51 * eps_max / eps_max          # coefficient of eps Lambda_U
chk('family U-meet coefficient 19.4', U1, 19.4, '<=')
U2 = 2 * 0.91 * 2 * 0.79 / 2 * 0.451 * 4.51                          # 2*0.91*(2 L_U)*0.79*Lambda_D^2, L_U<=Lam_U/2
chk('family U-inside-D coefficient 2.9', U2, 2.93, '<=')
V1 = 2 * 1.2 * 1.57 * 4.51 * eps_max                                  # 2q*[q(1+2ln1/q)]*1.57 Lambda' Lambda_D, per q Lambda_D
chk('family V-meet-D coefficient 1.7', V1, 1.7, '<=')
V2 = 2 * 0.91 * 2 * 0.79 / 2 * 0.451 ** 2                            # 2*0.91*(2qL_D)*0.79*Lambda_U^2 per q Lambda_D
chk('family V-inside-U coefficient 0.3', V2, 0.3, '<=')
chk('(19.4+2.93)/0.9 <= 24.9', (19.4 + 2.93) / 0.9, 24.9, '<=')
chk('(1.7+0.3)/0.49 <= 4.1', (1.7 + 0.3) / 0.49, 4.09, '<=')
chk('2 + 24.9 <= 26.9', 2 + 24.9, 26.9, '<=')
# totals
chk('26.3/0.1 = 263', 26.3 / 0.1, 263, '<=')
chk('2*263 = 526', 2 * 263, 526, '<=')
chk('526/ln 2 < 760', 526 / math.log(2), 760, '<=')
bad = 0
for name, v, c, d, ok in out:
    print('%-58s value %.6f  claimed %s %.4f  %s' % (name, v, d, c, 'ok' if ok else 'FAIL'))
    bad += 0 if ok else 1
print('failures:', bad)

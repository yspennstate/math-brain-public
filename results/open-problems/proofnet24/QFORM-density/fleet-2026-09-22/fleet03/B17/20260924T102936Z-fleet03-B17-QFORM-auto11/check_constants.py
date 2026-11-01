from math import sqrt, pi, acos, exp

# Exact orientation B=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]].
M = [[6,-2,-3],[-2,3,-6],[-3,-6,-2]]
MM = [[sum(M[i][k]*M[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert MM == [[49,0,0],[0,49,0],[0,0,49]]

c = (sqrt(7)-1)/sqrt(13)
mu = 1 - acos(c)/pi
r = sqrt(2*pi/9)
kappa = 1 - mu*(1-r)
C_heavy = 3*sqrt(2)*kappa
partner = 3*sqrt(2)*exp(-0.03)
gap = partner-C_heavy

assert 0 < c < 1
assert 0 < mu < 1
assert 0 < r < 1
assert C_heavy < 3*sqrt(2)
assert partner > 4
assert gap > 0.3287
assert gap < 0.3288

print('c =', format(c, '.16f'))
print('mu =', format(mu, '.16f'))
print('r =', format(r, '.16f'))
print('kappa =', format(kappa, '.16f'))
print('C_heavy =', format(C_heavy, '.16f'))
print('partner_theta_0.01 =', format(partner, '.16f'))
print('gap =', format(gap, '.16f'))
print('PASS QFORM-ONE-HEAVY-GAUSSIAN-SEA-CONE-TIP-RIGIDITY-v1')

import math

L = 4096.0
h = 3.0/5.0

# Exact family: V = I-(2/5)11^T, M = diag(L,1,1,1,1)V.
# The singular values are L,1,1,1,1.

G = 10.0 * L**(6.0/5.0)
C_vol = 6.0*math.sqrt(math.e)*(2.0*h)**(-0.5)*(3.0-4.0*h)**(-1.0)
B_vol = C_vol * G**(-1.0/6.0)
B_d5 = 5.0*math.sqrt(2.0*math.e)*L**(-1.0/5.0)
B_hub = 3.0*2.0**(5.0/6.0)*L**(-1.0/3.0)

g = 1.0/L
k1 = L**2/(L**2+g)
k = 1.0/(1.0+g)
theta = k1 + 4.0*k
q = 2.0*k1
gap = theta - 2.0*q
D = (1.0+L**2/g)*(1.0+1.0/g)**4
B_ridge = math.e/(math.sqrt(2.0*q)*math.sqrt(g)) * theta/gap * D**(-1.0/(2.0*theta))

deriv = (-1.0/(2.0*h) + 4.0/(3.0-4.0*h)
         -(1.0/6.0)*(2.0*math.log(L)
                     + math.log(1.5*(1.0-h)/h)))

print('L', L)
print('G_h=3/5', repr(G))
print('dlogB/dh at 3/5', repr(deriv))
print('threshold exp(35/2)', repr(math.exp(17.5)))
print('hub', repr(B_hub))
print('ridge g=1/L', repr(B_ridge))
print('ridge k1', repr(k1), 'k', repr(k), 'theta', repr(theta),
      'q', repr(q), 'gap', repr(gap), 'D', repr(D))
print('optimized D-prime volume', repr(B_vol))
print('D5', repr(B_d5))
print('asymptotic displayed-ridge constant', repr(5.0*math.e/2.0))

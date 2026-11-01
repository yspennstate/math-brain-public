from sympy import symbols, diff, simplify

A, L, beta = symbols('A L beta', real=True)
phi = A + beta*L
a = -diff(phi, beta)
shifted = simplify(phi + (beta-1)*a)
unshifted = simplify(phi + beta*a)
phi1 = simplify(phi.subs(beta, 1))
F = simplify(phi - (beta-1)*diff(phi, beta))

assert simplify(shifted - phi1) == 0
assert simplify(F.subs(beta, 1) - phi1) == 0
assert simplify(unshifted - A) == 0

print('constant-transmission exact check')
print('phi(beta) = A + beta L')
print('a = -phi_prime(beta) =', a)
print('shifted spectrum = phi(beta)+(beta-1)a =', shifted)
print('unshifted expression = phi(beta)+beta*a =', unshifted)
print('failed-boundary anchor phi(1) =', phi1)
print('F(1)-phi(1) =', simplify(F.subs(beta,1)-phi1))
print('ALL_EXACT_CHECKS_PASS')

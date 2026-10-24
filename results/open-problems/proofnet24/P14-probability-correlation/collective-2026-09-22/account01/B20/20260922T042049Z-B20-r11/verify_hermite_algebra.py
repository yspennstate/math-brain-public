import sympy as sp

n, s, t = sp.symbols('n s t', integer=True)
E = 2*n + 6 - 3*s
Z = n**2 + 3*n + 10 - (n + 4)*s
J_dis = 5 - s
G = sp.expand(E**2 - Z*J_dis)
expected_G = (5-n)*s**2 + (n**2-4*n-6)*s - n**2 + 9*n - 14
assert sp.expand(G - expected_G) == 0

L = (n-4)*(n-1)*(n+4)/(n+1)**3
num = sp.expand(sp.together(G.subs(s, L) * (n+1)**6))
expected_num = 2*n**6 + 70*n**5 - 33*n**4 + 185*n**3 + 1369*n**2 - 3147*n + 1170
assert sp.expand(num - expected_num) == 0

shifted = sp.expand(num.subs(n, t+6))
expected_shifted = 2*t**6 + 142*t**5 + 3147*t**4 + 33233*t**3 + 187651*t**2 + 551661*t + 666396
assert sp.expand(shifted - expected_shifted) == 0

print('G(s)=', G)
print('(n+1)^6 G(L_n)=', num)
print('n=t+6:', shifted)
print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')

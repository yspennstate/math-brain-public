import sympy as sp

sqrt = sp.sqrt
R = sp.Rational

d = R(1,16)
alpha = R(1,2) - d - sqrt(2*d)
lev = sp.simplify(d/alpha)
q = R(149,100)
gap = sp.simplify(q/2 - lev)
C = sp.N(sp.E*3/(sqrt(2*q)*alpha*(3-2*q)), 15)

x = (2*sqrt(15)-3*sqrt(2))/14
dstar = sp.simplify(x**2)

d2 = R(3,50)
a2 = sp.simplify(R(1,2)-d2-sqrt(2*d2))
q2 = R(4,3)
C2 = sp.N(sp.E*3/(sqrt(2*q2)*a2*(3-2*q2)), 15)

K = 12
selected_row = R(3,4*K)
full_row = selected_row + R(1,4)
partner_bound = sp.simplify(12/(1-sqrt(R(3,K))))

print("alpha_1_16 =", sp.simplify(alpha), "=", sp.N(alpha,12))
print("left_leverage_bound =", lev, "=", sp.N(lev,12))
print("q/2 - leverage =", gap, "=", sp.N(gap,12))
print("C_1_16_simple =", C)
print("delta_star =", dstar, "=", sp.N(dstar,12))
print("alpha_3_50 =", a2, "=", sp.N(a2,12))
print("C_3_50_q4/3 =", C2)
print("partner selected row leverage =", selected_row)
print("partner full-range row leverage =", full_row)
print("partner mu =", R(1,K), "partner bound =", partner_bound)

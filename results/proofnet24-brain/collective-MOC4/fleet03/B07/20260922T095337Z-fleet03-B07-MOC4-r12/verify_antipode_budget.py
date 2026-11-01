import sympy as sp

lam, mu, m33 = sp.symbols("lambda mu m33", positive=True)
t = sp.symbols("t", real=True)
u = sp.symbols("u", real=True)

alpha = sp.sqrt(mu)
beta = sp.sqrt(lam)
mab = sp.sqrt(lam * mu)
# Cubic stationarity on the mixed-Schur kernel ray:
# m_a3*beta + m_3b*alpha = 0.
ma3 = u
m3b = -u * beta / alpha

ca, cb = sp.cos(alpha*t), sp.cos(beta*t)
sa, sb = sp.sin(alpha*t), sp.sin(beta*t)

# Exact difference f(x(t),y(t))-f(e3,e3) after sphere stationarity.
expr = (
    lam*(ca-1) + mu*(cb-1)
    + m33*(ca-1)*(cb-1)
    + ma3*sa*(cb-1)
    + m3b*(ca-1)*sb
    + mab*sa*sb
)

J2 = sp.simplify(sp.diff(expr, t, 2).subs(t, 0))
J3 = sp.simplify(sp.diff(expr, t, 3).subs(t, 0))
J4 = sp.factor(sp.diff(expr, t, 4).subs(t, 0))

Delta_L = 2*lam
Delta_R = 2*mu
Delta_LR = 2*(lam + mu - 2*m33)
identity = sp.simplify(J4 + sp.Rational(3,8)*Delta_L*Delta_R*Delta_LR)

print("J2=", J2)
print("J3=", J3)
print("J4=", J4)
print("J4+3/8*Delta_L*Delta_R*Delta_LR=", identity)
assert J2 == 0
assert J3 == 0
assert identity == 0

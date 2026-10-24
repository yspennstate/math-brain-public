from fractions import Fraction as Q


def p_only_margin(p,L):
    # R_p(L) = (1+pL)/(1-p)
    R=(1+p*L)/(1-p)
    delta=(L-(2*L-1)*R)/(1-L)
    margin=2*delta/(R+L)**2
    simplified=2*(1-p)*(1-L-2*p*L*L)/((1-L)*(1+L)**2)
    assert margin == simplified
    return R,delta,margin

print('P01 T06 exact self-check: lambda-dependent degree-tilt compression')

# Broad support-free rectangle: p=P(nu>=2)<=1/2, L=61/100.
p=Q(1,2); L=Q(61,100)
R,delta,margin=p_only_margin(p,L)
assert 2*p*L*L+L < 1
assert R == Q(261,100)
assert delta == Q(179,1950)
assert margin == Q(17900,1010919)
print('p<=1/2, L=61/100:')
print('  criterion slack =', 1-L-2*p*L*L)
print('  R =', R)
print('  numerator margin delta =', delta)
print('  derivative margin =', margin, float(margin))

# Second broad support-free point: p<=1/4, L=73/100.
p=Q(1,4); L=Q(73,100)
R,delta,margin=p_only_margin(p,L)
assert 2*p*L*L+L < 1
assert margin == Q(1775,269361)
print('p<=1/4, L=73/100:')
print('  criterion slack =', 1-L-2*p*L*L)
print('  derivative margin =', margin, float(margin))

# Two-point localization theorem: P(nu=1)=1-p, P(nu=D)=p,
# p<=1/2, D=11, L=2/3.
p=Q(1,2); D=11; L=Q(2,3)
theta = p*(1+L)/(D*(1-p)+p*(1+L))
a = L/(1-L)
theta_vertex=(a-1)/(2*a)
assert theta == Q(5,38)
assert theta < theta_vertex == Q(1,4)
G = 1+(D-1)*theta-a*(D-1)*theta*(1-theta)
assert G == Q(11,361)
den = 1+(D-1)*theta+L
assert den == Q(170,57)
margin = 2*G/(den*den)
assert margin == Q(99,14450)
print('two-point {1,11}, p<=1/2, L=2/3:')
print('  theta upper =', theta)
print('  convex-vertex theta0 =', theta_vertex)
print('  G lower =', G)
print('  derivative margin =', margin, float(margin))

# Immediate boundary of this particular localized certificate at D=12.
D=12
theta = p*(1+L)/(D*(1-p)+p*(1+L))
assert theta == Q(5,41)
assert theta < Q(1,4)
G12 = 1+(D-1)*theta-a*(D-1)*theta*(1-theta)
assert G12 == -Q(24,1681)
print('D=12 at p=1/2, L=2/3 certificate value =', G12, float(G12))
print('  (method boundary only; not a counterexample)')

# Algebraic p-only frontier: 2 p L^2 + L < 1.
# Check the old static p-envelope endpoint for p=1/2 was 3/5,
# while the new point 61/100 lies strictly above it.
old = Q(3,5)
assert Q(61,100) > old
print('old p=1/2 static-envelope endpoint =', old)
print('new certified rational endpoint =', Q(61,100))

print('ALL_EXACT_CHECKS_PASS')

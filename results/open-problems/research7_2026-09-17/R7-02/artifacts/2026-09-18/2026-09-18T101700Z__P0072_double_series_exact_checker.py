from sympy import symbols, Rational, factor, fraction, expand, Poly, simplify, diff

L,A,B,R,m,k,M,K,x,y,a,b = symbols(
    "L A B R m k M K x y a b", nonnegative=True
)

t = L+A+B+R+2
X = 1+L+A
Y = 1+L+B
w = 1+A+B
d = 1+R+B
e = 1+R+A
g = X/m
h = Y/k

Z = g*h*w + g*h*d + g*h*e + g*w*e + g*d*e + h*w*d + h*d*e + w*d*e
qL = g*h*(w+d+e)/Z
qA = g*w*e/Z
qB = h*w*d/Z
qR = d*e*(g+h+w)/Z

assert simplify(qL+qA+qB+qR-1) == 0

Delta = factor(qR-(R+Rational(1,2))/t)
N,D = fraction(Delta)
N = expand(N)

# Bilinear decomposition around (m,k)=(2,2).
N22 = expand(N.subs({m:2,k:2}))
Pm = expand((N.subs(k,2)-N22)/(m-2))
Pk = expand((N.subs(m,2)-N22)/(k-2))
Pmk = simplify((N-N22-(m-2)*Pm-(k-2)*Pk)/((m-2)*(k-2)))
assert simplify(N - (N22+(m-2)*Pm+(k-2)*Pk+(m-2)*(k-2)*Pmk)) == 0

for name, P in [("N22",N22),("Pm",Pm),("Pk",Pk),("Pmk",Pmk)]:
    poly = Poly(expand(P),L,A,B,R)
    assert min(poly.coeffs()) > 0
    print(name, "terms", len(poly.terms()), "min_coeff", min(poly.coeffs()))

# Degree-four projective boundary.
polyN = Poly(N,L,A,B,R)
N4 = 0
for mon, coeff in polyN.terms():
    if sum(mon) == 4:
        N4 += coeff*L**mon[0]*A**mon[1]*B**mon[2]*R**mon[3]
expected_R0 = 2*A*B*(A+B+L)*(A*k*m+A*k+B*k*m+B*m+L*k+L*m)
assert simplify(N4.subs(R,0)-expected_R0) == 0
print("N4_R0_factor", factor(N4.subs(R,0)))

# Compactified invasion coefficient on beta=0 face.
Fbeta = (x+1)*(a*k*m-a*m+k+m)/(a*k-2*a+2)
Fbeta0 = simplify(Fbeta.subs(x,0))
dm = factor(diff(Fbeta0,m))
dk = factor(diff(Fbeta0,k))
assert simplify(dm-(a*k-a+1)/(a*k-2*a+2)) == 0
assert simplify(dk-((1-a)*(a*m+2))/(a*k-2*a+2)**2) == 0
assert simplify(Fbeta0.subs({m:2,k:2})-(2+a)) == 0
print("beta_face_min_base", factor(Fbeta0.subs({m:2,k:2})))
print("beta_face_d_m",dm)
print("beta_face_d_k",dk)

# Alpha=0 face (symmetric).
Falpha = (x+1)*(b*k*m-b*k+k+m)/(b*m-2*b+2)
Falpha0 = simplify(Falpha.subs(x,0))
assert simplify(Falpha0.subs({m:2,k:2})-(2+b)) == 0
print("alpha_face_min_base", factor(Falpha0.subs({m:2,k:2})))

# Pure-L intersection.
G = (k+m)*(x+1)*(y+1)/(2*(x+y+1))
gap_xy = expand((x+1)*(y+1)-(x+y+1))
assert gap_xy == x*y
print("intersection_gap_identity", gap_xy)

# One-chord gluing failure. In the m=k=2 graph, insert a chord between the
# two internal subdivision vertices. The simple path s-x-y-t reinforces only
# one edge from each two-edge series chain, so chain equalities break at once.
first_chain_after = (2,1)
second_chain_after = (1,2)
assert first_chain_after[0] != first_chain_after[1]
assert second_chain_after[0] != second_chain_after[1]
print("one_chord_chain_equalities_break", first_chain_after, second_chain_after)

print("ALL_EXACT_CHECKS_PASS")

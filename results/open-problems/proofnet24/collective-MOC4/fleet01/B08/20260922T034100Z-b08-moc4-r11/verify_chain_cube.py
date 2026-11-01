from fractions import Fraction
from itertools import permutations

P = list(permutations(range(1,5)))
name = lambda p: ''.join(map(str,p))

def evt_single(p, i, j):
    return int(p[i-1] == j)

def evt_set(p, S, T):
    return int(tuple(sorted(p[i-1] for i in S)) == tuple(sorted(T)))

def deficit(p):
    # Exact compound-event-span witness.
    return (
        1
        - evt_single(p,1,2) + evt_single(p,1,3)
        - evt_single(p,2,2) - evt_single(p,3,2)
        - evt_set(p,(1,2),(1,3))
        + evt_set(p,(1,3),(1,2))
    )

d = {name(p): deficit(p) for p in P}
assert min(d.values()) == 0
assert max(d.values()) == 2
assert {k:v for k,v in d.items() if v} == {
    '1423':1,'1432':1,'2314':1,'2413':1,'3142':1,
    '3214':1,'3241':1,'3412':2,'3421':1,'4132':1,'4312':1
}

# Rational chain parameters c1=3/5,s1=4/5,c2=c3=7/25,s2=s3=24/25.
x = Fraction(9,25)
y = Fraction(16,25)
u = Fraction(49,625)
q = (1-u)*(1-u)
alpha = Fraction(3,5)*Fraction(4,5)*Fraction(24,25)*Fraction(24,25)

p0 = {
    '1234': x*u*u,
    '1243': x*u*(1-u),
    '1324': x*(1-u)*u,
    '1423': x*q,
    '2134': y*u*u,
    '2143': y*u*(1-u),
    '3124': y*(1-u)*u,
    '4123': y*q,
}
p1 = {
    '1423': y*q,
    '2413': y*u*(1-u),
    '2431': y*u*u,
    '3421': y*(1-u)*u,
    '4123': x*q,
    '4213': x*u*(1-u),
    '4231': x*u*u,
    '4321': x*(1-u)*u,
}
assert sum(p0.values(), Fraction()) == 1
assert sum(p1.values(), Fraction()) == 1
assert all(w >= 0 for w in p0.values())
assert all(w >= 0 for w in p1.values())

delta0 = sum(w*d[s] for s,w in p0.items())
delta1 = sum(w*d[s] for s,w in p1.items())
A, B = '4123', '1423'
C2 = alpha*alpha*(d[B]-d[A])**2
prod = delta0*delta1

assert delta0 == Fraction(2985984, 9765625)
assert delta1 == Fraction(6211584, 9765625)
assert C2 == Fraction(47775744, 244140625)
assert prod - C2 == -Fraction(114709561344, 95367431640625)
assert C2/prod == Fraction(390625,388224)

# Exact residual normal form.
a,b = Fraction(d[A]), Fraction(d[B])
r0 = (delta0 - q*(y*a+x*b))/(1-q)
r1 = (delta1 - q*(x*a+y*b))/(1-q)
assert r0 == 0
assert r1 == Fraction(18432,30025)
assert y-r1 == Fraction(784,30025)

rhs = (
    q*q*a*b
    + q*(1-q)*((y*a+x*b)*r1 + (x*a+y*b)*r0 - x*y*(a-b)**2)
    + (1-q)*(1-q)*r0*r1
)
assert rhs == prod-C2

print('PASS exact Fraction witness')
print('delta0 =', delta0)
print('delta1 =', delta1)
print('C^2 =', C2)
print('delta0*delta1-C^2 =', prod-C2)
print('C^2/(delta0*delta1) =', C2/prod)
print('r0 =', r0, 'r1 =', r1, 'y-r1 =', y-r1)

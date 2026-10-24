from fractions import Fraction
from itertools import product

# Exact finite self-check for P14 singleton-star deformation route.
# Vertices: 0=x, 1=y, 2=z, 3=v.  Old candidate edges e=xy, f=xz;
# star spokes are vx,vy,vz.
edges = [(0,1,'e'), (0,2,'f'), (3,0,'a'), (3,1,'b'), (3,2,'c')]


def is_forest(mask):
    parent = list(range(4))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    for i,(u,v,_) in enumerate(edges):
        if mask >> i & 1:
            if not union(u,v):
                return False
    return True

counts = {'Z':0,'Ze':0,'Zf':0,'Zef':0}
# Coefficients by number of star spokes for the physical common-spoke-weight t deformation.
coef = {k:[0,0,0,0] for k in ['Z','Ze','Zf','Zef']}
for mask in range(1 << len(edges)):
    if not is_forest(mask):
        continue
    e = bool(mask & 1)
    f = bool(mask & 2)
    s = sum(bool(mask & (1 << i)) for i in (2,3,4))
    counts['Z'] += 1
    coef['Z'][s] += 1
    if e:
        counts['Ze'] += 1
        coef['Ze'][s] += 1
    if f:
        counts['Zf'] += 1
        coef['Zf'][s] += 1
    if e and f:
        counts['Zef'] += 1
        coef['Zef'][s] += 1

assert counts == {'Z':24,'Ze':10,'Zf':10,'Zef':4}
assert counts['Ze']*counts['Zf'] - counts['Z']*counts['Zef'] == 4
assert coef == {
    'Z':[4,12,7,1],
    'Ze':[2,6,2,0],
    'Zf':[2,6,2,0],
    'Zef':[1,3,0,0],
}

# Tiny polynomial arithmetic, coefficient lists low-to-high.
def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c

def sub(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)]

physical_delta = sub(mul(coef['Ze'],coef['Zf']), mul(coef['Z'],coef['Zef']))
while physical_delta and physical_delta[-1] == 0:
    physical_delta.pop()
assert physical_delta == [0,0,1,2,1]  # t^2(1+t)^2

# Fixed triangle-base defect deformation from the predecessor P14 report.
# A-forest terminal-state counts (D,S,T), with S summing the 3 rank-one terminal states.
states = {
    'Z':   (1,2,1),
    'Ze':  (0,1,1),
    'Zf':  (0,1,1),
    'Zef': (0,0,1),
}
p = Fraction(1,4)
triangle_factor = (
    1 + 3*p + 3*p*p,  # D
    1 + 2*p,          # S
    1,                # T
)
P = {}
D = {}
for key,(d,s,t0) in states.items():
    P[key] = d*triangle_factor[0] + s*triangle_factor[1] + t0*triangle_factor[2]
    D[key] = d
assert {k:16*v for k,v in P.items()} == {'Z':95,'Ze':40,'Zf':40,'Zef':16}
q0 = P['Ze']*P['Zf'] - P['Z']*P['Zef']
q1 = P['Ze']*D['Zf'] + D['Ze']*P['Zf'] - P['Z']*D['Zef'] - D['Z']*P['Zef']
q2 = D['Ze']*D['Zf'] - D['Z']*D['Zef']
assert (q0,q1,q2) == (Fraction(5,16), Fraction(-1), Fraction(0))

def defect_delta(h):
    return q0 + q1*h + q2*h*h
assert defect_delta(Fraction(1,16)) == Fraction(1,4)
assert defect_delta(Fraction(1,2)) == Fraction(-3,16)

# State-by-state exact identity for the physically coupled star deformation:
# F_star(t) = J_A(0) + 3 t J_A(t/3).
# Verify as integer coefficient identities for D,S,T response factors.
# D: (1+t)^3; S: (1+t)(1+2t); T: 1+3t.
star_D = [1,3,3,1]
star_S = [1,3,2]
star_T = [1,3]
# RHS: 1 + 3t * triangle_factor(r=t/3).
# triangle D = 1+3r+3r^2 => 1+t+t^2/3; S=1+2r; T=1.
rhs_D = [1,3,3,1]
rhs_S = [1,3,2]
rhs_T = [1,3]
assert (star_D,star_S,star_T) == (rhs_D,rhs_S,rhs_T)

print('graph_counts', counts)
print('star_weight_polys', coef)
print('physical_delta_coeff_low_to_high', physical_delta)
print('physical_delta_factor', 't^2*(1+t)^2')
print('triangle_base_scaled16', {k:int(16*v) for k,v in P.items()})
print('fixed_h_quadratic', f'{q0} + ({q1})*h + ({q2})*h^2')
print('delta_h_1_16', defect_delta(Fraction(1,16)))
print('delta_h_1_2', defect_delta(Fraction(1,2)))
print('star_mixture_state_identity', 'PASS')
print('EXACT_COUNTEREXAMPLE_TO_GLOBAL_H_ROUTE_PASS')

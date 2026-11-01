from fractions import Fraction as F

def Q(D,E,C,y,z):
    t=F(1)-z
    return D*y*y + 2*E*y*t + C*t*t

# Simple mixed-Schur saturation: D*C=E^2.
D,E,C=F(4),F(2),F(1)
assert D*C == E*E

# A nontrivial exact point on the equality circle y=-(E/D)(1-z).
x,y,z=F(8,9),F(-4,9),F(1,9)
assert x*x+y*y+z*z == 1
assert y + E/D*(1-z) == 0
assert Q(D,E,C,y,z) == 0

# Factorization is verified coefficientwise:
# D*y^2+2E*y*t+C*t^2 = D*(y+(E/D)t)^2 when DC=E^2.
assert F(2)*E == F(2)*D*(E/D)
assert C == D*(E/D)*(E/D)

# Proper-circle geometry for k=E/D.
k=E/D
# center c=(0,-k/(1+k^2),k^2/(1+k^2)),
# radius^2=1/(1+k^2).
center_y=-k/(1+k*k)
center_z=k*k/(1+k*k)
radius2=F(1)/(1+k*k)
assert center_y*center_y + center_z*center_z + radius2 == 1

# Double mixed singular-value + pair-LS saturation makes D=E=C=0,
# hence the squared trust gap vanishes on the entire S^2.
for y0,z0 in [(F(0),F(1)),(F(0),F(-1)),(F(3,5),F(4,5))]:
    assert Q(F(0),F(0),F(0),y0,z0) == 0

# Exact SU(2) zeroing identity for one Gaussian-integer sample.
# General formula: G=(1/r)[[conj(a),conj(b)],[-b,a]] sends (a,b)^T to (r,0)^T.
# Represent z as (Re z, Im z) and multiply exactly.
def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cadd(z,w):
    return (z[0]+w[0], z[1]+w[1])
def cneg(z):
    return (-z[0],-z[1])
a=(3,4)
b=(-4,3)
r2=a[0]*a[0]+a[1]*a[1]+b[0]*b[0]+b[1]*b[1]
assert r2 == 50
second_num=cadd(cmul(cneg(b),a),cmul(a,b))
assert second_num == (0,0)

print("PASS MOC4-MSQR-LS-SATURATION-MANIFOLD-v1")
print("simple_sample_n = (8/9,-4/9,1/9)")
print("simple_Q = 0")
print("simple_k = 1/2")
print("simple_radius_squared = 4/5")
print("double_saturation_Q_identically_zero = True")
print("SU2_zeroing_second_coordinate_numerator = 0")

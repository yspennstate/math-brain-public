import math

# r22 finite algebra/constants check

def B(k,q,Z):
    a = k/(2*q)
    return (2*math.pi)**a * (math.e/q)**(a/2) * Z**(-a/(2*k))

def weighted_bound(k,q,Z,gamma):
    a=k/(2*q)
    assert 0<gamma<a
    return (2*a/(gamma*(a-gamma))) * (2*math.pi)**gamma * (math.e/q)**(gamma/2) * Z**(-gamma/(2*k))

def half_riesz(k,q,Z):
    a=k/(2*q)
    assert a>0.5
    return (4*a/(a-0.5))*(math.e/q)**0.25*Z**(-1/(4*k))

def l2sq(k,q,Z):
    a=k/(2*q)
    assert a>0.5
    return (4*a/(2*a-1))*(math.e/q)**0.5*Z**(-1/(2*k))

for k,q,Z,g in [(2,1,3.7,0.5),(2,1.4,0.2,0.4),(3,2,7.1,0.5),(5,2,0.03,0.7)]:
    a=k/(2*q); b=B(k,q,Z); T=b**(1/a)
    lhs=2*T**g*(1/g+1/(a-g))
    rhs=weighted_bound(k,q,Z,g)
    assert abs(lhs-rhs) <= 1e-11*max(1,abs(rhs))

C_half = 8*math.e**0.25
C_l2 = 4*math.sqrt(math.e)
C_coll = 8*math.sqrt(math.e)
assert abs(half_riesz(2,1,1)-C_half)<1e-12
assert abs(l2sq(2,1,1)-C_l2)<1e-12

# M -> cM: Z_2 -> c^4 Z_2 and half-Riesz scales c^-1/2.
for c in (0.07,0.5,3.0,11.0):
    z=1.3
    ratio = half_riesz(2,1,(c**4)*z)/half_riesz(2,1,z)
    assert abs(ratio-c**(-0.5))<1e-11

# Whole-form scaling (d,M)->(cd,cM): scalar-pivot density certificate scales c^-1.
for c in (0.13,0.8,2.0,9.0):
    d=1.7; z=0.9
    old=abs(d)**-0.5*half_riesz(2,1,z)
    new=abs(c*d)**-0.5*half_riesz(2,1,(c**4)*z)
    assert abs(new/old-c**-1)<1e-11

# Matrix-Chernoff union bound for a rank-two frame with max leverage 1/50.
eps=1/50
logbase=-0.5-0.5*math.log(0.5)
chernoff_union=4*math.exp(logbase/(2*eps))
assert chernoff_union < 0.087

# Diffuse rank-two application: Z2 >= 1/256.
Z2=1/256
H=half_riesz(2,1,Z2)
density=math.sqrt(50)*H
assert abs(H-16*math.e**0.25)<1e-12

print("QFORM_B03_R22_CHECK_PASS")
print(f"C_half_q1={C_half:.15f}")
print(f"C_l2_q1={C_l2:.15f}")
print(f"C_collision_q1={C_coll:.15f}")
print(f"chernoff_union_eps_1_over_50={chernoff_union:.15f}")
print(f"rank2_diffuse_half_riesz={H:.15f}")
print(f"psd_heavy_route_density={density:.15f}")

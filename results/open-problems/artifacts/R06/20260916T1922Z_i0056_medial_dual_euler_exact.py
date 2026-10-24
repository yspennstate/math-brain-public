from itertools import product
import sympy as sp

print("R06 I0056 medial dual-Euler checker")

r3 = sp.sqrt(3)
r5 = sp.sqrt(5)
phi = (1+r5)/2

# Exact vertex constants used for the two regular auxiliary graphs:
# H_{4,5}: retained R06 f>=5 result (Oh edge formula + closure theorem).
# H_{5,4}: Haslegrave-Panagiotis exact quadrangulation value.
h4 = 2/r3
h5 = phi

# Every partial k-gon has at least two cyclic selected/unselected transitions.
def transitions(bits):
    k=len(bits)
    return sum(bits[i] != bits[(i+1)%k] for i in range(k))

for k in (4,5):
    checked=0
    for bits in product((0,1), repeat=k):
        if all(b==0 for b in bits) or all(b==1 for b in bits):
            continue
        assert transitions(bits) >= 2
        checked += 1
    print(f"partial C{k} transition patterns checked: {checked} PASS")

# For a connected hole-filled finite S in the tetrapentagonal medial graph,
# Euler + 4-regularity gives F4+F5 = n-B/2+1.
# Auxiliary outer-vertex expansion gives h4 F4 <= Q4 <= B/2 and
# h5 F5 <= Q5 <= B/2. Therefore
# B >= 2(n+1)/(1+1/h4+1/h5).
L = sp.simplify(2/(1+1/h4+1/h5))
L_simple = 4/(1+r3+r5)
assert sp.simplify(L-L_simple) == 0

# Previous edge lower and certified ball upper.
L_old = r3-1
U = 2/r5
assert sp.N(L-L_old) > 0
assert sp.N(U-L) > 0

# Closure conversion for a 4-regular graph with edge lower h<1:
# Phi_V >= h/(4-3h).
V_old = (1+2*r3)/11
V_new = sp.simplify(L/(4-3*L))
V_simple = 1/(r3+r5-2)
assert sp.simplify(V_new-V_simple) == 0
assert sp.N(V_new-V_old) > 0
assert sp.N(U-V_new) > 0

# Edge-homogeneous growth cross-check. For edge symbol <4,4;4,5>,
# t=((4+4)/2-2)*((4+5)/2-2)=5, hence Graves-Pisanski-Watkins
# growth rate rho=g(5)=(3+sqrt(5))/2. The existing ball upper is
# exactly 2(rho-1)/(rho+1). This is evidence for an extremal-ball route,
# not a lower-bound proof.
t = sp.Rational(5)
rho = sp.simplify((t-2+sp.sqrt(t*t-4*t))/2)
assert sp.simplify(rho-(3+r5)/2) == 0
assert sp.simplify(2*(rho-1)/(rho+1)-U) == 0

width = sp.simplify(U-L)
print("h4 =", h4)
print("h5 =", h5)
print("new Phi_E lower =", sp.simplify(L_simple), "~=", float(L))
print("old Phi_E lower =", L_old, "~=", float(L_old))
print("ball Phi_E upper =", U, "~=", float(U))
print("new edge interval width =", width, "~=", float(width))
print("new Phi_V lower =", V_simple, "~=", float(V_new))
print("old Phi_V lower =", V_old, "~=", float(V_old))
print("growth rho =", rho, "; 2(rho-1)/(rho+1) =", sp.simplify(2*(rho-1)/(rho+1)))
print("PASS")

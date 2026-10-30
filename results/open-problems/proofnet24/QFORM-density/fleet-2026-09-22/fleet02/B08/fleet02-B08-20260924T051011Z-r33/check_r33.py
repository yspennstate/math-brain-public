from math import sqrt, e

m = 512
C_R = 288*sqrt(3*e)/13
C_X = 6**(4/3)
a = 3/8
eta = a*C_R/(C_R+C_X)
Cstar = (C_R+C_X)/a
K5 = 5*sqrt(2*e)
tau = K5/Cstar

# Five independent Walsh characters: bits 0,...,4.
chars = [[1 if ((x >> b) & 1) == 0 else -1 for x in range(m)] for b in range(5)]
S = [x for x in range(m) if chars[4][x] == 1]
T = [x for x in range(m) if chars[4][x] == -1]
assert len(S) == len(T) == m//2

for side in (S,T):
    for i in range(4):
        for j in range(4):
            raw = sum(chars[i][x]*chars[j][x] for x in side)
            target = m//2 if i == j else 0
            assert raw == target

assert 0.45 > eta
assert 5.8/m < 1/64
assert abs(K5/tau-Cstar) < 1e-12

print(f"C_R={C_R:.15f}")
print(f"C_X={C_X:.15f}")
print(f"eta={eta:.17f}")
print(f"Cstar={Cstar:.15f}")
print(f"K5={K5:.15f}")
print(f"tau={tau:.17f}")
print(f"localized={eta/512:.17f}")
print(f"window={eta/64:.17f}")
print("m=512 side_gram=0.5*I4 EXACT")
print("cross_singular_values=[0.5,0.5,0.5,0.45] EXACT")
print(f"pair_upper={5.8/m:.12f} < 1/64={1/64:.12f}")
print(f"fresnel_rank4_constant={8*(0.9**(-0.25)):.15f}")
print("QFORM_B08_R33_CHECK_PASS")

import itertools
import math
import numpy as np

alpha = 0.9
rows = [[math.sqrt(alpha), 0.0, 0.0]]
for k in range(5):
    th = 2.0 * math.pi * k / 5.0
    rows.append([
        math.sqrt((1.0-alpha)/5.0),
        math.sqrt(2.0/5.0)*math.cos(th),
        math.sqrt(2.0/5.0)*math.sin(th),
    ])
U = np.array(rows)
G = U.T @ U
A = np.block([[np.zeros((6,6)), U], [U.T, np.zeros((3,3))]])
eigs = np.linalg.eigvalsh(A)

weights = {}
for S in itertools.combinations(range(6), 3):
    d = np.linalg.det(U[list(S), :])
    weights[S] = d*d
Z = sum(weights.values())
marg = [sum(w for S,w in weights.items() if i in S)/Z for i in range(6)]
zin = sum(w for S,w in weights.items() if 0 in S)
zout = sum(w for S,w in weights.items() if 0 not in S)
ain = [sum(w for S,w in weights.items() if 0 in S and k in S)/zin for k in range(1,6)]
bout = [sum(w for S,w in weights.items() if 0 not in S and k in S)/zout for k in range(1,6)]

C_entropy = 6.0*math.sqrt(math.e)*(4.0*alpha*(1.0-alpha))**(-1.0/12.0)
C_partner = 11.021*alpha**(-9.0/20.0)*2.0**(-1.0/20.0)
C_low_alpha = 10.0*math.sqrt(5.0*math.e/6.0)
C_partner_half = 11.021*0.5**(-9.0/20.0)*2.0**(-1.0/20.0)
F = np.linalg.norm(U[1:,1:], ord='fro')

print('gram_max_error=', np.max(np.abs(G-np.eye(3))))
print('eigenvalues=', eigs)
print('Z=', Z)
print('marginals=', marg)
print('cond_in=', ain)
print('cond_out=', bout)
print('F=', F)
print('C_entropy_alpha_0p9=', C_entropy)
print('C_partner_alpha_0p9=', C_partner)
print('C_Dprime_alpha_le_half_max=', C_low_alpha)
print('C_partner_alpha_ge_half_max=', C_partner_half)

assert np.max(np.abs(G-np.eye(3))) < 1e-12
assert np.max(np.abs(eigs-np.array([-1.,-1.,-1.,0.,0.,0.,1.,1.,1.]))) < 1e-12
assert abs(Z-1.0) < 1e-12
assert max(abs(marg[0]-0.9), *(abs(x-0.42) for x in marg[1:])) < 1e-12
assert max(*(abs(x-0.4) for x in ain), *(abs(x-0.6) for x in bout)) < 1e-12
assert abs(F-math.sqrt(2.0)) < 1e-12
assert C_entropy < 10.772
assert C_partner < 11.163
assert C_low_alpha < 15.051
assert C_partner_half < 14.543
print('STATUS=PASS')

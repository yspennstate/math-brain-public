import math
import numpy as np

C_star = 8*math.sqrt(2)*3**0.75*5**0.25/math.sqrt(math.e)
B_partner = 9.8345318556
c = 0.5

print(f"C_star={C_star:.12f}")
print(f"previous_six_dim_B={B_partner:.12f}")
print(f"six_dim_m=4*c*B={4*c*B_partner:.12f}")
print(f"six_dim_new_bound={(1/c)*(2+math.log(4*c*B_partner)):.12f}")

print(f"bank_bound_rankone_square={2*(3+math.log(8)):.12f}")

def family_matrix(m):
    u = np.ones(m)/math.sqrt(m)
    B = np.outer(u,u)
    H = np.array([[1.0]])
    Z = np.zeros((m,m))
    bank = np.block([[Z,B],[B.T,Z]])
    return np.block([
        [H, np.zeros((1,2*m))],
        [np.zeros((2*m,1)), bank],
    ])

for m in [2,4,16,64]:
    A = family_matrix(m)
    eig = np.linalg.eigvalsh(A)
    nz = eig[np.abs(eig)>1e-10]
    cross_entry = 1/m
    print(
        f"m={m} nonzero_eigs="
        + ",".join(f"{x:.12f}" for x in nz)
        + f" cross_entry={cross_entry:.12f}"
    )

from math import sqrt

A = ((0,2,2),(2,0,2),(2,2,0))

def matvec(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

checks = {}
checks['det_B_star'] = det3(A)
checks['eigvec_plus4'] = matvec(A,(1,1,1))
checks['eigvec_minus2_a'] = matvec(A,(1,-1,0))
checks['eigvec_minus2_b'] = matvec(A,(1,0,-1))
checks['density_constant'] = 3*(2**(2/3))*(16**(-1/3))
checks['peer_half_riesz_constant'] = 128*(4**(-1/4))

assert checks['det_B_star'] == 16
assert checks['eigvec_plus4'] == (4,4,4)
assert checks['eigvec_minus2_a'] == (-2,2,0)
assert checks['eigvec_minus2_b'] == (-2,0,2)
assert abs(checks['density_constant'] - 3*(2**(-2/3))) < 1e-12
assert abs(checks['peer_half_riesz_constant'] - 64*sqrt(2)) < 1e-12

for k,v in checks.items():
    print(f'{k}: {v}')

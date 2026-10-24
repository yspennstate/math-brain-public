from fractions import Fraction as F

B = [
    [F(31,49), F(-36,49), F(-12,49)],
    [F(-36,49), F(-23,49), F(-24,49)],
    [F(-12,49), F(-24,49), F(41,49)],
]

def matmul(A,C):
    return [[sum(A[i][k]*C[k][j] for k in range(len(C)))
             for j in range(len(C[0]))]
            for i in range(len(A))]

I = matmul(B,B)
assert I == [[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]

pairs = [(0,1),(0,2),(1,2)]
mins = [B[i][i]*B[j][j]-B[i][j]*B[j][i] for i,j in pairs]
assert mins == [F(-41,49), F(23,49), F(-31,49)]
assert max(abs(B[i][i]) for i in range(3)) == F(41,49)
assert max(abs(x) for x in mins) == F(41,49)

c = F(5295,21952)
eta_coeff = F(41,49)
assert c / eta_coeff == F(5295,18368)

print('B^2 = I: PASS')
print('max |diag B| =', eta_coeff)
print('principal 2x2 minors B =', ', '.join(str(x) for x in mins))
print('max |minor B| =', max(abs(x) for x in mins))
print('Edgeworth coefficient =', c, float(c))
print('coefficient versus eta_m =', c/eta_coeff, float(c/eta_coeff))

for m in (3,10,100):
    eta = eta_coeff/F(m)
    pair = max(abs(x) for x in mins)/F(m*m)
    delta = F(1,m*m)
    padded_diag_bound = eta + delta
    padded_same_bound = F(82,49*m**3) + F(1,m**4)
    padded_cross_bound = F(41,49*m*m) + F(72,49*m**3) + F(1,m**4)
    print(
        'm=',m,
        'eta=',float(eta),
        'max_pair_det=',float(pair),
        'padded_diag_bound=',float(padded_diag_bound),
        'padded_det_bound=',float(max(padded_same_bound,padded_cross_bound)),
    )

print('ALL EXACT CHECKS PASSED')

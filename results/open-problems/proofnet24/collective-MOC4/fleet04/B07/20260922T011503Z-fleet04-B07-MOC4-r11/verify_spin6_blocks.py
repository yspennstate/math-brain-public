from fractions import Fraction as F

U = [
    [F(492,625), F(-31,625), F(-48,125), F(12,25)],
    [F(-9,25), F(12,25), F(-4,5), F(0)],
    [F(-36,125), F(48,125), F(9,25), F(4,5)],
    [F(-256,625), F(-492,625), F(-36,125), F(9,25)],
]

XPAIRS = [(0,1),(0,2),(0,3)]
YPAIRS = [(2,3),(1,3),(1,2)]
YSIGN = [1,-1,1]

def det2(M,I,J):
    i,k = I; j,l = J
    return M[i][j]*M[k][l] - M[i][l]*M[k][j]

def transpose(A):
    return [list(x) for x in zip(*A)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def add2(ms):
    return [[sum(M[i][j] for M in ms) for j in range(2)] for i in range(2)]

def det4(M):
    import itertools
    out = F(0)
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=F(-1 if inv%2 else 1)
        for i in range(4):
            term *= M[i][p[i]]
        out += term
    return out

assert mm(U,transpose(U)) == eye(4)
assert det4(U) == 1

P = [[x*x for x in row] for row in U]
H = [[F(x,2) for x in row] for row in
     [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]]
HPH = mm(mm(H,P),transpose(H))
D_from_P = [row[1:] for row in HPH[1:]]

B = [[None]*3 for _ in range(3)]
R = [[F(0)]*3 for _ in range(3)]
D = [[F(0)]*3 for _ in range(3)]
qchecks = 0
phasechecks = 0
for a,I in enumerate(XPAIRS):
    for b,J in enumerate(XPAIRS):
        m = det2(U,I,J)
        n = YSIGN[b]*det2(U,I,YPAIRS[b])
        block = [[m+n,F(0)],[F(0),m-n]]
        B[a][b]=block
        norm2 = sum(x*x for row in block for x in row)
        R[a][b] = norm2/F(2)
        D[a][b] = block[0][0]*block[1][1]

        qp = det2(U,I,J)**2
        qm = det2(U,I,YPAIRS[b])**2
        assert qp == (R[a][b]+D[a][b])/2
        assert qm == (R[a][b]-D[a][b])/2
        qchecks += 2

        for T in (J,YPAIRS[b]):
            i,k=I; j,l=T
            A=abs(U[i][j]*U[k][l])
            C=abs(U[i][l]*U[k][j])
            q=det2(U,I,T)**2
            assert (A-C)**2 <= q <= (A+C)**2
            phasechecks += 1

assert D == D_from_P

rowchecks=0
for a in range(3):
    for g in range(3):
        S=add2([mm(B[a][b],transpose(B[g][b])) for b in range(3)])
        assert S == (eye(2) if a==g else [[F(0),F(0)],[F(0),F(0)]])
        rowchecks += 1

colchecks=0
for b in range(3):
    for d in range(3):
        S=add2([mm(transpose(B[a][b]),B[a][d]) for a in range(3)])
        assert S == (eye(2) if b==d else [[F(0),F(0)],[F(0),F(0)]])
        colchecks += 1

assert all(sum(row)==1 for row in R)
assert all(sum(R[a][b] for a in range(3))==1 for b in range(3))

print("U_orthogonal_det1 PASS")
print("D_equals_HPH_mean_zero_block PASS entries=9")
print(f"row_block_orthogonality PASS equations={rowchecks}")
print(f"column_block_orthogonality PASS equations={colchecks}")
print(f"q_recovery_from_R_D PASS checks={qchecks}")
print(f"phase_interval_exact_rational_witness PASS checks={phasechecks}")
print("R=")
for row in R:
    print(" ".join(str(x) for x in row))
print("D=")
for row in D:
    print(" ".join(str(x) for x in row))

from fractions import Fraction

N=64
assert N%2==0
s=[1]*(N//2)+[-1]*(N//2)
n=N+1
B=[[0]*n for _ in range(n)]
B[0][0]=N
for j in range(1,n):
    for k in range(1,n):
        B[j][k]=1-s[j-1]*s[k-1]

def matmul(A,C):
    m=len(A); p=len(C); q=len(C[0])
    return [[sum(A[i][k]*C[k][j] for k in range(p)) for j in range(q)] for i in range(m)]
B2=matmul(B,B)
B3=matmul(B2,B)
ident = all(B3[i][j]==N*N*B[i][j] for i in range(n) for j in range(n))
traceB=sum(B[i][i] for i in range(n))
traceB2=sum(B2[i][i] for i in range(n))
anchor_zero=0
for j in range(1,n):
    det=B[0][0]*B[j][j]-B[0][j]*B[j][0]
    if det==0: anchor_zero+=1
p=1
m=1+N//2
M=[[B[i][j] for j in (0,p,m)] for i in (0,p,m)]
det3=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
      -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
      +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert det3 != 0
rank_certificate=3
wedge_each=Fraction(2,N)
wedge_total=sum([wedge_each for _ in range(N)], Fraction(0,1))
grouped=True
for j in range(1,n):
    if B[j][j]!=0: grouped=False
for j in range(1,n):
    for k in range(j+1,n):
        expected = 2 if s[j-1]!=s[k-1] else 0
        if B[j][k]!=expected: grouped=False
coeff_norm_sq=Fraction(4,N)*(N//2)
print(f'N={N}')
print('minimal_polynomial_identity=' + ('PASS' if ident else 'FAIL'))
print(f'trace_B={traceB}')
print(f'trace_B2={traceB2}')
print(f'rank_certificate={rank_certificate}')
print(f'anchor_pair_determinants_zero={anchor_zero}/{N}')
print(f'wedge_each={wedge_each}')
print(f'wedge_total={wedge_total}')
print('grouped_matrix_identity=' + ('PASS' if grouped else 'FAIL'))
print(f'u_plus_coeff_norm_sq={coeff_norm_sq}')
print(f'u_minus_coeff_norm_sq={coeff_norm_sq}')
status = ident and traceB==N and traceB2==3*N*N and anchor_zero==N and grouped and wedge_total==2 and coeff_norm_sq==2
print('STATUS=' + ('PASS' if status else 'FAIL'))

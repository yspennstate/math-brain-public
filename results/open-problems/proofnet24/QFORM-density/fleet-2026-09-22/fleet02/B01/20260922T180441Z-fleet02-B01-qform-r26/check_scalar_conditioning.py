from fractions import Fraction
from itertools import combinations

eps=Fraction(1,128)
T=[
 [Fraction(1,2),Fraction(1,2),Fraction(-1,2),Fraction(-1,2)],
 [Fraction(1,2),Fraction(-1,2),Fraction(1,2),Fraction(-1,2)],
 [Fraction(1,2),Fraction(-1,2),Fraction(-1,2),Fraction(1,2)],
 [Fraction(1,2),Fraction(1,2),Fraction(1,2),Fraction(1,2)],
]
def tr(A): return [list(r) for r in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det(M):
    n=len(M)
    if n==1: return M[0][0]
    return sum((Fraction(-1) if j%2 else Fraction(1))*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))
D=[[Fraction(0) for _ in range(4)] for __ in range(4)]
for i,v in enumerate([Fraction(1),Fraction(1),Fraction(-1),eps]): D[i][i]=v
A=mm(tr(T),mm(D,T))
I4=[[Fraction(int(i==j)) for j in range(4)] for i in range(4)]
print('T_orthogonal=', mm(T,tr(T))==I4)
print('detA=',det(A))
mins=[]
for I in combinations(range(4),3):
    M=[[A[i][j] for j in I] for i in I]
    mins.append((I,det(M)))
print('principal_3x3_dets=',mins)
print('expected_minor=',-Fraction(1,4)*(1+eps))
print('r25_density_bound=',float(216*(4/(1+float(eps)))**(1/3)))
print('core_physical_diag=',Fraction(1,4))
print('core_row_leverage=',Fraction(3,4))
print('partner_factor=(16/3)^(1/4)=',float((16/3)**0.25))
for delta in [Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(1,16),Fraction(1,32)]:
    h=Fraction(8,3)*delta**3
    lower=Fraction(1,3)/delta**2
    print('delta',delta,'h',h,'conditional_sup_lower',lower,'h*lower',h*lower)
assert all(d == -Fraction(129,512) for _,d in mins)
print('STATUS=PASS')

from fractions import Fraction


def matmul(A,B,n):
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik=A[i][k]
            if aik:
                for j in range(n):
                    C[i][j]+=aik*B[k][j]
    return C

def charpoly_coeffs(A):
    n=len(A)
    # Newton identities using traces A^k; returns monic coefficients c1..cn
    P=[row[:] for row in A]
    traces=[0]*(n+1)
    traces[1]=sum(P[i][i] for i in range(n))
    for k in range(2,n+1):
        P=matmul(P,A,n)
        traces[k]=sum(P[i][i] for i in range(n))
    c=[0]*(n+1); c[0]=1
    for k in range(1,n+1):
        s=sum(c[k-i]*traces[i] for i in range(1,k+1))
        assert (-s)%k==0
        c[k]=(-s)//k
    return c[1:]

def bits_to_B(mask,n):
    return [[(mask>>(i*n+j))&1 for j in range(n)] for i in range(n)]

def B_to_A(B):
    return [[1-2*b for b in row] for row in B]

def vecmul(B,v):
    n=len(B)
    return [sum(B[i][j]*v[j] for j in range(n))&1 for i in range(n)]

def dot2(u,v):
    return sum(a*b for a,b in zip(u,v))&1

def krylov_event(B):
    n=len(B); u=[1]*n; v=u[:]
    moms=[]
    for k in range(n):
        moms.append(dot2(u,v))
        if k<n-1: v=vecmul(B,v)
    return moms[:-1]==[0]*(n-1) and moms[-1]==1, tuple(moms)

def coeff_event(A):
    n=len(A); c=charpoly_coeffs(A)
    # F(y)=chi_A(2y)/2^(n-1): leading coefficient 2,
    # and coefficient for y^(n-k) is c_k/2^(k-1).
    scaled=[]
    for k,ck in enumerate(c, start=1):
        d=1<<(k-1)
        assert ck%d==0, (n,k,ck)
        scaled.append(ck//d)
    # F mod 2 = 1: all positive-degree non-leading coefficients even,
    # constant odd.
    return all(x%2==0 for x in scaled[:-1]) and scaled[-1]%2==1, tuple(scaled), tuple(c)

def formula_count(n):
    assert n%2==0 and n>=2
    prod=1
    for j in range(1,n-1):
        prod*= (2**(n-1)-2**j)
    return 2**(2*n-1)*prod

def formula_prob(n):
    return Fraction(formula_count(n), 2**(n*n))

print('F0013 even-n 2-adic Krylov/Eisenstein exact self-check')
print('checker=python stdlib exact integers only')
for n in (2,4):
    total=1<<(n*n)
    kc=cc=0
    moment_hist={}
    for mask in range(total):
        B=bits_to_B(mask,n)
        ke,moms=krylov_event(B)
        A=B_to_A(B)
        ce,scaled,c=coeff_event(A)
        if ke: kc+=1
        if ce: cc+=1
        if ke!=ce:
            raise AssertionError((n,mask,ke,ce,moms,scaled,c))
        moment_hist[moms]=moment_hist.get(moms,0)+1
    f=formula_count(n)
    assert kc==cc==f
    print(f'n={n} total={total} krylov_count={kc} coeff_eisenstein_count={cc} formula_count={f} probability={formula_prob(n)}')

arch_irred={2:8,4:9024,6:11307502080}
for n in (2,4,6,8,10,12):
    cnt=formula_count(n); prob=formula_prob(n)
    line=f'n={n} formula_count={cnt} probability={prob}'
    if n in arch_irred:
        ir=arch_irred[n]
        assert cnt<=ir
        line += f' archived_irreducibles={ir} certified_fraction_of_archived_irreducibles={Fraction(cnt,ir)}'
    print(line)

# Additional exact divisibility sanity: every characteristic coefficient for n<=4
# obeys the universal 2^(k-1) divisibility used in the transformed polynomial.
print('ALL_EXACT_CHECKS_PASS')

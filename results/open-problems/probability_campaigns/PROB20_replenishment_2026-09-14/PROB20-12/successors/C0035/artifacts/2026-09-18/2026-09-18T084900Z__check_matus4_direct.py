from fractions import Fraction
from itertools import combinations, permutations, product

STATES = [(0,0),(0,1),(1,0),(1,1)]

def det(A):
    n=len(A)
    if n==0:
        return Fraction(1)
    A=[row[:] for row in A]
    ans=Fraction(1)
    for i in range(n):
        pivot=next((r for r in range(i,n) if A[r][i]),None)
        if pivot is None:
            return Fraction(0)
        if pivot!=i:
            A[i],A[pivot]=A[pivot],A[i]
            ans=-ans
        pv=A[i][i]
        ans*=pv
        for j in range(i,n):
            A[i][j]/=pv
        for r in range(i+1,n):
            c=A[r][i]
            if c:
                for j in range(i,n):
                    A[r][j]-=c*A[i][j]
    return ans

def cyl(p,a,b,bits):
    coeff={0:p,1:a,-1:a,2:b,-2:b}
    ones=[i for i,x in enumerate(bits) if x]
    zeros=[i for i,x in enumerate(bits) if not x]
    out=Fraction(0)
    for r in range(len(zeros)+1):
        for C in combinations(zeros,r):
            S=ones+list(C)
            M=[[coeff.get(j-i,Fraction(0)) for j in S] for i in S]
            out += (-1 if r%2 else 1)*det(M)
    return out

def table(p,a,b):
    probs={bits:cyl(p,a,b,bits) for bits in product([0,1],repeat=4)}
    marg={}
    P={}
    for i,s in enumerate(STATES):
        marg[i]=sum((v for bits,v in probs.items() if bits[:2]==s),Fraction())
        for j,t in enumerate(STATES):
            P[i,j]=probs[s+t]
    return marg,P,probs

def check(name,p,a,b):
    marg,P,probs=table(p,a,b)
    assert min(probs.values())>=0
    passed=0
    min_rational_margin=None
    min_gap_desc=None
    for perm in permutations(range(4)):
        i1,i2,i3,i5=perm
        # Four-state corollary of Matus: label 4 is absent.
        # L0 + sqrt(q) >= R.
        L0=P[i1,i3]+P[i5,i1]+P[i5,i2]+P[i5,i5]
        q=P[i3,i2]
        R=Fraction(1,4)*marg[i5]**2*P[i1,i1]*P[i1,i2]*P[i2,i3]
        assert q>=0
        if R<=L0:
            ok=True
            rational_margin=L0-R
        else:
            ok=(R-L0)**2<=q
            rational_margin=None
        assert ok
        passed += 1
        if rational_margin is not None and (min_rational_margin is None or rational_margin<min_rational_margin):
            min_rational_margin=rational_margin
            min_gap_desc=(perm,L0,q,R)
    print(name)
    print("marginals", [str(marg[i]) for i in range(4)])
    print("pair_table")
    for i in range(4):
        print("  ", [str(P[i,j]) for j in range(4)])
    print("all_24_Matus4_PASS", passed==24)
    print("all_24_already_pass_without_sqrt", all(
        Fraction(1,4)*marg[perm[3]]**2*P[perm[0],perm[0]]*P[perm[0],perm[1]]*P[perm[1],perm[2]]
        <= P[perm[0],perm[2]]+P[perm[3],perm[0]]+P[perm[3],perm[1]]+P[perm[3],perm[3]]
        for perm in permutations(range(4))
    ))
    print("smallest_rational_L0_minus_R", min_rational_margin)
    print("attaining_data", min_gap_desc)
    print()

check("sublattice_base_p=1/2_a=0_b=1/8", Fraction(1,2), Fraction(0), Fraction(1,8))
check("mixed_symbol_p=1/2_a=1/8_b=1/8", Fraction(1,2), Fraction(1,8), Fraction(1,8))
print("PASS")

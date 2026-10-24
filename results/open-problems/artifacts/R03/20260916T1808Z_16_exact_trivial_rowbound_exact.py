#!/usr/bin/env python3
"""
R03 exact checker — exact trivial row/column collision remainder.

Self-checks:
  1. Exhaust all iid sign matrices through n=4 and verify:
     - sign normalization to (n-1)x(n-1) binary matrices;
     - no signed row/column pair <=> binary matrix has no zero row/column
       and all rows/columns are distinct;
     - exact collision-free probability agrees with the signed-Stirling
       graph formula and with the A094000 Stirling formula.
  2. Verify the two exact formulas agree for n=2..12.
  3. Verify the current source sequence identity
       A116527(m)=A000410(m)-A000409(m), m=2..9.
     These sequence values are external exact source data; this checker
     verifies their arithmetic consequences, not their original enumeration.
  4. Compute source-backed normalized residual values
       r(n)=2^n P(singular AND no signed row/column pair)
     from the current A116527 table.  Values through n=9 are also covered
     by the published order<=8 classification used in prior R03 reports.
     The n=10 value uses the July-2026 order-9 database extension and is
     printed as SOURCE-BACKED ONLY, not promoted to the strict metric.
  5. Cross-check the source-backed n=10 arithmetic against A046747(9)
     and A094000(9).
  6. Refine retained C243 at its final F3 hyperplane step by classifying
     nonfat hyperplanes of cube density 3/8.  This strictly improves the
     rigorous n=10 residual bound.
  7. Subtract the exact trivial-collision mass.  This gives the strict
     full-domain R03 envelope: exact through n=9, refined-F3 from n=10.
  8. Exhibit the finite m=4 obstruction to naively multiplying row-good and
     column-good constraints inside the singular class.
"""
from itertools import product
from fractions import Fraction
from math import comb, factorial

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A)
    if n==0: return 1
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k]
            sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]

def normalize_sign(B):
    n=len(B)
    b11=B[0][0]
    N=[[B[i][j]*B[i][0]*B[0][j]*b11 for j in range(n)] for i in range(n)]
    A=[[(1-N[i][j])//2 for j in range(1,n)] for i in range(1,n)]
    return N,A

def signed_pair_collision(B):
    n=len(B)
    rows=[tuple(r) for r in B]
    cols=[tuple(B[i][j] for i in range(n)) for j in range(n)]
    def has_pair(vs):
        for i in range(n):
            for j in range(i+1,n):
                if all(vs[i][k]==vs[j][k] for k in range(n)): return True
                if all(vs[i][k]==-vs[j][k] for k in range(n)): return True
        return False
    return has_pair(rows) or has_pair(cols)

def binary_good(A):
    m=len(A)
    if m==0: return True
    rows=[tuple(r) for r in A]
    cols=[tuple(A[i][j] for i in range(m)) for j in range(m)]
    zero=(0,)*m
    return zero not in rows and zero not in cols and len(set(rows))==m and len(set(cols))==m

def s1(n,k):
    # signed Stirling number of first kind: x^(underline n)=sum s1(n,k)x^k
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j]=dp[i-1][j-1]-(i-1)*dp[i-1][j]
    return dp[n][k]

def A094000(m):
    # OEIS A094000 formula: nonzero/distinct rows AND columns, modulo row perms.
    return sum(s1(m+1,k)*comb(2**(k-1)-1,m) for k in range(1,m+2))

def p_trivial_complement_binary(n):
    m=n-1
    return Fraction(factorial(m)*A094000(m),2**(m*m))

def p_trivial_complement_graph(n):
    # Direct signed-graph inclusion-exclusion formula.
    tot=0
    for c in range(1,n+1):
        for d in range(1,n+1):
            tot += s1(n,c)*s1(n,d)*2**(2*n-c-d+c*d)
    return Fraction(tot,2**(n*n))

# Exhaustive normalization/collision self-check through n=4.
for n in range(1,5):
    good=0
    singular_good=0
    for flat in product((-1,1), repeat=n*n):
        B=[flat[i*n:(i+1)*n] for i in range(n)]
        N,A=normalize_sign(B)
        assert all(x==1 for x in N[0])
        assert all(N[i][0]==1 for i in range(n))
        assert (not signed_pair_collision(B)) == binary_good(A)
        dB=det_bareiss(B)
        dA=det_bareiss(A)
        assert (dB==0)==(dA==0)
        if not signed_pair_collision(B):
            good += 1
            singular_good += (dB==0)
    pgood=Fraction(good,2**(n*n))
    assert pgood==p_trivial_complement_binary(n)==p_trivial_complement_graph(n)
    print("exhaustive-sign",n,"collision_free",good,"singular_collision_free",singular_good,
          "Pgood",pgood,"PASS")

for n in range(2,13):
    a=p_trivial_complement_binary(n)
    b=p_trivial_complement_graph(n)
    assert a==b
    print("trivial-formula-agree",n,a,"PASS")

# Current external exact source data, OEIS as of 2026-09-16.
# A000410: singular m x m rational 0/1 matrices with nonzero distinct rows,
# modulo row permutations (offset 1).
A000410={
1:0,2:0,3:6,4:425,5:65625,6:27894671,7:35716401889,
8:144866174953833,9:1923407307449265675,
}
# A000409: same row-good singular class, but with a zero/equal column.
A000409={
2:0,3:6,4:350,5:43260,6:14591171,7:14657461469,
8:46173502811223,9:474928141312623525,
}
# A116527: singular matrices with nonzero pairwise-distinct rows AND columns,
# modulo row permutations. The n=9 term was added in July 2026.
A116527={
1:0,2:0,3:0,4:75,5:22365,6:13303500,7:21058940420,
8:98692672142610,9:1448479166136642150,
}
for m in range(2,10):
    assert A116527[m]==A000410[m]-A000409[m]
    print("source-identity",m,A116527[m],"PASS")

# A094000 source table check through m=9.
A094_source={
0:1,1:1,2:3,3:29,4:1015,5:126651,6:53354350,
7:74698954306,8:350688201987402,9:5624061753186933530,
}
for m,v in A094_source.items():
    assert A094000(m)==v
print("A094000-formula-source-table m=0..9 PASS")

# Source-backed normalized residual r(n) through n=10.
# Strict metric promotion:
#   n<=9: published order<=8 Zivkovic classification / prior R03 exact state.
#   n=10: July-2026 OEIS extension only; arithmetic is checked here, but the
#         external enumeration is not independently certified in this script.
print("exact-normalized-nontrivial-remainder")
R={}
for n in range(1,11):
    m=n-1
    if m==0:
        r=Fraction(0)
    else:
        r=Fraction(2**n*factorial(m)*A116527[m],2**(m*m))
    R[n]=r
    print("r",n,r,float(r))

expected_r10=Fraction(2053219217998690247625,9223372036854775808)
assert R[10]==expected_r10
print("r10_source_backed_only",R[10],float(R[10]),"ARITHMETIC_PASS_NOT_METRIC_PROMOTION")

# n=10 cross-check with total singular count A046747(9).
m=9;n=10
A046747_9=902616230040448613437952
p_total=Fraction(A046747_9,2**81)
p_good=p_trivial_complement_binary(n)
p_trivial=1-p_good
p_res=Fraction(factorial(9)*A116527[9],2**81)
assert p_total==p_trivial+p_res
print("n10_Ptrivial",p_trivial,float(p_trivial))
print("n10_Presidual",p_res,float(p_res))
print("n10_Ptotal",p_total,float(p_total))
print("n10_scaled_trivial",2**10*p_trivial,float(2**10*p_trivial))
print("n10_scaled_residual",2**10*p_res,float(2**10*p_res))
print("n10_scaled_total",2**10*p_total,float(2**10*p_total))
print("n10_total-decomposition PASS")

# Asymmetric row-good-only upper envelope and finite gluing-loss ratios.
print("row-only-relaxation")
for m in range(4,10):
    n=m+1
    rrow=Fraction(2**n*factorial(m)*A000410[m],2**(m*m))
    rex=R[n]
    print("n",n,"exact",rex,float(rex),"row_only",rrow,float(rrow),
          "exact_over_row",float(rex/rrow))
    assert rex<=rrow

# Concrete obstruction to multiplying row-good and col-good inside singular class.
# m=4 total singular labeled = A046747(4)=42976.
# row-good singular = 4!*A000410(4); by transpose col-good is same.
# both-good singular = 4!*A116527(4).
S=42976
Rg=factorial(4)*A000410[4]
Cg=Rg
Both=factorial(4)*A116527[4]
assert Both*S != Rg*Cg
print("conditional-independence-obstruction-m4",
      "S",S,"Rgood",Rg,"Cgood",Cg,"both",Both,
      "both*S",Both*S,"Rgood*Cgood",Rg*Cg,"PASS")

# Retained C243 F3 fallback, now subtracting exact trivial collision mass.
def stirling2(n,k):
    if n==k==0: return 1
    if n==0 or k==0: return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def partition_subspaces(m,k):
    return sum(comb(m,r)*stirling2(r,k) for r in range(k,m+1))

def falling_distinct_nonzero(k):
    x=1
    for j in range(k):
        x*=2**k-1-j
    return x

SING_REAL={
1:1,2:10,3:338,4:42976,5:21040112,6:39882864736,
7:292604283435872,8:8286284310367538176,
}
INV_REAL={k:2**(k*k)-v for k,v in SING_REAL.items()}
def ordered_basis_upper(k):
    d=falling_distinct_nonzero(k)
    return min(d,INV_REAL[k]) if k in INV_REAL else d

def f3_lower(m):
    if m==0: return Fraction(1)
    L=Fraction(2**m-1,2**m)
    for k in range(1,m):
        U=min(Fraction(1),Fraction(partition_subspaces(m,k)*ordered_basis_upper(k),2**(m*k)))
        q=Fraction(2**k,2**m)
        L=(1-Fraction(3,4)*q)*L-Fraction(1,4)*q*U
        assert L>=0
    return L


def falling(a,r):
    x=1
    for j in range(r):
        x*=a-j
    return x

def hyperplane_cube_numer(p,q):
    # 3*P(sum a_i U_i=0) * 2^(p+q) = 2^s + 2 cos((p-q)pi/3).
    # Return exact zero-subset count Z(p,q).
    s=p+q
    d=(p-q)%6
    # 2*cos(d*pi/3) is in {2,1,-1,-2,-1,1}.
    two_cos=(2,1,-1,-2,-1,1)[d]
    return (2**s + two_cos)//3

# Exact analytic-tier self-check by projective coefficient types.
# Fat: support 1, or support 2 with opposite coefficients -> density 1/2.
# Max nonfat: support 3 with a 2+1 sign split, or support 4 balanced -> 3/8.
# Every remaining nonfat hyperplane has density <= 11/32.
for mtest in range(2,13):
    high=0
    fat=0
    other_max=Fraction(0)
    for s in range(1,mtest+1):
        # projective sign patterns: identify (p,q) with (q,p), but count below
        for pplus in range(s+1):
            qminus=s-pplus
            z=hyperplane_cube_numer(pplus,qminus)
            density=Fraction(z,2**s)
            # count projective coefficient patterns of this p/q type on a fixed support
            if pplus==qminus:
                patterns=comb(s,pplus)//2
            elif pplus>qminus:
                patterns=comb(s,pplus)
            else:
                continue
            if s==1:
                assert density==Fraction(1,2)
                fat += comb(mtest,s)*patterns
            elif s==2 and pplus==qminus==1:
                assert density==Fraction(1,2)
                fat += comb(mtest,s)*patterns
            elif density==Fraction(3,8):
                assert (s==3 and sorted((pplus,qminus))==[1,2]) or (s==4 and pplus==qminus==2)
                high += comb(mtest,s)*patterns
            else:
                other_max=max(other_max,density)
    assert fat==mtest+comb(mtest,2)
    assert high==3*comb(mtest,3)+3*comb(mtest,4)
    assert other_max<=Fraction(11,32)
    print("F3-hyperplane-tier",mtest,"fat",fat,"high",high,
          "other_max",other_max,"PASS")

def f3_lower_refined_final(m):
    """Retained C243 through rank m-1, then exact hyperplane-density tiers."""
    if m==0:
        return Fraction(1,1)
    if m==1:
        return Fraction(1,2)
    L=Fraction(2**m-1,2**m)
    # Reach I_{m-1}, stopping before final hyperplane hit.
    for k in range(1,m-1):
        N=partition_subspaces(m,k)
        A=ordered_basis_upper(k)
        U=min(Fraction(1,1),Fraction(N*A,2**(m*k)))
        q=Fraction(2**k,2**m)
        L=(1-Fraction(3,4)*q)*L-Fraction(1,4)*q*U
        assert L>=0

    k=m-1
    # Fat partition hyperplanes: hit density 1/2.
    Nfat=partition_subspaces(m,k)
    Afat=ordered_basis_upper(k)
    Ufat=min(Fraction(1,1),Fraction(Nfat*Afat,2**(m*k)))

    # High nonfat hyperplanes: hit density exactly 3/8.
    Nhigh=3*comb(m,3)+3*comb(m,4)
    h=3*2**(m-3) if m>=3 else 0
    Ahigh=falling(h-1,k) if h-1>=k else 0
    Uhigh=min(Fraction(1,1),Fraction(Nhigh*Ahigh,2**(m*k)))

    # Ordinary nonfat <= 11/32.  Relative corrections:
    # high 12/32: +1/32 hit; fat 16/32: +5/32 hit.
    Lfinal=Fraction(21,32)*L-Fraction(1,32)*Uhigh-Fraction(5,32)*Ufat
    assert Lfinal>=0
    return Lfinal,L,Ufat,Uhigh

print("refined-F3-final-step")
for mm in range(5,16):
    Lnew,Lpre,Ufat,Uhigh=f3_lower_refined_final(mm)
    Lold=f3_lower(mm)
    if mm>=6: assert Lnew>=Lold
    print("refined-F3",mm,"L",Lnew,float(Lnew),
          "old",float(Lold),"gain",float(Lnew-Lold),
          "Ufat",float(Ufat),"Uhigh",float(Uhigh),"PASS")

print("strict-rigorous-envelope")
strict={}
for n in range(1,21):
    if n<=9:
        val=R[n]
        tag="exact-published-through-binary-order8"
    else:
        L=f3_lower_refined_final(n-1)[0]
        pgood=p_trivial_complement_binary(n)
        val=max(Fraction(0),2**n*(pgood-L))
        tag="refined-F3-upper"
    strict[n]=val
    print("strict-envelope",n,tag,val,float(val))

expected_f3_r10=Fraction(4039481031913758122055,9223372036854775808)
assert strict[10]==expected_f3_r10
assert R[10] < strict[10]
old_f3_r10=Fraction(4147725689935874803575,9223372036854775808)
assert strict[10] < old_f3_r10
print("strict-r10-refined-F3",strict[10],float(strict[10]),"PASS")
print("prior-r10-C243-F3",old_f3_r10,float(old_f3_r10))
print("r10-improvement",old_f3_r10-strict[10],float(old_f3_r10-strict[10]))
print("source-backed-r10-candidate",R[10],float(R[10]),"NOT_PROMOTED")
print("SELF-CHECK PASS")

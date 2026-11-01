from itertools import product
from fractions import Fraction

LETTERS = {'A':(0,1),'B':(1,0),'C':(0,0),'D':(1,1)}

def step(state, z, m):
    x,g=state; u,v=LETTERS[z]
    d=[0]*(m+1)
    for i in range(1,m+1):
        d[i]=(1-g[i-1])*int(bool(d[i-1] or (x[i-1]==v)))
    xp=x[1:]+(u,)
    gp=tuple([g[i+1]+d[i+2]-d[i+1] for i in range(m-1)] + [(1-d[m])*int(u==v)])
    assert all(t in (0,1) for t in gp)
    return xp,gp

def formal(m):
    return [(bits[:m],bits[m:]) for bits in product((0,1),repeat=2*m)]

def apply(s, word, m):
    for ch in word:
        s=step(s,ch,m)
    return s

def expected_output(m,r,z):
    zero=(0,)*m
    if z in 'AC' or r==0:
        return zero,zero
    e=[0]*m; e[r-1]=1; e=tuple(e)
    if z=='B' and r==m:
        return e,zero
    return e,e

def exhaustive_family(max_m=6):
    total=0
    for m in range(1,max_m+1):
        fs=formal(m)
        for r in range(m+1):
            for z in 'ABCD':
                w='A'*r+z+'A'*(m-r)
                out0=apply(fs[0],w,m)
                assert out0==expected_output(m,r,z),(m,r,z,out0,expected_output(m,r,z))
                for s in fs[1:]:
                    assert apply(s,w,m)==out0,(m,r,z,s,apply(s,w,m),out0)
                total += 1
        # Complement family around B, by direct check too.
        for r in range(m+1):
            for z in 'ABCD':
                w='B'*r+z+'B'*(m-r)
                out0=apply(fs[0],w,m)
                for s in fs[1:]:
                    assert apply(s,w,m)==out0,(m,r,z,w,s,apply(s,w,m),out0)
                total += 1
        print(f'ONE_DEFECT_FAMILY_m={m}_formal_states={len(fs)}_words_checked={8*(m+1)}_PASS')
    print('TOTAL_FAMILY_WORDS_CHECKED=',total)

def old_constant(m):
    return Fraction(8*4**m+10,21)

def paired_gap_bound(m):
    # p=P(A)=1/4, q=3/4. Group inter-non-A gaps in disjoint pairs.
    return Fraction(32*4**m, 3*(3*m+4))

def overlap_gap_exact(m):
    p=Fraction(1,4); q=Fraction(3,4)
    # E_a = 1/q + q * sum_{b=0}^{m-a-1} p^b E_b, 0<=a<m.
    A=[[Fraction(int(i==j)) for j in range(m)] for i in range(m)]
    rhs=[1/q for _ in range(m)]
    for a in range(m):
        for b in range(m-a):
            A[a][b] -= q*(p**b)
    for col in range(m):
        pivot=next(r for r in range(col,m) if A[r][col])
        if pivot!=col:
            A[col],A[pivot]=A[pivot],A[col]
            rhs[col],rhs[pivot]=rhs[pivot],rhs[col]
        pv=A[col][col]
        A[col]=[x/pv for x in A[col]]
        rhs[col]/=pv
        for r in range(m):
            if r==col: continue
            f=A[r][col]
            if f:
                A[r]=[A[r][c]-f*A[col][c] for c in range(m)]
                rhs[r]-=f*rhs[col]
    E=rhs
    # Exact residual verification.
    for a in range(m):
        rr=1/q
        for b in range(m-a):
            rr += q*(p**b)*E[b]
        assert E[a]==rr
    return E[0],E

exhaustive_family(6)
for m in range(2,13,2):
    ex,_=overlap_gap_exact(m)
    pair=paired_gap_bound(m)
    old=old_constant(m)
    print(f'm={m} w={m//2}')
    print('OLD=',old)
    print('PAIR_BOUND=',pair)
    print('OVERLAP_EXACT=',ex)
    print('OVERLAP_DECIMAL=',format(float(ex),'.15f'))
    print('OVERLAP_LT_OLD=',ex<old)
    if ex<old:
        print('IMPROVEMENT=',old-ex)
        print('RATIO=',ex/old)
    print('OVERLAP_LE_PAIR=',ex<=pair)

m=12
ex,_=overlap_gap_exact(m)
old=old_constant(m)
assert ex < old
assert ex < Fraction(2556528,1)
print('WIDTH6_CERTIFIED_ERROR_LT_2556528=',ex < 2556528)
print('WIDTH6_OLD=',old)
print('WIDTH6_NEW_EXACT=',ex)
print('WIDTH6_NEW_LT_INTEGER=2556528')
print('WIDTH6_EXACT_IMPROVEMENT=',old-ex)
print('ALL_EXACT_CHECKS_PASS')

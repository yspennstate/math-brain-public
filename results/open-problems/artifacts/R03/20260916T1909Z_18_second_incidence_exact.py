from itertools import combinations
from fractions import Fraction
from math import comb, ceil, log2
import time


def fall(a,m):
    if a < m:
        return 0
    z=1
    for j in range(m): z*=a-j
    return z


def canon_line(v,p):
    v=tuple(x%p for x in v)
    for x in v:
        if x:
            inv=pow(x,-1,p)
            return tuple((y*inv)%p for y in v)
    raise ValueError


def rref2(a,b,p):
    A=[list(a),list(b)]
    m=len(a);r=0
    for c in range(m):
        piv=None
        for i in range(r,2):
            if A[i][c]%p:
                piv=i;break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(2):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(m)]
        r+=1
        if r==2:break
    return tuple(tuple(row) for row in A[:r])


def line_mask(v,p,m):
    mask=0
    for bits in range(1<<m):
        s=0
        for i,a in enumerate(v):
            if (bits>>i)&1: s+=a
        if s%p==0: mask |= 1<<bits
    return mask


def high_lines(m,p):
    lines={}
    for S in combinations(range(m),3):
        for target in S:
            v=[0]*m
            for i in S: v[i]=1
            v[target]=-1
            c=canon_line(v,p)
            lines[c]=None
    for S in combinations(range(m),4):
        seen=set()
        for plus_t in combinations(S,2):
            plus=set(plus_t);v=[0]*m
            for i in S: v[i]=1 if i in plus else -1
            c=canon_line(v,p)
            seen.add(c)
        for c in seen: lines[c]=None
    return list(lines)


def bad_masks(m):
    out=[]
    for i in range(m):
        mask=0
        for bits in range(1<<m):
            if ((bits>>i)&1)==0: mask|=1<<bits
        out.append(mask)
    for i in range(m):
        for j in range(i+1,m):
            mask=0
            for bits in range(1<<m):
                if ((bits>>i)&1)==((bits>>j)&1):mask|=1<<bits
            out.append(mask)
    return out


def lower_M2(m,p):
    lines=high_lines(m,p)
    lmasks={v:line_mask(v,p,m) for v in lines}
    Vmask={}
    for a,b in combinations(lines,2):
        V=rref2(a,b,p)
        assert len(V)==2
        if V not in Vmask:
            Vmask[V]=lmasks[a]&lmasks[b]
    bm=bad_masks(m)
    total_lb=0
    hdist={}
    for mask in Vmask.values():
        h=mask.bit_count()
        hdist[h]=hdist.get(h,0)+1
        q=h-1
        total=fall(q,m)
        bad=0
        for B in bm:
            t=(mask&B).bit_count()-1
            bad += fall(t,m)
        g=total-bad
        if g>0: total_lb += g
    return len(lines),len(Vmask),hdist,total_lb


def qb(n,k,p):
    if k<0 or k>n:return 0
    num=den=1
    for i in range(k):
        num*=p**(n-i)-1
        den*=p**(k-i)-1
    return num//den


def cstar(p,dmax):
    return Fraction(p*(p*p-1),p**dmax-1)

cases=[
    (9,7,651685823418402269683200),
    (10,11,325043331888785398807391827200),
]

for m,p,M1 in cases:
    t=time.time()
    L,V,hdist,M2lb=lower_M2(m,p)
    dmax=m-ceil(log2(m+1))
    c=cstar(p,dmax)
    for d in range(dmax+1):
        z1=qb(d,1,p)
        z2=qb(d,2,p)
        lhs=(1 if d>=1 else 0)
        assert Fraction(z1,1)-c*z2 >= lhs
    scale=Fraction(2**(m+1),2**(m*m))
    old=scale*M1
    new=scale*(Fraction(M1,1)-c*M2lb)
    print(f'm={m} p={p}')
    print('high_lines',L)
    print('unique_2spaces',V)
    print('intersection_h_distribution',sorted(hdist.items()))
    print('M2_lower',M2lb)
    print('dmax',dmax,'cstar',c)
    print('old_r',old,float(old))
    print('new_r',new,float(new))
    print('improvement',old-new,float(old-new))
    print('elapsed_sec',round(time.time()-t,3))


def G_disjoint(m):
    u=m-6
    assert u>=1
    return (fall(9*(2**u)-1,m)
            -8*fall(6*(2**u)-1,m)
            -4*fall(3*(2**u)-1,m)
            -5*fall(5*(2**u)-1,m)
            -4*fall(4*(2**u)-1,m)
            -(7*u+comb(u,2))*fall(9*(2**(u-1))-1,m))
assert G_disjoint(9)==22039379834572800
assert (comb(9,3)*comb(6,3)//2)*9==7560
print('disjoint_triple_closed_form_PASS')
print('SELF-CHECK PASS')

from math import gcd
from fractions import Fraction


def matmul(A,B):
    n=len(A); m=len(B); p=len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def transpose(A): return [list(row) for row in zip(*A)]

def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def matsub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def rank_q(A):
    M=[[Fraction(x) for x in row] for row in A]
    m=len(M); n=len(M[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if M[i][c]), None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        q=M[r][c]
        M[r]=[x/q for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                q=M[i][c]
                M[i]=[M[i][j]-q*M[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def circulant(seq):
    v=len(seq)
    return [[seq[(j-i)%v] for j in range(v)] for i in range(v)]

def paf(a,t):
    v=len(a)
    return sum(a[i]*a[(i+t)%v] for i in range(v))

def shift_matrix(v,t):
    return [[1 if j==(i+t)%v else 0 for j in range(v)] for i in range(v)]

def scale(c,A): return [[c*x for x in row] for row in A]

def build_tcc(a,b):
    a=[-x for x in a]; b=[-x for x in b]
    v=len(a); A=circulant(a); B=circulant(b)
    H=[]
    H.append([1,1]+[1]*v+[1]*v)
    H.append([1,-1]+[1]*v+[-1]*v)
    for i in range(v): H.append([1,1]+A[i]+B[i])
    BT=transpose(B); AT=transpose(A)
    for i in range(v): H.append([1,-1]+BT[i]+[-x for x in AT[i]])
    return H

def support_to_seq(v,S):
    S=set(S)
    return [1 if i in S else -1 for i in range(v)]

def defect(a,b):
    v=len(a)
    return [0]+[paf(a,t)+paf(b,t)+2 for t in range(1,v)]

def verify_v19():
    v=19; N=40
    A0={0,1,2,3,4,5,8,10,14,16}
    B0={0,1,2,3,5,9,10,12,15,16}
    a=support_to_seq(v,A0); b=support_to_seq(v,B0)
    d=defect(a,b)
    assert d[6]==d[13]==4 and d[8]==d[11]==-4
    assert all(d[t]==0 for t in range(1,v) if t not in {6,13,8,11})
    D=[[d[(j-i)%v] for j in range(v)] for i in range(v)]
    r,s=6,8
    inv2=pow(2,-1,v)
    aa=((r+s)*inv2)%v; bb=((r-s)*inv2)%v
    Paa=shift_matrix(v,aa); Pmaa=shift_matrix(v,-aa%v)
    Pbb=shift_matrix(v,bb); Pmbb=shift_matrix(v,-bb%v)
    fact=scale(4,matmul(matsub(Paa,Pmaa),matsub(Pbb,Pmbb)))
    assert D==fact
    z=gcd(v,r-s)+gcd(v,r+s)-gcd(v,r-s,r+s)
    assert z==1
    assert rank_q(D)==v-z==18
    H=build_tcc(a,b)
    G=matsub(matmul(H,transpose(H)), scale(N,eye(N)))
    target=[[0]*N for _ in range(N)]
    for i in range(v):
        for j in range(v):
            target[2+i][2+j]=D[i][j]
            target[2+v+i][2+v+j]=D[i][j]
    assert G==target
    assert rank_q(G)==36
    for c in range(4,N,4):
        lower=v-(c-2)/2
        upper_trace=16*v/(c+16)
        upper_sq=64*v/(c*c)
        assert lower>min(upper_trace,upper_sq), (c,lower,upper_trace,upper_sq)
    print('v19 exact Gram/factor/rank/border checks passed')

def verify_symbolic_border_range():
    for v in range(11,202,2):
        N=2*v+2
        f8=8*8+(14-2*v)*8-32
        assert f8<0
        g12=12**2*(2*v-10)
        gtop=(2*v-2)**2*4
        assert g12>128*v and gtop>128*v
        for c in range(4,N,4):
            low=v-(c-2)/2
            tr=16*v/(c+16)
            sq=64*v/(c*c)
            assert not (low<=tr and low<=sq), (v,c,low,tr,sq)
    print('principal-border theorem inequalities checked for odd 11<=v<=201')

def verify_rank_formula_small():
    for v in range(5,22,2):
        reps=range(1,(v+1)//2)
        for r in reps:
            for s in reps:
                if r==s: continue
                d=[0]*v
                for t,val in ((r,4),((-r)%v,4),(s,-4),((-s)%v,-4)):
                    d[t]+=val
                D=[[d[(j-i)%v] for j in range(v)] for i in range(v)]
                z=gcd(v,r-s)+gcd(v,r+s)-gcd(v,r-s,r+s)
                assert rank_q(D)==v-z,(v,r,s,rank_q(D),v-z)
    print('rank formula checked exactly for all defect pairs at odd v<=21')

if __name__=='__main__':
    verify_v19()
    verify_symbolic_border_range()
    verify_rank_formula_small()
    print('ALL EXACT CHECKS PASSED')

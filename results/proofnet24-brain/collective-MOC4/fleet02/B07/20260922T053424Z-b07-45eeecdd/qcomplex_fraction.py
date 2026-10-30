from fractions import Fraction as F
Z=(F(0),F(0)); O=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def div(x,y):
    d=y[0]*y[0]+y[1]*y[1]
    return ((x[0]*y[0]+x[1]*y[1])/d,(x[1]*y[0]-x[0]*y[1])/d)
def sumz(xs):
    s=Z
    for x in xs: s=add(s,x)
    return s
def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def madd(A,B): return [[add(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B): return [[sub(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mmul(A,B):
    return [[sumz(mul(A[i][r],B[r][j]) for r in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mstar(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def minv(A):
    n=len(A); I=eye(n); M=[A[i][:]+I[i][:] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=Z)
        if p!=c: M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[div(x,q) for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q!=Z: M[r]=[sub(M[r][j],mul(q,M[c][j])) for j in range(2*n)]
    return [r[n:] for r in M]
def det(A):
    n=len(A); M=[r[:] for r in A]; out=O; sgn=1
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=Z),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; sgn=-sgn
        q=M[c][c]; out=mul(out,q)
        for r in range(c+1,n):
            if M[r][c]!=Z:
                t=div(M[r][c],q)
                for j in range(c,n): M[r][j]=sub(M[r][j],mul(t,M[c][j]))
    return neg(out) if sgn<0 else out
def diag(v): return [[v[i] if i==j else Z for j in range(len(v))] for i in range(len(v))]

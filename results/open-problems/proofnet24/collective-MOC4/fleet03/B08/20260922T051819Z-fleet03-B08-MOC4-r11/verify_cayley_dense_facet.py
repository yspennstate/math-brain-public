from fractions import Fraction as F
from itertools import permutations

class Q:
    __slots__=("r","i")
    def __init__(self,r=0,i=0): self.r=F(r); self.i=F(i)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o); return Q(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,o): return self+(-(o if isinstance(o,Q) else Q(o)))
    def __rsub__(self,o): return Q(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q) else Q(o); return Q(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q) else Q(o); n=o.r*o.r+o.i*o.i
        return self*Q(o.r/n,-o.i/n)
    def __eq__(self,o):
        o=o if isinstance(o,Q) else Q(o); return self.r==o.r and self.i==o.i
    def conj(self): return Q(self.r,-self.i)
    def n2(self): return self.r*self.r+self.i*self.i
    def __repr__(self): return f"({self.r})+({self.i})i"

Z=Q(); O=Q(1)
def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z) for j in range(len(B[0]))] for i in range(len(A))]
def adj(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def diag(v): return [[v[i] if i==j else Z for j in range(len(v))] for i in range(len(v))]
def inv(A):
    n=len(A); E=eye(n); M=[A[i][:]+E[i][:] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=Z)
        if p!=c: M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            f=M[r][c]
            if f!=Z: M[r]=[M[r][j]-f*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]
def det(A):
    n=len(A); M=[r[:] for r in A]; out=O; s=1
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=Z),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; s=-s
        q=M[c][c]; out=out*q
        for r in range(c+1,n):
            f=M[r][c]/q
            for j in range(c,n): M[r][j]=M[r][j]-f*M[c][j]
    return out*s
def prod(xs):
    z=O
    for x in xs: z=z*x
    return z

x=[F(483,50),F(-63,25),F(-72,25),F(-163,50),
   F(33,50),F(23,5),F(-139,25),F(9,25),
   F(-187,50),F(6,5),F(147,50),F(3,10),
   F(31,10),F(-14,25),F(1,50),F(-7,2)]
K=[[Z for _ in range(4)] for _ in range(4)]
for i in range(4): K[i][i]=Q(0,x[i])
t=4
for i in range(4):
    for j in range(i+1,4):
        z=Q(x[t],x[t+1]); t+=2
        K[i][j]=z; K[j][i]=-z.conj()
I=eye(4)
U=mul(inv(add(I,K)),sub(I,K))
assert mul(U,adj(U))==I
assert all(z!=Z for row in U for z in row)
pmin=min(z.n2() for row in U for z in row)
assert pmin>F(99,10000)

a=[Q(18,-17),Q(-20,2),Q(15,-22),Q(-21,2)]
b=[Q(-19,4),Q(25,-5),Q(18,-1),Q(-18,1)]
C=mul(mul(U,diag(b)),adj(U))
D=det(add(diag(a),C))
q=Q(-5782,-19099)
L=lambda z:(q*z).r

ps=list(permutations(range(4)))
v=[prod([a[i]+b[p[i]] for i in range(4)]) for p in ps]
H=[L(z) for z in v]
M=max(H); m=min(H); Fdet=L(D); gap=M-Fdet; width=M-m
assert M==F(-61633500) and ps[H.index(M)]==(0,1,2,3)
assert m==F(-59822291610)
assert gap>0

den=132146163883293812874
lam=[F(1697634460488463499,den),
     F(22235572512143239175,den),
     F(108212956910662110200,den)]
assert sum(lam)==1 and all(z>=0 for z in lam)
assert v[0]*lam[0]+v[1]*lam[1]+v[3]*lam[2]==D

def Aaxis(r,s,nx,ny,nz):
    A=diag(a); av,bv=a[r],a[s]; mm=(av+bv)/2; dd=(av-bv)/2
    A[r][r]=mm+dd*nz; A[s][s]=mm-dd*nz
    A[r][s]=dd*Q(nx,-ny); A[s][r]=dd*Q(nx,ny)
    return A
def h(r,s,n): return L(det(add(Aaxis(r,s,*n),C)))
def coeff(r,s):
    hz,hmz=h(r,s,(0,0,1)),h(r,s,(0,0,-1))
    hpx,hmx=h(r,s,(1,0,0)),h(r,s,(-1,0,0))
    hpy,hmy=h(r,s,(0,1,0)),h(r,s,(0,-1,0))
    return (hpx-hmx)/2,(hpy-hmy)/2,(hz-hmz)/2

pair=[]
for r in range(4):
    for s in range(r+1,4): pair.append(((r+1,s+1),)+coeff(r,s))
cx,cy,cz=next(row[1:] for row in pair if row[0]==(2,3))
T=width/F(100000)
assert cz>=0 and cx*cx+cy*cy > 2*cz*T+T*T
assert cx*cx+cy*cy < 2*cz*gap+gap*gap

print("PASS MOC4-CAYLEY-DENSE-FACET-v2")
print("unitary_exact=True")
print("all_16_entries_nonzero=True")
print("pmin_sq=",pmin)
print("D=",D)
print("support_max=",M,"support_min=",m,"max_perm=",tuple(i+1 for i in ps[H.index(M)]))
print("support_gap=",gap)
print("normalized_gap=",gap/width,"~",float(gap/width))
print("caratheodory_vertices=1234,1243,1342")
print("caratheodory_weights=",lam)
print("pair23_support_improvement_gt_width/100000=True")
print("pair23_optimum_still_below_M=True")

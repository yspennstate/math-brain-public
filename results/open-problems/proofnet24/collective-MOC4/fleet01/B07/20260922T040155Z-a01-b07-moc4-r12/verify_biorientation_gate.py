from fractions import Fraction as F

PAIRS=[(0,1),(0,2),(0,3)]
ALL4=set(range(4))
H=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]

def zadd(z,w): return (z[0]+w[0],z[1]+w[1])
def zsub(z,w): return (z[0]-w[0],z[1]-w[1])
def zmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def zprod(xs):
    z=(F(1),F(0))
    for x in xs: z=zmul(z,x)
    return z
def re(z): return z[0]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def givens(n,i,j,c,s):
    G=eye(n); G[i][i]=c; G[j][j]=c; G[i][j]=s; G[j][i]=-s; return G

def structured_K_X(a,b):
    W=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        ac=zprod([a[k] for k in range(4) if k!=i])
        for j in range(4):
            bc=zprod([b[k] for k in range(4) if k!=j])
            W[i][j]=re(zadd(zmul(ac,b[j]),zmul(a[i],bc)))
    Y=[[F(0) for _ in range(3)] for _ in range(3)]
    X=[[F(0) for _ in range(3)] for _ in range(3)]
    for aa,S in enumerate(PAIRS):
        Sc=tuple(sorted(ALL4-set(S)))
        Amin=zsub(zprod([a[k] for k in Sc]),zprod([a[k] for k in S]))
        Apl=zadd(zprod([a[k] for k in Sc]),zprod([a[k] for k in S]))
        for bb,T in enumerate(PAIRS):
            Tc=tuple(sorted(ALL4-set(T)))
            Bmin=zsub(zprod([b[k] for k in T]),zprod([b[k] for k in Tc]))
            Bpl=zadd(zprod([b[k] for k in T]),zprod([b[k] for k in Tc]))
            Y[aa][bb]=re(zmul(Amin,Bmin)); X[aa][bb]=re(zmul(Apl,Bpl))
    C=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            corr=sum(F(H[aa+1][i]*H[bb+1][j],8)*Y[aa][bb] for aa in range(3) for bb in range(3))
            C[i][j]=W[i][j]+corr
    K=[[sum(F(H[r+1][i]*H[c+1][j],4)*C[i][j] for i in range(4) for j in range(4)) for c in range(3)] for r in range(3)]
    return K,X

# Exact source-valid generic datum from the earlier parity-slack refutation.
U0=[
 [F(492,625),F(-31,625),F(-48,125),F(12,25)],
 [F(-9,25),F(12,25),F(-4,5),F(0)],
 [F(-36,125),F(48,125),F(9,25),F(4,5)],
 [F(-256,625),F(-492,625),F(-36,125),F(9,25)]]
t=F(1,5000); c=(1-t*t)/(1+t*t); s=2*t/(1+t*t)
U=mm(U0,givens(4,0,3,c,s))
a=[(F(-9,40),F(-39,20)),(F(-7,20),F(-37,40)),(F(-13,10),F(13,40)),(F(1,4),F(-7,10))]
b=[(F(-1,40),F(11,40)),(F(13,40),F(17,40)),(F(-23,40),F(-21,40)),(F(-59,40),F(33,40))]
K,X=structured_K_X(a,b)

def det2(rows,cols):
    i,k=rows; j,l=cols
    return U[i][j]*U[k][l]-U[i][l]*U[k][j]
R=[[F(0) for _ in range(3)] for _ in range(3)]
D=[[F(0) for _ in range(3)] for _ in range(3)]
for aa,S in enumerate(PAIRS):
    for bb,T in enumerate(PAIRS):
        Tc=tuple(sorted(ALL4-set(T)))
        qp=det2(S,T)**2; qm=det2(S,Tc)**2
        R[aa][bb]=qp+qm; D[aa][bb]=qp-qm

# Column complementary-pair planes beta=0 (12|34) and delta=2 (14|23).
beta,delta=0,2
Tpair=sum(K[a][beta]*D[a][beta]+K[a][delta]*D[a][delta]
          +F(1,2)*(X[a][beta]-X[a][delta])*(R[a][beta]-R[a][delta]) for a in range(3))
Cpair=sum(K[a][beta]*D[a][delta]+K[a][delta]*D[a][beta] for a in range(3))
slack=Tpair-abs(Cpair)

assert all(sum(U[i][k]*U[j][k] for k in range(4))==F(int(i==j)) for i in range(4) for j in range(4))
assert all(sum(R[i][j] for j in range(3))==1 for i in range(3))
assert all(sum(R[i][j] for i in range(3))==1 for j in range(3))
assert Cpair<0
assert slack==F(-370054743558932535893019,19531251562500031250000000)
assert slack<0
print('PASS MOC4-BIORIENTATION-PAIR-GATE-v1 exact negative-control application')
print('T_pair =',Tpair)
print('C_pair =',Cpair)
print('T_pair-|C_pair| =',slack)
print('orientation-reversing swap support improvement =',-slack)

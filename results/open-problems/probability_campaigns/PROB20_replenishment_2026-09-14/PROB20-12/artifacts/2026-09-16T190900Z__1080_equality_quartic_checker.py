from sympy import Matrix,Rational,simplify,factor,symbols,zeros,eye
from itertools import combinations

EDGES=list(combinations(range(6),2)); EIDX={e:i for i,e in enumerate(EDGES)}; PAIRS=EDGES; COLS=[(0,1),(2,3),(4,5)]
def coeffvec(nonzero):
    v=[0]*45
    for c,e,a in nonzero: v[15*c+EIDX[tuple(e)]]=a
    return v
V1080=coeffvec(
    [(0,e,1) for e in [(0,1),(4,5)]]+
    [(1,e,-1) for e in [(2,3),(2,4),(3,5)]]+
    [(2,e,-1) for e in [(0,2),(0,3),(1,2),(1,3),(2,3),(2,5),(3,4)]])
def probs(Q,complex_case=False):
    p=[]
    for a,b in COLS:
        for i,j in EDGES:
            z=simplify(Q[i,a]*Q[j,b]-Q[i,b]*Q[j,a])
            p.append(simplify(z*z))
    return p
def objective(p,v,k=0): return simplify(k+sum(Rational(a)*b for a,b in zip(v,p)))

Qeq=Matrix([
 [Rational(4,17),-Rational(10,17),-Rational(2,17),Rational(13,17),0,0],
 [Rational(2,17),-Rational(5,17),Rational(16,17),-Rational(2,17),0,0],
 [0,0,0,0,Rational(4,5),Rational(3,5)],
 [Rational(13,17),Rational(10,17),Rational(2,17),Rational(4,17),0,0],
 [0,0,0,0,Rational(3,5),-Rational(4,5)],
 [Rational(10,17),-Rational(8,17),-Rational(5,17),-Rational(10,17),0,0]])
assert simplify(Qeq.T*Qeq-eye(6))==zeros(6)
peq=probs(Qeq)
assert objective(peq,V1080,0)==0

BAS=[]
for a,b in PAIRS:
    M=zeros(6); M[a,b]=1; M[b,a]=-1; BAS.append(M)

def exact_grad_hess(Q,cv):
    d=[{e:Rational(cv[15*c+EIDX[e]]) for e in EDGES} for c in range(3)]
    dQ=[-2*Bi*Q for Bi in BAS]
    q2d=[2*Bi*Bi*Q for Bi in BAS]
    q2x={(i,j):2*(BAS[i]*BAS[j]+BAS[j]*BAS[i])*Q for i in range(15) for j in range(i+1,15)}
    grad=[Rational(0)]*15
    diag=[Rational(0)]*15
    cross={(i,j):Rational(0) for i in range(15) for j in range(i+1,15)}
    for c,(ca,cb) in enumerate(COLS):
        for e,coef in d[c].items():
            if not coef: continue
            r,s=e
            def det2(M1,a,M2,b): return M1[r,a]*M2[s,b]-M1[s,a]*M2[r,b]
            m0=det2(Q,ca,Q,cb)
            m1=[]
            for i in range(15):
                u=det2(dQ[i],ca,Q,cb)+det2(Q,ca,dQ[i],cb)
                m1.append(u); grad[i]+=coef*2*m0*u
            for i in range(15):
                u=det2(q2d[i],ca,Q,cb)+det2(Q,ca,q2d[i],cb)+det2(dQ[i],ca,dQ[i],cb)
                diag[i]+=coef*(m1[i]**2+2*m0*u)
            for i in range(15):
                for j in range(i+1,15):
                    q=q2x[(i,j)]
                    u=det2(q,ca,Q,cb)+det2(Q,ca,q,cb)+det2(dQ[i],ca,dQ[j],cb)+det2(dQ[j],ca,dQ[i],cb)
                    cross[(i,j)]+=coef*(2*m1[i]*m1[j]+2*m0*u)
    H=zeros(15)
    for i in range(15):
        H[i,i]=simplify(2*diag[i])
        for j in range(i+1,15):
            H[i,j]=H[j,i]=simplify(cross[(i,j)])
    return [simplify(x) for x in grad],H

grad,H=exact_grad_hess(Qeq,V1080)
assert all(g==0 for g in grad)
lam=symbols("lam")
hcp=factor(H.charpoly(lam).as_expr())
hexp=lam**9*(lam+8)**4*(289*lam+160)*(289*lam+1000)/83521
assert simplify(hcp-hexp)==0
assert H.rank()==6
print("EQUALITY_HESSIAN","rank",H.rank(),"charpoly",hcp)

N=H.nullspace()
assert len(N)==9
z=symbols("z0:9", real=True)
v=zeros(15,1)
for a,n in zip(z,N): v+=a*n
B=zeros(6)
for val,(i,j) in zip(v,PAIRS): B[i,j]=val; B[j,i]=-val
Qco=[Qeq]+[2*((-1)**n)*(B**n)*Qeq for n in range(1,5)]
def minor_series(r,s,ca,cb):
    out=[]
    for n in range(5):
        out.append(sum(Qco[k][r,ca]*Qco[n-k][s,cb]-Qco[k][s,ca]*Qco[n-k][r,cb] for k in range(n+1)))
    return out
coef=[Rational(0)]*5
for c,(ca,cb) in enumerate(COLS):
    for e in EDGES:
        a=V1080[15*c+EIDX[e]]
        if not a: continue
        m=minor_series(*e,ca,cb)
        for n in range(5):
            coef[n]+=a*sum(m[k]*m[n-k] for k in range(n+1))
coef=[simplify(x) for x in coef]
assert coef[:4]==[0,0,0,0]

m=Matrix([z[0]*z[3],z[1]*z[3],z[2]*z[3],z[3]*z[4],z[3]*z[5],
          z[3]*z[6],z[2]*z[7],z[5]*z[7],z[6]*z[7],z[7]*z[8]])
G=Matrix([
[100,-240,0,480,0,0,20,-40,0,0],
[-240,2232,200,-1574,-400,0,-48,96,0,578],
[0,200,80,-400,-160,0,0,0,0,0],
[480,-1574,-400,4593,800,0,96,-192,0,289],
[0,-400,-160,800,320,0,0,0,0,0],
[0,0,0,0,0,1345,0,0,0,0],
[20,-48,0,96,0,0,4,-8,0,0],
[-40,96,0,-192,0,0,-8,16,0,0],
[0,0,0,0,0,0,0,0,289,0],
[0,578,0,289,0,0,0,0,0,289]])
assert simplify(coef[4] + Rational(4,289)*(m.T*G*m)[0])==0
gcp=factor(G.charpoly(lam).as_expr())
gexp=lam**5*(lam-1734)*(lam-1345)*(lam-289)*(lam**2-5900*lam+1500000)
assert simplify(gcp-gexp)==0
assert G.rank()==5
assert 28810000 > 0 and 28810000 < 5900**2
print("NULLSPACE_QUARTIC","coef_t4 = -4/289 m^T G m","G_rank",G.rank(),"G_charpoly",gcp)
print("ALL EXACT CHECKS PASSED")

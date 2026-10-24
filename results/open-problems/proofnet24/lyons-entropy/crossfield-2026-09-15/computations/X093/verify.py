import sympy as sp
import mpmath as mp
import itertools,json,os
mp.mp.dps=160
N=sp.Matrix([[1,-1,-1,0],[0,1,-1,-1],[1,0,1,-1],[1,1,0,1]])
assert N.T*N==3*sp.eye(4)
P=N[:,:2]*N[:,:2].T/3
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
U=N[:,:2]*Y*N[:,:2].T/3
R=N[:,2:]*Y*N[:,2:].T/3
eta,eps,t,b,c=sp.symbols('eta eps t b c',real=True)
K=(1-eta)*P+eps*(sp.eye(4)-P)-eta*U/2+eps*R/2
perms=list(itertools.permutations(range(4)))
def det4(M):
    return sp.expand(sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*sp.prod(M[i,p[i]] for i in range(4)) for p in perms))
cs=[]; atoms=[]; d2=[]
for mask in range(16):
    k=mask.bit_count()
    MS=sp.Matrix.hstack(*[(K if mask>>i&1 else sp.eye(4)-K)[:,i] for i in range(4)])
    atom=det4(MS)
    fac=eta**(2-k) if k<2 else eps**(k-2) if k>2 else 1
    co=sp.cancel(atom/fac)
    assert not co.has(sp.zoo)
    assert sp.Poly(co,eta,eps)
    cs.append(co);atoms.append(atom)
    KP=P+t*(b*U+c*R)
    MP=sp.Matrix.hstack(*[(KP if mask>>i&1 else sp.eye(4)-KP)[:,i] for i in range(4)])
    d2.append(sp.expand(det4(MP)).coeff(t,2)*2)
R0=-sum(d2[i]*sp.log(cs[i].subs({eta:0,eps:0})) for i in range(16))
expected=2*sp.log(sp.Rational(3,4))*(b*b+c*c)-sp.Rational(8,9)*sp.log(2)*(b+c)**2
assert sp.expand_log(sp.expand(R0-expected),force=True).expand()==0
assert sum(d2)==0
expected_leads=[sp.Rational(x,y) for x,y in [(3,4),(2,3),(1,3),(1,9),(1,3),(1,9),(1,9),(1,3),(2,3),(4,9),(1,9),(2,3),(1,9),(2,3),(1,3),(3,4)]]
assert [z.subs({eta:0,eps:0}) for z in cs]==expected_leads
features=[sp.diag(1,0),sp.diag(0,1),sp.Matrix([[0,1],[1,0]]),Y]
for cols in [N[:,:2],N[:,2:]]:
    fmap=sp.Matrix([[(cols[i,:]*D.adjugate()*cols[i,:].T)[0]/3 for D in features] for i in range(4)])
    assert fmap.rank()==3
    assert fmap[:,3]==sp.zeros(4,1)
Hshape=sp.eye(2)+Y/2
assert sp.trace(Hshape.adjugate()*Y)**2/Hshape.det()==sp.Rational(4,3)
block=[];names=[]
for offset,label in [(0,'B'),(2,'C')]:
    for mat,name in [(sp.diag(1,0),'00'),(sp.diag(0,1),'11'),(sp.Matrix([[0,1],[1,0]]),'re'),(Y,'im')]:
        A=sp.zeros(4);A[offset:offset+2,offset:offset+2]=mat
        block.append(A);names.append(label+name)
for i in range(2):
    for j in range(2):
        for v,label in [(1,'re'),(sp.I,'im')]:
            A=sp.zeros(4);A[i,2+j]=v;A[2+j,i]=sp.conjugate(v)
            block.append(A);names.append('X'+str(i)+str(j)+label)
dirs=[N*A*N.T/3 for A in block]
def mm(M): return mp.matrix([[mp.mpc(str(sp.re(M[i,j])),str(sp.im(M[i,j]))) for j in range(M.cols)] for i in range(M.rows)])
Dm=[mm(A) for A in dirs]
Pf,Uf,Rf=map(mm,[P,U,R]);I=mp.eye(4)
results=[]
for es,fs in [('1e-4','1e-4'),('1e-8','1e-8'),('1e-8','1e-30'),('1e-30','1e-8'),('1e-5','1e-60'),('1e-60','1e-5')]:
    e,f=mp.mpf(es),mp.mpf(fs);L=-mp.log(e*f)
    KF=(1-e)*Pf+f*(I-Pf)-e*Uf/2+f*Rf/2
    Hess=mp.zeros(16);metric=mp.zeros(16)
    for mask in range(16):
        M=mp.matrix([[KF[i,j] if mask>>j&1 else I[i,j]-KF[i,j] for j in range(4)] for i in range(4)])
        p=mp.re(mp.det(M));assert p>0
        Minv=M**-1
        RR=[Minv*mp.matrix([[A[i,j]*(1 if mask>>j&1 else -1) for j in range(4)] for i in range(4)]) for A in Dm]
        tr=[sum(T[i,i] for i in range(4)) for T in RR]
        for a in range(16):
            for z in range(a,16):
                fisher=mp.re(p*tr[a]*tr[z])
                acc=mp.re(p*(tr[a]*tr[z]-sum(RR[a][i,j]*RR[z][j,i] for i in range(4) for j in range(4))))
                Hess[a,z]+=-fisher-acc*mp.log(p)
                if mask.bit_count() in (1,3):metric[a,z]+=fisher
    for i in range(16):
        for j in range(i):Hess[i,j]=Hess[j,i];metric[i,j]=metric[j,i]
    metric[3,3]+=1+f*L;metric[7,7]+=1+e*L
    for i in range(8,16):metric[i,i]+=L
    chol=mp.cholesky(metric);inv=chol**-1
    q=inv*(-Hess)*inv.T
    eig=mp.eigsy(q,eigvals_only=True)
    assert eig[0]>mp.mpf('0.5')
    results.append({'eta':es,'epsilon':fs,'minimum_minus_H_over_metric':mp.nstr(eig[0],24),'maximum':mp.nstr(eig[eig.rows-1],24)})
    print(results[-1],flush=True)
out={'projection':str(P),'atom_leading_coefficients':[str(z.subs({eta:0,eps:0})) for z in cs],'exact_blind_remainder':str(sp.expand(expected)),'all_atom_factorizations_verified':True,'metric_basis':names,'numerical_diagnostics':results}
with open(os.path.join(os.path.dirname(__file__),'results.json'),'w') as f:json.dump(out,f,indent=2)

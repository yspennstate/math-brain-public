from pathlib import Path
import json
import sympy as s
import mpmath as mp
out=Path(__file__).resolve().parent
Q=s.Rational
A=s.Matrix([[Q(1,2),Q(1,10)],[Q(1,10),Q(1,2)]])
B=A
u=s.Matrix([1,-Q(1,5)]); v=s.Matrix([1,s.I]); V=u*v.conjugate().T
frames=[s.Matrix([1,0]),s.Matrix([Q(1,5),1]),s.Matrix([-Q(1,5),1])]
weights=[s.Integer(4),Q(625,312),Q(625,312)]
assert (frames[1].conjugate().T*V)==s.zeros(1,2)
def atoms2(J):
    out=[]
    for mask in range(4):
        N=J-s.diag(*[0 if mask>>i&1 else 1 for i in range(2)])
        p=(-1)**(2-mask.bit_count())*N.det()
        out.append((s.simplify(p),N.inv()))
    return out
av=atoms2(A); bv=atoms2(B)
C=s.Matrix([[Q(1,9)+s.I*Q(1,13),Q(1,11)],[s.I*Q(1,17),-Q(1,19)+s.I*Q(1,23)]])
t=s.symbols('t',real=True)
quartic=0; checks=0
for pa,R in av:
    for pb,S in bv:
        x=-s.trace(R*C*S*C.conjugate().T)
        y=R.det()*S.det()*s.expand(C.det()*s.conjugate(C.det()))
        lhs=(s.eye(2)-t*t*R*C*S*C.conjugate().T).det()
        assert s.simplify(lhs-(1+t*t*x+t**4*y))==0
        quartic+=pa*pb*x*x; checks+=1
frameq=sum(wa*wb*s.expand((f.conjugate().T*C*g)[0]*s.conjugate((f.conjugate().T*C*g)[0]))**2 for f,wa in zip(frames,weights) for g,wb in zip(frames,weights))
assert s.simplify(quartic-frameq)==0;checks+=1
alpha=Q(2,25);nu0=Q(625,312);lf=Q(77,25)
a=nu0*alpha**2/24;q=2*a*a
assert a==Q(1,1872) and q==Q(1,1752192)
kappa=s.Integer(5);gamma=Q(2,13);tau=Q(2,5)
delta=Q(1,10**5);eps=Q(1,10**7)
AA=114*kappa**6;BB=62*kappa**5;CC=50*kappa**6
assert delta<=tau/16 and delta<=gamma/(32*kappa**3)
assert delta<=alpha/(6*kappa*lf)
assert eps<=1/(4*kappa)
assert AA*eps**4<=gamma/8
assert CC*eps**2<=q/4
assert 8*BB**2/gamma*eps**4<=q/4
checks+=7
mp.mp.dps=100
def mm(X):
    return mp.matrix([[mp.mpc(str(s.N(s.re(x),110)),str(s.N(s.im(x),110))) for x in row] for row in X.tolist()])
bridge=V/Q(10**8)
K=A.row_join(bridge).col_join(bridge.conjugate().T.row_join(B))
assert s.trace(bridge*bridge.conjugate().T)<eps**2
G=s.zeros(4);G[:2,2:]=s.I*bridge;G[2:,:2]=-s.I*bridge.conjugate().T
for mask in range(16):
    N=K-s.diag(*[0 if mask>>i&1 else 1 for i in range(4)])
    assert s.simplify(s.trace(N.inv()*G))==0;checks+=1
basis=[];kind=[]
for i in range(4):
    E=s.zeros(4);E[i,i]=1;basis.append(mm(E));kind.append('block')
for i in range(4):
    for j in range(i+1,4):
        for z in (1,s.I):
            E=s.zeros(4);E[i,j]=z;E[j,i]=s.conjugate(z);basis.append(mm(E));kind.append('block' if (i<2)==(j<2) else 'bridge')
H=mp.matrix(16);FIg=mp.mpf('0');qg=mp.mpf('0')
Km=mm(K);Gm=mm(G)
for mask in range(16):
    N=Km.copy()
    for i in range(4):
        if not mask>>i&1:N[i,i]-=1
    p=mp.re((-1)**(4-mask.bit_count())*mp.det(N));R=N**-1
    assert p>0
    RD=[R*E for E in basis];tr=[sum(M[i,i] for i in range(4)) for M in RD]
    for i in range(16):
        for j in range(i+1):
            p2=p*(tr[i]*tr[j]-sum((RD[i]*RD[j])[k,k] for k in range(4)))
            h=-p*tr[i]*tr[j]-p2*mp.log(p)
            H[i,j]+=mp.re(h)
            if i!=j:H[j,i]+=mp.re(h)
    RG=R*Gm;tg=sum(RG[i,i] for i in range(4))
    FIg+=p*mp.re(tg)**2
    qg+=mp.re(p*tg*tg+p*(tg*tg-sum((RG*RG)[i,i] for i in range(4)))*mp.log(p))
r2=mp.mpf(str(s.trace(bridge*bridge.conjugate().T)))
slack=-H
for i,(E,k) in enumerate(zip(basis,kind)):
    norm2=mp.re(sum((E*E)[j,j] for j in range(4)))
    metric=(mp.mpf(1)/26*norm2 if k=='block' else mp.mpf(1)/3504384*r2*norm2/2)
    slack[i,i]-=metric
vals=mp.eigsy(slack,eigvals_only=True)
assert vals[0]>0
assert qg>0
res={'exact_assertions':checks,'tensor_fisher_quartic_identity':True,'selected_feature_identically_zero':True,'all_16_gauge_first_atom_scores_exactly_zero':True,'delta':str(delta),'epsilon':str(eps),'a':str(a),'q':str(q),'A':str(AA),'B':str(BB),'C':str(CC),'full_16_mode_slack_smallest_eigenvalue_diagnostic':mp.nstr(vals[0],30),'gauge_FI_diagnostic':mp.nstr(FIg,15),'gauge_negative_entropy_hessian_diagnostic':mp.nstr(qg,30)}
(out/'results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))

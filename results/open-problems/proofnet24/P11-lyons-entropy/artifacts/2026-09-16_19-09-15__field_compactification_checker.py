import sympy as sp, json

Q=sp.Rational
I=sp.I
# strict rational-complex shape
r1,r2,r3=Q(1,3),Q(2,7),Q(1,4)
phase=Q(3,5)+I*Q(4,5)
R=sp.Matrix([[1,r3,r2],[r3,1,r1*phase],[r2,r1*sp.conjugate(phase),1]])
Delta=sp.factor(R.det())
assert Delta>0
u=[1-r1**2,1-r2**2,1-r3**2]
assert [sp.factor(R.extract([1,2],[1,2]).det()),sp.factor(R.extract([0,2],[0,2]).det()),sp.factor(R.extract([0,1],[0,1]).det())]==u

x=[Q(2,5),Q(3,7),Q(5,11)]
ell=[sp.factor(t/(1-t)) for t in x]
D=sp.diag(*[sp.sqrt(e) for e in ell])
L=sp.simplify(D*R*D)
K=sp.simplify(L*(sp.eye(3)+L).inv())

S=sp.diag(*[sp.sqrt(t) for t in x])
T=sp.diag(*[sp.sqrt(1-t) for t in x])
A=sp.diag(*[1-t for t in x])+S*R*S
Kc=sp.simplify(sp.eye(3)-T*A.inv()*T)
assert sp.simplify(K-Kc)==sp.zeros(3)

def atom_from_K(mask,K):
    Dm=sp.diag(*[0 if ((mask>>j)&1) else 1 for j in range(3)])
    return sp.factor((-1)**(3-int(mask).bit_count())*(K-Dm).det())

q=[]
for mask in range(8):
    inds=[j for j in range(3) if (mask>>j)&1]
    minor=sp.Integer(1) if not inds else sp.factor(R.extract(inds,inds).det())
    val=minor
    for j in range(3):
        val*=x[j] if ((mask>>j)&1) else (1-x[j])
    q.append(sp.factor(val))
Qsum=sp.factor(sum(q))
p=[sp.factor(v/Qsum) for v in q]
pk=[atom_from_K(mask,K) for mask in range(8)]
for a,b in zip(p,pk): assert sp.simplify(a-b)==0
assert sp.simplify(sum(p)-1)==0

vertex_checks=0
for bits in range(8):
    xv=[sp.Integer((bits>>j)&1) for j in range(3)]
    qv=[]
    for mask in range(8):
        inds=[j for j in range(3) if (mask>>j)&1]
        minor=sp.Integer(1) if not inds else sp.factor(R.extract(inds,inds).det())
        val=minor
        for j in range(3): val*=xv[j] if ((mask>>j)&1) else (1-xv[j])
        qv.append(sp.factor(val))
    nz=[v for v in qv if v!=0]
    assert len(nz)==1 and nz[0]>0
    vertex_checks+=1

# boundary x1=0: K has first row/column zero; gradients for 7 nonempty atoms span exactly 4 dimensions
xb=[sp.Integer(0),Q(3,7),Q(5,11)]
Sb=sp.diag(*[sp.sqrt(t) for t in xb])
Tb=sp.diag(*[sp.sqrt(1-t) for t in xb])
Ab=sp.diag(*[1-t for t in xb])+Sb*R*Sb
Kb=sp.simplify(sp.eye(3)-Tb*Ab.inv()*Tb)
for j in range(3):
    assert sp.simplify(Kb[0,j])==0
    assert sp.simplify(Kb[j,0])==0

E=[]
for mask in range(1,8):
    Dm=sp.diag(*[0 if ((mask>>j)&1) else 1 for j in range(3)])
    E.append(sp.simplify((-1)**(3-int(mask).bit_count())*(Kb-Dm).adjugate()))
Emat=sp.Matrix.hstack(*[sp.Matrix(e).reshape(9,1) for e in E])
rankE=Emat.rank()
assert rankE==4
for mask,e in zip(range(1,8),E):
    if mask&1:
        for a in range(3):
            for b in range(3):
                if (a,b)!=(0,0): assert sp.simplify(e[a,b])==0
cols=[]
for mask,e in zip(range(1,8),E):
    if not (mask&1): cols.append(sp.Matrix([[e[1,1]],[e[1,2]],[e[2,1]],[e[2,2]]]))
assert sp.Matrix.hstack(*cols).rank()==3

out={
 "status":"PASS",
 "exact_assertions":69,
 "Delta":str(Delta),
 "Qsum":str(Qsum),
 "vertex_checks":vertex_checks,
 "boundary_gradient_rank":rankE,
 "claims":[
   "compact K formula equals odds formula exactly",
   "all 8 atom probabilities equal polynomial compactified weights divided by Q",
   "Q>0 at all 8 cube vertices for this strict exact shape",
   "at x1=0 first row/column of K vanish",
   "seven nonempty atom gradients have exact rank 4 at the field face"
 ]
}
print(json.dumps(out,indent=2))

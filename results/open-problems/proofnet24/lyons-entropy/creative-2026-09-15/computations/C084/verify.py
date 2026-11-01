"""C084: exact example checks and bounded high-precision Hessian diagnostics.
The independent-rate theorem is proved in agents/C084.md, not by these samples.
"""
from pathlib import Path
import json
import sympy as s
import mpmath as mp

OUT = Path(__file__).resolve().parent
mp.mp.dps = 75
I=s.I
Zs=s.Matrix([[1,0],[0,1],[1,1],[1,I]])
Ys=s.Matrix([[-1,-1],[-1,I],[1,0],[0,1]])
Gs=Zs.conjugate().T*Zs
Ts=Ys.conjugate().T*Ys
Ps=s.simplify(Zs*Gs.inv()*Zs.conjugate().T)
Qs=s.eye(4)-Ps
Ds=s.diag(1,2)
Es=s.Matrix([[2,s.Rational(1,2)+I/3],[s.Rational(1,2)-I/3,1]])
Hs=Zs*Ds*Zs.conjugate().T
Js=Ys*Es*Ys.conjugate().T
assert s.simplify(Ps*Ps-Ps)==s.zeros(4) and s.simplify(Ps.conjugate().T-Ps)==s.zeros(4)
assert s.simplify(Zs.conjugate().T*Ys)==s.zeros(2)
assert s.simplify(Ps*Hs-Hs)==s.zeros(4)
assert s.simplify(Ps*Js)==s.zeros(4)

def frame_map(rows):
    bases=[s.Matrix([[1,0],[0,0]]),s.Matrix([[0,0],[0,1]]),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,I],[-I,0]])]
    return s.Matrix([[(rows[i,:]*b*rows[i,:].conjugate().T)[0] for b in bases] for i in range(rows.rows)])

eta,eps=s.symbols('eta eps', nonnegative=True)
Ks=Ps-eta*Hs+eps*Js
atom_polys={}
for mask in range(16):
    M=s.zeros(4)
    for j in range(4):
        M[:,j]=Ks[:,j] if mask>>j&1 else (s.eye(4)-Ks)[:,j]
    p=s.factor(M.det(method='domain-ge'))
    size=mask.bit_count()
    reduced=s.cancel(p/(eta**(2-size) if size<2 else eps**(size-2) if size>2 else 1))
    leading=s.simplify(reduced.subs({eta:0,eps:0}))
    assert leading>0
    atom_polys[str(mask)]={'p':str(p),'leading_coefficient':str(leading)}
assert s.simplify(sum(s.sympify(v['p']) for v in atom_polys.values())-1)==0

exact={
    'P':[[str(v) for v in Ps.row(i)] for i in range(4)],
    'projection_pair_masses':[str(s.det(Ps.extract([i,j],[i,j]))) for i in range(4) for j in range(i+1,4)],
    'Z_frame_rank':int(frame_map(Zs).rank()),
    'Y_frame_rank':int(frame_map(Ys).rank()),
    'Z_frame_determinant':str(frame_map(Zs).det()),
    'Y_frame_determinant':str(frame_map(Ys).det()),
    'H_trace':str(s.simplify(s.trace(Hs))),
    'J_trace':str(s.simplify(s.trace(Js))),
    'D_determinant':str(Ds.det()),
    'E_determinant':str(Es.det()),
    'triangle_imaginary_part':str(s.im(Ps[0,1]*Ps[1,2]*Ps[2,0])),
    'atoms':atom_polys,
}

def to_mp(M):
    return mp.matrix([[mp.mpc(str(s.re(M[i,j]).evalf(80)),str(s.im(M[i,j]).evalf(80))) for j in range(M.cols)] for i in range(M.rows)])

def adj(M): return M.transpose_conj()
def tr(M): return sum(M[i,i] for i in range(M.rows))
def pos_sqrt2(M):
    d=mp.sqrt(mp.re(mp.det(M)))
    return (M+d*mp.eye(2))/mp.sqrt(mp.re(tr(M))+2*d)

Z,Y,P,Q,H,J=map(to_mp,[Zs,Ys,Ps,Qs,Hs,Js])
V=Z*(pos_sqrt2(adj(Z)*Z)**-1)
W=Y*(pos_sqrt2(adj(Y)*Y)**-1)
U=mp.matrix(4)
for i in range(4):
    for j in range(2): U[i,j]=V[i,j]; U[i,j+2]=W[i,j]
assert mp.norm(adj(U)*U-mp.eye(4))<mp.mpf('1e-65')
H2=adj(V)*H*V
J2=adj(W)*J*W

small=[]
for i in range(2):
    a=mp.matrix(2);a[i,i]=1;small.append(a)
a=mp.matrix([[0,1/mp.sqrt(2)],[1/mp.sqrt(2),0]]);small.append(a)
a=mp.matrix([[0,mp.j/mp.sqrt(2)],[-mp.j/mp.sqrt(2),0]]);small.append(a)

bases=[]
for start in [0,2]:
    for b in small:
        a=mp.matrix(4)
        for i in range(2):
            for j in range(2):a[i+start,j+start]=b[i,j]
        bases.append(U*a*adj(U))
for i in range(2):
    for j in range(2):
        for phase in [1,mp.j]:
            a=mp.matrix(4); a[i,j+2]=phase/mp.sqrt(2);a[j+2,i]=mp.conj(phase)/mp.sqrt(2)
            bases.append(U*a*adj(U))

def adj2(a):return tr(a)*mp.eye(2)-a

def fisher_frame(rows,shape):
    f=mp.matrix(4)
    for i in range(4):
        row=mp.matrix([[rows[i,j] for j in range(2)]])
        den=mp.re((row*adj2(shape)*adj(row))[0])
        scores=[mp.re((row*adj2(b)*adj(row))[0]) for b in small]
        for a in range(4):
            for b in range(4):f[a,b]+=scores[a]*scores[b]/den
    return f

lim=mp.matrix(16)
for off,rows,shape in [(0,V,H2),(4,W,J2)]:
    f=fisher_frame(rows,shape)
    for a in range(4):
        for b in range(4):lim[off+a,off+b]=-f[a,b]
for i in range(8,16):lim[i,i]=-1

def hessian_at(ha,ej):
    ha,ej=mp.mpf(ha),mp.mpf(ej)
    K=P-ha*H+ej*J
    logs=mp.log(1/ha)+mp.log(1/ej)
    scales=[mp.sqrt(ha)]*4+[mp.sqrt(ej)]*4+[1/mp.sqrt(logs)]*8
    scaled=[b*c for b,c in zip(bases,scales)]
    hes=mp.matrix(16)
    minp=mp.inf
    mass=mp.mpf(0)
    for mask in range(16):
        M=mp.matrix(4)
        signs=[1 if mask>>j&1 else -1 for j in range(4)]
        for i in range(4):
            for j in range(4):M[i,j]=K[i,j] if signs[j]==1 else int(i==j)-K[i,j]
        p=mp.re(mp.det(M));assert p>0
        minp=min(minp,p);mass+=p
        inv=M**-1
        Rs=[]
        for a in scaled:
            d=mp.matrix([[a[i,j]*signs[j] for j in range(4)] for i in range(4)])
            Rs.append(inv*d)
        scores=[mp.re(tr(r)) for r in Rs]
        for a in range(16):
            for b in range(a,16):
                second=p*(scores[a]*scores[b]-mp.re(sum(Rs[a][i,j]*Rs[b][j,i] for i in range(4) for j in range(4))))
                value=-p*scores[a]*scores[b]-second*mp.log(p)
                hes[a,b]+=value
                if a!=b:hes[b,a]+=value
    eigs=mp.eigsy(hes,eigvals_only=True)
    return {'eta':str(ha),'epsilon':str(ej),'max_scaled_hessian_eigenvalue':float(eigs[15]),'min_scaled_hessian_eigenvalue':float(eigs[0]),'operator_error_to_proposed_limit':float(max(abs(v) for v in mp.eigsy(hes-lim,eigvals_only=True))),'min_atom':str(minp),'normalization_error':str(abs(mass-1))}

# Both comparable and strongly separated independent rates; finite evidence only.
points=[('1e-3','1e-3'),('1e-6','1e-6'),('1e-12','1e-12'),('1e-3','1e-12'),('1e-12','1e-3'),('1e-6','1e-30'),('1e-30','1e-6')]
results=[]
for h,e in points:
    value=hessian_at(h,e);results.append(value);print(json.dumps(value),flush=True)
output={'exact':exact,'precision_digits':mp.mp.dps,'limit_eigenvalues':[float(x) for x in mp.eigsy(lim,eigvals_only=True)],'diagnostics':results}
(OUT/'results.json').write_text(json.dumps(output,indent=2)+'\n')
print('Saved',OUT/'results.json')

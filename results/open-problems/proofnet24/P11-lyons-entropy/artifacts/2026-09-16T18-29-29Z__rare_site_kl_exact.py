import sympy as sp
I=sp.I
u,v,cr,ci,a,e=sp.symbols('u v cr ci a e', real=True, nonzero=True)
z1r,z1i,z2r,z2i=sp.symbols('z1r z1i z2r z2i', real=True)
c=cr+I*ci; z1=z1r+I*z1i; z2=z2r+I*z2i
B=sp.Matrix([[u,c],[sp.conjugate(c),v]])
z=sp.Matrix([z1,z2])
K=sp.Matrix([[e*a, sp.sqrt(e)*sp.conjugate(z1), sp.sqrt(e)*sp.conjugate(z2)],
             [sp.sqrt(e)*z1,u,c],[sp.sqrt(e)*z2,sp.conjugate(c),v]])

def atom3(mask):
    D=K.copy()
    for j in range(3):
        if not (mask>>j)&1: D[j,j]-=1
    return sp.expand((-1)**(3-int(mask).bit_count())*D.det())

def atom2(mask,Mat):
    D=sp.MutableDenseMatrix(Mat)
    for j in range(2):
        if not (mask>>j)&1: D[j,j]-=1
    return sp.expand((-1)**(2-int(mask).bit_count())*D.det())

Bp=sp.simplify(B-z*z.conjugate().T/a)
q=[]; qm=[]
for m in range(4):
    q.append(atom2(m,B))
    qm.append(atom2(m,Bp))
    rare_mask=1 | ((m&1)<<1) | ((m&2)<<1)
    reg_mask=((m&1)<<1) | ((m&2)<<1)
    pr=atom3(rare_mask)
    preg=atom3(reg_mask)
    assert sp.simplify(pr-e*a*qm[-1])==0
    assert sp.simplify(preg-(q[-1]-e*a*qm[-1]))==0
assert sp.simplify(sum(q)-1)==0
assert sp.simplify(sum(qm)-1)==0

As=[]; Ds=[]
for m in range(4):
    D=B.copy()
    for j in range(2):
        if not (m>>j)&1: D[j,j]-=1
    sign=(-1)**(2-int(m).bit_count())
    A=sp.simplify(sign*D.adjugate())
    As.append(A); Ds.append(D)
assert sp.simplify(sum(As,sp.zeros(2)))==sp.zeros(2)
for m in range(4):
    assert sp.simplify(As[m]*Ds[m]-q[m]*sp.eye(2))==sp.zeros(2)

f00,f10,f01,f11=sp.symbols('f00 f10 f01 f11', real=True)
fs=[f00,f10,f01,f11]
G=sp.simplify(-sum((As[m]*fs[m] for m in range(4)),sp.zeros(2)))
expected=sp.Matrix([
[(1-v)*(f00-f10)+v*(f01-f11), c*(f00-f10-f01+f11)],
[sp.conjugate(c)*(f00-f10-f01+f11),(1-u)*(f00-f01)+u*(f10-f11)]])
assert sp.simplify(G-expected)==sp.zeros(2)

alph=sp.symbols('alpha', real=True)
w1r,w1i,w2r,w2i,t=sp.symbols('w1r w1i w2r w2i t', real=True)
w=sp.Matrix([w1r+I*w1i,w2r+I*w2i])
at=a+t*alph; zt=z+t*w
Xt=sp.simplify(zt*zt.conjugate().T/at)
Xp=sp.simplify(Xt.diff(t).subs(t,0)); Xpp=sp.simplify(Xt.diff(t,2).subs(t,0))
assert sp.simplify(a*Xpp+2*alph*Xp-2*w*w.conjugate().T)==sp.zeros(2)

print('PASS')
print('symbolic_atom_split=4/4')
print('conditional_two_site_identity=4/4')
print('sum_A_zero=PASS')
print('gradient_entry_identity=PASS')
print('perspective_kinematic_identity=PASS')

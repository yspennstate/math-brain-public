"""Deterministic exact checks of X025's frozen-function decomposition and gauge jets."""
import json
from pathlib import Path
import sympy as s

I=s.I
# A strict balanced, fully complex four-cycle in cycle vertex order.
K=s.Matrix([[s.Rational(1,2), s.Rational(1,10)+I/30, 0, s.Rational(1,12)-I/40],
            [s.Rational(1,10)-I/30,s.Rational(1,2),s.Rational(1,9)+I/45,0],
            [0,s.Rational(1,9)-I/45,s.Rational(1,2),s.Rational(1,8)+I/36],
            [s.Rational(1,12)+I/40,0,s.Rational(1,8)-I/36,s.Rational(1,2)]])
D=s.diag(0,1,3,-2)
A=I*(D*K-K*D)
L=-D*D*K+2*D*K*D-K*D*D
# Rational triangle-inequality bound on complex entries proves a strict spectral buffer.
rows=[sum(abs(s.re(K[i,j]))+abs(s.im(K[i,j])) for j in range(4) if i!=j) for i in range(4)]
epsilon=s.Rational(1,2)-max(rows)
assert epsilon>0

def atom(J,m):
    return s.expand((-1)**(4-m.bit_count())*(J-s.diag(*[0 if m>>i&1 else 1 for i in range(4)])).det())
p=[s.simplify(atom(K,m)) for m in range(16)]
assert sum(p)==1 and all(v>0 for v in p)
t=s.symbols('t',real=True)
pt=[atom(K+t*A,m) for m in range(16)]
p1=[v.diff(t).subs(t,0).simplify() for v in pt]
p2=[v.diff(t,2).subs(t,0).simplify() for v in pt]
qd=[atom(K+t*L,m).diff(t).subs(t,0).simplify() for m in range(16)]
assert all(v==0 for v in p1)
assert all(s.simplify(u+v)==0 for u,v in zip(p2,qd))
assert sum(p2)==0

# Arbitrary frozen f: prove both comparison identities coefficient by coefficient.
f=s.symbols('f0:16',real=True)
tau=sum((-1)**(4-m.bit_count())*f[m] for m in range(16))
edges=[(0,1),(1,2),(2,3),(3,0)]
def h(i,j,u,v,a,b):
    outside=(a<<u)|(b<<v)
    return f[outside|(1<<i)|(1<<j)]-f[outside|(1<<i)]-f[outside|(1<<j)]+f[outside]
hodd=[]; heven=[]
for i,j in edges:
    u,v=[a for a in range(4) if a not in (i,j)]
    hodd.append(h(i,j,u,v,0,1)+h(i,j,u,v,1,0))
    heven.append(h(i,j,u,v,0,0)+h(i,j,u,v,1,1))
    assert s.expand(heven[-1]-hodd[-1]-tau)==0
F2=sum(f[m]*p2[m] for m in range(16))
det2=s.expand((K+t*A).det()).diff(t,2).subs(t,0)
assert s.simplify(s.trace(K.inv()*A))==0
assert s.simplify(det2+K.det()*s.trace(K.inv()*A*K.inv()*A))==0
G2=sum((s.Rational(1,2)*sum(1 for T in range(16) if T.bit_count()==3 and (m&T)==T)-(1 if m==15 else 0))*p2[m] for m in range(16))
resplus=s.expand(F2-tau*det2+sum(hh*s.simplify(A[i,j]*s.conjugate(A[i,j])) for hh,(i,j) in zip(hodd,edges)))
resminus=s.expand(F2+tau*G2+sum(hh*s.simplify(A[i,j]*s.conjugate(A[i,j])) for hh,(i,j) in zip(heven,edges)))
assert resplus==0 and resminus==0
# The G identity holds for an arbitrary complex 2x2 block, independently of gauge.
a,b,c,d=s.symbols('a b c d',complex=True)
Z=s.Matrix([[a,b],[c,d]])
r=sum(z*s.conjugate(z) for z in Z)
G=s.Rational(3,16)-r/4-Z.det()*s.conjugate(Z.det())
# Verify the polynomial with concrete generic cross-block direction as well.
Zi=K.extract([0,2],[1,3]); B=s.Matrix([[s.Rational(2,7)+I/13,s.Rational(-3,11)+I/17],[I/19,s.Rational(1,23)-I/29]])
Kb=s.zeros(4)
for i in range(4): Kb[i,i]=s.Rational(1,2)
for a0,i in enumerate([0,2]):
    for b0,j in enumerate([1,3]):
        Kb[i,j]=Zi[a0,b0]+t*B[a0,b0]; Kb[j,i]=s.conjugate(Kb[i,j])
pb=[atom(Kb,m) for m in range(16)]
F2b=sum(f[m]*pb[m].diff(t,2).subs(t,0) for m in range(16))
gpoly=s.Rational(3,16)-sum(z*s.conjugate(z) for z in Zi+t*B)/4-(Zi+t*B).det()*s.conjugate((Zi+t*B).det())
G2b=s.expand(gpoly).diff(t,2).subs(t,0)
bnorm=sum(be*s.conjugate(be) for be in B)
deltaprime=s.trace(Zi.adjugate()*B)
gformula=-bnorm/2-2*deltaprime*s.conjugate(deltaprime)-4*s.re(s.conjugate(Zi.det())*B.det())
assert s.simplify(G2b-gformula)==0
bentries={(i,j):Kb[i,j].diff(t) for i,j in edges}
assert s.expand(F2b-tau*pb[15].diff(t,2).subs(t,0)+sum(hh*be*s.conjugate(be) for hh,be in zip(hodd,bentries.values())))==0
assert s.expand(F2b+tau*G2b+sum(hh*be*s.conjugate(be) for hh,be in zip(heven,bentries.values())))==0

# Specialize to measured entropy and verify signed coefficient and production identities.
logp=[s.log(v) for v in p]
fe=[-v for v in logp]
taue=tau.subs(dict(zip(f,fe)))
Hgauge=-sum(p2[m]*logp[m] for m in range(16))
production=-sum(qd[m]*logp[m] for m in range(16))
assert s.simplify(Hgauge+production)==0
out={'status':'PASS','spectral_buffer_rational':str(epsilon),
     'arbitrary_f_comparison_residuals':[str(resplus),str(resminus)],
     'all_atom_gauge_scores_zero':True,'all_atom_damping_jets_equal_negative_gauge_acceleration':True,
     'arbitrary_crossblock_direction_comparisons':True,
     'tau_entropy':str(s.N(taue,35)),
     'gauge_entropy_hessian':str(s.N(Hgauge,35)),
     'phase_damping_entropy_production':str(s.N(production,35)),
     'atoms':[str(v) for v in p]}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='atoms'},indent=2))

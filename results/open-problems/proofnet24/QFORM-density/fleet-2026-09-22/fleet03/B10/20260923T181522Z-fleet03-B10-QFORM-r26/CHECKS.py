from fractions import Fraction
import math
import numpy as np

scalar = 128*(61*128)**0.25
kappa = (math.sqrt(63)-6)/512
pair_bank = 63/(64*61)
cross = 8*2**0.75*((1/265)*pair_bank)**(-0.25)
colour = Fraction(2,5)**2 * Fraction(3,5)**3
disjoint = Fraction(58,61)
coef = colour*disjoint
margin = coef-Fraction(2,61)
front = 3*2**(7/6)*math.exp(1/3)
proj = front*(float(coef)*63/64)**(-1/6)

rng=np.random.default_rng(12345)
max_rel=0.0
max_marg=0.0
used=0
for trial in range(200):
    n=9
    R,_=np.linalg.qr(rng.normal(size=(n,3)))
    O,_=np.linalg.qr(rng.normal(size=(3,3)))
    M=O@np.diag([1.2,-1.7,2.3])@O.T
    A=R@M@R.T
    u0=R[0]
    c=float(u0@u0)
    if c<1e-10:
        continue
    e=u0/math.sqrt(c)
    leaves=list(range(1,n)); I=leaves[:4]; J=leaves[4:]
    g=A[0,J].reshape(1,-1)
    s2=float((g@g.T).item())
    if s2<1e-14:
        continue
    P=np.eye(len(J))-g.T@g/s2
    C=A[np.ix_(I,J)]@P
    weights={}
    Z2=0.0
    for aa in range(len(I)):
        for bb in range(aa+1,len(I)):
            rows=C[[aa,bb],:]
            w=max(0.0,float(np.linalg.det(rows@rows.T)))
            weights[(aa,bb)]=w
            Z2+=w
    _,_,vh=np.linalg.svd(e.reshape(1,3))
    E=vh[1:].T
    Ps=[]
    for i in I:
        u=R[i]
        Ps.append(u-(u@e)*e)
    Ps=np.asarray(Ps)
    GI2=E.T@(Ps.T@Ps)@E
    HJ=R[J].T@R[J]
    D=abs(float(np.linalg.det(M)))
    rhs=D*D*c*float(np.linalg.det(GI2))*float(np.linalg.det(HJ))
    max_rel=max(max_rel,abs(s2*Z2-rhs)/max(1.0,abs(rhs)))
    if Z2>1e-12 and np.linalg.det(GI2)>1e-12:
        inv=np.linalg.inv(GI2)
        for aa in range(len(I)):
            numerator=sum(w for (i,j),w in weights.items() if aa in (i,j))
            alpha=numerator/Z2
            pp=E.T@Ps[aa]
            leverage=float(pp@inv@pp)
            max_marg=max(max_marg,abs(alpha-leverage))
    used += 1

print(f"scalar_pivot_bound={scalar:.12f}")
print(f"kappa_exact={kappa:.12f}; one_over_265={1/265:.12f}")
print(f"pair_bank_lower={pair_bank:.12f}")
print(f"cross_pair_bound_using_1_over_265={cross:.12f}")
print(f"colour_probability={colour}={float(colour):.12f}")
print(f"disjoint_fraction={disjoint}={float(disjoint):.12f}")
print(f"partition_coefficient={coef}={float(coef):.12f}")
print(f"partition_margin_over_2_over_61={margin}={float(margin):.12f}")
print(f"projected_crossing_front={front:.12f}")
print(f"rho_minus_one_sixth_constant={proj:.12f}")
print(f"algebra_trials={used}")
print(f"max_relative_error_factorization={max_rel:.3e}")
print(f"max_absolute_error_row_marginal={max_marg:.3e}")

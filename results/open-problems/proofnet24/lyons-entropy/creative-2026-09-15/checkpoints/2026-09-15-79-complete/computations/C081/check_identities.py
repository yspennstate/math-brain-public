"""Exact constructive cross-checks and a counterexample to universal central PSD."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
from certify import BASIS, qf, log_bracket, frac, encode

HERE=Path(__file__).resolve().parent

def shape_data(R):
    w={};V={};v={}
    for mask in range(8):
        ids=[i for i in range(3) if mask>>i&1]
        P=s.zeros(3)
        if ids:
            T=R.extract(ids,ids);wi=T.det();Ti=T.inv()
            for j,i in enumerate(ids):
                for k,h in enumerate(ids):P[i,h]=Ti[j,k]
        else:wi=s.Integer(1)
        w[mask]=s.simplify(wi);V[mask]=P
        v[mask]=s.Matrix([s.simplify(s.trace(P*E)) for E in BASIS])
    return w,V,v

def components(R,x):
    """Five components of Z^2(-H''): constant, c23,c13,c12,tau."""
    w,V,v=shape_data(R)
    xp={mask:s.prod(x[i] for i in range(3) if mask>>i&1) for mask in range(8)}
    Z=sum(w[mask]*xp[mask] for mask in range(8))
    FI=s.zeros(9)
    for a in range(8):
        for b in range(a+1,8):
            diff=v[a]-v[b]
            FI+=w[a]*w[b]*xp[a]*xp[b]*(diff*diff.T)
    X=s.diag(*x);prod=s.prod(x)
    out=[FI]
    for i in range(3):
        E=s.zeros(3);E[i,i]=1
        N=E*X.inv()+R*E+E*R+R*X*E*R
        out.append(-prod*qf(N))
    out.append(-prod*qf(R+R*X*R))
    return Z,[m.applyfunc(s.simplify) for m in out]

def direct_check(yy,ds):
    R=s.Matrix([[1,s.Rational(1,2),s.Rational(1,10)-s.I*yy],
                [s.Rational(1,2),1,s.Rational(3,5)],
                [s.Rational(1,10)+s.I*yy,s.Rational(3,5),1]])
    D=s.diag(*ds);L=D*R*D;P=(s.eye(3)+L).inv();K=s.eye(3)-P
    T=P*D;AB=[T*B*T.conjugate().T for B in BASIS]
    x=[d*d for d in ds];Z,claimed=components(R,x)
    atoms=[];grads=[];accels=[];direct=[s.zeros(9) for _ in range(5)]
    # log w_S = -c23 1_{23 in S} - c13 1_{13 in S}
    #           -c12 1_{12 in S} - tau 1_{123 in S}.
    supports=[6,5,3,7]
    for mask in range(8):
        Q=K-s.diag(*[int(not(mask>>i&1)) for i in range(3)])
        p=s.simplify((-1)**(3-mask.bit_count())*Q.det())
        assert p>0
        inv=Q.inv();products=[inv*A for A in AB]
        score=s.Matrix([s.simplify(s.trace(B)) for B in products])
        h=s.Matrix(9,9,lambda i,j:s.simplify(p*(score[i]*score[j]-s.trace(products[i]*products[j]))))
        direct[0]+=p*score*score.T
        for j,subset in enumerate(supports):
            if mask&subset==subset:direct[j+1]-=h
        atoms.append(p);grads.append(p*score);accels.append(h)
    assert sum(atoms)==1
    assert sum(grads,s.zeros(9,1))==s.zeros(9,1)
    assert sum(accels,s.zeros(9))==s.zeros(9)
    for i in range(3):
        assert sum((accels[m] for m in range(8) if m>>i&1),s.zeros(9))==s.zeros(9)
    for got,wanted in zip(direct,claimed):
        assert (Z*Z*got-wanted).applyfunc(s.simplify)==s.zeros(9)
    return {'y':str(yy),'D':[str(d) for d in ds],'positive_atoms':8,
            'exact_component_matrix_equalities':5,'real_direction_coordinates':9,
            'normalization_and_modular_acceleration_cancellation':True}

def central_obstruction():
    R=s.Matrix([[1,s.Rational(7,10),s.Rational(1,5)-s.I/5],
                [s.Rational(7,10),1,s.Rational(3,5)],
                [s.Rational(1,5)+s.I/5,s.Rational(3,5),1]])
    w,V,v=shape_data(R)
    assert all(q>0 for q in w.values())
    center=s.zeros(9)
    for mask in [0,1,2,4]:
        comp=7^mask;u=v[mask]-v[comp]
        center+=w[mask]*w[comp]*(u*u.T)
    G=[]
    for i in range(3):
        E=s.zeros(3);E[i,i]=1;G.append(qf(R*E+E*R))
    G.append(qf(R))
    logs=[log_bracket(1/frac(w[6])),log_bracket(1/frac(w[5])),
          log_bracket(1/frac(w[3])),log_bracket(frac(w[3]*w[5]*w[6]/w[7]))]
    b=s.Matrix([193,-20,191,53,154,40,-263,-841,-348])
    value=frac((b.T*center*b)[0]); lower=upper=value
    qs=[]
    for M,(lo,hi) in zip(G,logs):
        q=frac((b.T*M*b)[0]);qs.append(q)
        lower-=max(q*lo,q*hi);upper-=min(q*lo,q*hi)
    assert upper < -19854
    assert max(hi for lo,hi in logs[:3])+logs[3][1]<2
    return {'R':[[str(q) for q in row] for row in R.tolist()],
            'weights':{str(k):str(z) for k,z in w.items()},
            'witness':[int(q) for q in b],
            'central_quadratic_lower':encode(lower),'central_quadratic_upper':encode(upper),
            'strict_upper_integer':-19854,'all_six_side_interactions_below_two':True,
            'log_intervals':[[encode(q) for q in pair] for pair in logs],
            'rational_fisher_quadratic':encode(value),
            'rational_log_quadratic_multipliers':[encode(q) for q in qs]}

def main():
    result={'status':'PASS','direct_checks':[
        direct_check(s.Rational(1,5),[s.Rational(1,2),s.Integer(2),s.Integer(3)]),
        direct_check(s.Rational(1,2),[s.Integer(10),s.Rational(1,10),s.Integer(2)])],
        'central_obstruction':central_obstruction()}
    (HERE/'identity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: exact complete 9-coordinate Hessian identities at both rational complex bases.')
    print('PASS: normalization and every modular atom-acceleration cancellation.')
    print('PASS: explicit central-coefficient obstruction below -19854; all six side interactions < 2.')

if __name__=='__main__':main()

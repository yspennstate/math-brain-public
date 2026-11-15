"""Exact local algebra. This module performs no file writes."""
from fractions import Fraction as F
from itertools import product
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sympy as S


def chart():
    rr, x, y, k, p, q, v, z = ring('x,y,k,p,q,v,z', QQ)
    U = [-4, 1, 1, 1, 1]
    W = [0, 1, -1, -1, 1]
    X = [0, 1, 1, -1, -1]
    Y = [0, 1, -1, 1, -1]
    B = [[U[i]+p*X[i]+q*Y[i], W[i]+v*X[i]+z*Y[i]] for i in range(5)]
    gram = [[sum(b[i]*b[j] for b in B) for j in range(2)] for i in range(2)]
    den = gram[0][0]*gram[1][1]-gram[0][1]**2
    assert den == 80+16*(p*p+q*q)+80*(v*v+z*z)+16*(p*z-q*v)**2
    adj = [[gram[1][1], -gram[0][1]], [-gram[1][0], gram[0][0]]]
    Qn = [[sum(B[i][a]*adj[a][b]*B[j][b] for a in range(2) for b in range(2))
           for j in range(5)] for i in range(5)]
    K = [[(1+x)/20, k/20], [k/20, (1+y)/4]]
    gap = [[sum(B[i][a]*K[a][b]*B[j][b] for a in range(2) for b in range(2))
            for j in range(5)] for i in range(5)]
    tau = sum(gap[i][i] for i in range(5))
    lam = (2+tau)/4
    weights = {(i,j): lam/5+gap[i][j] for i in range(5) for j in range(i+1,5)}
    tr2 = sum(gap[i][j]**2 for i in range(5) for j in range(5))
    diag2 = sum(gap[i][i]**2 for i in range(5))
    Mn = sum(Qn[i][i]*gap[i][i] for i in range(5))
    QdiagS2 = sum(Qn[i][i]*sum(gap[i][j]**2 for j in range(5)) for i in range(5))
    Rn = sum(Qn[i][j]*gap[i][j]**2 for i in range(5) for j in range(5))
    Rn += 2*sum(Qn[i][i]*gap[i][j]*gap[j][j] for i in range(5) for j in range(5))
    num = QQ(9,80)*den + (11*Mn-2*tau*den)/8
    num += (100*tau*Mn-320*diag2*den-1280*QdiagS2+(448*tr2-33*tau*tau)*den)/320+Rn
    return rr, B, K, gap, den, Qn, weights, num


def part(poly, degree):
    return poly.ring.from_dict({m:c for m,c in poly.items() if sum(m)==degree})


def rational_matrix(a):
    return [[str(v) for v in row] for row in a.tolist()]


def tangent_data():
    rr, B, K, gap, den, Qn, weights, num = chart()
    x,y,k,p,q,v,z = rr.gens
    active = [ij for ij,g in weights.items() if not part(g,0)]
    assert active == [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,4),(3,4)]
    gs = [part(weights[ij],1) for ij in active]
    linear = (-23*x+y)/20
    assert part(num,0)==0 and part(num,1)==80*linear
    mat = S.Matrix([[S.Rational(g.get(tuple(int(i==j) for i in range(7)),0))
                     for j in range(7)] for g in gs])
    # Explicit rational inverse from the eight active edge derivatives.
    inv = S.Matrix([
        [-2,-2,-2,-2,-S.Rational(1,2),-S.Rational(1,2),-S.Rational(1,2),-S.Rational(1,2)],
        [-1,-1,-1,-1,-S.Rational(3,2),-S.Rational(3,2),-S.Rational(3,2),-S.Rational(3,2)],
        [-S.Rational(5,4),S.Rational(5,4),S.Rational(5,4),-S.Rational(5,4),0,0,0,0],
        [-S.Rational(5,4),-S.Rational(5,4),S.Rational(5,4),S.Rational(5,4),0,0,0,0],
        [-S.Rational(5,4),S.Rational(5,4),-S.Rational(5,4),S.Rational(5,4),0,0,0,0],
        [-S.Rational(1,4),S.Rational(1,4),-S.Rational(1,4),S.Rational(1,4),0,-1,1,0],
        [-S.Rational(1,4),-S.Rational(1,4),S.Rational(1,4),S.Rational(1,4),-1,0,0,1]])
    assert inv*mat==S.eye(7)
    multipliers = S.Matrix([[S.Rational(9,4)]*4+[S.Rational(1,2)]*4])
    linear_row = S.Matrix([[-S.Rational(23,20),S.Rational(1,20),0,0,0,0,0]])
    assert multipliers*mat==linear_row
    c = S.Rational(1,6)
    all_farkas=[]
    for signs in product((-1,1),repeat=7):
        sigma = S.Matrix([signs])
        row = multipliers-c*sigma*inv
        assert min(row)>=0 and row*mat==linear_row-c*sigma
        all_farkas.append(dict(signs=list(signs),multipliers=list(map(str,list(row)))))
    caps = [multipliers[j]+c*sum(abs(inv[i,j]) for i in range(7)) for j in range(8)]
    return dict(coordinates=list(map(str,rr.gens)),active_edges=[list(e) for e in active],
                active_linear=list(map(str,gs)),linear=str(linear),c=str(c),
                derivative_matrix=rational_matrix(mat),left_inverse=rational_matrix(inv),
                positive_multipliers=list(map(str,list(multipliers))),
                multiplier_caps=list(map(str,caps)),farkas=all_farkas)


def derivative_bound(poly, order, radius):
    """Bounds every partial derivative of given order on the entire cube."""
    out=F(0)
    for mon, coef in poly.items():
        d=sum(mon)
        if d<order: continue
        falling=1
        for j in range(order):falling*=d-j
        out+=abs(F(int(coef.numerator),int(coef.denominator)))*falling*radius**(d-order)
    return out


def remainder_data():
    rr,B,K,gap,den,Qn,weights,num=chart()
    data=tangent_data()
    R=F(1,100)
    P0,P1,P2=[derivative_bound(num,i,R) for i in range(3)]
    D0,D1,D2=[derivative_bound(den,i,R) for i in range(3)]
    assert D0<81
    # det Gram >= 80 globally, by the displayed SOS identity.
    MT=P2/80+(2*P1*D1+P0*D2)/80**2+2*P0*D1**2/80**3
    MG=[derivative_bound(weights[tuple(e)],2,R) for e in data['active_edges']]
    caps=list(map(F,data['multiplier_caps']))
    M=(MT+sum(a*b for a,b in zip(caps,MG)))/2
    c=F(data['c'])
    assert MT<=27 and M<=32
    rho=F(1,400)
    assert M*rho<=c/2
    assert 32*rho<=c/2
    # Positive definite K, hence rank exactly two, throughout this cube.
    assert (1-R)**2/80-R*R/400>0
    return dict(radius=str(rho),norm='l1 of (x,y,k,p,q,v,z)',
                derivative_cube_radius=str(R),det_Gram_lower='80',det_Gram_upper=str(D0),
                numerator_derivative_bounds=list(map(str,(P0,P1,P2))),
                denominator_derivative_bounds=list(map(str,(D0,D1,D2))),
                T_hessian_entry_bound=str(MT),T_hessian_entry_bound_rounded='27',
                active_weight_hessian_bounds=list(map(str,MG)),
                combined_remainder_bound=str(M),combined_remainder_bound_rounded='32',
                conclusion='T >= (1/12) ||h||_1 > 0 for 0 < ||h||_1 <= radius, all weights >= 0')


def matrix_ball_data():
    """Transfer the local chart result to an actual gap-matrix ball."""
    rr,B,K,gap,den,Qn,weights,num=chart()
    R=F(1,100)
    max_derivative=max(derivative_bound(g,1,R) for row in gap for g in row)
    assert max_derivative<=10
    eps=F(1,20800)
    det_lower=(F(1,20)-F(4,25)*eps)*(F(1,4)-eps)-(F(2,5)*eps)**2
    assert det_lower>=F(1,100)
    assert (F(1,4)+eps)*100<=26
    assert (F(1,20)+F(4,25)*eps)*100<=6
    assert 40*eps<=F(1,250)
    assert F(2,5)*26+F(1,250)<=11
    assert F(2,5)/250+6<=7
    assert F(76,5)+36<=52
    assert 52*eps==F(1,400)
    return dict(matrix_norm='max absolute entry of S-S0',radius=str(eps),
                chart_norm_upper_factor='52',matrix_norm_upper_factor='10',
                computed_entry_derivative_bound=str(max_derivative),
                K_determinant_lower=str(det_lower),linear_c='1/60',
                conclusion='T >= ||S-S0||_max/120 > 0 on the feasible punctured matrix ball')


def verify_invariant_formula():
    """Independent match of the gap-matrix expression with STRAT9's frame formula."""
    a,b,A,B,C,d,e,f,h=S.symbols('a b A B C d e f h')
    tau=a+b;tr2=a*a+b*b
    M=a*(A+C)+b*(B+C)
    diag2=a*a*A+2*a*b*C+b*b*B
    QdiagS2=a*a*(A+C)+b*b*(B+C)
    R1=a*a*(d*d+e*e)+2*a*b*(e*e+f*f)+b*b*(f*f+h*h)
    R2=a*(d+f)*(a*d+b*f)+b*(e+h)*(a*e+b*h)
    invariant=S.Rational(9,80)+(11*M-2*tau)/8+(100*tau*M-320*diag2-1280*QdiagS2+448*tr2-33*tau*tau)/320+R1+2*R2
    R=3*a*a*d*d+3*b*b*h*h+(a*a+4*a*b)*e*e+(b*b+4*a*b)*f*f+2*(a+b)*(a*d*f+b*h*e)
    old=S.Rational(9,80)+(11*M-2*tau)/8+(100*tau*M-1600*(a*a*A+b*b*B)-1280*(a*a+b*b)*C-640*a*b*C+415*(a*a+b*b)-66*a*b)/320+R
    assert S.expand(invariant-old)==0
    import sys
    from pathlib import Path
    sys.dont_write_bytecode=True
    sys.path.insert(0,str(Path(__file__).resolve().parent/'STRAT10'))
    import frame
    original=frame.formula().subs({frame.a:a,frame.r:b/a,frame.A:A,frame.B:B,frame.C:C,
                                  frame.d:d,frame.e:e,frame.f:f,frame.h:h},simultaneous=True)
    assert S.cancel(original-old)==0
    return True

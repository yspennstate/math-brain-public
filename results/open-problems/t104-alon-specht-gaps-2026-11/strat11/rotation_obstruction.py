"""An exact residual curve flat in the eigenframe rotation direction."""
import sys,os,json
from pathlib import Path
from fractions import Fraction as F
import sympy as S
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'STRAT10'
sys.dont_write_bytecode=True
sys.path.insert(0,str(SOURCE))
import family_certificate as fc
from cells import lower_value,vector_from_record


def build():
    t=fc.s;s=t**4
    U=S.Matrix([-4,1+s,1+s,1-s,1-s]);W=S.Matrix([0,1,-1,-1,1])
    tu=20+4*s*s
    cosine=(tu-t*t)/(tu+t*t)
    Ur=U*cosine+W*tu*t/(tu+t*t)
    Wr=-4*t*U/(tu+t*t)+W*cosine
    assert S.cancel((Ur.T*Ur)[0]-tu)==0
    assert S.cancel((Wr.T*Wr)[0]-4)==0
    assert S.cancel((Ur.T*Wr)[0])==0
    assert S.cancel(sum(Ur))==S.cancel(sum(Wr))==0
    # Equality of projectors also preserves every weight and endpoint chart.
    assert all(S.cancel(Ur[i]*Ur[j]/tu+Wr[i]*Wr[j]/4-U[i]*U[j]/tu-W[i]*W[j]/4)==0
               for i in range(5) for j in range(5))
    A=S.cancel(sum(a**4 for a in Ur)/tu**2)
    B=S.cancel(sum(a**4 for a in Wr)/16)
    C=S.cancel(sum(a*a*b*b for a,b in zip(Ur,Wr))/(4*tu))
    aa=(5+s*s)/(5+10*s-s*s)
    bank=json.loads((SOURCE/'moment_cells.json').read_text())+json.loads((SOURCE/'allN_optimized_cells.json').read_text())
    certificates=[]
    for i,rec in enumerate(bank):
        if F(rec['rlo'])<=1<=F(rec['rhi']):
            value=-lower_value((A,B,C),aa,F(1),vector_from_record(rec))
            certificates.append(fc.cert(value,'rotated negative moment '+str(i)))
    T=s*(1100-335*s+185*s*s+19*s**3+26*s**4-11*s**5)/(4*(s*s+5)*(s*s-10*s-5)**2)
    certificates.append(fc.cert(T,'positive T of rotated family'))
    # ||w(t)-w0||^2 is rational even though the normalized frame has radicals.
    distance2=S.cancel(2*(1-(Wr.T*W)[0]/4))
    assert S.cancel(distance2-4*t*t/(tu+t*t))==0
    certificates.append(fc.cert(distance2-t*t/9,'frame distance squared >= t^2/9'))
    # A relabeled copy tends to a different physical equality point. Removing
    # only one labeled corner cannot create a uniform positive margin.
    far_gap_entry=aa*((1+s)**2/tu+S.Rational(1,4))
    certificates.append(fc.cert(S.Rational(4,5)-far_gap_entry-S.Rational(1,3),
                               'swap vertices 0 and 1: matrix distance from original P0 > 1/3'))
    assert S.limit(T/t**2,t,0)==0
    assert S.limit(distance2/t**2,t,0)==S.Rational(1,5)
    return dict(label='PROVED by verify_rotation.py',parameter='0<t<=1/100',pressure_parameter='s=t^4',
                rotation_cosine=str(cosine),unnormalized_U=list(map(str,Ur)),unnormalized_W=list(map(str,Wr)),
                T=str(T),w_distance_squared=str(distance2),T_over_t_squared_limit='0',
                relabeling_obstruction=dict(permutation=[1,0,2,3,4],gap_00=str(far_gap_entry),
                                           distance_lower='1/3',T_limit='0'),
                certificates=certificates,
                conclusion='The curve remains in (11), has a nonzero pure-rotation tangent, and T=o(frame_distance^2). No positive linear or quadratic bound in full eigenframe distance is possible.')


if __name__=='__main__':
    data=build();(HERE/'rotation_obstruction.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PROVED: exact residual curve with T=o(frame distance squared).')

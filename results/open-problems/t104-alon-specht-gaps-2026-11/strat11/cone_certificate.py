"""Exact premises for the actual Bouligand tangent-cone identification.

The analytic argument is in RESULT.md: strictify a linearized direction,
then avoid the finite union of proper endpoint-disconnection varieties.
"""
import json,itertools
from fractions import Fraction as F
from pathlib import Path
import sympy as S
from frame_jets import build as frame_build


def build():
    data=frame_build()
    names=S.symbols('alpha beta theta p q v z')
    local={str(n):n for n in names}
    strict=[S.Rational(1),S.Rational(1,10),0,S.Rational(1,10),0,0,0]
    values=[S.sympify(rec['linear'],locals=local).subs(dict(zip(names,strict))) for rec in data['active_weights']]
    assert min(values)>0 and strict[1]>0 and 2*strict[0]-strict[1]>0
    # This rational pressure frame is exactly a point of the Cayley chart.
    cayley=F(1,1000)
    s=20*cayley/(20-cayley*cayley)
    cosine=(20-cayley*cayley)/(20+cayley*cayley)
    U=[F(-4),1+s,1+s,1-s,1-s];W=[0,1,-1,-1,1]
    tu=sum(u*u for u in U)
    assert cosine*cosine*tu==20 and 0<s<=F(1,100)
    Ds={(i,j):-2-20*(U[i]*U[j]/tu+F(W[i]*W[j],4)) for i in range(5) for j in range(i+1,5)}
    cuts=[]
    # Unique cuts: the side not containing vertex 4 is a nonempty subset of 0..3.
    for mask in range(1,16):
        side=[i for i in range(4) if mask&(1<<i)]
        crossing=[ij for ij in Ds if (ij[0] in side)!=(ij[1] in side)]
        pairs=[(a,b) for a,b in itertools.combinations(crossing,2) if Ds[a]!=Ds[b]]
        assert pairs
        a,b=pairs[0]
        cuts.append(dict(side=side,edges=[list(a),list(b)],difference=str(Ds[a]-Ds[b])))
    return dict(label='PROVED by verify_cone.py',
                cone='beta>=0 and all eight active weight derivatives in frame_expansion.json >=0; theta free',
                redundant_scale_inequality='2alpha-beta=5*(g01+g02+g03+g04)>=0',
                strict_direction=list(map(str,strict)),strict_weight_derivatives=list(map(str,values)),
                cayley_witness_parameter=str(cayley),pressure_witness_parameter=str(s),
                endpoint_cut_witnesses=cuts,
                density_lemma='A disconnected endpoint has all crossing D_ij equal for some nontrivial cut. Each such equality set is a proper algebraic set in the rational Cayley chart, as witnessed here. Its complement is dense. Strictify any cone direction and perturb by o(t) into that complement. Strict filter inactivity is checked by verify_filters.py.')


if __name__=='__main__':
    Path('tangent_cone_certificate.json').write_text(json.dumps(build(),indent=2)+'\n')
    print('PROVED: strictification and all fifteen proper disconnection varieties certified.')

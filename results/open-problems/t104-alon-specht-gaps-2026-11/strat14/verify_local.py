"""Exact physical local bounds for T5 at both equality types."""
import json
from pathlib import Path
from fractions import Fraction as F
from collar_algebra import BASES,chart,part,local_data,physical_ball_data,tangent,connected_expansion

HERE=Path(__file__).resolve().parent

def replay():
    results={}
    for kind in BASES:
        rr,B,K,S,d,Qn,weights,num=chart(kind)
        local=local_data(kind)
        assert part(num,0)==0
        assert all(sum(row[j] for row in B)==0 for j in range(2))
        assert sum(Qn[i][i] for i in range(5))==2*d
        assert all(sum(Qn[i][j] for j in range(5))==0 for i in range(5))
        assert all(sum(Qn[i][k]*Qn[k][j] for k in range(5))==d*Qn[i][j] for i in range(5) for j in range(5))
        assert all(sum(Qn[i][k]*S[k][j] for k in range(5))==d*S[i][j] for i in range(5) for j in range(5))
        assert sum(weights.values())==1
        from sympy.polys.domains import QQ
        tau=sum(S[i][i]for i in range(5))
        tr2=sum(S[i][j]**2 for i in range(5)for j in range(5))
        diag2=sum(S[i][i]**2 for i in range(5))
        Mn=sum(Qn[i][i]*S[i][i]for i in range(5))
        U=sum(Qn[i][i]*sum(S[i][j]**2 for j in range(5))for i in range(5))
        R1=sum(Qn[i][j]*S[i][j]**2 for i in range(5)for j in range(5))
        R2=sum(Qn[i][i]*S[i][j]*S[j][j]for i in range(5)for j in range(5))
        invariant=(14+2*tau)/9*(Mn-tau*d/5)+QQ(4,3)*tr2*d
        invariant-=QQ(2,3)*diag2*d+4*U
        invariant+=QQ(2,3)*R1+2*R2
        assert invariant==num
        assert sorted(str(part(w,0)) for w in weights.values())==(['0']*8+['1/2']*2 if kind=='edges' else ['0']*7+['1/3']*3)
        # Independently bound the nonlinear error after polynomial cancellation.
        # d has no linear term and d>=d(0), so this bounds T-L directly.
        L,Q,active,gs,A,l=tangent(kind)
        radius=F(local['derivative_cube_radius'])
        def envelope(poly):
            assert all(sum(m)>=2 for m in poly)
            return sum((abs(F(str(c)))*radius**(sum(m)-2) for m,c in poly.items()),F(0))
        alternative=envelope(num-d*L)/F(local['gram_lower'])
        alternative+=sum(F(c)*envelope(weights[ij]-g) for c,ij,g in zip(local['multiplier_caps'],active,gs))
        assert alternative<=local['remainder_rounded']
        assert F(local['collar_radius_l1'])*local['remainder_rounded']<=F(local['linear_norm_c'])/2
        ball=physical_ball_data(kind)
        assert F(ball['matrix_ball_radius'])*ball['extraction_factor']<=F(local['collar_radius_l1'])
        results[kind]=dict(local=local,ball=ball)
        connected_expansion(kind)
        print('PROVED (verify_local.py):',kind,'T5>=',local['conclusion_c'],'*||h||_1; rho=',local['collar_radius_l1'],
              '; T5>=',ball['T_distance_c'],'*||S-S0||_max; epsilon=',ball['matrix_ball_radius'],flush=True)
    assert results==json.loads((HERE/'local_certificates.json').read_text())
    return results

if __name__=='__main__':replay()

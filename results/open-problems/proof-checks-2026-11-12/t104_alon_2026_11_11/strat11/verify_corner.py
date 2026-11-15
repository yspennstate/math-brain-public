"""Replay the invariant identity, rational Farkas and derivative certificates."""
import json
from corner_algebra import tangent_data, remainder_data, matrix_ball_data, verify_invariant_formula, chart, part

def main():
    assert verify_invariant_formula()
    assert json.load(open('tangent_certificate.json'))==dict(label='PROVED by verify_corner.py',**tangent_data())
    data=remainder_data()
    assert json.load(open('remainder_certificate.json'))==dict(label='PROVED by verify_corner.py',**data)
    assert json.load(open('matrix_ball_certificate.json'))==dict(label='PROVED by verify_corner.py',**matrix_ball_data())
    # Verify the normalization and projector identities as polynomial identities.
    rr,B,K,gap,den,Qn,weights,num=chart()
    assert all(sum(b[j] for b in B)==0 for j in range(2))
    assert all(sum(Qn[i][j] for j in range(5))==0 for i in range(5))
    assert sum(Qn[i][i] for i in range(5))==2*den
    assert all(sum(Qn[i][k]*Qn[k][j] for k in range(5))==den*Qn[i][j] for i in range(5) for j in range(5))
    assert all(sum(Qn[i][k]*gap[k][j] for k in range(5))==den*gap[i][j] for i in range(5) for j in range(5))
    assert sum(weights.values())==1
    assert sorted(str(part(w,0)) for w in weights.values())==['0']*8+['1/2']*2
    print('PROVED: exact gap-matrix identity, projector and normalization; 128 rational Farkas certificates, c=1/6.')
    print('PROVED: physical local chart T >= ||h||_1/12, radius = '+data['radius'])
    print('PROVED: matrix ball ||S-S0||_max <= 1/20800: T >= ||S-S0||_max/120.')

if __name__=='__main__':main()

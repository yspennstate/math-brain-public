"""Exact independent check of the load-bearing six-edge mode in w402's proof."""
from fractions import Fraction as F
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent

# Pair (x,y) represents x + i*sqrt(3)*y, not ordinary Cartesian (x,y).
def add(p, q): return p[0] + q[0], p[1] + q[1]
def neg(p): return -p[0], -p[1]
def sub(p, q): return add(p, neg(q))
def scale(p, r): return p[0] * r, p[1] * r
def mul(p, q): return p[0]*q[0] - 3*p[1]*q[1], p[0]*q[1] + p[1]*q[0]
def norm2(p): return p[0]**2 + 3*p[1]**2
def inverse(p): return p[0]/norm2(p), -p[1]/norm2(p)


def main():
    start = time.monotonic()
    gate = json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    cases=[]
    unit=[(F(1),F(0)),(F(1,2),F(1,2)),(F(-1,2),F(1,2)),
          (F(-1),F(0)),(F(-1,2),F(-1,2)),(F(1,2),F(-1,2))]
    for n in gate['peer_mode_N_values']:
        delta=F(1,n)
        vertices=[scale(p,delta) for p in unit]
        edges=[sub(vertices[(j+1)%6],vertices[j]) for j in range(6)]
        modes=[scale(inverse(d),delta) for d in edges]
        residuals=[]
        for j in range(6):
            outgoing=scale(edges[j],F(1,2))
            incoming=scale(neg(edges[(j-1)%6]),F(1,2))
            external=scale(vertices[j],F(1,2))
            assert add(add(outgoing,incoming),external)==(0,0)
            residual=add(mul(outgoing,modes[j]),mul(incoming,modes[(j-1)%6]))
            assert residual==(0,0)
            residuals.append(residual)
            assert norm2(modes[j])==1
            p=add(vertices[j],outgoing)
            q=add(vertices[j],external)
            assert norm2(sub(p,q))==F(3,4)*delta**2
            assert norm2(sub(add((F(1),F(0)),modes[j]),(F(1),F(0))))==1
        assert max(norm2(add((F(1),F(0)),h)) for h in modes)==4
        broken=add(mul(scale(edges[0],F(1,2)),modes[0]),
                   mul(scale(edges[-1],F(1,2)),modes[-1]))
        assert broken==(delta,0) and norm2(broken)>0
        cases.append({'N':n,'six_vertex_residuals':'all exactly zero',
                      'midpoint_distance_squared':str(F(3,4)*delta**2),
                      'field_difference_squared':1,'maximum_field_norm_squared':4,
                      'wrong_incoming_sign_residual':str(delta)})
    assert time.monotonic()-start < gate['wall_seconds_cap']
    result={'command':'python -X utf8 ~/brain_workers/w403/check_peer_mode.py',
            'all_passed':True,'cases':cases,'runtime_seconds':time.monotonic()-start,
            'scope':'Independent exact-rational reproduction of w402 Lemma 2 and Proposition 3; not actual SAW partition sums or formal verification'}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'peer_mode.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()

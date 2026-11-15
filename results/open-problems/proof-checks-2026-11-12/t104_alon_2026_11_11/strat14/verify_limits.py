"""Exact equality witnesses, their original OPEN boxes and physical matrices."""
import json
from pathlib import Path
from fractions import Fraction as F
from quadratic_field import witnesses,evaluate,sign,in_box,encode,ZERO
from exact_bernstein import data,active_constraints

HERE=Path(__file__).resolve().parent

def records():
    target,gs=data()
    inputs=json.loads((HERE/'STRAT8/open_boxes.json').read_text())['boxes']
    out=[]
    for d,p in witnesses():
        assert evaluate(target,p,d)==ZERO
        values={k:evaluate(g,p,d) for k,g in gs.items() if k not in ('scale14','scale_guard')}
        assert all(sign(v,d)>=0 for v in values.values())
        assert values['connected']==ZERO and sign(values['rank'],d)>0 and sign(values['ratio'],d)>0
        hits=[b for b in inputs if in_box(p,b['box'],d)]
        assert hits
        for b in hits:
            assert all(sign(evaluate(g,p,d),d)>=0 for g in active_constraints([tuple(map(F,x))for x in b['box']]).values())
        out.append(dict(radicand=d,point=encode(p),nodes=[b['node']for b in hits]))
    return out

def replay():
    out=records()
    assert json.loads((HERE/'limit_points.json').read_text())['records']==out
    from collar_boxes import point_bank,base_matrix
    bank=point_bank()
    assert len(bank)==9
    for node,info in bank.items():
        base=base_matrix(info['kind'])
        weights=[F(1,5)+base[i][j] for i in range(5) for j in range(i+1,5)]
        assert sorted(weights)==([F(0)]*8+[F(1,2)]*2 if info['kind']=='edges' else [F(0)]*7+[F(1,3)]*3)
    print('PROVED (verify_limits.py): nine exact zero witnesses in original OPEN boxes;',sorted(bank),flush=True)
    print('PROVED (verify_limits.py): strict signed ambient Bernstein certificates are impossible on boxes containing these witnesses.',flush=True)
    return out

if __name__=='__main__':replay()

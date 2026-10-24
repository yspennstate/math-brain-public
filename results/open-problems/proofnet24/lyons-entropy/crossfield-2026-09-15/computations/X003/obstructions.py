"""Exact rational checks for the two stronger shortcuts excluded in X003."""
from pathlib import Path
import json
import sympy as s


def atoms(K):
    n=K.rows
    return [s.Matrix.hstack(*[(K if mask>>j&1 else s.eye(n)-K)[:,j]
                              for j in range(n)]).det() for mask in range(1<<n)]


def main():
    R=s.Rational
    K0=s.Matrix([[R(7,10),-R(3,20)],[-R(3,20),R(87,100)]])
    K1=s.Matrix([[R(21,50),R(19,100)],[R(19,100),R(43,50)]])
    C=(K0+K1)/2;E=(K1-K0)/2
    p=sorted([a*b for a in atoms(K0) for b in atoms(K1)],reverse=True)
    q=sorted(atoms(C.row_join(E).col_join(E.row_join(C))),reverse=True)
    gap=sum(q[:8])-sum(p[:8])
    assert gap==R(3,5000)
    sector_input=[R(1,25),R(4,25),R(4,25)]
    sector_output=[R(17,100),R(17,100),R(1,100),R(1,100)]
    sector_gain=-sum(x*s.log(x) for x in sector_output)+sum(x*s.log(x) for x in sector_input)
    sector_gain=s.expand_log(sector_gain,force=True)
    assert s.simplify(sector_gain-R(17,50)*s.log(R(16,17)))==0
    result=dict(input_top8_sum=str(sum(p[:8])),output_top8_sum=str(sum(q[:8])),
                majorization_violation=str(gap),sector_entropy_gain=str(s.simplify(sector_gain)),
                sector_entropy_gain_numeric=float(sector_gain))
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('obstructions-results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()

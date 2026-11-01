"""Exact check of a generic spectral shortcut obstruction.

This matrix is explicitly NOT a Rossman transfer. It refutes only an
inference from positivity/exchange symmetry/inertia/trace domination.
"""
import json
from fractions import Fraction as Q
from pathlib import Path


def multiply(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def main():
    states = [(i, j) for i in range(3) for j in range(3)]
    B = [[Q(1)-Q(3,20)*(x==y)+Q(17,20)*(x==(y[1],y[0]))
          for y in states] for x in states]
    assert all(v>0 for row in B for v in row)
    assert all(B[i][j]==B[j][i] for i in range(9) for j in range(9))
    assert all(sum(row)==Q(97,10) for row in B)
    power = B
    for _ in range(4):
        power = multiply(power,B)
    trace5 = sum(power[i][i] for i in range(9))
    tail5 = trace5-Q(97,10)**5
    assert tail5 == -Q(43193,20000)
    assert sum(B[i][i]for i in range(9)) == Q(51,5)
    out = {
        'status': 'exact generic shortcut obstruction PASS; not a Rossman matrix',
        'matrix': [[str(v) for v in row] for row in B],
        'eigenvalues': ['97/10']+['7/10']*5+['-1']*3,
        'trace': '51/5',
        'Perron_excluded_trace': '1/2',
        'shortest_tail_pair': '-3/10',
        'Perron_excluded_fifth_moment': str(tail5),
        'actual_exchange_pair_entry': '37/20',
        'maximum_possible_Rossman_exchange_entry_from_diagonal': '17/10',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items()if k!='matrix'},indent=2))


if __name__=='__main__':
    main()

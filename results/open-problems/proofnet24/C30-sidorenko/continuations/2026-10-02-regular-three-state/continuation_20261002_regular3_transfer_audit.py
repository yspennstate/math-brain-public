"""Distinct exact nine-state transfer audit of both three-state cones."""
import json
from collections import Counter
from pathlib import Path
from continuation_20261002_regular3_full_enumeration import (
    multiply, power, linear, encode)


def add_exp(a,b):
    return tuple(a[i]+b[i] for i in range(4))


def main():
    original=json.loads(Path(__file__).with_name(
        'continuation_20261002_regular3_full_enumeration.json').read_text())
    states=[(i,j) for i in range(3) for j in range(3)]
    summaries={}
    for cone in['I','T']:
        vals=([[1,0,0,1],[1,1,0,1],[1,1,1,1],
               [1,1,1,0],[1,1,0,0],[1,0,0,0]] if cone=='I' else
              [[2,0,0,0],[2,2,0,0],[2,2,2,0],
               [2,2,2,1],[2,2,0,1],[2,0,0,1]])
        forms=[linear(v) for v in vals]
        P=[[forms[0],forms[3],forms[4]],
           [forms[3],forms[1],forms[5]],
           [forms[4],forms[5],forms[2]]]
        transfer=[[multiply(multiply(P[i][j],P[i][l]),P[k][j])
                   for k,l in states] for i,j in states]
        total=Counter()
        for start in range(9):
            current=[Counter() for _ in states]
            current[start][(0,0,0,0)]=1
            for _ in range(5):
                nxt=[Counter() for _ in states]
                for i,poly in enumerate(current):
                    for j,shift_poly in enumerate(transfer[i]):
                        for mon,c in poly.items():
                            for shift,d in shift_poly.items():
                                nxt[j][add_exp(mon,shift)]+=c*d
                current=nxt
            total.update(current[start])
        density={a:3**5*v for a,v in total.items() if v}
        assert encode(density)==original['results'][cone]['density']
        summaries[cone]={'complete_density_coefficients_match':True,
                         'density_monomial_count':len(density)}
        print(cone,'complete polynomial matches',flush=True)
    # Natural cycle powers checked directly from the 3x3 operator P.
    cycle=json.loads(Path(__file__).with_name(
        'continuation_20261002_regular3_cycle_surplus.json').read_text())
    for cone in['I','T']:
        vals=([[1,0,0,1],[1,1,0,1],[1,1,1,1],
               [1,1,1,0],[1,1,0,0],[1,0,0,0]] if cone=='I' else
              [[2,0,0,0],[2,2,0,0],[2,2,2,0],
               [2,2,2,1],[2,2,0,1],[2,0,0,1]])
        f=[linear(v) for v in vals]
        P=[[f[0],f[3],f[4]],[f[3],f[1],f[5]],[f[4],f[5],f[2]]]
        X=[[{(0,0,0,0):int(i==j)} for j in range(3)] for i in range(3)]
        s=linear([3,2,1,1] if cone=='I' else[6,4,2,2])
        for n in range(1,7):
            Y=[[Counter() for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):Y[i][j].update(multiply(X[i][k],P[k][j]))
            X=Y
            if n in(4,6):
                tr=Counter()
                for i in range(3):tr.update(X[i][i])
                tr.subtract(power(s,n))
                assert encode(tr)==cycle['results'][cone][f'C{n}_excess']
        summaries[cone]['direct_operator_cycle_excesses_match']=True
    out={'status':'independent exact nine-state transfer and cycle audit PASS',
         'results':summaries}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()

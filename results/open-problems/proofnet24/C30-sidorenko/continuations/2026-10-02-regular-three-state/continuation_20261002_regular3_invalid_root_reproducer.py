"""HISTORICAL INVALID METHOD: not a density proof and not a valid theorem.

Reproduces discarded scratch JSON files without modifying them. It fixes
one vertex to host state0 and multiplies by3, which is INVALID for the
arbitrary regular host family. It is archived to preserve failed-route
provenance. The valid final proof enumerates all ten labels instead.
"""
import itertools
import json
from collections import Counter
from pathlib import Path
from continuation_20261002_regular3_full_enumeration import (
    multiply, power, linear, substitute, encode)


def main():
    edges=[(i,5+j) for i in range(5) for j in range(5)
           if (j-i)%5 in(0,1,4)]
    entry={(0,0):0,(1,1):1,(2,2):2,(0,1):3,(0,2):4,(1,2):5}
    bad_histogram=Counter()
    for other_labels in itertools.product(range(3),repeat=9):
        labels=(0,)+other_labels
        counts=[0]*6
        for u,v in edges:
            i,j=sorted((labels[u],labels[v]))
            counts[entry[i,j]]+=1
        bad_histogram[tuple(counts)]+=3  # THE HISTORICAL INVALID STEP.
    records={}
    for cone in['I','T']:
        vals=([[1,0,0,1],[1,1,0,1],[1,1,1,1],
               [1,1,1,0],[1,1,0,0],[1,0,0,0]] if cone=='I' else
              [[2,0,0,0],[2,2,0,0],[2,2,2,0],
               [2,2,2,1],[2,2,0,1],[2,0,0,1]])
        forms=[linear(v) for v in vals]
        powers={(j,n):power(f,n) for j,f in enumerate(forms) for n in range(16)}
        density=Counter()
        for counts,c in bad_histogram.items():
            T={(0,0,0,0):3**5*c}
            for j,n in enumerate(counts):T=multiply(T,powers[j,n])
            density.update(T)
        gap=Counter(density)
        gap.subtract(power(linear([3,2,1,1] if cone=='I' else[6,4,2,2]),15))
        expected=json.loads(Path(__file__).with_name(
            f'continuation_20261002_regular3_cone_{cone}_exploratory.json').read_text())
        assert encode(gap)==expected['gap']
        records[cone]={'historical_invalid_coefficients_match':True}
        if cone=='I':
            maps=[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,1,1,1]],
                  [[1,0,0,0],[0,1,0,0],[0,0,1,1],[1,1,1,0]],
                  [[1,0,0,0],[0,1,1,0],[0,0,0,1],[1,1,0,0]],
                  [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]]
            for pos,values in enumerate(maps):
                new_gap=substitute(gap,[linear(v) for v in values])
                old=json.loads(Path(__file__).with_name(
                    f'continuation_20261002_regular3_I_order{pos}_exploratory.json').read_text())
                assert encode(new_gap)==old['gap']
                records[cone][f'historical_order{pos}_matches']=True
                if pos==3:
                    # Analytic fourth-cycle trace must have no A*B^11*C^3 term.
                    assert new_gap[(1,11,3,0)]==-2834352
                    records[cone]['quartic_trace_contradiction_coefficient']=-2834352
    out={'status':'discarded INVALID root method reproduced; no theorem claim',
         'reason':'regularity does not imply host vertex transitivity',
         'records':records}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()

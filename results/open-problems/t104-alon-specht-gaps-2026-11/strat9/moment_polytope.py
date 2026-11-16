"""PROVED: rational building blocks for stronger weight-moment cells."""
import itertools
from fractions import Fraction as F


def vertices(enhanced=False,extra=()):
    inequalities = [((-1,0,0),-F(7,30)), ((0,-1,0),-F(7,30)),
        ((1,0,0),F(13,20)), ((0,1,0),F(13,20)), ((0,0,-1),F(0)),
        ((0,0,1),F(3,10)), ((1,0,1),F(4,5)), ((0,1,1),F(4,5)),
        ((1,1,2),F(7,5)), ((-1,-1,2),F(0)),
        ((-1,0,-1),-F(1,4)), ((0,-1,-1),-F(1,4))]
    if enhanced:
        inequalities.append(((-1,-1,-2),-F(4,5)))
        for k,c in [(F(3,2),F(27,25)),(F(2),F(11,8)),
                    (F(3),F(81,40)),(F(4),F(107,40))]:
            inequalities.extend([((k,0,1),c),((0,k,1),c)])
        for k,c in [(F(1),F(5,8)),(F(2),F(51,40)),(F(3),F(77,40))]:
            inequalities.extend([((k,0,-1),c),((0,k,-1),c)])
    inequalities.extend(extra)

    def det(m):
        if not m:
            return F(1)
        return sum((-1)**j*m[0][j]*det([row[:j]+row[j+1:] for row in m[1:]])
                   for j in range(len(m)))
    result = set()
    for ids in itertools.combinations(range(len(inequalities)), 3):
        mat = [list(map(F, inequalities[i][0])) for i in ids]
        divisor = det(mat)
        if not divisor:
            continue
        rhs = [inequalities[i][1] for i in ids]
        v = []
        for j in range(3):
            mm = [row[:] for row in mat]
            for i in range(3):
                mm[i][j] = rhs[i]
            v.append(det(mm)/divisor)
        if all(sum(x*y for x,y in zip(row,v)) <= bound for row,bound in inequalities):
            result.add(tuple(v))
    return sorted(result)


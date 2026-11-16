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


def value(v, a, r, tn, tj, td, tangent, shift, penalties=(0,0,0,0)):
    A, B, C = v
    fm = A+r*B+(1+r)*C
    k = A+B+2*C
    lam = (2+a*(1+r))/4
    ff = fm-(1+r)/5
    base = F(14,9)*ff+a*(2*(1+r)*ff/9+F(4,3)*(1+r*r)
               -F(14,3)*(A+r*r*B)-4*(1+r*r+r/3)*C)
    z = a*(2*tangent*fm-(1+r)*tangent*tangent)
    S = a*(F(9,10)*(1+r)-fm)-F(1,5)
    z1,z2,z3,z4=penalties
    return (base+(tn+tj)*z-lam/5*(tn*(2-k)+tj*(4-k)+2*td)
            +tn*(shift*S-F(1,2)*shift*shift)
            -a*(z1*(A-F(1,5))+z2*(B-F(1,5))+(z3+z4)*C))


def blocks(r, tn, tj, td, penalties=(0,0,0,0)):
    x, y = tn-td, tj+td
    z1,z2,z3,z4=penalties
    return [(F(8,3)-x-y+z1, 1+r-y,
             F(2,3)*r*(r+5)-x*(1+2*r)-y+z2+z4),
            (F(2,3)*(1+5*r)-x*(2+r)-y*r+z1+z3, r*(1+r)-y*r,
             F(8,3)*r*r-x*r-y*r+z2)]


def controls(evaluate, lo, hi):
    left, middle, right = evaluate(lo), evaluate((lo+hi)/2), evaluate(hi)
    return left, 2*middle-(left+right)/2, right


def minimum(evaluate, lo, hi):
    c0 = evaluate(F(0))
    plus, minus = evaluate(F(1)), evaluate(F(-1))
    c1, c2 = (plus-minus)/2, (plus+minus)/2-c0
    vals = [evaluate(lo), evaluate(hi)]
    if c2 > 0:
        x = -c1/(2*c2)
        if lo <= x <= hi:
            vals.append(evaluate(x))
    return min(vals)


def check(rec, verts):
    lo, hi, alo, ahi, tn, tj, td, t, v = [F(rec[k]) for k in
        ('rlo','rhi','alo','ahi','theta_n','theta_j','theta_d','tangent','shift')]
    assert 0 < lo <= hi <= 1 and 0 < alo <= ahi
    assert tn >= 0 and tj >= 0 and td >= 0
    penalties=tuple(map(F,rec.get('penalties',['0']*4)))
    assert len(penalties)==4 and all(x>=0 for x in penalties)
    for i in range(2):
        bernstein = [controls(lambda r: blocks(r,tn,tj,td,penalties)[i][j],lo,hi)
                     for j in range(3)]
        for k in range(3):
            aa, bb, cc = [bernstein[j][k] for j in range(3)]
            assert aa >= 0 and cc >= 0 and aa*cc >= bb*bb
    margin = min(minimum(lambda r: value(p,a,r,tn,tj,td,t,v,penalties),lo,hi)
                 for p in verts for a in (alo,ahi))
    assert margin >= 0
    return margin

from fractions import Fraction
from functools import lru_cache

def calc(rows, cols):
    n = rows*cols
    edges=[]
    for r in range(rows):
        for c in range(cols):
            u=r*cols+c
            if c+1<cols: edges.append((u,u+1))
            if r+1<rows: edges.append((u,u+cols))
    @lru_cache(None)
    def co(S):
        if S==0: return Fraction(1)
        V=[i for i in range(n) if (S//(2**i))%2]
        E=[(u,v) for u,v in edges if u in V and v in V]
        d=2*len(V)+len(E)
        return sum((Fraction(2,d)*co(S-2**v) for v in V), Fraction(0))
    @lru_cache(None)
    def oxy(S):
        if S==0: return Fraction(1)
        V=[i for i in range(n) if (S//(2**i))%2]
        E=[(u,v) for u,v in edges if u in V and v in V]
        d=2*len(V)+len(E)
        return sum((Fraction(1,d)*oxy(S-2**u-2**v) for u,v in E), Fraction(0))
    S=2**n-1
    return co(S), oxy(S)

threshold=Fraction(1,64)
rows=[]
for area in range(1,17):
    for r in range(1,area+1):
        if area%r: continue
        c=area//r
        if r>c: continue
        a,b=calc(r,c)
        rows.append((area,r,c,a,b,a+b))

assert all(s>=threshold for area,r,c,a,b,s in rows if area<=14)
assert calc(3,5)[0]+calc(3,5)[1] < threshold
assert calc(2,8)[0]+calc(2,8)[1] < threshold
assert calc(4,4)[0]+calc(4,4)[1] < threshold
assert calc(3,5)[1] == 0
print('PASS exact R08/E0011 direct-poison rectangle sweep')
print('threshold=1/64')
print('first_rectangle_area_below_threshold=15')
for area,r,c,a,b,s in rows:
    if area>=10:
        print('RECT',r,c,'area',area,'qCO',a,'qO',b,'qsum',s,'float',float(s))

from fractions import Fraction as F

def phi(x,p=5,d=3): return pow(x,d,p)
def vt(t,A,B,p=5,d=3):
    vals={x:phi((t+x)%p,p,d) for x in set(A)|set(B)}
    q=F(0)
    for u in range(1,p):
        good=(all(vals[a]<u for a in A) and all(vals[b]>=u for b in B)) or (all(vals[b]<u for b in B) and all(vals[a]>=u for a in A))
        if good: q += F(p,2*u*(p-u))
    return q

def root(T,W):
    s=[]; b=[]
    for a in range(4):
        A=(a,);B=tuple(x for x in range(4) if x!=a)
        s.append(sum((w*vt(t,A,B) for t,w in zip(T,W)),F(0)))
    for c in range(1,4):
        A=(0,c);B=tuple(x for x in range(4) if x not in A)
        b.append(sum((w*vt(t,A,B) for t,w in zip(T,W)),F(0)))
    return s,b
c072=root(tuple(range(5)),tuple(F(1,5) for _ in range(5)))
c073=root((0,1,2,3),tuple(F(1,4) for _ in range(4)))
c074=root((0,1,3,4),(F(4,15),F(1,3),F(4,15),F(2,15)))
assert c072 == ([F(1,3)]*4,[F(1,6)]*3)
assert c073 == ([F(25,96),F(25,96),F(5,12),F(5,12)],[F(5,24),F(5,24),F(0)])
assert c074 == ([F(7,18),F(13,36),F(5,18),F(5,24)],[F(2,9),F(5,36),F(1,9)])
assert c074 != c072 and c074 != c073
print('C074_PRIORCLASS_EXACT_COMPARE')
print('C072_1v3=',','.join(map(str,c072[0])))
print('C072_2v2=',','.join(map(str,c072[1])))
print('C073_1v3=',','.join(map(str,c073[0])))
print('C073_2v2=',','.join(map(str,c073[1])))
print('C074_1v3=',','.join(map(str,c074[0])))
print('C074_2v2=',','.join(map(str,c074[1])))
print('ALL_EXACT_COMPARISONS_PASS')

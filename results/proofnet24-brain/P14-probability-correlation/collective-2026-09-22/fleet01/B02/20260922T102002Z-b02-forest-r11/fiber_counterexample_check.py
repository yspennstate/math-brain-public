from itertools import combinations
from collections import Counter


def is_forest(n, E):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in E:
        a=find(a); b=find(b)
        if a==b: return False
        p[b]=a
    return True


def disconnected(n,E,u=0,v=1):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in E:
        a=find(a); b=find(b)
        if a!=b: p[b]=a
    return find(u)!=find(v)


def masks(n,E,condition=False):
    ans=[]
    for m in range(1<<len(E)):
        S=[E[i] for i in range(len(E)) if (m>>i)&1]
        if is_forest(n,S) and (not condition or disconnected(n,S)):
            ans.append(m)
    return ans


def rayleigh_and_fibers(n,E,e,f,condition=False):
    F=masks(n,E,condition)
    ie=E.index(e); jf=E.index(f); eb=1<<ie; fb=1<<jf
    C=[[] for _ in range(4)]
    for m in F:
        st=(2 if m&eb else 0)+(1 if m&fb else 0)
        C[st].append(m)
    source=Counter((a&b,a|b) for a in C[0] for b in C[3])
    target=Counter((a&b,a|b) for a in C[2] for b in C[1])
    gap=len(C[2])*len(C[1])-len(C[0])*len(C[3])
    return tuple(map(len,C)),gap,source,target

# Pure K4 obstruction: opposite marks 01 and 23, full-union/empty-intersection fiber.
K4=list(combinations(range(4),2))
counts,gap,S,T=rayleigh_and_fibers(4,K4,(0,1),(2,3),False)
assert counts==(15,9,9,5)
assert gap==6
assert S[(0,63)]==4
assert T[(0,63)]==2
assert sum(T.values())-sum(S.values())==6
fiber_diff=Counter(T[k]-S[k] for k in set(S)|set(T))
assert fiber_diff[-2]==1 and fiber_diff[1]==8

# Connected simple parent witness. g=01; H=G-g. 0 and 1 have no common neighbor,
# so contracting g creates no parallel edge. The offending fiber contracts to K4
# on {g*,2,3,5}; edge 04 is absent from that union.
H=[(0,2),(0,3),(0,4),(1,5),(2,3),(2,5),(3,5)]
countsD,gapD,SD,TD=rayleigh_and_fibers(6,H,(0,2),(3,5),True)
assert countsD==(30,18,18,10)
assert gapD==24
U=(1<<len(H))-1-(1<<H.index((0,4)))
assert SD[(0,U)]==4
assert TD[(0,U)]==2
A=(1<<H.index((0,3)))|(1<<H.index((1,5)))|(1<<H.index((2,3)))
B=(1<<H.index((0,2)))|(1<<H.index((2,5)))|(1<<H.index((3,5)))
assert (A&B,A|B)==(0,U)
for M in (A,B):
    EE=[H[i] for i in range(len(H)) if (M>>i)&1]
    assert is_forest(6,EE) and disconnected(6,EE)

G=[(0,1)]+H
countsG,gapG,_,_=rayleigh_and_fibers(6,G,(0,2),(3,5),False)
assert countsG==(62,42,42,26)
assert gapG==152

print('K4_COUNTS',counts,'GAP',gap,'FULL_FIBER_SOURCE_TARGET',S[(0,63)],T[(0,63)])
print('K4_NONZERO_FIBERS: one deficit -2 and eight surpluses +1; total gap 6')
print('CONNECTED_H_CONDITIONAL_COUNTS',countsD,'GAP',gapD,'BAD_FIBER',SD[(0,U)],TD[(0,U)])
print('SAMPLE_SOURCE_A',[(0,3),(1,5),(2,3)],'B',[(0,2),(2,5),(3,5)])
print('PARENT_G_COUNTS',countsG,'GAP',gapG)
print('STATUS=PASS')

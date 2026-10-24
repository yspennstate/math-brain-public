from functools import lru_cache

V = tuple(range(8))
COVERS = (
    (1,2),(1,6),(2,0),(2,7),(3,0),(3,4),
    (4,7),(5,7),(6,0),(6,4),(6,5),
)

rel = set(COVERS)
changed = True
while changed:
    changed = False
    for a,b in tuple(rel):
        for c,d in tuple(rel):
            if b == c and (a,d) not in rel:
                rel.add((a,d))
                changed = True

pred = {v:{u for u,w in rel if w==v} for v in V}

@lru_cache(None)
def exts(done):
    done=set(done)
    if len(done)==len(V):
        return ((),)
    out=[]
    for v in V:
        if v not in done and pred[v] <= done:
            for tail in exts(tuple(sorted(done|{v}))):
                out.append((v,)+tail)
    return tuple(out)

L=exts(())
E=len(L)

def cmp(a,b):
    if (a,b) in rel: return -1
    if (b,a) in rel: return 1
    return 0

def distinguishers(p,q):
    return tuple(z for z in V if z not in (p,q) and cmp(z,p)!=cmp(z,q))

def count_before(a,b):
    return sum(word.index(a)<word.index(b) for word in L)

assert E == 108
assert distinguishers(6,2) == (4,5)
assert distinguishers(0,7) == (4,5)
assert (6,4) in rel and (6,5) in rel and (4,7) in rel and (5,7) in rel
assert cmp(4,5) == 0
assert count_before(4,5) == 47

print("extensions",E)
print("D_6_2",distinguishers(6,2))
print("D_0_7",distinguishers(0,7))
print("double_fork","6<4,5<7","4||5")
print("count_4_before_5",count_before(4,5),"/",E)
print("POS3_PARTNER_SHARED_SUPPORT_CHECK_PASS")

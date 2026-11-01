from itertools import combinations

# Core poset: disjoint union C2={c1<c2} and C3={y1<x<y3}.
verts = ('c1','c2','y1','x','y3')
relations = {('c1','c2'),('y1','x'),('x','y3'),('y1','y3')}

def is_linear_extension(order):
    pos={v:i for i,v in enumerate(order)}
    return all(pos[a] < pos[b] for a,b in relations)

def shuffles(a,b):
    if not a:
        yield tuple(b); return
    if not b:
        yield tuple(a); return
    for r in shuffles(a[1:],b):
        yield (a[0],)+r
    for r in shuffles(a,b[1:]):
        yield (b[0],)+r

les=list(shuffles(('c1','c2'),('y1','x','y3')))
assert len(les)==10 and all(is_linear_extension(L) for L in les)

def count_before(a,b):
    return sum(L.index(a)<L.index(b) for L in les)

print('core_extensions',len(les))
for a,b in [('c1','y1'),('c1','x'),('c1','y3'),('c2','y1'),('c2','x'),('c2','y3')]:
    n=count_before(a,b)
    print(f'P({a}<{b})={n}/10')

# Contract C2 to z: z is incomparable with the 3-chain. Its position among
# the four gaps is uniform, so z<x in exactly two of four extensions.
q = [
    ('z','y1','x','y3'),
    ('y1','z','x','y3'),
    ('y1','x','z','y3'),
    ('y1','x','y3','z'),
]
qn=sum(L.index('z')<L.index('x') for L in q)
print('quotient_extensions',len(q))
print(f'P_Q(z<x)={qn}/4')
assert qn==2
assert count_before('c1','x')==7
assert count_before('c2','x')==3
assert count_before('c1','y1')==4
assert count_before('y3','c2')==4
print('same_outside_descendants_balanced',False)
print('escape_balanced_pairs','c1||y1','y3||c2')
print('POS3_MODULE_LIFT_COUNTEREXAMPLE_PASS')

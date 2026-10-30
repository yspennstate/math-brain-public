from functools import lru_cache
from fractions import Fraction
from itertools import combinations


def build_poset(m, extra=()):
    labels = ['a','b','x','d','e'] + [f'c{j}' for j in range(1,m+1)]
    idx = {v:i for i,v in enumerate(labels)}
    n = len(labels)
    rel = [[False]*n for _ in range(n)]
    covers = [('a','d'),('a','e'),('b','x'),('b','e'),('x','d')]
    covers += [('b','c1')]
    covers += [(f'c{j}',f'c{j+1}') for j in range(1,m)]
    covers += [(f'c{m}','d')]
    covers += list(extra)
    for u,v in covers:
        rel[idx[u]][idx[v]] = True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j] = True
    if any(rel[i][i] for i in range(n)):
        return labels, idx, None, None
    pred=[]
    for j in range(n):
        mask=0
        for i in range(n):
            if rel[i][j]:
                mask |= 1<<i
        pred.append(mask)
    return labels, idx, rel, pred


def count_extensions(m, extra=()):
    labels, idx, rel, pred = build_poset(m, extra)
    if rel is None:
        return 0
    n=len(labels)
    full=(1<<n)-1
    @lru_cache(None)
    def dp(mask):
        if mask==full:
            return 1
        total=0
        for i in range(n):
            if not ((mask>>i)&1) and (pred[i] & ~mask)==0:
                total += dp(mask | (1<<i))
        return total
    return dp(0)


def incomparable_pairs(m):
    labels, idx, rel, pred = build_poset(m)
    ans=[]
    for i,j in combinations(range(len(labels)),2):
        if not rel[i][j] and not rel[j][i]:
            ans.append((labels[i],labels[j]))
    return ans


def event_count(m,u,v):
    return count_extensions(m, ((u,v),))


def E_formula(m):
    return (m+1)*(m*m+9*m+16)//2


def A_poly(m,j):
    return -(m+3)*j*j + (2*m*m+11*m+13)*j + 2*m*m+8*m+6


def prob_formula(m,u,v):
    B=m*m+9*m+16
    D=(m+1)*B
    def is_c(s):
        return s.startswith('c') and s[1:].isdigit()
    if (u,v)==('a','b') or (u,v)==('d','e'):
        return Fraction(2*(m+3),B)
    if (u,v)==('a','x') or (u,v)==('x','e'):
        return Fraction(2*m*m+19*m+36,3*B)
    if u=='a' and is_c(v):
        j=int(v[1:])
        return Fraction(A_poly(m,j),D)
    if u=='x' and is_c(v):
        j=int(v[1:])
        return Fraction(j,m+1)
    if u=='e' and is_c(v):
        j=int(v[1:])
        return 1-prob_formula(m,'a',f'c{m+1-j}')
    rev=prob_formula(m,v,u) if (v,u)!=(u,v) else None
    if rev is not None:
        return 1-rev
    return None


def width_and_connected(m):
    labels, idx, rel, pred = build_poset(m)
    n=len(labels)
    width=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k<=width:
            continue
        verts=[i for i in range(n) if (mask>>i)&1]
        if all(not rel[i][j] and not rel[j][i] for i,j in combinations(verts,2)):
            width=k
    adj=[set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        if not rel[i][j] and not rel[j][i]:
            adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]-seen:
            seen.add(v); stack.append(v)
    return width, len(seen)==n


def check_autonomous_chain(m):
    labels, idx, rel, pred = build_poset(m)
    C={idx[f'c{j}'] for j in range(1,m+1)}
    outside=set(range(len(labels)))-C
    for z in outside:
        rels={(rel[z][c],rel[c][z]) for c in C}
        if len(rels)!=1:
            return False
    return True


for m in range(1,13):
    E=count_extensions(m)
    assert E==E_formula(m), (m,E,E_formula(m))
    for u,v in incomparable_pairs(m):
        p=Fraction(event_count(m,u,v),E)
        q=prob_formula(m,u,v)
        assert q is not None and p==q, (m,u,v,p,q)

qbal=[]
E1=count_extensions(1)
for u,v in incomparable_pairs(1):
    p=Fraction(event_count(1,u,v),E1)
    if Fraction(1,3)<=p<=Fraction(2,3):
        qbal.append((u,v,p))
assert qbal==[('x','c1',Fraction(1,2))], qbal

m=12
E=count_extensions(m)
width,connected=width_and_connected(m)
assert width==3 and connected and check_autonomous_chain(m)
rows=[]
for u,v in incomparable_pairs(m):
    num=event_count(m,u,v)
    p=Fraction(num,E)
    rows.append((u,v,num,p,Fraction(1,3)<=p<=Fraction(2,3)))
assert len(rows)==40

for m in range(7,101):
    for j in (1,m):
        for u in ('a','x','e'):
            p=prob_formula(m,u,f'c{j}')
            assert not (Fraction(1,3)<=p<=Fraction(2,3)), (m,u,j,p)

def all_formula_pairs(m):
    ans=[('a','b',prob_formula(m,'a','b')),('a','x',prob_formula(m,'a','x')),
         ('x','e',prob_formula(m,'x','e')),('d','e',prob_formula(m,'d','e'))]
    for j in range(1,m+1):
        for u in ('a','x','e'):
            ans.append((u,f'c{j}',prob_formula(m,u,f'c{j}')))
    return ans

def first_depth(m):
    depths=[]
    for u,v,p in all_formula_pairs(m):
        if Fraction(1,3)<=p<=Fraction(2,3) and v.startswith('c'):
            j=int(v[1:]); depths.append(min(j,m+1-j))
    return min(depths)

print('POS3_CORRIDOR_DEPTH_CERTIFICATE_PASS')
print('quotient_m1_extensions',E1)
for u,v in incomparable_pairs(1):
    p=prob_formula(1,u,v)
    print(f'quotient {u}<{v} {p.numerator}/{p.denominator}', 'BALANCED' if Fraction(1,3)<=p<=Fraction(2,3) else 'unbalanced')
print('family_formula E_m=(m+1)(m^2+9m+16)/2')
print('family_formula P(a<b)=P(d<e)=2(m+3)/(m^2+9m+16)')
print('family_formula P(a<x)=P(x<e)=(2m^2+19m+36)/(3(m^2+9m+16))')
print('family_formula P(x<c_j)=j/(m+1)')
print('family_formula P(a<c_j)=A_m(j)/((m+1)(m^2+9m+16))')
print('family_formula A_m(j)=-(m+3)j^2+(2m^2+11m+13)j+2m^2+8m+6')
print('family_formula P(e<c_j)=1-P(a<c_{m+1-j})')
print('m12 width',width,'connected',connected,'autonomous_chain',check_autonomous_chain(12),'extensions',E,'incomparable_pairs',len(rows))
for u,v,num,p,bal in rows:
    print(f'm12 {u}<{v} {num}/{E} = {p.numerator}/{p.denominator}', 'BALANCED' if bal else 'unbalanced')
for m in (7,12,30,60,120):
    print('first_balanced_module_depth',m,first_depth(m))

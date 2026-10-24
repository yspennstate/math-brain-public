from itertools import combinations
from fractions import Fraction

QWORDS=[
 ('a','x','d','e'),
 ('a','x','e','d'),
 ('a','e','x','d'),
 ('x','a','d','e'),
 ('x','a','e','d'),
]

def weight_by_interleaving(m,qword):
    I=['b']+[f'c{j}' for j in range(1,m+1)]
    n=len(I)+len(qword)
    ans=0
    for chosen in combinations(range(n),len(I)):
        chosen=set(chosen); ii=iter(I); qq=iter(qword); word=[]
        for k in range(n):
            word.append(next(ii) if k in chosen else next(qq))
        p={v:i for i,v in enumerate(word)}
        if p['b']<p['x'] and p['b']<p['e'] and p[f'c{m}']<p['d']:
            ans+=1
    return ans

def formulas(m):
    return [
      (m+1)*(m+4)//2,
      (m+1)*(m+2)*(m+6)//6,
      (m+1)*(m+2)*(m+6)//6,
      (m+1)*(m+2)//2,
      (m+1)*(m+2)*(m+3)//6,
    ]

def E(m):
    return (m+1)*(m*m+9*m+16)//2

for m in range(1,13):
    got=[weight_by_interleaving(m,q) for q in QWORDS]
    want=formulas(m)
    assert got==want,(m,got,want)
    assert sum(got)==E(m)

m=12
w=formulas(m); total=sum(w)
def event(q,u,v): return q.index(u)<q.index(v)
for pair in [('a','x'),('d','e'),('x','e')]:
    u,v=pair
    nu=Fraction(sum(event(q,u,v) for q in QWORDS),5)
    mu=Fraction(sum(wi for wi,q in zip(w,QWORDS) if event(q,u,v)),total)
    print(f'{u}<{v}: nu={nu.numerator}/{nu.denominator} mu={mu.numerator}/{mu.denominator}')
print('POS3_IDEAL_BLOCK_PROJECTION_PASS')
print('m12_weights',*w,'sum',total)
print('weight_formulas')
print('w1=(m+1)(m+4)/2')
print('w2=w3=(m+1)(m+2)(m+6)/6')
print('w4=(m+1)(m+2)/2')
print('w5=(m+1)(m+2)(m+3)/6')

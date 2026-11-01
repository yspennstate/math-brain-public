import sympy as s
from itertools import product
from collections import defaultdict
from fractions import Fraction
states=list(product([0,1],repeat=4))
G=[(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)]
a,t=s.symbols('a t',real=True)
p=[s.Rational(1,2)+a+t,s.Rational(1,2)+a-t,s.Rational(1,2)-a+t,s.Rational(1,2)-a-t]
raw={st:s.prod(p[i] if st[i] else 1-p[i] for i in range(4)) for st in states}
y={st:s.factor(sum(raw[tuple(st[j] for j in g)] for g in G)/4) for st in states}
groups=defaultdict(list)
for st in states:groups[str(y[st])].append(st)
for f,sts in groups.items():
 expr=y[sts[0]]
 print(sts,expr,'base=',s.factor(expr.subs(t,0)),'second=',s.factor(s.diff(expr,t,2).subs(t,0)))
curv=s.expand(-sum(s.diff(f,t,2).subs(t,0)*s.log(f.subs(t,0)) for f in y.values()))
print('CURV',s.simplify(curv))
print('AT 1/4',s.simplify(curv.subs(a,s.Rational(1,4))),s.N(curv.subs(a,s.Rational(1,4)),30))

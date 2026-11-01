from itertools import combinations
from sympy import Matrix, Rational, sqrt, simplify, N, E

r = Rational
U = Matrix([
    [2/sqrt(5), 0, 0],
    [0, 2/sqrt(5), 0],
    [1/(2*sqrt(5)),  1/(2*sqrt(5)),  r(1,2)],
    [1/(2*sqrt(5)), -1/(2*sqrt(5)), r(1,2)],
    [1/(2*sqrt(5)),  1/(2*sqrt(5)), -r(1,2)],
    [1/(2*sqrt(5)), -1/(2*sqrt(5)), -r(1,2)],
])
assert simplify(U.T*U) == Matrix.eye(3)
P = simplify(U*U.T)
assert simplify(P*P-P) == Matrix.zeros(6)

inds = range(6)
def w(S,T):
    return simplify(P.extract(S,T).det()**2)

triples = list(combinations(inds,3))
E3 = simplify(sum(w(S,T) for S in triples for T in triples))
assert E3 == 1

F3 = [(S,T) for S in triples for T in triples
      if {0,1}.issubset(S) and {0,1}.issubset(T)]
Z3 = simplify(sum(w(S,T) for S,T in F3))
assert Z3 == r(256,625)
m3 = [simplify(sum(w(S,T) for S,T in F3 if i in S)/Z3) for i in inds]
assert m3 == [1,1,r(1,4),r(1,4),r(1,4),r(1,4)]

pairs = list(combinations(inds,2))
F20 = [(S,T) for S in pairs for T in pairs if 0 not in S and 0 not in T]
F21 = [(S,T) for S in pairs for T in pairs if 1 not in S and 1 not in T]
E20 = simplify(sum(w(S,T) for S,T in F20))
E21 = simplify(sum(w(S,T) for S,T in F21))
assert E20 == E21 == r(27,25)
m20 = [simplify(sum(w(S,T) for S,T in F20 if i in S)/E20) for i in inds]
m21 = [simplify(sum(w(S,T) for S,T in F21 if i in S)/E21) for i in inds]
assert m20 == [0,r(104,135),r(83,270),r(83,270),r(83,270),r(83,270)]
assert m21 == [r(104,135),0,r(83,270),r(83,270),r(83,270),r(83,270)]

# Half allocate each residual family. Overlap terms then have total allocation one.
for S in pairs:
    for T in pairs:
        total = r(1,2)*int((S,T) in F20) + r(1,2)*int((S,T) in F21)
        assert total <= 1
Z20 = E20/2
Z21 = E21/2
assert Z20 == Z21 == r(27,50)

t3 = r(31,166)
t2 = r(135,332)
assert t3 + 2*t2 == 1
s = simplify(3*t3 + 4*t2)
assert s == r(363,166)
mix = [simplify(t3*m3[i] + t2*m20[i] + t2*m21[i]) for i in inds]
assert mix == [r(1,2),r(1,2),r(197,664),r(197,664),r(197,664),r(197,664)]
assert sum(mix) == s

q = 1
C = (E*s/(s-2*q)) * (t3**t3 * t2**(2*t2))**(r(1,2)/s) \
    * Z3**(-t3/(2*s)) * Z20**(-t2/(2*s)) * Z21**(-t2/(2*s))
print('P =', P)
print('E3 =', E3)
print('Z3 =', Z3, 'm3 =', m3)
print('raw E20,E21 =', E20, E21, 'allocated =', Z20, Z21)
print('m20 =', m20)
print('m21 =', m21)
print('weights =', t3, t2, t2, 's =', s, 'mixed =', mix)
print('C =', N(C,30))
assert N(C,20) < r(29199,1000)

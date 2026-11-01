from fractions import Fraction as F

# Nontrivial rational orthonormal pair.
u=(F(1,3),F(2,3),F(2,3))
v=(F(2,3),F(-2,3),F(1,3))
n=3

a=[z*z for z in u]
b=[z*z for z in v]
w={(i,j):(u[i]*v[j]-u[j]*v[i])**2 for i in range(n) for j in range(i+1,n)}

# Exact directed split supplied by the theorem / max-flow construction.
x={(0,1):F(1,9),(1,0):F(1,3),
   (0,2):F(0),(2,0):F(1,9),
   (1,2):F(1,9),(2,1):F(1,3)}

assert sum(a)==sum(b)==F(1)
assert sum(u[i]*v[i] for i in range(n))==0
assert sum(w.values())==1

for i in range(n):
    assert sum(w[min(i,j),max(i,j)] for j in range(n) if j!=i)==a[i]+b[i]
    assert sum(x[i,j] for j in range(n) if j!=i)==a[i]
    assert sum(x[j,i] for j in range(n) if j!=i)==b[i]

for (i,j),wij in w.items():
    assert x[i,j]+x[j,i]==wij

for mask in range(1,1<<n):
    S={i for i in range(n) if (mask>>i)&1}
    if len(S)==n:
        continue
    A=sum(a[i] for i in S)
    B=sum(b[i] for i in S)
    C=sum(w[i,j] for (i,j) in w if (i in S)^(j in S))
    assert abs(A-B)<=C
    print('cut', tuple(sorted(S)), A, B, C)

print('u =',u)
print('v =',v)
print('a =',a)
print('b =',b)
print('w =',w)
print('x =',x)
print('ALL_EXACT_CHECKS_PASS')

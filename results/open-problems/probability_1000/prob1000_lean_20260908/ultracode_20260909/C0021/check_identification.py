# The two identifications the bounds rest on, checked on small cases by brute force.
# (1) revealment(f) = D_k / 3^k. Sanity: k=1 gives 5/6, the known answer to Exercise VIII.1.
# (2) total influence I(f) = (3/2)^k, so Theorem VIII.6 gives delta >= I^2/n = (3/4)^k.  Brute force at k=2.
import itertools
from fractions import Fraction
from dp_exact import V, full
print("D_1/3 =", V(full(1))/3, "(known revealment of MAJ3: 5/6)")
def maj3(a,b,c): return 1 if a+b+c>0 else -1
def f2(x): return maj3(maj3(*x[0:3]),maj3(*x[3:6]),maj3(*x[6:9]))
I=Fraction(0)
for i in range(9):
    piv=0
    for x in itertools.product((-1,1),repeat=9):
        y=list(x); y[i]=-y[i]
        if f2(x)!=f2(y): piv+=1
    I+=Fraction(piv,2**9)
print("total influence at k=2 by brute force:", I, "= (3/2)^2 =", Fraction(9,4))
print("Theorem VIII.6 bound at k=2: delta >= I^2/n =", I*I/9, "= (3/4)^2 =", Fraction(9,16))
print("optimal revealment at k=2: D_2/9 =", V(full(2))/9, float(V(full(2))/9), " >= 9/16 =", 9/16, "OK" if V(full(2))/9 >= Fraction(9,16) else "VIOLATION")
print("optimal revealment at k=3: D_3/27 =", float(V(full(3))/27), " >= (3/4)^3 =", (3/4)**3)

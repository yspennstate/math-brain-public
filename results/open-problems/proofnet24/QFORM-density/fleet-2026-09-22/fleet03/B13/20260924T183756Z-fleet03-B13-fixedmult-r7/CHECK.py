from fractions import Fraction as F

d=F(2,35)
p=F(1,400)
h=F(13,148)
q2=d*d+p
qb=F(789,10360)
assert qb*qb-q2==F(3733,107329600)>0
assert 1-d-qb-4*h==F(5339,10360)>0
assert 1-d-2*qb-9*h==0
assert F(30,1)/h==F(4440,13)<342

# scalar/no-pivot branch: square to avoid floating point
assert F(14**2)*F(2,1)/h/d < 342**2

# scalar/pair branch = 16 sqrt(350)
assert F(16**2)*350 < 342**2

# rigorous log(125/14) < 219/100 via e^x Taylor lower bound
x=F(219,100)
term=F(1)
S=term
for k in range(1,9):
    term=term*x/k
    S+=term
assert S>F(125,14)

Bup=F(12)+F(22,7)+F(219,50)
assert Bup==F(6833,350)
nested=Bup/d
assert nested==F(6833,20)<342

print("qbound_gap",qb*qb-q2)
print("no_pivot",F(30,1)/h)
print("nested_scalar",nested)
print("QFORM_B13_R7_342_CHECK_PASS")

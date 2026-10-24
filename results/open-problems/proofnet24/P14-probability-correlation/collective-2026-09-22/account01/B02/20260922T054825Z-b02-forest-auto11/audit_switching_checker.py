from fractions import Fraction


def det3(M):
    a,b,c=M[0]
    d,e,f=M[1]
    g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

# K3. Rank-degree homogenization h=y^2+y(z1+z2+z3)+z1z2+z1z3+z2z3.
# At the all-ones point, grad(h)grad(h)^T-h Hess(h), on (y,z1,z2):
rank_block=[[11,8,8],[8,9,2],[8,2,9]]
assert det3(rank_block)==-49

# Source-valid ground-set-degree homogenization is y*h for K3 (ground set size 3).
ground_block=[[60,8,8],[8,9,2],[8,2,9]]
assert det3(ground_block)==3724

# Exact failure of the rank-slack A2 inequality claimed in the lead report.
mu=Fraction(9,7)
v=Fraction(24,49)
R=2
p=Fraction(3,7)
c=Fraction(8,49)
a2_lhs=v*v/(R-mu)+3*c*c/p
assert a2_lhs==Fraction(128,245)
assert a2_lhs-v==Fraction(8,245)>0
assert v-mu*(R-mu)/R==Fraction(3,98)>0

# Abstract three-bit count witness showing endpoint/unit pairwise NC alone does not imply
# safety after doubling the g activity. Columns are (ef)=(00,10,01,11).
g0=(4,7,9,9)
g1=(6,4,0,0)
a0,b0,c0,d0=g0
a1,b1,c1,d1=g1
A=b0*c0-a0*d0
B=b0*c1+b1*c0-a0*d1-a1*d0
C=b1*c1-a1*d1
assert (A,B,C)==(27,-18,0)
q=lambda t:A+B*t+C*t*t
assert (q(0),q(1),q(2))==(27,9,-9)
# Unit pair gaps for (e,g) and (f,g).
gap_eg=(b0+d0)*(a1+c1)-(a0+c0)*(b1+d1)
gap_fg=(c0+d0)*(a1+b1)-(a0+b0)*(c1+d1)
assert gap_eg==44
assert gap_fg==180

print('K3_rank_block_det',det3(rank_block))
print('K3_ground_block_det',det3(ground_block))
print('K3_rank_A2_lhs',a2_lhs,'rhs',v,'excess',a2_lhs-v)
print('K3_rank_variance_bound_excess',v-mu*(R-mu)/R)
print('abstract_gap_polynomial',A,B,C,'values',q(0),q(1),q(2))
print('abstract_unit_pair_gaps',q(1),gap_eg,gap_fg)
print('STATUS=PASS')

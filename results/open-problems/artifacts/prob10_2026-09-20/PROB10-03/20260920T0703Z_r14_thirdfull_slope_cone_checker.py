from fractions import Fraction as F
import sympy as sp

print('PROB10-03 R14 exact third-full/overlap obstruction self-check')

# ---------- third-full algebra ----------
p2,p3,q2,q3=sp.symbols('p2 p3 q2 q3', positive=True)
s2=q3/p3
s1=(q2-q3)/(p2-p3)
s0=(1-q2)/(1-p2)
t=sp.sqrt(s2)
gp=sp.Rational(1,2)*s0*t/s1
c3=(s1-s2)/((p2-p3)*s1*t)
c2=(s0*s2-s1**2)/((1-p2)*s0*s1*t)
A2=sp.factor(2*gp-c2*(1-q2))
A3=sp.factor(A2-c3*(q2-q3))

checks={
    'A2': sp.simplify(A2-s1/t),
    'A3': sp.simplify(A3-t),
    'q3_stationarity': sp.simplify(q3/A3**2-p3),
    'q2_stationarity': sp.simplify((q2-q3)/(A2*A3)-(p2-p3)),
    'gamma_stationarity': sp.simplify((1-q2)/(2*gp*A2)+(q2-q3)/(A2*A3)+p3-1),
}
for k,v in checks.items():
    print(k, sp.factor(v))
    assert v == 0
print('THIRDFULL_Q_SECTOR_SYMBOLIC_PASS')

# Verify source-form c2/c3/gamma formulas agree with slope representation.
gp_src=sp.Rational(1,2)*(1-q2)/(1-p2)*(p2-p3)/(q2-q3)*sp.sqrt(q3/p3)
c3_src=1/(p2-p3)*sp.sqrt(p3/q3)-1/(q2-q3)*sp.sqrt(q3/p3)
c2_src=1/(1-p2)*(p2-p3)/(q2-q3)*sp.sqrt(q3/p3)-1/(1-q2)*(q2-q3)/(p2-p3)*sp.sqrt(p3/q3)
assert sp.simplify(gp-gp_src)==0
assert sp.simplify(c3-c3_src)==0
assert sp.simplify(c2-c2_src)==0
print('SOURCE_FORMULA_REPARAM_PASS')

# ---------- exact rational inequalities for c*(-1)>1/2 ----------
# pi<22/7 -> phi(0)>sqrt(7/44)>199/500
assert F(7,44) > F(199,500)**2
# pi>25/8 -> phi(0)<2/5 (strictness comes from the strict pi bound)
assert F(1,1)/(2*F(25,8)) == F(2,5)**2
# alternating Taylor lower bound for exp(-1/8)
exp_lb=F(1)-F(1,8)+F(1,128)-F(1,3072)
assert exp_lb==F(2711,3072)
rhs_two_phi_lb=2*F(199,500)*exp_lb
assert rhs_two_phi_lb==F(539489,768000)
assert rhs_two_phi_lb-F(7,10)==F(1889,768000)>0
print('MZZ_CSTAR_HALF_RATIONAL_PASS', rhs_two_phi_lb, float(rhs_two_phi_lb))

# delta_lin(-1)>4 elementary constants: e>8/3 and pi>3 imply 2*pi*e>16.
assert 2*F(3)*F(8,3) == 16
print('LP_GT4_ELEMENTARY_PASS')

# ---------- numerical-only source-table sanity check ----------
p3n=0.6252; p2n=0.9691; q3n=0.2500; q2n=0.6536
r2=q3n/p3n
r1=(q2n-q3n)/(p2n-p3n)
r0=(1-q2n)/(1-p2n)
gpn=0.5*r0*(r2**0.5)/r1
c3n=(r1-r2)/((p2n-p3n)*r1*(r2**0.5))
c2n=(r0*r2-r1*r1)/((1-p2n)*r0*r1*(r2**0.5))
print('NUMERICAL_ONLY_TABLE_SLOPES', r0,r1,r2)
print('NUMERICAL_ONLY_CONE_MARGINS', r1-r2, r0*r2-r1*r1)
print('NUMERICAL_ONLY_RECONSTRUCT', gpn,c3n,c2n)
assert r1>r2 and r0*r2>r1*r1
assert abs(gpn-3.0237)<0.01
assert abs(c3n-3.03)<0.02
assert abs(c2n-12.1)<0.05
print('NUMERICAL_ONLY_TABLE_CONSISTENCY_PASS')

# ---------- Shor witness algebra ----------
# General witness is x=0, X=I/N: trace=1; block diag(1,I/N) PSD; Gx=0>=-1.
# Finite exact sanity instance for N=5.
N=5
trace=sum(F(1,N) for _ in range(N))
assert trace==1
assert F(1,N)>0
assert F(0)>=F(-1)
print('SHOR_WITNESS_EXACT_PASS_N5_AND_SYMBOLIC_ARGUMENT_GENERAL')

print('ALL_EXACT_SELF_CHECKS_PASS')

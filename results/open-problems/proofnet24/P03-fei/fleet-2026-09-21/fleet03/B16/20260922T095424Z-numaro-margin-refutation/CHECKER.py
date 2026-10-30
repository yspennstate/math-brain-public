from fractions import Fraction as F

# Exact source data inherited from the source-checked strong Numaro witness.
p = F(223,456)
alpha = F(57,256)
alpha_other_sum = F(465,256)
pout = F(1019,2048)
c0 = F(33525607,125000000)  # 0.268204856
C0 = F(64548,10000)         # 6.4548

V = lambda x: 4*x*(1-x)

# Independent exact checks of the one-core output and Poincare denominator.
assert F(1,2) - alpha*(F(1,2)-p) == pout
V1 = V(p)
I = alpha*V1 + alpha_other_sum
Vout = V(pout)
Q = (I - Vout)/4

assert V1 == F(51959,51984)
assert I == F(476039,233472)
assert Vout == F(1048551,1048576)
assert Q == F(62098577,239075328)
assert Q > 0

# The peer's rigorous logarithmic enclosure is much tighter; these deliberately
# coarse rational bounds are enough for the theorem in REPORT.md:
#       -0.038024 < D_{Gamma^dagger} < -0.038023.
deficit_lo = F(38023,10**6)
deficit_hi = F(38024,10**6)

# Gamma^dagger = Gamma_0 + c0*p(1-p), and adding c*p(1-p)
# changes the gate defect by c*Q. Hence c_G = c0 - D_dagger/Q.
cG_lo = c0 + deficit_lo/Q
cG_hi = c0 + deficit_hi/Q

assert cG_lo == F(3218187637329239,7762322125000000)
assert cG_hi == F(3218217521745239,7762322125000000)
assert cG_lo > F(1,100)  # certified c=0.01 pays every AND/OR read-once gate

# Scalar-variance repair center if one insisted on this one-parameter repair.
Cscalar_lo = C0 + cG_lo/4
Cscalar_hi = C0 + cG_hi/4
assert Cscalar_lo == F(203635135047129239,31049288500000000)
assert Cscalar_hi == F(203635164931545239,31049288500000000)

print('PASS')
print('p', p, 'pout', pout)
print('alpha1', alpha, 'alpha_other_sum', alpha_other_sum)
print('V1', V1)
print('I', I)
print('Vout', Vout)
print('Q', Q, float(Q))
print('cG_lower', cG_lo, format(float(cG_lo), '.16f'))
print('cG_upper', cG_hi, format(float(cG_hi), '.16f'))
print('rigorous_ratio_vs_AND_c001_lower', format(float(cG_lo/F(1,100)), '.12f'))
print('scalar_center_lower', Cscalar_lo, format(float(Cscalar_lo), '.15f'))
print('scalar_center_upper', Cscalar_hi, format(float(Cscalar_hi), '.15f'))

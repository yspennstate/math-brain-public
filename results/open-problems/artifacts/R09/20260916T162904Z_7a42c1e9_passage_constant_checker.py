from fractions import Fraction
# Published rigorous site-percolation lower bound p_c(Z^3)>0.2522 is used analytically.
p0=Fraction(1261,5000)          # 0.2522
delta0=Fraction(1,1000)        # 0.001
xmin=p0-delta0                 # 0.2512
C=Fraction(1153,1000)          # 1.153
# Psi'(x)=1/(2 sqrt(x(1-x))). For x in [xmin,1/2], Psi' is decreasing.
# Verify Psi'(xmin)<C without floating point: 1 < 4*xmin*(1-xmin)*C^2.
cert=4*xmin*(1-xmin)*C*C
assert cert>1
print('p0',p0)
print('delta0',delta0)
print('xmin',xmin)
print('C',C)
print('4*xmin*(1-xmin)*C^2',cert)
print('certificate Psi_prime(xmin)<C: TRUE')
# Exact l1-ball count formula self-check for first 100 radii.
def brute(L):
    return sum(1 for x in range(-L,L+1) for y in range(-L,L+1) for z in range(-L,L+1) if abs(x)+abs(y)+abs(z)<=L)
def formula(L):
    return (4*L**3+6*L**2+8*L+3)//3
for L in range(0,101): assert brute(L)==formula(L)
print('l1_ball_formula_checked_L_0_to_100: TRUE')
print('PASS')

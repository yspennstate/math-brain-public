from fractions import Fraction
import mpmath as mp

mp.mp.dps = 70

# --- Exact Hadamard source ---
H0 = [
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
    [1, 1, 1, 1],
]

def dot(a,b):
    return sum(Fraction(x,2)*Fraction(y,2) for x,y in zip(a,b))

for i in range(4):
    for j in range(4):
        assert dot(H0[i], H0[j]) == (1 if i == j else 0)

D = [1,1,-1,0]
A = [[sum(Fraction(H0[k][i],2)*D[k]*Fraction(H0[k][j],2)
          for k in range(4)) for j in range(4)] for i in range(4)]
A_expected = [
    [Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(-3,4)],
    [Fraction(1,4), Fraction(1,4), Fraction(-3,4), Fraction(1,4)],
    [Fraction(1,4), Fraction(-3,4), Fraction(1,4), Fraction(1,4)],
    [Fraction(-3,4), Fraction(1,4), Fraction(1,4), Fraction(1,4)],
]
assert A == A_expected

# For z in [1/2,1], f_Z(z)=8/3 (1-z)^3 and conditional cap is reciprocal.
def fz(z):
    z = mp.mpf(z)
    return mp.mpf(8)/3*(1-z)**3

for z in ['0.5','0.75','0.9','0.99']:
    assert fz(z) > 0
assert 1/fz('0.99') > 10**5
assert 1/fz('0.999') > 10**8

# --- Six-variable fully shared spectral stress ---
sqrt = mp.sqrt
pi = mp.pi

a = 1 + sqrt(2)
t1 = mp.tan(pi/24)
t2 = 1/sqrt(3)
c = 7*sqrt(3)/4
d = (9*sqrt(6)+17*sqrt(3))/8
e = (2*sqrt(6)+3*sqrt(3))/4

def L(t):
    return mp.log((t+a)/(a-t))

def Fplus(t):
    return (c*L(t)
            + d*(1/(t-a)+1/(t+a))
            + (e/2)*(1/(t-a)**2-1/(t+a)**2))

c0 = sqrt(3)/12
dm = (9*sqrt(3)+5*sqrt(6)-4*sqrt(2)-8)/8
dp = (9*sqrt(3)+5*sqrt(6)+4*sqrt(2)+8)/8

def Fminus(t):
    return (-c0*L(t)
            - dm/(t-a) - dp/(t+a)
            - e/(2*(t-a)**2) + e/(2*(t+a)**2))

p_closed = 12*((Fplus(t1)-Fplus(0)) + (Fminus(t2)-Fminus(t1)))

u = [sqrt(mp.mpf(2)/3), -1/sqrt(6), -1/sqrt(6)]
v = [0, 1/sqrt(2), -1/sqrt(2)]
n = [1/sqrt(3)]*3

def Jsheet(theta, sign):
    aa = [u[i]*mp.cos(theta)+v[i]*mp.sin(theta)+sign*n[i] for i in range(3)]
    b = [abs(x) for x in aa]
    M = max(b)
    e1 = sum(b)
    e2 = b[0]*b[1]+b[0]*b[2]+b[1]*b[2]
    e3 = b[0]*b[1]*b[2]
    return 1/M - e1/(2*M**2) + e2/(3*M**3) - e3/(4*M**4)

# Independent quadrature, segmented to avoid sign/max kinks.
N = 72
pts = [2*pi*k/N for k in range(N+1)]
p_quad = mp.mpf('0')
for sign in (1,-1):
    for k in range(N):
        p_quad += mp.quad(lambda th: Jsheet(th, sign), [pts[k],pts[k+1]])

partner = mp.mpf(91)/36 + (mp.mpf(13)/6)*mp.log(2)
ceiling = 3*sqrt(2)

assert abs(p_closed-p_quad) < mp.mpf('1e-45')
assert p_closed > partner
assert p_closed < ceiling

print('PASS')
print('conditional_cap_z=0.99 =', mp.nstr(1/fz('0.99'), 30))
print('conditional_cap_z=0.999 =', mp.nstr(1/fz('0.999'), 30))
print('p_balanced =', mp.nstr(p_closed, 60))
print('p_quad_check =', mp.nstr(p_quad, 60))
print('partner =', mp.nstr(partner, 60))
print('gain =', mp.nstr(p_closed-partner, 60))
print('3sqrt2 =', mp.nstr(ceiling, 60))
print('gap =', mp.nstr(ceiling-p_closed, 60))

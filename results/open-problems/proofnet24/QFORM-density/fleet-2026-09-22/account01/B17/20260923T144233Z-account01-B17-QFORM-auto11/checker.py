import sympy as sp
from mpmath import iv

# Exact physical matrix for the six-coordinate witness.
M = sp.Matrix([
[1,1,-2,-2,-2,-2],
[1,1,-2,-2,-2,-2],
[-2,-2,1,1,-2,-2],
[-2,-2,1,1,-2,-2],
[-2,-2,-2,-2,1,1],
[-2,-2,-2,-2,1,1],
])
A = M/6
assert A.rank() == 3
assert sorted(A.eigenvals().keys()) == [-1,0,1]
assert A.eigenvals()[sp.Integer(1)] == 2
assert A.eigenvals()[sp.Integer(-1)] == 1
assert A.eigenvals()[sp.Integer(0)] == 3
assert all(x != 0 for x in A)

# Half-angle rational integrands in the two sign cells.
t = sp.symbols('t', real=True)
s2,s3,s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
c = 1+s2
Jp = (-7*s3/(4*(t-c))
      -(9*s6+17*s3)/(8*(t-c)**2)
      -(2*s6+3*s3)/(4*(t-c)**3)
      +7*s3/(4*(t+c))
      -(9*s6+17*s3)/(8*(t+c)**2)
      +(2*s6+3*s3)/(4*(t+c)**3))
Jn = (s3/(12*(t-c))
      +(9*s3+5*s6-4*s2-8)/(8*(t-c)**2)
      +(2*s6+3*s3)/(4*(t-c)**3)
      -s3/(12*(t+c))
      +(9*s3+5*s6+4*s2+8)/(8*(t+c)**2)
      -(2*s6+3*s3)/(4*(t+c)**3))

Bp = 2*s6+3*s3
Ap = 9*s6+17*s3
Fp = ((7*s3/4)*sp.log((t+c)/(c-t))
      +Ap/8*(1/(t-c)+1/(t+c))
      +Bp/8*(1/(t-c)**2-1/(t+c)**2))
Cm = 9*s3+5*s6-4*s2-8
Cp = 9*s3+5*s6+4*s2+8
Fn = ((s3/12)*sp.log((c-t)/(c+t))
      -Cm/(8*(t-c))-Cp/(8*(t+c))
      -Bp/(8*(t-c)**2)+Bp/(8*(t+c)**2))
assert sp.simplify(sp.diff(Fp,t)-Jp) == 0
assert sp.simplify(sp.diff(Fn,t)-Jn) == 0

# Directed interval evaluation of the exact endpoint expression.
iv.dps = 70
s2i,s3i,s6i = iv.sqrt(2),iv.sqrt(3),iv.sqrt(6)
ci = 1+s2i

def Fpi(x):
    Ap=9*s6i+17*s3i; Bp=2*s6i+3*s3i
    return ((7*s3i/4)*iv.log((x+ci)/(ci-x))
            +Ap/8*(1/(x-ci)+1/(x+ci))
            +Bp/8*(1/(x-ci)**2-1/(x+ci)**2))
def Fni(x):
    Bp=2*s6i+3*s3i
    Cm=9*s3i+5*s6i-4*s2i-8
    Cp=9*s3i+5*s6i+4*s2i+8
    return ((s3i/12)*iv.log((ci-x)/(ci+x))
            -Cm/(8*(x-ci))-Cp/(8*(x+ci))
            -Bp/(8*(x-ci)**2)+Bp/(8*(x+ci)**2))

t0=iv.tan(iv.pi/24)
t1=1/s3i
z=iv.mpf([0,0])
p = 12*((Fpi(t0)-Fpi(z))+(Fni(t1)-Fni(t0)))
lo=float(p.a); hi=float(p.b)
assert lo > 4.063
assert hi < 4.064
assert hi < 3*(2**0.5)
print('QFORM_B17_SIX_TRIANGULAR_ROTATED_CHECK_PASS')
print('p0 interval:', p)
print('finite witness lower certificate: p0 > 4.063')
print('3sqrt2 =', 3*(2**0.5))

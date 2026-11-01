import math
import numpy as np
from fractions import Fraction

L=math.sqrt(6/math.pi)
rho0=43/50

def Cweighted(M):
    prod=math.prod(M)
    S=sum(x**(2/3) for x in M)
    return 2*math.sqrt(math.pi*math.sqrt(2)*prod*S**1.5)

def Ccap(rho):
    return Cweighted([1/rho,L,L])

def Cgauss(rho):
    return 3*math.sqrt(2)/(1-rho*rho)

assert Cgauss(rho0) < 16.375
assert Ccap(rho0) < 16.375
assert max(Cgauss(rho0),Ccap(rho0)) < 16.375

rho=math.sqrt(3)/2
C4=Cweighted([2/math.sqrt(3),1,1])
assert C4 < 10.585

R=np.array([
    [1/2,1/2,1/2],
    [5/6,-1/6,-1/6],
    [-1/6,5/6,-1/6],
    [-1/6,-1/6,5/6],
],dtype=float)
J=np.diag([1.0,1.0,-1.0])
assert np.max(np.abs(R.T@R-np.eye(3))) < 1e-12
A=R@J@R.T
A_exact=np.array([
    [1/4,5/12,5/12,-7/12],
    [5/12,25/36,-11/36,1/36],
    [5/12,-11/36,25/36,1/36],
    [-7/12,1/36,1/36,-23/36],
],dtype=float)
assert np.max(np.abs(A-A_exact)) < 1e-12
ev=np.linalg.eigvalsh(A)
assert np.max(np.abs(ev-np.array([-1.0,0.0,1.0,1.0]))) < 1e-12
assert np.min(np.abs(A)) > 0

Rf=[
    [Fraction(1,2),Fraction(1,2),Fraction(1,2)],
    [Fraction(5,6),Fraction(-1,6),Fraction(-1,6)],
    [Fraction(-1,6),Fraction(5,6),Fraction(-1,6)],
    [Fraction(-1,6),Fraction(-1,6),Fraction(5,6)],
]
gram=[[sum(Rf[k][i]*Rf[k][j] for k in range(4)) for j in range(3)] for i in range(3)]
assert gram == [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]

print("QFORM_B17_WEIGHTED_ONEHEAVY_CHECK_PASS")
print(f"L=sqrt(6/pi)={L:.15f}")
print(f"rho0=43/50={rho0:.15f}")
print(f"C_gauss(rho0)={Cgauss(rho0):.15f}")
print(f"C_weighted(rho0)={Ccap(rho0):.15f}")
print(f"uniform_patch={max(Cgauss(rho0),Ccap(rho0)):.15f}<16.375")
print(f"rho_explicit=sqrt(3)/2={rho:.15f}")
print(f"C_four_variable={C4:.15f}<10.585")
print("R^T R=I_3 exact; spec(A)={-1,0,1,1}; every A entry nonzero")

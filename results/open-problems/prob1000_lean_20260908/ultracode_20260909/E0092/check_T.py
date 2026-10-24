# Which reading of Diaconis's T(n,N) gives 0.24853 n at N = 2n?
from scipy.optimize import brentq
import math
H=lambda x: -x*math.log2(x)-(1-x)*math.log2(1-x)
a=brentq(lambda x:H(x)-0.5,1e-9,0.5)
print("alpha* = H^{-1}(1/2) =",a)
print("reading A: (N/2)/(1-H^{-1}) at N=2n ->", 1/(1-a),"n")
print("reading B: (N/2) ln 1/(1-2H^{-1}) at N=2n ->", math.log(1/(1-2*a)),"n")
print("reading C: (N/2) log2 1/(1-2H^{-1}) at N=2n ->", math.log2(1/(1-2*a)),"n")

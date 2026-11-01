"""The three-atom case symbolically.

With atoms d1,d2,d3 and both constraints tight (xi'(0)=0 and xi''(0)=0), Cramer's rule gives

    xi(0) - 1 = det N' / det N,

    N  columns: [ (d^2+s)^3 , d(d^2+s) , 3d^2-s ],
    N' columns: [ (1-d^2-s)(d^2+s)^2 , d(d^2+s) , 3d^2-s ],

after clearing one factor (d_i^2+s)^{-3} from each column.  The weights are nonnegative exactly when
three analogous determinant ratios are nonnegative.  This factors both determinants.
"""
import sympy as sp

d1, d2, d3, s = sp.symbols('d1 d2 d3 s')
D = (d1, d2, d3)
def colN(d):  return [ (d**2+s)**3, d*(d**2+s), 3*d**2-s ]
def colNp(d): return [ (1-d**2-s)*(d**2+s)**2, d*(d**2+s), 3*d**2-s ]
N  = sp.Matrix([[colN(d)[r]  for d in D] for r in range(3)])
Np = sp.Matrix([[colNp(d)[r] for d in D] for r in range(3)])
dN  = sp.factor(sp.expand(N.det()))
dNp = sp.factor(sp.expand(Np.det()))
print("det N  =", dN)
print()
print("det N' =", dNp)

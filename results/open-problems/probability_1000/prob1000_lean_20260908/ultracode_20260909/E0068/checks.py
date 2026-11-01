# E0068 checks. (1) The sigma∘Hardy-Weinberg example: V^3 = V exactly, V^2 != V, V is a genuine QSO.
# (2) Same example at random points in floating point (independent of the symbolic check).
# (3) m = 2 exhaustive: V^{r-1} = id as a polynomial identity forces identity or swap.
# (4) The edge-composition degree fact used in Theorem A, checked symbolically for a chain of three edge maps.
import sympy as sp, numpy as np, itertools, random

# ---------- (1) symbolic
x1,x2,x3 = sp.symbols('x1 x2 x3', nonnegative=True)
p = x1 + x2/2; q = x3 + x2/2
def V(v):
    a,b,c = v
    pp = a + b/2; qq = c + b/2
    return (sp.expand(qq**2), sp.expand(2*pp*qq), sp.expand(pp**2))   # swap(1,3) after Hardy-Weinberg
X = (x1,x2,x3)
V1 = V(X); V2 = V(V1); V3 = V(V2)
s = x1+x2+x3
# V^3 = V holds on the simplex: compare after reducing modulo s = 1 (substitute x3 = 1-x1-x2)
sub = {x3: 1-x1-x2}
diff3 = [sp.simplify((V3[k]-V1[k]).subs(sub)) for k in range(3)]
diff2 = [sp.simplify((V2[k]-V1[k]).subs(sub)) for k in range(3)]
print("V^3 - V on simplex:", diff3)
print("V^2 - V on simplex (should be nonzero):", diff2)
# coefficients P_{ij,k}: read off the symmetric cubic matrix
polyV = [sp.Poly(V1[k], x1,x2,x3) for k in range(3)]
P = np.zeros((3,3,3))
for k in range(3):
    d = polyV[k].as_dict()
    for mon, c in d.items():
        idx = [t for t in range(3) for _ in range(mon[t])]
        i,j = idx
        if i==j: P[i,i,k] = float(c)
        else: P[i,j,k] = P[j,i,k] = float(c)/2
print("P nonneg:", (P>=-1e-12).all(), " sum_k P_ij,k = 1 for all i,j:", np.allclose(P.sum(axis=2), 1))
print("supports B({i}) =", [set(np.nonzero(P[i,i,:]>0)[0]) for i in range(3)])

# ---------- (2) numeric
def Vn(v):
    a,b,c = v; pp = a+b/2; qq = c+b/2
    return np.array([qq*qq, 2*pp*qq, pp*pp])
rng = np.random.default_rng(1)
worst3 = 0; worst2 = 0
for _ in range(20000):
    v = rng.dirichlet(np.ones(3))
    w1 = Vn(v); w2 = Vn(w1); w3 = Vn(w2)
    worst3 = max(worst3, abs(w3-w1).max()); worst2 = max(worst2, abs(w2-w1).max())
print("numeric: max|V^3-V| =", worst3, " max|V^2-V| =", worst2)

# ---------- (3) m = 2
t,a,b,c = sp.symbols('t a b c')
f = a*t**2 + 2*b*t*(1-t) + c*(1-t)**2        # x'_1 on S^1, x = (t, 1-t), a=P11,1 b=P12,1 c=P22,1
# V^{r-1} = id as a polynomial identity forces degree 1: coefficient of t^2 must vanish
print("m=2: t^2 coefficient of edge map:", sp.expand(f).coeff(t,2))
# with a-2b+c = 0 the map is affine: f = c + (2b-2c) t ; it must map [0,1] onto [0,1] with finite order
print("m=2 affine form:", sp.expand(f.subs(a, 2*b-c)))
# affine maps of [0,1] onto itself: t -> t or t -> 1-t, i.e. (b,c) = (1/2,0) or (1/2,1): identity or swap.

# ---------- (4) edge composition degree
def g(aa, tt): return tt + aa*tt*(1-tt)
a1,a2,a3 = sp.symbols('a1 a2 a3')
comp = sp.expand(g(a1, g(a2, g(a3, t))))
print("degree of g_{a1} o g_{a2} o g_{a3}:", sp.Poly(comp, t).degree(), " leading coeff:", sp.factor(sp.Poly(comp,t).LC()))
# identity only if all a_i = 0
sol = sp.solve([sp.Poly(comp - t, t).coeff_monomial(t**k) for k in range(2, 9)], [a1,a2,a3], dict=True)
print("solutions of composition = t:", sol)

# ---------- (5) the linear family: stochastic M with M^r = M, r = 3 (a 2-cycle on the image), m = 3
M = np.array([[0,1,0.5],[1,0,0.5],[0,0,0]])  # columns stochastic: e1->e2, e2->e1, e3->(e1+e2)/2
print("M^3 == M:", np.allclose(np.linalg.matrix_power(M,3), M), " M^2 == M:", np.allclose(M@M, M))

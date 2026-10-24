import sympy as sp

u,v,w,a,b,c,l1,l2,l3,d = sp.symbols('u v w a b c l1 l2 l3 d', nonzero=True)
A = (2*c*u+l3)/(2*b)
B = (2*a*u+l2)/(2*b)
Q = 2*a*u*v + 2*b*v*w + 2*c*w*u + l1*u + l2*v + l3*w + d
R = sp.factor(sp.expand(Q - 2*b*(v+A)*(w+B)))
expected = -(2*a*c/b)*u**2 + (l1-(a*l3+c*l2)/b)*u + d-l2*l3/(2*b)
assert sp.simplify(R-expected) == 0

M = sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])
assert sorted(M.eigenvals().keys()) == [-1,2]
assert M.eigenvals()[-1] == 2
assert M.eigenvals()[2] == 1
assert M.det() == 2

# Optimization A/R + B R with A=1/|b| and B=4/sqrt(|ac|)
# gives 2 sqrt(A B)=4/(sqrt(|b|)*|ac|^(1/4)).
print('QFORM_B04_CROSS_TRIANGLE_CHECK')
print('bilinear_completion=PASS')
print('unit_triangle_spectrum={2,-1,-1}')
print('unit_triangle_det=2')
print('optimized_cap_unit_edges=4')

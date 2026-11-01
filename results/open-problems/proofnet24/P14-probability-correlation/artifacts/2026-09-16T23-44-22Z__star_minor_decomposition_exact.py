import sympy as sp
D,P,Q,S,T,g,h,k=sp.symbols('D P Q S T g h k')
F=D*(1+g+h+k+g*h+g*k+h*k)+P*(1+h+k)+Q*(1+g+k)+S*(1+g+h)+T
zero={g:0,h:0,k:0}
L=4*F.subs(zero)
for v in (g,h,k):
    L += sp.diff(F,v).subs(zero)
for u,v in ((g,h),(g,k),(h,k)):
    L += sp.Rational(1,3)*sp.diff(F,u,v).subs(zero)
L=sp.expand(L)
assert L==8*D+6*(P+Q+S)+4*T
print('STAR_MINOR_OPERATOR=', L)
print('EXPECTED=8*D+6*(P+Q+S)+4*T')
print('STAR_MINOR_DECOMPOSITION_EXACT_PASS')

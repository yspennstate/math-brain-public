"""Symbolic checks of the exact discrete martingale and drift, independently coded."""
import sympy as s

a, c, h, L, S = s.symbols('a c h L S', positive=True)
b, d = 1-a, 1-c
Q = L*a*b + c*d + L*h
masses = [a*c*(d+L*b+L*h), b*d*(c+L*a+L*h), L*a*h*d, L*b*h*c]
q = [m/Q for m in masses]
fa, fc, fh = q[0]+q[2]-a, q[0]+q[3]-c, q[2]+q[3]-h
g = a*d+b*c-a*b-c*d/L
increments = [1/(a*S)+L/(c*S), -1/(b*S)-L/(d*S),
              1/(a*S)-L/(d*S), -1/(b*S)+L/(c*S)]
checks = {
    'path probabilities sum to 1': sum(q)-1,
    'exact E[M(n+1)-M(n)|F_n] = 0': sum(p*z for p,z in zip(q,increments)),
    'drift of a': fa-L*a*b*(c-a)/Q,
    'drift of c': fc-c*d*(a-c)/Q,
    'drift of h': fh-L*h*(g-h)/Q,
    'drift of delta': fa-fc+(L*a*b+c*d)*(a-c)/Q,
    'g on diagonal': g.subs(c,a)-(1-1/L)*a*b,
    'g for ell=1': g.subs(L,1)-(a-c)**2,
    'Q on positive equilibrium curve': Q.subs({c:a,h:(1-1/L)*a*b})-2*L*a*b,
    'h eigenvalue on equilibrium curve': s.diff(fh,h).subs({c:a,h:(1-1/L)*a*b})+(1-1/L)/2,
}
for label, expression in checks.items():
    reduced = s.factor(expression)
    assert reduced == 0, (label,reduced)
    print(label + ': EXACT PASS')
for av,cv in [(0,1),(1,0)]:
    vals = [s.factor(f.subs({a:av,c:cv,h:1})) for f in [fa,fc,fh]]
    assert vals == [0,0,0]
    print(f'Additional boundary equilibrium (a,c,h)=({av},{cv},1): {vals}')
initial_variance = s.factor((2*(1+2*L)*(1+L)**2+2*L*(1-L)**2)/(2+6*L))
print('E[(M1-M0)^2] =', initial_variance)
assert s.factor(initial_variance-(3*L**3+3*L**2+5*L+1)/(3*L+1)) == 0
print('ALL SYMBOLIC CHECKS PASS')

# Lower bound for alpha_m from the lumped (1 vs block {2..m}) construction.
# f(x)=a x^2+2b x(1-x)+c(1-x)^2 with a=b=alpha, c=1-(m-1)alpha; threshold where f'(p)=-1.
import sympy as sp
al,x=sp.symbols('alpha x')
m=sp.symbols('m',positive=True)
def thresh(mv):
    a=al;b=al;c=1-(mv-1)*al
    f=a*x**2+2*b*x*(1-x)+c*(1-x)**2
    res=sp.factor(sp.resultant(sp.expand(f-x),sp.expand(sp.diff(f,x)+1),x))
    sols=[s for s in sp.Poly(res,al).nroots() if s.is_real and 0<s<1]
    return res,sols
for mv in [2,3,4,5,6,10]:
    res,sols=thresh(mv)
    print("m=",mv,"resultant:",res," roots in (0,1):",sols, " upper bounds: 1/(2m)=",1/(2*mv)," new=",((mv+1)-(mv*mv+1)**0.5)/(2*mv))
# general m symbolic
a=al;b=al;c=1-(m-1)*al
f=a*x**2+2*b*x*(1-x)+c*(1-x)**2
res=sp.factor(sp.resultant(sp.expand(f-x),sp.expand(sp.diff(f,x)+1),x))
print("general m:",res)
# check the m=2 value equals (3-sqrt7)/4
print(sp.nsimplify(thresh(2)[1][0]), (3-sp.sqrt(7))/4, sp.N((3-sp.sqrt(7))/4))

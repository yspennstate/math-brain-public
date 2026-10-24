import sympy as S
a,t,s=S.symbols('a t s',real=True)
Z=6+t;p=(8+5*t)/(4*Z);z=(2*a+S.I*t/4)/Z
k13=s*(-a/2-S.I)/Z;k23=s*(1+S.I*a/2)/Z
detQ=-(8-t)/(4*Z)
red=lambda f:S.factor(S.cancel(S.expand(f).subs(a*a,1-t)))
v1=red(-((p-1)*k13-z*k23)/detQ)
v2=red(-(-S.conjugate(z)*k13+p*k23)/detQ)
print('v1=',v1);print('v2=',v2)
for v in [v1,v2]: print('abs2=',red(v*S.conjugate(v)).subs(s*s,t))

import sympy as s
from pathlib import Path
q,l,c=s.symbols('q l c',positive=True)
A=c*(l*l+3*l*c+q*c*c)
B=c*c*(3*l+q*c)
u=l*l*(l+2*c); v=l*l*c
cats=[('E1',A+u,A,1),('E2',A,A+u,1),('E0',A,A,q-2),('D12',B+v,B+v,2),('D1',B+v,B,2*(q-2)),('D2',B,B+v,2*(q-2)),('D0',B,B,(q-2)*(q-3))]
terms=[]; cert=[]
sub={q:5,l:s.Rational(2,5),c:s.Rational(3,25)}
for name,x,y,m in cats:
    for name2,z,w,n in cats:
        diff=s.expand(x*z-y*w)
        sign=s.sign(diff.subs(sub))
        if sign==0: assert diff==0
        else:
            poly=s.Poly(sign*diff,l,c,q)
            assert all(co>=0 for co in poly.coeffs()), (name,name2,s.factor(diff))
        terms.append(m*n*sign*diff/2)
        cert.append((name,name2,int(sign),str(s.factor(diff))))
F=s.factor(sum(terms).subs(c,(1-l)/q))
der=s.factor(s.diff(F,q))
t,a=s.symbols('t a',nonnegative=True)
num,den=s.fraction(s.factor(der.subs({q:t+2,l:a/(a+1)})))
positive=s.Poly(s.expand(num),t,a)
assert all(co>=0 for co in positive.coeffs()),s.factor(num)
out='Exact depth-two binary-tree pair TV:\n'+str(F)+'\nDerivative in continuous q:\n'+str(der)+'\nAfter q=t+2 and lambda=a/(a+1):\nnum='+str(s.expand(num))+'\nden='+str(s.factor(den))+'\nAll numerator coefficients nonnegative.\n\nSign certificate (ordered category pairs):\n'+'\n'.join(map(str,cert))+'\n'
Path(__file__).with_name('depth_two_symbolic.log').write_text(out,encoding='utf8')
print(out[:2500],flush=True)

exec(open('computations/X022/perspective_probe.py').read().split('res=[]')[0])
n=3
f=sum(s.binomial(2*n,2*j)*B**(2*j)*C**(2*n-2*j)*mom(2*j,A)*mom(2*n-2*j,D) for j in range(n+1))/s.Integer(2*n*(2*n-1))
h=s.hessian(f,vars)
pt=(s.Rational(1,5),s.Rational(1,5),s.Rational(3,10),s.Rational(1,10))
hr=h.subs(dict(zip(vars,pt)))
e,v=np.linalg.eigh(np.array(hr,float))
v0=v[:,0]
print('e',e[0],'v',v0)
vr=s.Matrix([s.Rational(round(float(x)*10),10) for x in v0])
w=s.factor((vr.T*hr*vr)[0])
print('rational v',list(vr),'quadratic',w, 'decimal',float(w))
print('scaled vec',list(vr*10),'scaled quadratic',w*100)
print('g3',s.factor(f))

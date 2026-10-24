import sympy as s
k,n=s.symbols('k n',integer=True,positive=True)
m=[s.Integer(1)]+[s.rf(k,r)/s.rf(n+1,r) for r in range(1,5)]
v=s.factor(2*m[4]-8*m[3]*m[1]+6*m[2]**2)
print('E difference fourth',v)
print('mean fourth',s.factor(s.summation(v,(k,1,n))/n))

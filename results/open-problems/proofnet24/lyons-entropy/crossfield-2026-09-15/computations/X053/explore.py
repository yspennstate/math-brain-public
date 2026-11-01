import sympy as s
x,y,z,c=s.symbols('x y z c',real=True)
u=[1-x-y-z,1-x+y+z,1+x-y+z,1+x+y-z]
f=[a*a-c*c for a in u]
print(s.factor(f[2]*f[3]-f[0]*f[1]))
print('difference',s.factor((u[2]-c)*(u[3]-c)-(u[0]+c)*(u[1]+c)))

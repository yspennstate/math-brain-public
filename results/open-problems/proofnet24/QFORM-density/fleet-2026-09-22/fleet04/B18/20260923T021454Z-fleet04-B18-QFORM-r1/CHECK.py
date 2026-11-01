import math

def alpha_star(R):
    return (3-5*R+math.sqrt(25*R*R+18*R+9))/12

def H(R,a):
    return a*(1-a)**1.5*math.sqrt(a+R)/(1+R)

def C(R):
    a=alpha_star(R)
    return 6*H(R,a)**(-1/3)

for R in (0.25,1.0,4.0):
    a=alpha_star(R)
    residual=6*a*a+(5*R-3)*a-2*R
    print(R,a,residual,C(R))

grid=max(C(0.25+i*(4-0.25)/200000) for i in range(200001))
print("moderate_shear_grid_max",grid)
print("r2_equal_split",6*(40/3)**(1/3))
assert grid < 14.041
assert abs(6*alpha_star(4)**2+(20-3)*alpha_star(4)-8) < 1e-12

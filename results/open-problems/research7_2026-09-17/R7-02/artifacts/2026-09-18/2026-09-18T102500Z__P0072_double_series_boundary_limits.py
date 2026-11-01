from sympy import symbols, factor, limit, simplify

rho,x,y,a,b,m,k=symbols('rho x y a b m k', positive=True)

def qR(ell,alpha,beta,rho):
    g=(ell+alpha)/m
    h=(ell+beta)/k
    w=alpha+beta
    d=rho+beta
    e=rho+alpha
    Z=(g*h*w+g*h*d+g*h*e+g*w*e+g*d*e+h*w*d+h*d*e+w*d*e)
    return d*e*(g+h+w)/Z

ell=1-a-(x+1)*rho
expr_beta=factor(limit(qR(ell,a,x*rho,rho)/rho,rho,0))
expected_beta=(x+1)*(a*k*m-a*m+k+m)/(a*k-2*a+2)
assert simplify(expr_beta-expected_beta)==0
print('beta_face_limit',expr_beta)

ell=1-b-(x+1)*rho
expr_alpha=factor(limit(qR(ell,x*rho,b,rho)/rho,rho,0))
expected_alpha=(x+1)*(b*k*m-b*k+k+m)/(b*m-2*b+2)
assert simplify(expr_alpha-expected_alpha)==0
print('alpha_face_limit',expr_alpha)

ell=1-(x+y+1)*rho
expr_inter=factor(limit(qR(ell,x*rho,y*rho,rho)/rho,rho,0))
expected_inter=(k+m)*(x+1)*(y+1)/(2*(x+y+1))
assert simplify(expr_inter-expected_inter)==0
print('intersection_limit',expr_inter)

print('ALL_EXACT_BOUNDARY_LIMITS_PASS')

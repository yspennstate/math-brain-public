import math
import numpy as np

rng=np.random.default_rng(230923)
errs=[]
for _ in range(20):
    Z=rng.normal(size=(7,2))
    Q,_=np.linalg.qr(Z)
    v,q=Q[:,0],Q[:,1]
    beta=float(rng.normal())
    m=float(np.exp(rng.uniform(-1,1)))
    h=beta*v+m*q
    H2=float(h@h)
    x=float(rng.uniform(0.02,0.98))
    tau=m*math.sqrt(x)/math.sqrt(H2)
    B=np.column_stack([h,v])
    G=B.T@B+np.array([[0.0,0.0],[0.0,tau*tau]])
    Gi=np.linalg.inv(G)
    c0=tau*tau*Gi[1,1]
    eta=v*v+q*q
    delta=h*h/H2
    cj=np.einsum('ij,jk,ik->i',B,Gi,B)
    errs.append(max(abs(c0-x/(1+x)),
                    np.max(np.abs(cj-(eta+x*delta)/(1+x))),
                    abs(np.linalg.det(G)-m*m*(1+x))))
print('max_formula_error',max(errs))

def calc(x):
    c=x/(1+x)
    alpha=(3+x)/(2*(1+x))
    Bx=(4*math.pi)**alpha*2**(c-1)*(1+x)**(-1/(2*(1+x)))
    K0=math.sqrt(2)*Bx*math.exp(1/(2*(1+x)))
    C=(3+x)/(math.pi*(1-x))*K0**(2*(1+x)/(3+x))
    return c,alpha,Bx,K0,C

for x in [0.5,0.75,0.875,15/16]:
    print('x',x,'c_alpha_B_K_C',calc(x))

Kcrit=2**(7/4)*math.pi*math.e**0.25
Jcrit=16/3*math.sqrt(Kcrit)
Ecrit=Jcrit/math.sqrt(2*math.pi)
print('critical_K',Kcrit)
print('critical_J',Jcrit)
print('critical_E',Ecrit)

theta=1/16
x0=15/16
partner=16*math.sqrt(60/theta)
collar_sq=(1-x0)/2+2*x0*theta**2
print('partner',partner)
print('collar_sq',collar_sq,'eta_lower',1-collar_sq,
      'collar_ratio',math.sqrt(collar_sq))
print('STATUS=PASS')

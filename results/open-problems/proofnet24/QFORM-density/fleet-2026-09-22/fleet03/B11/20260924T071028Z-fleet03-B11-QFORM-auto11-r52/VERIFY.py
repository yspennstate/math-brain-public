import math
import numpy as np
from mpmath import gamma, pi

rng=np.random.default_rng(20260924)
max_err_jw=0.0
max_err_jv=0.0
max_err_det=0.0

def wedge_norm(x,y):
    z=float(np.dot(x,x)*np.dot(y,y)-np.dot(x,y)**2)
    return math.sqrt(max(0.0,z))

for _ in range(20000):
    Z=rng.normal(size=(7,4))
    frame,_=np.linalg.qr(Z)
    eH,t,w,v=[frame[:,j] for j in range(4)]

    kappa=10.0**rng.uniform(-1.0,1.0)
    q=rng.uniform(1.0e-5,1.0)
    a=kappa*math.sqrt(q)
    b=kappa*math.sqrt(1.0-q)
    c=(1.0 if rng.random()<0.5 else -1.0)*10.0**rng.uniform(-1.0,1.0)
    eta=float(rng.normal())
    delta=float(rng.normal())

    H,T,W,V=rng.normal(size=4)
    Vp=V+eta*W
    S=a*H+b*T
    svec=a*eH+b*t
    g=v+eta*w

    gradQ=(2.0*W*svec + 2.0*S*w + 2.0*c*Vp*g + 2.0*delta*W*w)
    JW=wedge_norm(w,gradQ)
    JV=wedge_norm(g,gradQ)

    rhs_JW=2.0*math.sqrt(kappa*kappa*W*W+c*c*Vp*Vp)
    rhs_JV=2.0*math.sqrt((1.0+eta*eta)*kappa*kappa*W*W+(S+delta*W)**2)

    max_err_jw=max(max_err_jw,abs(JW-rhs_JW))
    max_err_jv=max(max_err_jv,abs(JV-rhs_JV))

    # (S,V',W) -> (Z,Y,X)=(S+delta W,cV',kappa W)
    L=np.array([[1.0,0.0,delta],[0.0,c,0.0],[0.0,0.0,kappa]])
    max_err_det=max(max_err_det,abs(abs(np.linalg.det(L))-kappa*abs(c)))

Cstar=float((2.0/3.0)*pi*(gamma(0.25)/gamma(0.75))**2)
C2=1.5*Cstar**(2.0/3.0)
joint_tail_constant=math.pi/math.sqrt(2.0)

print(f"max_JW_identity_error={max_err_jw:.17g}")
print(f"max_JV_identity_error={max_err_jv:.17g}")
print(f"max_linear_det_error={max_err_det:.17g}")
print(f"Cstar={Cstar:.15f}")
print(f"C2={C2:.15f}")
print(f"joint_tail_constant_pi_over_sqrt2={joint_tail_constant:.15f}")
assert max_err_jw < 1e-9
assert max_err_jv < 1e-8
assert max_err_det < 1e-10
assert abs(Cstar-18.333828848054324) < 1e-12
assert abs(C2-10.429417208172787) < 1e-12
print("QFORM_B11_R52_TWOCHART_JACOBIAN_CHECK_PASS")

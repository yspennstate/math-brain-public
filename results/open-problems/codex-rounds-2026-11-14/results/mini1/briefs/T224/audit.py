"""Small independent checks of PROOF.md. Standard library only; no simulation."""
import json
import math
import random
from fractions import Fraction
from pathlib import Path

rng = random.Random(224)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def phi(x):
    return (math.sin(x), math.cos(x))

def dphi(x):
    return (math.cos(x), -math.sin(x))

def mean_feature(xs):
    return tuple(sum(phi(x)[j] for x in xs)/len(xs) for j in range(2))

def residual(xs,g):
    return tuple(a-b for a,b in zip(mean_feature(xs),g))

def risk(xs,g):
    r=residual(xs,g)
    return dot(r,r)/2

def gradient(xs,g):
    r=residual(xs,g)
    return [dot(dphi(x),r) for x in xs]

max_hessian_fd_error=0.0
max_hessian_gradient_error=0.0
max_coupling_violation=-math.inf
min_psd=math.inf
for trial in range(200):
    n=5
    xs=[rng.uniform(-2,2) for _ in range(n)]
    es=[rng.uniform(-1,1) for _ in range(n)]
    g=(rng.uniform(-.5,.5),rng.uniform(-.5,.5))
    r=residual(xs,g)
    jv=tuple(sum(dphi(x)[j]*e for x,e in zip(xs,es))/n for j in range(2))
    psd=dot(jv,jv)
    min_psd=min(min_psd,psd)
    curvature=-sum(dot(r,phi(x))*e*e for x,e in zip(xs,es))/n
    exact=psd+curvature
    eps=1e-4
    plus=[x+eps*e for x,e in zip(xs,es)]
    minus=[x-eps*e for x,e in zip(xs,es)]
    fd=(risk(plus,g)-2*risk(xs,g)+risk(minus,g))/(eps*eps)
    max_hessian_fd_error=max(max_hessian_fd_error,abs(fd-exact))
    gp=gradient(plus,g)
    gm=gradient(minus,g)
    gd=sum(e*(p-m)/(2*eps) for e,p,m in zip(es,gp,gm))/n
    max_hessian_gradient_error=max(max_hessian_gradient_error,abs(gd-exact))
    # Independent direct evaluation of d(q^2)/2 from two vector fields.
    vs=[rng.uniform(-2,2) for _ in range(n)]
    ws=[v+rng.uniform(-.2,.2) for v in vs]
    rm=(rng.uniform(-.4,.4),rng.uniform(-.4,.4))
    fv=mean_feature(vs)
    fm=tuple(gj+rj for gj,rj in zip(g,rm))
    zeta=tuple(vj-mj for vj,mj in zip(fv,fm))
    eta=math.sqrt(dot(zeta,zeta))
    h=math.sqrt(dot(rm,rm))  # exact global h for phi=(sin,cos)
    ew=[w-v for w,v in zip(ws,vs)]
    q2=sum(e*e for e in ew)/n
    q=math.sqrt(q2)
    rw=residual(ws,g)
    wdot=[-dot(dphi(w),rw) for w in ws]
    vdot=[-dot(dphi(v),rm) for v in vs]
    lhs=sum(e*(dw-dv) for e,dw,dv in zip(ew,wdot,vdot))/n
    rhs=(h+eta+q)*q2+eta*q  # B=M=1
    max_coupling_violation=max(max_coupling_violation,lhs-rhs)

# Exact rational checks of every optimized power, using different expressions.
power_checks=[]
for c in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(7,4)):
    p=1-c/2
    exponent=c/p
    assert exponent==2*c/(2-c)
    for kap in (Fraction(0),Fraction(1,2),Fraction(3)):
        horizon=1/(c+4+2*kap)
        early=(4+2*kap)*horizon-1
        late=-c*horizon
        assert early==late
        power_checks.append({'c':str(c),'kappa':str(kap),'a':str(-early)})

# Constant and stopping-threshold checks without exponent overflow.
max_constant_ratio=0.0
max_stop_ratio=0.0
for _ in range(200):
    A=rng.uniform(0,3)
    B=rng.uniform(0,3)
    M=rng.uniform(0,2)
    T=rng.uniform(1,30)
    HT=rng.uniform(0,4)
    expfac=math.exp(2*M*(1+B))
    K=(2*A*A+2*A*A*B**4+16*A**4*(1+B)**2)*expfac
    terms=(2*A*A*B**4*T*T*expfac+2*A*A+16*A**4*(1+B)**2*T**4*expfac)
    ratio=terms/(K*(1+T)**4)
    max_constant_ratio=max(max_constant_ratio,ratio)
    assert ratio<=1+1e-12
    z=1/(2*(1+B)*T*math.exp(HT+M*(1+B)))
    qbound=B*z*math.exp(HT+M+M*B)
    max_stop_ratio=max(max_stop_ratio,qbound*T)
    assert qbound*T<.5

# A linear feature check: the positive Jacobian term must contract, not expand.
# For phi(w)=w (a local algebra check only), g=0, G_i=mean(w).
w=[.8,-.1,.4]
v=[.2,-.3,.7]
e=[a-b for a,b in zip(w,v)]
mean_e=sum(e)/len(e)
linear_inner=sum(ei*mean_e for ei in e)/len(e)
assert abs(linear_inner-mean_e**2)<1e-14

assert max_hessian_fd_error<2e-7
assert max_hessian_gradient_error<2e-8
assert max_coupling_violation<=1e-12
out={
 'seed':224,
 'hessian_and_coupling_cases':200,
 'max_hessian_risk_second_difference_error':max_hessian_fd_error,
 'max_hessian_gradient_difference_error':max_hessian_gradient_error,
 'max_coupling_inequality_violation':max_coupling_violation,
 'min_jacobian_square_term':min_psd,
 'max_constant_ratio':max_constant_ratio,
 'max_stopping_bound_times_T':max_stop_ratio,
 'exact_power_checks':power_checks,
 'linear_psd_sign_check':True,
 'status':'PASS',
 'scope':'Algebra and finite-difference audit only; not evidence of the infinite-time theorem by simulation.'
}
Path('audit_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

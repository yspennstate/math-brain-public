"""Independent exact series and high-precision trigonometric endpoint audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
import resource
import signal
import sys
import time
import mpmath as mp
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU,(180,180))
start=time.monotonic()
N=4

def const(x): return [F(x)]+[F(0)]*N
def add(a,b): return [x+y for x,y in zip(a,b)]
def neg(a): return [-x for x in a]
def scale(a,c): return [x*c for x in a]
def mul(a,b):
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]
def inv(a):
    assert a[0]
    b=[1/a[0]]+[F(0)]*N
    for i in range(1,N+1): b[i]=-sum(a[j]*b[i-j] for j in range(1,i+1))/a[0]
    return b
def div(a,b): return mul(a,inv(b))
def power(a,n):
    b=const(1)
    for _ in range(n): b=mul(b,a)
    return b
def deriv(a): return [i*a[i] for i in range(1,N+1)]+[F(0)]
one=const(1)
w=const(0); w[1]=F(1)

def A(z):
    z2=mul(z,z)
    return div(power(add(one,z2),3),scale(mul(mul(z,add(one,neg(z))),
           mul(add(const(3),neg(z2)),add(add(z2,scale(z,4)),one))),2))
def f(z):
    z2=mul(z,z)
    return div(mul(z,add(power(z,4),const(7))),scale(mul(
        mul(add(one,neg(z)),add(one,z)),add(const(3),neg(z2))),6))
invB=div(scale(mul(mul(w,add(one,neg(w))),mul(
    add(const(3),neg(power(w,2))),add(add(power(w,2),scale(w,4)),one))),2),
    power(add(one,power(w,2)),3))

H=[21,189,280,105,-122,-93,-32,-9,-3]
positive=[sum(H[i]*comb(8-i,k-i) for i in range(k+1)) for k in range(9)]
assert positive==[21,357,2191,6930,12688,13860,8764,2856,336]
assert all(c>0 for c in positive)
ev=lambda p,z:sum(c*z**i for i,c in enumerate(p))

# Full polynomial identity for the endpoint speed, without SymPy or samples.
def pa(a,b,c=1):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=c*v
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pm(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,wv in enumerate(b): out[i+j]+=v*wv
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pp(a,n):
    out=[1]
    for _ in range(n): out=pm(out,a)
    return out
def pd(a): return [i*a[i] for i in range(1,len(a))] or [0]
nA=pp([1,0,1],3)
dA=pm([0,2],pm([1,-1],pm([3,0,-1],[1,4,1])))
nf=[0,7,0,0,0,1]
df=pm([6,0,-6],[3,0,-1])
Lf_num=pm([1,0,1],pa(pm(pd(nf),df),pm(nf,pd(df)),-1))
LA_num=pm([1,0,1],pa(pm(pd(nA),dA),pm(nA,pd(dA)),-1))
Ns=pa(pa(pm([18],pm(Lf_num,pm(dA,nA))),
         pm([7],pm(pp(df,2),pm(dA,nA))),-1),
      pm([18],pm(nf,pm(df,LA_num))),-1)
numV=pm([0,1,-1],H)
denV=pm([27],pm(pp([1,1],2),pp([1,0,1],3)))
assert pm(Ns,denV)==pm(numV,pm([54],pm(pp(df,2),pp(nA,2))))

def target(z):
    k=z*z*(z**4+7)*(z*z+4*z+1)/(3*(z+1)*(z*z+1)**3)
    v=z*(1-z)*ev(H,z)/(27*(z+1)**2*(1+z*z)**3)
    aq=(1+z*z)**3/(2*z*(1-z)*(3-z*z)*(z*z+4*z+1))
    return k,v,aq/v

second_num=[-21,-588,-3052,-2401,9962,21452,7262,-14785,-14874,
            -2124,2496,1293,450,204,78,21,3]
def second(z):
    return ev(second_num,z)/(54*(z+1)**3*(z*z-3)*(z*z+1)**3*(z*z+4*z+1))

exact=[]
for j in range(1,30):
    r=F(j,30)
    z=div(add(const(r),neg(w)),add(one,scale(w,r)))
    alpha=mul(A(z),invB)
    eta=mul(add(f(z),f(w)),invB)
    X=div(deriv(eta),deriv(alpha))
    Y=add(eta,neg(mul(alpha,X)))
    k,v,curv=target(r)
    assert X[0]==k and Y[0]==Y[1]==0
    assert -X[1]/6==v
    assert 2*Y[2]/36/v**2==curv
    rc=(1-r)/(1+r)
    kc,vc,cc=target(rc)
    assert k+kc==1 and v==vc and curv==cc
    # Third graph derivative is independent of the chosen regular parameter.
    third=(6*Y[3]*X[1]-12*Y[2]*X[2])/X[1]**4
    assert X[2]/18==second(r)
    aq=ev(nA,r)/ev(dA,r)
    la=ev(LA_num,r)/ev(dA,r)**2
    third_formula=(la/3-aq)/v**2-aq*second(r)/v**3
    assert third==third_formula
    exact.append({'z':str(r),'contact':str(k),'speed':str(v),
                  'curvature':str(curv),'third_graph_derivative':str(third)})

mp.mp.dps=100
delta=3*mp.pi/4; gamma=mp.pi/4; h=mp.mpf(4)/3
rows=[]
max_limit_error=mp.mpf(0)
for fs in ('.000001','.001','.03','.15','.3333333333333333','.5',
           '.7','.95','.999','.999999'):
    u=mp.mpf(fs)*delta; T=delta-u
    a=lambda t:mp.sin(gamma)/(2*mp.pi*(mp.cos(t-u)+mp.cos(gamma)))
    b=lambda t:a(-t)
    e=lambda t:(mp.sin(T)/(mp.cos(t)-mp.cos(T))-
        h*mp.sin(h*T)/(mp.cos(h*t)-mp.cos(h*T)))/(2*mp.pi)
    def point(t):
        av,bv,ee=a(t),b(t),e(t)
        ap,bp,ep=mp.diff(a,t),mp.diff(b,t),mp.diff(e,t)
        W=av*bp-ap*bv
        return (ee*bp-ep*bv)/W,(av*ep-ap*ee)/W
    k=mp.sin(u)*mp.sin(T)/mp.sin(delta)*(mp.cot(T)-h*mp.cot(h*T))
    a0=a(T)
    a1=mp.diff(a,T)
    e1=(h*h/mp.sin(h*T)**2-1/mp.sin(T)**2-(h*h-1)/3)/(8*mp.pi)
    d=e1-k*a1
    dsym=(mp.mpf(2)/3*(h*h-1)-
        (mp.cot(T)-h*mp.cot(h*T))*(mp.cot(u)-h*mp.cot(h*u)))/(8*mp.pi)
    v=2*d/a0; curvature=mp.pi*a0*a0/d
    kr,vr,cr=target(mp.tan(T/3))
    assert 0<k<1 and d>0
    for x,y in ((k,kr),(v,vr),(curvature,cr),(d,dsym)):
        assert abs(x-y)<mp.mpf('1e-65')*max(abs(x),abs(y))
    # Direct derivatives of the original pole-containing formulas at a nearby point.
    epsilon=min(u,T)*mp.mpf('1e-12')
    t=T-epsilon
    x,y=point(t)
    xp=mp.diff(lambda q:point(q)[0],t)
    yp=mp.diff(lambda q:point(q)[1],t)
    xpp=mp.diff(lambda q:point(q)[0],t,2)
    ypp=mp.diff(lambda q:point(q)[1],t,2)
    graph2=(ypp*xp-yp*xpp)/xp**3
    errs=[abs((x-k)/(-epsilon*v)-1),
          abs(y/(mp.pi*a0*v*epsilon**2)-1),
          abs(xp/v-1),abs(graph2/curvature-1)]
    assert max(errs)<mp.mpf('1e-8'),(fs,errs)
    max_limit_error=max(max_limit_error,max(errs))
    # Interior points must remain in the correct open arc rectangle.
    for fraction in ('-.98','-.5','0','.5','.98'):
        xx,yy=point(mp.mpf(fraction)*T)
        assert 0<xx<k and 0<yy<k and xx+yy<k
    rows.append({'u_over_delta':fs,'contact':float(k),'speed':float(v),
        'curvature':float(curvature),'maximum_limit_relative_error':float(max(errs))})

# Try to refute analytic gluing: at equal weights reflection changes the
# sign of the third graph derivative. Compute it from regularized coefficients.
u=T=delta/2
r=mp.sqrt(2)-1
# Independently use the closed X'' endpoint formula from the symbolic jet.
xsecond=second(r)
k,v,curvature=target(r)
a0=mp.sin(gamma)/(2*mp.pi*(1+mp.cos(gamma)))
third=2*mp.pi*a0*(mp.cot(delta)-xsecond/v)/v**2
assert abs(third)>1
exact_third=-(4168422*mp.sqrt(2)+494262)/1803649
assert abs(third-exact_third)<mp.mpf('1e-90')
assert abs(xsecond-v/2)<mp.mpf('1e-90')
# Re-evaluate the third graph derivative from the original trigonometric
# envelope, independently of all rational jets, at equal weights.
t=T-mp.mpf('1e-12')
xp=mp.diff(lambda q:point(q)[0],t)
yp=mp.diff(lambda q:point(q)[1],t)
xpp=mp.diff(lambda q:point(q)[0],t,2)
ypp=mp.diff(lambda q:point(q)[1],t,2)
xppp=mp.diff(lambda q:point(q)[0],t,3)
yppp=mp.diff(lambda q:point(q)[1],t,3)
third_direct=(yppp*xp*xp-yp*xppp*xp-3*ypp*xp*xpp+3*yp*xpp*xpp)/xp**5
third_limit_error=abs(third_direct-third)
assert third_limit_error<mp.mpf('1e-8')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes=rss if sys.platform=='darwin' else rss*1024
assert rss_bytes<1024**3
result={'positive_sign_coefficients':positive,'exact_series_checks':exact,
    'trigonometric_checks':rows,'equal_weight_third_derivative_from_SW':float(third),
    'third_derivative_original_trigonometric_limit_error':float(third_limit_error),
    'maximum_limit_relative_error':float(max_limit_error),
    'resources':{'elapsed_seconds':time.monotonic()-start,
        'peak_rss_MiB':rss_bytes/1024**2,'nice':os.getpriority(os.PRIO_PROCESS,0)}}
Path('join_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact Fraction-series endpoint checks:',len(exact))
print('PASS full integer endpoint-speed identity and positive-coefficient transform')
print('PASS original-trigonometric endpoint/curvature checks:',len(rows))
print('sign certificate:',positive)
print('maximum endpoint-limit relative error:',float(max_limit_error))
print('equal-weight third graph derivative from SW:',float(third))
print('third-derivative original-trigonometric limit error:',float(third_limit_error))
print('resources:',json.dumps(result['resources'],sort_keys=True))

import sympy as sp
import numpy as np, math, json

# ---------- exact symbolic core ----------
a,b,x,y,c,eps,t = sp.symbols('a b x y c eps t', positive=True, real=True)
an,Er,Ei,Zr,Zi,B11,B22,Hr,Hi = sp.symbols(
    'an Er Ei Zr Zi B11 B22 Hr Hi', real=True)
I=sp.I
eta=Er+I*Ei
zeta=Zr+I*Zi
h=Hr+I*Hi

U=sp.Matrix([[b,a,0],[-a,b,0],[0,0,1]]) # columns w,u,e3
Kblock=sp.Matrix([[eps,0,0],[0,x,c],[0,c,y]])
K=sp.expand(U*Kblock*U.T)
Ablock=sp.Matrix([[an, sp.conjugate(eta), sp.conjugate(zeta)],
                  [eta,B11,sp.conjugate(h)],
                  [zeta,h,B22]])
A=sp.expand(U*Ablock*U.T)

def atom(mask, Q):
    D=sp.diag(*[0 if (mask>>j)&1 else 1 for j in range(3)])
    return sp.expand((-1)**(3-bin(mask).count('1')) * (Q-D).det())

def reduce_norm(expr):
    # Reduce modulo a^2+b^2=1 by eliminating even powers of b.
    e=sp.expand(expr)
    poly=sp.Poly(e,b)
    out=0
    for (kb,),coef in poly.terms():
        if kb%2==0:
            out += coef*(1-a*a)**(kb//2)
        else:
            out += coef*b*(1-a*a)**((kb-1)//2)
    return sp.factor(sp.expand(out))

p=[]; dp=[]; ddp=[]
for mask in range(8):
    f=atom(mask,K+t*A)
    p.append(sp.factor(f.subs(t,0)))
    dp.append(sp.factor(sp.diff(f,t).subs(t,0)))
    ddp.append(sp.factor(sp.diff(f,t,2).subs(t,0)))

d=x*y-c*c
d0=(1-x)*(1-y)-c*c
r=x-d
s=y-d

assert sp.simplify(reduce_norm(p[7]) - eps*d)==0
assert sp.simplify(reduce_norm(p[3]) - eps*r)==0
boundary_expected={
    0:d0, 1:a*a*r, 2:b*b*r, 3:0,
    4:s, 5:a*a*d, 6:b*b*d, 7:0
}
for mask,val in boundary_expected.items():
    assert sp.simplify(reduce_norm(p[mask].subs(eps,0))-reduce_norm(val))==0, (mask, reduce_norm(p[mask].subs(eps,0)), reduce_norm(val))

# Leading rare normal Fisher coefficient.
lead_dp12=sp.simplify(reduce_norm(dp[3].subs(eps,0)))
lead_dp123=sp.simplify(reduce_norm(dp[7].subs(eps,0)))
assert sp.simplify(lead_dp12-r*an)==0
assert sp.simplify(lead_dp123-d*an)==0
assert sp.simplify(lead_dp12**2/r + lead_dp123**2/d - x*an**2)==0

# Common log(eps) second-derivative coefficient.
common_dd=sp.simplify(reduce_norm(ddp[3]+ddp[7]))
assert sp.simplify(common_dd - 2*(an*B11-(Er**2+Ei**2)))==0

# Stable zeta block: mixed zeta/B frozen terms cancel across split atoms.
def coeff(expr, vars_pows):
    z=sp.expand(expr)
    for var,powv in vars_pows:
        z=sp.diff(z,var,powv)
    subs={B11:0,B22:0,Hr:0,Hi:0,an:0,Er:0,Ei:0,Zr:0,Zi:0}
    return sp.simplify(reduce_norm(z.subs(subs)))
patterns=[]
for mask in [1,2,5,6]:
    patterns.append((mask, coeff(ddp[mask].subs(eps,0),[(Hr,1),(Zr,1)]),
                           coeff(ddp[mask].subs(eps,0),[(Hi,1),(Zi,1)])))
expected=[(1,4*a*b,4*a*b),(2,-4*a*b,-4*a*b),(5,-4*a*b,-4*a*b),(6,4*a*b,4*a*b)]
assert patterns==expected, patterns
A2,B2,R,D=sp.symbols('A2 B2 R D', positive=True)
log_cancel=sp.expand_log(
    -sp.log(A2*R)+sp.log(B2*R)+sp.log(A2*D)-sp.log(B2*D), force=True)
assert sp.simplify(log_cancel)==0

# Fisher cross zeta-real vs arbitrary tangent changes dr,dd cancels.
dr,dd=sp.symbols('dr dd', real=True)
k=sp.symbols('k', real=True)
fish_cross = k*(A2*dr)/(A2*R) + (-k)*(B2*dr)/(B2*R) + (-k)*(A2*dd)/(A2*D) + k*(B2*dd)/(B2*D)
assert sp.simplify(fish_cross)==0

# Pure-zeta frozen coefficient and determinant identity.
assert sp.simplify(sp.expand(r*s-d*d0)-c*c)==0
frozen_half=(1-x)*sp.log(d0/s)+(2*x-1)*sp.log(r/d)-x*sp.log(r/d)
target_half=(1-x)*sp.log(d*d0/(r*s))
assert sp.simplify(sp.expand_log(frozen_half-target_half,force=True))==0

exact = {
    "status":"PASS",
    "claims":[
        "p12=eps*(x-detM), p123=eps*detM",
        "boundary law is two-site DPP M with fixed split weights a^2,b^2",
        "leading rare normal Fisher coefficient = x*an^2/eps",
        "common log(1/eps) coefficient = 2*(an*B11-|eta|^2)",
        "zeta/B mixed frozen terms cancel",
        "zeta/B Fisher cross cancels",
        "(x-detM)*(y-detM)-detM*det(I-M)=c^2",
        "pure-zeta frozen coefficient = 2(1-x) log(detM det(I-M)/((x-detM)(y-detM))) |zeta|^2"
    ]
}

# ---------- targeted numerical refutation search near pair-degenerate shape face ----------
def adj3(A):
    aa,bb,cc=A[0]; dd_,ee,ff=A[1]; gg,hh,ii=A[2]
    return np.array([[ee*ii-ff*hh, cc*hh-bb*ii, bb*ff-cc*ee],
                     [ff*gg-dd_*ii, aa*ii-cc*gg, cc*dd_-aa*ff],
                     [dd_*hh-ee*gg, bb*gg-aa*hh, aa*ee-bb*dd_]],dtype=complex)
def atom_data(K):
    pp=np.empty(8); Es=[]
    for mask in range(8):
        Dm=np.diag([0.0 if (mask>>j)&1 else 1.0 for j in range(3)])
        Q=K-Dm
        sign=(-1)**(3-int(mask).bit_count())
        pp[mask]=float(np.real(sign*np.linalg.det(Q)))
        if mask: Es.append(sign*adj3(Q))
    return pp,Es
def score(K):
    ev=np.linalg.eigvalsh(K)
    if ev[0]<=1e-12 or ev[-1]>=1-1e-12: return None
    pp,Es=atom_data(K)
    if pp.min()<=1e-13: return None
    cc=np.array([math.log(pp[2]*pp[4]/(pp[0]*pp[6])),
                 math.log(pp[1]*pp[4]/(pp[0]*pp[5])),
                 math.log(pp[1]*pp[2]/(pp[0]*pp[3]))])
    tau=math.log(pp[0]*pp[3]*pp[5]*pp[6]/(pp[1]*pp[2]*pp[4]*pp[7]))
    Mm=np.diag(cc)+tau*K
    detm=float(np.real(np.linalg.det(Mm)))
    if detm<=1e-14: return None
    V=np.diag(pp[1:])-np.outer(pp[1:],pp[1:])
    T=np.empty((7,7)); vv=np.empty(7)
    for i,E in enumerate(Es):
        vv[i]=float(np.real(np.trace(Mm@E)))
        for j,F in enumerate(Es):
            T[i,j]=float(np.real(np.trace(Mm@E@Mm@F)))
    C=(T+T.T)/2+detm*V
    try:
        if np.linalg.eigvalsh(C)[0]<=1e-13: return None
        margin=float(vv@np.linalg.solve(C,vv)-2)
    except np.linalg.LinAlgError:
        return None
    return margin

def R_shape(rho, u3, q):
    rho3=math.sqrt(1-u3)
    u=1-rho*rho
    det_target=q*u*u*u3
    cosv=(det_target-1+rho3*rho3+2*rho*rho)/(2*rho3*rho*rho)
    if abs(cosv)>1: return None
    th=math.acos(max(-1,min(1,cosv)))
    return np.array([[1,rho3,rho*np.exp(-1j*th)],
                     [rho3,1,rho],
                     [rho*np.exp(1j*th),rho,1]],dtype=complex)
def K_from_R_x(R,xx):
    xx=np.array(xx,float); ell=xx/(1-xx)
    S=np.diag(np.sqrt(ell)); L=S@R@S
    return L@np.linalg.inv(np.eye(3)+L)

rng=np.random.default_rng(202609161846)
best=None; accepted=0; neg=0
for _ in range(6000):
    rho=rng.uniform(0.08,0.92)
    u3=10**rng.uniform(-8,-2)
    qv=rng.uniform(0.05,0.95)
    Rm=R_shape(rho,u3,qv)
    if Rm is None: continue
    xx=rng.uniform(0.08,0.92,3)
    Knum=K_from_R_x(Rm,xx)
    m=score(Knum)
    if m is None: continue
    accepted+=1
    if best is None or m<best: best=m
    if m < -1e-8: neg+=1

out={"exact_symbolic":exact,
     "numerical_diagnostic":{
        "status":"NUMERICAL_ONLY_NOT_GLOBAL_CERTIFICATE",
        "seed":202609161846,
        "requested":6000,
        "accepted":accepted,
        "negative_count":neg,
        "best_normalized_margin_s_minus_2":best,
        "domain":"tau>=0 shapes with rho1=rho2, u3 in [1e-8,1e-2], interior fields; targeted near u3=0 pair-degenerate face"
     }}
print(json.dumps(out,indent=2))
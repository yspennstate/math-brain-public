"""Exact algebra for X076's variable-channel curvature theorem.

The universal nonnegativity proof is in agents/X076.md.  This script checks
its rational/logarithmic identities and a full physical acceleration example.
"""
import json
from pathlib import Path
import sympy as s

OUT = Path(__file__).resolve().parent
checks = {}

def check(name, expression):
    expression=s.expand_log(expression,force=True)
    replacements={}
    for atom in expression.atoms(s.log):
        arg=atom.args[0]
        if arg.is_Rational and arg>0:
            numerator,denominator=arg.as_numer_denom()
            replacements[atom]=sum(exponent*s.log(prime) for prime,exponent in s.factorint(numerator).items())-sum(exponent*s.log(prime) for prime,exponent in s.factorint(denominator).items())
    value = s.factor(s.cancel(s.expand(expression.xreplace(replacements))))
    assert value == 0, (name, value)
    checks[name] = True

x, l = s.symbols("x l", positive=True)
w = x + l - 2*x*l
f = -(1-x)*(1-l)*(s.log(1-x)+s.log(1-l)) - x*l*(s.log(x)+s.log(l)) - w*(s.log(w)-s.log(2))
L = 2*s.log(w)-s.log(4)-s.log(x)-s.log(l)-s.log(1-x)-s.log(1-l)
A = (1-l)/(1-x) + l/x + (1-2*l)**2/w
B = 1/w-L
C = (1-x)/(1-l) + x/l + (1-2*x)**2/w
check("scalar_hessian_xx", s.diff(f,x,2)+A)
check("scalar_hessian_xl", s.diff(f,x,l)+B)
check("scalar_hessian_ll", s.diff(f,l,2)+C)

h,z,LL,TT = s.symbols("h z L T")
D=1+h*z
E=1+2*h*z+z*z
xx=(1-h)/2
ll=xx*(1-z)/D
ww=s.factor(xx+ll-2*xx*ll)
aa=s.factor(A.subs({x:xx,l:ll}, simultaneous=True))
cc=s.factor(C.subs({x:xx,l:ll}, simultaneous=True))
bb=1/ww-LL
rr=s.factor(cc-bb*bb/aa)
target_r=2*D/E*(D*(2*z*z/(1-z*z)+LL)-xx*(1-xx)*LL*LL)
check("transformed_A", aa-E/(2*xx*(1-xx)*D))
check("transformed_R",rr-target_r)
N=s.expand(2*D*D*(2*z*z/(1-z*z)+LL)-D*(1-h*h)*LL*LL/2-E*(TT+h*LL/2)**2)
check("quadratic_degree",s.diff(N,h,3))
U,V=s.symbols("U V")
Nv=s.expand(N.subs({LL:U-V,TT:(U+V)/2}))
plus=(1+z)**2*(4*z*z/(1-z*z)+2*(U-V)-U*U)
minus=(1-z)**2*(4*z*z/(1-z*z)+2*(U-V)-V*V)
middle=4*z*z-(1-z)*U*U-(1+z)*V*V+(1-z*z)*U*V+2*(1-z*z)*(U-V)
check("Bernstein_plus",Nv.subs(h,1)-plus)
check("Bernstein_minus",Nv.subs(h,-1)-minus)
check("Bernstein_middle",Nv.coeff(h,0)-Nv.coeff(h,2)-middle)
check("Bernstein_decomposition",Nv-(1+h)**2*plus/4-(1-h)**2*minus/4-(1-h*h)*middle/2)

t=s.symbols("t",real=True)
a=s.Rational(2,5); u=s.Rational(3,5); r=s.Rational(1,5); lam=s.Rational(1,3)
alpha=s.Integer(1); beta=s.Integer(1); radial=s.Integer(2); imag=s.Rational(1,7); delta=s.Rational(1,2)
at=a+t*alpha;ut=u+t*beta;lt=lam+t*delta
rhot=(r+t*radial)**2+t*t*imag*imag
pM=s.Matrix([(1-at)*(1-ut)-rhot,(1-at)*ut+rhot,at*(1-ut)+rhot,at*ut-rhot])
detdir=alpha*beta-radial**2-imag**2
for j,sign in enumerate([1,-1,-1,1]):
    check(f"active_acceleration_{j}",s.diff(pM[j],t,2)-2*detdir*sign)

def channel(q, parameter):
    mat=s.Matrix([[1-parameter,0],[parameter/2,(1-parameter)/2],[parameter/2,(1-parameter)/2],[0,parameter]])
    return (mat*q[:2,:]).col_join(mat*q[2:,:])

p_phys=channel(pM,lt)
q0=pM.subs(t,0);q1=s.diff(pM,t).subs(t,0)
p_affine=channel(q0+t*q1,lt)

def exact_Q(prob):
    p0=prob.subs(t,0)
    p1=s.diff(prob,t).subs(t,0)
    p2=s.diff(prob,t,2).subs(t,0)
    return sum(p1[j]**2/p0[j]+p2[j]*s.log(p0[j]) for j in range(len(p0)))

Qphysical=exact_Q(p_phys)
Qchannel=exact_Q(p_affine)
x1=u-r*r/a;x0=u+r*r/(1-a)
g=s.diff(f,x).subs({x:x1,l:lam})-s.diff(f,x).subs({x:x0,l:lam})
check("null_Lagrangian_compensation",Qphysical-Qchannel+2*g*detdir)

Qsq=0
sq_terms=[]
for offset in [0,2]:
    pp=q0[offset]+q0[offset+1]
    xp=q0[offset+1]/pp
    ppdot=q1[offset]+q1[offset+1]
    ep=(q1[offset+1]-xp*ppdot)/pp
    up=ppdot/pp
    ap=A.subs({x:xp,l:lam});bp=B.subs({x:xp,l:lam});cp=C.subs({x:xp,l:lam})
    vp=s.diff(f,l).subs({x:xp,l:lam})-s.log((1-lam)/lam)
    rp=cp-bp*bp/ap
    parts=[pp*(up-vp*delta)**2,pp*ap*(ep+bp*delta/ap)**2,pp*(rp-vp*vp)*delta**2]
    sq_terms.extend(parts)
    Qsq+=sum(parts)
check("physical_velocity_channel_squares",Qchannel-Qsq)

certificate={
    "exact_checks":checks,
    "number_exact_checks":len(checks),
    "example":{
        "active_kernel":[[str(a),str(r)],[str(r),str(u)]],
        "spectator":str(lam),
        "active_direction":[[str(alpha),str(radial-s.I*imag)],[str(radial+s.I*imag),str(beta)]],
        "spectator_direction":str(delta),
        "active_direction_determinant":str(detdir),
        "conditional_means":[str(x1),str(x0)],
        "physical_negative_Hessian":str(s.N(Qphysical,35)),
        "channel_square_sum":str(s.N(Qchannel,35)),
        "determinant_margin":str(s.N(-2*g*detdir,35)),
        "six_square_terms":[str(s.N(v,30)) for v in sq_terms],
    },
    "scope":"Universal scalar inequalities are proved analytically in X076.md; numerical displays do not replace their proof."
}
(OUT/"certificate.json").write_text(json.dumps(certificate,indent=2)+"\n")
print(json.dumps(certificate,indent=2))

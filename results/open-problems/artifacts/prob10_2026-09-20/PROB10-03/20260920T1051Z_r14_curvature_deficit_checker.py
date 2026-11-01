import math
import sympy as sp

# Exact symbolic backbone.
z,R,K,mu = sp.symbols("z R K mu", positive=True)
v = 1-z
psi = -z-sp.log(1-z)
G = sp.Rational(1,2)*(mu**2+v-1-sp.log(v))
assert sp.simplify(G-(mu**2/2+psi/2)) == 0

# Exact identity from tilted-Gaussian IBP plus the Brascamp--Lieb rearrangement:
# c=E[-r'], z=c-R, and R<=K/(1+K)c imply R<=K z.
c=sp.symbols("c", positive=True)
expr = sp.expand(K*(z+R) - (1+K)*R)
assert sp.simplify(expr-(K*z-R)) == 0

# Sharpness on quadratic Gaussian tilts phi=-a x^2/2+b x.
a,b=sp.symbols("a b", positive=True)
vg=1/(1+a)
mug=b/(1+a)
Rg=a**2/(1+a)
zg=1-vg
assert sp.simplify(zg-Rg/a)==0
Dg=sp.Rational(1,2)*(mug**2+vg-1-sp.log(vg))
psig=-zg-sp.log(1-zg)
assert sp.simplify(Dg-(mug**2/2+psig/2))==0

# Stationary complete-third substitutions.
m,d2,C,dq,L,q3,q2,s2,B = sp.symbols(
    "m d2 C dq L q3 q2 s2 B", positive=True)
tU = m*C*dq/L
outer_ref = d2*q3/2 + (-tU-sp.log(1-tU))/(2*m**2*C)
tH = C*(1-q2)/(2*B)
inner_ref = s2*q2/2 + (-tH-sp.log(1-tH))/(2*C)
assert sp.simplify(outer_ref-d2*q3/2 - (-tU-sp.log(1-tU))/(2*m**2*C))==0
assert sp.simplify(inner_ref-s2*q2/2 - (-tH-sp.log(1-tH))/(2*C))==0

print("EXACT_CURVATURE_DEFICIT_IDENTITIES_PASS")
print("EXACT_QUADRATIC_GAUSSIAN_SHARPNESS_PASS")

# Numerical-only falsification scout at the archived delta=1e-3 waypoint.
p2=0.967828984055228
p3=0.597722018031788
q2n=0.638663550092673
q3n=0.229918637629570
alpha=12.3164333569308
c2=12.52805599281815
c3=2.839127862412615
gp=3.153765242988234
Bn=39.26289564113617
mn=c3/c2
d2n=p2-p3
s2n=1-p2
Cn=c2*c2/alpha
Ln=2*Bn/(1+2*Bn*s2n)
tUn=mn*Cn*(q2n-q3n)/Ln
tHn=Cn*(1-q2n)/(2*Bn)
ps=lambda t:-t-math.log1p(-t)

Aq=2*gp-c2*(1-q2n)
Dq=Aq-c3*(q2n-q3n)
Ac3=(0.5*(p2*q2n-p3*q3n)
     -math.log(Dq/Aq)/(2*c3*c3)
     -(q2n-q3n)/(2*c3*Dq)
     -q3n*(q2n-q3n)/(2*Dq*Dq))
Ac2=(0.5*(1-p2*q2n)
     -math.log(Aq/(2*gp))/(2*c2*c2)
     -(1-q2n)/(2*c2*Aq)
     +(1-q2n)/(2*c3)*(1/Aq-1/Dq)
     -q3n*(1-q2n)/(2*Dq*Dq))
oldU=d2n*q3n/2
newU=oldU+ps(tUn)/(2*mn*mn*Cn)
oldH=s2n*q2n/2
newH=oldH+ps(tHn)/(2*Cn)
polyU=oldU+Cn*(q2n-q3n)**2/(4*Ln**2)
polyH=oldH+Cn*(1-q2n)**2/(16*Bn**2)
assert 0<tUn<1 and 0<tHn<1
assert newU>polyU>oldU and newH>polyH>oldH
assert Ac3>newU and Ac2>newH
print("NUMERICAL_ONLY_DELTA_1E3")
print("tU",repr(tUn),"Ac3",repr(Ac3),"old_lower",repr(oldU),"poly_lower",repr(polyU),"psi_lower",repr(newU),"slack",repr(Ac3-newU))
print("tH",repr(tHn),"Ac2",repr(Ac2),"old_lower",repr(oldH),"poly_lower",repr(polyH),"psi_lower",repr(newH),"slack",repr(Ac2-newH))
print("ALL_SELF_CHECKS_PASS")

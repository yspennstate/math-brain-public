from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 80
D = Decimal
M = 23

# Rounded Diaz source saddle used only for the fixed-outer diagnostic.
a = D("6.718433003118395")
nu_ps = D("1.2782018")
nu_ns1 = D("0.33277280")
ell_ns1 = D("0.5364470029682571")
q = D("0.74798692381442122423211536496280225427890493384178182525172855275624637824954579")
b = D("0.12788252751663062358618842906614360363910760429797021776854309368117468435113381")
source_base = (D(1)+D("1e-7"))*D("0.9999998965")
source_margin = -source_base.ln()

def dpow(x,n):
    y=D(1)
    for _ in range(n):
        y*=x
    return y

def delta_b(i,j):
    if i<j or j<1:
        return D(0)
    base=(-D(2)*a).exp()*dpow(a,i+j)/(D(factorial(i))*D(factorial(j)))
    return base*(D(2) if i>j else D(1))

delta=[D(0)]+[delta_b(i,1) for i in range(1,M+1)]
A=[D(0)]+[dpow(nu_ps,i) for i in range(1,M+1)]
B=nu_ns1
c=[D(0)]+[b*dpow(q,i)/(D(2)*ell_ns1) for i in range(1,M+1)]

f0=[D(0)]+[delta[i]*B/(A[i]+B) for i in range(1,M+1)]
t0=[D(0)]+[delta[i]*A[i]/(A[i]+B) for i in range(1,M+1)]
E0=sum(f0,D(0))
Phi0=sum((delta[i]*(A[i]+B).ln() for i in range(1,M+1)),D(0))
J_iid=sum((t0[i]*(-(D(1)-c[i]*E0).ln()) for i in range(1,M+1)),D(0))

def false_mass(E,z):
    return sum((delta[i]*(z*B)/(A[i]*(D(1)-c[i]*E)+z*B)
                for i in range(1,M+1)),D(0))

def solve_z(E):
    lo=D("1e-12")
    hi=D("1e12")
    assert false_mass(E,lo) < E < false_mass(E,hi)
    for _ in range(300):
        mid=(lo+hi)/D(2)
        if false_mass(E,mid)<E:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/D(2)

def derivative(E):
    z=solve_z(E)
    Den=[None]+[A[i]*(D(1)-c[i]*E)+z*B for i in range(1,M+1)]
    t=[D(0)]+[delta[i]*A[i]*(D(1)-c[i]*E)/Den[i] for i in range(1,M+1)]
    Dterm=sum((t[i]*c[i]/(D(1)-c[i]*E) for i in range(1,M+1)),D(0))
    return -Dterm-z.ln(), z, Dterm

def Phi(E):
    z=solve_z(E)
    return (sum((delta[i]*(A[i]*(D(1)-c[i]*E)+z*B).ln()
                 for i in range(1,M+1)),D(0))
            -E*z.ln())

# Bracket and solve the one-dimensional fixed-outer rescued inner optimum.
lo=E0*D("0.99")
hi=E0*D("1.01")
assert derivative(lo)[0] > 0
assert derivative(hi)[0] < 0
for _ in range(250):
    mid=(lo+hi)/D(2)
    if derivative(mid)[0] > 0:
        lo=mid
    else:
        hi=mid
E_star=(lo+hi)/D(2)
d_star,z_star,D_star=derivative(E_star)
Phi_star=Phi(E_star)
Delta_inner=Phi0-Phi_star
erosion=J_iid-Delta_inner

assert abs(d_star) < D("1e-70")
assert D(0) < Delta_inner < J_iid
assert Delta_inner/J_iid > D("0.999")
assert D("0.999") < z_star < D(1)
assert E_star < E0

print("PROB10_04_IID_PRIORITY_SCALARIZATION_DIAGNOSTIC")
print("ROUNDED_SOURCE_OUTER_SADDLE_ONLY_NOT_GLOBAL_ENDPOINT")
print("M =",M)
print("E_source =",E0)
print("J_iid_at_unreoptimized_split =",J_iid)
print("E_star_fixed_outer =",E_star)
print("z_star_fixed_outer =",z_star)
print("D_star =",D_star)
print("stationarity_residual =",d_star)
print("Delta_inner_after_exact_scalar_reoptimization =",Delta_inner)
print("reoptimization_erosion =",erosion)
print("fraction_of_J_iid_retained =",Delta_inner/J_iid)
print("published_rounded_source_log_margin =",source_margin)
print("Delta_inner/source_margin =",Delta_inner/source_margin)
print("ALL_SCALARIZATION_DIAGNOSTIC_CHECKS_PASS = True")

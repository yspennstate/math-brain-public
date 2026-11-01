from fractions import Fraction
import math, random
import mpmath as mp

mp.mp.dps = 50

def F(x):
    x = abs(mp.mpf(x))
    if x == 0:
        return mp.mpf("0")
    return x*x*mp.log(x)

def kernel_closed(a,b,c,d):
    x=a-b; u=a+b; y=c-d; v=c+d
    vals=[
        (1,x-y),(1,x+y),
        (-1,x-v),(-1,x+v),
        (-1,u-y),(-1,u+y),
        (1,u-v),(1,u+v),
    ]
    return sum(sig*F(lam) for sig,lam in vals)/16

def envelope(a,b,c,d):
    q=sorted(abs(mp.mpf(x)) for x in (a,b,c,d))
    q1,q2,q3,q4=q
    if q1 == 0:
        return mp.mpf("0")
    return q1*q2*(2-q3/(2*q4)+mp.log(q3/q2))-q1*q1/2

def quad_cut(a,b,c,d, cutoff=mp.mpf("1200")):
    fun=lambda s: mp.sin(a*s)*mp.sin(b*s)*mp.sin(c*s)*mp.sin(d*s)/(s**3)
    pts=[mp.mpf("0"),1,4,16,64,256,cutoff]
    total=mp.mpf("0")
    for lo,hi in zip(pts[:-1],pts[1:]):
        if hi>lo:
            total += mp.quad(fun,[lo,hi])
    return total, 1/(2*cutoff**2)

# Exact cancellation checks of the regularizers.
for a in range(-4,5):
  for b in range(-4,5):
    for c in range(-3,4):
      for d in range(-3,4):
        x=a-b; u=a+b; y=c-d; v=c+d
        vals=[
            (1,x-y),(1,x+y),(-1,x-v),(-1,x+v),
            (-1,u-y),(-1,u+y),(1,u-v),(1,u+v)
        ]
        assert sum(sig for sig,_ in vals)==0
        assert sum(sig*lam*lam for sig,lam in vals)==0

tests=[
    (1,.3,.8,.2),(1,.1,1,.1),(.7,.2,.43,.17),
    (1.436,1.424,.132,.173),(1.261,1.117,1.021,.497),
    (.929,.930,.893,.280),(.674,.621,1.098,1.492),
    (1.427,.839,.695,.439),(.392,.085,.521,.248)
]
max_err=mp.mpf("0"); max_env_ratio=mp.mpf("0")
for t in tests:
    kc=kernel_closed(*t)
    kn,tail=quad_cut(*t)
    err=abs(kc-kn)
    max_err=max(max_err,err)
    assert err < mp.mpf("3e-6")
    bd=envelope(*t)
    assert abs(kc) <= bd + mp.mpf("1e-40")
    if bd:
        max_env_ratio=max(max_env_ratio,abs(kc)/bd)

# PSD check from the closed kernel on a deterministic family.
pairs=[(.2,.7),(.4,.9),(.1,1.2),(.33,.51),(.8,1.1)]
M=mp.matrix([[kernel_closed(a,b,c,d) for c,d in pairs] for a,b in pairs])
eigvals=mp.eigsy(M,eigvals_only=True)
min_eig=min(eigvals)
assert min_eig > mp.mpf("-1e-40")

print("regularizer_cancellation_cases", 9*9*7*7)
print("numerical_formula_cases", len(tests))
print("max_formula_cutoff_error", mp.nstr(max_err,16))
print("cutoff_tail_bound_each", mp.nstr(1/(2*mp.mpf("1200")**2),16))
print("max_closed_over_envelope", mp.nstr(max_env_ratio,16))
print("psd_family_size", len(pairs))
print("min_closed_kernel_eigenvalue", mp.nstr(min_eig,16))
for eps in [mp.mpf("1e-1"),mp.mpf("1e-2"),mp.mpf("1e-3"),mp.mpf("1e-4")]:
    k=kernel_closed(1,eps,1,eps)
    lead=mp.mpf("0.5")*eps**2*mp.log(1/eps)+mp.mpf("0.75")*eps**2
    print("diag", mp.nstr(eps,6), "K/e^2", mp.nstr(k/eps**2,16),
          "remainder_over_e4", mp.nstr((k-lead)/eps**4,16))
print("PASS")

"""Independent algebra/derivative self-check for B12 region-2 two-block regrouping.

No certificate candidate is used.  This verifies only the exact analytic identities
behind r2_two_block_enclosure.py, not an FEI certificate.
"""
import json, random
import mpmath as mp

mp.mp.dps = 80
LN2 = mp.log(2)
random.seed(20260921)

# Arbitrary continuous nonmonotone PL G on a dense deterministic grid.
breaks = [mp.mpf(1) + mp.mpf(j)/8 for j in range(0, 321)]
vals = []
g = mp.mpf("9")
for j in range(len(breaks)):
    g += mp.mpf(str(random.uniform(-0.35, 0.55)))
    vals.append(g)

def seg_index(t):
    if t <= breaks[0]: return 0
    if t >= breaks[-1]: return len(breaks)-2
    lo, hi = 0, len(breaks)-1
    while hi-lo > 1:
        m=(lo+hi)//2
        if breaks[m] <= t: lo=m
        else: hi=m
    return lo

def G(t):
    i=seg_index(t)
    s=(vals[i+1]-vals[i])/(breaks[i+1]-breaks[i])
    return vals[i]+s*(t-breaks[i])

def Gp(t):
    i=seg_index(t)
    return (vals[i+1]-vals[i])/(breaks[i+1]-breaks[i])

def ell(v): return -mp.log(1-v)/v

def psi(z):
    w=(1-2*z)**2
    if w == 0: return mp.mpf(0)
    return -w*mp.log(w,2)/z

c=mp.mpf("0.003")
max_identity=mp.mpf(0)
max_margin=mp.mpf(0)
max_q_derivative=mp.mpf(0)
N=4000
for _ in range(N):
    x=mp.mpf(str(random.uniform(1.0001,1.9999)))
    y=mp.mpf(str(random.uniform(1.0001,18.0)))
    p=mp.power(2,-x); v=mp.power(2,-y)
    lam=-mp.log(1-v,2)
    def Ghat(t):
        r=mp.power(2,-t)
        return G(t)+c*(1-r)
    A=(Ghat(x)-Ghat(x+lam))/v
    B=Ghat(y)/(1-v)
    C=-8*p*x
    D=-8*(1-v)*(1-p)*ell(v)/LN2
    E=-8*(1-p)
    F=(psi(p)-psi(p*(1-v)))/v
    GG=psi(1-v)/v
    original=A+B+C+D+E+F+GG

    K0=lambda t: G(t)+psi(mp.power(2,-t))
    AF0=(K0(x)-K0(x+lam))/v
    CE=-8*(1+p*(x-1))
    Q=G(y)/(1-v)+D+GG
    grouped=AF0+c*(1-p)+CE+Q
    max_identity=max(max_identity,abs(original-grouped))

    Amargin=(c*(1-p)-c*(1-p*(1-v)))/v
    Bmargin=c*(1-v)/(1-v)
    max_margin=max(max_margin,abs((Amargin+Bmargin)-c*(1-p)))

    # Q derivative: use p itself as fixed p*; avoid PL nodes.
    def Qfun(t):
        vv=mp.power(2,-t)
        return (G(t)/(1-vv)
                -8*(1-p)*(1-vv)*ell(vv)/LN2
                +psi(1-vv)/vv)
    s=Gp(y)
    psip=mp.diff(psi,1-v)
    analytic=(s/(1-v)-LN2*v*G(y)/(1-v)**2
              +LN2*(psip+psi(1-v)/v)
              +8*(1-p)*(1-ell(v)))
    numerical=mp.diff(Qfun,y)
    max_q_derivative=max(max_q_derivative,abs(analytic-numerical))

out={
    "status":"SELF_CHECK_ONLY_NOT_CERTIFICATE",
    "samples":N,
    "mp_dps":mp.mp.dps,
    "max_grouped_identity_abs_error":mp.nstr(max_identity,12),
    "max_margin_extraction_abs_error":mp.nstr(max_margin,12),
    "max_q_derivative_abs_error":mp.nstr(max_q_derivative,12),
    "result":"PASS" if max_identity < mp.mpf('1e-60') and max_margin < mp.mpf('1e-60') and max_q_derivative < mp.mpf('1e-60') else "FAIL"
}
print(json.dumps(out,indent=2))

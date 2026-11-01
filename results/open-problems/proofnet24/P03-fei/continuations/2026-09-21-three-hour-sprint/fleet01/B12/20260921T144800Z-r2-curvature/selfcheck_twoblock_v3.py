"""Independent high-precision check of the B12 v3 J'' identity and curvature lemma.

This is not a production certificate: it uses arbitrary affine G segments rather
than the pinned value-iteration candidate.  It checks only the algebra/calculus
used by r2_two_block_enclosure_v3.py.
"""
import json, random
import mpmath as mp

mp.mp.dps=80
random.seed(20260921)
L=mp.log(2)

def phi(w):
    return mp.mpf("0") if w == 0 else -w*mp.log(w,2)

def psit(v):
    m=1-2*v
    return phi(m*m)/(1-v)

def ell(v):
    return -mp.log(1-v)/v

def J(x,p,s,g0,y0,y,c=mp.mpf("0.003")):
    v=mp.power(2,-y)
    G=g0+s*(y-y0)
    return (G/(1-v)+psit(v)/v+c*(1-p)-8*(1+p*(x-1))
            -8*(1-p)*(1-v)*ell(v)/L)

def Cyy(v):
    m=1-2*v
    N=2*v**3-2*v+(-4*v**2+3*v-1)*mp.log(m)
    return 2*L*N/(v*(1-v)**3)

def Jpp(x,p,s,g0,y0,y):
    v=mp.power(2,-y)
    G=g0+s*(y-y0)
    Bpp=-2*L*s*v/(1-v)**2 + L**2*v*G*(1+v)/(1-v)**3
    Dpp=8*L*(1-p)*(1/(1-v)-ell(v))
    return Bpp+Cyy(v)+Dpp

def Jp(x,p,s,g0,y0,y):
    return mp.diff(lambda z:J(x,p,s,g0,y0,z),y)

max_abs=mp.mpf("0")
max_rel=mp.mpf("0")
for _ in range(3000):
    x=mp.mpf(str(random.uniform(1,2))); p=mp.power(2,-x)
    y0=mp.mpf(str(random.uniform(1.001,25)))
    y=y0+mp.mpf(str(random.uniform(0,0.2)))
    s=mp.mpf(str(random.uniform(-35,35)))
    g0=mp.mpf(str(random.uniform(-10,60)))
    a=Jpp(x,p,s,g0,y0,y)
    b=mp.diff(lambda z:J(x,p,s,g0,y0,z),y,2)
    e=abs(a-b)
    max_abs=max(max_abs,e)
    max_rel=max(max_rel,e/(1+abs(b)))

# Check the convex quadratic lower-bound lemma and concave endpoint lemma
# numerically on smooth arbitrary affine-G cells.  Curvature signs are certified
# here by dense high-precision sampling only, so this block is an implementation
# sanity check, not interval proof evidence.
convex_cases=0; concave_cases=0; violations=0; best_gain=mp.mpf("0")
for _ in range(1200):
    x=mp.mpf(str(random.uniform(1,2))); p=mp.power(2,-x)
    y0=mp.mpf(str(random.uniform(1.02,12)))
    r=mp.mpf(str(random.uniform(1e-4,0.04)))
    yc=y0+r
    a=y0; b=y0+2*r
    s=mp.mpf(str(random.uniform(-25,30)))
    g0=mp.mpf(str(random.uniform(-5,45)))
    grid=[a+(b-a)*k/80 for k in range(81)]
    curv=[Jpp(x,p,s,g0,y0,t) for t in grid]
    vals=[J(x,p,s,g0,y0,t) for t in grid]
    true_grid=min(vals)
    if min(curv)>0:
        convex_cases+=1
        k=min(curv)*mp.mpf("0.999999999999")
        d=abs(Jp(x,p,s,g0,y0,yc))
        qlb=J(x,p,s,g0,y0,yc)-d*d/(2*k)
        mv=J(x,p,s,g0,y0,yc)-d*r
        if qlb>true_grid+mp.mpf("1e-55"):
            violations+=1
        best_gain=max(best_gain,qlb-mv)
    elif max(curv)<0:
        concave_cases+=1
        elb=min(J(x,p,s,g0,y0,a),J(x,p,s,g0,y0,b))
        if elb>true_grid+mp.mpf("1e-55"):
            violations+=1

print(json.dumps({
  "precision_digits":80,
  "derivative_trials":3000,
  "max_abs_Jpp_formula_error":mp.nstr(max_abs,18),
  "max_rel_Jpp_formula_error":mp.nstr(max_rel,18),
  "curvature_cell_trials":1200,
  "convex_sampled_cells":convex_cases,
  "concave_sampled_cells":concave_cases,
  "curvature_lemma_sampled_violations":violations,
  "largest_sampled_quadratic_vs_center_MVT_gain":mp.nstr(best_gain,18),
  "scope":"algebra/calculus sanity check only; not production certificate evidence"
},indent=2))

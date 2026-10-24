import itertools
import math
import numpy as np

TOL = 2e-10

def invariants(R, brute_D=True):
    n = R.shape[0]
    triples = list(itertools.combinations(range(n), 3))
    pairs = list(itertools.combinations(range(n), 2))
    v = {}
    for K in triples:
        d = np.linalg.det(R[list(K), :])
        v[K] = float(d*d)
    c = np.sum(R*R, axis=1)
    g = {}
    for i, j in pairs:
        g[(i,j)] = float(np.linalg.norm(np.cross(R[i], R[j]))**2)
    C2 = float(np.dot(c,c))
    G2 = sum(x*x for x in g.values())
    V2 = sum(x*x for x in v.values())
    if brute_D:
        D = 0.0
        for K,a in v.items():
            sK = set(K)
            for L,b in v.items():
                if sK.isdisjoint(L):
                    D += a*b
    else:
        D = 1-C2+G2-V2
    Wnorm = 0.0
    for S in pairs:
        ext = [v[tuple(sorted(S + (k,)))] for k in range(n) if k not in S]
        Wnorm += sum(ext)**2 - sum(x*x for x in ext)
    return {
        "v":v, "c":c, "g":g, "C2":C2, "G2":G2, "V2":V2,
        "D":D, "Wnorm":Wnorm,
        "sum_v":sum(v.values()), "sum_c":float(c.sum()), "sum_g":sum(g.values())
    }

rng = np.random.default_rng(20260923)
X = rng.normal(size=(8,3))
R = np.linalg.qr(X)[0]
inv = invariants(R, brute_D=True)
assert np.linalg.norm(R.T@R-np.eye(3), ord=2) < TOL
assert abs(inv["sum_v"]-1) < TOL
assert abs(inv["sum_c"]-3) < TOL
assert abs(inv["sum_g"]-3) < TOL
assert abs(inv["D"]-(1-inv["C2"]+inv["G2"]-inv["V2"])) < TOL
assert abs(inv["Wnorm"]-(inv["G2"]-3*inv["V2"])) < TOL
assert abs(inv["D"]-(1-inv["C2"]+inv["Wnorm"]+2*inv["V2"])) < TOL

print("random_frame")
print("C2=%.12f G2=%.12f V2=%.12f D=%.12f Wnorm=%.12f" %
      (inv["C2"],inv["G2"],inv["V2"],inv["D"],inv["Wnorm"]))

for m in (8,20):
    th = 2*np.pi*np.arange(m)/m
    Rc = np.zeros((m+1,3))
    Rc[0,0]=1.0
    Rc[1:,1]=math.sqrt(2/m)*np.cos(th)
    Rc[1:,2]=math.sqrt(2/m)*np.sin(th)
    ci = invariants(Rc, brute_D=True)
    assert np.linalg.norm(Rc.T@Rc-np.eye(3), ord=2) < TOL
    assert abs(ci["C2"]-(1+4/m)) < TOL
    assert abs(ci["D"]) < TOL
    assert abs(max(ci["g"].values())-2/m) < TOL
    print("coloop_m=%d C2=%.12f D=%.3e gmax=%.12f" %
          (m,ci["C2"],ci["D"],max(ci["g"].values())))

cross_const = 6*math.e*2**(1/3)
pair_const = 256*math.sqrt(6)
print("delta_1_4_cross_constant=%.12f" % cross_const)
print("delta_1_4_pair_constant=%.12f" % pair_const)
print("QFORM_B11_R35_COLLISION_STAR_CHECK_PASS")

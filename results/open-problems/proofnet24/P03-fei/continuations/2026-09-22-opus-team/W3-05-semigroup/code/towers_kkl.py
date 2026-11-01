"""KKL split along the towers of Numaro's g: K_d = int_0^1 Kgf_d(z)/z dz with
Kgf_d(z) = A_g(Z_{d-1}(z)) z Z_{d-1}'(z) + Z_g'(Z_{d-1}(z)) Kgf_{d-1}(z),
A_g(y) = sum_T w_g(T) (sum_{j in T} log(1/Inf_g(j))) y^{|T|-1}.  Check d=1 against the direct split."""
import math, numpy as np
from fei_core import Spec, load_numaro, LN2, lowprio
from towers import gate_polys_from_spec, peval
lowprio()
g = Spec.from_table(load_numaro()); Zc, Pc = gate_polys_from_spec(g)
K1, R1, inf = g.kkl_split()
li = -np.log(inf); s = np.zeros(g.ws.size)
for i in range(g.n): s += li[i]*((g.idx>>i)&1)
Ac = np.zeros(g.n+1)
for k in range(1, g.n+1):
    sel = g.ks==k; Ac[k-1] = (g.ws[sel]*s[sel]).sum()
def state(d, z):
    Z, Z1, Kg = z, 1.0, 0.0
    for _ in range(d):
        gz, gz1, _ = peval(Zc, Z); a, _, _ = peval(Ac, Z)
        Kg = a*z*Z1 + gz1*Kg
        Z1 = gz1*Z1; Z = gz
    return Z, Z1, Kg
xs, ws = np.polynomial.legendre.leggauss(400)
zs = 0.5*(xs+1); wz = 0.5*ws
out=[]
for d in range(1, 8):
    K = sum(wq*state(d, zq)[2]/zq for zq, wq in zip(zs, wz))
    st = state(d, 1.0); I = st[1]
    H = None
    out.append("d=%d I=%.6g K=%.6f K/I=%.6f log(1/minInf)*1=%.4f" % (d, I, K, K/I, d*math.log(1/inf.min())))
out.insert(0, "direct d=1: K=%.6f" % K1)
txt='\n'.join(out); print(txt); open('../logs/towers_kkl.log','w').write(txt+'\n')

"""Self-compositions g^(d) of a balanced gate g, by generating functions (no truth tables).

For balanced inner functions, w_F(union S_i) = w_G(T) prod w_f(S_i), hence with
  Z(z) = sum_S w(S) z^{|S|},   Psi(z) = sum_S w(S) log(1/w(S)) z^{|S|}
we have Z_d = Z_g o Z_{d-1} and Psi_d = Psi_g o Z_{d-1} + (Z_g' o Z_{d-1}) Psi_{d-1}  (Z_0 = z, Psi_0 = 0).
At z = e^{-2t}: E_t|S| = z Z'/Z, Var_t = (z^2 Z'' + z Z')/Z - E^2, Cov_t(|S|, L) = z Psi'/Z - E Psi/Z,
-dH(q_t)/dt = 2 Cov_t(|S|, L) + 4 t Var_t.   H = Psi_d(1), I = Z_d'(1).
Gates: Numaro's g (18 inputs) and MAJ3.
"""
import math
import numpy as np
from fei_core import Spec, load_numaro, LN2, lowprio

lowprio()


def gate_polys_from_spec(sp):
    n = sp.n
    Zc = np.zeros(n + 1); Pc = np.zeros(n + 1)
    for k in range(n + 1):
        sel = sp.ks == k
        Zc[k] = sp.ws[sel].sum()
        Pc[k] = (sp.ws[sel] * sp.L[sel]).sum()
    return Zc, Pc


def peval(c, y):
    """value, first and second derivative of polynomial with coefficients c at y."""
    v = d1 = d2 = 0.0
    for k in range(len(c) - 1, -1, -1):
        d2 = d2 * y + 2 * d1
        d1 = d1 * y + v
        v = v * y + c[k]
    return v, d1, d2


def tower_state(Zc, Pc, depth, z):
    # returns Z, Z', Z'', Psi, Psi' of g^(depth) at z
    Z, Z1, Z2, Ps, Ps1 = z, 1.0, 0.0, 0.0, 0.0
    for _ in range(depth):
        gz, gz1, gz2 = peval(Zc, Z)
        gp, gp1, _ = peval(Pc, Z)
        nZ = gz
        nZ1 = gz1 * Z1
        nZ2 = gz2 * Z1 * Z1 + gz1 * Z2
        nPs = gp + gz1 * Ps
        nPs1 = gp1 * Z1 + gz2 * Z1 * Ps + gz1 * Ps1
        Z, Z1, Z2, Ps, Ps1 = nZ, nZ1, nZ2, nPs, nPs1
    return Z, Z1, Z2, Ps, Ps1


def tilt_from_state(st, z, t):
    Z, Z1, Z2, Ps, Ps1 = st
    E = z * Z1 / Z
    V = (z * z * Z2 + z * Z1) / Z - E * E
    U = Ps / Z
    cov = z * Ps1 / Z - E * U
    return E, V, cov, 2 * cov + 4 * t * V, U + 2 * t * E + math.log(Z)


def main():
    lines = []
    P = lambda s: (lines.append(s), print(s, flush=True))
    g = Spec.from_table(load_numaro())
    gates = [("Numaro g", *gate_polys_from_spec(g), 7),
             ("MAJ3", np.array([0, 0.75, 0, 0.25]), np.array([0, 0.75 * math.log(4), 0, 0.25 * math.log(4)]), 12)]
    for name, Zc, Pc, dmax in gates:
        P("## tower of %s" % name)
        P("# d  n  I  H/I(bits)  H/(I-1)(bits) | t=0.25: E_t Var_t cov/Var (-dH/dt)/Var | t=1: E_t cov/Var")
        n1 = len(Zc) - 1
        for d in range(1, dmax + 1):
            st1 = tower_state(Zc, Pc, d, 1.0)
            H, I = st1[3], st1[1]
            row = "%2d %.3e %.6g %.6f %.6f" % (d, n1 ** d, I, H / I / LN2, H / (I - 1) / LN2)
            for t in [0.25, 1.0]:
                z = math.exp(-2 * t)
                E, V, cov, mdH, Hq = tilt_from_state(tower_state(Zc, Pc, d, z), z, t)
                row += " | t=%g: E=%.4f V=%.4g cov/V=%.4f mdH/V=%.4f Hq=%.4f" % (t, E, V, cov / V, mdH / V, Hq)
            P(row)
    with open('../logs/towers.log', 'w') as fh:
        fh.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()

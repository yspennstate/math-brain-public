"""The functional A(f) = E_{S ~ mu} log2(1 / up(S)), up(S) = sum_{U >= S} mu(U) = P[spectral sample covers S].

H = A + B with B = E_mu log2(up/mu). Checks:
  (1) A = H when the spectrum sits on one level (so "A <= C I" contains FEI for homogeneous spectra);
  (2) the tower law A(F(psi,...,psi)) = A(F) + I(F) A(psi) for balanced psi;
  (3) A/I, B/I, H/I on standard families.
Exact transforms, float64.
"""
import numpy as np

from predictor import wht, up_lam, f_and, f_maj, f_tribes, f_pmk33, compose, table_from


def parts(f, n):
    mu = wht(f) ** 2
    idx = np.arange(1 << n)
    pc = np.zeros(1 << n)
    for i in range(n):
        pc += (idx >> i) & 1
    I = float((pc * mu).sum())
    up = up_lam(mu, n, 1.0)
    m = mu > 1e-300
    H = float((mu[m] * np.log2(1.0 / mu[m])).sum())
    A = float((mu[m] * np.log2(1.0 / up[m])).sum())
    return I, H, A, H - A


def show(name, f, n):
    I, H, A, B = parts(f, n)
    print("%-28s n %2d  I %8.5f  H %8.5f  A %8.5f  B %8.5f   A/I %7.4f  B/I %7.4f  H/I %7.4f"
          % (name, n, I, H, A, B, A / I, B / I, H / I))
    return I, H, A, B


def main():
    # (1) homogeneous degree-2 Boolean function: f = x1 x2 if x2 = x3 else x4 x2
    hom = table_from(lambda b: np.where(b[1] == b[2], b[0] ^ b[1], b[3] ^ b[1]).astype(bool), 4)
    show("homogeneous deg 2", hom, 4)
    par = table_from(lambda b: (b[0] ^ b[1] ^ b[2]).astype(bool), 3)
    show("parity 3", par, 3)
    # (3) families
    for n in (3, 5, 9, 13):
        show("majority %d" % n, f_maj(n), n)
    show("AND 4", f_and(4), 4)
    show("tribes 2x3", f_tribes(2, 3), 6)
    show("tribes 3x4", f_tribes(3, 4), 12)
    pm = f_pmk33()
    Ip, Hp, Ap, Bp = show("PM(K33)", pm, 9)
    # (2) tower law
    m3 = f_maj(3)
    I3, H3, A3, B3 = show("maj3", m3, 3)
    f9 = compose(m3, 3, m3, 3)
    I9, H9, A9, B9 = show("maj3(maj3)", f9, 9)
    print("tower law maj3: A(F)+I(F)A(psi) = %.9f  measured %.9f" % (A3 + I3 * A3, A9))
    f12 = compose(m3, 3, hom, 4)
    I12, H12, A12, B12 = show("maj3(hom)", f12, 12)
    Ih, Hh, Ah, Bh = parts(hom, 4)
    print("tower law maj3(hom): %.9f  measured %.9f" % (A3 + I3 * Ah, A12))
    print("tower limits A(psi)/(I(psi)-1): maj3 %.6f   PM(K33) (if balanced; mean %.6f) %.6f   H-limit %.6f"
          % (A3 / (I3 - 1), float(pm.mean()), Ap / (Ip - 1), Hp / (Ip - 1)))


if __name__ == "__main__":
    main()

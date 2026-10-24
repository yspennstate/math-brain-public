#!/usr/bin/env python3
"""A08 exact finite-algebra certificate for T228_EXPLICIT_CLOSURE §§1–3.

Uses only Python's standard library and Fraction. There is no floating-point
arithmetic, numerical integration, parameter sampling, or third-party CAS.

The polynomial derivations encode the analytic identities tanh'=sech^2 and
(sech^2)'=-2 sech^2 tanh. Analytic facts (Gaussian integration, Holder,
Banach, Borel–Cantelli, convexity, weak convergence) are audited separately
in ../reviews/A08.md; this script is not a machine formalization of them.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path


EXPECTED_SHA256 = "a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f"
# A frozen byte-for-byte source prevents concurrent reviews from moving the
# target after it is checked. Sections 1–3 are unchanged from the first read.
PROOF = Path(__file__).with_name("A08_reviewed_source.md")
NAMES = ("x", "A", "z", "t", "u", "d", "E", "eta", "v", "r", "h", "R", "phi")
ZERO = (0,) * len(NAMES)
LINES = []


def emit(line):
    LINES.append(line)
    print(line)


class Poly:
    """Small exact multivariate polynomial ring over Q."""

    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {m: F(c) for m, c in value.items() if c}
        else:
            self.terms = {} if value == 0 else {ZERO: F(value)}

    @staticmethod
    def symbol(name):
        power = list(ZERO)
        power[NAMES.index(name)] = 1
        return Poly({tuple(power): F(1)})

    def __add__(self, other):
        result = dict(self.terms)
        for monomial, coefficient in Poly(other).terms.items():
            result[monomial] = result.get(monomial, F(0)) + coefficient
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        result = {}
        for left, a in self.terms.items():
            for right, b in Poly(other).terms.items():
                monomial = tuple(i + j for i, j in zip(left, right))
                result[monomial] = result.get(monomial, F(0)) + a * b
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = Poly(1)
        for _ in range(n):
            result *= self
        return result

    def __eq__(self, other):
        return self.terms == Poly(other).terms

    def diff(self, name):
        i = NAMES.index(name)
        result = {}
        for monomial, coefficient in self.terms.items():
            if monomial[i]:
                lower = list(monomial)
                lower[i] -= 1
                result[tuple(lower)] = coefficient * monomial[i]
        return Poly(result)

    def substitute(self, name, value):
        i = NAMES.index(name)
        result = Poly()
        for monomial, coefficient in self.terms.items():
            lower = list(monomial)
            lower[i] = 0
            result += Poly({tuple(lower): coefficient}) * Poly(value) ** monomial[i]
        return result


x, A, z, t, u, d, E, eta, v, r, h, R, phi = map(Poly.symbol, NAMES)


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    emit("PASS " + label)


def dz(poly):
    return poly.diff("z") + u * poly.diff("t") - 2 * u * t * poly.diff("u")


def dx(poly):
    return poly.diff("x") + A * dz(poly)


def absolute_envelope(poly):
    """Use |t|<=1, u<=1, |z|u<=1; retain d and |E| as symbols.

    All allowed inputs are polynomial sums in z,t,u,d,E. A z factor must
    have an accompanying u factor. After coefficientwise triangle bounds,
    E denotes |E| and d is nonnegative.
    """
    result = Poly()
    zi, ti, ui, di, ei = map(NAMES.index, ("z", "t", "u", "d", "E"))
    allowed = {zi, ti, ui, di, ei}
    for monomial, coefficient in poly.terms.items():
        assert all(power == 0 or index in allowed for index, power in enumerate(monomial))
        assert monomial[ui] >= monomial[zi]
        reduced = list(ZERO)
        reduced[di] = monomial[di]
        reduced[ei] = monomial[ei]
        result += Poly({tuple(reduced): abs(coefficient)})
    return result


def gaussian_moment(n):
    if n % 2:
        return F(0)
    result = F(1)
    for k in range(1, n, 2):
        result *= k
    return result


def gaussian_expectation(poly, name):
    i = NAMES.index(name)
    result = Poly()
    for monomial, coefficient in poly.terms.items():
        reduced = list(monomial)
        reduced[i] = 0
        result += Poly({tuple(reduced): coefficient * gaussian_moment(monomial[i])})
    return result


actual_hash = sha256(PROOF.read_bytes()).hexdigest()
emit("A08 exact checker: sections 1–3")
emit("Proof SHA256: " + actual_hash)
check("proof bytes match audited version", actual_hash == EXPECTED_SHA256)

# Section 1: formal differentiation under z=A*x, t=tanh(z), u=sech^2(z).
s = z + d * t
sp = 1 + d * u
spp = -2 * d * u * t
check("s' = 1+d*u", dz(s) == sp)
check("s'' = -2*d*u*t", dz(sp) == spp)
gradient_factor = sp * (s - E)
H = sp ** 2 - 2 * d * u * t * (z + d * t - E)
check("derivative of s'*(s-E) equals H", dz(gradient_factor) == H)
Psi = x - eta * A * gradient_factor
check("Psi' = 1-eta*A^2*H", dx(Psi) == 1 - eta * A ** 2 * H)
expanded_H = 1 + 2 * d * u + d ** 2 * u ** 2 - 2 * d * z * u * t - 2 * d ** 2 * u * t ** 2 + 2 * d * u * t * E
check("complete expansion of H", H == expanded_H)
check("coefficientwise |H-1| bound", absolute_envelope(H - 1) == 4 * d + 3 * d ** 2 + 2 * d * E)
check("1+r^2 >= 2*r via a square", 1 + r ** 2 - 2 * r == (r - 1) ** 2)
# Analytically cosh^2(z)=1+sinh^2(z)>=1+z^2>=2|z|, so |z|u<=1/2<=1.
check("s'*(s-E) remainder expansion", gradient_factor == z + d * z * u + (1 + d * u) * (d * t - E))
M = 1 - eta * A ** 2
remainder = -eta * A * (gradient_factor - z)
check("Psi=M*x+remainder under z=A*x", (Psi - M * x - remainder).substitute("z", A * x) == 0)
check("coefficientwise remainder bound B", absolute_envelope(gradient_factor - z) == d + (1 + d) * (d + E))
check("B bracket polynomial", d + (1 + d) * (d + E) == 2 * d + d ** 2 + (1 + d) * E)

# Section 2: exact certificates for the two elementary transcendental bounds.
# Machin: tan(4 atan(1/5)-atan(1/239))=1. The angle lies in (0,1),
# hence in (0,pi/2), since pi=4 int_0^1 1/(1+t^2)dt > 2.
tan_one = F(1, 5)
tan_two = 2 * tan_one / (1 - tan_one ** 2)
tan_four = 2 * tan_two / (1 - tan_two ** 2)
tan_difference = (tan_four - F(1, 239)) / (1 + tan_four * F(1, 239))
check("Machin tangent identity", tan_two == F(5, 12) and tan_four == F(120, 119) and tan_difference == 1)
check("Machin angle is in (0,1)", 4 * F(5, 26) - F(1, 239) > 0 and F(4, 5) < 1)
# atan(x)>x-x^3/3 and atan(x)<x for 0<x<1, by integrating the exact
# finite geometric-series remainder. Thus pi exceeds the following rational.
pi_certificate = 16 * (F(1, 5) - F(1, 5) ** 3 / 3) - 4 * F(1, 239)
pi_reference = F(157, 50)
check("pi > 3.14 from exact atan bounds", pi_certificate == F(281476, 89625) and pi_certificate > pi_reference)
e_certificate = sum((F(1, factorial(n)) for n in range(7)), F(0))
e_reference = F(1359, 500)
check("e > 2.718 from its first seven series terms", e_certificate == F(1957, 720) and e_certificate - e_reference == F(1, 18000))

# phi'=-A*phi. Gaussian moments follow by integration by parts.
gaussian_derivative = (A * phi).diff("A") - A * phi * (A * phi).diff("phi")
check("(A*phi(A))'=(1-A^2)*phi(A)", gaussian_derivative == (1 - A ** 2) * phi)
check("normal second and fourth moments", gaussian_moment(2) == 1 and gaussian_moment(4) == 3)
check("mean of 1-A^2 is zero", gaussian_expectation(1 - A ** 2, "A") == 0)
# Splitting at |A|=1 gives E|1-A^2|=4 phi(1)=4/sqrt(2*pi*e).
normal_absolute_upper = F(97, 100)
square_margin = normal_absolute_upper ** 2 * 2 * pi_reference * e_reference - 16
check("4/sqrt(2*pi*e) < 97/100", square_margin > 0)

delta = F(1, 1000)
eta_lo, eta_hi = F(99, 100), F(101, 100)
check("uniform |eta-1| <= 1/100", 1 - eta_lo == eta_hi - 1 == F(1, 100))
h1_upper = normal_absolute_upper + F(1, 100)
check("uniform h_eta(1) < 98/100", h1_upper == F(98, 100))
perturbation_upper = 6 * delta + 3 * delta ** 2
check("E|E|<1 perturbation coefficient", perturbation_upper == F(6003, 1000000))
q = h1_upper + eta_hi * perturbation_upper
check("exact q equals stated decimal", q == F(98606303, 100000000))
check("uniform q is strictly below one", 1 - q == F(1393697, 100000000) and q < 1)
quadratic = 1 - 2 * eta + 3 * eta ** 2
check("h_eta(2)=1-2*eta+3*eta^2", gaussian_expectation(M ** 2, "A") == quadratic)
check("uniform h_eta(2) minimum certificate", quadratic.substitute("eta", eta_lo + v) == F(19603, 10000) + F(197, 50) * v + 3 * v ** 2)
check("h_eta(2) is uniformly above one", F(19603, 10000) - 1 == F(9603, 10000) and F(197, 50) > 0)
check("uniform divergence witness: |A|>=2 implies |M|>2", eta_lo * 4 - 1 == F(74, 25) and F(74, 25) > 2)

# Optional strengthening: log L is actually finite, as L>=4d+3d^2>0.
c = 4 * delta + 3 * delta ** 2
check("strictly positive lower bound for L", 0 < c < 1 and c == F(4003, 1000000))
check("L lower bound for 0<=eta*A^2<=1", 1 - r + c * r - c == (1 - c) * (1 - r))
check("L lower bound for eta*A^2>=1", r - 1 + c * r - c == (1 + c) * (r - 1))

# Section 3: initial moment, explicit drift rate algebra, compact minorization.
psi_at_zero = Psi.substitute("x", 0).substitute("z", 0).substitute("t", 0).substitute("u", 1)
check("Psi(0)=eta*A*(1+d)*E", psi_at_zero == eta * A * (1 + d) * E)
drift_rate = (1 + h) * F(1, 2)
check("p>1 drift rate r=(1+h)/2<1 when 0<h<1", 1 - drift_rate == (1 - h) * F(1, 2))
geometric_sum = q / (1 - q)
check("Borel-Cantelli geometric series algebra", (1 - q) * geometric_sum == q and geometric_sum > 0)
sigma_lo = eta_lo
sigma_hi = 2 * eta_hi * (1 + delta)
check("uniform compact Gaussian scale bounds", sigma_lo == F(99, 100) and sigma_hi == F(101101, 50000) and 0 < sigma_lo < sigma_hi)
mean_bound = R + 2 * eta_hi * (1 + delta) * (2 * R + delta)
check("explicit compact mean bound", mean_bound == F(126101, 25000) * R + F(101101, 50000000))

emit("EXACT pi lower certificate = " + str(pi_certificate))
emit("EXACT e lower certificate = " + str(e_certificate))
emit("EXACT square margin for 0.97 bound = " + str(square_margin))
emit("EXACT q = " + str(q) + " = 0.98606303")
emit("EXACT 1-q = " + str(1 - q))
emit("EXACT min h_eta(2) = 19603/10000 = 1.9603")
emit("All " + str(sum(line.startswith('PASS ') for line in LINES)) + " exact checks passed.")
Path(__file__).with_suffix(".out").write_text("\n".join(LINES) + "\n")

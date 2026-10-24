# Exact scalar-kernel sharpening of the fixed-multiplicity theorem

For the pinned fixed-multiplicity manuscript at commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, retain the constants in the scalar-pivot half-potential calculation instead of rounding twice.

With (eta=1/100) and (L_0=4+4log16),
[
eta^{-1/2}(8+3L_0)
=200+120log16.
]
After the unit tail,
[
C_9=201+120log16.
]
The outer scalar pivot multiplies by (10), so the main theorem admits
[
oxed{C_{17}=2010+1200log16<5338}
]
instead of (10000).

Thus, for independent real variables with densities bounded by (K), arbitrary symmetric (A), arbitrary affine terms, and (s_{17}(A)ge s>0),
[
oxed{|p_{X^TAX+ell^TX+c}|_{infty,mathrm{ess}}
le (2010+1200log16)rac{K^2}{s}
<5338rac{K^2}{s}.}
]

The proof uses only conditional density caps, the square-root pushforward kernel, and the audited logarithmic convolution bounds. It does not add support, moment, sign, or independence-after-rotation assumptions. Continuity is not claimed here. The unrestricted (s_3) conjecture remains open.

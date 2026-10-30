# Addendum — all nonzero signed physical pivots via the rank-two half-Riesz receiver

This addendum strengthens the r24 sign compiler by actually applying the completed orientation-free rank-two fractional theorem at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

That theorem proves, for a quadratic form in two independent cap-one original coordinates with any invertible symmetric `2x2` matrix `K` and arbitrary affine term,

`sup_s E |Y^T K Y + ell^T Y-s|^(-1/2)
 <=16 sqrt(30)|det K|^(-1/4)`,                                    (A.1)

because in the two-coordinate application the affine term lies in the full rank-two range. The larger arbitrary-ambient affine constant `128` is therefore unnecessary here.

## A.1 Signed scalar-discriminant dichotomy

Keep the notation of the main report. Thus

`H=[[a,b^T],[b,C]]`

is an invertible ORIGINAL-coordinate physical `3x3` block and, after conditioning every outside original coordinate,

`Q=aX^2+2X(b^T Y+r)+Y^T C Y+2d^T Y+c`,                           (A.2)

where `X` is independent of the pair `Y=(Y_1,Y_2)`, and now `Y_1,Y_2` themselves are independent cap-one original coordinates.

For every target value `t`, scalar root inversion gives

`p_Q(t)
 <= E [D_t(Y)_+^(-1/2)]`,                                        (A.3)

with

`D_t(Y)=Y^T K Y+2(r b-a d)^T Y+r^2-a(c-t)`,
`K=bb^T-aC`.                                                      (A.4)

The determinant identity proved in the main report is

`det K=a det H`.                                                   (A.5)

Hence every **nonzero** physical scalar pivot `a` gives an invertible `K`. Since

`D_+^(-1/2)<=|D|^(-1/2)`                                         (A.6)

away from the null set `D=0`, the completed rank-two fractional estimate (A.1) applies directly to (A.4):

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(30)|a det H|^(-1/4).`                                 (A.7)

The bound is uniform in all outside couplings because those couplings only alter the affine parameters in (A.2).

This is `QFORM-NONZERO-PHYSICAL-PIVOT-HALF-RIESZ-v1`.

It is not claimed as a replacement for the source theorem; it is the exact scalar-discriminant application needed by B11.

## A.2 Signature tracking sharpens the minority branch

Assume now that `H` has inertia `(2,1)` or `(1,2)`.

- If `a` has the **minority** inertia sign, then `a det H>0` and the main report proves the much sharper elliptic-shell estimate

  `||p_Q||_infinity <=2 sqrt(pi)(a det H)^(-1/4)`.                (A.8)

  This estimate even allows `Y_1,Y_2` to be dependent, provided their joint density is capped.

- If `a` has the **majority** inertia sign, then `a det H<0`. The discriminant matrix `K` is itself indefinite. Its quadratic output can therefore retain the familiar rank-two logarithmic density singularity. Nevertheless the third scalar variable does **not** require a bounded density for that rank-two receiver. Scalar root inversion asks only for the fractional potential in (A.3), and (A.1) gives exactly the needed integrability. Thus

  `boxed:
   ||p_Q||_infinity <=16 sqrt(30)|a det H|^(-1/4)`               (A.9)

  on the majority-pivot branch.

This gives a particularly transparent answer to the B11 mechanism question. The third direction removes the opposite-sign logarithm in two different ways depending on the physical signature:

1. minority scalar -> elliptic two-dimensional discriminant shells, with `s^(-2)` superlevel area and a direct finite layer cake;
2. majority scalar -> the residual discriminant stays rank-two indefinite and may have an unbounded logarithmic density, but its `1/2`-Riesz potential is uniformly finite. The scalar-root Jacobian needs exactly that potential, not the residual `L^infinity` density.

In contrast, with only two variables the same scalar-root step leaves a one-dimensional discriminant and reaches the logarithmic endpoint.

## A.3 Consequence for a physical triple

For any invertible indefinite ORIGINAL-coordinate principal triple `H`, every nonzero physical diagonal is therefore a valid scalar pivot. If `a=H_ii`:

`||p_{X^TAX}||_infinity
 <= C_sign |a det H|^(-1/4)`,                                    (A.10)

where

`C_sign=2 sqrt(pi)` if `a` is the minority sign,
`C_sign=16 sqrt(30)` if `a` is the majority sign.                 (A.11)

Outside dimension, spectrum and couplings remain arbitrary.

The only scalar-completion endpoint not covered by (A.10) is an **exact zero physical pivot**. That endpoint is qualitatively different and is handled by the separate source-valid null-scalar/dependent-pair weak-`L^(3/2)` theorem when its hypotheses are met. Near-zero nonzero pivots remain quantitatively expensive in (A.10), so the global no-pivot problem still requires aggregation rather than selecting a tiny pivot.

## A.4 Partner comparison on the hidden-minority endpoint

For the designated fleet04/B11 frustrated endpoint

`C0=[[1,1,1],[1,1,-1],[1,-1,1]]`,

all three physical diagonals are majority-sign pivots and `|a det C0|=4`. The generic half-Riesz compiler (A.9) gives

`||p||_infinity <=16 sqrt(30)/sqrt(2)=8 sqrt(60)`                 (A.12)

whereas the completed partner theorem at `eta=0` gives the much sharper actual inequality

`||p||_infinity <=6 sqrt(pi)`.                                    (A.13)

Thus the partner geometry is not redundant with the fractional compiler: it sharply pays the all-majority sign-frustrated near-null chamber, while (A.9) supplies a robust all-orientation fallback whenever a quantitative nonzero pivot/determinant currency is available.

Full QFORM remains open; this addendum proves essential boundedness only in the stated physical-triple branches and does not establish continuity.

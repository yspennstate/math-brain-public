# Nonnegative four-cycle averaging coefficient on a two-state quotient

3 October2026. Exact finite proof of a restricted structural lemma; historical
novelty unverified. The unrestricted colored-coefficient problem is not solved.

Let A be any symmetric entrywise nonnegative2x2 kernel on two equal atoms,
and let B be any real symmetric2x2 kernel, with no domination restriction.
Write

    A=[[a,c],[c,d]], a,c,d>=0,
    B=[[u,w],[w,v]], u,w,v real.

On the ten-vertex Möbius ladder H, let the four edges of a selected square
carry B and its other eleven edges carry A. Then the corresponding colored
density is nonnegative. Therefore the total coefficient C4 in the binary-
coordinate expansion is nonnegative on this quotient.

## Exact quartic form

Summing all1024 assignments of the ten source vertices to the two atoms,
before dividing by2^10, gives a polynomial

    Q=Au(a,c,d)u^4+Av(a,c,d)v^4+f(a,c,d)w^4
           +w^2[C(a,c,d)u^2+D(a,c,d)v^2+E(a,c,d)uv].       (1)

These are the only possible B exponent types on a four-cycle. The number
of transitions between the two host labels around that cycle is even:
zero transitions gives u^4 or v^4; four transitions gives w^4; two
transitions gives w^2 times u^2,uv,or v^2.

Every coefficient polynomial in(1) has nonnegative integer coefficients,
because it groups products of eleven nonnegative A edge entries. The exact
counts of their nonzero terms are:

| Coefficient | Number of A monomials |
|:---|---:|
| Au |13|
| Av |13|
| f |16|
| C |17|
| D |17|
| E |18|

The exact determinant identity

    4 C(a,c,d)D(a,c,d)-E(a,c,d)^2                         (2)

has66 nonzero monomial coefficients and all are positive integers. It is
homogeneous of degree22; its minimum coefficient is24 and maximum16008.
Every term contains c^2. Its complete coefficient list is the field
`four_cd_minus_e_squared` in
`continuation_20261003_C4_twostate_discriminant.json`.
The six coefficient polynomials are in `quartic_coefficients` in that same
file. This is a complete exact polynomial certificate, not a numerical
PSD check.

Consequently C,D>=0 and E^2<=4CD throughout the nonnegative orthant. The
matrix [[C,E/2],[E/2,D]] is positive semidefinite, including the boundaries
C=0 or D=0. Thus the square-bracketed quadratic in(1) is nonnegative for
all real u,v. The three remaining fourth-power terms are nonnegative,
and w^2>=0, proving Q>=0. Division by2^10 preserves its sign. The five
squares of ML10 are rotation-equivalent, so totalC4 is five times this
colored density and is also nonnegative.

## Regeneration and limits

`continuation_20261003_C4_twostate_discriminant.py` reconstructs the source
edges and selected square, sums every one of the2^10 labelings, and groups
all A/B exponent histograms. It computes(2) by ordinary integer polynomial
multiplication and subtraction, independently of numerical transfer
optimization. All arithmetic is exact and every resulting coefficient is
saved. A separate exact audit, `C4_twostate_ant_independent_check.py`,
eliminates the five right labels after fixing each of the 32 left-label
assignments. It independently reconstructs all 1,024 source assignments,
all six grouped quartic coefficient polynomials, and the 66-term determinant
certificate. It matches the author calculation exactly; its saved report is
`C4_twostate_ant_independent_checks.json`.

This lemma includes arbitrary symmetric nonnegative A, not merely a
convolution base, and arbitrary symmetric signed B. It does not establish
the analogous PSD determinant inequalities in larger host dimension.
The global C4 reflection formula remains a trace(F B F B) sum whose
positivity must still be justified there. No implication to full ML10
Sidorenko is asserted from the two-state lemma alone.

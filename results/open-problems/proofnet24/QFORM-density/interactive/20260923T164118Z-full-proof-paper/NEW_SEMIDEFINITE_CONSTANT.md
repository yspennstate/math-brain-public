# Constant130 for a separated nonzero semidefinite spectrum

Status: proved below and in paper_work/semidefinite.tex, Theorem
sd:separated. This is not a claim of literature novelty.

Let X have independent coordinate densities bounded by one. Let A be
positive semidefinite of rank r>=3 with every nonzero eigenvalue at
least theta>0. For arbitrary linear b and constant c,

    ||p_(X^T A X+b^T X+c)||_infty <=130/theta.

Negative semidefinite A follows by reflection.

## Proof

Scale theta=1 and write A=R Lambda R^T with R^TR=I and Lambda>=I.
Every row leverage |r_i|^2 is at most a_ii. Use a one-coordinate pivot
if a_ii>=1/2. Its Schur complement has rank one less, remains positive
semidefinite, and has every nonzero eigenvalue at least one.

Otherwise all leverages are below1/2. Fresnel inversion, geometric
Brascamp--Lieb, and the integrated Fourier inequality
integral |psi|^p<=4pi/sqrt(p) give

    |phi_Q(t)| <=min(1,(4pi/|t|)^(r/2)).

The Gaussian-damped proof is Lemma sd:frame. It allows arbitrary linear
terms and arbitrary rough coordinate laws.

For j<=r the bound is at most min(1,(4pi/|t|)^(j/2)).
The Fejer kernel in Lemma sd:fejer gives

    alpha1 <=2sqrt(2)sqrt(4pi)/sin(1)^2 <15 (r>=1),
    alpha2 <=4pi/sin(1)^2 <18              (r>=2),
    ||p_Q||_infty <=12                    (r>=3)

in the absence of a pivot.

With a pivot, Q=a(X_i-m)^2+R has square-root profile
K=a^(-1/2)<=sqrt(2). Its first concentration level is <=4sqrt(2)<15.
Composition gives alpha2<=4sqrt(2)*sqrt(2)*15=120.
The inverse-half-moment bound, with alpha2(R)<=120, gives

    ||p_Q||_infty
      <=3sqrt(2)sqrt(120(3+log120))
      =129.6957291679615 <130.

All constants are independent of rank and dimension.

## Scope

This improves the recorded304 constant by reusing a sharper existing
composition inequality. It does not assume rank three, but DOES require
all nonzero eigenvalues>=theta, rather than merely lambda_3>=theta.
The arbitrary-rank lambda_3-normalized theorem with possibly tiny
remaining eigenvalues still has the separate constant17100.
The unrestricted indefinite conjecture remains open.

## Independent check of the grouped-crossing extension

The WS and GC derivations in research_work/structure_new.md were checked
separately. Complex pushforwards are bounded by unconditional projection
densities; no conditional-density bound is assumed. Smoothing the complex
light projection and applying conditional Cauchy--Schwarz in I cancels
M_I from the kernel convolution. The remaining difference variables
in J have independent cap-one densities.

Weighted Holder has exponents sum_(S containing i)w_S/alpha_i=1.
The joint projection Gram determinant is S_M^2 det(C_S C_S^T).
Entropy subadditivity gives the stated exp(ell/2) factor; the Fourier
and density constants in GC agree algebraically.

No gap was found in that extension under its explicit hypotheses.
It does not establish a uniform structural split for every matrix with
three large eigenvalues, and the small-leak parameter still degenerates.

## Exact definite rank-three constant58 and range-affine3e

The recorded arbitrary-affine rank-three constant82 is improved to58
in Theorem sd:rank-three. The entire proof is in semidefinite.tex.
No claim of literature novelty is made.

Scale the three nonzero same-sign eigenvalues to be at least one.
Write A=R Lambda R^T with R an orthonormal three-frame.
If every row leverage is at most1/2, the sharp diffuse Fourier
theorem gives density<=3e, including all original-coordinate affine
terms.

Otherwise a row leverage is greater than1/2, so its positive diagonal
pivot a is greater than1/2. The positive Schur complement has exact
rank two and both eigenvalues>=1. The revised exact-rank-two theorem
gives alpha2<=32sqrt2<46. Thus for any V>=1,

    ||p_Q||infty
      <=sqrt2 sup_s E|T-s|^-1/2
      <=sqrt2 [V+46(3+2logV)/V].

At V=20 this is57.5307287961<58.

If b belongs to range(A), translate each original coordinate to remove
the linear term. The heavy-pivot Schur remainder is then a positive
rank-two quadratic without a linear component outside its range.
Its two-dimensional orthogonal projection has densitycap2, and
its two eigenvalues>=1 give output density<=2pi. Retaining the occupied
side in the conditional square density gives

    p_Q(s)<=a^-1/2 E[(s-T)^-1/2 1_{T<s}].

For a density bounded by M, the one-sided expectation is at most
integral_0^infinity min(1,M t^-2)dt=2sqrtM.
The heavy branch is therefore <=4sqrtpi<3e.
Together with the diffuse branch this proves3e for every in-range
affine term. This latter bound is already in the source synthesis
and is reproduced with complete details, not asserted as a new result.

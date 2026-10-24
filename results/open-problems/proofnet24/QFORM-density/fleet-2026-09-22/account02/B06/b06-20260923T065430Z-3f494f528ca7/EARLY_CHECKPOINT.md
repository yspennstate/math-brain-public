SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T06:54:30Z.
attacking: a product-weighted receiver for the anchored double-star/one-null physical fiber, retaining arbitrary background quadratic curvature.

# Early substantive checkpoint

Full QFORM remains open. This checkpoint records two calculations to be proved fully in REPORT.md.

## 1. One-null weighted coupled-fiber estimate
Let X,Y be independent real variables with densities <=1 and independent of a background random object Omega. Let A(Omega), B(Omega), R(Omega) be arbitrary measurable real functions, assume B has a one-dimensional density bounded by L, and fix a!=0. Then

T=a X^2+2 A X+2 B Y+R

has an essentially bounded density with

||p_T||_infinity <= 6 L^(2/3) |a|^(-1/3).

Reason: condition on Omega. Completing the X-square gives a conditional density g with ||g||_(3/2)<=2|a|^(-1/3), uniformly in A. The density of 2BY has L^3 norm <=(2|B|)^(-2/3). Young L^(3/2)*L^3->L^infinity gives the conditional bound 2^(1/3)|a|^(-1/3)|B|^(-2/3). Bathtub under a density cap L gives E|B|^(-2/3)<=6*2^(-1/3)L^(2/3), yielding the stated constant. The arbitrary background term R is only a conditional translation.

For a quadratic form, if physical anchors i,j satisfy A_ii=a!=0, A_jj=A_ij=0, and sigma_j=(sum_{k notin{i,j}} A_jk^2)^(1/2)>0, the existing weighted affine-fiber Brascamp--Lieb theorem gives density cap sqrt(e)/sigma_j for B=sum_k A_jk X_k plus any outside affine shift. Therefore

||p_(X^TAX)||_infinity <= 6 e^(1/3) |a|^(-1/3) sigma_j^(-2/3),

with every remaining quadratic coefficient and coupling retained.

## 2. Why the opposite-sign two-nonzero-diagonal receiver cannot ignore the remainder
For independent cap-one X,U,Y,V uniform on [-1/2,1/2],

X^2-Y^2+2UX+2VY+(U^2-V^2)=(X+U)^2-(Y-V)^2.

The two sums have triangular densities positive at zero. Writing P=(X+U)-(Y-V), Q=(X+U)+(Y-V), the joint density of (P,Q) is continuous and positive at (0,0), so PQ has a logarithmically unbounded density at zero. Thus random linear coefficients do not by themselves regularize an opposite-sign anchor pair when arbitrary background quadratic curvature is allowed to recenter the two critical values. The third spectral direction must be consumed jointly in that branch. This refutes an intermediate receiver only, not full QFORM.

Source inputs to be pinned in the final report: account03/B06 r28 anchored Schur/double-star currency; account02/B06 weighted affine-fiber BL; newest-Claude coordinate-fiber/Fourier package at e5f71d79eff325201dd0274053d20268ce65b837.
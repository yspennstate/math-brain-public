# Square hub with a bilinear Schur receiver

Status: proved scoped theorem. The coefficient-dependent bound is not by itself an unrestricted spectral theorem.

## Abstract receiver

Let H,Y,Z be mutually independent real random variables with Lebesgue densities bounded by one. Let a,c be nonzero real numbers, u a real constant, phi(Y,Z) any measurable real function, and r(Y) any measurable real function. Then

Q=a(H+phi(Y,Z))^2+r(Y)+(cY+u)Z

has a density bounded by

||p_Q||_infinity ≤ 8/sqrt(|ac|).

The arbitrary vertex shift phi may involve both light variables and may be nonlinear. The residual r may contain an arbitrary Y-only potential.

Proof. For any density-cap-one H, any shift h_0, and any a nonzero, the density of a(H+h_0)^2 at a noncritical value v is at most 1/sqrt(|a v|), with zero density on the forbidden side. Thus, after conditioning on Y,Z and ignoring the side indicator,

p_{Q|Y,Z}(s)
 ≤ 1/sqrt(|a| |s-r(Y)-(cY+u)Z|).

A general rearrangement fact is that if W has a probability density bounded by N, then for every target t,

E |W-t|^(-1/2) ≤ 2sqrt(2N).

Indeed, the integral is maximized by placing density N on the centered interval of length 1/N; direct integration gives 2sqrt(2N).

Condition on Y. Except on a null event, cY+u is nonzero, and the scaled Z law has density cap N=1/|cY+u|. The rearrangement fact gives

E_Z |s-r(Y)-(cY+u)Z|^(-1/2)
 ≤ 2sqrt(2/|cY+u|).

The variable cY+u has density cap 1/|c|, so a second application gives
E_Y |cY+u|^(-1/2)≤2sqrt(2/|c|).
Combining the two inequalities proves 8/sqrt(|ac|). The estimates hold uniformly in s, phi, r, and u.

## Quadratic matrix interpretation

Let (H,Y,Z) be three physical independent originals with cap-one densities. Suppose the H-H quadratic coefficient is a nonzero and, after completing its square, the light residual is

r(Y)+(cY+u)Z

with c nonzero. Then the full quadratic-affine density obeys the displayed bound, regardless of the affine coefficients and the vertex shift. In matrix terms, if the 2 by 2 Schur complement of the physical H entry has one zero diagonal entry and a nonzero off-diagonal entry c/2, this receiver applies. Arbitrary couplings to other independent originals are allowed after conditioning them, provided the same principal three-input coefficients a and c remain fixed. The conditioned values only change affine terms and target shifts.

This hypothesis is different from a zero diagonal in the original physical matrix: the diagonal vanishes after the hub square is completed.

## A rank-three example with no zero physical diagonal and no definite pair

Take

A=[[1,1,1],
   [1,1,-1],
   [1,-1,1]].

Its eigenvalues are 2,2,-1, hence s_3(A)=1. Every physical diagonal is one. Every principal 2 by 2 determinant is zero, so the definite two-hub receiver does not apply. Nevertheless,

X^TAX=(X_1+X_2+X_3)^2-4X_2X_3.

Here a=1 and c=-4, so the density cap is 8/sqrt(4)=4. An arbitrary affine b_1X_1+b_2X_2+b_3X_3 remains in the receiver after completing the X_1 square: the residual becomes a Y-only affine term plus (-4Y+u)Z. Conditioning additional original inputs converts their cross terms with this triple into affine terms, so the same cap applies with arbitrary outside couplings.

## Boundary

The receiver's constant depends on |ac|. A global or principal-block condition s_3(A)≥1 does not automatically bound |ac| below for every Schur representation; other receivers may be needed when this product is small. A general symmetric matrix with s_3(A)≥1 is not covered by this result alone.

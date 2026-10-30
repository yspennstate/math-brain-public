# Exact calculation: one-sided carrier with a singleton third resource

## 1. General source-valid transfer

Let X in R^m, Y in R^n and W in R be disjoint ORIGINAL-coordinate product banks, all one-dimensional input densities <=1. Let C be a real m x n matrix with c=||C||op>0, let B=B^T be arbitrary, and let a!=0. Define

Q=2X^TCY+Y^TBY+aW^2+alpha^TX+beta^TY+dW+c0.

The completed fleet03/B18 theorem QFORM-ONE-SIDED-CROSS-SQUARE-LP-v1 applies with M=2C and G(Y)=Y^TBY+beta^TY. At q=3/2,

||p_Q||_infinity <= (12/2^(1/3)) (|a|c^2)^(-1/3).                 (1)

The theorem also gives a continuous C_0 density for this displayed standalone form. No independence is asserted for spectral rotations: the theorem uses only the disjoint original banks X,Y,W.

Let u,v be top singular vectors, Cv=cu and C^Tu=cv. If additionally Bv=0, then

A=[[0,C,0],[C^T,B,0],[0,0,a]]

has eigenvectors (u,+v,0)/sqrt(2), (u,-v,0)/sqrt(2), and the W basis vector, with eigenvalues c,-c,a. Thus c>=1 and |a|>=1 put the form in the exact owner target regardless of the rest of spec(B|v^perp). Equation (1) gives

||p_Q||_infinity <= 12/2^(1/3)=9.524406311809196... .             (2)

This gives a target-level closure with arbitrary high-rank and non-diagonal same-side curvature B, provided one top right cross direction lies in ker(B).

## 2. Exact stress family

Fix unit u in R^m and v in R^n and 0<epsilon<1. Set

C=uv^T,   B_epsilon=epsilon(I-vv^T),   a=1,

and

Q_epsilon=2(u^TX)(v^TY)+epsilon(||Y||_2^2-(v^TY)^2)+W^2.          (3)

The physical matrix A_epsilon has exact spectrum

{-1,1,1, epsilon (multiplicity n-1), 0 (multiplicity m-1)}.        (4)

Hence exactly three eigenvalues have modulus >=1. The nonzero high-rank tail epsilon(I-vv^T) is retained exactly; it is not deleted as a small random perturbation. From (2), for every m,n, every 0<epsilon<1 and every allowed product law,

||p_(Q_epsilon)||_infinity <= 12/2^(1/3) <9.525,                  (5)

and the standalone density is continuous and vanishes at infinity.

## 3. Every physical cross cut has rank at most two

Let I,J be arbitrary disjoint sets of ORIGINAL coordinates. Split I_X=I cap X, I_Y=I cap Y and likewise J_X,J_Y; W contributes no cross edge. The cross matrix A_epsilon[I,J] has rows of only two possible directions:

- for i in I_X, row_i = u_i [0_(J_X), v_(J_Y)];
- for i in I_Y, row_i = v_i [u_(J_X), -epsilon v_(J_Y)].

Therefore

rank A_epsilon[I,J] <=2                                             (6)

for every disjoint physical cut I,J, even though A_epsilon itself has three unit-scale eigenvalues and arbitrary additional epsilon-spectrum.

Consequences for the pinned e5f Fourier route:

- Theorem D has Z=e_3(A_IJ^T A_IJ)=0 for every physical cut, so its rank-three cross-volume certificate is unavailable identically, independent of its marginal gate.
- The D_5 extension likewise has Z_5=0 on every cut.
- At epsilon=0 the exact rank-three core has signature (2+,1-), so the pinned ruled one-sheet theorem gives p_(Q_0)(t)<=pi sqrt(2) for a.e. t>=0. This is a real target inequality, but it does not cover the epsilon>0 high-rank tail or the opposite sheet.

Thus (5) is not a fixed-minor or cross-volume consequence. It spends a genuinely disjoint third smoothing resource W^2 while allowing all Y-side curvature to remain inside G(Y).

## 4. Primary-source boundary

The only external probabilistic theorem used inside the fleet03/B18 receiver is Rudelson--Vershynin, arXiv:1402.4492, Theorem 1.2: if independent real variables have densities bounded by K and sum_j a_j^2=1, then the density of sum_j a_j X_j is bounded by sqrt(2) K a.e.; the constant is optimal. No moment, support, log-concavity, iid, centering, symmetry or smoothness condition appears. It is used only on original-coordinate product banks.

## 5. Remaining implication

The full conjecture remains open. This calculation closes the branch once one can expose an ORIGINAL-coordinate principal pattern consisting of: zero X-side quadratic curvature, a cross block C with c>=1, a disjoint scalar square |a|>=1, no W-(X,Y) retained cross edges, and one top right cross singular direction annihilated by B (the last condition only certifies that the retained pattern itself supplies the three target eigenvalues; the density bound (1) does not require it).

The first unpaid compiler question is to route an arbitrary surviving matrix into this pattern or prove that failure forces an already-paid ridge/grouped-cross/hub/volume branch. Small nonzero residuals cannot be dropped under the owner input class.

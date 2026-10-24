SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T00:42:18Z.
attacking: collective higher-rank Schur regularity; pay exact rank-two Schur residuals without post-rotation independence and isolate what fails as one residual curvature vanishes.

# Early checkpoint — collective rank-two Schur compiler

Status: supporting lemma proved; full QFORM remains open.

Let the two selected ORIGINAL coordinates be U=(X_i,X_j), the remaining original coordinates be Z, and write a quadratic-plus-affine form as

Q(U,Z)=U^T D U+2U^T BZ+Z^T C Z+b_U^T U+b_Z^T Z+c,

where D is an invertible indefinite 2x2 matrix. Put Delta=|det D| and kappa=sigma_min(D). Completing this pair only in the original coordinates gives

Q=(U+D^{-1}(BZ+b_U/2))^T D(U+D^{-1}(BZ+b_U/2))+R(Z),

where the quadratic part of R is the Schur complement S=C-B^T D^{-1}B and the affine part is arbitrary.

Assume rank(S)=2, with nonzero eigenvalues eta_1,eta_2. The completed orientation-free rank-two affine half-Riesz theorem at math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a gives

sup_t E |R-t|^{-1/2} <= 128 |eta_1 eta_2|^{-1/4}.

Therefore

sup_t P(|R-t|<rho) <= 128 |eta_1 eta_2|^{-1/4} sqrt(rho).

Feeding H=128|eta_1eta_2|^{-1/4} into the completed physical-pair logarithmic compiler at math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f yields the new collective estimate

||p_Q||_infinity <= 64 (Delta kappa)^(-1/4) |eta_1 eta_2|^(-1/8).                 (1)

This pays the two Schur eigenvalues collectively; it does not select a large physical Schur entry and it makes no independence claim after diagonalizing S.

There is a sharper homogeneous/range-affine same-sign branch. If eta_1 eta_2>0 and the affine part of R lies in Range(S), then after completing inside the two-dimensional spectral range the projected pair has joint density <=2, so the completed rank-two semidefinite theorem from the required e5f71d79... source gives

L:=||p_R||_infinity <= 2 pi / sqrt(|eta_1 eta_2|).                              (2)

Retain the full logarithmic pair envelope rather than downgrading (2) to a square-root small-ball bound. The pair theorem gives, for every r>0,

p_Q(t) <= 2 sqrt(2)/r + Delta^(-1/2) E log_+( 2r^2/(kappa |t-R|) ).             (3)

If a scalar R has density cap L, layer cake gives, with a=2r^2/kappa,

E log_+(a/|t-R|)
 = integral_0^infinity P(|t-R|<a e^{-v}) dv
 <= Phi(2La),

where Phi(A)=A for A<=1 and Phi(A)=1+log A for A>1. Taking r=sqrt(2 Delta), so 2La=8LDelta/kappa, gives

||p_Q||_infinity <= Delta^(-1/2) [2+Phi(8LDelta/kappa)]
 <= Delta^(-1/2) [3+log_+(8LDelta/kappa)].                                     (4)

Combining (2) and (4),

||p_Q||_infinity <= Delta^(-1/2)
  [3+log_+(16 pi Delta/(kappa sqrt(|eta_1 eta_2|)))].                           (5)

This is only logarithmic in a vanishing second same-sign Schur curvature, versus the power loss in (1).

Concrete owner-target test: Q_gamma=2XY+Z^2+gamma W^2, 0<gamma<=1, for four independent cap-one variables. Its eigenvalues are {1,-1,1,gamma}, so s_3=1. Choosing the hyperbolic pair (X,Y) gives Delta=kappa=1 and S=diag(1,gamma), so (5) gives 3+log(16pi/sqrt(gamma)), which deteriorates. But the required e5f71d79... Theorem A applied to the three-variable core 2XY+Z^2 gives ||p_(2XY+Z^2)||_infinity<=6sqrt(pi), and convolution with the independent law of gamma W^2 cannot raise L-infinity. Thus

||p_(Q_gamma)||_infinity <= 6 sqrt(pi)                                         (6)

uniformly in gamma. The residual-height summary loses the third smoothing resource even though the full target does not. This is an obstruction to that proof interface, not a counterexample to QFORM.

Next: determine whether the product provenance of a general same-sign rank-two Schur residual gives a square-root small-ball profile uniform through one vanishing eigenvalue, or whether one must retain the third resource jointly before any residual-height reduction. Keep the live near-zero-half-Riesz and two-sheet-X-ray corrections in force.

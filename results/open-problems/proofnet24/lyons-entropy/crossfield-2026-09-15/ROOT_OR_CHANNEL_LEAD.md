# Root lead — independent OR noise over active low-rank kernels

Status: exact channel identity and open compensated-curvature route. It is not a concavity proof. Root contribution, not an additional sub-agent.

Let D=diag(d_i), 0<=d_i<1, let B be a fixed n-by-r matrix, and let M>=0 vary affinely with K=D+B M B*<=I. Put V=(I-D)^(-1/2)B and N=V M V*. Then 0<=N<=I. If X has DPP kernel N and Y is an independent product-Bernoulli subset with probabilities d_i, their union Z=X union Y has exactly the DPP kernel K.

Proof: for every coordinate set S,

    P(Z intersect S=empty)
      =prod_(i in S)(1-d_i) det(I-N_S)
      =det(I-D_S-(BMB*)_S)=det(I-K_S).

Avoidance probabilities determine a finite subset law by inclusion-exclusion. This is a parameter-independent measured channel from a rank-r DPP to a full-rank kernel with fixed diagonal noise. V need not be an isometry; its fixed support still has dimension at most r, so rank-two support results apply to the input covariance.

Its conditional probabilities are explicit:

    C(z|x)=1_(x subset z) prod_(i in z minus x)d_i prod_(j outside z)(1-d_j).

The entropy identity is

    H(P_K)=H(P_N)+sum_i(1-Nii)h(d_i)-H(X|Z).

Indeed Z|X independently fills the coordinates outside X. This formula alone does not settle concavity: the changing posterior term has no automatic favorable sign, even though the middle term is affine. A generic entropy-data-processing claim must not be substituted for a curvature comparison.

For an affine active direction, write input score s_x=p'_x/p_x and acceleration a_x=p''_x/p_x. The channel gives output score E[s_X|Z] and acceleration E[a_X|Z]. Thus its exact entropy curvature is

    -H''(Z)=E[E(s_X|Z)^2]+E[a_X log P(Z)].

Subtracting the analogous input identity yields

    -H''(Z)=-H''(X)-E Var(s_X|Z)
             +E[a_X(log P(Z)-log P(X))].

All expectations use the fixed joint channel law. The final log expression is a joint random variable, not a replacement of the output law by a projection or spectral entropy. Consequently rank-two input concavity survives OR noise precisely when the lost Fisher information is paid by the displayed acceleration correction and any original strict margin. X001's marked erasure construction pays this automatically; independent OR noise is a concrete broader target for X061/X065/X066.

For singular atoms restrict to the constant positive support locally, or derive interior identities first and then take continuous probability limits. No atomwise derivative quotient is asserted at a changing zero.

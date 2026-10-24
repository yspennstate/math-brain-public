# Root continuation — the last swap-even channel comparison

This is an exact rewriting of X076, not an extra worker or a proof of the remaining sign. X072 and X076 leave only a definite active two-by-two velocity moving opposite to its spectator at a swap-symmetric three-site base. All measurements remain in the original coordinates.

Use a fixed coordinate phase gauge to make the active coupling r real and nonnegative. Write the active covariance as M=[[a,r],[r,u]], with spectator lambda. Put b=1-a, q=ab, rho=r², x1=u-rho/a, x0=u+rho/b. Let f(x,lambda) be the entropy of the four probabilities

    ((1-x)(1-lambda), (x+lambda-2x lambda)/2,
     (x+lambda-2x lambda)/2, x lambda).

The exact negative two-variable Hessian J(x,lambda) is given explicitly in X076. Set J_s=J(x_s,lambda),

    g=f_x(x1,lambda)-f_x(x0,lambda)>=0,
    k=f_lambda(x1,lambda)-f_lambda(x0,lambda),
    ell1=(rho/a², 1, -2r/a)^T,
    ell0=(rho/b², 1,  2r/b)^T,
    e=(1,0,0)^T.

For the real active velocity B=[[alpha,z],[z,beta]], let t=(alpha,beta,z)^T. Define

    H0=diag(1/q,0,0)
         +a J1_11 ell1 ell1^T+b J0_11 ell0 ell0^T,
    H=H0+diag(0,0,2g)-g(E12+E21),
    c=a J1_12 ell1+b J0_12 ell0-k e,
    d=a J1_22+b J0_22>0.

Substitution in X076 equation (1) gives the complete physical curvature

    -H''(B direct-sum delta)=t^T H t+2delta c^T t+d delta²
      =d(delta+c^T t/d)²+t^T(H-cc^T/d)t.

An imaginary component of the active off-diagonal velocity adds exactly 2g times its square and has no mixed terms. Thus the whole swap-even question is the explicit THREE-BY-THREE matrix inequality

    H-cc^T/d >= 0.

X076's jointly concave variable-channel theorem already proves

    R:=H0-cc^T/d >=0.

The sole extra obligation is the Lorentz determinant payment

    t^T R t >=2g(alpha beta-z²).

It is automatic for nonpositive active determinant, and the same-sign definite active/spectator case is covered by X015. No free replacement of measured Fisher information or omission of channel acceleration is present here. A sharp determinant coefficient of R, in the spirit of X068's two-site calculation, or an integrated logarithmic bound on this three-by-three matrix is a concrete next target. The displayed reduction itself does not establish that coefficient is at least g.

The case r=0 follows separately from the independent pivot and the two-site entropy theorem. Strict interior formulas and continuity handle any subsequently proved closed-domain extension. No assertion of full three-site or unrestricted Lyons concavity is made.


Update: X085 closes this entire full-Hessian comparison when the spectator BASE eigenvalue is 1/2, with arbitrary spectator velocity and arbitrary active block. Its exact endpoint inequality (5) is an equivalent reduction for the remaining arbitrary spectator base. See agents/X085.md for the positive decomposition and explicit gap.

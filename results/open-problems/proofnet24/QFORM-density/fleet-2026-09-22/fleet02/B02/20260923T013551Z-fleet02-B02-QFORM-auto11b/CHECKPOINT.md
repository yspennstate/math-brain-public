SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T01:35:51Z.
attacking: the first unpaid high-leverage/near-coloop Fourier collar using sharp D'/D5 and the designated fleet03/B02 exact-rank-three receiver.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## 1. Sharp-HY entropic D' compiler

Let `M=A[I,J]` be a physical cross block and let `mu` be ANY probability law on its nonzero physical `3x3` minors. Put

`K(mu)=exp(H(mu)+E_mu log det(M[S,T])^2)`,

and let `alpha_i=P_mu(i in S)`, `beta_j=P_mu(j in T)`. If `1<=q<3/2` and `alpha_i<=q/2` for every row, then the corrected determinant/BL proof plus sharp Hausdorff--Young gives

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] K(mu)^(-1/6)`.

More exactly the factor `e` can be replaced by

`[R_q(alpha) C(beta)]^(1/3)`,

where

`R_q(alpha)=prod_i (1-alpha_i/q)^(-(q-alpha_i)/2)`,
`C(beta)=prod_j (1-beta_j)^(-(1-beta_j)/2)`,

and `R_q C<=e^3`.

Proof calculation: after decoupling and Jensen,

`E F_t^q <= K(mu)^(-1/2) (pi/|t|)^3 q^(-3/2) R_q(alpha) C(beta)`.

Thus `|phi_Q(t)|<=min(1,B|t|^(-3/(2q)))`; exact inversion gives the displayed density bound. Same-side quadratic terms and outside couplings remain arbitrary. This extends the newest sharp-HY natural-volume theorem to the entropy-reweighted minor laws used by the current hub reductions.

At `h=5/8`, `q=5/4`, the clean coefficient is `12e/sqrt(5)=14.587831...`, improving the older entropic D' coefficient `24sqrt(e/5)=17.695934...`. With entropy budget `L=log 64`, the paid branch is therefore

`||p_Q||_infinity <= (24e/sqrt(5)) Z^(-1/6) =29.175663... Z^(-1/6)`.

## 2. Designated partner closes the doubly concentrated anchored terminal leaf

A fresh compatible fleet02/B07 result proves the following two-level concentration fact for an anchored third-minor packet of total squared mass `Z`: for any `h>1/2`, either one of the two residual-pair levels is `h`-diffuse, or one actual physical `3x3` cross minor `C` satisfies

`|det C|^2 > (2h-1)^2 Z`.

Condition on every original coordinate outside those six physical coordinates. The cross block is then exactly the invertible `3x3` matrix `C`. Apply the designated partner fleet03/B02 theorem `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1` (commit `484c89f85cda352b2c4318364a6206ebc4154950`):

`||p_Q||_infinity <=6 |det C|^(-1/3)`.

Therefore the terminal concentrated leaf satisfies the new actual inequality

`boxed: ||p_Q||_infinity < 6(2h-1)^(-1/3) Z^(-1/6).`

For the live anchored packet `Z>1/768` and `h=2/3`,

`||p_Q||_infinity < 6*3^(1/3)*768^(1/6) =26.186968...`.

This removes the no-pivot/principal-spectrum conversion previously used for that terminal leaf and improves its recorded bound `125.306` to `<26.187`. The partner theorem also supplies an `L^1` characteristic-function estimate, so this terminal branch has a continuous density.

## 3. Remaining interface after this checkpoint

The terminal double-concentration leaf is paid. The genuinely unpaid anchored branch is now the level-0/level-1 conditional-diffuse collar, where the fixed row/column anchors have marginal one and prevent direct D'. The next calculation is to determine whether its residual two-volume can be combined with the physical anchor pair by a dependence-safe fractional/pair receiver; arbitrary same-bank curvature prevents replacing the rectangular Schur aggregate by the full symmetric Schur remainder without proof.

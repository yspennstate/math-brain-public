# account01/B03 r15 — s8 compiler and review closure

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.
Run: 20260924T154801Z-account01-B03-fixedmult-audit-r15.

## Theorem candidate

For independent real coordinates with densities bounded by K, arbitrary real symmetric A, arbitrary b,c, and s_8(A)>=s>0,
||p_(X^TAX+b^TX+c)||_infinity < 2400 K^2/s.

This preserves all original assumptions and does not claim the unrestricted three-eigenvalue problem.

## Normalized proof

Set K=s=1 and use the s8 structural pivot scale eta=1/100.

### Pivot branches
A scalar pivot leaves at least seven Schur directions. The audited five-direction full-half-potential theorem from the nine/400 source is <115, so the outer square profile costs at most eta^(-1/2)=10 and gives density <1150.

A definite two-coordinate pivot with determinant modulus >=eta gives density <=pi/sqrt(eta)<40.

An indefinite pair with determinant modulus D>=eta leaves at least six Schur directions. The quarter-power/log-potential estimate gives
D^(-1/2)(6+log16+L0)+1/e <199
using log16<3 and L0=4+4log5<54/5.

### No pivot: large third volume
Use kappa=1/6400. The s8 terminal reduction gives either V3>=kappa^3 or the robust collar below. In the first case a fair literal coordinate cut gives Z3>=4^(-3)kappa^3, hence Z3^(-1/6)<=160. The marginal-free q=3 receiver gives density <15*160=2400 and a C0 density.

### Robust collar
The good-seed/two-sided collar produces a literal original-coordinate pair H, complement L, C=A[H,L], with
g=det(CC^T)>=delta_*^2/2>8/25.

Put Q_C=C^T(CC^T)^(-1)C, q_i=(Q_C)_ii and J={i:q_i>2/3}. Since Q_C is a rank-two orthogonal projection, |J|<=2.

For low-leverage coordinates set P=I-Q_C, r_i=d_iP and choose lambda_i=r_ii/(1-q_i). The exact anchored disjoint-minor identity gives an error E with zero diagonal and
||E||_F^2 <= 3 W_dis/g.

If |J|<=1 and W_dis<=g/48, then ||E||_F<=1/4. The residual has global rank <=4+|J|<=5 and restricted low-coordinate rank <=2. Singular-value perturbation from s_8(A)>=1 forces at least three low diagonal coefficients |lambda_i|>=3/4. On those coordinates
|R_ii|>=0.74,
sum_(j!=i)|R_ij| < 2(sqrt(0.0101)+1/4)<0.701.
Strict diagonal dominance forces rank three, contradicting restricted rank <=2. Therefore W_dis>g/48.

The product-safe disjoint incident-volume receiver then gives
||p_Q||_infinity <= C_inc W_dis^(-1/6),
C_inc=3*2^(5/6)*e^(2/3),
and with the source value g>=0.3649442658... the bound is <23.48. This branch has C0 density.

### Two-high endpoint is empty
If J={i,j}, write w_ab=det(C_ab)^2/g. Cauchy-Binet gives sum w_ab=1 and the projection marginals give q_i=sum_(b!=i) w_ib. Hence
w_ij >= q_i+q_j-1 >1/3
and det(C_ij)^2>g/3>8/75.

No-pivot entry bounds give |A_uv|^2<eta^2+eta=101/10000 for every physical off-diagonal entry. All four entries of C_ij are off diagonal, so
|det C_ij|<101/5000,
det(C_ij)^2<10201/25000000<8/75,
a contradiction.

Thus all no-pivot states close.

## Scaling
For general K,s put Y=KX and
Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
Then s_8(A/s)>=1 and Q=(s/K^2)Qtilde, giving the factor K^2/s.

## Review state
This is a complete B03 reconstruction. A genuinely separate complete PASS review of the same s8 chain exists at account03/B08, audits/account03/B08/20260924T151825Z-account03-B08-s8-full-review-r59/AUDIT.md. Thus the requested count of two separate mathematical end-to-end reviews is present. Owner-level release/validation remains a distinct decision.

Current lower frontier: no closed s7 theorem located. Existing s7 artifacts establish structural overlap/collar information but still lack the product-preserving analytic receiver needed for a full arbitrary-law density theorem. The unrestricted s3 conjecture remains open.

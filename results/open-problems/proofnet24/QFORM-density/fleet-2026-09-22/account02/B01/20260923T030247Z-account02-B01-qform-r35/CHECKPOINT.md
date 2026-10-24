SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T03:02:47Z.
attacking: the critical two-row volume endpoint by replacing the failed h<1 Jensen limit with projected-slope L2/Plancherel smoothing, then spending an independent third square on a strict-N3 dense-leaf family.

# Early checkpoint: two-physical-hub critical half-Riesz endpoint

Programme: QFORM-DENSITY-3EIG-20260922. Run: `20260923T030247Z-account02-B01-qform-r35`.
Status: supporting target-level theorem; full QFORM remains OPEN.

## Theorem (critical two-row half-Riesz)
Let X=(X1,X2) and Y=(Y1,...,Ym) have mutually independent real coordinates, each with density at most one. Let C be any real symmetric 2x2 matrix, M any real 2xm matrix of rank two, c in R2 fixed, and R(Y) any real measurable function finite a.s. Put

S = X^T C X + 2 X^T(MY+c) + R(Y),
D = det(M M^T)>0.

Then

H_{1/2}(S):=sup_s E|S-s|^{-1/2} <= 2^(11/4) D^(-1/8).

No condition is imposed on C or R. In particular arbitrary quadratic curvature and affine terms among the Y variables are allowed.

### Proof
Write, for t != 0,

F_t(u)=int_{R2} f1(x1)f2(x2) exp(it x^T Cx + 2it u.x) dx.

If g_t(x)=f1(x1)f2(x2)exp(it x^T Cx), then under the Fourier convention ghat(xi)=int exp(i xi.x)g(x)dx,

F_t(u)=ghat_t(2tu).

The two-dimensional product-projection theorem used in the current Claude report gives the density p of MY+c the cap

||p||_infinity <= 2 D^(-1/2).

Hence ||p||_2 <= sqrt(2) D^(-1/4). Since |exp(it R(Y))|=1,

|phi_S(t)| <= E |F_t(MY+c)| <= ||p||_2 ||F_t||_2.

Plancherel and fi<=1, int fi=1 give

||F_t||_2^2 = (2|t|)^(-2) int |ghat_t(xi)|^2 dxi
            = pi^2 |t|^(-2) int f1(x1)^2 f2(x2)^2 dx
            <= pi^2 |t|^(-2).

Therefore

|phi_S(t)| <= min(1, pi sqrt(2) D^(-1/4)|t|^(-1)).                 (1)

For alpha=1/2, the Riesz identity

|x|^(-1/2)=sqrt(2/pi) int_0^infty cos(tx)t^(-1/2)dt

is legitimate after expectation because (1) makes the weighted characteristic-function integral absolutely convergent. Thus, with K=pi sqrt(2)D^(-1/4),

H_{1/2}(S)
 <= sqrt(2/pi) int_0^infty t^(-1/2)min(1,K/t)dt
 = 4 sqrt(2/pi) sqrt(K)
 = 2^(11/4)D^(-1/8).

This is the exact `h=1` two-row endpoint where account03/B01's completed volume-marginal theorem has q=2 and denominator 2-q=0. The mechanism changes: it uses the L2 density of the jointly projected slope (MY)_1,(MY)_2 and Plancherel in the two physical hub variables, not a scalar quadratic-phase envelope.

## Physical third-pivot corollary
Let k,i,j be distinct original coordinates of a quadratic form, with a=A_kk !=0. Complete the square in X_k and let S be the Schur residual. If the 2 x (n-3) matrix M consisting of the i,j rows of the Schur residual against the remaining original coordinates has rank two, then

||p_Q||_infinity <= 2^(11/4)|a|^(-1/2) det(MM^T)^(-1/8).

This is the source square-peel inequality followed by the theorem above. It retains all other Schur curvature and all affine leakage.

## Strict-N3 dense-leaf stress family to be completed in the final report
For m large, two physical hubs coupled at size ~m^(-1/2) to two disjoint banks have MM^T comparable to I2 while every physical pair determinant is O(1/m). Add a full-rank dense leaf self-block with entries O(m^(-1/2)) and an independent delocalized square on a third bank. The theorem above ignores the dense leaf self-block, while the independent square converts H_{1/2} into a bounded density. The final report will record the exact constants, spectral check and the comparison with the newest source Theorem H and account03/B01.

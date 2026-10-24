# account02/B04 — product rearrangement: pure-cross triple closure

Run: `account02-B04-20260922T122057Z-01c809a1`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The owner target is unchanged: for arbitrary independent real inputs with densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, diagonal-basis, or post-rotation-independence assumption is used below.

The first unpaid implication after the present run is global rather than local:

> **QFORM-MIXED-LEVERAGE-AGGREGATION.** Combine the proved diffuse rank-three branch, the nonzero scalar-pivot Schur bounds, and the zero-diagonal pure-cross bound proved here into a dimension-free argument from the sole spectral hypothesis `A` has at least three eigenvalues `|lambda|>=1`. A fixed coordinate triple can have arbitrarily small determinant, so a one-minor selection argument is not enough.

This is the same global aggregation frontier identified independently by account01/B11 after its binary-indefinite and Schur-pivot theorem. The present report pays its explicit local all-zero-diagonal `3x3` exception and gives a separate overlapping shifted-square estimate.

## 2. Corrections and source dependencies consumed

Fresh owner controls and the live correction inbox were read before publication. In particular this report does **not** use the false law-uniform pointwise quadratic-phase decay, a cross minor by itself, a two-sheet X-ray cap by itself, post-rotation independence, or a universal constant `pi`.

Named partner actually applied:

- account03/B04, canonical report `yspennstate/math-open-problems@f824ded997ee16c741468bb49860e1ccaf18d8bd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/a03-b04-20260922T115126Z-qform-r11/REPORT.md`, blob `2438594f82b064359483972f59f4d061a6814ce0`. It proves, for a density-`<=M` scalar `Y`,
  `|| E exp(i t lambda Y^2) ||_{L^3(dt)} <= 2(2pi)^(1/3) M^(2/3)|lambda|^(-1/3)`.

Other compatible completed result actually used:

- account01/B11, canonical report `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`, blob `17a44fbdfb6c987ed46e2e76833c60497b33f025`. It proves determinant-scale `L^3` control for every nondegenerate indefinite binary quadratic and closes both signs of every nonzero scalar pivot via Schur smoothing, while explicitly leaving the invertible all-zero-diagonal physical `3x3` block as a local scalar-pivot exception.

## 3. A genuinely overlapping shifted-square theorem

### Theorem 3.1 — `QFORM-SHIFTED-SQUARE-PRODUCT-REARRANGEMENT-v1`

Let `X,Y,Z` be independent real variables with densities bounded by one. Let `a,gamma` be nonzero reals and `alpha,beta` arbitrary. Then

`Q = a (Z-alpha X-beta Y)^2 - gamma X Y`

has an essentially bounded density and

`||p_Q||_infinity <= 4 sqrt(2) / sqrt(|a gamma|)`.

No independence is asserted after rotating to the quadratic-form eigenbasis.

### Proof

Reflection of the output lets us assume `a>0`. Condition on `X=x,Y=y`. Translation of `Z` preserves its density cap, and the pushforward of a density-`<=1` variable by `a z^2` has density at most

`a^(-1/2) s^(-1/2) 1_{s>0}`.

Therefore

`p_Q(t) <= a^(-1/2) integral f_X(x) f_Y(y) (t+gamma x y)_+^(-1/2) dx dy`.   (3.1)

Fix `x!=0`. The random variable `W=t+gamma xY` has density bounded by

`M_x=1/(|gamma x|)`.

For every probability density `h<=M`, the decreasing-rearrangement/bathtub inequality gives

`integral_0^infinity s^(-1/2)h(s)ds <= 2 sqrt(M)`.   (3.2)

Indeed the decreasing weight is maximized by filling the interval `(0,1/M)` at height `M`.

Applying (3.2) to the inner `y` integral in (3.1) yields

`p_Q(t) <= 2/(sqrt(|a gamma|)) integral f_X(x)|x|^(-1/2)dx`.

A second bathtub inequality, now for the even decreasing rearrangement of `|x|^(-1/2)`, gives

`integral f_X(x)|x|^(-1/2)dx
 <= integral_{-1/2}^{1/2}|x|^(-1/2)dx
 = 2 sqrt(2)`.

Hence the claimed bound follows uniformly in `t`.

### Explicit fully overlapping indefinite instance

Take `a=1`, `alpha=beta=1`, `gamma=4`. Then

`Q_0=(Z-X-Y)^2-4XY
   =X^2+Y^2+Z^2-2XY-2XZ-2YZ`.

Its matrix is `A_0=2I-J`, whose eigenvalues are `2,2,-1`. Thus it is a genuinely rotated indefinite target form with every coordinate participating in every spectral direction, and

`||p_{Q_0}||_infinity <= 2 sqrt(2)`.

This estimate uses the original product law directly and never multiplies rotated marginals.

### Named-partner theorem applied to an actual inequality

For fixed `(x,y)` define

`F_{x,y}(t)=E_Z exp(i t a(Z-alpha x-beta y)^2)`.

The account03/B04 theorem applies uniformly to the translated density of `Z` and gives

`||F_{x,y}||_3 <= 2(2pi)^(1/3)|a|^(-1/3)`.

Since

`phi_Q(t)=E_{X,Y}[ exp(-it gamma XY) F_{X,Y}(t) ]`,

Minkowski gives the genuine overlapping Fourier estimate

`||phi_Q||_3 <= 2(2pi)^(1/3)|a|^(-1/3)`.   (3.3)

Equation (3.3) is not promoted to an `L^1` characteristic-function bound; the density theorem above is instead proved by product-space rearrangement. This distinction avoids the known false pointwise-decay route.

## 4. Product-density logarithmic envelope

The second theorem attacks the exact all-zero-diagonal physical-triple exception left by account01/B11.

### Lemma 4.1 — product logarithmic envelope

If `U,V` are independent with densities at most one and `P=UV`, then for every `s!=0`,

`p_P(s) <= 4 log(1+1/(2 sqrt(|s|)))`.   (4.1)

### Proof

The product density has the usual version

`p_P(s)=integral f(u)g(s/u) du/|u|`.

Put `r=sqrt(|s|)` and split into `|u|>=r` and `|u|<r`. On the first set, discard `g<=1`:

`I_1 <= integral_{|u|>=r} f(u)du/|u|`.

Among densities `0<=f<=1` of mass one, the latter is maximized by filling the measure-one set nearest the two boundary points `+-r`, so

`I_1 <= 2 integral_r^{r+1/2} du/u
     =2 log(1+1/(2r))`.

On `|u|<r`, substitute `v=s/u`. Then `du/|u|=dv/|v|` and `|v|>r`, so the same argument with `g` gives the same bound. Summing proves (4.1).

Consequently, for `W=2cUV`,

`p_W(w) <= (2/|c|) log(1+ sqrt(|c|/2)/sqrt(|w|))`.   (4.2)

The logarithmic singularity is retained rather than falsely bounded; the third original coordinate will integrate it.

## 5. Pure-cross `3x3` theorem

### Theorem 5.1 — `QFORM-PURE-CROSS-TRIPLE-v1`

Let `X,Y,Z` be independent real variables with densities bounded by one and let `a,b,c` be nonzero. Put

`Q=2aXY+2bXZ+2cYZ`.

Let

`B=[[0,a,b],[a,0,c],[b,c,0]]`, so `det B=2abc`.

Then `Q` has an essentially bounded density satisfying the determinant-scale estimate

`||p_Q||_infinity <= C_cross |det B|^(-1/3)`,   (5.1)

where the explicit universal constant is

`C_cross = 2^(4/3) [ log(1+sqrt(2)) + sqrt(2) log(1+1/sqrt(2)) ]
          < 4.127`.

The same bound holds after adding arbitrary affine terms in `(X,Y,Z)`. Therefore, after conditioning on all other coordinates, it also holds for an ambient quadratic form whenever the chosen physical principal triple has this zero-diagonal block `B`, regardless of couplings to the conditioned coordinates.

### Proof

Condition on `X=x`. Complete the cross product:

`Q
 =2c (Y+(b/c)x)(Z+(a/c)x) - kappa x^2`,

where `kappa=2ab/c`. For every fixed `x`, the translated `Y` and `Z` remain independent with density caps one. By (4.2), with `A=sqrt(|c|/2)`,

`p_Q(t)
 <= (2/|c|) integral f_X(x)
      log(1+A/sqrt(|t+kappa x^2|)) dx`.   (5.2)

We now integrate the logarithm by layer cake. For `s>0`,

`log(1+A/sqrt(|t+kappa x^2|))>s`

is equivalent to

`|t+kappa x^2| < delta_s`,

where

`delta_s=A^2/(e^s-1)^2`.

The elementary quadratic-sublevel estimate

`|{x: |t+kappa x^2|<delta}| <= 2 sqrt(2delta/|kappa|)`   (5.3)

holds uniformly in `t`: after scaling it is the length estimate for `|x^2-u|<epsilon`, whose largest interval length occurs at the tangency scale and is at most `2sqrt(2epsilon)`.

Since `f_X<=1` and has mass one, (5.3) yields

`integral f_X(x) log(1+A/sqrt(|t+kappa x^2|))dx
 <= integral_0^infinity min(1, R/(e^s-1)) ds`,

where

`R=2 sqrt(|c|/|kappa|)=sqrt(2)|c|/sqrt(|ab|)`.

The last integral is explicit. With

`J(R)=log(1+R)+R log(1+1/R)`,   (5.4)

one obtains

`||p_Q||_infinity <= (2/|c|) J(sqrt(2)|c|/sqrt(|ab|))`.   (5.5)

Permute the three input coordinates so that `|c|=L=max(|a|,|b|,|c|)`, and put `P=|abc|`. Then

`L=P^(1/3) u`, with `u>=1`,

and the argument of `J` in (5.5) is exactly

`sqrt(2) u^(3/2)`.

The function

`u -> J(sqrt(2)u^(3/2))/u`

is decreasing for `u>=1`. Indeed `J'(r)=log(1+1/r)`, so its derivative has the sign of

`(1/2) r log(1+1/r) - log(1+r)`,

which is negative for `r>=sqrt(2)` because `r log(1+1/r)<=1` while `log(1+r)>1/2`. Thus (5.5) is maximized at `u=1` and

`||p_Q||_infinity
 <= 2 P^(-1/3) J(sqrt(2))
 = 2^(4/3) J(sqrt(2)) |det B|^(-1/3)`,

which is (5.1).

Finally, if affine terms `ell^T x+d` are present, `B` is invertible and the translation `h=(1/2)B^{-1}ell` gives

`x^T Bx+ell^T x+d=(x+h)^T B(x+h)+constant`.

Coordinatewise translations preserve independence and all density caps. When the three variables are part of a larger ambient quadratic form, conditioning outside the triple produces only such affine and constant terms, so the same conditional bound survives averaging.

QED.

## 6. Explicit target instance and relation to the B11 exception

For `a=b=c=1`,

`Q=2(XY+XZ+YZ)`

has matrix eigenvalues `2,-1,-1`, hence satisfies the exact three-large-eigenvalue target. Formula (5.5) gives the sharper instance bound

`||p_Q||_infinity
 <=2[log(1+sqrt(2))+sqrt(2)log(1+1/sqrt(2))]
 <3.276`.

More generally, whenever an ambient physical principal `3x3` block is invertible and all three of its diagonal entries vanish, Theorem 5.1 supplies exactly the local branch that the account01/B11 scalar-pivot argument cannot enter. In particular, if `|det B|>=1`, the conditional ambient density is bounded by `C_cross<4.127`.

This is complementary to, not a replacement for, account01/B11: its nonzero-pivot Schur mechanism and the present pure-cross mechanism together cover the local invertible physical-triple dichotomy once a determinant-scale triple has been supplied.

## 7. Full-target status and next attack

The full conjecture is **not proved**. The remaining obstruction is to extract or aggregate these local controls from only the global spectral assumption. For rank exactly three, writing `A=U Lambda U^T`, Cauchy-Binet gives

`sum_{|I|=3} det(U_I)^2=1`,

and `det(A_I)=det(Lambda) det(U_I)^2`, but selecting one `I` loses dimension and naively averaging `|det(A_I)|^(-1/3)` is also dimension-sensitive. The live diffuse result covers maximum row leverage `<=1/12`; the hard mixed-leverage regime must exploit the distribution of the wedge weights rather than a single smallest/biggest minor.

A useful exact identity for the next run is the fixed-row wedge budget. If `u_i` is a row of a rank-three orthonormal frame `U`, then

`sum_{j<k, j,k!=i} det[u_i,u_j,u_k]^2 = ||u_i||_2^2`.

Thus a large-leverage row carries a dimension-free total determinant budget across all partner pairs. The unpaid step is to convert this **aggregate** budget into an averaged conditional density estimate without choosing one pair and without replacing the original product law by independent rotated coordinates.

No full-solution, novelty, or continuity claim is made beyond the branches proved above.

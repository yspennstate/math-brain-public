SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T14:24:57Z.
attacking: literature-to-proof transfer for the doubly aligned rank-two collar; exact Schur determinant identity plus the source-valid rank-two half-Riesz endpoint, then an fleet04/B18 dependence-safe outer square.

# fleet03/B18 r30 — doubly aligned rank-two collar away from the Schur collision

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING STRUCTURAL IMPLICATION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** essential boundedness and absolute continuity are proved on the new branch; continuity is not claimed.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and live correction boundary

The full owner target is unchanged: for arbitrary dimension, arbitrary independent real inputs with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `X^T A X`, or give a valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, smoothness, iid, or diagonal-basis assumption is added below.

This run starts exactly at the local debt left by fleet03/B18 r30's transverse augmentation theorem. There the rank-two physical cross block `B` between two disjoint original-coordinate product banks `X,Y` is coupled to an original scalar `Z` by slopes `c,d`. If either `c` has a component transverse to `ran B` or `d` has a component transverse to `ran B^T`, augmenting the cross block gives rank three and pays the branch. The unpaid collar is therefore

`c in ran B`, `d in ran B^T`.

The present argument pays this **exact doubly aligned collar away from one explicit scalar Schur collision**. It uses no post-rotation independence, no conditional-cap-as-independence step, no arbitrary-joint coarea theorem, no fixed-good-minor extraction, and no pointwise law-uniform quadratic van-der-Corput estimate.

## 2. Primary theorem matched exactly

The primary external theorem used is:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949.

If `f(x)=prod_i f_i(x_i)` and each one-dimensional `f_i` is a probability density with `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. In the present argument it is used only at `k=2`, separately inside the two disjoint original-coordinate product banks. Thus the two projected bank variables may have dependent coordinates internally, but the two banks remain genuinely independent because their source-coordinate sets are disjoint.

The immutable internal endpoint derived from exactly this source and two-dimensional Plancherel is fleet03/B18 r26, `QFORM-CROSSBLOCK-RANK2-HALFRIESZ-v1`, canonical report

`yspennstate/math-open-problems@d01d9d8a4d7664bfb2ae9c6da3f4d41867ddac16`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T102742Z-fleet03-B18-QFORM-r26/REPORT.md`.

It states: if `X,Y` are disjoint original product banks, `F(X),G(Y)` are arbitrary same-side measurable phases, and `C` is a rank-two physical cross block with nonzero singular-value product `Delta_C`, then

`sup_u E |F(X)+G(Y)+2 X^T C Y-u|^(-1/2) <= 8 Delta_C^(-1/4)`.

Consequently, one nonzero original-coordinate scalar Schur pivot `a` in front of such a residual gives

`||p_Q||_infinity <= 8 |a|^(-1/2) Delta_C^(-1/4)`.

For completeness, the Fourier input is `|phi(t)|<=min(1,2 pi Delta_C^(-1/2)/|t|)`. Multiplication by the half-Riesz Fourier weight `|t|^(-1/2)` is integrable and gives the displayed constant. This is a grouped two-dimensional Plancherel estimate, not the refuted one-dimensional stationary-phase claim.

## 3. New theorem — aligned-collar off-collision payment

### Theorem `QFORM-ALIGNED-RANK2-SCHUR-OFFCOLLISION-v1`

Let `Z`, `X=(X_i)_(i in I)` and `Y=(X_j)_(j in J)` be mutually independent original-coordinate blocks, with every one-dimensional density bounded by one. Let

`Q = a Z^2 + b Z + 2 Z c^T X + 2 Z d^T Y + F(X)+G(Y)+2 X^T B Y`,

where `F,G` are arbitrary real measurable functions, `B` is a real rank-two matrix, and the nonzero singular values of `B` have product

`Delta = sigma_1(B) sigma_2(B)>0`.

Assume the two scalar slopes are exactly aligned with the rank-two cross spaces:

`c in ran B`, `d in ran B^T`.

Let `B^+` denote the Moore--Penrose inverse and define the scalar collision parameter

`theta = d^T B^+ c`.

If

`a != 0` and `a != theta`,

then `Q` has an absolutely continuous law and

`boxed: ||p_Q||_infinity <= 8 Delta^(-1/4) [ |a| |a-theta| ]^(-1/4).`   (3.1)

No continuity conclusion is asserted.

### Proof

Take a thin singular-value decomposition

`B = U Sigma V^T`, `Sigma=diag(sigma_1,sigma_2)`,

with `U,V` having orthonormal columns. Exact alignment gives unique vectors `gamma,delta in R^2` such that

`c=U gamma`, `d=V delta`.

Because `B^+=V Sigma^(-1) U^T`,

`theta = delta^T Sigma^(-1) gamma`.   (3.2)

Complete the original scalar square. Writing

`s(X,Y)=c^T X+d^T Y+b/2`,

we have

`Q = a [ Z+s(X,Y)/a ]^2 + R(X,Y)`,

where, after expanding the square, all pure-X terms, pure-Y terms, affine terms and constants can be absorbed into new same-side functions `F_a(X),G_a(Y)`, while the X--Y cross block is exactly

`B_a = B - (1/a) c d^T
     = U [ Sigma-(1/a) gamma delta^T ] V^T`.   (3.3)

Since the middle matrix is 2 by 2, the matrix determinant lemma gives

`det[ Sigma-(1/a) gamma delta^T ]
 = det(Sigma) [1-(1/a) delta^T Sigma^(-1)gamma]
 = Delta (a-theta)/a`.   (3.4)

Under `a!=theta` this middle matrix is invertible, hence `B_a` has rank exactly two and its two nonzero singular values have product

`Delta_a = |det[ Sigma-(1/a)gamma delta^T ]|
         = Delta |a-theta|/|a|`.   (3.5)

The r26 rank-two cross half-Riesz theorem applies to

`R(X,Y)=F_a(X)+G_a(Y)+2 X^T B_a Y+constant`,

because `X,Y` are still the two disjoint original-coordinate product banks. Therefore

`sup_u E|R-u|^(-1/2) <= 8 Delta_a^(-1/4)`.   (3.6)

Conditioned on `(X,Y)`, the translated variable `Z+s(X,Y)/a` is a translate of the original cap-one scalar density. The elementary square-density formula therefore yields, for almost every output value `q`,

`p_Q(q) <= |a|^(-1/2) E|q-R|^(-1/2)`.   (3.7)

Combining (3.5)--(3.7),

`||p_Q||_infinity
 <= 8 |a|^(-1/2) [Delta |a-theta|/|a|]^(-1/4)
 = 8 Delta^(-1/4) [|a||a-theta|]^(-1/4)`,

which is (3.1). The same conditional formula constructs the density, so absolute continuity is proved. `QED`

### Quantitative interpretation

If `Delta>=delta0`, `|a|>=alpha` and `|a-theta|>=eta`, then

`||p_Q||_infinity <= 8 delta0^(-1/4)(alpha eta)^(-1/4)`.

Thus the exact doubly aligned collar is fully paid away from the two scalar degeneracies `a=0` and `a=theta`. The second value is not a heuristic: it is precisely where the post-pivot rank-two cross determinant vanishes.

## 4. Concrete target-valid application

Take five independent cap-one original variables `(Z,X1,Y1,X2,Y2)` and

`Q0 = 2 Z^2 +2 Z X1 +2 Z Y1 +2 X1 Y1 +2 X2 Y2`.   (4.1)

Here

`B=I_2`, `c=d=e_1`, `Delta=1`, `theta=1`, `a=2`.

Theorem 3 therefore gives

`boxed: ||p_(Q0)||_infinity <= 8*2^(-1/4)
 = 6.727171322029716... .`   (4.2)

The physical matrix is

`[[2,1,1,0,0],
  [1,0,1,0,0],
  [1,1,0,0,0],
  [0,0,0,0,1],
  [0,0,0,1,0]]`,

with characteristic polynomial

`lambda (lambda-3)(lambda-1)(lambda+1)^2`.

Hence its spectrum is `{3,1,-1,-1,0}` and it already lies inside the owner target with four eigenvalues of modulus at least one.

After the `Z` pivot the residual cross block is exactly `diag(1/2,1)`, so the determinant payment is literal rather than asymptotic.

## 5. Required designated-partner application

Use the completed fleet04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, immutable source

`yspennstate/math-open-problems@4ea84670b15b538f2163d53bf31f81cd1f1eabfa`,

with claim-card source at `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

It proves that if a base variable has density cap `M` and an outer original scalar square with coefficient `r!=0` is completed dependence-safely, then

`||p||_infinity <= 2 sqrt(M/|r|)`

without requiring independence after the translated square completion.

Apply it to any outer nonzero physical pivot whose Schur residual is in Theorem 3. If the outer coefficient is `r`, (3.1) supplies

`M <= 8 Delta^(-1/4)[|a||a-theta|]^(-1/4)`.

Therefore the actual partner splice is

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(2) |r|^(-1/2)
    Delta^(-1/8)[|a||a-theta|]^(-1/8).`   (5.1)

This proves absolute continuity and essential boundedness; continuity is not promoted through the partner wrapper.

A literal coupled target example is

`Q1=(W+Z)^2 + Q0`,   (5.2)

where `W` is one more independent cap-one original coordinate. Completing the outer `W` square leaves the residual `Q0`, so the partner theorem with `r=1` and (4.2) gives

`boxed: ||p_(Q1)||_infinity <= 2 sqrt(8*2^(-1/4))
 = 2^(19/8)
 = 5.187358218604039... .`   (5.3)

The physical characteristic polynomial of (5.2) is

`lambda (lambda-4)(lambda-1)^2(lambda+1)^2`,

so its spectrum is `{4,1,1,-1,-1,0}`. Thus five eigenvalues have modulus at least one. The outer square is genuinely translated by `Z`, so this is an actual use of the dependence-safe partner interface rather than an independent-convolution special case.

## 6. What remains unpaid

The new theorem does **not** prove the unrestricted conjecture. Within the local rank-two-cross/scalar-hub architecture, the remaining exact doubly aligned collision set is

`a=0` or `a=theta=d^T B^+ c`.

The transverse theorem from the immediately preceding B18 run pays `dist(c,ran B)>0` or `dist(d,ran B^T)>0`; the present theorem pays exact alignment away from the collision. A uniform near-collision theorem is still required because the bound in (3.1) diverges as `a->theta`. One may not replace a small nonzero collision gap by zero on arbitrary unbounded inputs.

Globally, the bare target hypothesis `s_3(A)>=1` still does not force this rank-two-cross/scalar-hub decomposition with uniform parameters. The full product-preserving ridge/grouped-coordinate compiler and arbitrary-extra-spectrum handling remain open. Full-target continuity is also open.

## 7. Checks and integrity

Exact algebra checked:

- `B_a=B-c d^T/a` after scalar square completion;
- in aligned SVD coordinates, `det(Sigma-gamma delta^T/a)=Delta(a-theta)/a`;
- example `Q0` characteristic polynomial is `lambda(lambda-3)(lambda-1)(lambda+1)^2`;
- coupled example `Q1` characteristic polynomial is `lambda(lambda-4)(lambda-1)^2(lambda+1)^2`;
- constants are `8*2^(-1/4)=6.727171322029716...` and `2^(19/8)=5.187358218604039...`.

Only the two files in this run's immutable B18 directory are written in `math-open-problems`; no peer artifact, control file, task state, notification setting, public release, permission, workflow or external account is changed. The changed-file text contains no credentials, tokens, account identifiers beyond the logical fleet label, or unrelated private material.

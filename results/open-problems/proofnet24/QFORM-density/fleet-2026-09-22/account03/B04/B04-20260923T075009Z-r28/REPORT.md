SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T07:50:09Z.
attacking: adaptive second-volume Fourier smoothing, with a sharp half-Riesz rearrangement replacing the nonsharp outer-square step and a new genuinely rotated indefinite test family.

# account03/B04 r28 — sharp half-Riesz rearrangement and adaptive pair-volume square lift

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Product Fourier rearrangement  
**Status:** `NEW SUPPORTING THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`  

The unrestricted conjecture is not proved here. The new result extends the previously paid rank-two volume branch from one fixed interpolation exponent to the whole marginal range below the true method endpoint `3/4`, and improves the dependence-safe outer-square constant by solving the underlying one-dimensional rearrangement problem sharply. No pointwise quadratic-phase decay, arbitrary-joint coarea estimate, post-rotation independence, moment assumption, support regularity, Gaussianity or log-concavity is used.

The historical owner-message URL supplied in the task points to commit `0dc369ddf8b860648dd780d8f92c62994dc53ecf`, whose README is an older FEI state. Fresh `main` has the later QFORM-only control; under the owner's precedence rule the later live control is the operative one.

## 1. Completed peer result actually applied

The designated partner `account04/B04` has no completed current-QFORM canonical report or shared handoff visible in the fresh repository search, so no designated-partner theorem is invented.

The completed peer theorem actually applied at equation level is account03/B01:

`yspennstate/math-open-problems@e83f41d90267abdb753682dbe60bceecd8e6558a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T223030Z-auto12/REPORT.md`.

Let `R` be an arbitrary quadratic-affine form in independent original coordinates. Suppose a physical cross block `M=A[I,J]` has

`E=e_2(M^T M)>0`,

and let `alpha_i`, `beta_j` be the row and column inclusion marginals of the natural squared-`2 x 2`-minor law

`w_ST=det(M[S,T])^2/E`.

For every `2/3<theta<1`, if `theta alpha_i<=1/2` for all rows, the source proves

`||p_R||_3 <= F(theta)^(2/3) E^(-1/6)`,                    (1.1)

where

`F(theta)= e * [3 theta/(3 theta-2)] * K_theta^(-1/(4 theta))`,

`K_theta=theta^(-theta)(1-theta)^(-(1-theta))`.              (1.2)

The theorem also applies after transposition, replacing row marginals by column marginals. It retains arbitrary same-bank quadratic curvature and outside couplings. This is an integrated product-space Fourier result, not a law-uniform pointwise Fresnel estimate.

## 2. New sharp rearrangement theorem for the half-Riesz kernel

### Theorem `QFORM-SHARP-L3-HALFRIESZ-v1`

Let `p` be any probability density on `R` with finite `L^3` norm `N=||p||_3`. Then

`sup_t int_R |x-t|^(-1/2) p(x) dx
 <= C_H N^(3/4)`,                                               (2.1)

with the sharp constant

`C_H = 2 sqrt(2 pi) / 3^(1/4)
     = 3.809251227455829...`.                                   (2.2)

The constant is attained by an explicit compactly supported decreasing rearrangement after translation and scaling.

### Proof

Translation reduces to `t=0`. Put `k(x)=|x|^(-1/2)`. For arbitrary `lambda,mu>0` and `u>=0`, maximize the cubic polynomial in `u` to obtain the pointwise Young-Fenchel inequality

`k u <= lambda u + mu u^3
       + [2/(3 sqrt(3 mu))] (k-lambda)_+^(3/2)`.                 (2.3)

Indeed the positive maximum of `(k-lambda)u-mu u^3` occurs at

`u=sqrt((k-lambda)/(3mu))`.

The remaining kernel integral is exact:

`int_R (|x|^(-1/2)-lambda)_+^(3/2) dx
 = (3 pi/2) lambda^(-1/2)`.                                    (2.4)

To see (2.4), on the positive half-line put `x=lambda^(-2)u` and then `u=y^2`; the beta integral is

`int_0^1 (u^(-1/2)-1)^(3/2)du
 =2 B(1/2,5/2)=3pi/4`,

and symmetry doubles it.

Integrating (2.3) therefore gives

`I:=int k p
 <= lambda + mu N^3 + [pi/sqrt(3)] mu^(-1/2)lambda^(-1/2).` (2.5)

The two-variable minimum occurs at

`lambda=sqrt(pi/(2sqrt(3))) N^(3/4)`,
`mu=lambda/N^3`,                                                (2.6)

and substitution into (2.5) yields exactly (2.1)-(2.2).

Sharpness is not only formal. At the minimizing parameters define

`p_*(x)=[(|x|^(-1/2)-lambda)_+/(3mu)]^(1/2)`.                   (2.7)

The first-order equations in (2.6), together with the same beta integrals, give exactly

`int p_*=1`, `int p_*^3=N^3`,

and equality holds in (2.3) pointwise on the support. Hence (2.2) is sharp. QED.

This improves the earlier dependence-safe square potential coefficient `4` to `C_H=3.809251...`.

## 3. New adaptive pair-volume theorem

Let a full quadratic form have a nonzero original-coordinate pivot. Complete only that physical coordinate:

`Q=a[X_0+m(Y)]^2+R(Y)`, `a!=0`,                                 (3.1)

where `X_0` is independent of the remaining original coordinates `Y`; the shift `m(Y)` may depend arbitrarily on the same variables that determine `R`.

Suppose the exact Schur residual `R` has a physical cross block `M` with second volume `E=e_2(M^TM)>0`. Let

`mu_r=max_i alpha_i`, `mu_c=max_j beta_j`,
`mu=min(mu_r,mu_c)`.                                             (3.2)

### Theorem `QFORM-ADAPTIVE-E2-SHARP-SQUARE-v1`

If

`mu<3/4`,                                                        (3.3)

then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= C_ad(mu) |a|^(-1/2) E^(-1/8)`,                              (3.4)

where

`theta_0=0.999666325350825...`                                  (3.5)

is the unique root in `(2/3,1)` of

`-log(1-theta)=8theta/(3theta-2)`,                               (3.6)

and

`theta_*(mu)=min{theta_0,1/(2mu)}`,                              (3.7)

with

`C_ad(mu)=C_H sqrt(F(theta_*(mu)))`.                             (3.8)

Here the convention in (3.7) is harmless when the selected marginal maximum is zero; in the present `E>0` setting some marginals are positive.

Numerically, if

`mu <= mu_0:=1/(2theta_0)=0.500166893012555...`,

then the optimized coefficient is already the universal plateau

`C_ad(mu)=10.87750568366085...`.                                (3.9)

For `mu_0<mu<3/4`, the optimizer is `theta_*=1/(2mu)` and one may write

`C_ad(mu)
 = C_H [ 3e/(3-4mu) ]^(1/2)
   K_{1/(2mu)}^(-mu/4).`                                        (3.10)

### Proof

Orient `M` so that the selected side has maximum natural pair-volume marginal `mu`. The source theorem (1.1) is admissible whenever

`2/3<theta<1`, `theta mu<=1/2`.                                  (3.11)

For fixed `Y=y`, the density cap `f_{X_0}<=1` implies the shifted-square conditional density envelope

`p_{Q|Y=y}(q)
 <= |a|^(-1/2)|q-R(y)|^(-1/2)`.                                 (3.12)

Averaging (3.12) and applying Theorem (2.1) to the `L^3` density of `R` gives

`||p_Q||_infinity
 <= C_H |a|^(-1/2)||p_R||_3^(3/4)
 <= C_H sqrt(F(theta)) |a|^(-1/2)E^(-1/8).`                     (3.13)

It remains only to optimize `theta` under (3.11). Differentiating `log F` gives

`d/dtheta log F(theta)
 =[-(3theta-2)log(1-theta)-8theta]
   /[4theta^2(3theta-2)].`                                      (3.14)

The numerator is strictly increasing through one zero because the equivalent function

`-log(1-theta)-8theta/(3theta-2)`

has derivative

`1/(1-theta)+16/(3theta-2)^2>0`,

with limits `-infinity` at `2/3+` and `+infinity` at `1-`. Thus `F` decreases to the unique `theta_0`, then increases. The constrained minimizer is exactly (3.7). Condition `mu<3/4` is exactly what guarantees the admissible interval in (3.11) is nonempty. QED.

The source's fixed choice `theta=3/4` only paid `mu<=2/3`; (3.4) pays **every fixed natural pair-volume marginal strictly below `3/4`**, with the exact optimized coefficient. The divergence as `mu upward 3/4` is a method endpoint, not evidence of a target counterexample.

This theorem proves absolute continuity and an essential `L^infinity` bound. It does **not** prove continuity in the general dependent-shift form (3.1).

## 4. Companion sharp square rearrangement

For completeness, another exact product-space rearrangement is useful. If `X` has density at most one and `b` is fixed, then

`||p_{(X-b)^2}||_(3/2) <=2`,                                    (4.1)

sharply. Indeed with

`g(r)=f_X(b+r)+f_X(b-r)`, `r>0`,

we have `0<=g<=2`, `int_0^infinity g=1`, and

`p_{(X-b)^2}(y)=g(sqrt(y))/(2sqrt(y))`.

Consequently

`int p^(3/2)
 =2^(-1/2) int_0^infinity g(r)^(3/2)r^(-1/2)dr
 <=int_0^infinity g(r)r^(-1/2)dr
 <=2sqrt(2)`,                                                   (4.2)

where the final step is the one-dimensional bathtub principle: put density `2` on `[0,1/2]`. Taking the `2/3` power gives (4.1), with equality for a unit interval centered at `b`.

Thus when the square in (3.1) is actually independent of `R` with a fixed shift, Young gives the alternate bound

`||p_Q||_infinity
 <=2 F(theta_*)^(2/3)|a|^(-1/3)E^(-1/6)`.                      (4.3)

The dependence-safe theorem (3.4) is the more useful statement for Schur completion and is the main result of the run.

## 5. Genuinely rotated indefinite target outside the old fixed gate

Let

`c=cos(pi/8)`, `s=sin(pi/8)`,

and define the `4 x 2` matrix `U` by rows

`sqrt(7/10)(c,-s)`,
`sqrt(3/10)(c,-s)`,
`sqrt(7/10)(s,c)`,
`sqrt(3/10)(s,c)`.

The two displayed directions are orthonormal and the weights in each repeated direction sum to one, hence

`U^T U=I_2`.

Set

`M=2U`, `d=(1/8,1/8,1/8,1/8)^T`,                                (5.1)

and for independent original coordinates `Z`, `X in R^4`, `Y in R^2` put

`Q_*=(Z+d^T X)^2+2X^T M Y`.                                    (5.2)

The physical coefficient matrix is

`A_*=[[1,d^T,0],[d,dd^T,M],[0,M^T,0]]`.                         (5.3)

Every entry of the `X-Y` cross block is nonzero; the `pi/8` mixing makes it genuinely rotated in the original product coordinates. Also all four `Z-X` couplings and all entries of the rank-one `X-X` curvature `dd^T` are nonzero.

### Spectral target certificate

Let

`B=diag(1, [[0,M],[M^T,0]])`.

Because `M^TM=4I_2`, the spectrum of `B` contains `+2,+2,-2,-2` (plus `1,0,0`). The perturbation `A_*-B` is the sum of the off-diagonal star `[0,d^T;d,0]`, whose operator norm is `||d||=1/4`, and `dd^T`, whose norm is `||d||^2=1/16`. Hence

`||A_*-B||op <=5/16`.                                           (5.4)

Weyl therefore gives two eigenvalues at least `2-5/16=27/16` and two at most `-27/16`. Thus `A_*` is indefinite and has at least four eigenvalues of modulus greater than one; it is a valid exact-target matrix.

### Pair-volume currency and the new estimate

The only nonzero `2 x 2` row minors of `M` choose one row from the first repeated direction and one from the second. Their squared-volume law has row marginals exactly

`(7/10,3/10,7/10,3/10)`.                                      (5.5)

Thus

`mu=7/10`.

The old fixed `theta=3/4` gate fails because `(3/4)(7/10)=21/40>1/2`. The adaptive theorem instead takes

`theta_*=1/(2mu)=5/7`.                                          (5.6)

Also

`E=e_2(M^TM)=e_2(4,4)=16`.                                     (5.7)

At `theta=5/7`,

`K_theta=1.818968511653173...`,
`F(theta)=33.07096956390116...`,
`C_ad(7/10)=21.90599983011287...`.                              (5.8)

Therefore for **every** admissible cap-one product input law,

`boxed:
 ||p_(Q_*)||_infinity
 <= C_ad(7/10) * 16^(-1/8)
 =15.48988102854417... .`                                      (5.9)

This is a genuinely rotated indefinite example covered by the new theorem but not by the source's concrete `theta=3/4` pair-volume gate.

A direct numerical eigenvalue check, used only as an audit rather than the proof certificate, gives approximately

`(-2.000000,-1.980219,0,0,0.983507,2.000000,2.059212)`.

The exact Weyl estimate (5.4), not this floating-point spectrum, proves target membership.

## 6. What this does and does not close

The run closes an analytic gap inside the existing pair-volume branch:

1. the half-Riesz `L^3 -> L^infinity` outer-square receiver is now sharp;
2. the fractional pair-volume Fourier exponent is optimized rather than frozen at `3/4`;
3. every fixed natural pair-volume marginal `<3/4` is paid;
4. the proof tolerates the full Schur-dependent square shift `m(Y)` and arbitrary same-bank curvature in the residual.

It does **not** prove that the bare three-large-eigenvalue hypothesis always produces a pivot whose exact Schur residual has `mu<3/4` and dimension-free `|a|^4E` currency. The remaining structural debt for B04 is therefore

`QFORM-E2-MARGINAL-3/4-OR-HUB-ROUTING-v1`:

> from a surviving full-target state, either obtain a physical pivot with `|a|^4 E_2` bounded below and selected natural pair-volume marginal `<3/4`, so (3.4) fires, or show that marginal concentration `>=3/4` quantitatively forces one of the already-paid exact-star, mixed-hub, grouped-pair, ridge, true-pair-Schur, or higher-volume branches before any vanishing local coefficient is inverted.

The strict `3/4` threshold is now the actual analytic frontier for this fractional-`E_2` mechanism.

## 7. Correction and regularity ledger

Consumed and respected: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive conditional projection-height moments can diverge; rotations do not preserve independence; a bounded projection density alone does not control an indefinite quadratic pushforward; naive fiber-sup integration can lose dimension; a single well-conditioned physical minor is not automatic.

No Monte Carlo or histogram is used. Numerical computations only audit closed-form constants and the example; all target membership and inequalities have analytic certificates.

**General theorem regularity:** absolute continuity + essential boundedness. Continuity not proved in the dependent-square scope.  
**Full QFORM:** OPEN.  
**Native brain ingestion:** not verified; repository retrieval/use is not native learned-memory ingestion, so status remains `WITHOUT_VERIFIED_BRAIN`.  
**Model self-report:** `GPT-5.6 Sol`.  
**Configured reasoning level:** `UNKNOWN_NOT_EXPOSED`.  
**Reasoning-token/provider-thinking counters:** `NOT_EXPOSED`.

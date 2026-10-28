# account01/B17 — global lightlike one-heavy stress theorem

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** QFORM-B17-20260923T023752Z-r11  
**Assignment:** Sharp constant and witnesses  
**Status:** SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Target and source state

The full target remains open: for every dimension, every product law of independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal finite essential-density bound for `Q=X^TAX`, or give a valid counterexample. Continuity is tracked separately.


The known source-valid diffuse construction gives the target-level lower obstruction `C_* >= 3 sqrt(2)`. The purpose here is to test a genuinely rotated mixed-leverage mechanism that is not diagonal and in which one physical coordinate is shared exactly between a positive and the negative spectral directions.

## 2. Partner theorem used at an actual inequality

The designated partner `account02/B17` proved `QFORM-ONE-HEAVY-DIFFUSE-NOESCAPE-v1` at

- `yspennstate/math-open-problems@fbf14cd80c31d2100cf849494016bb4703aefdd7`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T181037Z-r11/REPORT.md`.

Its Corollary 3.2 states: if `X` has arbitrary density at most one, `G~N(0,1)` is independent, `ell in [0,1]`, and

`H = sqrt(12 ell) X + sqrt(1-ell) G`,

then for every `a>=0`,

`E exp(-a H^2) <= (1+2a)^(-1/2)`.

This result is applied below with `a=t^2/72`; it is the key inequality in the global Fourier estimate, not merely a comparison citation.

## 3. The lightlike one-heavy Gaussian-completion model

Let

`J=diag(1,1,-1)`,

`w_+=(e_1+e_3)/sqrt(2)`, `w_-=(e_1-e_3)/sqrt(2)`.

Then in coordinates `(u,z,v)` along `(w_+,e_2,w_-)`,

`y^T J y = 2uv+z^2`.

Fix `theta in [0,1]`. Let `X` have an arbitrary probability density `f_X<=1`, and let `G_0,G_1,G_2` be independent `N(0,1/12)`, independent of `X`. Define

`U_theta = sqrt(theta) X + sqrt(1-theta) G_0`,

`V=G_1`, `W=G_2`, and

`T_theta = 2 U_theta V + W^2`.

The heavy row is Euclidean-nonzero but `J`-lightlike: `w_+^T J w_+=0`. Hence this is neither an aligned positive heavy row nor an aligned negative heavy row.

### Theorem 3.1 — QFORM-LIGHTLIKE-ONE-HEAVY-GLOBAL-v1

For every `theta in [0,1]` and every cap-one law of `X`, `T_theta` has a bounded continuous density satisfying

`||p_{T_theta}||_infinity <= C_light`,

where

`C_light = 3 Gamma(1/4)/(sqrt(pi) Gamma(3/4))`

`= 5.007761050044439...`.

The constant is dimension-free and law-uniform inside this Gaussian-completion architecture. It is larger than the known lower obstruction `3sqrt(2)=4.242640687119285...`; the excess is Fourier absolute-value slack and is not a new lower bound.

### Proof

Conditioning on `U_theta=u`, Gaussianity of `V` gives

`E[exp(i t 2uV)|U_theta=u] = exp(-t^2 u^2/6)`.

Independently,

`E exp(i t W^2) = (1-it/6)^(-1/2)`.

Therefore

`phi_theta(t) = (1-it/6)^(-1/2) E exp(-t^2 U_theta^2/6)`.

Put `H=sqrt(12) U_theta`. The partner theorem with `a=t^2/72` gives the actual estimate

`E exp(-t^2 U_theta^2/6) = E exp(-(t^2/72)H^2)`

`<= (1+t^2/36)^(-1/2)`.

Also

`|(1-it/6)^(-1/2)|=(1+t^2/36)^(-1/4)`.

Hence

`|phi_theta(t)| <= (1+t^2/36)^(-3/4)`.

The right side lies in `L^1(R)`. Fourier inversion therefore gives a bounded continuous density, and

`||p_{T_theta}||_infinity`

`<= (1/(2pi)) int_R (1+t^2/36)^(-3/4) dt`

`= (3/sqrt(pi)) Gamma(1/4)/Gamma(3/4)`.

This proves the theorem. Notice that no law-uniform pointwise quadratic-phase decay is asserted: the decay comes from an exact Gaussian linear factor plus the partner's square-Laplace domination after the diffuse completion.

## 4. Exact finite target matrices realizing the stress family

The limiting model above has an exact original-coordinate product realization before taking the diffuse limit.

For each `m>=1`, form an `(1+3m) x 3` row matrix `R_m` with rows

- one heavy row `sqrt(theta) w_+`;
- `m` rows `sqrt((1-theta)/m) w_+`;
- `m` rows `m^(-1/2) e_2`;
- `m` rows `m^(-1/2) w_-`.

Exactly,

`R_m^T R_m`

`= theta w_+w_+^T + (1-theta)w_+w_+^T + e_2e_2^T + w_-w_-^T`

`=I_3`.

Set

`A_m=R_m J R_m^T`.

Because `R_m` is an isometry from `R^3` into the physical space,

`A_m R_m=R_m J`,

and every finite `A_m` has exact nonzero spectrum

`{1,1,-1}`.

Put the arbitrary cap-one law `X` on the heavy physical coordinate and put independent `Unif[-1/2,1/2]` laws on all `3m` diffuse coordinates. If

`S_m=m^(-1/2) sum_{j=1}^m U_j`, `U_j iid Unif[-1/2,1/2]`,

and `S_m^(+),S_m^(2),S_m^(-)` are independent copies, then the physical quadratic form is exactly

`Q_m=2 U_m V_m + W_m^2`,

where

`U_m=sqrt(theta)X+sqrt(1-theta)S_m^(+)`,

`V_m=S_m^(-)`, `W_m=S_m^(2)`.

Thus the finite family is genuinely rotated, source-valid, and product-preserving in the original coordinates. The CLT gives `Q_m => T_theta`.

## 5. Uniform local-limit transfer for the exact finite family

Weak convergence alone does not control density peaks, so we also prove uniform density convergence for each fixed `theta` and fixed heavy law `X`.

Let `h_m` be the density of `S_m`. It is symmetric unimodal. Ball's cube-slicing theorem gives

`||h_m||_infinity <= sqrt(2)`

for the normalized equal-weight cube projection. Consequently the density of `U_m` is bounded by `2`, uniformly in `m>=2` and `theta`: if `theta>=1/2`, use the scaled heavy law cap `theta^(-1/2)<=sqrt(2)`; if `theta<1/2`, use the scaled diffuse cap `sqrt(2)/(sqrt(1-theta))<=2`. Convolution cannot increase the chosen cap.

Let

`chi_m(s)=E exp(i s S_m)=[sinc(s/(2sqrt(m)))]^m`.

For every `m>=2`,

`|chi_m(s)| <= min(1,3/|s|)`.

Indeed, with `x=|s|/(2sqrt(m))`, if `x<=1`, `sinc x<=exp(-x^2/6)`, so

`|s| |chi_m(s)| <= 2sqrt(m) x exp(-m x^2/6)<3`.

If `x>=1`, write `q=sin(1)`. On `[1,infinity)`, `|sinc x|<=min(q,1/x)`. Hence

`|s| |chi_m(s)| <= 2sqrt(m) q^(m/2) x^(1-m/2) <=3`;

the final one-variable maximum over integers `m>=2` is below `2.92`.

Next let

`psi_m(t)=E exp(i t S_m^2)`.

Since `h_m` is symmetric decreasing on each half-line and has cap `M<=sqrt(2)`, split at `r=|t|^(-1/2)`. The central interval contributes at most `2Mr`. On each tail the first-derivative van der Corput bound for phase `t x^2`, followed by Abel summation against the monotone amplitude, contributes at most `M/(|t|r)`. Therefore

`|psi_m(t)| <= min(1,4sqrt(2)|t|^(-1/2))`.

For the bilinear factor, put `delta=3/(2|t|)`. When `|t|>=3/2`, the density cap `2` of `U_m` and the preceding `chi_m` estimate imply

`|E chi_m(2tU_m)|`

`<= E min(1,delta/|U_m|)`

`<= 4delta + 4delta log(1/delta)+delta`

`=delta[5+4log(1/delta)]`.

Thus, for `|t|>=3/2`,

`|phi_{Q_m}(t)|`

`<= 4sqrt(2)|t|^(-1/2) * (3/(2|t|))[5+4log(2|t|/3)]`.

This is an integrable envelope independent of `m`, `theta`, and the cap-one heavy law. For bounded `t`, use `|phi|<=1`.

For fixed `theta` and fixed `X`, the three diffuse banks converge jointly to independent `N(0,1/12)` variables, so `phi_{Q_m}(t)->phi_theta(t)` pointwise. Dominated convergence therefore gives

`||phi_{Q_m}-phi_theta||_1 ->0`.

Fourier inversion yields the strong local limit

`||p_{Q_m}-p_{T_theta}||_infinity ->0`.

In particular,

`limsup_{m->infinity} ||p_{Q_m}||_infinity <= C_light=5.007761050044439...`.

For every `m>=2`, the same integrable characteristic-function estimate also supplies a bounded continuous density for this exact finite family.

## 6. Sharpness information and what this excludes

At `theta=0` the limit is the fully Gaussian signature `(+,+,-)` model. Its density at zero equals exactly

`3sqrt(2)`.

Thus this family contains the known sharp lower-obstruction endpoint. The designated partner's orientation-uniform central theorem additionally gives

`p_{T_theta}(0)<=3sqrt(2)`

for every `theta`, while Theorem 3.1 controls all output levels by `C_light` for the null-orientation branch.

The latest `account02/B17` majority-sign aligned theorem (`B17-20260923T014533Z-r14-multiscale`) gives the complementary global Gaussian-completion bound

`||p_{X^2+G_+^2-G_-^2}||_infinity <=4.2216798636024726...<3sqrt(2)`.

Hence a single macroscopic physical row is now globally controlled in two canonical stress geometries: aligned-majority and exactly lightlike shared-sign orientation. This does not cover every orientation globally, several interacting heavy rows, coupled non-Gaussian residuals, finite/mesoscopic overshoot outside the present bank architecture, higher spectral rank, or the full arbitrary matrix theorem.

## 7. Quantitative proof constraint

The theorem exposes a concrete limitation of an absolute-Fourier proof near the apparent sharp constant. Even when the partner square-Laplace comparison exactly dominates the bilinear factor by its Gaussian calibration, taking absolute values in Fourier inversion pays

`C_light/(3sqrt(2)) = 1.180340599016096...`.

So an argument seeking the sharp constant `3sqrt(2)` cannot simply combine that pointwise characteristic-function magnitude comparison with absolute Fourier inversion; it must retain phase/cancellation or use a positive geometric kernel. For existence of some universal constant, however, the same mechanism succeeds cleanly on this genuinely rotated shared-coordinate family.

## 8. Unpaid implication

Full QFORM remains open. A witness above `3sqrt(2)`, if one exists, must still be sought among mechanisms not excluded here: multiple non-collinear macroscopic rows, coupled spectral tails sharing physical coordinates, genuinely finite or mesoscopic non-Gaussian effects, or higher-rank interactions. Conversely, a full proof still needs a product-preserving reduction that places arbitrary matrices into controlled branches without using any refuted fiber/coarea interface.

## Sources

- `account02/B17`, one-heavy square-Laplace theorem: `yspennstate/math-open-problems@fbf14cd80c31d2100cf849494016bb4703aefdd7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T181037Z-r11/REPORT.md`.
- K. Ball, *Cube slicing in R^n*, Proc. Amer. Math. Soc. 97 (1986), 465–473, for the normalized cube-projection density cap used only in the finite local-limit transfer.

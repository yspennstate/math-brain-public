# account02/B13 — support-free near-null product interpolation and pivot-free local triple payment

**Run:** `20260922T172625Z-account02-B13-productset-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `PARTNER-GAP-CLOSED / SUPPORTING-LOCAL-THEOREM / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form density conjecture remains **OPEN / NOT PROVED**. This run starts from the exact product bang-bang reduction already proved by this slot and attacks the newest designated-partner gap: account03/B13 asked for a support-free interpolation from its exact null-pair product envelope to pairs having small nonzero diagonal squares. That interpolation is proved below with explicit constants and then combined with the completed weak-`L^2` ridge theorem to obtain a robust ambient three-coordinate density bound.

The first unpaid implication **after** this run is not local continuity of the null pair. It is now an aggregate selection/payment theorem: convert the existing finite-heavy-core / grouped-coordinate determinant packets into one of the robust local pair payments below, or aggregate the diffuse bordered-minor bank before reciprocal payment, while preserving original-coordinate product provenance and arbitrary extra spectrum.

## 1. Sources and correction status

Fresh protected controls were reread before this write at

`yspennstate/math-research-brain@757247132f122cc18bfb84412588f66cd8676212`,


Mathematical sources actually used:

1. **Exact product bang-bang reduction**, account02/B13:
   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.
   For every fixed slab kernel, the worst cap-one product law is reduced exactly, in supremum, to unit-measure product indicators. No interval or bounded-fragment hypothesis is introduced.

2. **Designated partner result: null-pair product smoothing**, account03/B13:
   `yspennstate/math-open-problems@a7594ff13b36fbc1819f60ec287e8232bd39974d`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T165804Z-account03-B13-qform-r12/REPORT.md`.
   Its exact endpoint theorem is
   `p_{UV}(z) <= 4 asinh(1/(2 sqrt(|z|))) <= 2 Psi(z)`
   for independent cap-one `U,V`, uniformly after deterministic translations. Its stated next implication is a support-free near-null interpolation allowing small nonzero squares in both hyperbolic variables.

3. **Weak-`L^2` logarithmic ridge**, account03/B16:
   `yspennstate/math-open-problems@c301be6b21f382934962aeb4c019b713377eac2f`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/B16-20260922T135620Z-r11/REPORT.md`.
   With
   `Psi(u)=1+log(1/|u|)` for `0<|u|<=1` and `Psi(u)=|u|^(-1/4)` for `|u|>=1`, it proves uniformly in `a`
   `||Psi(a+z^2)||_{L^{2,infinity}(dz)} <= sqrt(15)`,
   with the exact scaling cost `delta^(-1/4)`, and `int g h <=2||h||_{2,infinity}` for every probability density `0<=g<=1`.

Live corrections were refreshed before publication. In particular this report does not use law-uniform pointwise Fresnel decay, post-rotation independence, unrestricted fiber suprema, conditional-cap-as-independence, a universal good fixed minor/cross-rank dichotomy, bounded-diameter localization, fixed fragment count, or operator-norm continuity of slab volume on remote supports.

## 2. Starting unpaid implication

The partner endpoint corresponds to the binary form `2bUV`. A perturbative coefficient argument is unavailable: this slot's preceding run proved that arbitrarily small operator-norm matrix perturbations can have order-one effects on fixed product-set slab volumes after supports are translated far away. The correct question is therefore intrinsic to the actual level hyperbola:

> If
> `q(u,v)=a u^2+2buv+c v^2`
> is still strongly hyperbolic, can one retain the partner's logarithmic product envelope with a universal multiplicative loss, uniformly over all fragmented cap-one product laws and all translations?

The next theorem answers this affirmatively on a quantitative near-null collar.

## 3. Support-free near-null asinh envelope

Let `U,V` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1` and total mass one. Consider

`q(u,v)=a u^2+2buv+c v^2`,

where `b!=0` and

`|a| <= |b|/2`,  `|c| <= |b|/2`.                                    (3.1)

The hypotheses imply `D:=b^2-ac >=3b^2/4>0`, so the form is indefinite and nonsingular.

### Theorem 3.1 — `QFORM-NEAR-NULL-ASINH-v1`

Put `delta=sqrt(D)`. After adding an arbitrary affine function of `(u,v)`, let `t_*` denote the resulting critical value. Then for almost every `t!=t_*`,

`p_q(t) <= (2/delta) asinh( theta sqrt(2kappa/|t-t_*|) ),`             (3.2)

where, after reflecting one variable if necessary so `b>0`,

`kappa=(b+delta)/2`,
`r=c/(2kappa)`, `s=a/(2kappa)`,
`theta=1+(|r|+|s|)/2`.

In particular, under (3.1),

`boxed( p_q(t) <= (2 sqrt(3)/|b|) Psi((t-t_*)/(2|b|)) ).`             (3.3)

No support, moment, continuity, centering, connectedness, or fragment-count assumption is imposed on `f,g`.

### Proof

Affine terms can be removed by a deterministic translation because the binary quadratic matrix is invertible. The two one-dimensional input laws are translated separately, so independence and the density caps are preserved. It therefore suffices to prove the homogeneous statement with `t_*=0`. Reflect `V` if needed and assume `b>0`.

The algebraic factorization

`q(u,v)=2kappa (u+r v)(v+s u)`                                      (3.4)

is exact. Indeed `2kappa s=a`, `2kappa r=c`, and

`kappa + ac/(4kappa)=b`

because `kappa` is the positive root of `kappa^2-bkappa+ac/4=0`.

Set

`x=u+r v`, `y=v+s u`, `d=1-rs`.

Using the same quadratic identity,

`d = delta/kappa >0`.                                                 (3.5)

Hence the linear map `(u,v)->(x,y)` has Jacobian determinant `d`, while `q=2kappa xy`. For `z!=0`, write

`w=z/(2kappa)`.

The product-density formula gives

`p_q(z)= (1/(2delta)) int_R f(U(x))g(V(x)) dx/|x|`,                   (3.6)

where on the hyperbola `y=w/x`,

`U(x)=(x-rw/x)/d`,
`V(x)=(w/x-sx)/d`.                                                    (3.7)

Consider one sign branch `x=epsilon e^t`, `epsilon in {+1,-1}`, and put

`H(t)=f(U(t))g(V(t))`, `0<=H<=1`, `L=int_R H(t)dt`,
`A=int e^tH(t)dt`, `B=int e^(-t)H(t)dt`.                              (3.8)

Since `|x|=e^t` and `|y|=|w|e^(-t)`,

`A+|w|B = int (|x|+|y|)H dt`.                                        (3.9)

Differentiate (3.7). With prime denoting `d/dt`,

`U'=(x+r y)/d`, `V'=-(s x+y)/d`.

Solving these two equations back for `x,y` gives the exact identities

`x=U'+rV'`, `y=-(sU'+V')`.                                           (3.10)

Therefore

`|x|+|y| <= (1+|s|)|U'|+(1+|r|)|V'|`.                               (3.11)

Now `U(t)` and `V(t)` are each of the form `alpha e^t+beta e^(-t)`. Each has at most one critical point, hence every real value has multiplicity at most two on a sign branch. Since `g<=1`,

`int |U'|H dt <= int |U'| f(U(t))dt <=2 int f =2`,                    (3.12)

and similarly `int |V'|H<=2`. Combining (3.9)--(3.12),

`A+|w|B <= 2(2+|r|+|s|)=4theta`.                                    (3.13)

By AM-GM,

`sqrt(AB) <=2theta/sqrt(|w|)`.                                       (3.14)

The partner's centered-cosh rearrangement now applies verbatim, but we include the two-line argument for completeness. Translate `H` in `t` so its two exponential moments become equal. Their common value is `sqrt(AB)`, hence

`sqrt(AB)=int cosh(t) H_shift(t)dt`.

Among all functions `0<=H<=1` of mass `L`, the integral against the even increasing function `cosh` is minimized by `1_{[-L/2,L/2]}`. Thus

`sqrt(AB)>=2sinh(L/2)`.                                               (3.15)

Equations (3.14)--(3.15) yield, for each sign branch,

`L<=2 asinh(theta/sqrt(|w|))`.

There are two sign branches. Substituting into (3.6) proves (3.2).

It remains to extract a simple scaled envelope. Under (3.1),

`sqrt(3)/2 <= delta/b <= sqrt(5)/2`,
`theta <=3-sqrt(3)`,
`kappa/b <=(1+sqrt(5)/2)/2`.                                         (3.16)

Put `u=|z|/(2b)`. Then

`theta sqrt(2kappa/|z|) <= A0/sqrt(u)`,
`A0=(3-sqrt(3))*sqrt((1+sqrt(5)/2)/2) < sqrt(2)`.                     (3.17)

For `u>=1`, `asinh(A0/sqrt(u)) <=sqrt(2)u^(-1/2)<=(3/2)u^(-1/4)`. For `0<u<=1`, let `L0=log(1/u)`. The derivative of `asinh(A0 exp(L0/2))` with respect to `L0` is at most `1/2`, while `asinh(A0)<asinh(sqrt(2))<3/2`; hence

`asinh(A0/sqrt(u)) <=(3/2)(1+log(1/u))`.                              (3.18)

Finally `2/delta<=4/(sqrt(3)b)`. Combining (3.2), (3.17), and (3.18) gives (3.3). QED.

### Why this is not the failed perturbative mechanism

No comparison between two matrices or two slab kernels appears. The proof parameterizes the **actual** perturbed hyperbola, retains both original independent densities inside the same incidence integral, and pays the perturbation through the exact derivatives of the inverse hyperbolic coordinates. Remote translations are already absorbed exactly before the estimate, so they cannot amplify a small coefficient into an uncontrolled error term.

## 4. Ambient three-coordinate near-null theorem

Consider any real symmetric ambient matrix. Select three original independent coordinates whose physical principal block is

`B=[[a,b,p],[b,c,q],[p,q,gamma]]`,                                   (4.1)

with `b!=0`, `det B!=0`, and

`|a|,|c| <= |b|/2`.                                                   (4.2)

All coefficients outside this triple and all cross couplings are arbitrary.

### Theorem 4.1 — `QFORM-NEAR-NULL-PAIR-PLUS-SQUARE-v1`

For independent cap-one input laws,

`boxed( ||p_{X^TAX}||_infinity
       <= C_near (|b| |det B|)^(-1/4) ),`                             (4.3)

where

`C_near = 12 sqrt(5) (5/2)^(1/4)
        = 33.7404795114209...`.                                       (4.4)

The theorem is support-free and survives arbitrary outside quadratic terms and cross couplings.

### Proof

Condition on every original coordinate outside the selected triple. Their effect is an arbitrary affine term in the three remaining independent cap-one variables. Let

`C=[[a,b],[b,c]]`, `D=b^2-ac=|det C|`.

For fixed third coordinate and fixed outside variables, complete the square in the first two coordinates. This merely translates the first two original one-dimensional laws separately. The remaining first-two quadratic part is exactly the binary form of Theorem 3.1. The residual quadratic coefficient in the third coordinate is the scalar Schur complement

`s_3=gamma-(p,q)C^(-1)(p,q)^T=det B/det C`,                           (4.5)

so `|s_3|=|det B|/D`.

By (3.3), after absorbing all affine shifts into a scalar `A`, the conditional pair density is bounded by

`(2sqrt(3)/|b|) Psi(A +/- delta_3 z^2)`,

where

`delta_3=|s_3|/(2|b|)`.

Average over the third cap-one marginal and apply the account03/B16 weak-`L^2` theorem plus `int gh<=2||h||_{2,infinity}`:

`||p_Q||_infinity
 <= 2^(5/4) (2sqrt(3)) sqrt(15)
    ( D/(|b|^3 |det B|) )^(1/4).`                                    (4.6)

Condition (4.2) gives `D<=5b^2/4`, so (4.6) becomes (4.3)--(4.4). The bound is uniform in the conditioned outside coordinates; averaging preserves it. QED.

This strictly extends the partner's exact-null block `a=c=0` to a quantitative collar. The constant is not optimized.

## 5. Exact-rank-three aggregate collar

The same theorem can be combined with the partner's original-coordinate aggregate construction rather than selecting a third physical coordinate.

Assume `A=R Lambda R^T` has exact rank three, `R^TR=I_3`, and choose physical spectral rows `r_i,r_j`. Put

`a=r_i^T Lambda r_i`, `b=r_i^T Lambda r_j`, `c=r_j^T Lambda r_j`,
`Delta=||r_i wedge r_j||^2`.

Suppose `b!=0`, `Delta>0`, and `|a|,|c|<=|b|/2`. Let `v` be the Euclidean unit vector orthogonal to the pair and form the normalized original-coordinate tail aggregate

`Z=sum_{k notin {i,j}} <r_k,v> X_k`.

Parseval gives sum of squared coefficients equal to one, and the already completed affine-fiber theorem used by the partner gives `||p_Z||_infinity<=sqrt(e)`. The determinant of the three-direction compression `[r_i,r_j,v]^T Lambda [r_i,r_j,v]` is exactly `det(Lambda) Delta`. Therefore the same Schur calculation as in Section 4, now pairing the weak-`L^2` ridge against a density cap `sqrt(e)`, yields

`boxed( ||p_Q||_infinity
 <= C_near e^(1/4)
    ( |b| |det Lambda| Delta )^(-1/4) ),`                             (5.1)

with

`C_near e^(1/4)=43.3236332638965...`.                                (5.2)

This is a robust neighborhood of the partner's simultaneous-null aggregate endpoint. It still requires enough geometric currency in `|b|Delta`; proving that some near-null pair carries such currency in every remaining exact-rank-three frame is a separate structural question.

## 6. A pivot-free local corollary for every invertible physical triple

The near-null theorem also removes the discontinuity between a nonzero diagonal-pivot argument and the exactly-zero null-pair endpoint.

Let `B` be any invertible physical `3x3` principal block and define

`m=max_{1<=i<=j<=3}|B_ij|`.

### Corollary 6.1 — `QFORM-INVERTIBLE-TRIPLE-MAXENTRY-v1`

For the full ambient quadratic form, with arbitrary outside terms,

`boxed( ||p_Q||_infinity
 <= C_block (m |det B|)^(-1/4) ),`                                    (6.1)

where

`C_block=16*2^(1/4)*sqrt(15)
       =73.6924696255505...`.                                         (6.2)

### Proof

If some diagonal entry has magnitude at least `m/2`, apply the completed account03/B16 all-Schur-pivot theorem

`||p_Q||_infinity <=16sqrt(15)(|a||det B|)^(-1/4)`

and use `|a|>=m/2`.

Otherwise every diagonal has magnitude `<m/2`. A maximum entry must then be an off-diagonal `b` with `|b|=m`, and its two adjacent diagonal entries satisfy the hypotheses of Theorem 4.1. That theorem gives the smaller constant `C_near< C_block`. QED.

This is a local theorem, not a good-minor selection theorem. Diffuse frames can make every fixed triple's `m|det B|` tiny; the live corrections explicitly forbid promoting one reciprocal small minor into a global proof.

## 7. Return to the extremal product-set formulation

By this slot's exact bang-bang theorem, every density statement above transfers with **the identical constant** to the geometric slab problem on arbitrary unit-measure product sets. For example, under the hypotheses of Theorem 4.1, for all measurable `E_k` with `|E_k|=1`, all `t`, and all `epsilon>0`,

`|{x in product E_k: t<=x^TAx<=t+epsilon}|
 <= C_near (|b||det B|)^(-1/4) epsilon`.                              (7.1)

No centered interval, bounded diameter, bounded fragment count, or coefficient-continuity reduction is made.

## 8. Target-level consequence and remaining debt

The partner's named near-null interpolation gap is closed: the logarithmic hyperbolic product envelope survives simultaneous diagonal perturbations `|a|,|c|<=|b|/2` at a universal cost, and the weak-`L^2` third-direction payment then gives a bounded ambient density with an explicit determinant currency. In particular, every invertible physical triple has a pivot-free local estimate depending only on `m|det B|`, continuously covering tiny and zero diagonal pivots.

This does **not** prove the full conjecture. The three-large-eigenvalue hypothesis does not force a single physical triple with `m|det B|` universally bounded below. The next implication is therefore:

`QFORM-AGGREGATE-NEAR-NULL-DETERMINANT-PAYMENT-v1`:

> Starting from the current finite-heavy-core / grouped-coordinate determinant packets, pay the diffuse collection of bordered `3x3` currencies by aggregating original independent coordinates **before** taking reciprocal fourth roots; use Theorem 3.1 on near-null pair fibers and the existing rank-two affine half-Riesz theorem on complementary orientations. The result must retain arbitrary self blocks, outside couplings, additional spectrum and arbitrary fragmented product supports.

A proof of that aggregate implication, together with the already paid diffuse ridge branch, would materially advance the exhaustive structural reduction. A counterexample must be a genuine cap-one product-law / unit-product-set construction, not merely a receiver density or matrix-norm instability.

## 9. Verification

A deterministic standard-library checker tests the exact factorization, `kappa d=delta`, Schur determinant identity, and the uniform collar constants on 20,000 random admissible coefficient systems. The archived output ends `QFORM_NEAR_NULL_CHECK_PASS`; the maximum observed relative factorization error is below `9e-14`, and no constant inequality fails. These computations are sanity checks only; the proofs above are analytic.

No full-QFORM proof, optimal constant, continuous density representative, or independent-review claim is made.
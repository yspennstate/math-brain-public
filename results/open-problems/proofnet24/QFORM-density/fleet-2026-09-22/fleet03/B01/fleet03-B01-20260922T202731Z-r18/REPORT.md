SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-22T20:27:31Z.
attacking: off-diagonal-row averaged-frequency L^q smoothing with arbitrary residual quadratic coupling.

# QFORM fleet03/B01 r18 — exact-zero row endpoint and logarithmic signed-Fejer control

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / PROVED_INTERMEDIATE_OBSTRUCTION / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Fresh state and duplicate avoidance

The exact target remains open: for arbitrary `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal essential-supremum bound, or give a target-valid counterexample. Continuity is tracked separately.


A source-matching result appeared before this write, so I did not duplicate it. `fleet02/B02`, run `20260922T201015Z-fleet02-B02-qform-r12`, proves the general physical-row shear theorem

`T=aX^2+2XU+R`, `X independent of (U,R)`, `||p_U||_infinity<=M`,

`||p_T||_p <= [2^(p-1)/(2-p)]^(1/p) M^((p-1)/p)`, `1<p<2`,

uniformly in `a`, including `a=0`, and hence a global `L^3` characteristic-function bound at `p=3/2`. Source used here: `yspennstate/math-open-problems@99f0eb89b7b1ad3ef3f225460fb08d4d22c19a75`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T201015Z-fleet02-B02-qform-r12/REPORT.md`.

The new work below pays the **exact-zero scalar-pivot endpoint more sharply**: all finite density `L^p` exponents, a nearly linear small-ball estimate, a logarithmic signed-Fejer bound, and a sharp obstruction showing why the same improvement cannot be extended to arbitrary nonzero pivots without spending residual curvature.

## 2. Mandatory phase-aligned counterexample remains in force

For every `s!=0` and every small `delta>0`, the set

`E(s,delta)={x:dist(sx^2,2pi Z)<=delta}`

has infinite Lebesgue measure. Choosing a measurable subset of measure one and taking its indicator as the density gives

`Re E exp(i s X^2)>=cos(delta)`.

Thus no positive power pointwise decay in `|s|` can hold uniformly over all cap-one densities. Nothing below invokes such a bound.

## 3. Exact-zero physical row: all finite `L^p` exponents

### Theorem 3.1 — `QFORM-ZERO-PIVOT-ROW-ALL-LP-v1`

Let `X` be independent of a random pair `(U,R)`. Assume `X` has a probability density `f<=1` and `U` has a marginal density bounded by `M<infinity`. No independence between `U` and `R` is assumed. Put

`T=2XU+R`.                                                    (3.1)

Then for every `1<p<infinity`, `T` has a density and

`boxed: ||p_T||_p <= p M^(1-1/p).`                           (3.2)

No regularity of `R`, moments, support assumptions, or conditional density cap for `U|R` is used.

### Proof

Condition on `(U,R)=(u,r)`. Since `U` has a density, `P(U=0)=0`. For `u!=0`, the conditional density of `2uX+r` is

`q_(u,r)(y)=(2|u|)^(-1) f((y-r)/(2u))`.                      (3.3)

Hence

`||q_(u,r)||_p=(2|u|)^(-(1-1/p)) ||f||_p
               <=(2|u|)^(-(1-1/p))`,                        (3.4)

because `0<=f<=1` and `int f=1` imply `||f||_p<=1`.

Write

`beta=1-1/p in (0,1)`.                                       (3.5)

The unconditional law is the mixture of the conditional densities (3.3). Minkowski therefore gives

`||p_T||_p <= E (2|U|)^(-beta)`.                              (3.6)

Among probability densities `g<=M`, the expectation of the symmetric decreasing kernel `|u|^(-beta)` is maximized by the cap-saturated centered interval `g=M 1_{|u|<=1/(2M)}`. Consequently

`E (2|U|)^(-beta)
 <= M int_{-1/(2M)}^{1/(2M)} (2|u|)^(-beta) du
 = M^beta/(1-beta)
 = p M^(1-1/p)`.                                             (3.7)

This proves (3.2). QED.

### Physical-row specialization

If `A_ii=0`, write

`U_i=sum_{j!=i} A_ij X_j`,
`R_i=X_{-i}^T A_{-i,-i} X_{-i}`,                             (3.8)

so `Q=2X_iU_i+R_i`. Let

`sigma_i=(sum_{j!=i} A_ij^2)^(1/2)`.                         (3.9)

The one-dimensional product-projection estimate used and source-pinned in the completed fleet02/B02 report gives

`||p_(U_i)||_infinity <= sqrt(2)/sigma_i`                    (3.10)

when `sigma_i>0`. Therefore, for every finite `p>1`,

`boxed:
 ||p_Q||_p <= p (sqrt(2)/sigma_i)^(1-1/p).
`                                                                  (3.11)

This is an ambient full-matrix statement: the residual matrix and all of its couplings are arbitrary. It is not an `L^infinity` theorem.

## 4. Distribution-function consequence: a nearly linear zero-pivot estimate

For every interval `I` of length `ell`, Holder and (3.2) give

`P(T in I) <= p (M ell)^(1-1/p)`.                            (4.1)

If

`x=M ell <= e^(-2)`,                                         (4.2)

choose `p=log(1/x)>=2`. Then

`x^(1-1/p)=e x`,                                              (4.3)

and therefore

`boxed:
 P(T in I) <= e M ell log(1/(M ell)).
`                                                                  (4.4)

Thus an exact zero physical pivot is only one logarithm away from the target linear small-ball estimate, under no control at all on the dependence of the residual term `R` on `U`.

For a zero diagonal physical row of a quadratic form, (3.10) turns this into

`P(Q in I)
 <= (e sqrt(2) ell/sigma_i)
    log(sigma_i/(sqrt(2) ell))`                              (4.5)

whenever `sqrt(2) ell/sigma_i<=e^(-2)`.

## 5. The logarithm is genuinely necessary for one zero-pivot row

Take independent

`X,U ~ Uniform[-1/2,1/2]`, `R=0`, and `T=2XU`.                (5.1)

The density is computed exactly as

`p_T(t)=log(1/(2|t|)) 1_{0<|t|<1/2}`.                       (5.2)

Indeed the product `Z=XU` has density

`p_Z(z)=2 log(1/(4|z|))`, `0<|z|<1/4`,                      (5.3)

and `T=2Z` gives (5.2). Consequently

`P(|T|<=ell/2)=ell[1+log(1/ell)]`                            (5.4)

for `0<ell<1`.

So no estimate `P(T in I)<=C M |I|` can follow from the zero-pivot row resource alone. Equivalently, one zero bilinear row does **not** imply a bounded density. This is an intermediate-mechanism obstruction, not a QFORM counterexample: the corresponding two-variable matrix has only the two large eigenvalues `+1,-1`.

## 6. Signed-Fejer averaged-frequency theorem for the zero-pivot row

The designated partner `fleet04/B01` proved the exact signed-Fejer interface. For a law `mu` with characteristic function `phi`, define

`D_T mu(y)=(1/(2pi)) int_{-T}^T (1-|t|/T)
             Re(e^(-ity) phi(t)) dt`.                        (6.1)

Its canonical report is

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

The partner theorem identifies `D_T mu=p_mu*K_T` when a density exists, where

`K_T(x)=2 sin^2(Tx/2)/(pi T x^2)`,
`K_T>=0`, `int K_T=1`, `||K_T||_infinity=T/(2pi)`,             (6.2)

and proves `||p_mu||_infinity=sup_{T,y}D_T mu(y)` whenever the left side is finite, with the converse bounded-Fejer criterion as well.

Apply this result to Theorem 3.1. Let `q=p/(p-1)`. Interpolation between `L^1` and `L^infinity` for the probability kernel gives

`||K_T||_q
 <= ||K_T||_infinity^(1-1/q)
 = (T/(2pi))^(1/p)`.                                         (6.3)

Therefore Holder in physical space and (3.2) yield the genuine signed averaged-frequency estimate

`boxed:
 sup_y D_T law(T)(y)
 <= p M (T/(2pi M))^(1/p),   every p>1.
`                                                                  (6.4)

This is a direct application of the designated partner theorem to a new inequality, not a citation-only use.

Put

`L=log(T/(2pi M))`.                                           (6.5)

If `T/(2pi M)>=e^2`, choose `p=L` in (6.4). Then

`boxed:
 sup_y D_T law(T)(y)
 <= e M log(T/(2pi M)).
`                                                                  (6.6)

For `T/(2pi M)<e^2`, the trivial probability-kernel bound gives

`sup_y D_T law(T)(y)<=T/(2pi)<e^2 M`.                        (6.7)

Thus a compact all-scale version is

`boxed:
 sup_y D_T law(T)(y)
 <= e^2 M + e M log_+(T/(2pi e^2 M)).
`                                                                  (6.8)

For an actual zero-diagonal physical row, substitute `M<=sqrt(2)/sigma_i` from (3.10).

### Sharp logarithmic growth in the rank-two control

For the explicit product law (5.1), use the scaled Fejer kernel in (6.2):

`D_T(0)=int K_T(s) log(1/(2|s|)) 1_{|s|<1/2} ds`.             (6.9)

With `z=Ts`,

`K_T(z/T) dz/T = [2 sin^2(z/2)/(pi z^2)] dz`.                (6.10)

The bracketed kernel has total mass one, and its product with `|log|z||` is integrable both at zero and infinity. Hence dominated convergence after separating the `log T` term gives

`boxed: D_T(0)=log T + O(1) as T->infinity.`                 (6.11)

Therefore even the **signed** Fejer quantity grows logarithmically from one exact-zero bilinear row. The logarithm is not merely an artifact of taking absolute values in Fourier space. A third independent/product-preserving curvature resource is genuinely needed to turn this endpoint into the target uniform Fejer bound.

## 7. New general-row small-ball corollary from the completed peer theorem

The fleet02/B02 source-matching theorem is still useful at nonzero or unknown scalar pivot. Write

`x=M ell`, `L=log(1/x)`.                                      (7.1)

When `x<=e^(-4)`, set

`delta=2/L`, `p=2-delta`.                                    (7.2)

The peer bound and Holder imply

`P(T in I)
 <= [2^(1-delta)/delta]^(1/(2-delta))
    x^((1-delta)/(2-delta)).`                                (7.3)

A direct algebraic comparison gives

`log( RHS / sqrt(xL) )
 = [L+log L-2log2]/[2L-2] <= 2/3`,                           (7.4)

where the final inequality for `L>=4` follows from

`3 log L-6log2+4<=L`,                                        (7.5)

with equality at `L=4` and decreasing derivative thereafter. Thus

`boxed:
 P(T in I)
 <= e^(2/3) sqrt(M ell log(1/(M ell)))
 <2 sqrt(M ell log(1/(M ell))).
`                                                                  (7.6)

For a full quadratic form and a physical row with off-diagonal norm `sigma_i>0`, (3.10) yields

`P(Q in I)
 <2 sqrt( (sqrt(2) ell/sigma_i)
          log(sigma_i/(sqrt(2) ell)) )`                      (7.7)

whenever `sqrt(2) ell/sigma_i<=e^(-4)`.

This is weaker than the exact-zero estimate (4.5), but it is uniform through every scalar pivot and arbitrary residual dependence.

## 8. Why the `p<2` barrier for a general scalar pivot is real

The fleet02/B02 theorem stops at `p<2`. That endpoint cannot be removed using only the hypotheses of its physical-row model.

Take independent

`X,U ~ Uniform[-1/2,1/2]`,                                   (8.1)

and set

`a=1`, `R=U^2`.                                               (8.2)

Then `U` has density cap one but

`T=X^2+2XU+U^2=(X+U)^2`.                                    (8.3)

The sum `S=X+U` has triangular density

`h(s)=(1-|s|) 1_{|s|<1}`.                                   (8.4)

Therefore

`p_T(y)=[h(sqrt(y))+h(-sqrt(y))]/[2sqrt(y)]
       =(1-sqrt(y))/sqrt(y)`, `0<y<1`.                       (8.5)

Hence `p_T notin L^2` and `||p_T||_infinity=infinity`. This proves that no theorem depending only on a cap for `U`, the independence of `X`, and arbitrary residual dependence can upgrade the general-row estimate to `L^2` or `L^infinity` when `a!=0`.

Again, this is **not** a counterexample to the QFORM target: the matrix behind (8.3) has rank one. It is a source-valid falsifier of a tempting intermediate endpoint upgrade. To pass from (7.6) to the full theorem, the proof must spend additional curvature/spectral currency rather than squeeze more from the one-row shear alone.

## 9. Consequence for the current full-target route

The exact-zero and nonzero-pivot behavior now has a sharp functional-analytic boundary:

* exact zero pivot plus one bounded-density shear gives every finite density `L^p`, nearly linear `ell log(1/ell)` concentration, and only logarithmic signed-Fejer growth;
* arbitrary scalar pivot gives the completed peer's `1<p<2` density scale and the new optimized `sqrt(ell log(1/ell))` concentration;
* the nonzero square-collapse example proves that a row-only `L^2/L^infinity` endpoint is false;
* the rank-two bilinear example proves that a zero-row-only uniform signed-Fejer endpoint is also false.

So the first unpaid implication is no longer to improve a single-row oscillatory estimate. It is to **spend the simultaneously retained third-direction/residual disjoint-pair resource before the logarithmic Fejer growth develops**. In the exact-rank-three overlap-one branch of fleet02/B02, the selected near-isotropic row already carries both its global row `L^3` credit and a quantitative residual disjoint-pair mass. A successful grouped estimate must combine those two resources jointly; multiplying fictitious independent characteristic functions is not allowed.

Essential boundedness of the full target remains OPEN. Continuity of the full target remains OPEN. The new exact-zero theorem proves only finite-`p` densities and concentration/Fejer estimates; no continuous representative is claimed.

## 10. Provenance and execution status

Designated partner actually applied: `fleet04/B01`, signed-Fejer exact interface, canonical source stated in Section 6.

Completed same-scope peer consumed to avoid duplication: `fleet02/B02`, physical-row `1<p<2` theorem, source stated in Section 1.

Repository transport and read/write do not establish native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`. No scheduler, notification, email, Drive, public-release, workflow, paid-model/API/Codex, credential, or cross-account action is part of this mathematical report.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T11:32:53Z.
attacking: posterior-to-prior transfer of the random conditional critical value, and a Gaussian-to-Laplace two-sided certificate for the remaining minority/two-sheet mass.

# QFORM B15 — critical-value prior transfer and dual minority packing

**Status:** `PROVED_SUPPORTING_LEMMAS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and first unpaid implication

The owner target remains: independent real coordinates with probability densities `0<=f_i<=1`, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one; prove a universal essential-density bound for `Q=X^T A X`, or give a valid target counterexample. No moment, support, log-concavity, connectedness, diagonal-basis, or post-rotation independence assumption is made.

The first unpaid implication in the physical-indefinite-three-block branch can now be stated sharply. Once the conditional majority one-sheet submeasure has been paid, a putative large heat height must simultaneously:

1. force substantial **unconditioned original product-law mass** of outside coordinates whose conditional critical value lies above a heat-mode-dependent threshold; and
2. force **two adjacent minority/two-sheet output intervals**, on opposite sides of a Laplace mode, to carry comparable mass.

The remaining task is to rule out this simultaneous configuration from original-coordinate product provenance (or route it into a completed volume/grouped-coordinate exit). A generic X-ray bound is not enough; `QFORM-TWOSHEET-XRAY-ONLY-FALSE` remains binding.

## 2. Sources actually consumed and applied

Required owner-pinned source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`;
- `.../FOURIER_ROUTE_REPORT.md`;
- `.../COUNTEREXAMPLE_SEARCH.md`.

The completed result from that source applied below is Theorem C in `COUNTEREXAMPLE_SEARCH.md`: for an exact rank-three `(+,+,-)` form, the majority one-sheet output submeasure has density at most

`C_B=(lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta`,

hence `C_B<=pi sqrt(2)/kappa`, `kappa=min(lambda_1,lambda_2,mu)`.

Latest compatible assigned partner used:

`fleet03/B15`, source-pinned at
`yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T103159Z-fleet03-B15-qform-auto11/REPORT.md`.

Its abstract paid-submeasure lemma gives balanced Laplace half-posterior excision and the two-sided local packing bounds (3.4)--(3.7). I also use the immediately preceding completed fleet03/B15 Gaussian Gibbs theorem, source-pinned at the same repository commit:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T082718Z-fleet03-B15-qform-auto16/REPORT.md`.

That theorem gives the heat-mode subgaussian posterior, inverse-weight identity, and exact KL identity used in Section 5 below.

## 3. Ambient rough one-sheet payment, rechecked

Let `S` be three original coordinates, `W=X_{S^c}`, and suppose the physical principal block `B=A_SS` is invertible of signature `(2,1)`, with eigenvalues `lambda_1,lambda_2,-mu`, all three magnitudes positive. Put

`kappa=min(lambda_1,lambda_2,mu)`.

Condition on `W=w`. Then

`Q_w(x)=x^T B x+2d(w)^T x+c_0(w)`

`      =(x+B^{-1}d(w))^T B (x+B^{-1}d(w))+c(w)`,

where

`c(w)=c_0(w)-d(w)^T B^{-1}d(w)`.

This is a translation in the three **original** coordinates, so their conditional laws remain independent with cap-one densities. Diagonalising `B` is used only to write the quadratic surface; no independence after that rotation is asserted.

Define the random majority event

`G={Q>=c(W)}`

and its output submeasure

`mu_G(E)=P(Q in E, G)`.

Applying the owner-pinned ruled theorem conditionally gives, for every interval `I`,

`P(Q in I, G | W=w) <= C_B |I|`,

where

`C_B=(lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi)
 [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta`

and

`C_B<=pi sqrt(2)/kappa`.

Averaging in `w` yields the ambient measure domination

`boxed(mu_G <= C_B dx.)`                                           (3.1)

### Rough-input audit

There is no continuity shortcut hidden in (3.1). If desired, mollify only the three active **original-coordinate** marginals: `f_i^(eta)=f_i*gamma_eta`. This preserves independence and the cap `<=1`, and their threefold product converges in `L^1`. The conditional completion shift depends on `w`, but translation leaves the same `L^1` error. Deterministic quadratic pushforward and restriction to `G` contract total variation. Thus the smooth conditional interval inequality passes to the rough source with the same constant and then averages in `w`. This proves essential boundedness of `mu_G`; it does not prove continuity of its density.

## 4. Gaussian-to-Laplace compiler: large heat height forces two-sided minority packing

Fix `epsilon>0`. Write

`gamma_epsilon(u)=(sqrt(2pi)epsilon)^(-1) exp(-u^2/(2epsilon^2))`,

`ell_epsilon(u)=(2epsilon)^(-1) exp(-|u|/epsilon)`.

The pointwise kernel ratio is

`gamma_epsilon(u)/ell_epsilon(u)
 =sqrt(2/pi) exp(-z^2/2+|z|)`, `z=u/epsilon`,

so

`boxed(gamma_epsilon(u) <= c_0 ell_epsilon(u),
       c_0=sqrt(2e/pi).)`                                          (4.1)

Let

`M=max_y E gamma_epsilon(Q-y)`,

`L=max_y E ell_epsilon(Q-y)`.

Then (4.1) gives

`boxed(L >= M/c_0.)`                                               (4.2)

Now apply the latest fleet03/B15 paid-submeasure theorem to the event `G` in (3.1). If `M>c_0 C_B`, then `L>C_B`. Let `z_*` be a global Laplace mode. Put

`a=epsilon(M/c_0-C_B)>0`,

`R=log(2/a)`.

The partner theorem gives a radius

`r_*=log(2/[epsilon(L-C_B)]) <= R`

and minority-event masses at least `epsilon(L-C_B)/2 >= a/2` on both sides. Therefore, enlarging the two intervals from `r_*epsilon` to `R epsilon`,

`boxed(P(G^c, z_*<Q<z_*+R epsilon) >= a/2,)`                       (4.3)

`boxed(P(G^c, z_*-R epsilon<Q<z_*) >= a/2.)`                       (4.4)

Here `G^c={Q<c(W)}` is exactly the conditional minority/two-sheet event. The quantity `a` is automatically at most one because the partner Laplace balance gives `epsilon L<=1`, so `R>=log 2` is well-defined.

Thus a high Gaussian heat mode cannot hide merely in a one-sided or infinitesimal endpoint defect: after the majority submeasure is paid, it forces **two-sided local minority packing** at the same smoothing scale, with explicit mass

`(epsilon/2)(M/c_0-C_B)`.

No continuity of the raw output density is used.

## 5. New posterior-to-prior critical-value transfer

Let `y_*` be a global Gaussian heat mode at scale `epsilon`, so

`M=E gamma_epsilon(Q-y_*)`.

Define the Gaussian Gibbs posterior on the original source space by

`dnu/dP=gamma_epsilon(Q-y_*)/M`,

and put

`U=(Q-y_*)/epsilon`,

`R_c=(y_*-c(W))/epsilon`.

The completed fleet03/B15 Gaussian theorem gives

`E_nu exp(vU)<=exp(v^2/2)` for every real `v`,                      (5.1)

and hence

`nu(U<-d)<=exp(-d^2/2)`.                                           (5.2)

From the paid submeasure (3.1),

`M nu(G)=(mu_G*gamma_epsilon)(y_*)<=C_B`.                           (5.3)

If `R_c>=d` and `U>=-d`, then

`Q>=y_*-d epsilon>=c(W)`,

so the point lies in `G`. Therefore

`{R_c>=d} subset G union {U<-d}`,

and for every `d>0`,

`boxed(nu(R_c>=d) <= delta_d:=C_B/M+exp(-d^2/2).)`                 (5.4)

This is the posterior critical-value shadowing inequality.

The genuinely new step is to transfer (5.4) back to the **unconditioned product law** `P`. Define

`E_d={c(W)>y_*-d epsilon}={R_c<d}`.

Then

`nu(E_d)>=1-delta_d`.                                              (5.5)

The Gaussian Gibbs theorem also gives the exact entropy identity

`D_KL(nu||P)
 =-log(sqrt(2pi)epsilon M)-(1/2)E_nu U^2`

and hence

`D_KL(nu||P)<=L_G:=-log(sqrt(2pi)epsilon M)`.                      (5.6)

Let `p=P(E_d)` and `a_nu=nu(E_d)`. Data processing to the indicator of `E_d` yields

`D_KL(nu||P)>=kl(a_nu||p)`

`=a_nu log(a_nu/p)+(1-a_nu)log((1-a_nu)/(1-p))`

`>=a_nu log(1/p)-h(a_nu)`,                                        (5.7)

where `h` is binary entropy. In particular `h(a_nu)<=log 2` and `a_nu>=1-delta_d`. If `delta_d<1`, (5.6)--(5.7) imply

`(1-delta_d) log(1/p) <= L_G+log 2`.

Therefore

`boxed(P(c(W)>y_*-d epsilon)
 >= [sqrt(2pi)epsilon M/2]^(1/(1-delta_d)).)`                      (5.8)

If additionally `delta_d<=1/2`, then `a_nu>=1-delta_d>=1/2` and the binary entropy is decreasing on `[1/2,1]`, so `h(a_nu)<=h(delta_d)`. This improves (5.8) to

`boxed(P(c(W)>y_*-d epsilon)
 >= [sqrt(2pi)epsilon M exp(-h(delta_d))]^(1/(1-delta_d)).)`       (5.9)

### Self-consistent blow-up scale

If `M>=4C_B`, choose

`d_M=sqrt(2 log(M/C_B))`.

Then `exp(-d_M^2/2)=C_B/M` and

`delta_{d_M}=2C_B/M<=1/2`.

Hence

`boxed(P(c(W)>y_*-epsilon sqrt(2log(M/C_B)))`
` >= [sqrt(2pi)epsilon M exp(-h(2C_B/M))]^(1/(1-2C_B/M)).)`       (5.10)

A simpler but weaker form is

`boxed(P(c(W)>y_*-epsilon sqrt(2log(M/C_B)))`
` >= [sqrt(2pi)epsilon M/2]^(1/(1-2C_B/M)).)`                     (5.11)

Thus a sequence with `M/C_B -> infinity` cannot obtain its heat height solely from an exotic Gibbs reweighting of a tiny set of outside coordinates: it forces a quantitative **base-law** upper-tail event for the actual conditional critical value `c(W)`.

This is a real product-provenance interface, because `W` is a subcollection of the original independent coordinates. It is not yet a proof of the full target: a one-sided upper tail for `c(W)` may itself be large.

## 6. Combined obstruction to a blow-up sequence

For every ambient physical `(2,1)` three-block, any scale-`epsilon` Gaussian heat maximum `M` with `M>max(4C_B,c_0 C_B)` forces simultaneously:

1. the base-law critical-value tail (5.10)/(5.11) at the Gaussian mode `y_*`; and
2. the two-sided conditional-minority packing (4.3)/(4.4) around a Laplace mode `z_*`.

So the local obstruction is no longer merely “control the two-sheet trace.” A genuine blow-up sequence must make the outside product law create many critical values near/above the heat center **and** place minority-sheet mass on both sides of a balanced mode at the same microscopic scale.

A useful contrapositive of (5.8) is: if a structural branch can prove

`P(c(W)>y_*-d epsilon)<=p`,

then, with `delta_d=C_B/M+exp(-d^2/2)<1`, necessarily

`-log(sqrt(2pi)epsilon M)
 >=(1-delta_d)log(1/p)-log 2`.                                    (6.1)

Thus an original-coordinate tail estimate for the Schur critical value can be compiled directly into a heat-height bound; no continuity theorem is needed.

## 7. Regularity ledger

The logical implications remain separated.

- For every nonzero symmetric `A`, the quadratic pushforward of an absolutely continuous joint law is absolutely continuous. Local coarea/submersion gives this because `grad(x^T A x)=2Ax` vanishes only on the proper null subspace `ker A`.
- Absolute continuity alone does not imply essential boundedness.
- The ruled estimate (3.1) is an **essential-density** statement for a positive submeasure, obtained directly from interval/coarea geometry plus product-projection provenance.
- The rough-input limiting argument uses source `L^1`/total variation only to pass that measure inequality; it does not infer height from continuity.
- Fixed-instance `C_0` conclusions, where available from completed source reports, are qualitative and separate.
- The universal essential `L^infinity` bound under the owner target remains open.

## 8. What remains

The first unpaid local implication is to exploit the original-coordinate law of the Schur critical value `c(W)` together with the two-sided minority packing certificate. A sufficient next theorem would be a product-preserving alternative saying that, for every high local ratio `M/C_B`, either the tail event in (5.10) is quantitatively too small, or the two-sided minority intervals in (4.3)--(4.4) trigger a completed volume/grouped-coordinate payment. Generic two-sheet X-ray control is explicitly excluded by the live correction.

Globally, one must still supply the structural glue for matrices having no uniformly conditioned physical indefinite triple. The owner-pinned Fourier report supplies completed determinant-volume exits in several diffuse regimes, but not a universal partition theorem covering every three-large-eigenvalue matrix.

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**

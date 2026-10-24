SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T17:52:42.882125912Z.
attacking: repair the invalid interval-to-Borel frozen-slice receiver by identifying the exact Borel concentration currency, prove sharp interface obstructions, and spend a completed e5f hub theorem on a target-valid lift.

# account02/B05 auto11 — Borel-stable hub receiver and exact rough-interface obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound; complementary constructions/source-valid counterexamples.  
**OWNER CONTROL:** revision `2026-09-22.15`, current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `PROVED_SUPPORTING_THEOREM / PROVED_INTERMEDIATE-INTERFACE OBSTRUCTIONS / FULL QFORM OPEN`.  
**Regularity:** the new receiver proves essential boundedness under a Borel slice profile; continuity is not asserted there. The target-valid e5f lift below has a continuous density by an L1 characteristic-function estimate.

The current owner correction explicitly invalidates the earlier account02/B05 use of an interval-only frozen-slice square-root estimate as though it were a Borel-set profile for an arbitrary rough hub. The valid interval/Fourier estimate is preserved; the rough-law corollary is not. This run identifies exactly what replacement is sufficient, proves that neither interval control nor a half-Riesz potential implies it, and then shows with a target-valid exact-rank-three lift that genuine third curvature repairs the logarithmic witness when it is retained before maximalisation.

## 1. First unpaid implication at start

The corrected unpaid step is not “improve the interval exponent.” It is:

`QFORM-HUB-JOINT-MAXIMAL-CURVATURE-BRIDGE-v1`:

> In a rough one-hub / near-null / mixed-transverse packet, obtain the O(epsilon) interval bound while retaining the independent scalar-bank or third-curvature variable jointly with the curved slice. Do not first turn an interval profile or a fractional trace into a supremum over arbitrary measurable frozen fibers.

The theorem below makes the missing maximal currency explicit.

## 2. `QFORM-HUB-BOREL-FROSTMAN-RECEIVER-v1`

Let `X` be independent of `(L,Y)`, with a probability density `f_X<=1`, and let `a!=0`. Assume the joint law of `(L,Y)` is absolutely continuous in the `L` coordinate and disintegrates as

`nu(dl,dy)=dl mu_l(dy)`,

where `mu_l` is a finite measure on the `Y` line, `m(l):=mu_l(R)`, and

`int_R m(l) dl=1`.

For `0<beta<=1`, define the Borel concentration seminorm

`K_beta(l):=sup_{0<|E|<infinity} mu_l(E)/|E|^beta`,                    (2.1)

where the supremum is over measurable `E subset R` of finite positive Lebesgue measure.

Suppose `K_beta(l)<=K` for a.e. `l`. Then for

`Q=2 a X L + Y`                                                        (2.2)

one has

`boxed{ ||p_Q||_infinity <= ((1+beta)/beta) K^(1/(beta+1)) |a|^(-1/(beta+1)). }`    (2.3)

The statement is at the essential-density / interval-measure level; no continuity of the frozen slices is assumed.

### Proof

For fixed `l!=0`, the hub density kernel, viewed as a function of `y`, is

`h_{q,l}(y)=(2|a l|)^(-1) f_X((q-y)/(2 a l)).`                         (2.4)

It has

`0<=h_{q,l}<=H_l:=(2|a l|)^(-1)`,  and  `int h_{q,l}(y)dy=1`.           (2.5)

Layer cake and (2.1) yield

`int h_{q,l} dmu_l`
` = H_l int_0^1 mu_l({h_{q,l}>H_l s}) ds`
` <= K H_l int_0^1 |{h_{q,l}>H_l s}|^beta ds`
` <= K H_l (int_0^1 |{h_{q,l}>H_l s}| ds)^beta`
` = K H_l^(1-beta).`                                                    (2.6)

The penultimate inequality is Jensen for the concave map `x^beta`; the last identity uses (2.5). Trivially also

`int h_{q,l} dmu_l <= m(l)H_l.`                                        (2.7)

Therefore

`p_Q(q) <= int_R min{ K(2|a l|)^(beta-1), m(l)/(2|a l|) } dl.`         (2.8)

For any `R>0`, use the first term on `|l|<R` and the second outside:

`p_Q(q) <= (2^beta K/beta)|a|^(beta-1) R^beta + 1/(2|a|R).`            (2.9)

The minimizing radius satisfies

`R^(beta+1)=[2^(beta+1)K|a|^beta]^(-1).`                               (2.10)

Substitution gives (2.3). QED.

For the square-root exponent,

`boxed{ beta=1/2:  ||p_Q||_infinity <= 3 K^(2/3)|a|^(-2/3). }`         (2.11)

This is the rigorous Borel-stable receiver that the invalid interval-to-Borel transfer was trying to emulate. It never takes an unrestricted curved-fiber supremum; it assumes exactly the measurable-set profile needed by layer cake.

## 3. `QFORM-INTERVAL-TO-BOREL-HUB-TRANSFER-FALSE-v1`

The distinction between interval control and (2.1) is real even for laws constructed from independent cap-one coordinates.

For an integer `N>=2`, let

`E_N = union_{k=1}^N [3Nk, 3Nk+1/N]`,                                  (3.1)

and let `X,U` be independent with density `1_{E_N}`. Since `|E_N|=1`, these are probability densities with cap one.

For every interval `J` of length `h`,

`|E_N intersect J| <= sqrt(h/N).`                                      (3.2)

Indeed: if `h<=1/N`, the left side is at most `h`; if `1/N<h<3N-1/N`, `J` meets at most one tooth and the left side is at most `1/N`; if `h>=3N-1/N>=N`, the left side is at most one. Each case gives (3.2).

Let `L` be independent and uniform on `[1/N,1+1/N]`, and put

`Y=-sqrt(2) L U`.                                                       (3.3)

For every fixed `l` and every interval `I`, scaling (3.2) gives

`P(Y in I | L=l) <= 2^(-1/4)(lN)^(-1/2)|I|^(1/2)`
`                  <= 2^(-1/4)|I|^(1/2).`                              (3.4)

Thus the frozen slices enjoy a uniform interval square-root estimate.

But their Borel square-root seminorms diverge. The entire scaled support has Lebesgue measure `sqrt(2)l` and conditional mass one, so

`K_{1/2}(l) >= 2^(-1/4) l^(-1/2).`                                     (3.5)

At `l=1/N`, this is at least `2^(-1/4)sqrt(N)`.

The logarithmic cost appears in the corresponding hub output. Set

`B_N=sqrt(2)L(X-U).`                                                    (3.6)

Since

`p_{X-U}(0)=int 1_{E_N}(x)^2 dx=1`,                                   (3.7)

conditioning on `L` gives the exact identity

`boxed{ p_{B_N}(0)=2^(-1/2) int_{1/N}^{1+1/N} dl/l
                     =2^(-1/2) log(N+1). }`                            (3.8)

Hence no universal receiver may replace the Borel profile in Theorem 2 by interval-only square-root control. This is an intermediate proof-interface counterexample, not a counterexample to QFORM: the quadratic matrix of (3.6) has only the two nonzero eigenvalues `+1,-1`.

## 4. Apply the newest designated partner result: half-Riesz does not Borelise the slice

The newest completed account03/B05 result is

`yspennstate/math-open-problems@9e0a5c32599f8cc180dd905615c9d034a9b51d2c:`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T172119Z-account03-B05-QFORM-r29/REPORT.md`.

Its `QFORM-RATIOPACKET-CURRENCY-COMPENSATION-v1` proves, in the low-`Psi` active-shear chamber,

`chi |det C| + Psi >= (1/4) mu m theta^4`,                              (4.1)

and therefore obtains the strong pair trace

`sup_t E|Q-t|^(-1/2) <=128(8chi/(mu m theta^4))^(1/4)`                  (4.2)

whenever the displayed low-`Psi` hypotheses hold. The partner correctly does **not** claim that (4.2) is itself a density theorem.

The following construction proves why (4.2) cannot be converted abstractly into the Borel currency (2.1).

For `N>=2`, put

`delta=N^(-2)`, `D=16N^4`,

`g_N(y)=N 1_{ union_{k=1}^N [kD,kD+delta] }(y).`                        (4.3)

This is a probability density. For every `t`, the contribution of a nearest component to

`int |y-t|^(-1/2) g_N(y)dy`                                            (4.4)

is at most `2sqrt(2)`. Every non-nearest component is at distance at least `(D-delta)/2>D/3`; since each has mass `1/N`, all non-nearest components together contribute at most

`sqrt(3)/sqrt(D)=sqrt(3)/(4N^2)<1/8.`                                  (4.5)

Thus

`boxed{ sup_t int |y-t|^(-1/2)g_N(y)dy <3 }`                            (4.6)

uniformly in `N`.

On the other hand, for `E` equal to the union of the `N` support components,

`|E|=N delta=1/N`, `mu_N(E)=1`, so

`boxed{ K_{1/2}(mu_N)>=sqrt(N). }`                                     (4.7)

Therefore there is no universal implication

`bounded half-Riesz potential => bounded Borel square-root profile`.   (4.8)

This is a real application/obstruction for partner r29: its increasingly strong half-Riesz credit in the low-`Psi` chamber must be coupled to the two independent scalar banks **before** a maximal measurable-set operation. Passing first through a Borelised frozen profile is provably impossible in general.

## 5. Apply the required pinned e5f completed result to a target-valid lift

Now lift the logarithmic witness (3.6) by a genuinely independent third curvature. Let `S_1,S_2` be independent cap-one variables, independent of `(L,X,U)`, and define

`Q_N=sqrt(2)L(X-U)+(S_1+S_2)^2/2.`                                     (5.1)

In the variable order `(L,X,U,S_1,S_2)`, the quadratic matrix is the direct sum of

`[[0,1/sqrt(2),-1/sqrt(2)], [1/sqrt(2),0,0], [-1/sqrt(2),0,0]]`

and

`[[1/2,1/2],[1/2,1/2]].`                                               (5.2)

Hence its spectrum is exactly

`{-1,1,1,0,0}`.                                                        (5.3)

So (5.1) is in the exact target class for every `N`.

Apply Theorem H from the required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Take hub `H={L}` and light set `I={X,U,S_1,S_2}`. On `I`, the quadratic block is rank one,

`A_II=v v^T`, `v=(0,0,1/sqrt(2),1/sqrt(2))`,                            (5.4)

while the hub-cross column is

`A_IH=(1/sqrt(2),-1/sqrt(2),0,0)^T`.                                   (5.5)

The augmented row vectors are therefore

`(0, 1/sqrt(2)), (0,-1/sqrt(2)), (1/sqrt(2),0), (1/sqrt(2),0)`.        (5.6)

Their Gram matrix is `I_2`, and every normalized leverage is exactly `1/2`, so all hypotheses of Theorem H are met. With one hub and one Fresnel square, Theorem H gives

`|phi_{Q_N}(t)| <= 4 pi^(3/2)|t|^(-3/2).`                              (5.7)

Combining with `|phi|<=1`,

`int_R |phi_{Q_N}(t)|dt <=6(4pi^(3/2))^(2/3)`.                         (5.8)

Fourier inversion yields the dimension- and `N`-free bound

`boxed{ ||p_{Q_N}||_infinity <=3*2^(4/3)=7.559526299369239... }`        (5.9)

and the density is continuous because the characteristic function is integrable.

This is the required concrete application of a completed `e5f71d79...` result to a real target inequality. It proves that the logarithmic frozen-slice pathology from Section 3 is a failure of the interval-to-Borel proof interface, not a QFORM counterexample: once a genuine third curvature is retained jointly, the whole output is uniformly smoothed.

## 6. Relation to the current Claude continuation

The verified Claude continuation at commit

`c4c23b784395630c094ba299a50712209921d1ae`

updates `single_hub_core/REPORT.md` with the open “hub that sees P” quantity

`Phi(s)=int [ sup_{|A|=1} int_A W(x,p) dx ] dp`                         (6.1)

and proposed estimate `(SP) Phi(s)<=C`. That report explicitly keeps `(SP)` open and observes growth of related maximal functionals for comb laws. The Borel receiver above clarifies the same obstruction from the real-variable side: the dangerous operation is the arbitrary measurable top-set supremum after freezing. An interval profile or a half-Riesz trace does not control it.

Thus the next viable proof should estimate the hub/light pairing before taking this maximal operation, or derive a product-sensitive Borel profile from additional genuine curvature—not from interval data alone.

## 7. Exact remaining implication

The first unpaid B05 implication after this run is:

`QFORM-HUB-JOINT-MAXIMAL-CURVATURE-BRIDGE-v1`:

> In the surviving rough one-hub / near-null / mixed-transverse configuration, combine the hub with the partner r29 pair half-Riesz resource and the two independent scalar banks at the **joint** coarea/Fourier level to prove an `O(epsilon)` interval estimate. The argument must occur before the arbitrary-set supremum represented by `K_beta` or Claude's `Phi(s)`. If the mixed determinant currency collapses, transfer to the already identified escaped-curvature structural branch rather than attempting to Borelise (4.2).

Equivalently, the missing factor is now isolated: one needs a product-sensitive estimate of a hub kernel against a moving curved trace that retains third smoothing until after aggregation. Flat interval Frostman control and isolated fractional trace control are separately insufficient.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No moments, compact support, log-concavity, identical laws, post-rotation independence, arbitrary-joint coarea bound, positive conditional-density moment, unrestricted fiber supremum, or law-uniform pointwise stationary-phase decay is used.

## Source pins

Current controls were read fresh from `yspennstate/math-research-brain` at the run start and refreshed before this report; the programme revision is `2026-09-22.5`, owner control `2026-09-22.15`, and the current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

Required old-Claude source actually applied: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md` Theorem H; `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md` were also read at their pinned revision.

Current Claude continuation checked: `math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`, `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`; `(SP)` is used only as an open-obstruction comparison, never as a premise.

Designated partner actually applied: `math-open-problems@9e0a5c32599f8cc180dd905615c9d034a9b51d2c`, account03/B05 r29.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T07:19:47Z.
attacking: the zero-anchor shared-coefficient double-star branch; replace factorized negative moments by a joint-density weighted receiver and isolate the near-collinear coefficient tube.

# account03/B06 r29 — shared-coefficient weighted double-star receiver

**Run:** `20260923T071947Z-account03-B06-qform-r29`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Classification:** `NEW SUPPORTING ANALYTIC THEOREM + LIVE ZERO-ANCHOR APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first missing implication

The owner target remains: for every dimension, independent ORIGINAL real coordinates whose one-dimensional probability densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal constant, or give a valid target counterexample. No Gaussian, log-concave, moment, compact-support, connected-support, iid, or diagonal-basis assumption is added. Orthogonal changes of deterministic matrices are not used to manufacture independence.

The previous B06 run proved an aggregate two-hub anchor currency. In its zero-cross-anchor branch, after writing the cross block around one physical row/column anchor as

`B=[[0,r^T],[c,D]]`,

the whole incident determinant mass is exactly

`Z_anchor=||c||_2^2 ||r||_2^2`.

In the live low-disjointness chamber,

`Z_anchor > (127/800) G^4`,                                         (1.1)

hence

`||c||_2 ||r||_2 > sqrt(127/800) G^2
                    =0.3984344362... G^2`.                          (1.2)

A fresh account02/B06 result pays the special case in which the two random anchor coefficients are functions of disjoint product banks. The first missing implication is the genuinely shared-background case: after the two physical anchor variables are removed, their linear coefficient forms may depend on the SAME remaining original coordinates. Their negative moments cannot then be factorized.

This run proves a weighted joint-density replacement. It never takes the supremum of the singular conditional bound `1/sqrt(|WZ|)`; it integrates that singularity against the genuine two-dimensional coefficient law before inversion.

Consumed corrections include: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projection-density caps are false; post-rotation independence is false; unrestricted fiber suprema lose dimension; aggregate determinant mass does not force one uniformly good physical minor; and a small nonzero tail may not be silently discarded.

## 2. Source-valid inputs

### 2.1 Previous B06 anchor currency

`QFORM-TWO-HUB-ANCHOR-CURRENCY-v1` and
`QFORM-ANCHOR-SCHUR-COFACTOR-IDENTITY-v1`:

`yspennstate/math-open-problems@36cc5730f42c76c15fdc330dc4b47beec060b8fd`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T061939Z-account03-B06-qform-r28/REPORT.md`.

These give (1.1)-(1.2) without selecting one local `2x2` minor.

### 2.2 Weighted affine-fiber projection theorem

Account02/B06 proved `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a `k`-dimensional orthonormal projection of an original product vector with cap-one coordinates, its joint density is at most `exp(k/2)`. In particular, a scalar unit projection has density cap `sqrt(e)` and a two-dimensional orthonormal projection has joint density cap `e`.

### 2.3 Fresh complementary B06 result

Account02/B06, at

`yspennstate/math-open-problems@efbbfe33c64d3a5cbdaf1085d9b5df37bd87feaf`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T065430Z-3f494f528ca7/REPORT.md`,

proved the disjoint-coefficient theorem

`||p_(2XW+2YZ+R)||_infinity <=4 sqrt(L_W L_Z)`

when `W` and `Z` are functions of independent background banks. It explicitly leaves the shared-background case unpaid. The theorem below removes that factorization assumption at the price of a joint-density term.

### 2.4 Completed account04 dependence-safe square theorem

The exact designated partner `account04/B06` still has no completed current-QFORM canonical artifact in the repository at this run's source check. I therefore do not fabricate one. The compatible completed account04 result actually used below is account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

If a base variable has density cap `M`, and the translated original-coordinate square variable has conditional density cap one, then for `a!=0`

`||p_(R+aV_R^2)||_infinity <=2 sqrt(M/|a|)`.                       (2.1)

No independence between `R` and `V_R` is required.

## 3. Joint negative half-moment lemma

The analytic core is an elementary two-dimensional weighted estimate.

### Lemma 3.1 — `QFORM-JOINT-COEFFICIENT-NEGATIVE-HALF-MOMENT-v1`

Let `(W,Z)` have an absolutely continuous probability law. Assume

`||p_W||_infinity <= L_W`,
`||p_Z||_infinity <= L_Z`,
`||p_(W,Z)||_infinity <= H`,                                      (3.1)

where `L_W,L_Z,H` are finite and positive. Then

`boxed:
 E |WZ|^(-1/2)
 <=4 sqrt(3) sqrt(L_W L_Z + H).
`                                                                        (3.2)

No independence between `W` and `Z` is assumed.

#### Proof

Normalize

`U=L_W W`, `V=L_Z Z`.                                             (3.3)

Their marginal densities are at most one and their joint density `q` is at most

`m=H/(L_W L_Z)`.                                                  (3.4)

Set `S=|UV|`. Fix `R>0`. For `t<R/(2m)`, split the event `{S<=t}` according to `|U|<=R`. Since `q<=m` and `p_U<=1`,

`P(S<=t, |U|<=R)
 <= integral_(|u|<=R) min(1,2mt/|u|) du
 =4mt[1+log(R/(2mt))].`                                         (3.5)

On `|U|>R`, the event `|UV|<=t` implies `|V|<=t/R`; the marginal cap of `V` gives

`P(S<=t, |U|>R) <=2t/R`.                                        (3.6)

Write `R=k/m`, so

`t_0=R/(2m)=k/(2m^2)`.                                          (3.7)

For `0<t<t_0`, (3.5)-(3.6) become

`P(S<=t)
 <=m t [4+4log(t_0/t)+2/k].`                                    (3.8)

For `t>=t_0` use the trivial bound one. By the layer-cake formula,

`E S^(-1/2)
 =(1/2) integral_0^infinity t^(-3/2) P(S<=t) dt.`                (3.9)

The two elementary integrals are

`integral_0^(t_0) t^(-1/2) dt=2 sqrt(t_0)`,
`integral_0^(t_0) t^(-1/2) log(t_0/t) dt=4 sqrt(t_0)`.           (3.10)

Hence

`E S^(-1/2)
 <= sqrt(k/2)(12+2/k) + m sqrt(2/k)
 = 6sqrt(2)sqrt(k) + sqrt(2)(1+m)/sqrt(k).`                      (3.11)

Optimize at `k=(1+m)/6`. This gives

`E S^(-1/2) <=4 sqrt(3(1+m)).`                                  (3.12)

Undoing (3.3),

`E|WZ|^(-1/2)
 <=sqrt(L_WL_Z) 4sqrt(3(1+H/(L_WL_Z)))
 =4sqrt(3) sqrt(L_WL_Z+H).`

This proves (3.2). QED.

The important point is that the singularity is integrated against the complete joint law. The proof does not replace it by `sup 1/sqrt(|WZ|)`, which is infinite.

## 4. Shared-background double-star receiver

### Theorem 4.1 — `QFORM-SHARED-COEFFICIENT-DOUBLESTAR-v1`

Let `X,Y` be independent real random variables with densities bounded by one. Let `Omega` be independent of `(X,Y)`. Let `W=W(Omega)`, `Z=Z(Omega)`, and `R=R(Omega)` be arbitrary measurable real variables. Assume `(W,Z)` obeys (3.1). Then

`T=2XW+2YZ+R`                                                     (4.1)

has a continuous density vanishing at infinity, with

`boxed:
 ||p_T||_infinity
 <=2 sqrt(3) sqrt(L_W L_Z + H).
`                                                                        (4.2)

#### Proof

Condition on `Omega=omega`; write `w=W(omega)`, `z=Z(omega)`, and absorb `R(omega)` as a translation. Since `X` and `Y` are still independent, the densities of `2wX` and `2zY` have `L^2` norms at most

`(2|w|)^(-1/2)`, `(2|z|)^(-1/2)`,                                  (4.3)

because `int f_X^2<=1` and `int f_Y^2<=1`. Young/Cauchy-Schwarz gives

`||p_(T|Omega=omega)||_infinity
 <=1/[2sqrt(|wz|)]`.                                                (4.4)

The joint absolute continuity of `(W,Z)` makes `wz=0` a null event. Averaging (4.4) and applying Lemma 3.1 yields

`||p_T||_infinity
 <=(1/2)E|WZ|^(-1/2)
 <=2sqrt(3)sqrt(L_WL_Z+H).`                                        (4.5)

For almost every `omega`, the convolution of the two `L^2` densities in (4.3) is a continuous `C_0` function. The right side of (4.4) is integrable by Lemma 3.1. Dominated convergence therefore shows that the averaged density is continuous and vanishes at infinity. QED.

This strictly changes the mechanism from the fresh disjoint-bank theorem: `W` and `Z` may now share all background coordinates and may be arbitrarily dependent. The only new currency is their genuine two-dimensional density cap.

## 5. Original-product linear coefficients

Let `Omega=(Omega_1,...,Omega_m)` have independent cap-one coordinates and let

`W=alpha.Omega+w_0`,
`Z=beta.Omega+z_0`,                                                (5.1)

where `alpha,beta` are nonzero and linearly independent. Put

`kappa=sqrt(||alpha||^2||beta||^2-(alpha.beta)^2)`,
`sin(theta)=kappa/(||alpha||||beta||)`.                            (5.2)

The weighted affine-fiber theorem gives

`L_W <=sqrt(e)/||alpha||`,
`L_Z <=sqrt(e)/||beta||`,
`H <=e/kappa`.                                                     (5.3)

Indeed `(W,Z)` is an invertible linear image, with determinant `kappa`, of the two-dimensional orthonormal projection onto `span{alpha,beta}`, whose density cap is `e`.

Substituting (5.3) in (4.2) gives the explicit product-law corollary

`boxed:
 ||p_T||_infinity
 <= [2sqrt(3e)/sqrt(||alpha||||beta||)]
    sqrt(1+1/sin(theta)).
`                                                                        (5.4)

No physical entry or local determinant is inverted. The two entire coefficient vectors are paid first.

## 6. Application to the live r28 zero-anchor hub

Return to the zero-cross anchor from Section 1. Let the two physical anchor variables be `X,Y`, and put every other original coordinate into `Omega`. The complete quadratic form in those two anchors can be written exactly as

`Q=2X W(Omega)+2Y Z(Omega)+R(Omega)`,                              (6.1)

because the anchor cross coefficient is zero. Same-side self-block couplings and cross-bank leaf couplings are all retained in the linear forms `W,Z`; every term not involving `X` or `Y` stays in the arbitrary quadratic remainder `R`.

Let `alpha,beta` be the full coefficient vectors of `W,Z` on `Omega`. The opposite-bank components of these vectors are exactly the r28 star vectors `r,c` on disjoint coordinate subsets. Therefore

`||alpha||>=||r||`, `||beta||>=||c||`,                              (6.2)

and (1.2) gives

`||alpha||||beta||
 >sqrt(127/800) G^2.`                                               (6.3)

Define the physical coefficient angle by

`sin(theta)=sqrt(||alpha||^2||beta||^2-(alpha.beta)^2)
             /(||alpha||||beta||).`                                (6.4)

### The transverse shared-coefficient exit

If

`sin(theta)>=eta>0`,                                                (6.5)

then (5.4) and (6.3) give

`boxed:
 ||p_Q||_infinity
 <
 [2sqrt(3e) sqrt(1+eta^(-1))/(127/800)^(1/4)] G^(-1).
`                                                                        (6.6)

At the concrete collar `eta=1/4`,

`boxed:
 ||p_Q||_infinity <20.233/G.
`                                                                        (6.7)

The density is continuous on this subbranch.

This closes a genuinely shared-background version of the diffuse double-star packet. It includes arbitrary same-side anchor couplings; account02/B06's factorization hypothesis is no longer needed.

### Failure is an explicit near-collinear tube

If (6.5) fails, set

`lambda=(alpha.beta)/||alpha||^2`,
`epsilon=beta-lambda alpha`.                                      (6.8)

Then

`epsilon perpendicular alpha`,
`||epsilon||=||beta|| sin(theta)<eta ||beta||`.                    (6.9)

Thus at `eta=1/4` the only unclosed zero-anchor shared-coefficient state has the two complete physical coefficient forms within relative angle `arcsin(1/4)` of a rank-one coefficient line. The residual `epsilon` is NOT discarded; fragmented cap-one inputs make such perturbative deletion invalid without a separate stability theorem.

This is a sharper obstruction than “the coefficients share coordinates.” The remaining branch is now an explicit near-collinear coefficient tube carrying the same aggregate determinant currency (1.1).

## 7. Actual account04 square-smoothing splice

In the already-existing outer-square chamber in which the zero-anchor packet above is the residual variable `R_0` and a genuine original-coordinate scalar pivot supplies

`Q_final=R_0+a V_(R_0)^2`, `a!=0`,                                (7.1)

with the conditional density cap-one property required by account04/B18, equation (6.7) gives

`M=||p_(R_0)||_infinity <20.233/G`.                                (7.2)

Apply the completed account04/B18 theorem (2.1) at this actual inequality:

`||p_(Q_final)||_infinity
 <=2sqrt(M/|a|)
 < 8.997/sqrt(|a|G).`                                              (7.3)

No independence between `R_0` and the translated square is manufactured. Equation (7.3) is an essential-density conclusion; account04/B18 does not by itself upgrade the final density to a continuous representative.

The exact designated partner `account04/B06` remained without a completed current-QFORM canonical report at the source check, so no result is attributed to it.

## 8. What is new and the first unpaid implication

This run advances the curved-fiber branch in three ways.

1. It proves a joint negative-half-moment estimate using **both marginal and joint density caps**, avoiding the infinite worst-fiber supremum.
2. It converts that lemma into a continuous-density receiver for `2XW+2YZ+R` in which the two random coefficients may be arbitrarily dependent because they share the entire background product vector.
3. It applies the receiver to the live r28 zero-anchor aggregate hub. Quantitative transversality of the two full coefficient forms pays the branch by `<20.233/G`; failure forces a concrete near-collinear coefficient tube rather than an unstructured shared-dependence obstruction.

The first unpaid implication is now

`QFORM-ZERO-ANCHOR-NEAR-COLLINEAR-THIRD-DIRECTION-v1`:

> In the live zero-anchor state satisfying (1.1) and (6.9), retain the nonzero residual coefficient vector `epsilon`, all same-bank quadratic curvature and all complementary spectrum, and consume the third large spectral direction before paying the hyperbolic singularity. Prove either a product-preserving stability extension of Theorem 4.1 that is uniform as `sin(theta)->0`, or route the near-collinear packet into an already-paid rank-three ruled / aggregate-volume / ridge exit.

The fresh rank-two resonant example from account02/B06 shows why simply deleting the third direction cannot work: two opposite-sign completed squares can retain a logarithmic singularity.

## 9. Status

* `QFORM-JOINT-COEFFICIENT-NEGATIVE-HALF-MOMENT-v1`: proved.
* `QFORM-SHARED-COEFFICIENT-DOUBLESTAR-v1`: proved.
* r28 zero-anchor, shared-background, `sin(theta)>=1/4`: paid by `<20.233/G`, continuous density.
* Existing outer-square splice of that branch: essential bound `<8.997/sqrt(|a|G)`.
* Near-collinear coefficient tube: unresolved.
* Full universal QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Universal continuity conclusion: **OPEN**.

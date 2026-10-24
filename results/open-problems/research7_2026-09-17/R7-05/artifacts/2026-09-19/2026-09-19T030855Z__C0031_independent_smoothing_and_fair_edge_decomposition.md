# C0031 — independent finite-variance smoothing closes the hard edge for a no-density subclass; exact fair edge decomposition for discrete Pareto

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Canonical target: `C0031`, Bordenave–Chafaï heavy-tailed circular-law almost-sure upgrade  
Methods: **B24 / B18 / B27**  
Initial run snapshot: `5453f7fc0702ae816c3d6c3712318209ee86b741`  
Fresh pre-write master: `78380d46fc2f9ef308d4b322570e7ba1e45a09c1`

## 1. Cumulative starting point

The frozen source metric is `BC_AS`, equal to 1 only when the full Bordenave–Chafaï no-density almost-sure endpoint is proved, and 0 otherwise. It enters this run at 0.

The preceding R7-05 run reduced the symmetric discrete-Pareto benchmark to a random-normal arithmetic statement after extracting unit-amplitude signs. Its exact endpoint was a stretched-exponential floor for

`A_n(z)=a_n^{-1}X_n-zI`,

because all logarithmic mass above `exp(-n^q)` is already controlled almost surely by earlier C0031 work. The previous conditional bridge showed that a polynomial LCD lower bound for a thinned random normal would imply this floor.

This run changes the viewpoint. Instead of continuing to push the random-normal LCD directly, it asks what class of heavy-tailed atoms makes the hard edge a standard smoothed-analysis problem after conditioning. This produces one complete subclass theorem and then an exact decomposition showing why the discrete-Pareto benchmark is close to, but not automatically inside, that class.

## 2. B24 — extremal object: isolate the independent-smoothing case and prove it completely

Let `0<alpha<2`. Suppose the heavy-tailed atom has a decomposition

`xi = H + sigma Z`,

where

1. `H` is in the same alpha-stable domain of attraction required by the Bordenave–Chafaï heavy-tail theorem;
2. `Z` is independent of `H`, centered, non-degenerate, and has finite positive variance;
3. `sigma>0` is fixed.

After rescaling `Z`, assume `E|Z|^2=1`. The sum `H+sigma Z` has the same alpha-stable tail domain because a finite-second-moment variable is negligible relative to an alpha-stable tail when `alpha<2`.

The important point is that this class can remain purely atomic. For example, take `H` to be an integer-valued symmetric Pareto-type variable and `Z` an independent Rademacher sign. Then `xi` is discrete and has no bounded density.

### Theorem 1 (polynomial hard-edge floor under independent finite-variance smoothing)

Let `X_n=(xi_ij)_{i,j<=n}` be the nested iid matrix with `xi=H+sigma Z` as above, and let `a_n` be the heavy-tail normalization. Fix a bounded Borel set `K subset C`. Then there exists `B<infinity` such that, almost surely, for Lebesgue-a.e. `z in K`,

` s_min(a_n^{-1}X_n-zI) >= n^{-B}`

for all sufficiently large `n` (the exceptional starting index may depend on `z`). Consequently, for every fixed `q>0`,

` s_min(a_n^{-1}X_n-zI) >= exp(-n^q)`

for all sufficiently large `n`, almost surely for Lebesgue-a.e. `z`.

#### Proof

Write `H_n=(H_ij)` and `Z_n=(Z_ij)`. Then

`X_n-a_n zI = sigma [ Z_n + B_n(z) ]`,

where

`B_n(z)=sigma^{-1}(H_n-a_n zI)`.

We first show that the random deterministic core has polynomial norm almost surely. Stable-domain regular variation implies a tail bound of the form

`P(|H|>t) <= t^{-alpha+o(1)}`.

Choose `C>3/alpha`. Then

`P(max_{i,j<=n}|H_ij|>n^C)
 <= n^2 P(|H|>n^C)
 <= n^{2-alpha C+o(1)}`,

which is summable. Borel–Cantelli therefore gives

`max_{i,j<=n}|H_ij| <= n^C`

eventually almost surely. Hence

`||H_n|| <= n max_{i,j<=n}|H_ij| <= n^{C+1}`

eventually. Also `a_n` is regularly varying with exponent `1/alpha`, so for every fixed `epsilon>0`,

`a_n <= n^{1/alpha+epsilon}`

eventually. Thus for every bounded `K` there is a deterministic exponent `gamma` such that, almost surely eventually,

`sup_{z in K} ||B_n(z)|| <= n^gamma`.                                      (2.1)

Now condition on the entire heavy core `(H_ij)`. Tao–Vu's shifted-iid invertibility theorem, quoted as Theorem 1.8 in Cook, *Lower bounds for the smallest singular value of structured random matrices* (Ann. Probab. 46 (2018), arXiv:1608.07347v5), states: for an iid centered unit-variance noise matrix and every desired polynomial failure exponent `R>0`, there is `beta=beta(R,gamma)` such that uniformly over every deterministic complex perturbation `B` satisfying `||B||<=n^gamma`,

`P_Z( s_min(Z_n+B) <= n^{-beta} ) <= C_{R,gamma} n^{-R}`.                    (2.2)

Take `R>2`. On the almost-sure event where (2.1) holds, (2.2) applies for every fixed `z in K` and all large `n`.

To obtain the single-event, Lebesgue-a.e.-`z` statement needed by Hermitization, do not discretize `z`. Instead integrate the conditional failure indicators. For large `n`,

`E_Z[ integral_K 1_{s_min(Z_n+B_n(z))<=n^{-beta}} dz | H ]
 <= |K| C n^{-R}`.

Summing in `n` and using Tonelli gives finite conditional expectation. Therefore, for almost every realization of the noise matrix and for Lebesgue-a.e. `z in K`, only finitely many failures occur. Unconditioning preserves this probability-one statement.

Finally,

`s_min(a_n^{-1}X_n-zI)
 = (sigma/a_n) s_min(Z_n+B_n(z))
 >= sigma a_n^{-1} n^{-beta}
 >= n^{-B}`

for some finite `B`, after increasing `B` to absorb the slowly varying factor in `a_n`. Since every inverse polynomial eventually dominates `exp(-n^q)`, the second assertion follows. QED.

### Corollary 2 (source-level a.s. convergence for the independent-smoothing subclass)

Under the full Bordenave–Chafaï heavy-tail hypotheses plus the decomposition `xi=H+sigma Z` above, the empirical eigenvalue measure converges almost surely to the same heavy-tailed limiting law `mu_alpha`.

#### Reason

The cumulative C0031 work has already reduced the missing no-density a.s. endpoint to lower-log uniform integrability and, more sharply, to the ultra-hard-edge defect below `exp(-n^q)`. All singular-value mass above that scale is already controlled almost surely; the source supplies the remaining Hermitization and shifted-singular-measure convergence inputs. Theorem 1 removes the ultra-hard edge completely for Lebesgue-a.e. shift on one probability-one event. Therefore the existing Hermitization argument closes for this subclass.

This is a restricted theorem and does **not** move `BC_AS`, because a general stable-domain atom need not admit a non-trivial independent convolution factor.

## 3. B18 — another language: exact fair Bernoulli edge-flow decomposition of the discrete-Pareto benchmark

Return to the symmetric discrete-Pareto benchmark from STUCK1:

`P(xi=k)=P(xi=-k)=p_k`,

with

`p_k=c_alpha k^{-1-alpha}` and `c_alpha=(2 zeta(1+alpha))^{-1}`.

The previous run extracted only the unit-magnitude coordinates of a tested column. Here there is an exact stronger decomposition that keeps a fair sign in **every** entry while keeping its amplitude uniformly bounded.

### Lemma 3 (fair edge-flow decomposition)

There exist random variables `(Y,A,epsilon)` such that

`xi = Y + A epsilon`,

where `epsilon` is a fair Rademacher sign independent of `(Y,A)`, and

`A in {1/2,1}`.

Equivalently,

`2 xi = Z + K epsilon`,

where `Z=2Y` is integer-valued and `K in {1,2}`.

#### Proof

Consider the graph on the support `Z\{0}` with one central edge `{-1,+1}` and the ordinary adjacent edges

`{k,k+1}` and `{-k,-(k+1)}`, `k>=1`.

For `k>=1`, define

`w_k = 2 sum_{j=k+1}^infinity (-1)^{j-k-1} p_j
     = 2(p_{k+1}-p_{k+2}+p_{k+3}-...)`.

Because `p_j` is strictly decreasing to zero, the alternating-series theorem gives `w_k>0`. Moreover

`w_{k-1}+w_k=2p_k`, `k>=2`.

Define the central-edge weight

`w_0=2p_1-w_1`.

Since `w_1<2p_2<2p_1`, we also have `w_0>0`. Thus at every vertex `+/- k`, the sum of incident edge weights equals `2p_k`.

The sum of all edge weights is 1: summing weighted degrees over all vertices gives

`sum_vertices degree_weight = sum_{k>=1} 2 vertices * 2p_k = 2`,

and every edge is counted twice.

Now sample an edge with probability equal to its weight and, independently, choose one of its two endpoints with a fair sign. The probability of landing at vertex `+/- k` is one half of its incident edge-weight sum, namely `p_k`, so the resulting endpoint has exactly the law of `xi`.

For an ordinary adjacent edge, write its two endpoints as `Y +/- 1/2`; for the central edge write them as `0 +/- 1`. The endpoint selection is the independent Rademacher `epsilon`. Hence `A in {1/2,1}` and the claimed representation follows. QED.

### What the decomposition buys

For the iid matrix, conditional on all latent edges,

`2(X_n-a_n zI)=D_n(z)+K_n circ E_n`,                                  (3.1)

where

- `E_n` has iid fair Rademacher entries;
- `K_n` is a deterministic conditional profile with entries in `{1,2}`;
- `D_n(z)=Z_n-2a_n zI` is the conditional deterministic core.

The latent edge has the same Pareto-order tail as the endpoint. If we truncate **latent edges** rather than the output `xi`, then conditioning preserves independence of all Rademacher signs. Choosing `C>3/alpha`, the event that every latent midpoint in the `n x n` block has size at most `n^C` fails only summably often. On that event, `D_n(z)` has polynomial norm for bounded `z`.

Thus the discrete-Pareto benchmark has been reduced to a bounded-profile smoothed-analysis problem:

> For every deterministic complex core `D_n` of polynomial operator norm and every deterministic profile `K_ij in {1,2}`, obtain a summable polynomial lower-tail estimate for `s_min(D_n+K circ E_n)`.

This is substantially narrower than the previous heavy-tailed random-normal theorem: the noise is now bounded, centered and fair in every coordinate.

## 4. The exact existing-theorem boundary

Two neighboring published results explain why (3.1) is close but not yet automatic.

1. Tao–Vu's shifted-iid theorem (Cook's Theorem 1.8) allows an arbitrary complex deterministic core of polynomial norm and gives arbitrarily high polynomial confidence, but its random perturbation is iid. It applies immediately when the amplitude profile is constant.

2. Cook's Theorem 1.26 treats a non-identical standard-deviation profile `A` with arbitrary polynomial-size mean profile `B`, provided the profile is super-regular. Our profile `K/2 in {1/2,1}` is maximally dense and hence super-regular. However the theorem's displayed error term is only

`O(sqrt(log n/n))`,

on the polynomial hard-edge event (with an operator-norm restriction). This is exactly the non-summable scale already encountered in the Bordenave–Chafaï source obstruction, so Theorem 1.26 alone does not provide the required full-sequence Borel–Cantelli conclusion.

Cook explicitly notes that stronger Littlewood–Offord tools should improve this probability bound but are not pursued there. This makes the remaining discrete-Pareto benchmark gap unusually concrete: upgrade the dense bounded-profile Bernoulli perturbation from Cook's `sqrt(log n/n)` confidence to summable confidence at any polynomial or stretched-exponential hard-edge scale.

This comparison also shows why the independent-smoothing theorem above succeeds: conditioning leaves an **iid** finite-variance perturbation, so Tao–Vu's arbitrarily high polynomial-confidence shifted theorem applies directly.

## 5. B27 — swap quantifiers: use a.e. shift by Fubini, not uniform-in-z discretization

Hermitization does not require a uniform statement over every complex shift; it requires the lower-log control for Lebesgue-a.e. `z` on one probability-one matrix event. The proof of Theorem 1 uses this quantifier structure exactly.

This matters because a lattice-grid approximation to `a_n z` is useless at the hard edge: an `O(1)` error in raw operator norm is enormously larger than a target polynomial least-singular value, so Weyl perturbation cannot transfer an integer-shift estimate to a generic `z`.

By contrast, a smoothed-analysis estimate uniform over deterministic cores can be integrated in `z`, and Tonelli plus Borel–Cantelli produces the required one-event/a.e.-`z` conclusion without a continuum union bound.

For the discrete-Pareto edge decomposition, the same Fubini step would complete the hard edge as soon as the bounded-profile Bernoulli perturbation theorem has a summable failure bound. Thus the remaining obstacle is not the continuum of complex shifts; it is the confidence exponent for the bounded non-iid amplitude profile.

## 6. Source and prior-art check, 2026-09-19

- Bordenave–Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, Theorem 6.2: general heavy-tail convergence in probability; bounded density gives a.s. convergence; the text explicitly says the authors believe the a.s. upgrade should hold generally but their small-singular-value control is too slow.
- Tao–Vu, shifted iid invertibility theorem, quoted as Cook Theorem 1.8: arbitrary deterministic complex perturbation of polynomial norm, iid centered unit-variance noise, arbitrarily high polynomial-confidence hard-edge bound.
- Nicholas Cook, *Lower bounds for the smallest singular value of structured random matrices*, Ann. Probab. 46 (2018), arXiv:1608.07347v5. Theorem 1.26 handles a super-regular variance profile with arbitrary polynomial-size mean profile but has a `sqrt(log n/n)` term; Remark 1.16 says stronger Littlewood–Offord tools may improve that probability bound.
- Aizenman–Germinet–Klein–Warzel, *On Bernoulli Decompositions for Random Variables, Concentration Bounds, and Spectral Localization* (PTRF 143 (2009), arXiv:0707.0095), gives a general Bernoulli decomposition with state-dependent amplitude. Lemma 3 above is more specialized: for this discrete-Pareto benchmark it produces a fair sign at every coordinate with amplitude only `1/2` or `1`. No novelty claim is made without a targeted prior-art search for this exact edge-flow representation.

A bounded fresh search did not expose a theorem settling the full Bordenave–Chafaï no-density a.s. endpoint. This is negative evidence only, not an openness or novelty certificate.

## 7. Metric and status

Frozen metric: `BC_AS`.

Before: `0`.

After: `0` (**NO MOVEMENT**).

Mathematical status: **PARTIAL / SOURCE OPEN**.

New complete results in this run:

1. a full polynomial hard-edge theorem for every heavy stable-domain law carrying an independent finite-variance iid smoothing component, valid for Lebesgue-a.e. complex shift on one probability-one event;
2. consequently, the full Bordenave–Chafaï almost-sure ESD conclusion for that no-density convolution subclass;
3. an exact fair Bernoulli edge-flow decomposition of the symmetric discrete-Pareto benchmark with bounded amplitude set `{1/2,1}`;
4. a precise residual theorem: obtain summable hard-edge confidence for dense bounded Bernoulli amplitude profiles under arbitrary polynomial deterministic complex perturbations.

The source-wide metric stays 0 because arbitrary stable-domain atoms need not possess an independent convolution factor, and Cook's existing bounded-profile theorem does not supply summable confidence.

Next recommended nonrepeating Section-B triple: **B4 / B20 / B28**.

- **B4:** prove the weaker bounded-profile smoothed theorem first for real cores or for a typical iid `{1,2}` profile, completely.
- **B20:** inspect exactly where Tao–Vu's arbitrary-high-confidence shifted-iid proof fails when the deterministic coefficient profile varies in `[1,2]`; isolate the one inverse-Littlewood–Offord step that needs replacement.
- **B28:** replace worst-case deterministic profiles by the typical latent profile generated by Lemma 3 if this yields exponentially good expansion/arithmetic regularity.

No P26 or distinct OTHER-track audit is claimed.
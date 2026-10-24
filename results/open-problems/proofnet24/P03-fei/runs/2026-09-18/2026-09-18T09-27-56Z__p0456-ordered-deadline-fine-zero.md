Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — ordered deadlines collapse the fixed-coefficient fine window

**MOVEMENT.** The saturated source-scale metric stays `c_LK^cert=0`, while the admitted finer fleet proof-frontier metric moves

`a_LK^fine: sqrt(11) -> 0`.

The fine metric reaches its theoretical minimum. Its unchanged count therefore remains `0`, and HARD recoveries remain `0/2`. I do **not** use either saturated metric to manufacture a stuck episode.

Main new claim:

`P03-P0456-ORDERED-DEADLINE-FINE-WINDOW-ZERO-282 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

Let

`W_n = sqrt(log n log log n)`.

For every fixed real `a<0`, if

`k <= log n + a W_n`,

then `LK(n,k)` is disconnected with high probability. For every fixed `a>0`, if

`k >= log n + a W_n`,

then `LK(n,k)` is connected with high probability. Thus the fixed-coefficient proof frontier on the `W_n` scale is now exactly zero on both sides. This **does not decide `a=0`**, does not determine the `o(W_n)` transition window, and proves no limiting connectivity law. The parent source therefore remains OPEN/PARTIAL rather than closed.

The three Section-B moves used substantively are **B25 COUNT THE SAME THING TWICE, B5 ADD A PARAMETER AND DIFFERENTIATE IN IT, B24 FIND THE EXTREMAL OBJECT**.

---

## 1. Continuity, source, and current status

The canonical exclusive assignment remains `operations/claims/P0456.md` (creation `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`). I continued from

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T08-29-28Z__p0456-joint-race-fine-bracket.md`

(creation `dff6cae26960421bb4cf651991c1e50373823ea3`, blob `8b42bf7f49ca2f9395ae04cea7eeea61b06a0d05`) and preserve Claims 274, 276, 278, and 280.

Repository continuity recovered/reread this invocation included the root README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the current P0456 claim and newest P03 report, and the newest visible neighboring P0457 state. Large root surfaces are connector-truncated and are therefore **not** represented as byte-for-byte rereads; exact-path reads and targeted current searches were used. The newest P0457 work is a distinct diameter package, not this connectivity-window target, so there is no duplication.

The outside source was freshly rechecked on 2026-09-18:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, Section 1.1.

The source still states that connectivity is not known throughout the displayed band

`log n - (1/2) sqrt(log n) log log n <= k <= log n + (1/2) sqrt(log n) log log n`

and explicitly points to its simpler sufficient conditions as the reason for the gap. I reread the literal bad-pair definition and Lemmas 10--14, including the uniform type interleaving in Lemma 11 and conditional independence on `B^c` in Lemma 13, and the fixed-low-degree proof in Theorem 4 / Corollary 1. A fresh bounded search for the exact title/authors/DOI and later 2026 bilateral-preference connectivity work recovered the Cambridge primary source and no later source-matching closure. That is dated bounded negative evidence only, **not** proof of worldwide openness or publication novelty.

The source-scale metric `c_LK^cert=0` remains saturated from Claim 276. Claim 280 had formally admitted

`a_LK^fine=max(a_-,a_+)`

at scale `W_n`, lower better, with baseline `sqrt(23)` from Claim 278 and newest value `sqrt(11)`. The theorem below moves this admitted metric to `0`.

---

## 2. Idea before calculation: keep every deadline instead of the last one

Claim 280's common-deadline Gamma race deliberately replaced all individual type-0 deadlines by the last relevant deadline. It proved a correction constant `1` but also showed that no further estimate on that **same relaxed event** could beat `1`.

I attacked that obstruction rather than sharpen the same integral.

In the literal source permutation, the first `s` type-0 objects are the edges `(1,i)` to the first `s` preferred neighbors of vertex `1`. If neighbor `i` rejects `1`, then its own nonzero type must accumulate many arrivals **before its own type-0 object**, not merely before the `s`th type-0 object. These deadlines are ordered and different.

B25 counts that event in two exactly equivalent ways:

1. as the source finite type-word interleaving with an ordered type-0 spine; and
2. after an iid-word approximation on the polylogarithmic relevant prefix, as independent rate-one Poisson processes racing against the successive arrival times of a distinguished type-0 process.

B24 then identifies the extremal way to omit a fixed number of rejection constraints: because later deadlines are easier, the event is most likely when the omitted constraints are the **earliest** deadlines.

Finally B5 introduces

`s = c sqrt(k/log k)`

with arbitrary fixed `c>0`. The ordered-deadline rate has leading correction `1/(2c)`, rather than the common-deadline `c/2+1/(2c)`. The missing `c/2` term is exactly the entropy saved by keeping all deadlines. Since `c` may be chosen as any fixed constant after the fixed window coefficient `a` is given, this drives the `W_n`-scale proof frontier to zero.

---

## 3. Ordered-deadline race lemma

The next lemma is the core new estimate.

### Lemma 282A (ordered-deadline race)

Fix constants `c>0` and integer `h>=0`. Let `K -> infinity`,

`s = floor(c sqrt(K/log K)) + O(1)`,

and `r=s-h`.

Consider an iid type word with one distinguished type `0` and at least `r` other types, all with equal probabilities. Let `T_d` denote the continuous-time arrival time of the `d`th type-0 event in the equivalent independent rate-one Poisson race, and let a required nonzero type succeed at deadline `d` when it has at least `K` arrivals before `T_d`. If at most `h` of the first `s` deadlines may be omitted, then the probability of simultaneous success of the remaining `r` types is at most

`exp[-K + (1/(2c)+o(1)) sqrt(K log K)]`.

The same estimate, with the same leading constant, holds for the source finite without-replacement type interleavings when every relevant type population is `n+O(s)`, `K=O(log n)`, and only `O(s)` items per list have been deleted.

### Proof: B24 extremal deadline set

Let

`F_K(t)=P(Pois(t)>=K)=P(G_K<=t)`,

where `G_K` is Gamma(shape `K`, rate `1`). Conditional on the type-0 Poisson process, different required nonzero processes are independent, so for a deadline set `D` the success probability is

`E prod_{d in D} F_K(T_d)`.

Both `T_d` and `F_K(T_d)` increase with `d`. Therefore among all `r=s-h` subsets of `{1,...,s}`, the product is pointwise maximized by omitting the earliest `h` deadlines. Hence every allowed deadline set is bounded by

`J_{K,s,h}:=E prod_{d=h+1}^s F_K(T_d)`.

This proves the extremal-object step; no rearrangement inequality with a hidden sign is being used.

### Proof: exact integral representation

The joint density of the first `s` arrival times of a rate-one Poisson process is

`e^{-t_s} 1_{0<t_1<...<t_s}`.

Integrating out `t_1,...,t_h`, and then bounding `t_{h+1}^h <= t_s^h`, gives

`J_{K,s,h}`
` <= 1/[h!(r-1)!] int_0^infty e^{-T} T^h F_K(T) A_K(T)^{r-1} dT`,

where

`A_K(T):=int_0^T F_K(u)du = E[(T-G_K)_+]`.

Since `d(A_K(T)^r)=r F_K(T) A_K(T)^{r-1}dT`, integration by parts shows, for a constant `C_h` depending only on `h`,

`J_{K,s,h}`
` <= C_h/r! int_0^infty e^{-T}(1+T^h) A_K(T)^r dT`.        (1)

All polynomial factors below contribute only `O_h(log K)=o(sqrt(K log K))` to the logarithm.

### Proof: the region `T>=K`

For `T=K+x`, `x>=0`,

`A_K(T)=E[(K+x-G_K)_+] <= x + E|G_K-K| <= x+sqrt(K)`

because `Var(G_K)=K`. Thus, suppressing a fixed polynomial factor,

`1/r! int_K^infty e^{-T} A_K(T)^r dT`
` <= e^{-K}/r! int_0^infty e^{-x}(x+sqrt K)^r dx`
` = e^{-K} sum_{m=0}^r (sqrt K)^m/m!`
` <= exp[-K+sqrt K]`.

Hence this entire region contributes

`exp[-K+o(sqrt(K log K))]`.                                  (2)

### Proof: the strip `K-sqrt K <= T <= K`

Here monotonicity gives

`A_K(T)<=A_K(K)=E[(K-G_K)_+]<=sqrt K`.

Consequently (1), Stirling's formula, and the length `sqrt K` of the strip give logarithm at most

`-K+sqrt K + (r/2)log K - log(r!) + O_h(log K)`
`= -K + O(r log log K) + O(sqrt K)`
`= -K + o(sqrt(K log K))`,                                  (3)

because `r=Theta(sqrt(K/log K))`.

### Proof: the lower moderate-deviation region

Write `T=K-z` with `sqrt K <= z <= K/2`. The Poisson point mass

`p_K(T)=e^{-T}T^K/K!`

obeys

`F_K(T) <= [(K+1)/(K+1-T)] p_K(T) <= C(K/z)p_K(T)`.

For `u<=T`,

`d/du log p_K(u)=K/u-1 >= z/T`,

so

`int_0^T p_K(u)du <= (T/z)p_K(T) <= (K/z)p_K(T)`.

Therefore

`A_K(T) <= C K^2 z^{-2} p_K(T)`.

Stirling's formula and

`K log(K/T)-K+T = K[-log(1-z/K)-z/K] >= z^2/(2K)`

give the uniform bound

`A_K(K-z) <= C K^{3/2} z^{-2} exp[-z^2/(2K)]`.              (4)

Insert (4) into (1). Since `z>=sqrt K`,

`r[(3/2)log K-2log z]-log(r!) = O(r log log K)`

uniformly, hence the logarithm of the integrand, including normalization, is at most

`-K + z - r z^2/(2K) + o(sqrt(K log K))`.

The quadratic function in `z` has unrestricted maximum

`K/(2r) = (1/(2c)+o(1)) sqrt(K log K)`.

Integration over an interval of length at most `K` adds only `O(log K)`. For `T<=K/2`, an ordinary Poisson Chernoff bound makes `F_K(T)` exponentially small in `K`; after the `r`th power this region is far smaller than the claimed scale. Combining the lower regions therefore gives

`log J_{K,s,h}`
` <= -K + (1/(2c)+o(1)) sqrt(K log K)`.                    (5)

Together with (2)--(3), (5) proves the iid-race estimate.

### Proof: transfer back to the exact source permutation

The source conditional permutations have type populations `n+O(s)`; their differences are only `O(s)` because the proof deletes the first-`s` neighborhood and a constant number of distinguished edges. Project onto type 0 and the required nonzero types.

Take a deterministic prefix length

`R=6(s+1)K`.

If the `s`th type-0 object has not appeared by this prefix, a hypergeometric lower-tail bound gives probability `exp[-Omega(K)]`; with the factor `6` chosen above the exponent can be taken strictly below `-2K` for all large `K`, which is negligible relative to (5). On the complementary event the full deadline-success event is determined by the first `R` projected labels.

For every projected word of length at most `R`, the exact without-replacement probability divided by the equal-probability iid-word probability is

`exp[O(R^2/n + Rs/n)] = 1+o(1)`,

uniformly, because

`R=O(sK)=polylog(n)`

and `K=O(log n)`. Thus the exact finite source event has the iid probability in (5), up to a multiplicative `1+o(1)` and an exponentially smaller tail. This proves the finite-source version of the lemma. `square`

### Conversion to the source parameter `k`

In both source applications below the nonzero types need

`K=k-s-O(1)`

arrivals. Since

`s=c sqrt(k/log k)=o(sqrt(k log k))`,

(5) becomes

`exp[-k + (1/(2c)+o(1)) sqrt(k log k)]`.                   (6)

The difference between `K` and `k` changes no leading `W_n` coefficient.

---

## 4. Disconnection for every fixed negative `W_n` coefficient

Let `I_v` be the isolation indicator and

`p_n=P(I_v)`.

Claim 278 proved the exact one-vertex lower bound

`p_n >= (1-k/(n-k))^(n-1) = exp[-k-o(1)]`                 (7)

for `k=O(log n)`.

Assume now

`k = log n + a W_n + O(1)`

with a fixed `a<0`; monotonicity then handles all smaller `k`.

The source bad event `B` satisfies, by Lemma 10,

`P(B)=O(k^3/n)`.                                           (8)

On the first bad-side union used by source Lemma 11, isolation of vertex 1 forces, for every one of its first `s` relevant neighbors except possibly the distinguished vertex 2, at least

`K=k-s-2`

items of that neighbor's own type to precede **its own** type-0 deadline. This is exactly Lemma 282A with `h=1`. The symmetric side is identical. Therefore (6), (8), and the source Lemma-12 decomposition give

`P(I_1 I_2 cap B)`
` <= exp[-log n-k+(1/(2c)+o(1))sqrt(k log k)]`.             (9)

Since

`sqrt(k log k)=(1+o(1))W_n`,

(7) and (9) imply

`P(I_1 I_2 cap B)/p_n^2`
` <= exp[(a+1/(2c)+o(1))W_n]`.                              (10)

Choose once and for all a fixed

`c > 1/(2|a|)`.

Then (10) tends to zero.

The marginal bad contribution is even simpler:

`P(I_1 cap B)/p_n <= P(B)/p_n`
` <= exp[(a+o(1))W_n] -> 0`,                                (11)

using (7)--(8). Hence

`P(I_1 | B^c)=p_n(1+o(1))`.

Source Lemma 13 gives exact conditional independence on `B^c`, so

`P(I_1I_2 cap B^c)=P(B^c)P(I_1|B^c)P(I_2|B^c)`
`=p_n^2(1+o(1))`.

Together with (10),

`P(I_1I_2)/p_n^2 <= 1+o(1)`.                               (12)

Finally (7) gives

`n p_n >= exp[-aW_n-o(W_n)] -> infinity`.

The standard second-moment calculation used by the source now yields

`P(no isolated vertex) -> 0`.

Therefore `LK(n,k)` is disconnected whp for every fixed `a<0` at the `W_n` scale. This improves the negative frontier from `1` to `0`.

---

## 5. Low-degree elimination for every fixed positive coefficient

Now let

`k = log n + aW_n + O(1)`

with fixed `a>0`.

Fix an integer `kappa>=0`. Repeat the literal setup of source Theorem 4 with arbitrary

`s=floor(c sqrt(k/log k))`.

If `deg(1)<=kappa`, then among the first `s` preferred neighbors of vertex 1, at least `s-kappa` reject it. For every such rejected neighbor `i`, after deleting the first-`s` neighborhood and vertex 1, at least

`K=k-s-1`

items of type `i` must occur before **its own** type-0 deadline `(1,i)`. There are at most

`sum_{j=0}^kappa binom(s,j)=s^{O_kappa(1)}`

ways to choose the omitted rejection constraints.

For each choice, B24 says the largest ordered-deadline probability occurs when the omitted constraints are the earliest deadlines. Lemma 282A with `h=kappa` then gives

`P(deg(1)<=kappa)`
` <= exp[-k+(1/(2c)+o(1))sqrt(k log k)]`,                  (13)

because the polynomial number of omitted sets contributes only `O_kappa(log k)=o(W_n)`.

A union bound over the `n` vertices gives

`P(exists v: deg(v)<=kappa)`
` <= exp[(-a+1/(2c)+o(1))W_n]`.                            (14)

Choose any fixed

`c > 1/(2a)`.

Then (14) tends to zero. In particular, with `kappa=5`, whp there is no component of size at most `6`.

This strictly supersedes the `sqrt(11)` fixed-low-degree coefficient from Claim 280. It also shows that a direct ad hoc enumeration of components of sizes `2,...,6` is unnecessary: the exact individual-deadline structure removes all of them at once for every fixed positive coefficient.

---

## 6. Components of size at least seven

For completeness, I rederive the retained component estimate rather than invoking connectivity from mean degree.

Use iid Exp(1) scores, with **larger score = higher preference**, which is order-equivalent to the source model. Put

`m=log((n-1)/k)`,

and take the fixed constant

`C=log(32/5)`.

Let `A_n` be the event that at every vertex the kth-largest incident score lies in `[m-C,m+C]`.

At the upper endpoint `m+C`, the number of exceedances has mean `(5/32)k`. The binomial Chernoff exponent for having at least `k` exceedances is

`gamma_+ k`,  where `gamma_+=log(32/5)-1+5/32 > 1`.

At the lower endpoint `m-C`, the exceedance mean is `(32/5)k`; the corresponding lower-tail exponent is

`gamma_- k`, where `gamma_-=32/5-1-log(32/5)>1`.

Since `k=log n+O(W_n)`, a union bound over all vertices gives

`P(A_n^c)=o(1)`.                                            (15)

On `A_n`, define

`p_tree=e^C k/(n-1)=(32/5)k/(n-1)`,

`p_cross=e^{-C}k/(n-1)=(5/32)k/(n-1)`.

If a fixed set of `r` vertices is a component, it contains a spanning tree whose `r-1` edge scores are at least `m-C`, and every one of its `r(n-r)` crossing-edge scores is at most `m+C`. These are disjoint edge sets, hence independent. Cayley's formula gives

`P(exists an r-component, A_n)`
` <= binom(n,r) r^(r-2) p_tree^(r-1) (1-p_cross)^(r(n-r))`. (16)

For every fixed `r`, (16) has logarithm

`[1-(5/32)r] log n + O_r(log log n+W_n/log n)`.

Thus the contribution tends to zero for each `r=7,...,12`.

For `13<=r<=n/2`, the same standard estimates used by the source give

`P(exists such a component, A_n)`
` <= n/sqrt(2pi) sum_{r=13}^{floor(n/2)}`
` exp{r[1+log(n p_tree)-n p_cross/2+o(1)]}`.               (17)

The bracket in (17) equals

`-(5/64+o(1))log n`.

Choose a fixed `delta` with

`1/13 < delta < 5/64`.

For all sufficiently large `n` the bracket is at most `-delta log n`, so the geometric sum in (17) is `o(1)` because `13 delta>1`. Combining (14)--(17), whp there is no component of any size `1<=r<=n/2`. Hence the graph is connected.

By monotonicity in `k`, this proves connectivity for every sequence with

`k >= log n+aW_n`

for fixed `a>0`.

---

## 7. Theorem and metric consequence

Combining Sections 4--6 proves Claim 282:

**Theorem.** Let `W_n=sqrt(log n log log n)`.

- For every fixed `a<0`, `LK(n,k)` is disconnected whp whenever `k<=log n+aW_n`.
- For every fixed `a>0`, `LK(n,k)` is connected whp whenever `k>=log n+aW_n`.

Therefore the formally admitted fleet proof-frontier metric satisfies

`a_- = 0`, `a_+ = 0`, and `a_LK^fine=0`.

Before/after:

`a_LK^fine: sqrt(11) -> 0`.

This is genuine movement to the theoretical minimum, not a relabeling. The source-scale metric stays `c_LK^cert=0` and is already saturated.

The theorem still does **not** decide what happens at `k=log n+o(W_n)`, and in particular does not determine connectivity at the zero coefficient itself. It therefore narrows the source's open problem sharply but does not close its precise-threshold request.

### Why the common-deadline constant `1` was not intrinsic

Claim 280's common-deadline race had correction

`(c/2+1/(2c))sqrt(k log k)`.

The ordered-deadline theorem has only

`(1/(2c)+o(1))sqrt(k log k)`.

The lost `c/2` was the cost of pretending that every nonzero type could wait until the last type-0 deadline. Keeping the individual deadlines restores the factorial ordering entropy and removes that term.

This also supplies the requested B5 interpolation information: at the `W_n` scale the leading coefficient `1/(2c)` is strictly decreasing in `c`, and no finite positive extremizer remains. For each fixed nonzero source coefficient `a`, one chooses a finite `c` after `a` is fixed. Sending `c` to infinity **with `n`** is not used here and would require a new uniform error analysis; no such stronger statement is claimed.

---

## 8. Failure analysis and exact remaining obligation

The current method has saturated both admitted coefficient metrics, so another run on the same metric cannot count as movement or as a stuck episode.

The live mathematical obligation is now below `W_n`:

1. obtain a sharp asymptotic for `P(I_v)`, not merely the exact lower bound `exp[-k-o(1)]`;
2. make the ordered-deadline estimate uniform when the cutoff multiplier `c` grows with `n`, or derive the correct saddle point at the next candidate scale;
3. determine whether pair isolation remains asymptotically independent at `k=log n+o(W_n)`;
4. on the positive side, sharpen the all-vertex kth-threshold envelope and small-component estimates on the same finer scale;
5. ultimately decide coefficient zero and, if possible, the limiting connectivity law.

The simplest next candidate scale suggested by the ordered-race calculation is `sqrt(log n)`, because choosing `s` of order `sqrt(k)` makes the previously negligible `+s` difference between `K` and `k` enter at leading order. I **do not** freeze a `sqrt(log n)` metric in this report: no source-supported certified baseline at that scale has yet been proved. Its state is `UNMEASURED`, not zero.

A promising next exact object is the normal-transition limit of

`A_K(K+x sqrt K)/sqrt K`,

where `A_K(T)=E[(T-G_K)_+]`. Any next-scale claim must include the `K=k-s-O(1)` shift rather than optimizing only the Poisson race and forgetting the deleted-edge cost.

No HARD recovery is consumed: the admitted metric moved this run. Recoveries remain `0/2`.

---

## 9. Directed independent audit: P04 Claim 44

The newest P04 recovery report at 08:46Z creates no new mathematical claim, so the newest accessible **unaudited** concrete P04 claim after P03's prior audit of Claim 43 is Claim 44 in

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T07-44-02Z__run-report.md`,

creation commit

`ea60d9802c16435ef9c8504e206ce36462b3bee4`,

blob

`7e0626e73c9f5a26ea59e44b7b97f3e750e1c171`.

The audited claim is

`P04-I0101-S3-STANDARD-HEXAGON-44 = PROVED / STRUCTURAL-PARTIAL`.

My verdict is

`P03-AUDIT-P04-I0101-S3-STANDARD-HEXAGON-283 = PASS (CLAIM-SCOPED)`.

This is **not** a repeat of `P03-AUDIT-P04-I0101-A3-SIGNED-QUOTIENT-281`; Claim 43 and Claim 44 are distinct.

### Independent derivation

Let `rho` be the real orthogonal two-dimensional standard representation of `S_3`. Its character is

`chi(e)=2`, `chi(3-cycle)=-1`, `chi(reflection)=0`.

Hence for the three even matrices and separately for the three odd matrices,

`<rho(g),rho(h)>_F = 2` if `g=h`, and `-1` otherwise,

while the even and odd triangle spans are Frobenius-orthogonal. Each parity triangle sums to zero.

For signs `epsilon_g in {+1,-1}`, the signed sum on one triangle is zero if all three signs agree. Otherwise one sign is the minority sign; using the zero-sum relation, the signed sum is `2 epsilon_m rho(m)`, with singular values `(2,2)`. If both parity components are nonzero, after factoring one orthogonal matrix their normalized sum is `I+Q` with `Q` a reflection, hence singular values `(2,0)` before the outer factor two. Therefore the full signed sum has singular values exactly

- `(0,0)` when both parity triples are constant;
- `(2,2)` when exactly one is nonconstant;
- `(4,0)` when both are nonconstant.

Since the unweighted complement matrix is `M_N=-F/2`, its singular values are exactly `(0,0)`, `(1,1)`, or `(2,0)` in the same cases.

For nonnegative weights `w_i` on one parity triangle, whose Gram matrix has diagonal `2` and off-diagonal `-1`,

`||sum_i w_i rho(g_i)||_F^2 = 3 sum_i w_i^2 - m^2`,

where `m=sum_i w_i`. At fixed total mass, equal weights minimize the norm. With `k=1,2,3` available positions, the exact minima are

`2m^2`, `(1/2)m^2`, `0`,

respectively. Thus nonzero exact cancellation is possible iff all three positions in that parity triangle are available, and then the weights must be equal. Orthogonality of the two parity spans makes the full support criterion the conjunction of these two triangle criteria.

For the report's uniform 64-mask consequence, let `r_+` and `r_-` be masses supported respectively on the events that the even or odd triple is fully complementary. Each event has probability `1/8` under the already-proved uniform mask law. Put

`T=r_++r_-`, `S=r_+-r_-`, and `E[T]=mu`.

Then

`E[T^2+S^2]=2(E[r_+^2]+E[r_-^2])`
` >= 16((E r_+)^2+(E r_-)^2)`
` >= 8 mu^2`,

by Cauchy--Schwarz on the two support events and then the two-variable quadratic minimum at equal means. Equality uses constant conditional mass on each full-triangle event and equal means. At `mu=6` the equality rule puts mass `24`, i.e. weight `8` on each of the three available channels. It gives exactly

`Var(T)=126`, `E[S^2]=126`, and `E[T^2+S^2]=288=8*6^2`.

An independent exact self-check over all 64 sign masks and the exact `Q(sqrt(3))` representation was executed and archived:

- checker `proofnet24/P03-fei/artifacts/2026-09-18/p04_claim44_standard_hexagon_audit_check.py`, creation `9c548327e2b6c4462f2c292b4fd3569eea89684f`, blob `78d23edccd87c354144a1f39cf945a599b3174d5`;
- output `proofnet24/P03-fei/artifacts/2026-09-18/p04_claim44_standard_hexagon_audit_check.out`, creation `bbe2b83249bc895bfb05cb836f4f1a13d59773f6`, blob `10496ebebc56eaaf07c93a93fe39ede7082e434a`;
- terminal line: `ALL_EXACT_CHECKS_PASS True`.

The checker independently obtains 4 constant/constant masks, 24 one-nonconstant masks, and 36 two-nonconstant masks with squared singular-value pairs `(0,0)`, `(4,4)`, `(16,0)`, respectively, and verifies the support-Pareto and 64-mask energy values exactly.

**Scope warning:** this PASS certifies Claim 44's local standard-sector theorem and its stated uniform-mask energy consequence, conditional only on the previously established uniform-mask law. It does **not** certify P04's eventual Paley-theta source conjecture or its current 4177 frontier as an asymptotic theorem.

---

## 10. Source/prior-art and novelty record

Primary source checked: Dabirian--Subramanian, DOI `10.1017/jpr.2025.10051`, especially Section 1.1, Lemmas 10--14, Theorem 4 / Corollary 1, and Theorem 5. The paper's printed theorem remains the `+/-1/2` coefficient result at the coarser `sqrt(log n) log log n` scale, and Section 1.1 still labels the displayed band as open.

Fresh bounded 2026-09-18 searches used the exact paper title, author pair, DOI, `LK(n,k) connectivity`, and `bilateral preference random graph connectivity`. They recovered the Cambridge journal article and adjacent/nonmatching literature but no later theorem resolving this exact source question. Search failure is not a novelty certificate.

Claims 276, 278, 280, and 282 therefore retain `PUBLICATION-NOVELTY-UNVERIFIED`. The ordered-deadline Poissonization mechanism is elementary in ingredients; no claim is made that such an argument is new outside this repository.

---

## 11. Next state

Current state:

`P0456_ACTIVE_BELOW_WN / c_LK^cert=0 SATURATED / a_LK^fine=0 SATURATED / NEXT_FINER_METRIC=UNMEASURED / RECOVERIES_USED=0/2`.

Do not count future `0 -> 0` reports on either saturated metric as stuck runs. A new finer metric may be admitted only after an actual theorem supplies a source-matching baseline.

The next mathematical target is the coefficient-zero/finer window. The suggested next method triple, distinct from this run, is **B6 DEFORM TO A POINT YOU CAN SOLVE, B13 FIND WHAT ONLY INCREASES, B27 SWAP THE QUANTIFIERS**. A concrete first task is to derive the sharp `s=Theta(sqrt k)` ordered-deadline variational problem **including** the deletion shift `K=k-s-O(1)`, and then see whether it certifies any nonzero range on the `sqrt(log n)` scale. A theorem there is PARTIAL unless it genuinely narrows the source transition further.

---

## 12. `ledger_delta` for P26

```text
track: P03
source: P0456 Dabirian--Subramanian, J. Applied Probability 63(2) (2026), Section 1.1
claim: P03-P0456-ORDERED-DEADLINE-FINE-WINDOW-ZERO-282
status: PROVED / FINER-WINDOW-PARTIAL / SOURCE OPEN / PUBLICATION-NOVELTY-UNVERIFIED
source_metric: c_LK^cert = 0 -> 0 SATURATED
fine_metric: a_LK^fine = sqrt(11) -> 0 SATURATED (movement)
fine_unchanged_count: 0
recoveries_used: 0/2
theorem: every fixed a<0 at W_n=sqrt(log n log log n) is disconnected whp; every fixed a>0 is connected whp
remaining: coefficient zero and o(W_n) transition / limiting law
next_finer_metric: UNMEASURED (do not encode as zero)
peer_audit: P03-AUDIT-P04-I0101-S3-STANDARD-HEXAGON-283 = PASS (CLAIM-SCOPED)
peer_source_report: proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T07-44-02Z__run-report.md @ ea60d9802c16435ef9c8504e206ce36462b3bee4, blob 7e0626e73c9f5a26ea59e44b7b97f3e750e1c171
shared_ledgers: no edits by P03; P26 only
```

**End of complete run report.**

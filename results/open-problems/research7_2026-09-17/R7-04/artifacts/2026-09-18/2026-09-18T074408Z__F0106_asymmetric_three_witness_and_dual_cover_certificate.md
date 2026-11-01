Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# F0106 — asymmetric overlap, reliability expansion, and an explicit Talagrand-dual cover certificate

Date: 2026-09-18
Slot: `R7-04`
Target: `F0106` — Michel Talagrand, *Are Many Small Sets Explicitly Small?*, canonical Conjecture 7.9 / author-preprint Conjecture 7.8, with canonical dual Conjecture 7.12 / author-preprint Conjecture 7.11.
Methods in this ordinary research iteration: **B15 / B18 / B27**.

This artifact continues the already admitted source problem. It proves new restricted theorems and a source-dual sufficient criterion, but it does **not** prove or refute the universal conjecture and makes no novelty claim.

## 1. Setup and frozen metric

Let `S` be finite. For `I subseteq S`, write

`H_I={J subseteq S:I subseteq J}`.

A probability law `nu` on `2^S` is `r`-spread if

`nu(H_I) <= r^{|I|}`

for every `I subseteq S`. Given `0<alpha<1`, `W_alpha(nu)` is the law obtained by sampling `J~nu` and retaining every element of `J` independently with probability `alpha`.

Talagrand asks whether there is a universal `alpha>0` such that, for every `0<p<1` and every `alpha p`-spread `nu`,

`W_alpha(nu) <=_st mu_p`,

where `mu_p` is Bernoulli product measure.

The frozen metric is

`alpha_dom := sup({a in (0,1): the exact source domination theorem holds with alpha=a for every finite S,p,nu} union {0}).`

The entering bracket is

`0 <= alpha_dom <= alpha_*`,

where `alpha_*` is the unique root of

`-alpha_* log(1-alpha_*)=1`,

numerically `alpha_*=0.740753643351695...`.

The upper bound was proved in the first F0106 run from the uniform-singleton obstruction. The preceding runs proved all disjoint-witness families safe through `alpha_*`, a positive weighted-overlap regime via Harris/Janson, all sunflower witness families safe in the source-relevant range, and the three-edge triangle safe through `alpha_*`.

---

# 2. B15 — break symmetry: the first asymmetric non-sunflower three-edge clutter

The preceding run solved the symmetric triangle. The natural asymmetric three-edge test is the path

`B_1={1,2},  B_2={2,3},  B_3={3,4}`.

Its minimal-witness family is connected, pairwise overlapping along a chain, and is not a sunflower. Put

`A_P={K: B_1 subseteq K or B_2 subseteq K or B_3 subseteq K}`.

Let `r=alpha p` and define

`a=nu(H_{12}), b=nu(H_{23}), c=nu(H_{34}),`

`u=nu(H_{123}), v=nu(H_{234}).`

## 2.1 Exact thinning identity

Conditional inclusion-exclusion on the three edge-events gives

`theta_{J,alpha}(A_P)
 = alpha^2(1_{12 subseteq J}+1_{23 subseteq J}+1_{34 subseteq J})
   -alpha^3(1_{123 subseteq J}+1_{234 subseteq J}).`

Indeed the nonadjacent pair `(12,34)` contributes `-alpha^4 1_{1234 subseteq J}`, while the triple intersection contributes `+alpha^4 1_{1234 subseteq J}`, so those two terms cancel exactly.

Averaging,

`W_alpha(nu)(A_P)=alpha^2[a+b+c-alpha(u+v)].`                         (2.1)

Spreadness gives

`a,b,c <= r^2`.                                                       (2.2)

The shared vertices give stronger capacity inequalities. Since

`H_{12} union H_{23} subseteq H_2`,

we have

`a+b-u = nu(H_{12} union H_{23}) <= nu(H_2) <= r`,

hence

`u >= (a+b-r)_+`.                                                     (2.3)

Similarly,

`v >= (b+c-r)_+`.                                                     (2.4)

Substituting (2.3)--(2.4) into (2.1),

`W_alpha(nu)(A_P)/alpha^2
 <= a+b+c-alpha[(a+b-r)_+ +(b+c-r)_+].`                              (2.5)

For fixed `b`, the right side is increasing separately in `a` and `c`, because each one-sided slope is either `1` or `1-alpha>0`. Thus the maximum under (2.2) has `a=c=r^2`. We reduce to

`F(b)=2r^2+b-2alpha(r^2+b-r)_+`, `0<=b<=r^2`.                        (2.6)

If `r<=1/2`, then `r-r^2>=r^2`; the positive part in (2.6) vanishes throughout the interval and

`F(b)<=3r^2`.                                                         (2.7)

If `r>1/2`, then `r-r^2<r^2`. Since `r=alpha p<alpha`, this regime forces `alpha>1/2`. The slope of (2.6) is `1` before `b_0=r-r^2` and `1-2alpha<0` after `b_0`, so the maximum is attained at `b_0` and

`F(b)<=r+r^2`.                                                        (2.8)

Under product measure,

`mu_p(A_P)=3p^2-2p^3=p^2(3-2p) >= p^2`.                             (2.9)

If `r<=1/2`, (2.7) yields

`W_alpha(nu)(A_P) <= 3alpha^4 p^2`.

If `r>1/2`, (2.8) yields

`W_alpha(nu)(A_P) <= alpha^3 p+alpha^4p^2`.

But `alpha p=r>1/2`, so `alpha^3p < 2alpha^4p^2`, and again

`W_alpha(nu)(A_P) < 3alpha^4p^2`.

Therefore:

### Theorem 2.1 — asymmetric path is safe

For every

`alpha <= 3^(-1/4)`,

all `0<p<1`, and every `alpha p`-spread law `nu`,

`W_alpha(nu)(A_P) <= mu_p(A_P)`.

Since `alpha_*<3/4<3^(-1/4)`, the entire source-relevant interval `alpha<=alpha_*` is safe for this first asymmetric non-sunflower three-edge geometry.

For completeness, `alpha_*<3/4` follows without decimal numerics: `log 2>2/3` from the strict inequality `log x>2(x-1)/(x+1)` for `x>1`, hence

`-(3/4)log(1-3/4)=(3/2)log2>1`,

and monotonicity of `-x log(1-x)` gives `alpha_*<3/4`.

### B15 outcome

Breaking the triangle symmetry did not expose a counterexample. Instead, the shared-vertex spread constraints (2.3)--(2.4) create exactly the compensating negative intersection terms needed to keep the path safe. This identifies a concrete mechanism a larger counterexample must evade: it needs enough incompatible overlap that local vertex capacities cannot be charged to all pair intersections simultaneously.

---

# 3. B18 — reliability / cluster language exposes the exact sign problem

Let the distinct minimal witnesses of an arbitrary proper nonempty up-class `A` be

`B_1,...,B_m`.

For a nonempty index set `F subseteq [m]`, write

`U(F)=union_{j in F} B_j`.

## Proposition 3.1 — exact reliability expansion

For every deterministic `J subseteq S`,

`theta_{J,alpha}(A)
 = sum_{empty != F subseteq [m]}
     (-1)^{|F|+1} alpha^{|U(F)|} 1_{U(F) subseteq J}.`                (3.1)

Consequently,

`W_alpha(nu)(A)
 = sum_{empty != F subseteq [m]}
     (-1)^{|F|+1} alpha^{|U(F)|} nu(H_{U(F)}),`                       (3.2)

whereas

`mu_p(A)
 = sum_{empty != F subseteq [m]}
     (-1)^{|F|+1} p^{|U(F)|}.`                                       (3.3)

### Proof

Conditional on `J`, `A` occurs after thinning exactly when at least one witness `B_j subseteq J` survives. Apply finite inclusion-exclusion to these witness-survival events. A subfamily `F` survives simultaneously exactly when all coordinates in `U(F)` survive, which has probability `alpha^{|U(F)|}` if `U(F) subseteq J` and zero otherwise. This proves (3.1). Averaging gives (3.2). Setting `nu` to the deterministic full set and replacing retention `alpha` by `p` gives (3.3). `QED`

## 3.2 The gluing failure in one line

Spreadness gives only the one-sided inequalities

`nu(H_U) <= (alpha p)^{|U|}`.                                       (3.4)

In (3.2), (3.4) helps on odd-cardinality witness clusters `|F|`, whose coefficients are positive, but it points in the wrong direction on even clusters, whose coefficients are negative. Thus a term-by-term comparison of (3.2) with (3.3) cannot work without **lower information on selected union-marginals** or a positive majorant that removes the alternating terms.

The previous disjoint, Janson, sunflower, triangle and path arguments can all be read as different ways of restoring that missing information. The next section constructs the simplest universal positive majorant directly in Talagrand's own dual language.

### B18 outcome

The problem is now localized more sharply than “overlap is hard”. The exact obstruction is alternating reliability-cluster mass: spreadness controls every principal marginal from above, but the even-cluster terms require either shared-capacity lower bounds or a nonnegative cover replacing inclusion-exclusion. Any counterexample must survive both the earlier dense-overlap/non-sunflower restrictions and the positive-cover criterion below.

---

# 4. B27 — swap the quantifiers: one explicit dual measure for all J

Talagrand's dual Conjecture 7.11 uses

`h(I,J)=(alpha p)^(-|I|) 1_{I subseteq J}` for nonempty `I`,

and `h(emptyset,J)=1`.

It asks for one probability law `eta` depending on `(A,p,alpha)` but **not on J** such that for every `J subseteq S`,

`theta_{J,alpha}(A)
 <= mu_p(A) * integral h(I,J) d eta(I).`                              (4.1)

The following gives a complete explicit certificate whenever `A` has a sufficiently cheap principal-upset cover.

## Theorem 4.1 — explicit cover-supported dual certificate

Let `C` be any finite family of nonempty subsets of `S` such that

`A subseteq union_{I in C} H_I`.                                     (4.2)

Put

`q=alpha^2 p`.

If

`sum_{I in C} q^{|I|} <= mu_p(A)`,                                  (4.3)

then Talagrand's dual inequality (4.1) holds for this `A,p,alpha`. Hence, for every `alpha p`-spread law `nu`,

`W_alpha(nu)(A) <= mu_p(A)`.

### Proof

Write `m_A=mu_p(A)>0` and

`M=(1/m_A) sum_{I in C} q^{|I|} <=1`.

Define a probability measure `eta` by

`eta(I)=q^{|I|}/m_A` for `I in C`,

and place the leftover mass `1-M` at `emptyset`. (If a cover is written with duplicates, combine them first.)

Fix `J subseteq S`. If an `alpha`-thinning `K` of `J` lies in `A`, then by (4.2) there exists some `I in C` with `I subseteq K`, necessarily also `I subseteq J`. The union bound therefore gives

`theta_{J,alpha}(A)
 <= sum_{I in C: I subseteq J} alpha^{|I|}.`                          (4.4)

On the other hand,

`m_A integral h(I,J)deta(I)
 = m_A(1-M)
   + sum_{I in C:I subseteq J} (alpha p)^(-|I|) q^{|I|}`

`= m_A(1-M)
   + sum_{I in C:I subseteq J} alpha^{|I|}`,                          (4.5)

because `q/(alpha p)=alpha`. The first term is nonnegative, so (4.5) dominates (4.4). This proves (4.1).

Integrating (4.1) against an `alpha p`-spread `nu` gives the source domination exactly as in Talagrand's duality argument, since

`integral h(I,J)dnu(J) <=1`

for every `I`. `QED`

## Corollary 4.2 — cover-cost necessary condition for a counterexample

Define the positive cover cost

`Phi_q(A)=min { sum_{I in C} q^{|I|} : C finite, nonempty I's, A subseteq union_{I in C} H_I }.`

Then

`Phi_{alpha^2p}(A) <= mu_p(A)`                                       (4.6)

is sufficient for source domination on `A`.

Therefore every genuine source counterexample at `(alpha,p,A)` must satisfy the strict necessary condition

`Phi_{alpha^2p}(A) > mu_p(A)`.                                       (4.7)

This is not claimed to characterize failure: even when (4.7) holds, a more economical dual probability `eta` using shared mass on smaller intersections can still exist. The point is that the simplest positive principal-upset cover has now been exhausted exactly.

## Corollary 4.3 — witness-count barrier

Let the minimal witnesses of `A` be `B_1,...,B_m`, and put

`k=min_j |B_j|`.

Using the minimal witnesses themselves as `C`,

`Phi_{alpha^2p}(A)
 <= sum_j (alpha^2p)^{|B_j|}
 <= m alpha^{2k} p^k`.                                               (4.8)

Because `A` contains `H_{B_j}` for a witness of size `k`,

`mu_p(A)>=p^k`.                                                       (4.9)

Hence:

### Theorem 4.4 — few-witness theorem

If

`m alpha^{2k} <=1`,                                                   (4.10)

then the exact Talagrand domination inequality holds for `A` against **every** `alpha p`-spread law.

Thus any counterexample at parameter `alpha` must satisfy

`m > alpha^{-2k}`.                                                     (4.11)

In particular, throughout the only still-viable universal range `alpha<=alpha_*`, a counterexample must have

`m > alpha_*^{-2k}`.

The first integer consequences are:

- if `k=1`, at least `2` minimal witnesses;
- if `k=2`, at least `4` minimal witnesses;
- if `k=3`, at least `7` minimal witnesses;
- if `k=4`, at least `12` minimal witnesses.

For `k=2`, this subsumes both the preceding symmetric triangle and the new asymmetric path as far as the source-relevant interval is concerned: **every up-class with at most three 2-uniform minimal witnesses is safe for every `alpha<=alpha_*`**, regardless of its overlap geometry.

The exact numerical thresholds above use only the previously established value of `alpha_*`; e.g. `alpha_*^{-4}=3.3212748...`, so a two-uniform counterexample needs at least four minimal edges.

### B27 outcome

The quantifier swap succeeds on a large explicit class: one probability measure `eta` now controls **all** ambient sets `J` simultaneously whenever the positive cover cost is below the product probability. A genuine counterexample must therefore be simultaneously

1. in the viable range `alpha<=alpha_*`;
2. weighted-overlap dense (from the previous Janson theorem);
3. non-sunflower (from the previous sunflower theorem);
4. cover-resistant in the sharp sense (4.7); and
5. large enough to violate the witness-count barrier (4.11).

For two-uniform minimal witnesses the first unresolved witness count is therefore four.

---

# 5. What remains open

None of B15/B18/B27 proves a positive universal lower bound on `alpha_dom`, and none produces a counterexample below `alpha_*`.

The new exact blocker can be phrased in Talagrand's dual variables. When

`Phi_{alpha^2p}(A)>mu_p(A)`,

the witness-supported positive cover has too much total mass. To continue, one must show that a more efficient probability `eta` can share mass across several witness constraints — typically by putting weight on proper intersections or other sets that contribute simultaneously to many `J` — or else exhibit an up-class for which every such shared-mass construction fails.

The reliability expansion (3.2) says the same thing from the primal side: one must exploit enough even-cluster cancellation to compensate for the failure of the positive union-bound cover.

For two-uniform witness systems, the first possible obstruction by witness count now has at least four edges. This is the simplest special core the next diagnosis should inspect; no claim is made that every four-edge clutter is unresolved or that four edges suffice for a counterexample.

---

# 6. Frozen metric and protocol state

Before this run:

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`.

After this run:

`0 <= alpha_dom <= alpha_* = 0.740753643351695...`.

**NO MOVEMENT.**

Ordinary unchanged count: **`2 -> 3`**.

Status: **PARTIAL / SOURCE OPEN / CLOSABLE OUTSIDE**.

Because this is the third consecutive ordinary no-movement F0106 run, the next R7-04 iteration is required by Section I of the owner directive to be a **thinking-only STUCK1 diagnosis**, not another ordinary research triple. It should isolate the exact dual shared-mass obstruction, consolidate every route and failure, identify the simplest four-witness instance still unproved and the nearest solved analogue, then choose exactly one recovery action and exactly three subsequent Section-B methods.

---

# 7. Dated source / literature check — 2026-09-18

- Talagrand's currently reachable author-hosted preprint `https://michel.talagrand.net/preprints/small.pdf` still states the target as Conjecture 7.8 on PDF p. 9 and the equivalent dual as Conjecture 7.11. The repository's canonical prize copy numbers the same statements 7.9 and 7.12. The source itself explicitly notes that the desired dual measure `eta` is the missing object.
- Chen Li, *On p-Spread Measures*, arXiv:2609.08967v1, submitted 2026-09-08, proves comparison/coupling results for p-spread measures and the fractional discrete-convexity problem. The abstract/current record does not state the exact one-product thinning stochastic domination required by F0106.
- Jinyoung Park, *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*, arXiv:2609.14681v1, submitted 2026-09-13, gives a dimension-independent bound toward Talagrand's discrete convexity conjecture, with a `log log` loss; it does not state the exact F0106 stochastic-domination theorem.
- Ascoli--He--Park--Talagrand, *A reformulation of the discrete Convexity Conjecture via k-thresholds*, arXiv:2608.11183v1, submitted 2026-08-11, treats the broader discrete convexity conjecture and several graph-property classes, not this exact universal thinning-domination statement.
- A bounded fresh search on 2026-09-18 did not locate a later source-matching proof or refutation. This is negative evidence only, not a certification of current openness or novelty.

No finite checker was created in this iteration: the new claims are symbolic theorem-sized statements with complete proofs above, and the protocol forbids checker churn when the frozen source metric does not move.

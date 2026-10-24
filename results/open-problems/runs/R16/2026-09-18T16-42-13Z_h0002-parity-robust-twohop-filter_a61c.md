Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa)` remains at the last supported concrete value `rho*(q_128-q0/64)`, with asymptotic supremum `rho*(q_inf-q0/64)`. This run proves a new source-valid **parity-robust one-or-two-hop gluing theorem** and a polynomial spectral corollary based on `A + A^2/lambda` that tolerates a `-lambda` eigenvalue and therefore includes balanced bipartite expanders excluded by the previous absolute-gap criterion. Section-B methods actually used: **#8 GO THE OTHER WAY AND DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #23 DO WHAT THE PROPOSER DID NOT EXPECT**.

# R16 — H0002: parity-robust two-hop sprinkling and the spectral filter `A + A^2/lambda`

## 1. Continuity, ownership, and required reads

This run continues the active exclusive R16 HARD OUTSIDE claim `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026). It does **not** restart the stale Beck--Fiala scheduler title and does not reopen H0022.

Before research I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/H0002.md`;
- `probability_1000_intake_H_20260914/problems.jsonl`, whose H0002 row source-checks the exact Question 5.1 statement;
- the newest own report `runs/R16/2026-09-18T15-52-39Z_h0002-perron-profile-spectral-criterion_4e91.md`;
- the newest visible same-source neighboring G0010 terminal handoff and G0011 final-recovery report.

The newest R16 report proposed methods `#3/#17/#23`, but `#3` had already been used on H0002 in an earlier run. The controlling owner rule asks for methods not previously tried on the problem, so I replaced that repeated move by unused move **#8**. The actual triple this run is therefore `#8/#17/#23`.

The frozen quantitative class remains exactly the canonical claim:

- `0<epsilon<=1`, `0<rho<=1`, `kappa>0`, `n=|G|`, `lambda=lambda(G)`;
- `q0 := 1-exp(-epsilon^2/288)` and `alpha0 := rho*q0/64`;
- **H1:** `lambda(G-S) >= (1-epsilon/8)lambda` for every `|S|<=rho n`;
- **H2:** `e_G(A,B) >= kappa lambda n` for all disjoint `A,B` with `|A|,|B|>=alpha0 n`;
- **H3:** `lambda(G)->infinity`.

The tracked metric is the largest explicit constant giant fraction proved uniformly on this frozen class at `p >= (1+epsilon)/lambda`, with success probability bounded below by a positive constant depending only on the frozen parameters.

The controlling proof correction remains the 14:58 R16 report: artificial coarse blocks made from disconnected first-round components are invalid. Every gluing argument below works only with the quotient whose vertices are the **actual first-round connected components**.

## 2. Fresh source and prior-art check — 18 Sep 2026

The live arXiv record still exposes only v1 of arXiv:2608.19145, submitted 19 Aug 2026. Question 5.1 still asks:

> What natural conditions on `G` imply that if `p >= (1+epsilon)/lambda(G)` then with constant probability `G_p` contains a component of size `Omega(|G|)`?

The source explicitly says the main obstruction is localization of the spectral radius on a small part of the graph. A bounded 18 Sep search by exact title/arXiv ID/authors and combinations of `percolation`, `spectral radius`, `bipartite`, `two-step`, `two-hop`, `expander mixing`, and `A^2` found no later source-matching resolution. This is negative evidence only, not an openness or novelty certificate.

Relevant baselines checked:

1. CMW themselves use `K_{s,t}` as the sharp model showing that bipartite/two-step geometry matters at the spectral threshold.
2. Diskin--Erde--Kang--Krivelevich, *Percolation through Isoperimetry* (Ann. IHP 2026; arXiv:2308.10267), prove a strong regular growing-degree theorem from one-set isoperimetry and use multi-round exposure; they also show fixed positive ordinary isoperimetry can be insufficient. Their theorem is a baseline, not the irregular spectral statement below.
3. Bipartite/two-step spectral mixing and polynomial filtering are standard spectral-graph ideas; e.g. nonbacktracking and biregular walk spectra are classical machinery. I make **no novelty claim** for the polynomial-filter idea itself. The potentially new item is the explicit reduction of the parity-robust filtered condition below to CMW Question 5.1 at the exact `1/lambda(G)` scale. A bounded search did not locate this exact corollary, which is not a novelty certificate.

## 3. Why the previous natural spectral criterion had a real blind spot

The preceding R16 report used

`A = lambda v v^T + E`, `||E|| = Lambda := max_{i>=2}|lambda_i|`,

and obtained macroscopic pair expansion from a condition of the form

`L_alpha(v)^2 - Lambda/(2lambda) > 0`.

That is clean for non-bipartite pseudorandom graphs, but it deliberately treats a large negative eigenvalue as bad. A balanced bipartite expander has eigenvalue `-lambda`, so `Lambda/lambda=1` even when its geometry is excellent for percolation. In particular, `K_{m,m}` has perfectly flat Perron vector but fails the old absolute-gap test.

The new route asks whether **parity, rather than poor mixing, is what caused the failure**. The answer is yes: one step connects opposite sides, two steps connect the same side. This suggests that the correct finite language for the gluing stage should retain both path lengths `1` and `2`.

## 4. Method #8 — discretize macroscopic communication to lengths 1 and 2

For disjoint sets `A,B` and a vertex `z`, write

`d_A(z) := |N(z) cap A|`, `d_B(z) := |N(z) cap B|`.

Define the **capped external two-hop capacity**

`C2(A,B) := sum_{z notin A union B} min{d_A(z),lambda} min{d_B(z),lambda}`.

The cap at `lambda` is essential: it records the amount of two-hop mass that can actually be converted into independent constant-probability connectors at edge density `Theta(1/lambda)`, instead of allowing all length-two walks to concentrate through a tiny number of enormous-degree middle vertices.

For constants `kappa_1,kappa_2>0` and a macroscopic threshold `alpha>0`, define the **one-or-two-hop mixing condition**:

`H2^{<=2}(alpha;kappa_1,kappa_2):`

for every disjoint `A,B` with `|A|,|B|>=alpha n`, at least one of

1. `e_G(A,B) >= kappa_1 lambda n`, or
2. `C2(A,B) >= kappa_2 lambda^2 n`

holds.

This condition allows `e_G(A,B)=0` for some macroscopic pairs, provided there is enough two-hop communication through vertices outside `A union B`. That is exactly what the old direct-pair condition could not see.

## 5. Main theorem — parity-robust three-round gluing at the CMW threshold

Set

`a := 1-epsilon/8`,

`delta := epsilon/128`,

`eta := a*(1+epsilon-delta)-1`,

`q := 1-exp(-eta^2/18)`.

For `0<epsilon<=1`, one has `eta>epsilon/4>0` and `eta<1`.

### Theorem 5.1 — one-or-two-hop giant criterion

Fix `epsilon,rho,kappa_1,kappa_2>0` and let `G=G_n` be a graph sequence with `lambda=lambda(G)->infinity`. Assume:

1. **spectral deletion resilience:** for every `S` with `|S|<=rho n`,
   `lambda(G-S) >= a lambda`;
2. for some fixed `alpha` with `0<alpha<q rho/3`, the condition `H2^{<=2}(alpha;kappa_1,kappa_2)` holds.

Then, for every

`p >= (1+epsilon)/lambda(G)`, 

there exists `c=c(epsilon,rho,kappa_1,kappa_2,alpha)>0` such that for all sufficiently large `n`,

`P( L1(G_p) >= (q rho-alpha)n ) >= c-o(1)`.

In particular, taking the frozen `alpha=alpha0=rho*q0/64` and using old H2 as the direct alternative gives the already certified concrete frozen metric

`g_twoaxis >= rho*(q_128-q0/64)`,

where this `q` is exactly `q_128`.

### Proof

By monotonicity it is enough to take `p=(1+epsilon)/lambda`.

#### Step 1: a genuine three-round exposure

Let

`p1 := (1+epsilon-delta)/lambda`.

Choose `r` so that the union of three independent percolations with edge probabilities `p1,r,r` has law `G_p`, i.e.

`1-p = (1-p1)(1-r)^2`.

Put

`x := (p-p1)/(1-p1) = delta/[lambda(1-p1)]`.

Then

`r = 1-sqrt(1-x) = x/(1+sqrt(1-x)) >= x/2 >= delta/(2lambda)`.      (5.1)

Call the three independent rounds `G1,G2,G3`.

#### Step 2: first-round seed components

Run the same adaptive deletion exploration used in the earlier valid R16 H0002 theorem. Before each attempt the deleted set `S` has size at most `rho n`; hence by H1,

`lambda(G-S) >= a lambda`.

Therefore

`p1 lambda(G-S) >= a(1+epsilon-delta) = 1+eta`.

Choose a vertex attaining the maximum of the normalized Perron vector of `G-S` and reveal its `G1`-component. CMW Lemma 3.1(b), applied with supercritical margin `eta` and `C=1`, gives conditional probability at least

`q = 1-exp(-eta^2/18)`

that this component has size more than

`(eta/6) lambda(G-S) >= s := (a eta/6)lambda`.             (5.2)

Call such a component successful. A failed explored component has size at most `s`.

We recall the endpoint adaptive-seed lemma proved in the valid 11:42 R16 line. If each adaptive trial has conditional success probability at least `q`, each success removes at least `s` vertices and each failure at most `s`, then before a deletion budget `R` is exhausted there is a probability `c_seed(q)>0`, uniformly in `R/s`, of accumulating at least `qR` successful mass.

For completeness, the comparison behind that lemma is short. If the target `qR` is missed, put `y=R/s`. Failure forces roughly `(1-q)y` failed trials before roughly `qy` successful trials. Dominate the adaptive success indicators from below by iid `Ber(q)`. With

`k=ceil(qy)`, `r0=floor((1-q)y)+1`,

the probability that the `k`th success occurs before the `r0`th failure is

`P(Bin(k+r0-1,q) >= k)`.

Here `k+r0-1=y+O(1)` and `k-q(k+r0-1)=O(1)`. For large `y` the standardized threshold tends to zero, so the probability tends to `1/2`; for bounded `y`, only finitely many threshold pairs occur and the all-success event supplies a positive minimum. Thus a uniform `c_seed(q)>0` exists.

Apply this with `R=rho n`. With probability at least `c_seed(q)`, the union `U` of successful **actual `G1` connected components** has total seed mass

`W:=|U| >= q rho n`.                                           (5.3)

Every successful component has at least `s` vertices, so their number `m` satisfies

`m <= n/s = [6/(a eta)] n/lambda`.                            (5.4)

No artificial union is treated as connected.

#### Step 3: deterministic cut extraction on the true quotient

Condition on a first-round realization satisfying (5.3). If some final component after rounds 2 and 3 contains seed mass at least `W-alpha n`, we are done.

Suppose not. Consider the connected components of the final graph, but assign each only the number of vertices it contains from `U`. These weights sum to `W`, and every weight is strictly less than `W-alpha n`.

Since `W>=q rho n>3alpha n`, there is a union of final components whose seed weight lies in `[alpha n,W-alpha n]`: if some component already has weight at least `alpha n`, take it; otherwise greedily add components of weight `<alpha n` until crossing `alpha n`, producing weight `<2alpha n<=W-alpha n`.

Thus failure of the claimed giant produces a partition

`U=A dotcup B`

such that `A` and `B` are each unions of first-round successful components,

`|A|,|B|>=alpha n`,                                             (5.5)

and there is **no final path** from `A` to `B`.

There are at most `2^m` possible such cuts.

#### Step 4: direct one-hop cuts

Fix one cut `(A,B)` satisfying (5.5). If the first alternative of `H2^{<=2}` holds, there are at least `kappa_1 lambda n` host edges directly from `A` to `B`.

If any such edge appears in round 2, the cut is joined. By (5.1),

`P(no round-2 direct edge across A,B)`

`<= exp(-r kappa_1 lambda n)`

`<= exp(-(delta kappa_1/2)n)`.                                (5.6)

#### Step 5: two-hop cuts

Suppose instead the second alternative holds:

`C2(A,B)>=kappa_2 lambda^2 n`.

For every `z outside A union B`, let `E_z` be the event that round 2 contains at least one edge from `z` to `A` and round 3 contains at least one edge from `z` to `B`.

The events `(E_z)` are independent over distinct `z`: their round-2 edge sets `E(z,A)` are disjoint, their round-3 edge sets `E(z,B)` are disjoint, and the two rounds are independent.

Let `f_r(d)=1-(1-r)^d`. From `r>=delta/(2lambda)`, monotonicity in `r`, and concavity of `d -> 1-(1-delta/(2lambda))^d`, for every integer `d>=0` we have

`f_r(d) >= c_delta min{d/lambda,1}`,                           (5.7)

where

`c_delta := 1-exp(-delta/2)>0`.

Indeed, for `d<=lambda`, concavity between `0` and `lambda` gives

`f_r(d) >= (d/lambda) [1-(1-delta/(2lambda))^lambda]`

`>= (d/lambda)(1-exp(-delta/2))`,

and for `d>=lambda` monotonicity gives the same bound with the minimum equal to `1`.

Therefore

`P(E_z)`

`= f_r(d_A(z)) f_r(d_B(z))`

`>= (c_delta^2/lambda^2) min{d_A(z),lambda} min{d_B(z),lambda}`.

Using independence over `z`,

`P(no two-hop connector from A to B)`

`<= exp(-sum_z P(E_z))`

`<= exp(-c_delta^2 kappa_2 n)`.                               (5.8)

Any `E_z` supplies a final path `A-z-B`, contradicting the cut.

#### Step 6: union bound over true component cuts

Let

`c_* := min{delta kappa_1/2, c_delta^2 kappa_2}>0`.

By (5.6)--(5.8), every possible bad quotient cut survives rounds 2 and 3 with probability at most `exp(-c_* n)`. By (5.4), the number of cuts is at most

`2^m <= exp([6 log 2/(a eta)] n/lambda) = exp(o(n))`

because `lambda->infinity`. Hence, conditioned on the seed event,

`P(some bad macroscopic quotient cut survives) = o(1)`.

So with probability `c_seed(q)-o(1)` the final graph contains a connected component carrying at least

`W-alpha n >= (q rho-alpha)n`

seed vertices, hence at least that many vertices in total. This proves Theorem 5.1. QED.

## 6. Method #17 — the number `-1` points to the filter `x+x^2`

The previous absolute-gap condition fails on bipartite graphs because the normalized adjacency has an eigenvalue `-1`. The simplest polynomial that preserves the Perron mode at `x=1` but annihilates the bipartite parity mode at `x=-1` is

`x+x^2 = x(1+x)`.

On the adjacency matrix this is exactly

`T := A + A^2/lambda`.                                        (6.1)

This is also precisely the matrix that counts one-step communication plus normalized two-step communication. The algebra therefore matches the probabilistic one-or-two-hop condition above rather than being an arbitrary spectral trick.

Let `G` be connected, let `v>0` be its unit `l2` Perron vector, and write the adjacency eigenvalues as

`lambda=lambda_1 >= lambda_2 >= ... >= lambda_n >= -lambda`.

Define

`x_i:=lambda_i/lambda`,

`Theta_2 := max_{i>=2} |x_i+x_i^2|`.                          (6.2)

Then

`T = 2lambda vv^T + E`, `||E||_op = Theta_2 lambda`.          (6.3)

For `alpha in (0,1/2]`, define as before

`L_alpha(v) := min_{|S|>=alpha n} (1/sqrt(n)) sum_{x in S} v_x`.

### Proposition 6.1 — polynomial mixing forces direct-or-two-hop capacity

Assume `Delta(G)<=D lambda` for a fixed `D>=1` and put

`K := 2 L_alpha(v)^2 - Theta_2/2`.

If `K>0`, then every disjoint `A,B` with `|A|,|B|>=alpha n` satisfies `H2^{<=2}` with the explicit constants

`kappa_1 = K/[2(1+2D)]`,

`kappa_2 = K/[2D^2]`.                                        (6.4)

#### Proof

For disjoint `A,B`, let `1_A,1_B` be their indicators. By (6.3), disjointness, and `sqrt(|A||B|)<=n/2`,

`1_A^T T 1_B`

`>= 2lambda <1_A,v><1_B,v> - Theta_2 lambda sqrt(|A||B|)`

`>= lambda n [2L_alpha(v)^2-Theta_2/2]`

`= K lambda n`.                                               (6.5)

On the other hand,

`1_A^T T 1_B = e(A,B) + P2(A,B)/lambda`,                      (6.6)

where

`P2(A,B):=sum_{z in V} d_A(z)d_B(z)`

is the total number of length-two `A-z-B` walks.

Set

`beta:=K/[2(1+2D)]`.

If `e(A,B)>=beta lambda n`, the direct alternative holds with `kappa_1=beta`.

Otherwise (6.5)--(6.6) give

`P2(A,B) >= (K-beta)lambda^2 n`.                              (6.7)

The contribution of middle vertices lying inside `A union B` is controlled by the direct cut:

`sum_{z in A} d_A(z)d_B(z) <= Delta sum_{z in A} d_B(z) = Delta e(A,B)`,

and similarly for `z in B`. Hence

`sum_{z in A union B} d_A(z)d_B(z) < 2D beta lambda^2 n`.     (6.8)

Subtracting (6.8) from (6.7),

`P2_out(A,B):=sum_{z notin A union B}d_A(z)d_B(z)`

`>= [K-(1+2D)beta]lambda^2 n`

`= (K/2)lambda^2 n`.                                         (6.9)

Finally, because every degree is at most `Dlambda`, for each `z`

`min{d_A(z),lambda} >= d_A(z)/D`,

and likewise for `B`. Therefore

`C2(A,B) >= P2_out(A,B)/D^2 >= [K/(2D^2)]lambda^2 n`.         (6.10)

This is exactly the second alternative with `kappa_2=K/(2D^2)`. QED.

## 7. A parity-robust Perron spectral criterion for CMW Question 5.1

Retain `alpha=alpha0=rho*q0/64`. Define the Perron localization profile

`U_rho(v):=max_{|S|<=rho n} sum_{x in S}v_x^2`.

The previous R16 Rayleigh calculation gives

`lambda(G-S) >= lambda(G) (1-2m_S)/(1-m_S)`,

where `m_S=sum_{x in S}v_x^2`. Hence

`U_rho(v) <= epsilon/(8+epsilon)`                             (7.1)

implies H1.

Combining (7.1), Proposition 6.1 and Theorem 5.1 gives the following source-valid theorem.

### Theorem 7.1 — parity-robust filtered spectral criterion

Fix `epsilon,rho,D>0`. Let `G_n` be connected graphs with `lambda(G_n)->infinity` and `Delta(G_n)<=D lambda(G_n)`. Let `v_n` be their unit Perron vectors. Put

`alpha0 = rho[1-exp(-epsilon^2/288)]/64`.

Assume uniformly that

`U_rho(v_n) <= epsilon/(8+epsilon)`                            (7.2)

and, for some `K_*>0`,

`2 L_alpha0(v_n)^2 - (1/2) max_{i>=2}|x_i+x_i^2| >= K_*`,     (7.3)

where `x_i=lambda_i/lambda_1`.

Then for every `p>=(1+epsilon)/lambda(G_n)`, with probability bounded below by a positive constant, `G_{n,p}` contains a component of at least

`rho*(q_128-q0/64)n`

vertices for all sufficiently large `n`.

This is a PARTIAL answer to CMW Question 5.1. It is not claimed to characterize the optimal natural conditions.

### Why this is strictly more parity-tolerant than the preceding R16 spectral criterion

For a connected `d`-regular bipartite graph, the spectrum contains both `d` and `-d`. The old absolute-gap parameter sees `|-d|/d=1` and therefore fails automatically at the small `alpha0` relevant here.

The new filter sees

`(-1)+(-1)^2=0`.

Thus exact bipartiteness is not penalized.

For a vertex-transitive `d`-regular bipartite graph, `v=n^{-1/2}1`, so

`U_rho(v)=rho`, `L_alpha(v)=alpha`, `D=1`.

If every eigenvalue other than the forced pair `+/-d` has absolute value at most `beta d`, then

`Theta_2 <= beta+beta^2`.

Consequently (7.3) follows from

`beta+beta^2 < 4 alpha0^2`.                                  (7.4)

In particular, the balanced complete bipartite graph `K_{m,m}` has spectrum `{m,-m,0,...,0}`, so `Theta_2=0`; for `rho<=epsilon/(8+epsilon)` it satisfies the localization side as well. The theorem therefore recognizes the standard supercritical giant in balanced bipartite geometry, while the previous absolute-gap criterion could not even enter the proof.

This example is diagnostic, not a novelty claim about `K_{m,m}` percolation.

## 8. Method #23 — let direct macroscopic edges vanish on purpose

The proposer emphasizes spectral localization and robust connectivity. The unexpected test was to permit a much harsher failure than ordinary connectivity arguments usually tolerate:

`e(A,B)=0`

for some macroscopic seed unions `A,B`.

Theorem 5.1 shows that this need not matter. If there is capped two-hop capacity `Omega(lambda^2 n)` through the outside reservoir, two independent sprinkle rounds create `exp(-Omega(n))` failure for that cut. This is strong enough to beat the `exp(O(n/lambda))` entropy of the true seed-component quotient under H3.

So the direct-pair H2 condition from the first R16 theorem is **not conceptually essential**. What is essential for the present proof architecture is a macroscopic communication channel whose per-cut failure exponent is linear in `n`; direct edges are only one such channel.

The precise invariant exposed by the run is therefore:

> after the local supercritical seed phase, every macroscopic partition of actual seed components must carry enough **usable capacity at some bounded path length** to beat the quotient cut entropy.

Lengths `1` and `2` already suffice to remove the artificial penalty for strong bipartiteness.

## 9. What this run did not prove

1. The frozen metric itself did **not** move. The last supported concrete value remains
   `rho*(q_128-q0/64)`, with the already known asymptotic supremum `rho*(q_inf-q0/64)` on H1--H2--H3.
2. The theorem does not remove H3. The two-hop cut union bound uses `m=O(n/lambda)=o(n)`.
3. The polynomial condition (7.3) is sufficient, not necessary, and can be quantitatively severe because `alpha0` is small.
4. No claim is made that polynomial spectral filters or two-step mixing are new. A publication-level prior-art audit is still required for the exact percolation corollary.
5. This does not close CMW Question 5.1, which is intentionally open-ended and asks for natural conditions rather than one canonical characterization.

## 10. Beck--Fiala title reconciliation

The scheduler title is still historically Beck--Fiala, but current primary literature makes that source target a baseline rather than an unresolved R16 problem.

- Bansal--Jiang, arXiv:2508.03961, prove the conjectured `O(sqrt(t))` regime for `t>=log^2 n` and give weaker polylogarithmic losses below that range.
- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted **10 Sep 2026**, state the stronger Komlos theorem with universal constant `3 sqrt(2 pi)` and explicitly derive

  `disc(F) < 3 sqrt(2 pi t)`

  for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188, posted **17 Sep 2026**, give an independently authored elementary simplification proving Komlos with constant `36`.

These are extremely recent preprint/technical-report results rather than mature refereed consensus, but on their stated theorems the old complete uniform Beck--Fiala metric is currently bounded by

`B(t,n) < 3 sqrt(2 pi t)` for every `t>=1` and every `n`.

This is a **KNOWN current-literature baseline**, not an R16 result, and is why the active exclusive R16 research target remains H0002.

## 11. Method accounting and next move

Actual methods this run:

- **#8 DISCRETIZE:** replaced arbitrary macroscopic communication geometry by a two-channel finite language: usable paths of length `1` or `2`.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** the bipartite obstruction is the normalized eigenvalue `-1`; the polynomial `x+x^2` vanishes exactly there and turns into the one-plus-two-step matrix `A+A^2/lambda`.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** allowed a macroscopic pair to have zero direct edges and proved that a third-vertex reservoir can glue it anyway.

All three routes converged to the same parity-robust theorem rather than producing three unrelated lemmas.

The only Section-B moves not yet used on H0002 are now **#16 COMPUTE EVERY SMALL CASE, #26 HUNT THE SPORADIC CASE, #28 REPLACE FOR ALL WITH TYPICAL**. Those are therefore the next triple. The next substantive target is not another split-constant optimization: it is to test whether the filtered criterion can be weakened from a worst-case condition over **all** macroscopic cuts to a condition on the random family of cuts generated by the seed quotient, or whether an explicit multipartite/sporadic family defeats that quantifier swap.

## 12. Protocol/accounting

No checker was manufactured because this run's new claims are analytic theorem-sized statements with full proofs on the page and no finite computational core.

`ledger_delta`:

```yaml
worker: R16
target: H0002
source: arXiv:2608.19145v1, Question 5.1
status_before: PARTIAL / SOURCE OPEN / ACTIVE
status_after: PARTIAL / SOURCE OPEN / ACTIVE
metric: g_twoaxis(epsilon,rho,kappa)
before: rho*(q_128-q0/64)
after: rho*(q_128-q0/64)
movement: none
supported_unchanged_count_before: 1
supported_unchanged_count_after: 2
new_result: parity-robust H1 + H2^{<=2} + H3 giant theorem; polynomial A+A^2/lambda spectral corollary
closure_claimed: false
claim_or_ownership_change: none
methods: [8,17,23]
next_methods: [16,26,28]
```

The run is **not yet in a stuck recovery**: this is the second consecutive supported no-movement run on the frozen metric. A third consecutive no-movement run would trigger the owner's Section-I stuck protocol on the subsequent invocation.

No shared root ledger, peer research file, claim file, scheduler, email, Drive item, public post, permission, purchase, or workflow was changed.

## 13. Model/scheduler control limitation

The model-control limitation remains exactly as recorded in the controlling policy and fleet ledger. The exposed task control surface provides prompt/title, schedule or start offset, timing mode, enablement, and task identity, but **no binding model-family selector, reasoning-effort selector, or authenticated applied-model receipt**. GPT-6/maximum can therefore only be requested in prompt text in this interface. Enforcing it would require the scheduler/API itself to expose model and reasoning fields plus per-run runtime attestation.

The historical P26 `You cannot modify this task` denial was authorization-context-specific; repository history records a later successful P26 update from an authorized context. The compliant workaround for any currently denied task remains the owning authorized workspace/account context or platform support, never duplication or permission bypass.

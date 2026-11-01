Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — Poisson isolated vertices and the constant-width connectivity window

**SOURCE-MATCHING CANDIDATE COMPLETE / AUDITS PENDING.** All three previously admitted fixed-coefficient proof-frontier metrics remain saturated at their theoretical minima,

- `c_LK^cert=0` at `sqrt(log n) log log n`,
- `a_LK^fine=0` at `sqrt(log n log log n)`,
- `b_LK^sqrt=0` at `sqrt(log n)`,

and I do **not** manufacture a stuck count from those saturated quantities. HARD recoveries remain `0/2`.

The new theorem goes below every previously frozen scale and identifies the full constant-width critical law. I therefore do not invent another fixed-coefficient metric. Instead the new source-matching limiting-law parameter is explicit:

`lambda_LK(c) = e^{-c}` for the asymptotic number of isolated vertices when `k-log n -> c`.

Main new claim:

`P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Let `k=k_n` be integer-valued and suppose

`k - log n -> c in R`.

If `Z_n` denotes the number of isolated vertices of `LK(n,k)`, then

`Z_n => Poisson(e^{-c})`,

and

`P(LK(n,k) is connected) -> exp(-e^{-c})`.

In particular, the source's Section 1.1 connectivity-window gap is closed at the mathematical level by an `O(1)` window, with the same limiting connectivity law as the classical Erdos--Renyi connectivity window. This is **not yet protocol-closed**: the source-matching proof still requires the two independent OTHER-track audits mandated by the fleet protocol, and publication novelty remains unverified.

The three Section-B moves used substantively were **#3 PROVE SOMETHING STRONGER, #11 DUALIZE, #25 COUNT THE SAME THING TWICE**.

---

## 1. Continuity, source gate, and repository status

The canonical exclusive claim remains

`operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

I continued from the newest complete P03 report

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T11-32-44Z__p0456-sparse-deletion-sqrtlog-zero.md`,

creation commit `6bd701b61ce35adee5c0bf6565fbc78ee5953b9c`, blob `8f6735ab1bd8515834a6091b8d7afffb8a2218a0`, and preserve Claims 274, 276, 278, 280, 282, 284, 286.

Repository continuity this invocation recovered/reread the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` by exact-path read, the canonical P0456 claim and targeted ownership/history search, the newest P03 P0456 report, the retained Claim-280 component proof, and the newest P04/I0101 handoff for the directed-audit duty. Large root ledgers/search surfaces are connector-truncated, so I do not claim byte-for-byte rereads of every large file; exact paths and scoped searches were used where needed.

Fresh source/status verification on 2026-09-18 recovered the Cambridge primary article:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579; published online 18 December 2025; DOI `10.1017/jpr.2025.10051`.

Cambridge Section 1.1 still says explicitly that it is unknown whether connectivity holds inside

`log n - (1/2) loglog n sqrt(log n) <= k <= log n + (1/2) loglog n sqrt(log n)`,

and says more elaborate or exact sufficient conditions might close the gap. The source's Lemma 10 gives `P(B)=O(k^3/n)` for its pair-interaction event and Lemma 13 gives exact conditional independence on `B^c`.

Fresh bounded searches for the exact title/authors/DOI, `LK(n,k) Poisson isolated vertices`, `bilateral preference connectivity log n + c`, and 2026 citing/author material recovered the current Cambridge paper and its arXiv lineage, but no later source-matching constant-window or Poisson theorem. This is dated bounded negative evidence only, **not** proof of worldwide openness or publication novelty.

P0457 remains a distinct diameter problem and is not duplicated here.

---

## 2. Idea before proof — the exact lower event is already asymptotically exact

Claim 278 produced the exact sufficient-event integral

`p_* = (m)_k/(k-1)! int_0^1 q(x) Q(x)^(k-1) (1-x)^(m-k) dx`,

where

`m=n-1`, `N=n-k-1`,

`q(x)=P(Bin(N,x)>=k)`, `Q(x)=int_0^x q(u)du`.

The lower bound from marking **all** incident points was

`p_* >= (1-k/(n-k))^(n-1) = e^{-k}(1+o(1))`

when `k=O(log n)`.

The question for this run was whether the exact first-`k` marking probability is larger by a nontrivial constant, and whether internal edges among the first `k` neighbors change that constant.

The answer to both is no.

The key B11 duality is that `q_h(x)=P(Bin(N,x)>=h)` is the distribution function of the `h`th order statistic `B_h` of `N` independent uniforms. Therefore

`Q_h(x)=E[(x-B_h)_+]`.

The mean of `B_h` is exactly `mu_h=h/(N+1)`. Replacing the random `B_h` by its mean turns the marked integral into a beta integral that evaluates **exactly** to `(1-mu_h)^m`. The random fluctuation of `B_h` is only `Theta(sqrt(k)/n)`, while the marked saddle lies a further `Theta(k/n)` to the right. Thus the beta-mean lower event is asymptotically all of the marked event.

I first tried to refute this by looking for mass near the normal-transition region `x~k/n`. That region loses an exponentially positive fraction of `k` in the Laplace exponent; the dominant point is instead near `x~2k/n`, exactly where the beta fluctuation is exponentially irrelevant. This is the mechanism that was hidden by the previous `sqrt(k)` race analysis.

---

## 3. B11/B25 marked-saddle lemma

We need a slightly more general version because later interaction bounds may lower a rejection threshold by a fixed integer.

### Lemma 3.1 (fixed-defect marked saddle)

Let `d>=0` be fixed, `h=k-d`, `m=n+O(1)`, `N=n+O(k)`, with `k->infinity` and `k=O(log n)`. Put

`q_h(x)=P(Bin(N,x)>=h)`,

`Q_h(x)=int_0^x q_h(u)du`.

Let `M_{k,h}(m,N)` be the probability that the first `k` points, in increasing order, among `m` iid Uniform[0,1] points are all marked, where a point at `x` is independently marked with probability `q_h(x)`. Then

`M_{k,h}(m,N) = exp(-h)(1+o(1))`,

uniformly for fixed `d` and the displayed ranges of `m,N`.

#### Proof

The exact rank-`k` reduction is

`M_{k,h} = (m)_k/(k-1)! int_0^1 q_h(x) Q_h(x)^(k-1) (1-x)^(m-k) dx`.

Since `d(Q_h^k)=k q_h Q_h^(k-1) dx`, integration by parts gives

`M_{k,h} = (m)_{k+1}/k! int_0^1 Q_h(x)^k (1-x)^(m-k-1) dx`.      (3.1)

Now let

`B_h ~ Beta(h,N-h+1)`.

The standard beta-binomial identity gives

`q_h(x)=P(B_h<=x)`

and hence

`Q_h(x)=E[(x-B_h)_+]`.                                      (3.2)

Write

`mu=E B_h = h/(N+1)`,

`Var(B_h)=h(N-h+1)/((N+1)^2(N+2)) = O(k/n^2)`.               (3.3)

By convexity,

`Q_h(x)>= (x-mu)_+`.                                        (3.4)

Substituting `(x-mu)_+` in (3.1) yields an exact beta integral:

`(m)_{k+1}/k! int_mu^1 (x-mu)^k (1-x)^(m-k-1) dx
 = (1-mu)^m`.                                                (3.5)

This already gives the lower bound.

For the upper bound, split at

`x_0 = mu + k/(2N)`.

For `x>=x_0`, write, using `E B_h=mu`,

`Q_h(x)=x-mu+R_h(x)`,

`R_h(x)=E[(B_h-x)_+]`.                                      (3.6)

At `x_0`, the corresponding binomial mean is `(3/2+o(1))k`, while the threshold is `h=k+O(1)`. A fixed Chernoff lower-tail bound therefore gives constants `gamma>0`, `C<infinity` such that uniformly for `x>=x_0`,

`P(B_h>x)<=C e^{-gamma k}`.                                 (3.7)

By Cauchy--Schwarz and (3.3),

`R_h(x) <= O(sqrt(k)/n) e^{-gamma k/2}`.                    (3.8)

Since `x-mu>=k/(2N)`,

`sup_{x>=x_0} k R_h(x)/(x-mu) ->0`.                         (3.9)

Hence on this whole region

`Q_h(x)^k=(x-mu)^k(1+o(1))` uniformly.                      (3.10)

On `x<=x_0`, use

`Q_h(x)<= (x-mu)_+ + E|B_h-mu|
        <= (x-mu)_+ + O(sqrt(k)/n)`.                         (3.11)

Set `x=mu+zk/N`. For `0<=z<=1/2`, Stirling in the integrand of (3.1) gives, uniformly away from a vanishing `O(k^{-1/2})` neighborhood of zero,

`log(integrand contribution) <= -h + k(log z-z+1) + o(k)`

after the common beta normalization. The function `log z-z` is increasing on `(0,1)` and at `z=1/2` equals `-log 2-1/2<-1`. Thus this region is smaller than `(1-mu)^m` by `exp(-eta k)` for some `eta>0`. For `x<mu+O(sqrt(k)/n)`, (3.11) instead gives the stronger factor `k^{-k/2+O(k)}`. Therefore

`M_{k,h}=(1-mu)^m(1+o(1))`.                                (3.12)

Finally, because `m=n+O(1)`, `N=n+O(k)` and `h=O(log n)`,

`m log(1-h/(N+1)) = -h+O(k^2/n)=-h+o(1)`.                  (3.13)

Combining (3.12)--(3.13) proves the lemma. `square`

**B25 check.** The same constant is therefore obtained two ways: from the beta-mean integral (3.5) and from the marked point-process saddle (3.6)--(3.13). Both give multiplicative constant `1` in front of `e^{-h}`.

---

## 4. Exact one-vertex isolation probability

### Theorem 4.1

Uniformly for `k=log n+O(1)` (indeed for `k->infinity`, `k=O(log n)`),

`P(I_v)=e^{-k}(1+o(1))`.                                    (4.1)

#### Proof

Let `S` be the first `k` preferred neighbors of `v`, with incident order statistics

`X_(1)<...<X_(k)`.

Delete all edges internal to `S` from the neighbors' rejection tests. The resulting sufficient event is exactly the Claim-278 marked event with `h=k`, `m=n-1`, `N=n-k-1`, so Lemma 3.1 gives

`P(E_v)=e^{-k}(1+o(1))`.                                    (4.2)

Hence `P(I_v)>=e^{-k}(1+o(1))`.

For the upper bound, fix a constant `L` with

`L-1-log L > 2`; for instance `L=8`, and put

`G_v={X_(k)<=Lk/n}`.

Then

`P(G_v^c)=P(Bin(n-1,Lk/n)<=k-1)
 <= exp(-(L-1-log L+o(1))k)=o(e^{-k})`.                      (4.3)

Call an internal edge `{i,j}` of `S` **active** if its weight is below at least one of its two target edges `(v,i),(v,j)`. Conditional on the incident weights at `v` and on `G_v`, each of the at most `k^2/2` internal edges is active with probability at most `Lk/n`, independently across internal edges. Therefore

`P(at least two active internal edges, G_v)=O(k^6/n^2)=o(e^{-k})`. (4.4)

If there is no active internal edge, `v` is isolated iff `E_v` holds.

If there is exactly one active internal edge, isolation implies that **every** selected neighbor has at least `k-1` outside-`S` competitors before its target edge; relaxing the nonendpoints from `k` to `k-1` only enlarges the event. The active internal edge is independent of all these outside edge lists conditional on the incident weights. Hence, by a union bound over internal pairs and Lemma 3.1 with `h=k-1`,

`P(I_v, G_v, at least one active edge)
 <= O(k^2) (Lk/n) M_{k,k-1}
 = O(k^3/n) e^{-(k-1)}(1+o(1))
 = o(e^{-k})`.                                               (4.5)

Equations (4.2)--(4.5) give (4.1). `square`

Consequently, if `k-log n->c`,

`E Z_n = n P(I_v) -> e^{-c}`.                               (4.6)

This answers the one-vertex multiplicative-constant question from the previous run: `c_0=1`.

---

## 5. B3 stronger target: fixed factorial moments, not only a second moment

The main remaining issue is dependence among isolated vertices. The previous source proof controls only two vertices through the event `B`; for a Poisson theorem we need every fixed factorial moment.

The useful fact is that, for any fixed number of roots, all non-product interactions are carried by a **sparse finite family of cross edges or label overlaps**. The same sparse-interaction mechanism from Claim 286 is therefore strong enough at constant scale once the one-root multiplicative saddle is known.

### Lemma 5.1 (fixed-root sparse-interaction decoupling)

Fix `r>=1`. For distinct vertices `v_1,...,v_r`, with `k=log n+O(1)`,

`P(I_{v_1}...I_{v_r}) = e^{-rk}(1+o(1))`.                   (5.1)

#### Proof — lower bound

Temporarily delete the `binom(r,2)` root-root edges when forming each root's preference order. The remaining incident edge families of the `r` roots are independent. For root `a`, let `S_a` be its first `k` labels among the `n-r` nonroot vertices.

By rank-label symmetry, the `S_a` are independent uniform `k`-subsets of the nonroot labels, independent of the numerical order statistics. Thus

`P(S_a are pairwise disjoint)=1-O_r(k^2/n)=1-o(1)`.          (5.2)

On the disjoint-label event put

`U={v_1,...,v_r} union S_1 union ... union S_r`.

For every `u in S_a`, retain only edges from `u` to `V\U`. There are

`N_r=n-r-rk=n+O_r(k)`

such edges, and these retained edge lists are pairwise disjoint over all selected neighbors and all roots. Let `D_a` be the event that each `u in S_a` has at least `k` retained edges below its target edge `(v_a,u)`.

Conditional on the root incident weights, the `D_a` are independent; by Lemma 3.1 with `m=n-r`, `N=N_r`,

`P(D_a)=e^{-k}(1+o(1))`.                                    (5.3)

The disjoint-label event is independent of the order-statistic values and changes only which iid edge lists are named. Therefore

`P(D_1...D_r, S_a disjoint)=e^{-rk}(1+o(1))`.               (5.4)

Choose `L=L(r)` so large that `L-1-log L>r+2`. On `D_1...D_r`, the event that some root kth incident weight exceeds `Lk/n` has probability `o(1)` by the same marked-saddle tail split used in Lemma 3.1. Add back the root-root edges. With conditional probability `1-O_r(k/n)=1-o(1)`, all of them exceed every root's kth threshold. On that event the selected sets remain the `S_a`, and every `D_a` is a sufficient condition for actual isolation regardless of the deleted cross edges, because each selected neighbor already has `k` competitors in `V\U`.

Hence

`P(I_{v_1}...I_{v_r}) >= e^{-rk}(1-o(1))`.                  (5.5)

#### Proof — upper bound

Work on the event that all root kth thresholds are at most `Lk/n`; its complement has probability `o(e^{-rk})` by the choice `L-1-log L>r+2`.

If the actual isolated-root configuration does **not** satisfy the disjointized events `D_1,...,D_r`, then at least one of the following finite interaction witnesses occurs:

1. a root-root edge lies among the first `k` edges of one endpoint;
2. two root preference sets share a label;
3. an edge joining a selected neighbor to another vertex of `U` occurs below the relevant target deadline.

There are `O_r(1)` possible witnesses of type 1, `O_r(k^2)` possible label coincidences of type 2, and `O_r(k^2)` candidate edges of type 3. On the bounded-threshold event, a specified type-1 or type-3 edge is early with probability `O_r(k/n)`, while by rank-label symmetry a specified pairwise selected-set overlap has total probability `O_r(k^2/n)`.

Condition on one such first witness and delete every other cross-block edge. For each root this can remove or pre-supply only `O_r(1)` rejection constraints/competitors. The ordered-deadline proof underlying Claim 286 is uniform under any fixed number of such omissions: for every fixed `D`,

`P(a root has all but at most D of its first k proposals rejected after at most D fixed competitor shifts)
 <= exp(-k+o(k))`.                                           (5.6)

After the cross-block deletion the relevant outside lists for distinct roots are disjoint, so the `r` factors in (5.6) multiply. Thus the contribution of every interaction witness is at most

`exp(-rk+o(k)) * O_r(k/n)`

for an edge witness, or

`exp(-rk+o(k)) * O_r(k^2/n)`

for a label-overlap witness. Summing `O_r(k^2)` possibilities gives

`P(I_{v_1}...I_{v_r}, some interaction witness)
 <= e^{-rk} n^{-1+o(1)} = o(e^{-rk})`.                       (5.7)

Outside the witness event, actual isolation forces all `D_a`, so (5.4) and (5.7) give

`P(I_{v_1}...I_{v_r})<=e^{-rk}(1+o(1))`.                    (5.8)

Combining (5.5) and (5.8) proves (5.1). `square`

**Why (5.6) is not a hidden new assumption.** Claim 286 proved, for every fixed `kappa`, the one-root bound `P(deg(v)<=kappa)<=exp[-k+epsilon sqrt(k)+o(sqrt(k))]` after choosing a fixed ordered-deadline cutoff. Conditioning a fixed number of prescribed internal competitors or omitting a fixed number of deadlines changes only that fixed `kappa`/threshold defect. The disjointized construction above makes the root blocks independent before multiplication. Thus (5.6) is exactly the fixed-defect form of the retained Claim-286 argument, not an appeal to unproved independence.

---

## 6. Poisson law for isolated vertices

Let

`Z_n=sum_{v=1}^n I_v`.

For every fixed integer `r>=1`, Lemma 5.1 gives

`E[(Z_n)_r]
 = (n)_r P(I_1...I_r)
 = (n)_r e^{-rk}(1+o(1))`.                                  (6.1)

If `k-log n->c`, then

`(n)_r e^{-rk} -> e^{-rc}`.                                 (6.2)

These are exactly the factorial moments of `Poisson(e^{-c})`. The Poisson law is moment-determinate, hence

`boxed{ Z_n => Poisson(e^{-c}). }`                           (6.3)

In particular,

`P(Z_n=0)->exp(-e^{-c})`.                                   (6.4)

---

## 7. Nontrivial components vanish in the same constant window

It remains to show that connectivity differs from the event `Z_n=0` by `o(1)`.

### 7.1 Fixed component sizes `2<=r<=6`

Choose a constant `L` with `L-1-log L>2`. By a union bound and the order-statistic Chernoff estimate,

`P(exists v: X_(k)(v)>Lk/n)
 <= n exp(-(L-1-log L+o(1))k)=o(1)`                          (7.1)

for `k=log n+O(1)`.

Work on this global threshold event. If a fixed `r`-set `S`, `2<=r<=6`, is a connected component, then it contains a spanning tree `T`. Every tree edge is bilaterally preferred, hence each such edge has weight at most `Lk/n`. The `r-1` tree edges are distinct independent uniforms, so conditioning on a particular tree costs at most

`(Lk/n)^(r-1)`.                                             (7.2)

After those `r-1` prescribed internal edges are exposed, every vertex of `S` has graph degree at most `r-1`. Delete all remaining cross-block interactions and apply the same fixed-defect ordered-deadline estimate as (5.6) to the `r` vertices. Since `r` is fixed, prescribed tree competitors account for only `O_r(1)` threshold shifts, and the remaining root blocks are disjoint. Therefore, for a fixed labeled `S` and fixed tree `T`,

`P(S is a component with tree T, global threshold event)
 <= (Lk/n)^(r-1) exp(-rk+o(k))`.                             (7.3)

There are at most `binom(n,r) r^(r-2)` choices of `S,T`. Hence

`P(exists r-component)
 <= n^r O_r(1) (k/n)^(r-1) e^{-rk+o(k)}+o(1)
 = n^{1-r+o(1)} k^{r-1} ->0`.                               (7.4)

This treats every fixed `2<=r<=6` directly; no mean-degree argument is used.

### 7.2 Sizes `r>=7`

Retain the exact source-compatible exponential-score/Cayley envelope proved in Claim 280. With `C=log(32/5)`, for every fixed `r` and `k=log n+O(1)`,

`P(exists r-component)
 <= binom(n,r) r^(r-2) p_tree^(r-1) (1-p_cross)^(r(n-r))`,

whose logarithm has leading coefficient

`(1-5r/32) log n + O_r(loglog n)`.                           (7.5)

Thus all fixed `r=7,...,12` vanish. Claim 278's uniform version of the same envelope excludes every size `13<=r<=n/2` uniformly in the present regime. Therefore

`P(exists component of size 2,...,floor(n/2)) ->0`.          (7.6)

---

## 8. Connectivity limiting law and exact source implication

A disconnected graph either has an isolated vertex or has a component of size between `2` and `n/2`. Therefore, by (6.4) and (7.6),

`P(LK(n,k) connected)
 = P(Z_n=0)+o(1)
 -> exp(-e^{-c})`.                                           (8.1)

This proves Claim 288.

Consequences:

1. if `k-log n -> +infinity`, the theorem plus monotonicity gives connectivity whp once the sequence is compared above any fixed `c`;
2. if `k-log n -> -infinity`, it gives disconnection whp by comparison below any fixed `c`;
3. for every finite limiting offset `c`, the exact limiting connectivity probability is `exp(-e^{-c})`;
4. the source's entire displayed Section-1.1 band is therefore mathematically resolved by a stronger `O(1)` theorem.

The result remains labeled **candidate complete / audits pending**, not protocol-closed, until two independent OTHER-track audits verify the full implication chain.

---

## 9. Adversarial self-audit and failure checks

I tried three ways to break the argument.

### 9.1 Could the marked integral have a second saddle near `x~k/n`?

No. In the beta-dual variable `x=mu+zk/N`, the low region has exponent controlled by `log z-z`; on `z<=1/2` it is separated from the beta-mean saddle by a fixed positive multiple of `k`. The fluctuation scale of the beta order statistic is only `sqrt(k)/n`, so it cannot repair that loss.

### 9.2 Could internal first-`k` edges change the multiplicative isolation constant?

No. On `X_(k)<=Lk/n`, two or more active internal edges have probability `O(k^6/n^2)=o(e^{-k})`. A single active edge can lower outside rejection thresholds by at most one; Lemma 3.1 shows that its total contribution is `O(k^3/n)e^{-(k-1)}=o(e^{-k})`.

### 9.3 Could finite-root dependence survive at order one?

The only ways for the disjointized root blocks to interact are root-root rank events, selected-label overlaps, and active cross edges. Their probabilities carry an additional `n^{-1+o(1)}` after the retained fixed-defect isolation cost. This is exactly why the pair obstruction from the old source proof disappears once one asks for the true joint event instead of the coarse bad-event necessary condition.

The weakest point that an independent audit should attack is Lemma 5.1's fixed-defect product passage (5.6)--(5.7): verify carefully that every interaction witness changes only `O_r(1)` root constraints before disjointization and that no hidden shared edge remains in the outside lists.

---

## 10. Directed P04/I0101 audit duty

The newest P04 report I recovered is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T10-50-12Z__stuck-recovery-sixrun-rotation-handoff.md`,

creation commit `0bae9b472059407291083f04a1c494490337b924`.

It explicitly creates **no new mathematical claim** and rotates I0101 to successor-admission hold after the CLOSABLE six-run rule. The preceding mathematical Claim 45 was already audited by P03 as `P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285`, and the prior P04 claims listed in the current task prompt have already been P03-audited.

Accordingly, there is **no genuinely new accessible P04 mathematical claim to audit this run**. I do not fabricate or repeat an audit.

---

## 11. Prior-art status and honesty boundary

Fresh bounded web queries on 2026-09-18:

- exact title/authors/DOI;
- `LK(n,k) Poisson isolated vertices bilateral preference`;
- `bilateral preference connectivity log n + c`;
- current Dabirian/Subramanian publications and the arXiv lineage.

Recovered: the current Cambridge 2026 paper and older arXiv version. No later theorem matching (6.3) or (8.1) was recovered. This is **not** a worldwide novelty certificate. Claim 288 therefore remains `PUBLICATION-NOVELTY-UNVERIFIED`.

The mechanism also has a classical analogue: once rare isolated-vertex indicators have asymptotically factorized fixed factorial moments and nontrivial components vanish, the limiting connectivity law is the Renyi/Erdos--Renyi form. What is new here, if it survives external audit/prior-art checking, is the source-specific beta-marking and sparse-interaction proof for the bilateral preference model.

---

## 12. Exact remaining obligations / next state

Mathematical source target: **candidate complete** by Claim 288.

Protocol closure obligations remain:

1. obtain the P26 independent full-proof audit;
2. obtain one additional distinct OTHER-track end-to-end audit (the directed inbound lane is P02 -> P03 under the fleet table, subject to current availability);
3. adversarially recheck Lemma 5.1's finite-root disjointization and fixed-defect factorization against the literal source edge lists;
4. after two audit passes, package a self-contained paper folder comparing Claim 288 line-by-line with source Section 1.1 and recording the bounded prior-art search.

No rotation occurs now: closure is not certified until the audit requirements are met.

---

## 13. `ledger_delta` for P26

Requested shared-ledger reconciliation only; P03 does not edit shared root ledgers.

- Track: `P03`.
- Canonical claim: `P0456` (Dabirian--Subramanian, Section 1.1 connectivity window).
- New claim: `P03-P0456-POISSON-CRITICAL-WINDOW-288`.
- Mathematical status: `PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- New theorem: if `k_n-log n -> c`, then isolated-vertex count `Z_n => Poisson(e^{-c})` and `P(connectivity)->exp(-e^{-c})`.
- One-vertex constant: `P(I_v)=e^{-k}(1+o(1))` for `k=log n+O(1)`.
- Existing fixed-coefficient metrics remain saturated at zero; no stuck count is attached to saturation.
- New limiting-law parameter: `lambda_LK(c)=e^{-c}`.
- Activity: `ACTIVE_AUDIT_PENDING`; do not rotate or mark CLOSED until two independent OTHER-track audits pass.
- Directed P03->P04 duty: no new P04 claim existed after the 10:50:12Z handoff, so no redundant audit was created.

---

## 14. Model / tool limitations

Requested model: GPT-6, reasoning maximum. Actual exposed runtime for this report: **GPT-5.6 Sol; reasoning level UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The task-control interface still exposes title/prompt, timing mode, schedule/relative start, and enabled state, but no model-family selector or reasoning-effort selector. A real change requires the owning scheduler/workspace/API layer to expose and persist those fields and return applied-runtime telemetry. Permission denial must be handled only through the owning context/admin/support; no duplicate-task or permission-bypass workaround is authorized.

GitHub is the only delivery destination used. No Gmail/email, Drive, public posting, paid compute, access changes, unreviewed external scripts, or workflow execution were used.

**End of complete run report.**

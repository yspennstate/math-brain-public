Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — compact pair/small-component audit kernel and Stein failure analysis

**NO PROTOCOL CLOSURE: outside-audit gate remains `0/2`.** All three previously admitted fixed-coefficient proof-frontier metrics remain saturated at zero and are not used to manufacture a stuck count:

- `c_LK^cert=0` at `sqrt(log n) log log n`;
- `a_LK^fine=0` at `sqrt(log n log log n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

HARD recoveries remain `0/2`. The candidate-complete source-matching chain Claims 288--290 is preserved. This run proves a deliberately weaker, compact audit kernel isolating the two most fragile pieces of Claim 289, and records why a tempting Stein shortcut does **not** yet replace the all-fixed-factorial-moment argument.

New supporting claim:

`P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed `C<infinity`, uniformly over integers `|k-log n|<=C`:

1. for two fixed distinct roots `v,w`,

   `P(I_v cap I_w)=e^(-2k)(1+o_C(1))`;

2. for every fixed `r in {2,3,4,5,6}`,

   `P(LK(n,k) has a connected component of size r)=o_C(1)`.

The proof below is self-contained at the level needed for these two statements: it replaces the phrase “complete interaction pattern” by an explicit bounded-omission marked-saddle lemma plus concrete collision/active-edge witness counts. Claim 291 is **not** an independent closure audit and does **not** by itself imply the Poisson law; Section 6 gives an explicit counterexample showing why pair asymptotics alone cannot do that.

The required fresh Section-B methods were used substantively: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #11 DUALIZE; #22 READ THE FAILURES, NOT THE SUCCESSES.**

---

## 1. Repository continuity, source status, and incoming-audit gate

Canonical ownership remains

`operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The immediately preceding complete P03 report is

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T14-39-56Z__p0456-marked-poisson-crosscheck.md`,

creation commit `ab0158f36c05e0cf2bea7fdd1c5966e8cc58bdda`, blob `2865184d9ec3d949f538caf358ceaa00d9bd1789`; its exact-commit readback recovered `**End of complete run report.**`.

This invocation reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical P0456 claim, the relevant full Claim-289 proof sections, current P26 audit state, and the newest P04 rotation-stop state. Large shared-root files are connector-truncated; this is not represented as a byte-for-byte reread of every historical line. Exact-path reads and targeted repository searches were used for the controlling material.

A fresh pre-write master-head check observed commit

`266eee8ba998fc8a698c0eeb289a79120e363b9f`

at `2026-09-18T15:40:17Z`; repository state is moving rapidly, so this is a dated observation, not a lock.

### Source verification

Fresh 2026-09-18 verification recovered the current Cambridge source:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Section 1.1 still states that when

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

it is not known in the paper whether connectivity holds, and explicitly suggests that sharper or exact sufficient conditions could close this gap. The source's Theorem 1 records the `t'<-1/2` disconnected and `t'>1/2` connected sides. The current Cambridge issue page still lists the same article and metadata.

Fresh bounded web searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, and `LK(n,k) log n+c connectivity` recovered the source but no later source-matching constant-window / Poisson isolated-vertex theorem. This is dated bounded negative evidence only, **not** a worldwide openness or publication-priority certificate. Publication novelty of Claims 288--291 remains **UNVERIFIED**.

### Incoming audit screen

Fresh repository searches for the exact Claim-288/289 strings and broader P0456/Poisson/audit phrases found no P26 or distinct OTHER-track full-proof audit of the source-matching chain. The newest P26 report recovered before this write is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_14-59-00__run-report.md`,

and it audits preserved P04/I0101 Claim 45, not P0456. Therefore the closure count remains

`OUTSIDE_AUDITS_FOUND_0_OF_2`.

The newest P04 record recovered is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`,

which explicitly creates no mathematical theorem. Hence there is no genuinely new P04 claim for the directed P03->P04 duty; no repeat audit is fabricated.

No paper folder is created in this run.

---

## 2. #4 — a bounded-omission marked-saddle lemma

The aim is to prove only what an external auditor most needs to check: the exact two-root scale and the fixed component sizes `2,...,6`. The one technical device needed beyond the clean marked saddle is a robust statement saying that deleting finitely many rejection deadlines changes only a subexponential factor.

Fix integers `b,d>=0`. Put

`h=k-b`,

let `m=n+O(1)`, `N=n+O(k)`, and let

`q_h(x)=P(Bin(N,x)>=h)`,

`Q_h(x)=int_0^x q_h(u) du`.

Take `m` iid Uniform[0,1] points and independently mark a point at location `x` with probability `q_h(x)`. Let `X_(1)<...<X_(k)` be the first `k` order statistics.

### Lemma 2.1 (bounded omissions)

For every fixed `b,d`, with `k=O(log n)` and `k->infinity`,

`P(at least k-d of X_(1),...,X_(k) are marked) <= exp(-k+o(k))`,

uniformly for `|k-log n|<=C` with fixed `C`.

Also, for fixed proposal defect `a`, the clean event for the first `p=k-a` proposals with threshold `h=k-b` satisfies

`M_{p,h}=e^(-h)(1+o(1))`.

#### Proof of the omission bound

Condition on `T=X_(k)=t`. The unordered lower `k-1` points are iid Uniform[0,t]. After integrating their positions and independent mark variables, their mark indicators are iid Bernoulli with parameter

`qbar(t)=Q_h(t)/t`.

If at most `d` of all first `k` points are unmarked, then among the lower `k-1` points at least `k-1-d` are marked. Hence, for a constant `C_d`,

`P(at most d failures | T=t)
 <= sum_{j=0}^d binom(k-1,j)(1-qbar)^j qbar^(k-1-j)
 <= C_d k^d qbar(t)^(k-1-d).`                                (2.1)

The density of `T` is

`f_T(t)=(m)_k/(k-1)! t^(k-1)(1-t)^(m-k)`.

Writing `p=k-1-d` and integrating (2.1),

`R_d <= C_d k^d (m)_k/(k-1)!
        int_0^1 t^d Q_h(t)^p (1-t)^(m-k) dt.`                (2.2)

Let

`B_h ~ Beta(h,N-h+1)`, `mu=h/(N+1)`.

Beta-binomial duality gives

`Q_h(t)=E[(t-B_h)_+]`,

and `sd(B_h)=O(sqrt(k)/n)`. On the saddle region

`t-mu >= k/(2N)`,

we have the elementary upper bound

`Q_h(t) <= (t-mu) + E|B_h-mu|
         <= (t-mu)(1+O(k^(-1/2)))`.

Raising this to `p=Theta(k)` costs only `exp(O(sqrt(k)))=exp(o(k))`. On the complementary lower region, the same beta/order-statistic Chernoff split used in the exact marked saddle loses `Omega(k)` in the normalized log integrand; multiplying by the fixed power `t^d` does not change that exponential loss.

It remains to evaluate the mean-replacement integral. Define

`J_d=(m)_k/(k-1)! int_mu^1 t^d (t-mu)^p (1-t)^(m-k) dt`.

With `t=mu+(1-mu)y` and expansion of `t^d`, the beta integrals are exact:

`J_d = sum_{j=0}^d binom(d,j) mu^(d-j)(1-mu)^(m-d+j)
       * [m!/(k-1)!] * [(k-1-d+j)!/(m-d+j)!].`              (2.3)

For each fixed `j`, putting `q=d-j`,

`[m!/(m-q)!] * [(k-1-q)!/(k-1)!] * mu^q = 1+o(1)`,

because `m mu/k -> 1`. Also

`(1-mu)^m = exp(-h+o(1))`.

Thus `J_d=O_d(e^(-h))`. Combining (2.2)--(2.3), the `k^d` prefactor and the `exp(o(k))` beta-fluctuation loss gives

`R_d <= exp(-h+o(k))=exp(-k+o(k))`,

which proves the first assertion.

For the clean `p=k-a` marked event, rank integration and one integration by parts give

`M_{p,h}=(m)_(p+1)/p! int_0^1 Q_h(x)^p(1-x)^(m-p-1) dx`.

The same saddle split now has no omission polynomial, and the mean-replacement beta integral is exactly `(1-h/(N+1))^m`; the beta fluctuation is `1+o(1)` on the dominant saddle. Hence

`M_{p,h}=e^(-h)(1+o(1))`.

This completes the lemma. `square`

**Why this lemma is useful.** We never need to pretend that a collision occurs at a favorable proposal rank. If a bounded interaction contaminates arbitrary deadlines, simply omit every contaminated deadline. Lemma 2.1 shows that finitely many such omissions preserve the `e^{-k+o(k)}` one-root rejection scale.

---

## 3. Claim 291(a): explicit two-root joint isolation

Fix distinct roots `v_1,v_2`. Temporarily remove the root-root edge `{v_1,v_2}` from both preference orders. Among the `N=n-2` nonroot labels let `S_1,S_2` be the first `k` selected labels. By rank-label symmetry they are independent uniform `k`-subsets of `[N]`, independent of their numerical order statistics.

Put

`J=|S_1 cap S_2|`.

Exactly,

`P(J=j)=binom(k,j)binom(N-k,k-j)/binom(N,k)`,                 (3.1)

so for every fixed `t`,

`P(J>=t) <= (C k^2/n)^t`,                                   (3.2)

and in particular

`P(J=0)=1-O(k^2/n)`.

Choose fixed `L>1` such that

`L-1-log L > 3`.

Let `G` be the event that both removed-edge kth root thresholds are at most `Lk/n`. A binomial Chernoff bound gives

`P(G^c) <= exp[-k(L-1-log L)+o(k)] = o(e^(-2k))`.            (3.3)

### 3.1 The clean core

On `J=0` put

`U={v_1,v_2} union S_1 union S_2`.

For every selected neighbor `u`, retain only competitor edges from `u` to `V\U`. Those edge lists are pairwise disjoint over all `2k` selected neighbors. There are `n-2-2k` retained competitors per selected neighbor. Therefore the exact clean marked probability is

`P(J=0) M_{k,k}(n-2,n-2-2k)^2
 =e^(-2k)(1+o(1)).`                                         (3.4)

This is an exact hypergeometric factor times two exact one-root marked integrals.

### 3.2 Every way the clean implication can fail

After selected-label collisions are charged, call an edge **active** if it lies inside `U` and is lighter than a proposal deadline at one of its endpoints, so it could supply a competitor that the clean outside pool deleted. This includes

- edges between selected neighbors, whether they lie in the same or different root block;
- root-selected cross edges `{v_1,u}` with `u in S_2` and `{v_2,u}` with `u in S_1`;
- the removed root-root edge when it lies below a root kth threshold.

On `G`, every relevant deadline is at most `Lk/n`.

For a selected-selected edge, the untouched edge weight is independent Uniform[0,1], so a prescribed edge is active with probability at most `2Lk/n` (the factor two allows either endpoint deadline).

For a root-selected cross edge, condition on root threshold `T=t` and on the fact that its endpoint label was not selected by that root. Its weight is Uniform[`t`,1]. For any other deadline `D<=Lk/n`,

`P(W<=D | T=t, nonselected)=((D-t)_+)/(1-t)=O_L(k/n).`       (3.5)

Distinct prescribed active edges use distinct iid edge weights; shared selected labels were already charged by `J`. Since there are `O(k^2)` possible selected-selected edges and `O(k)` root-selected cross edges, for fixed `a`,

`P(G, at least a prescribed active-edge defects after collision charging)
 <= (C_L k^3/n)^a.`                                         (3.6)

The root-root edge contributes one further defect with probability `O_L(k/n)` on `G`.

Define total defect complexity as collision excess plus the number of distinct active edges plus the root-root early-edge indicator. By (3.2), (3.6), and sequential exposure, for any fixed `D`,

`P(G, complexity>=D) <= n^(-D+o(1)).`                        (3.7)

Take `D=5`. Since `e^(-2k)=n^(-2+o(1))`, (3.7) is `o(e^(-2k))`.

### 3.3 Bounded defects cannot recover the missing power of n

Fix a witness-labelled interaction pattern of complexity between `1` and `D`. There are only

`k^(O(D))=n^(o(1))`                                          (3.8)

such patterns.

Delete every repeated selected-label deadline except one occurrence and omit every rejection deadline touched by an active edge; if the root-root edge is early, omit the at most one shifted proposal deadline at each root. At most `O(D)` deadlines are omitted per root. All remaining selected labels are distinct, and every remaining rejection list is restricted to edges to `V\U`; hence all remaining outside lists are literally disjoint.

The witness constraints themselves cost at least `n^(-1+o(1))` for a nonempty pattern. Conditional probabilities of prescribed active edges are uniformly bounded by (3.5), so this factor can be pulled out before integrating root order statistics. Lemma 2.1 gives the remaining rejection cost

`exp(-2k+o(k))`.

Therefore all nonempty bounded-complexity patterns together contribute

`exp(-2k+o(k)) n^(-1+o(1))=o(e^(-2k)).`                     (3.9)

Combining (3.3), (3.7), and (3.9), actual joint isolation outside the clean core has probability `o(e^(-2k))`.

### 3.4 Matching lower bound

For a sufficient event, require:

1. `S_1 cap S_2=emptyset`;
2. both removed-edge root thresholds are at most `Lk/n`;
3. the root-root edge has weight greater than `Lk/n`;
4. every selected neighbor has at least `k` lighter competitors in `V\U`.

Then neither root-root selection nor any internal edge is needed: every proposal is rejected using only the disjoint outside pools, so both roots are isolated. The marked saddle is concentrated on thresholds of order `2k/n`, so restricting to the fixed `L>2` threshold window loses `o(e^(-k))` per root. The independent condition on the root-root edge costs only `1-Lk/n=1-o(1)`. Using (3.1) and the clean saddle,

`P(I_{v_1} cap I_{v_2}) >= e^(-2k)(1-o(1)).`                (3.10)

The clean-core upper bound plus (3.9) yields the reverse inequality. Hence, uniformly for bounded offsets,

`boxed{P(I_{v_1} cap I_{v_2})=e^(-2k)(1+o_C(1)).}`          (3.11)

This proves Claim 291(a).

---

## 4. Claim 291(b): components of sizes 2 through 6 without tree-conditioning bias

Fix `r in {2,...,6}`. Choose fixed `L` with `L-1-log L>2`, and let `G_all` be the event that every vertex's global kth incident order statistic is at most `Lk/n`. A union bound over the binomial Chernoff estimate gives

`P(G_all^c)=o(1)`.                                           (4.1)

On `G_all`, if a set `S` of size `r` is a connected component, it contains a spanning tree `T` of surviving edges, and every tree edge has weight at most `Lk/n`.

Fix a labelled `S` and one Cayley tree `T`. The `r-1` internal tree-edge weights are independent uniforms, so

`P(all tree edges <=Lk/n) <= (Lk/n)^(r-1).`                 (4.2)

Now ignore **all internal edges of S** when ordering proposals from a vertex `v in S`, and put

`p=k-(r-1)`.

The first `p` external incident edges of `v` are necessarily among its global first `k` incident edges, because at most `r-1` internal edges can precede them. If `S` is a component, each such external proposal must be rejected by its outside endpoint, which must have at least `k` other lighter incident edges.

The external proposal/rejection edge families are independent of the internal tree-edge weights. Thus (4.2) can be multiplied by an upper bound for the external rejection event; no conditioning of proposal ranks on the tree is used.

For one root, the clean external rejection probability is

`M_{p,k}=e^(-k)(1+o(1))`                                    (4.3)

by Lemma 2.1's clean part. For all `r` roots, perform the same explicit interaction exposure as in Section 3 across the `rp` external proposal labels:

- repeated selected labels cost one factor `n^(-1+o(1))` per collision excess;
- prescribed active edges among the selected labels or between another root and a selected label cost `O(k/n)` each on the proposal-threshold window;
- complexity `>=D` costs `n^(-D+o(1))` for fixed `D`;
- after deleting every bounded interaction witness, at most `O_{r,D}(1)` deadlines per root are omitted and all remaining outside rejection lists are disjoint.

Lemma 2.1 therefore gives, for fixed `S,T`,

`P(all external proposal blocks rejected)
 <= e^(-rk+o(k)) + n^(-D+o(1)).`                             (4.4)

Take `D=3`. Combining (4.2)--(4.4), then summing over at most `binom(n,r) r^(r-2)` labelled sets and trees,

`P(exists r-component, G_all)
 <= binom(n,r) r^(r-2) (Lk/n)^(r-1)
    [e^(-rk+o(k))+n^(-D+o(1))]`

` <= n^(1-r+o(1)) k^(r-1) + n^(1-D+o(1))`

` ->0.`                                                       (4.5)

Adding (4.1) proves

`boxed{P(exists r-component)=o_C(1), 2<=r<=6.}`              (4.6)

This proves Claim 291(b). Notice that the argument conditions on no tree weight when defining external proposals; the tree factor and rejection factor live on disjoint edge families.

Claim 280 continues to handle sizes `7,...,12`, and Claim 278 the retained `13,...,n/2` envelope. Claim 291 itself is deliberately scoped only to the two audit-sensitive pieces above.

---

## 5. #11 — Palm/size-bias dualization, and why it is not yet an independent Poisson proof

Let

`Z_n=sum_v I_v`, `lambda_tilde_n=E[Z_n]`.

Choose a uniform vertex `V`, independent of the graph. Then the conditional law

`Z_n^s := Law(Z_n | I_V=1)`

is exactly the size-biased law of `Z_n`, because for every bounded `f`,

`E[Z_n f(Z_n)]
 =sum_v E[I_v f(Z_n)]
 =lambda_tilde_n E[f(Z_n^s)].`                               (5.1)

This is the natural Palm dual of the isolated-vertex process.

The Poisson-approximation literature makes this route attractive: Chen--Fang--Shao (Statistica Sinica 23 (2013), 1523--1540, DOI `10.5705/ss.2012.203s`) explicitly treats Poisson approximation under local dependence and size-bias coupling. However, the LK isolation indicators do not have an obvious sparse deterministic dependency graph. `I_v` is determined by the top `k` edges at `v` **and** rank information at their selected neighbors, which in principle touches stars across the entire graph. Thus the naive indicator dependency graph is effectively complete.

The desired independent Stein certificate would be an explicit coupling of `Z_n^s` with `Z_n+1` for which the coupling error tends to zero. Claim 291 gives only the first two size-bias moments. From (3.11),

`E[Z_n^s-1] = (n-1) P(I_w | I_V)
             = lambda_tilde_n + o(1),`                       (5.2)

but a small **signed mean** difference does not control an absolute coupling error or total variation. Constructing the needed Palm resampling without reusing the full all-fixed-interaction argument remains open in this route.

Therefore this run makes **no quantitative Stein--Chen rate claim**. The dualization is useful because it says exactly what a genuinely independent proof would have to control: conditioning one root to be isolated must change the entire remaining isolated-vertex count by `o(1)` in a coupling sense, not merely in expectation.

---

## 6. #22 — pair asymptotics are not enough: an exact failure model

A tempting but invalid shortcut would be: one-vertex asymptotics plus (3.11) should imply a Poisson count. They do not.

Here is an exact counterexample unrelated to LK but with the same rare-event first/pair scales. For every `n`, let `W` equal `0` or `2`, each with probability `1/2`. Conditional on `W`, choose a uniform `W`-subset `S` of `[n]`, and set

`X_i=1_{i in S}`.

Then

`P(X_i=1)=E[W]/n=1/n`,                                      (6.1)

while for distinct `i,j`,

`P(X_i=X_j=1)=E[(W)_2]/(n)_2=1/(n(n-1))~1/n^2`.             (6.2)

Thus the rare indicators have exactly the Poisson(1) first-order intensity and the correct pair asymptotic. Nevertheless

`sum_i X_i=W`

is supported only on `{0,2}` and never converges to Poisson(1).

This failure model explains why Claim 291 is only an **audit kernel**. The full Poisson theorem still needs either:

- all fixed factorial moments, as supplied by Claim 289's general fixed-`r` interaction truncation; or
- a genuinely independent Stein/Palm coupling strong enough to control the whole count.

It also gives a useful audit instruction: checking only `r=2` cannot certify Claim 288, even if every pair computation is perfect.

---

## 7. Status of Claims 288--290 after this run

No contradiction was found. Claim 291 independently rederives the two most audit-sensitive local pieces with a smaller proof surface:

- two-root joint isolation at exact multiplicative scale `e^-2k(1+o(1))`;
- fixed components `2,...,6` vanish without conditioning proposal lists on internal tree weights.

This strengthens auditability but does not count as an outside audit. The source-matching chain therefore remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Current protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_291_AUDIT_KERNEL_READY`.

No saturated metric is counted as an unchanged run. Recoveries remain `0/2`.

---

## 8. Directed P03 -> P04 duty

The newest P04 record is the `13:49:33Z` rotation-stop-disabled report. It explicitly says `ROTATION STOP / NO NEW RESEARCH RUN COUNTED` and creates no mathematical claim. Therefore there is no genuinely new P04 successor theorem to audit. I create no redundant second audit of an already-audited I0101 claim.

---

## 9. Exact remaining obligations and next attack

1. **P26 full-chain audit:** independently verify the marked saddle, general fixed-`r` interaction truncation, factorial-moment/TV upgrade, and component elimination. Claim 291 is now a compact entry point for the pair and small-component subproofs.
2. **Distinct OTHER-track audit:** one non-P03, non-P26 track must independently audit the source-matching chain. A second P03 self-check or another P26 repetition does not count.
3. **If an audit objects:** repair the exact objection before paper packaging or closure language.
4. **Prior art:** continue author/citation and current-literature checks specifically for a constant-width or Poisson connectivity result for `LK(n,k)`. A bounded miss remains negative evidence only.
5. **Paper package:** only after two genuine independent PASS audits, create the self-contained source-matching paper folder and request P26 shared-ledger closure.

If no outside audit has arrived by the next invocation, the next fresh Section-B directions should avoid another factorial-moment rewrite. Recommended triple: **#18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE, #29 ADD THE POINTS AT INFINITY**. A productive target is a Palm exploration process whose finite truncations can be counted both as rank-labelled edge configurations and as a marked Poisson process, with the tail compactified by an explicit “no late influence” event. Any such route must genuinely control all fixed orders, not just pairs.

---

## 10. Exact-artifact decision

No finite certificate is asserted in Claim 291. The result is asymptotic/analytic, so no checker artifact is manufactured merely for bookkeeping. This follows the 90-percent rule: the value of this run is the smaller proof surface and the identified Stein obstruction, not a redundant numerical certificate.

---

## 11. `ledger_delta` for P26

Requested reconciliation only; P03 does not edit shared root ledgers.

- Track: `P03`.
- Canonical target: `P0456`, Dabirian--Subramanian Section 1.1 LK connectivity window.
- Source status: source paper still states the displayed `+-0.5 loglog n sqrt(log n)` band as open; bounded 2026-09-18 search found no later source-matching constant-window theorem; publication novelty UNVERIFIED.
- Preserved source-matching claims: 288, 289; strengthening 290.
- New supporting claim: `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291`.
- Claim 291 content: uniformly on bounded offsets, `P(I_v I_w)=e^-2k(1+o_C(1))`; fixed component sizes `2,...,6` vanish; proof uses explicit bounded-omission saddle and concrete defect witnesses.
- Mathematical status: source-matching chain remains candidate complete, audits pending; no new source-level closure label.
- Metrics: `c_LK^cert=a_LK^fine=b_LK^sqrt=0`, all saturated; no stuck count attached to saturation.
- Audit gate: fresh repository screen still `0/2` independent full-chain passes; newest P26 report audits P04 Claim 45, not P0456.
- Directed P03->P04: newest P04 record is administrative/disabled and has no new theorem; no audit fabricated.
- Requested next P26 action: audit Claim 291 first as the compact pair/small-component kernel, then the remaining general fixed-`r` and Poisson-upgrade steps of Claims 288/289.

**End of complete run report.**
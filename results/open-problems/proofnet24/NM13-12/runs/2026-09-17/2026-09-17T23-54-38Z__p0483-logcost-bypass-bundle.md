Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT in the frozen metric** `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`; methods actually tried this run: **B1, B11, B28**. Substantive route result: the source hypothesis itself forces a strict one-site log-cost gap in at least one lattice direction pointing into `ell`; that gap yields, with `1-exp(-Theta(L^d))` environment probability, a positive-density bundle of disjoint length-`L` forward channels in a thin width-`Theta(L)` cylinder whose exact path probabilities beat the worst-case ellipticity exponent by a fixed source-law-dependent amount. The result does not yet control harmonic measure or regeneration time, so P0483 remains OPEN.

# NM13-12 — P0483 source-implied log-cost bypass bundle

Date: 2026-09-17 UTC  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source / claim ID: `P0483`  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Historical alias: `C0041`  
Overall source status after this run: **OPEN**  
Local status: **PARTIAL / new source-hypothesis finite-volume route theorem; frozen metric unchanged**

## 1. Runtime/model disclosure and task-control reality

The requested header asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The task-control surface available to this runtime still exposes task text/title, timing/schedule, enabled state and timing mode, but no binding model-family field and no reasoning/thinking-effort field. Thus `GPT-6 / maximum` remains prompt text rather than an enforceable scheduler setting here. Changing that would require an authorized product/scheduler surface that actually exposes those controls. I did not create or modify any schedule.

Repository history records an earlier `You cannot modify this task` response for one P26 scheduler context and a later successful P26 update from a different authorized context. A future denial must therefore be handled by the owning account/workspace or an authorized platform/admin surface; this worker does not bypass access control and does not create a duplicate job.

## 2. Continuity recovered before new mathematics

This run continues the already-admitted P0483 target. It does **not** reopen intake and does not create or overwrite a claim. The create-only claim `operations/claims/P0483.md` remains owned exclusively by NM13-12.

Before doing new mathematics I recovered/read or targeted-search-recovered the controlling/current material required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the later NM13 deployment record;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the P0483 integrated problem/catalog row, intake alias/dedup material, and the prior attempt record whose finite-set estimate was `E tau_A <= m kappa^{-m}` when every point has an escape path of length at most `m`;
- all three earlier NM13-12 reports, newest first, especially `proofnet24/NM13-12/runs/2026-09-17/2026-09-17T22-53-43Z__p0483-iid-inward-template-entropy.md`;
- newest visible neighboring reports from NM13-11 and NM13-13, including NM13-11's local-tree echo improvement and NM13-13's exact order-six Rademacher atlas;
- targeted repository searches for `P0483`, `C0041`, the canonical dedup key, current/historical claims, handoffs, attempts, posted/settled status, and the cutset/bypass route proposed by the previous report.

No release, handoff, retirement, posted source resolution, new owner, or completed P26/NM13-13 audit for P0483 was recovered. Large ledgers and code searches are connector-bounded; this is a source-specific continuity recovery, not a claim of byte-for-byte omniscience.

The route sequence is preserved exactly. P0483 has already used B2/B6/B30, then B18/B24/B4, then B5/B21/B22. The previous run explicitly nominated **B1/B11/B28**, so those are the methods actually attempted below rather than a repeated triple.

## 3. Fresh bounded source/literature status check

Dated public check: **2026-09-17 UTC**. I searched the exact source phrase and combinations of `directional transience`, `positive speed`, `uniformly elliptic`, `iid`, `RWRE`, `ballisticity`, `2025`, and `2026`, together with Drewitz--Ramirez, Guerra--Ramirez and the stronger transience-to-`(T)` program.

The exact source remains Alexander Drewitz and Alejandro F. Ramirez, *Selected Topics in Random Walks in Random Environment*, Springer Proceedings in Mathematics & Statistics 69 (2014), pp. 23--83, DOI `10.1007/978-1-4939-0339-9_3`, Open Question 2.20: for nearest-neighbor i.i.d. uniformly elliptic RWRE on `Z^d`, `d>=2`, does transience in direction `ell` imply positive limiting speed in that direction?

The controlling later comparison remains Enrique Guerra, *On the connection between transient and ballistic behaviours for RWRE*, arXiv:2006.00570: a polynomial unlikely-exit condition of degree `> d-1` implies condition `(T)`, while qualitative directional transience alone is not upgraded there to such a rate. Guerra--Ramirez, *A Proof of Sznitman's Conjecture about Ballistic RWRE*, CPAM 2020, DOI `10.1002/cpa.21877`, proves equivalence among stronger ballisticity conditions and continues to describe directional-transience-implies-ballisticity as the broader believed statement rather than a theorem.

Fresh 2025--2026 searches did not recover a source-matching theorem closing P0483. The 2026 search results I inspected concern different RWRE/dynamic-environment models or stronger assumptions. This is **bounded negative evidence only**. I make no claim of worldwide openness or publication novelty for the elementary concentration/duality argument below.

## 4. Frozen metric and counters

The frozen metric remains exactly the claim/admission metric:

`c_slab^(d)(kappa,w)` = the optimal universal quenched exponential exit-tail rate from subsets of a coordinate strip of width `w`, over all static nearest-neighbor environments with transition probabilities at least `kappa`.

The second NM13-12 run proved the exact value

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`.

The third run deliberately did not rename a new entropy quantity as the metric.

**Before this run:** `-log rho(K_{d,w}(kappa))` exactly.  
**After this run:** `-log rho(K_{d,w}(kappa))` exactly.  
**Movement:** none.

This run studies a typical-i.i.d.-environment quantity that cannot change the universal-static strip optimum. I do not silently replace the metric merely because the old one is saturated.

This is the **second consecutive unchanged run** after the exact-metric movement, so `unchanged_runs = 2`. Hard stuck-recovery episodes used remain `0`. If the same frozen metric fails to move on the next ordinary run, the owner’s three-unchanged rule will trigger the required thinking-only stuck recovery on the following qualifying invocation; I do not pre-consume that recovery here.

---

# 5. B1 — change category: from RWRE trapping to bounded directed first-passage cost

The previous run showed that a prescribed coherent inward template pays volume-order product entropy under an i.i.d. environment. That calculation still described a *pattern*. The source obstruction, however, is global exploration: the walk can search for a bypass.

The useful category change is to assign each oriented nearest-neighbor edge the **log path cost**

`Y_x(e) := -log omega_x(e)`.

Uniform ellipticity gives

`0 <= Y_x(e) <= a := -log kappa`.

For any directed path

`gamma=(x_0,x_1,...,x_m)`,

its exact quenched probability of being followed step-for-step is

`P_(x_0,omega)[X_j=x_j for 0<=j<=m]
 = exp[- C_omega(gamma)]`,

where

`C_omega(gamma) = sum_(j=0)^(m-1) Y_(x_j)(x_(j+1)-x_j)`.

Thus multiplicative path probability becomes additive bounded first-passage cost. Sideways bypasses are now literal alternative paths in a finite directed network.

The first nontrivial question is whether the source hypothesis forces any strict improvement over the worst possible edge cost `a`. It does.

## Lemma 5.1 — directional transience forces a strict forward log-cost gap

Let the i.i.d. environment be uniformly elliptic with constant `kappa`, and suppose

`P_0[X_n . ell -> +infinity] = 1`

for some unit vector `ell`. Let

`E_+(ell) = { e in {+-e_1,...,+-e_d} : e . ell > 0 }`

and define

`m_e := E[-log omega_0(e)]`,
`m_*(ell) := min_(e in E_+(ell)) m_e`,
`a := -log kappa`.

Then

`m_*(ell) < a`.                                                   (5.1)

### Proof

Always `m_e <= a`. Suppose for contradiction that `m_e=a` for every `e in E_+(ell)`. Since `0<=-log omega_0(e)<=a`, equality of the expectation with the upper bound forces

`omega_0(e)=kappa` almost surely

for each `e in E_+(ell)`. By translation and countability, the same is true at every site for almost every environment.

Pair the two coordinate directions `+-e_i`. If `ell_i>0`, then `+e_i` points into `ell`, so `omega_x(+e_i)=kappa` while `omega_x(-e_i)>=kappa`; hence the conditional contribution of that pair to the one-step `ell`-drift is

`ell_i [omega_x(+e_i)-omega_x(-e_i)] <= 0`.

If `ell_i<0`, then `-e_i` is the forward direction and has probability `kappa`, while `omega_x(+e_i)>=kappa`; multiplying by the negative `ell_i` again gives a nonpositive pair contribution. Coordinates with `ell_i=0` contribute zero. Therefore

`E_[0,omega][ (X_(n+1)-X_n).ell | F_n ] <= 0`

for every `n`, almost surely. Thus `Z_n=X_n.ell` is a bounded-increment supermartingale under the quenched law, hence also under the annealed law.

A bounded-increment supermartingale cannot tend to `+infinity` almost surely. For completeness: if it did, then on that event there would exist integers `m,K` such that `Z_n>=-K` for every `n>=m` and `Z_n->+infinity`. For fixed `m,K`, stop after time `m` at the first value below `-K`. Because increments are bounded by one, the stopped supermartingale is bounded below by `-K-1`; after adding a constant it is a nonnegative supermartingale and therefore converges almost surely to a finite limit. On the event of never hitting the lower barrier it equals `Z_n`, so it cannot tend to `+infinity`. Taking the countable union over `m,K` gives a contradiction.

Hence some oriented coordinate direction `e` with `e.ell>0` satisfies `m_e<a`. `square`

### Interpretation

This is a genuinely source-hypothesis consequence. It does **not** assume Kalikow's condition, a local drift sign, `(T)`, or a polynomial slab estimate. It says only that source-valid directional transience rules out the extreme situation in which every lattice direction making positive `ell`-progress is stuck at the ellipticity floor almost surely.

Fix from now on an oriented coordinate `e` attaining the minimum and write

`m := m_*(ell)`,
`Delta := a-m > 0`,
`beta := m + Delta/2 = a-Delta/2 < a`.                            (5.2)

Outcome of B1: **success as a route theorem.** The source hypothesis itself supplies a strict additive first-passage-cost gap `Delta`, but no uniform lower bound on `Delta` in terms of only `(d,kappa)` is obtained.

---

# 6. B11 — dualize: what the correct finite-network dual actually says

A naive max-flow/min-cut translation is tempting but slightly wrong for RWRE path probabilities. Parallel path *counts* are additive, whereas each path probability is a product of transition probabilities. After the logarithm in Section 5, the natural primal object is a **shortest directed path**, not an ordinary maximum flow.

For a finite directed graph with nonnegative costs `c(u,v)`, the minimum cost from `s` to `t` has the standard LP dual

`T(s,t) = max { phi(t)-phi(s) : phi(v)-phi(u) <= c(u,v) for every directed edge u->v }`.     (6.1)

Thus a large adverse barrier corresponds to a feasible potential that accumulates large height while respecting every local log-cost constraint. A single cheap path disproves such a large dual potential difference. This is the correct dual certificate for multiplicative path probabilities.

For the rectangular cylinders used below we can add a genuine cut statement. Let `e` be one of the signed coordinate vectors and let `H_e` be the integer hyperplane orthogonal to it. For transverse points `z in H_e`, the straight forward lines

`gamma_z = (z,z+e,...,z+Le)`

are vertex-disjoint. Therefore any vertex set meeting every selected straight channel has cardinality at least the number of selected channels. Equivalently, once `r` of these lines have low log-cost, their union carries an integral `r`-path flow and every vertex separator of that cheap-channel subgraph has size at least `r` (the elementary Menger duality).

The important diagnostic is also negative: **a large cut cardinality is not yet a large quenched hitting probability.** Each cheap channel may still have probability `exp[-Theta(L)]`. A proof of P0483 must eventually convert route abundance into harmonic measure / regeneration-time control, not merely exhibit routes.

Outcome of B11: **success in identifying the correct dual and a precise limitation of the naive cutset idea.** This prevents the next run from falsely treating many geometrical bypasses as though their total hitting probability were automatically order one.

---

# 7. B28 — typical environment: a quantitative one-scale bypass bundle

The log-cost gap from Lemma 5.1 and the exact independence of disjoint straight lines give a clean one-scale statement with explicit error.

Choose coordinates so the selected oriented direction is `e=+-e_i`. For `W,L>=1`, let

`Z_W = { z in Z^d : z_i=0 and |z_j|<=W for j!=i }`,

so

`N_W := |Z_W| = (2W+1)^(d-1)`.

For each `z in Z_W`, define its straight-line log cost

`S_z(L) := sum_(r=0)^(L-1) [-log omega_(z+r e)(e)]`.               (7.1)

The collections of environment sites used by distinct `z` are disjoint, so the random variables `S_z(L)` are independent. Each is a sum of `L` i.i.d. variables in `[0,a]` with mean `m=a-Delta`.

## Theorem `NM13-12-P0483-BYPASS-BUNDLE-05`

Under the source hypothesis of Lemma 5.1, fix `e`, `a`, `Delta`, and `beta=a-Delta/2` as above. Then for every `L,W>=1`,

`P[ at least N_W/2 of the lines gamma_z satisfy S_z(L) <= beta L ]
 >= 1 - exp[ N_W log 2 - (Delta^2/(4a^2)) L N_W ].`               (7.2)

In particular, whenever

`L >= L_0 := 8 a^2 log 2 / Delta^2`,

that probability is at least

`1 - exp[ -(Delta^2/(8a^2)) L N_W ].`                              (7.3)

Every good line in (7.2) has exact quenched path probability at least

`exp[-beta L] = exp[-(a-Delta/2)L]`,                               (7.4)

and the good lines are pairwise vertex-disjoint.

### Proof

For one line, Hoeffding's inequality gives

`p_L := P[S_z(L)>beta L]
      = P[S_z(L)-mL > (Delta/2)L]
      <= exp[-2 L (Delta/2)^2/a^2]
      = exp[-Delta^2 L/(2a^2)].`                                   (7.5)

Let `B` be the number of bad lines. By line independence, for any `p>=p_L` one may dominate `B` by `Bin(N_W,p)`. The elementary binomial tail bound

`P[B>=N_W/2]
 <= sum_(k>=N_W/2) binom(N_W,k) p_L^k
 <= 2^(N_W) p_L^(N_W/2)`

therefore yields exactly (7.2). If `L>=L_0`, then

`log 2 <= Delta^2 L/(8a^2)`,

and (7.3) follows. Finally, by the definition of log cost, following a good straight line has probability `exp[-S_z(L)]>=exp[-beta L]`. `square`

### Corollary 7.1 — a thin source-direction cylinder with a strict exponent gain

Let

`b := sum_(j!=i) |ell_j|`.

Choose a positive constant

`theta <= Delta/[4a(d-1)]`,                                       (7.6)

and, if `b>0`, also require

`theta <= (e.ell)/(2b)`.                                          (7.7)

Put `W_L=floor(theta L)` and `N_L=(2W_L+1)^(d-1)`.

On the good-environment event from (7.3), select any good line `gamma_z`. Starting from the origin, first move inside the left cross-section to `z` along a monotone transverse path. Its length is at most `(d-1)W_L`, and uniform ellipticity gives this approach path probability at least

`exp[-a(d-1)W_L]`.

Following `gamma_z` afterwards has probability at least `exp[-beta L]`. Hence the quenched probability of following this complete in-cylinder path is at least

`exp[-a(d-1)W_L-beta L]
 >= exp[-(a-Delta/4)L].`                                           (7.8)

The endpoint also makes definite source-direction progress. Indeed

`(z+Le).ell >= L(e.ell)-W_L b >= (L/2)(e.ell)`                     (7.9)

when `b>0`, while the statement is immediate if `b=0`.

Thus, for all sufficiently large `L`, with environment probability at least

`1 - exp[-c L N_L] = 1-exp[-Theta(L^d)]`                            (7.10)

for the explicit constant `c=Delta^2/(8a^2)` times the fixed `theta`-dependent cross-section factor, there exists a path from the origin, staying in a width-`Theta(L)` cylinder, that advances at least `(e.ell)L/2` in the source direction and whose exact quenched path probability has exponent

`a-Delta/4 < a=-log kappa`.                                        (7.11)

This is a strict improvement over the universal worst-case cost `kappa^L=exp(-aL)` forced only by uniform ellipticity.

### Corollary 7.2 — positive-density cheap-channel cut resistance

On the same event, at least `N_L/2` pairwise vertex-disjoint straight channels have cost at most `beta L`. Therefore every vertex set that meets all of these cheap longitudinal channels has cardinality at least `N_L/2 = Theta(L^(d-1))`.

This is the promised one-scale typical-environment bypass statement. It is exact in its quantifiers and does not use simulation, an unproved multiscale induction, or an assumption that a finite computation settles an asymptotic exponent.

### What this does and does not buy

The theorem is stronger than the preceding full-bulk-template entropy calculation in one important sense: it starts from the **actual source hypothesis** and does not prescribe a rare sign-reversing environment. It proves that directional transience itself forces a strict forward log-cost slack and that i.i.d. sampling turns the slack into many independent cheap channels with a volume-order environment failure exponent.

But it is still not ballisticity. The lower bound in (7.8) is exponentially small in `L`. Even polynomially many disjoint straight channels do not by themselves turn that into a nonvanishing exit probability. The missing step is therefore no longer “show that a sideways bypass exists”; it is:

> turn source-implied cheap-path **free energy / path abundance** into a sufficiently strong annealed or quenched **hitting-probability** estimate, without assuming the polynomial condition that existing ballisticity theorems already require.

That is a sharper obstruction than the preceding route had.

---

# 8. Relation to existing theory and novelty discipline

The ingredients “bounded log edge costs,” Hoeffding concentration, shortest-path LP duality, and Menger's theorem are standard. I make **no novelty claim** for any of them separately. I also did not locate, in the bounded search, a paper stating the exact source-hypothesis implication `m_*(ell)<-log kappa` together with the disjoint straight-channel estimate above, but a negative search is not a novelty certificate. The result is recorded as an internal route theorem and **PARTIAL** relative to P0483.

The theorem does not subsume Guerra's polynomial criterion: it controls the existence of cheap directed paths, whereas `(P)_M` controls the probability of exiting a large box through the wrong boundary. Those are different objects. Treating (7.10) as though it were a polynomial back-exit estimate would be a quantifier error.

Likewise, nothing here contradicts Fribergh--Kious's diagnosis that the uniformly elliptic difficulty is global exploration / large-scale zig-zagging. The result makes that diagnosis more concrete: local route existence is overwhelmingly typical; what remains is to control which routes the random walk actually discovers and with what harmonic measure.

## 9. Method outcomes

### B1 — CHANGE THE CATEGORY

Recast products of RWRE transition probabilities as additive bounded directed first-passage costs. This yielded Lemma 5.1: directional transience forces a strict forward mean log-cost gap `Delta>0` in at least one lattice direction with positive `ell` projection.

**Outcome:** success; new source-hypothesis quantitative structure, but no frozen-metric movement.

### B11 — DUALIZE

Used shortest-path LP duality to identify the correct dual object as a cost-Lipschitz potential, and Menger duality on the selected straight-channel bundle. This also exposed why the naive “large cut = good escape probability” inference is invalid for multiplicative RWRE path weights.

**Outcome:** success as route clarification; the missing quantity is harmonic measure/free energy, not geometric connectivity.

### B28 — REPLACE FOR-ALL WITH FOR-TYPICAL

Proved Theorem `NM13-12-P0483-BYPASS-BUNDLE-05`: in a width-`Theta(L)` cylinder, a positive density of independent straight channels beat the worst ellipticity log-cost exponent, with failure probability `exp[-Theta(L^d)]`; Corollary 7.1 converts one of them into an origin-accessible path that still makes linear source-direction progress.

**Outcome:** success; complete one-scale theorem with explicit error. It does not establish an asymptotic ballistic exponent or a regeneration moment.

No checker artifact is created for this run because the new claim is analytic, not a finite enumeration; the complete argument is on this page. This follows the owner's instruction not to manufacture certificates when they do not test a new finite claim.

## 10. Next route

Because the frozen metric is now unchanged for two consecutive runs, the next ordinary invocation should make one genuine attempt to move the source-relevant obstruction before a stuck recovery becomes mandatory. Do **not** optimize another straight-line Hoeffding constant.

Use three methods not yet used on P0483:

- **B3 — prove something stronger:** replace “there exists a cheap path” by an exponentially weighted path partition function / free-energy lower bound in a thin forward cone, so route entropy can compete with the exponential cost in (7.8);
- **B13 — find what only increases:** seek a monotone exploration quantity measuring discovered forward conductance or accumulated cheap-channel mass along regeneration attempts;
- **B27 — swap the quantifiers:** instead of finding, for each scale, one favorable channel, ask whether one source-selected oriented direction `e` admits a scale-uniform cone estimate on a positive-probability set of environments, then determine exactly what is lost when moving from environment-typical to walk-typical.

A valid next movement would be a rigorously stronger hitting-probability or regeneration-tail bound with explicit quantifiers under the unchanged source process. A mere restatement of (7.2)--(7.11) with different constants is not movement.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  claim_id: P0483
  canonical_dedup_key: directional_transience_versus_positive_speed_under_uniform_ellipticity
  source_status: OPEN
  local_status: PARTIAL
  frozen_metric: c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))
  metric_before: -log rho(K_{d,w}(kappa))
  metric_after: -log rho(K_{d,w}(kappa))
  movement: false
  unchanged_runs: 2
  hard_stuck_recoveries_used: 0
  methods:
    - B1: "recast multiplicative RWRE paths as bounded directed first-passage log cost; proved directional transience forces a strict forward mean log-cost gap Delta>0 in some lattice direction"
    - B11: "used shortest-path LP duality plus Menger duality on disjoint straight channels; identified harmonic measure rather than cut cardinality as the remaining obstruction"
    - B28: "proved a one-scale typical-environment bundle theorem: at least half of Theta(L^(d-1)) straight channels have cost <=(a-Delta/2)L except with exp(-Theta(L^d)) probability, and one origin-accessible path advances linearly in ell with path exponent <=a-Delta/4"
  strongest_new_claim: NM13-12-P0483-BYPASS-BUNDLE-05
  new_finite_artifact: none
  audit_P26: not_requested_not_passed
  audit_secondary_NM13_13: not_requested_not_passed
  closure: false
  next_methods:
    - B3
    - B13
    - B27
  next_step: "amplify cheap-path existence into a source-valid path-partition/harmonic-measure or regeneration-tail estimate; do not spend another run optimizing the same straight-channel constant"
  literature_check_date_utc: 2026-09-17
  literature_scope: "original Drewitz-Ramirez source; Guerra-Ramirez stronger ballisticity equivalences; Guerra transience-to-(T) polynomial criterion; targeted 2025-2026 exact-phrase and author/citation searches"
  literature_access_limit: "bounded public web/repository search; negative search is not worldwide-openness or novelty proof"
```

## 12. Run status

One immutable report is the only repository write warranted by this invocation. The existing ownership claim remains untouched. No shared root, peer namespace, schedule, email, Drive item, workflow, permission, or public posting was modified.
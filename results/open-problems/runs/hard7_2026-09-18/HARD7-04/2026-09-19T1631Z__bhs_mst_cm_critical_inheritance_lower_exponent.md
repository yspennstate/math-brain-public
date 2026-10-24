Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `beta_MST^- >= 0 -> beta_MST^- >= eta=(tau-3)/(tau-1)`. Methods tried: B1 / B2 / B19.**

# HARD7-04 — critical-cluster inheritance gives the source-predicted MST diameter lower exponent

Status: **PARTIAL**. The Bhamidi–Sen heavy-tailed configuration-model MST universality problem is not solved in full.

## 1. Continuity, Section-I rotation, and capability honesty

This execution began from the newest HARD7-04 checkpoint rather than restarting admission. The predecessor claim `VDH-8.3-DUALITY` had already consumed both permitted Section-I stuck-recovery cycles, and its frozen metric remained unchanged at the 15:30Z checkpoint. Continuing that route would violate the owner directive. I therefore released it explicitly to `UNASSIGNED AFTER HARD7-04 HANDOFF` at commit `7847eaf270ace2898764c6ac7072c80f3b4c135e`, preserving its strongest source-size and post-giant histogram checkpoints, and then screened a fresh source.

Before the new claim I re-read the controlling HARD7 instructions, root campaign index/ranking, `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest own report, and neighboring HARD reports. The large intake collection was checked through its indexed source/alias records rather than falsely claiming a byte-for-byte dump in one connector response.

The exposed task interface still provides no model selector, reasoning-effort selector, or guaranteed execution duration. GPT-6/maximum is therefore prompt-requested only. This execution identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, hence `UNVERIFIED`. Changing model/reasoning would require an authorized platform interface that actually exposes those controls. Historical `You cannot modify this task` errors are authorization/context restrictions; the compliant workaround is the owning/authorized context or platform support, never a duplicate task or permission bypass. No schedule was created, disabled, re-enabled, or modified in this run.

## 2. Fresh admission: heavy-tailed MST universality for the configuration model

The new exclusive claim is `operations/claims/BHS-MST-CM-UNIV.md`, owned by HARD7-04. The corrected claim was read from `master` after commit `7cef6e0d0498fb078ab1f71dead684a325dfc5dd`.

Primary source:

Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, Probab. Theory Relat. Fields 188 (2024), 729–804, arXiv:2009.10696v4, DOI 10.1007/s00440-024-01259-3.

The paper proves the heavy-tailed MST scaling limit for a rank-one inhomogeneous model. In Section 8 it explicitly identifies the next universality program as including, in its words, **“starting with the configuration model and (simple) random graphs with given degree sequence”**, and expects the `tau in (3,4)` giant-component MST to have the same limit under suitable assumptions. The paper also explains why the already-known critical configuration-model metric limit does not itself finish the MST problem: the complement of the dominant critical component must still be controlled.

The paper’s introduction records the underlying strong-disorder distance prediction as a well-known physics problem going back to work beginning in 2003: MST distances should scale as

`n^eta,    eta=(tau-3)/(tau-1),    tau in (3,4)`.

### Fixed subclass retained here

To remove the source phrase “under suitable assumptions” from the moving part of this track, this run fixes deterministic degree sequences with:

- `min_i d_i >= 3`;
- power-law exponent `tau in (3,4)`;
- `nu_n -> nu>1`;
- Bhamidi–Dhara–van der Hofstad–Sen Assumptions **1(i), 1(ii), and 2** plus their supercritical critical-percolation setup `(1.11)--(1.12)`.

The exclusion of Assumption 1(iii) is deliberate: it asks for linear degree-one mass and is incompatible with `min d_i>=3`. Their Theorem 1.3, Theorem 1.4, and Corollary 1.5 for critical percolation explicitly require only 1(i), 1(ii), 2 together with `(1.11)--(1.12)`.

Give every configuration-model edge an iid continuous weight, monotonically transformed to `Unif[0,1]`. Let `M_n` be the MST of the component carrying the giant; under the retained minimum-degree condition the base configuration model is connected with probability tending to one, so on that event this is the full MST.

### Ownership and current-status screen

Immediately before create-only admission, direct fetch of `operations/claims/BHS-MST-CM-UNIV.md` returned 404, and searches for the source title/arXiv ID, `configuration model MST heavy-tailed`, and the canonical ID found no existing exclusive claim or posted equivalent. Critical-configuration-model geometry targets and the random 3-regular MST theorem are not aliases.

A bounded current-literature refresh dated 2026-09-19 used the exact source title/authors and the queries `configuration model minimal spanning tree heavy-tailed`, `configuration model minimum spanning tree power law tau 3 4`, `given degree sequence MST scaling limit heavy-tailed random graph`, and 2025/2026 variants. It recovered the source paper, the published critical heavy-tailed configuration-model geometry papers, and the finite-third-moment/random-regular MST line, but no later theorem resolving the source-matching `tau in (3,4)` configuration-model MST scaling limit. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Frozen measurable quantity and before/after value

Define

`beta_MST^- := sup { beta>=0 : for every delta in (0,1) there is c_delta>0 such that liminf_n P(diam(M_n)>=c_delta n^beta)>=1-delta }`.

Admission baseline was the trivial certificate

`beta_MST^- >= 0`.

This run proves, for the fixed subclass above,

`beta_MST^- >= eta=(tau-3)/(tau-1)`.

Thus the quantity **moves** from `0` to the full source-predicted lower exponent `eta`. This is only the lower direction. No upper tightness, GH/GHP convergence of the MST, or universality identification is claimed.

## 4. Ninety-percent research route: B1 / B2 / B19

The idea was committed before theorem bookkeeping at `a4ed8457690aea8e36f1eb81486eee6f2e97c8ad`.

- **B1 — CHANGE THE CATEGORY.** Replace final-MST geometry by a statement about the entire threshold-percolation filtration generated by the edge weights. **Successful.**
- **B2 — ATTACK THE NEGATION FIRST.** Try to make later, heavier edges create a shortcut that destroys a large critical-window distance inside the final MST. **The proposed obstruction is impossible.**
- **B19 — MAKE IT AN ALGORITHM.** Read the issue directly from Kruskal/cut optimality. **Successful and gives a deterministic lemma.**

The preceding HARD7-04 run used B9/B23/B27, so this is a genuinely different triple.

## 5. Deterministic filtration-inheritance lemma

**Lemma.** Let `G=(V,E)` be a finite connected graph with distinct real edge weights, let `T` be its MST, and for `p` let `G_{<=p}` be the spanning subgraph containing exactly the edges of weight at most `p`. If `C` is any connected component of `G_{<=p}`, then:

1. `T[C]` is connected;
2. for every `x,y in C`, the unique `T`-path from `x` to `y` uses only edges of weight at most `p` and stays inside `C`;
3. consequently `d_T(x,y) >= d_{G_{<=p}}(x,y)` and `diam(T) >= diam(C)`.

**Proof.** Fix `x,y in C`. Suppose the unique `T`-path from `x` to `y` contains an edge `e` with weight `w(e)>p`. Removing `e` splits `T` into two vertex sets `A,B` with `x in A`, `y in B`. Since `x,y` are connected inside `C`, an `x-y` path in `G_{<=p}` crosses the cut `(A,B)` in some edge `f`. Then `w(f)<=p<w(e)`. The graph `T-e+f` is a spanning tree with strictly smaller total weight than `T`, contradiction. Hence every edge of the `T`-path has weight at most `p`. Such a path cannot leave the threshold component `C`, because every vertex reached from `C` by an edge of weight at most `p` belongs to the same threshold component. This proves (1) and (2). Since the `T`-path is one particular path in `G_{<=p}[C]`, its edge count is at least the shortest-path distance there, proving (3). QED.

The cut argument itself is standard MST/Kruskal folklore. I do **not** claim novelty for the lemma. Its value here is that it transfers a published critical configuration-model diameter scale into the final supercritical MST without any monotonicity assumption on graph distance under edge addition.

## 6. Published critical input

Use the critical cutoff

`p_n := 1/nu_n`,

which is the `lambda=0` case of the heavy-tailed critical window.

Bhamidi, Dhara, van der Hofstad and Sen, *Global lower mass-bound for critical configuration models in the heavy-tailed regime*, arXiv:2005.02566v2 / EJP 2022, prove under exactly Assumptions 1(i), 1(ii), 2 and `(1.11)--(1.12)` that, for each fixed ordered critical component,

`n^{-eta} C_(i)(p_n) => M_i`

in Gromov–Hausdorff–Prokhorov topology (Theorem 1.4), and hence

`n^{-eta} diam(C_(i)(p_n)) => diam(M_i)`

(Corollary 1.5).

The limit is nondegenerate as a metric space. Their discussion describes `M_i` as a tilted inhomogeneous continuum random tree followed by a finite Poisson number of point identifications. The ICRT construction starts from a branch of strictly positive random length. A quotient of a real tree by finitely many point identifications cannot collapse uncountably many singleton equivalence classes to one point. Therefore

`D_i:=diam(M_i)>0` almost surely.

This positivity argument is included because the frozen metric requires an arbitrarily high-probability lower bound, not merely a positive-probability event.

## 7. Theorem: source-predicted lower diameter exponent for the retained CM subclass

**Theorem.** Under the fixed assumptions in Section 2, with

`eta=(tau-3)/(tau-1)`,

for every `delta in (0,1)` there is `c_delta>0` such that

`liminf_{n->infinity} P(diam(M_n) >= c_delta n^eta) >= 1-delta`.

In particular,

`beta_MST^- >= eta`.

**Proof.** Let `D_1=diam(M_1)` be the first critical limiting diameter. Since `D_1>0` almost surely, for arbitrary `delta in (0,1)` choose a continuity point `c_delta>0` of the distribution of `D_1` so small that

`P(D_1>2c_delta)>1-delta/3`.

Corollary 1.5 gives

`n^{-eta} diam(C_(1)(p_n)) => D_1`.

By convergence in distribution, after decreasing `c_delta` if necessary and taking `n` large,

`P(diam(C_(1)(p_n)) >= c_delta n^eta) > 1-2delta/3`.

It remains only to ensure that this threshold component lives inside the graph whose MST is `M_n`. Under Assumption 1(ii), the degree sequence has a finite limiting second moment, while Assumption 1(i) gives

`d_max=O(n^{1/(tau-1)})=o(n^{1/2})`

because `tau>3`. With `min_i d_i>=3`, the standard configuration-model connectivity theorem (Łuczak; see also Federico–van der Hofstad, *Critical window for connectivity in the Configuration Model*, arXiv:1603.03254) gives

`P(CM_n(d) is connected) -> 1`.

Thus for all sufficiently large `n` this connectivity event has probability at least `1-delta/3`.

Couple the iid `Unif[0,1]` MST weights with percolation in the usual way: retain an edge at level `p_n` exactly when its weight is at most `p_n`. On the connectivity event, `M_n` is the MST `T_n` of the whole configuration model. Applying the deterministic lemma to the largest component `C_(1)(p_n)` gives pathwise

`diam(M_n)=diam(T_n) >= diam(C_(1)(p_n))`.

Therefore, by a union bound,

`P(diam(M_n) >= c_delta n^eta) >= 1-delta`

for all sufficiently large `n`. Since `delta` was arbitrary, the definition of `beta_MST^-` yields `beta_MST^- >= eta`. QED.

## 8. What this does and does not establish

This is a genuine source-relevant asymptotic movement, not a finite-size fit: the lower diameter exponent for the retained heavy-tailed configuration-model subclass reaches the predicted value `eta`.

It does **not** prove:

- `diam(M_n)=O_P(n^eta)`;
- tightness of the rescaled whole MST;
- convergence in GH/GHP topology;
- identification of the limit with the Bhamidi–Sen rank-one MST limit;
- the source statement for arbitrary low-degree mass or every degree sequence hidden by the phrase “suitable assumptions.”

The source itself already warns where the missing mathematics lies: the critical component limit is only one part of the Kruskal process. One must control the forest hanging off the dominant critical structure as the threshold moves from the critical window to `1`, uniformly enough that no branch contributes macroscopic `n^eta` geometry beyond the candidate limit.

This is now the sharp remaining obstruction for this track. A natural next fresh triple is **B6** (deform outward from the solved critical window), **B20** (identify exactly where Kruskal’s complement-control algorithm can fail), and **B30** (control one postcritical scale at a time).

## 9. Verification / bookkeeping

No exact-arithmetic checker was manufactured in this run: the new result is an asymptotic theorem with a full proof on the page and has no finite arithmetic core. That is intentional under the 90/10 rule.

Immutable idea artifact:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1631Z__bhs_mst_cm_critical_inheritance_idea.md`

Canonical claim:

`operations/claims/BHS-MST-CM-UNIV.md`

Ledger delta, without editing the shared root ledger:

`HARD7-04 | BHS-MST-CM-UNIV | beta_MST^-: >=0 -> >=eta=(tau-3)/(tau-1) | PARTIAL`

Source URLs checked:

- https://arxiv.org/abs/2009.10696
- https://arxiv.org/abs/2005.02566
- https://arxiv.org/abs/1703.07145
- https://arxiv.org/abs/1603.03254

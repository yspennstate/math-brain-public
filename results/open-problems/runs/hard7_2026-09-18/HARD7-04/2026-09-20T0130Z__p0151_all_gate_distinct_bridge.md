Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b3 -> gamma_E >= b4` with `b4>b3`**; methods actually used: **B3 / B14 / B25**.

# HARD7-04 bounded research iteration — all-gate distinct-bridge amplification for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run proves a stronger expected-largest-component lower exponent for the exact admitted fixed-outdegree sequential preferential-attachment model. It does **not** identify the critical-window width, prove a matching upper bound, establish tightness, or give a scaling limit. No simulation is used as proof. The substantive claim is analytic; its full proof is given below and isolated as `artifacts/hard7_2026-09-18/HARD7-04/p0151_all_gate_distinct_bridge_lemma.md`.

## 1. Continuity, ownership, repository state, and consumed evidence

I resumed the active exclusive claim `operations/claims/P0151.md`, owned by `HARD7-04`. I did not restart the retired P0157, configuration-model MST, BHS, I0049, or independently-attached-edge routes.

Before doing mathematics I reread the required control surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the P0151 intake/catalog traces, including the intake tier row `P0151|3|critical window, fixed-outdegree PA` and the preserved catalog derived from the `problems.jsonl` campaign ledger;
- `operations/claims/P0151.md`;
- the immediately preceding HARD7-04 reports `2026-09-19T2228Z__bhs_handoff_p0151_block_activation.md`, `2026-09-19T2330Z__p0151_tangent_bootstrap.md`, and `2026-09-20T0030Z__p0151_ticket_recent_bridge.md`;
- the neighboring preferential-attachment status report `runs/R08/20260917T223457Z_rotation_preferential_attachment_status_5d8c41.md` and current claim-delta screens that explicitly mark P0151 active under HARD7-04.

The current posting registry adds no P0151-equivalent posted paper. Repository ownership remains unambiguous: `P0151` is still HARD7-04's canonical claim and other current admission screens treat it as active-other-owner.

The frozen source model is unchanged. Fix integer `m>=2`, `delta>0`, and Ray's sequential fixed-outdegree affine preferential-attachment model `PA_n^(m,delta)(d)`: every arriving vertex has exactly `m` sequential edges to older vertices, with probabilities proportional to current degree plus `delta`, intermediate degree updates included, no self-loops, followed by independent bond retention `pi`.

Put

`a:=m+delta`, `A:=2m+delta`.

Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models* (arXiv:2312.14085; EJP 31 (2026)), prove

`pi_c = delta / [2( m(m+delta) + sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The source-level target retained by P0151 is the finite-size critical regime for this fixed-outdegree sequential model: the critical window and the scale/law of the largest critical components, not threshold identification.

### Current-literature refresh, 20 September 2026

A bounded fresh search rechecked the exact model against the current neighboring literature:

1. Hazra--van der Hofstad--Ray, arXiv:2312.14085, identify `pi_c` through the Pólya-point-tree mean-offspring spectral radius and prove the giant/no-giant transition; they do not supply a finite-size critical-window theorem for the exact fixed-outdegree sequential ensemble.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937 (22 Dec 2025), prove a `(log n)^(-2)` window and `sqrt(n)/log n` largest-critical-component scale for sparse growing graphs whose new vertex connects **independently** to earlier vertices. Their abstract explicitly states the independent-connection model, so it is not automatically the fixed-`m` sequential model here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844 (26 Jun 2026), study an inhomogeneous random graph with a preferential-attachment kernel in the infinite-variance regime and a moving threshold `p_n`; it is a different ensemble and parameter regime.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded search. This is **bounded negative evidence only**, not a worldwide novelty certificate.

---

## 2. Frozen metric and strict before/after movement

Let `C_max(n,pi_c)` denote the largest component after critical bond percolation and retain the admitted source-relevant metric

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The previous run proved

`gamma_E >= b3`,

where

`b2 := [m+a m pi_c]/A`,
`z := a pi_c/A`,
`b3 := b2 + z[1-(1-z)^(m-1)]`.

This run proves

`gamma_E >= b4 := b2 + m(m-1) z^2`.                              (2.1)

The improvement is strict. By Bernoulli's union bound,

`1-(1-z)^(m-1) <= (m-1)z`,

so

`b3-b2 <= (m-1)z^2 < m(m-1)z^2=b4-b2`.                           (2.2)

Thus `b4>b3` for every `m>=2`, `delta>0`.

For orientation only, not proof: at `m=2`, `delta=1`,

`pi_c≈0.04587585476806849`,
`b2≈0.4550510257216822`,
`b3≈0.4558086795799345`,
`b4≈0.4565663334381869`.

The source-level state remains OPEN/PARTIAL because a one-sided expected-size exponent is much weaker than a critical-window theorem.

---

## 3. Idea before code: what was missing from the preceding bridge proof

The previous run deliberately used **edge 1 as a fixed gate** and captured at most one recent outside target. That made the proof easy to localize but discarded two first-order resources:

1. any one of the `m` birth edges can be the retained ticket-hit edge that connects the new vertex to the tracked component;
2. once such a gate exists, **every distinct retained recent outside target of the same birth** is connected through that new vertex and can be captured.

The obvious stronger claim, “just multiply the old bridge term by `m` and by the number of successful outside edges,” is not valid without corrections. Two exact obstructions must be paid:

- several gate edges make the ordered gate--bridge pair count overcount the same bridge edge;
- several bridge edges can hit the same outside vertex, so successful bridge edges are not automatically distinct new vertices.

The new route is to count ordered gate--bridge pairs and subtract both defects. The key point is that the ticket-thinning construction makes the duplicate-target defect only `O(1/t)` and the multiple-gate defect quadratic in `S_t/t`. Both are summable after the same second-moment bootstrap.

This is the substantive new mechanism of the run.

---

# 4. B3 — prove something stronger: capture every distinct bridge target

Use the ticket-thinned connected exploration from the preceding report. At the beginning of birth `t+1`, let `Q_t` be a connected set contained in one true percolation component. Each `u in Q_t` carries frozen ticket mass `ell_u(t)` satisfying

`0 <= ell_u(t) <= d_u(t)+delta`.

Set

`S_t := sum_{u in Q_t} ell_u(t)`, `N_t:=|Q_t|`.

Every admitted vertex carries at least base ticket mass `a`, so for a fixed seed constant `C_0`,

`N_t <= S_t/a + C_0`.                                             (4.1)

The source attachment denominators satisfy for a fixed `K<infinity`, all large `t`, and each edge label `j`,

`At-K <= D_{t,j} <= At+K`.                                       (4.2)

### Gate thinning

If edge `j` targets `u in Q_t`, accept it as a ticket hit with auxiliary probability

`ell_u(t)/(d_u+delta)`,

using the frozen ticket weight and the current underlying attractiveness. Require also that the percolation mark is retained. Denote the resulting indicator by `G_j`.

The attractiveness cancels exactly, so conditional on arbitrary earlier outcomes in the same birth,

`P(G_j=1 | birth history) = pi S_t/D_{t,j}`.                      (4.3)

### External base-ticket bridge thinning

Fix `rho in (0,1)` and

`R_t(rho):={ceil((1-rho)t),...,t}`.

For `u in R_t(rho)\Q_t`, every vertex has current attractiveness at least `a`. If an edge targets such a `u`, accept it as an external base-ticket bridge with auxiliary probability

`a/(d_u+delta)`

and require retention. Denote the event by `B_j`; for a specified `u`, write `B_j(u)`.

If

`M_t:=|R_t(rho)\Q_t|`,

then, again after exact cancellation and conditional on arbitrary earlier birth outcomes,

`P(B_j=1 | birth history)=pi a M_t/D_{t,j}`,                      (4.4)

and

`P(B_j(u)=1 | birth history)=pi a/D_{t,j}`.                       (4.5)

Equation (4.5) remains true if the same vertex was hit earlier in the birth: its attractiveness rises by one, but the thinning denominator rises with it and cancels again.

Let

`G:=sum_j G_j`, `L:=sum_j B_j`.

If `G>=1`, the new vertex is connected by a retained edge to `Q_t`. Therefore every distinct target of a `B`-edge is connected through that new vertex. Let `D` be the number of distinct bridge targets and capture **all** of them, assigning each captured old vertex base ticket mass `a` once. The new vertex itself is admitted whenever `G>=1` and receives base ticket mass `a`.

The birth increment remains deterministically bounded:

`0<=Delta_t:=S_{t+1}-S_t <= m+a+a(m-1)=:B_*`.                    (4.6)

So proving the stronger capture rule does not sacrifice the bounded-increment architecture.

Outcome of B3: **the process can safely capture all distinct bridge targets; the only remaining issue is to quantify distinctness and gate overcounting.**

---

# 5. B14 — find the group acting: restore all `m` symmetric gate positions

The previous proof broke edge-label symmetry by privileging edge 1. Here the `m` birth labels are treated symmetrically through the exact identity

`GL = sum_{j != k} G_j B_k`,                                      (5.1)

because one edge cannot simultaneously target `Q_t` and `R_t(rho)\Q_t`.

The ordered pair count has `m(m-1)` possible gate--bridge label pairs. The fixed-gate proof only exploited `m-1` of them.

For every ordered pair `j!=k`, regardless of whether the gate-labelled edge is revealed before or after the bridge-labelled edge, the frozen thinnings (4.3)--(4.4) give

`P(G_j B_k | F_t) >= p_- q_-`,                                   (5.2)

where

`p_-:=pi S_t/(At+K)`,
`q_-:=pi a M_t/(At+K)`.

Hence

`E[GL|F_t] >= m(m-1)p_-q_-`.                                     (5.3)

This is the first-order factor-`m` gain over the fixed-gate route. It is not yet a proof because `GL` counts one bridge edge several times when there are several gates.

Outcome of B14: **edge-label symmetry exposes the correct first-order ordered-pair coefficient `m(m-1)` instead of the fixed-gate coefficient `m-1`.**

---

# 6. B25 — count the same object twice and pay the exact defects

Two elementary counting inequalities convert the ordered-pair count into actual distinct captured vertices.

## 6.1 Multiple-gate correction

Pointwise, for integers `G,L in {0,...,m}`,

`L 1_{G>=1} >= GL - m binom(G,2)`.                                (6.1)

Proof: if `G=0` or `1`, equality holds. If `G>=2`,

`GL-L=(G-1)L <= m(G-1) <= m binom(G,2)`.

Conditional gate probabilities are at most

`p_+:=pi S_t/(At-K)`,

so

`E[binom(G,2)|F_t] <= binom(m,2)p_+^2
 = O(S_t^2/t^2)`.                                                  (6.2)

Thus using all `m` gates costs only a quadratic shadow-density defect.

## 6.2 Duplicate-target correction

Let `C_same` be the number of unordered bridge-edge pairs that hit the same outside recent vertex. If one vertex is hit `r` times then it contributes `r-1` to `L-D`, while `binom(r,2)>=r-1`; therefore

`D >= L-C_same`.                                                    (6.3)

For a fixed pair of edge labels and a fixed outside recent vertex `u`, (4.5) and (4.2) yield

`P(B_j(u)B_k(u)|F_t) <= (pi a)^2/(At-K)^2`.

Summing over at most `t` outside recent vertices and `binom(m,2)` edge pairs,

`E[C_same|F_t] <= C/t`.                                            (6.4)

Combining (6.1)--(6.4),

`E[D 1_{G>=1}|F_t]
 >= m(m-1)p_-q_- - C S_t^2/t^2 - C/t`.                           (6.5)

Now `|R_t(rho)|>=rho t-C`, while (4.1) gives

`M_t>=rho t-N_t-C >= rho t-S_t/a-C`.

Using `(x)_+>=x` inside `q_-`,

`E[D 1_{G>=1}|F_t]
 >= [m(m-1)pi^2 a rho/A^2] S_t/t
    - C S_t^2/t^2 - C S_t/t^2 - C/t`.                            (6.6)

Each distinct captured target contributes ticket mass `a`, so the new first-order bridge coefficient is

`eta_rho := m(m-1)a^2 pi^2 rho/A^2`.                              (6.7)

Outcome of B25: **the symmetric ordered-pair count is converted into real distinct captured vertices with only a quadratic gate defect and an `O(1/t)` duplicate-target defect.**

---

# 7. Upper drift and the self-consistent second moment

The stronger process adds more bridge mass, so the preceding `E S_t^2=O(t)` estimate must be reproved rather than imported.

Let `K_t` be the number of ordinary ticket hits on tracked vertices and `I_t=1_{G>=1}`. As before,

`E[K_t|F_t] <= m S_t/(At-K)`,                                     (7.1)
`E[I_t|F_t] <= m pi S_t/(At-K)`.                                  (7.2)

For captures, `D1_{G>=1}<=L1_{G>=1}<=GL`. For every ordered pair `j!=k`, the gate probability is at most `pi S_t/(At-K)` and the total external bridge probability is at most `pi a t/(At-K)`. Hence

`E[D1_{G>=1}|F_t]
 <= m(m-1) [pi S_t/(At-K)] [pi a t/(At-K)].                      (7.3)

At `pi=pi_c`, define

`b4 := [m+a m pi_c]/A + m(m-1)a^2 pi_c^2/A^2`.                    (7.4)

Equations (7.1)--(7.3) imply

`E[Delta_t|F_t] <= [b4+O(1/t)] S_t/t`.                            (7.5)

The crucial exact inequality is

`b4<1/2`.                                                          (7.6)

### Proof of (7.6)

Put

`s:=sqrt(m(m-1)a(a+1))`,
`r:=s/a=sqrt(m(m-1)(a+1)/a)`,
`x:=a pi_c=delta/[2(m+r)]`.

Then

`1/2-b4
 = [delta/2-mx-m(m-1)x^2/A]/A
 = x[r-m(m-1)x/A]/A`.                                             (7.7)

Because `x<delta/(2m)`,

`m(m-1)x/A < (m-1)delta/(2A) < (m-1)/2`,

while

`r>sqrt(m(m-1))>(m-1)/2`.

Thus the bracket in (7.7) is positive, proving (7.6).

Now square the bounded-increment recursion. From (4.6) and (7.5), for any `c` satisfying `2b4<c<1` and all sufficiently large `t`,

`Y_{t+1} <= (1+c/t)Y_t + C`, `Y_t:=E S_t^2`.                      (7.8)

Induction gives

`E S_t^2=O(t)`.                                                     (7.9)

This closes the self-consistency loop for the stronger all-gate process.

---

# 8. Lower drift, bootstrap, and the new exponent

The ordinary ticket-hit count gives

`E[K_t|F_t] >= m S_t/(At+K)`.                                     (8.1)

A Bonferroni bound for activation gives

`P(I_t=1|F_t)
 >= m pi_c S_t/(At+K) - C S_t^2/t^2`.                             (8.2)

Add the bridge contribution (6.6), multiplied by ticket mass `a`. For

`b_rho := b2 + m(m-1)a^2 pi_c^2 rho/A^2`,                         (8.3)

we obtain

`E[Delta_t|F_t]
 >= [b_rho/t-C/t^2]S_t - C S_t^2/t^2 - C/t`.                     (8.4)

Taking expectations and using (7.9),

`mu_{t+1} >= [1+b_rho/t-C/t^2]mu_t - C/t`, `mu_t:=E S_t`.         (8.5)

A positive polynomial seed is available by discarding bridge captures and using the global chord

`1-(1-pi_c y)^m >= [1-(1-pi_c)^m]y`.

Exactly as in the admission run, this yields

`mu_t >= c t^{b1}`,                                                (8.6)

where

`b1=[m+a(1-(1-pi_c)^m)]/A>0`.

Let `H_t` satisfy

`H_{t+1}=H_t[1+b_rho/t-C/t^2]`.

Then `H_t=Theta(t^{b_rho})`. Dividing (8.5) by `H_{t+1}`, the total normalized error after time `T` is `O(T^{-b_rho})`, while the normalized seed from (8.6) is `Omega(T^{b1-b_rho})`. Their ratio is `Omega(T^{b1}) -> infinity`. Choose one fixed large `T`; iterating gives

`E S_n >= c_rho n^{b_rho}`.                                      (8.7)

Finally, regardless of bridge captures, the activation probability has the global chord lower bound

`E[I_t|F_t] >= q(pi_c) S_t/(At+K)`,
`q(pi):=1-(1-pi)^m>0`.

Each activation adds a new vertex to `Q`, so summing with (8.7) yields

`E|Q_n| >= c'_rho n^{b_rho}`.                                     (8.8)

By construction `Q_n` is contained in one true percolation component, hence

`E|C_max(n,pi_c)| >= E|Q_n|`.

Therefore

`gamma_E >= b_rho` for every fixed `rho<1`.                        (8.9)

Letting `rho↑1`,

`gamma_E >= b4
 = [m+a m pi_c]/A + m(m-1)(a pi_c/A)^2`.                       (8.10)

This proves the advertised strict movement `b3 -> b4`.

---

## 9. Three materially different moves and what happened

- **B3 PROVE SOMETHING STRONGER.** Instead of adding one old bridge target after a fixed gate, capture every distinct external base-ticket target whenever any retained gate exists. This succeeded, but only after explicitly controlling two overcounting defects.
- **B14 FIND THE GROUP ACTING.** Restored the symmetry of all `m` birth-edge labels. The first-order bridge count is naturally an ordered-pair count over `m(m-1)` gate--bridge labels, giving the factor-`m` gain discarded by the previous edge-1 gate construction.
- **B25 COUNT THE SAME THING TWICE.** Converted ordered gate--bridge pairs into actual distinct captured vertices. Multiple gates cost `O(S_t^2/t^2)` and duplicate outside targets cost only `O(1/t)` because the external base-ticket thinning makes each specified target have probability `pi a/D_{t,j}`.

This triple is new for P0151 and differs from the preceding `B1/B15/B30`, `B5/B12/B20`, and `B2/B7/B19` triples.

The negation test was substantive: the naive identity “ordered pairs = distinct captures” is false whenever there are multiple gates or repeated outside targets. The proof succeeds precisely because both failure mechanisms admit quantitative corrections below the first-order drift scale.

---

## 10. What moved, what did not, and the remaining full-scope gap

### Source-relevant movement

Before:

`gamma_E >= b3 = b2 + z[1-(1-z)^(m-1)]`, `z=a pi_c/A`.

After:

`gamma_E >= b4 = b2 + m(m-1)z^2`.

Strict movement: `b4>b3` for all frozen source parameters `m>=2`, `delta>0`.

### Auxiliary progress

1. Recovered a fully symmetric within-birth exploration using every possible gate label.
2. Proved a distinct-target conversion lemma with explicit defect scales.
3. Reproved the second moment for the enlarged process from the exact inequality `b4<1/2`; no inherited second-moment claim was assumed.
4. The one-birth constant-ticket architecture is now visibly limited by the remaining gap to `1/2`.

### Remaining source gap

Still **UNKNOWN / OPEN**:

- whether the power exponent is exactly `1/2` in this fixed-outdegree model;
- whether the true largest critical component is `Theta(sqrt(n)/log n)`;
- whether the window width is `(log n)^(-2)`;
- tightness, joint component scaling, and any limiting law;
- a rigorous finite-graph transfer from the Pólya-point-tree spectral eigenfunction to the source critical window.

The next nonrepeating route should not merely add another constant-number bridge event. The all-gate calculation shows that constant base tickets extract the entire first-order ordered-pair gain available from one birth while still leaving `b4<1/2`. A genuinely new method should therefore use **age/degree-dependent ticket mass or a two-sided/multi-seed exploration approximating the critical Pólya-point-tree eigenfunction**, with a truncation argument strong enough to retain `E S_t^2=O(t)` or an alternative moment closure.

This is the exact new obstruction; no stuck trigger applies because the frozen metric moved strictly this run.

---

## 11. Validation performed

- Checked every deterministic ticket-domination step under repeated hits in one birth.
- Checked that the specified-target external thinning remains `pi a/D_{t,j}` after an earlier hit because the updated attractiveness cancels with the updated thinning denominator.
- Checked the pointwise integer inequalities `L1_{G>=1} >= GL-m binom(G,2)` and `D>=L-C_same`.
- Checked the exact algebra proving `b4<1/2` from the source threshold formula, rather than from floating-point examples.
- Checked strict comparison `b4>b3` symbolically from `1-(1-z)^(m-1)<m(m-1)z` after the sharper bound `1-(1-z)^(m-1)<= (m-1)z`.
- Used no finite simulation, asymptotic fit, or independently-attached-edge theorem as proof for the fixed-outdegree model.

No exact-arithmetic program was added because there is no finite exhaustive claim in this iteration; the theorem-sized analytic proof is on the page and in the matching artifact.

---

## 12. Capability / scheduler honesty

The actual runtime exposed here is **GPT-5.6 Sol**; the reasoning level is **UNVERIFIED**. GPT-6 / maximum was requested in prompt text only and was not authenticated as the runtime.

The exposed native automation interface still offers task title, prompt, schedule, timing mode, and enabled state. It still exposes **no model selector, no reasoning-effort selector, and no guaranteed execution duration**. Changing the requested model/effort from prompt-only to enforced scheduler configuration therefore requires a platform-level scheduler capability (or an authorized account/workspace interface that exposes those fields); there is no repository-side workaround.

The old P26 `You cannot modify this task` result is not a universal current P26 state: current root `RESULTS.md` records that a later authorized context successfully updated P26, while another exposed context denied edits to a different set including all 20 R-series jobs. The correct workaround for a denied native task is to use the authorized owner/workspace context or platform support; **do not** bypass the restriction by cloning the task. This run did not modify, create, disable, or re-enable any schedule.

---

## 13. Ledger delta (own-track suggestion only; shared root not edited)

`HARD7-04 | P0151 fixed-outdegree PA critical window | gamma_E lower bound | b3 -> b4=[m+a m pi_c]/A + m(m-1)(a pi_c/A)^2 | PARTIAL / SOURCE OPEN`

No shared ledger, peer claim, schedule, email, Drive object, permission, workflow, or public posting was changed.
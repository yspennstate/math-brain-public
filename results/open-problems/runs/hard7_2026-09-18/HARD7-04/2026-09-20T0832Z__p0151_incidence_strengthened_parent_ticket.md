Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b9 -> gamma_E >= b10>b9`**; methods actually tried: **B13 / B15 / B4**.

# HARD7-04 bounded research iteration — incidence-strengthened historical-parent ticket

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The full analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_incidence_strengthened_parent_ticket_20260920T0832Z.md`

created at commit

`f8075151e54da64809ad1cfe161237f270e7a154`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, I0048, any solved degree-count target, the Kemeny/extremal-hitting-time papers, or the independently-attached-edge growing-graph model.

Before the new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md` and the current exclusion registry;
- the P0151 intake/catalog traces and current ownership search;
- `operations/claims/P0151.md`;
- the newest own-track substantive report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0730Z__p0151_parallel_historical_parents.md` and its analytic artifact;
- the neighboring preferential-attachment report `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`, which classifies the threshold-level I0048 scope as later-literature-known and does not own the critical-window target;
- the current master branch state before writing; no competing P0151 claim was found.

`POSTED.md` contains no source-equivalent P0151 paper. The canonical P0151 claim remains owned by HARD7-04. No shared root ledger was edited; the `ledger_delta` below is for the designated maintainer only.

---

## 2. Source statement and current-literature refresh — 20 September 2026

The source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probability proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The frozen source target is the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this exact fixed-outdegree sequential model.

Fresh bounded searches on **20 September 2026** rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`. This identifies the threshold and giant/no-giant transition for the fixed-outdegree affine PA model, not a finite-size critical-window theorem for this exact model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`. It proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale for models in which a new vertex connects independently to earlier vertices; that hypothesis does not automatically include fixed-`m` sequential PA.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026. This is a different inhomogeneous PA-kernel ensemble in the infinite-variance regime.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is negative search evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`.

The frozen source-relevant quantity remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved

`gamma_E>=b9`,

where

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1,d_*A/[4(a+m)pi^3])`,

`kappa_1:=2vartheta(a+m)pi^3/A`,

`d_7:=1/2-(b_U+kappa_1)`,

`lambda:=min(1,d_7A/[4(m-1)(a+m)pi^3])`,

`S:=vartheta+(m-1)lambda`,

and

`b9:=b6+a^2pi^3S/A^2`.

This run proves

`gamma_E>=b10`,

with

`b10:=b6+a(a+1)pi^3S/A^2`,                                      (3.1)

and therefore

`b10-b9=a pi^3S/A^2>0`.                                          (3.2)

So the frozen source metric moves strictly:

**Before:** `gamma_E>=b9`.

**After:** `gamma_E>=b10>b9`.

The unchanged-run counter remains reset.

For orientation only, at `m=2, delta=1`, the inherited ticket strengths are both one, so `S=2`, and

`b9≈0.4593297298598153`,

`b10≈0.4593529018720591`.

No finite-size fit or simulation is used in the proof.

---

## 4. Mathematical idea written before any code

The previous parallel-parent theorem still used the generic ordinary-vertex ticket numerator `a=m+delta`. That throws away a structural fact specific to a historical parent: if `v=p_j(u)`, then the edge `(u,v)` itself has already increased `v`'s graph degree by one after `v` was born.

Thus every nonseed historical parent has current attractiveness at least `a+1`, not just `a`. The new route is therefore:

1. keep exactly the previous simple-good-root set and the same total ticket strengths `S`;
2. replace each historical ticket `q a/w_v` by `q(a+1)/w_v`;
3. prove that the deliberately unused upper-drift margin from the prior construction absorbs the resulting `+1` cost uniformly over every `m>=2`, `delta>0`.

The exact missing lemma for going materially farther is now clear: a **depth-two ancestral supply lemma** controlling the mass of captured historical parents whose own parents are still outside the shadow. This run does not assume such a lemma.

No code was warranted because the new claim is analytic and parameter-uniform rather than finite/exhaustive.

---

## 5. B13 — find what only increases

If `v=p_j(u)>=3` is a historical parent of an ordinary vertex `u`, then `v` is born with degree `m` and attractiveness `a`. The later edge `(u,v)` increments its graph degree by one. Degrees never decrease, so at every later completed time `t>=u`,

`w_v(t)>=a+1`.                                                     (5.1)

Hence the new ticket probability

`q_j(a+1)/w_v(t)`                                                  (5.2)

is valid for every old historical parent because `0<q_j<=1`.

**Outcome B13:** succeeded. The parent relation itself contains one irreversible unit of attractiveness that the previous generic ticket ignored.

---

## 6. B15 — break the generic-vertex symmetry

Use the same simple-good roots `S_t` as the previous run: their `m` historical parents are ordinary, outside the shadow, and pairwise distinct. Their historical percolation bits are fresh under deferred decisions.

Conditional on a designated retained current gate and designated accepted capped bridge to a root `u in S_t`, historical label `j` now contributes frozen expected attractiveness

`pi * [q_j(a+1)/w_{p_j(u)}(t)] * w_{p_j(u)}(t)
 =pi q_j(a+1)`.

Summing labels gives exact raw historical reward

`pi(a+1)S`.                                                        (6.1)

The inherited simple-good capped-mass supply is

`sum_{u in S_t}c(w_u(t))
 >=a t-(1+a)W_t-aZ_t-2AN_t^rep-C`.

Therefore the new historical lower drift is

`eta_10 W_t/t`,

where

`eta_10=a(a+1)pi^3S/A^2`,                                        (6.2)

up to exactly the same lower-order `W_t^2/t^2`, `W_tZ_t/t^2`, `W_tN_t^rep/t^2`, `W_t/t^2`, and `1/t` errors as before.

Adding the base process gives the coefficient `b10` in (3.1).

**Outcome B15:** succeeded. Distinguishing actual historical parents from generic outside vertices yields the strict gain (3.2).

---

## 7. B4 — prove the one-generation strengthening completely

The only new global issue is second-moment closure. For one historical label with strength `q`, a captured parent of frozen weight `w>=a+1` has final current-birth weight at most `w+m`, so

`pi q(a+1)(w+m)/w <= pi q(A+1)`.

Thus the total historical upper-drift coefficient becomes

`kappa_10:=2(A+1)pi^3S/A`,                                       (7.1)

instead of the previous

`kappa_P=2pi^3S`.

The old construction intentionally left enough margin. Write

`M_old:=1/2-(b_U+kappa_P)`.

From the definitions of `vartheta` and `lambda`,

`kappa_1<=d_*/2`,

`kappa_F<=d_7/2`,

so

`M_old>=d_*/4`.                                                    (7.2)

The `+1` ticket costs only

`Delta_U:=kappa_10-kappa_P
        =2pi^3S/A
        =kappa_P/A`.                                               (7.3)

Because (7.2) implies `kappa_P<=3d_*/4` and `A=2m+delta>4`,

`Delta_U<=3d_*/(4A)<3d_*/16<d_*/4<=M_old`.                       (7.4)

Hence

`U_10:=b_U+kappa_10<1/2`.                                        (7.5)

The square-jump estimate changes only by a fixed constant because

`[q(a+1)/w](w+m)^2<=C(w+m)`;

summing historical parent incidences is still controlled by the inherited square-attractiveness budget `E V_t=O(t)`. Therefore

`E W_t^2=O(t)`.                                                    (7.6)

The mean recurrence is consequently

`mu_{t+1}
 >=[1+b10/t-C/t^2]mu_t
   -C/t-Ct^(h-1)-C log(t)/t`,                                    (7.7)

with `h=m/A<1/2`. The inherited gate-only seed exponent

`b1=[m+a(1-(1-pi)^m)]/A>h`

dominates all normalized error tails after a sufficiently large deterministic start time, giving

`E W_n>=c n^b10`.

Future gate activations turn shadow-attractiveness growth into component-size growth, so

`gamma_E>=b10`.                                                    (7.8)

Also

`eta_10/kappa_10=a(a+1)/[2A(A+1)]<1/2`,

and `b6<b_U`, hence `b10<1/2`.

**Outcome B4:** succeeded. The full one-generation strengthening closes for every source parameter without borrowing the unresolved depth-two supply problem.

---

## 8. Tests / validation actually performed

There is no finite certificate claim in this run. Validation consisted of:

- line-by-line algebraic comparison of the old and new lower coefficients;
- a parameter-uniform margin proof (7.2)--(7.5), rather than sampling covariance/parameter points;
- a numerical sanity evaluation at `m=2, delta=1`, used only for orientation and not as evidence for the theorem;
- exact GitHub readback of the full analytic artifact at commit `f8075151e54da64809ad1cfe161237f270e7a154`.

No checker was manufactured because no finite statement required one.

---

## 9. Unresolved full-scope gap

The source problem remains open. This run does **not** prove:

- `gamma_E=1/2`;
- a matching upper bound;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` window for the exact fixed-outdegree sequential model;
- tightness or a scaling-limit law;
- transfer of the independent-edge theorem to the sequential fixed-`m` model.

The exact next missing lemma for the most promising new continuation is:

> **Depth-two ancestral supply lemma.** Quantitatively lower-bound, by `c t-o(t)` in the relevant capped mass, the set of simple-good bridged roots whose captured historical parents have at least one fresh ordinary historical parent still outside the current shadow, with all collision/revelation losses controlled strongly enough that the resulting extra ancestral reward has a linear-in-`W_t/t` drift term.

Without such a lemma, recursively harvesting grandparents would be a heuristic, not a theorem.

---

## 10. Model / scheduler capability honesty

The exposed scheduler interface still has fields for title, prompt, schedule, timing mode, and enabled state, but no model selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt-requested only in this environment. This run's authenticated model identity is GPT-5.6 Sol; reasoning effort is not exposed, so it is reported as `UNVERIFIED`.

Changing the scheduler-level model/reasoning setting would require a platform capability or workspace/runtime control not present in the exposed automation API; a repository edit cannot do it.

The repository policy also records that modification probes for P26, P01, and P03 returned `You cannot modify this task`. The authorized workaround is to resolve task/account/workspace ownership through the product's permitted interface or platform support. Creating a duplicate schedule or bypassing the restriction is not an authorized workaround. No scheduler change was attempted in this run.

---

## 11. Ledger delta for designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | metric gamma_E lower bound | b9 -> b10=b6+a(a+1)pi_c^3 S/A^2 > b9 | PARTIAL / SOURCE OPEN | methods B13,B15,B4 | artifact f8075151e54da64809ad1cfe161237f270e7a154`

No root ledger was directly modified.

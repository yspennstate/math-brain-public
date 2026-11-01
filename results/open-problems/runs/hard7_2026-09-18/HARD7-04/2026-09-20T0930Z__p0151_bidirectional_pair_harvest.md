Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b10 -> gamma_E >= b11>b10`**; methods actually tried: **B22 / B27 / B10**.

# HARD7-04 bounded research iteration — bidirectional current-pair historical harvest

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The theorem-sized proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_bidirectional_pair_harvest_20260920T0930Z.md`

created at commit

`f9cf13729fff6cb0a04d978af0406b777126fea4`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and repository state consumed

I resumed the exclusive canonical claim `operations/claims/P0151.md`, owned by `HARD7-04`. I did not restart I0049, I0048, any solved degree-count target, Kemeny/extremal-hitting-time work, or the independently attached-edge growing-graph model.

Before the new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the intake/catalog trace containing `P0151|3|critical window, fixed-outdegree PA`;
- `operations/claims/P0151.md`;
- the neighboring PA report `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`, which treats the threshold-level I0048 scope as later-literature-known and does not own P0151;
- the latest own report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0832Z__p0151_incidence_strengthened_parent_ticket.md` and its matching artifact;
- the current HARD7-04 run directory immediately before writing. No later own-track report or competing P0151 claim was present.

`POSTED.md` contains no source-equivalent P0151 paper. No shared root ledger was edited; the ledger delta below is for the designated maintainer only.

---

## 2. Source statement and current-literature refresh — 20 September 2026

The source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The canonical P0151 source statement records Ray's future-work formulation, **“It would be interesting to study the critical regime of preferential attachment models”**, with the retained exact problem being the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this fixed-outdegree sequential model.

Fresh bounded searches on **20 September 2026** rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact fixed-outdegree threshold and giant/no-giant transition, not a finite-size critical-window theorem for this exact model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025: `(log n)^(-2)` window and `sqrt(n)/log n` critical scale when a new vertex connects independently to earlier vertices. That independence assumption does not automatically include the exact fixed-`m` sequential birth law here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026: a different inhomogeneous PA-kernel ensemble in the `tau in (2,3)` regime with a moving threshold.
4. Ray, *Stochastic processes on preferential attachment models*, arXiv:2411.14111 / 2024 thesis: the source-side preferential-attachment stochastic-process program.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`.

The frozen source-relevant quantity is

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Inherit

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1,d_*A/[4(a+m)pi^3])`,

`kappa_1:=2vartheta(a+m)pi^3/A`,

`d_7:=1/2-(b_U+kappa_1)`,

`lambda:=min(1,d_7A/[4(m-1)(a+m)pi^3])`,

`S:=vartheta+(m-1)lambda`,

`eta_10:=a(a+1)pi^3S/A^2`,

`kappa_10:=2(A+1)pi^3S/A`,

`b10:=b6+eta_10`,

and the proved upper coefficient

`U_10:=b_U+kappa_10<1/2`.

Define

`M_10:=1/2-U_10>0`,

`rho:=min(1,M_10/[2kappa_10])`,

and

`b11:=b10+rho eta_10`.                                           (3.1)

This run proves

`gamma_E>=b11>b10`,                                               (3.2)

with exact positive gap

`b11-b10=rho a(a+1)pi_c^3 S/A^2>0`.                             (3.3)

It also proves `b11<1/2`.

Thus the metric moves strictly:

**Before:** `gamma_E>=b10`.

**After:** `gamma_E>=b11>b10`.

The unchanged-run counter resets.

---

## 4. Idea written before any validation

The previous theorem used only one orientation of current labels `{1,2}`: label 1 gated into the connected shadow and label 2 bridged to a simple-good outside root, after which fresh historical parent edges of that root were harvested with inverse-weight tickets.

The new observation is that the reverse orientation is exactly disjoint:

`E_12(u)={1 gate, 2 bridge to u}`,

`E_21(u)={1 bridge to u, 2 gate}`.

No `E_12(u)` can coexist with any `E_21(u')`, because label 1 (and label 2) would have to target both the frozen inside set and an outside root. Therefore the reverse orientation can carry a genuinely additive historical reward. To keep the full all-parameter second-moment architecture valid, the reverse ticket family is deterministically throttled by the already proved residual upper-drift margin.

No checker was manufactured because this is an analytic theorem over the full parameter family, not a finite certificate.

---

## 5. B22 — read the failure: all ordered pairs cannot simply be multiplied

I first tried to harvest historical parents from all `m(m-1)` ordered current gate/bridge pairs. That shortcut fails without a new collision theorem: different ordered pairs can occur in the same birth and can lead to the same bridged root or same historical parent. Pairwise distinctness of one root's historical parents does not make current ordered-pair rewards globally disjoint.

The Jorritsma--Maillard--Mörters independent-edge theorem does not repair this for the exact source model, because fixed outdegree and within-birth updates create dependencies absent from their birth law.

**Outcome B22:** failed as a full `m(m-1)` amplification, but identified exact event disjointness as the quantity that must replace heuristic independence.

---

## 6. B27 — swap the orientation quantifier

Instead of requiring the directed condition “label 1 gate, label 2 bridge,” require only that among labels `{1,2}` one is the gate and the other is the bridge.

For a simple-good root `u`, the reverse orientation satisfies the same first-order lower bound as the forward one:

`P(E_21(u)|F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`,                               (6.1)

because edge 1 first targets/accepts the outside root with probability at least `pi c(w_u)/(At+K)`, leaves frozen shadow attractiveness `W_t` unchanged, and edge 2 then gates into the shadow with probability at least `pi W_t/(At+K)`.

After `E_21(u)`, the historical percolation bits of `u` are still fresh and may be exposed exactly as in the previous theorem.

**Outcome B27:** succeeded. The source exploration admits a rigorously disjoint reverse current-pair orientation, with no independent-edge approximation.

---

## 7. B10 — derandomize the safe extra strength from the residual margin

Let the existing historical ticket strengths be `q_1=vartheta`, `q_j=lambda` for `j>=2`. On the reverse event use the scaled ticket

`rho q_j(a+1)/w_{p_j(u)}(t)`.

Every historical parent has attractiveness at least `a+1`, so this is a valid probability. Its conditional frozen expected reward is exactly

`pi rho q_j(a+1)`.

Summing historical labels gives reverse raw reward `pi rho(a+1)S`. Using (6.1) and the inherited simple-good-root supply estimate yields the extra lower drift

`rho eta_10 W_t/t`

up to the same lower-order `W_t^2/t^2`, `W_tZ_t/t^2`, `W_tN_t^rep/t^2`, `W_t/t^2`, and `1/t` terms as before. Disjointness from the forward orientation makes this reward genuinely additive, proving lower coefficient `b11`.

The reverse upper coefficient is at most `rho kappa_10`. Hence

`U_11:=U_10+rho kappa_10
 <=1/2-M_10/2
 <1/2`.                                                          (7.1)

The inverse-weight square-jump estimate remains controlled by the inherited global budget `E V_t=O(t)`, so

`E W_t^2=O(t)`.                                                    (7.2)

The mean recurrence becomes

`mu_{t+1}
 >=[1+b11/t-C/t^2]mu_t
   -C/t-Ct^(h-1)-C log(t)/t`,                                    (7.3)

with `h=m/A<1/2`. The inherited gate-only seed exponent is strictly larger than `h`, so the same normalized recurrence bootstrap gives

`E W_n>=c n^b11`.

The retained-gate activation conversion then gives a connected percolation component with expected size at least `c'n^b11`, proving (3.2).

Finally,

`eta_10/kappa_10=a(a+1)/[2A(A+1)]<1/2`,

and therefore `b11<U_11<1/2`.

**Outcome B10:** succeeded. Residual-margin throttling closes the full parameter range without numerical sampling or an unproved deeper-ancestry lemma.

---

## 8. Validation actually performed

There is no finite claim in this run. Validation consisted of:

- an exact event-disjointness check for the two orientations;
- a full all-parameter upper-margin calculation `U_11<1/2`;
- the inherited square-budget verification with the scaled reverse ticket;
- a fresh source/current-literature search separating fixed-outdegree sequential PA from independent-edge growing-graph theorems;
- exact GitHub readback of the full analytic artifact at commit `f9cf13729fff6cb0a04d978af0406b777126fea4`.

No finite-size fit, simulation, or sampled parameter grid is used as evidence for the theorem.

---

## 9. Remaining full-scope gap

The source problem remains **OPEN**. This run does not prove:

- `gamma_E=1/2`;
- a matching upper bound;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` critical window for the exact fixed-outdegree sequential model;
- tightness or a scaling-limit law;
- a transfer theorem from the independent-edge growing-graph model.

The next genuinely different local obstruction is a **current-birth collision packing lemma**: quantify how much first-order historical reward can be harvested from a matching/packing of several current gate/bridge label pairs while charging each newly captured root/ancestor once. A deeper alternative remains the previously identified depth-two ancestral-supply problem. A subsequent run should use a fresh triple; unused P0151 moves include B8, B9, B16, B17, B21, B23, B26 and B29.

---

## 10. Model / scheduler capability honesty

The exposed task interface still provides scheduling/task fields but no model selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt-requested only; this run actually identifies as **GPT-5.6 Sol**, and reasoning effort is **UNVERIFIED**.

The repository's latest configuration ledger records that P26 had a historical `You cannot modify this task` failure in one authorization context but was later successfully updated from an authorized context. For any task that still returns that denial, the compliant workaround is the owning/authorized account or workspace UI, or platform support; creating a duplicate job or bypassing permissions is not an authorized workaround. No scheduler change was attempted in this run.

---

## 11. Ledger delta for designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b10 -> b11=b10+rho*a(a+1)*pi_c^3*S/A^2 > b10 | PARTIAL / SOURCE OPEN | methods B22,B27,B10 | artifact f9cf13729fff6cb0a04d978af0406b777126fea4`

No root shared ledger was modified.
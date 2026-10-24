Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b2 -> gamma_E >= b3` with `b3>b2`**; methods actually used: **B1 / B15 / B30**.

# HARD7-04 bounded research iteration — ticket-thinned recent-bridge exploration for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This report proves a new restricted lower bound for the exact admitted fixed-outdegree sequential preferential-attachment model. It does **not** identify the full critical window, a matching upper bound, tight component scaling, or a limiting law. No simulation is used as proof. No finite checker was created because the substantive claim is analytic and the proof is on the page.

## 1. Continuity, ownership, exclusions, and source check

I resumed the exclusive canonical claim `operations/claims/P0151.md` owned by `HARD7-04`. I reread the controlling HARD7 files, root `POSTED.md` / `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, the P0151 intake/catalog records, the newest own reports

- `runs/hard7_2026-09-18/HARD7-04/2026-09-19T2228Z__bhs_handoff_p0151_block_activation.md`,
- `runs/hard7_2026-09-18/HARD7-04/2026-09-19T2330Z__p0151_tangent_bootstrap.md`,

and the newest repository ownership/status screens mentioning P0151. The claim remains owned by HARD7-04; no competing canonical owner or posted equivalent surfaced. I did not return to the retired P0157, configuration-model MST, I0049, or known independent-edge special cases.

The frozen source model remains Ray's sequential fixed-outdegree affine preferential-attachment model `PA_n^(m,delta)(d)` with fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential edges from each arriving vertex to older vertices, attachment probabilities proportional to current degree plus `delta`, and independent bond retention `pi`. Put

`a := m+delta`, `A := 2m+delta`.

Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models* (EJP 31, 2026; arXiv:2312.14085), prove

`pi_c = delta / ( 2*( m*(m+delta) + sqrt(m*(m-1)*(m+delta)*(m+1+delta)) ) )`.

Their mean-offspring kernel and spectral calculation identify `1/pi_c` but do not give the finite-size critical window for this fixed-outdegree sequential ensemble. Their extended Pólya-point-tree eigenfunction is proportional to `x^(-1/2)`, which is useful structural evidence for why a one-shadow recursion should be improvable, but I do not use local-limit heuristics as a finite-graph proof.

Fresh bounded searches through **20 September 2026** rechecked the exact fixed-outdegree model against: Hazra--van der Hofstad--Ray; Jorritsma--Maillard--Mörters, arXiv:2512.18937 (independent connections to earlier vertices, `(log n)^(-2)` window and `sqrt(n)/log n` critical largest component); Banerjee--Bhamidi--van der Hofstad--Ray, arXiv:2512.15561 (uniform-attachment subcritical coagulation); Mörters--Schätze, arXiv:2606.27844 (different inhomogeneous preferential-attachment kernel in the infinite-variance regime); and the older near-critical attachment-rule model of Eckhoff--Mörters--Ortgiese. I did not locate this ticket-thinning/recent-bridge lower bound or a source-matching fixed-outdegree critical-window theorem. This is bounded negative evidence only, not a novelty certificate.

## 2. Frozen quantity and before/after

Let `C_max(n,pi_c)` be the largest component after bond percolation at the exact threshold, and keep the admitted metric

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved

`gamma_E >= b2 := [m + a*m*pi_c]/A`.                                      (2.1)

This run proves the strictly stronger lower bound

`gamma_E >= b3 := b2 + (a*pi_c/A) * [ 1 - (1-a*pi_c/A)^(m-1) ]`.           (2.2)

The added term is strictly positive for `m>=2`, `delta>0`. In fact the proof below also shows `b3<1/2`, so this remains a restricted lower-bound advance rather than identification of the expected `1/2` power suggested by neighboring independent-edge models.

For orientation only, not proof: at `m=2, delta=1`,

`pi_c = 0.045875854768...`,
`b2 = 0.455051025722...`,
`b3 = 0.455808679580...`.

---

## 3. Negation test before the successful route

The obvious way to exploit an activated birth is to add every retained outside target of that birth to the shadow component with its **full current attractiveness**. This indeed creates a new first-order bridge term, but it destroys the bounded-increment estimate used in the previous second-moment bootstrap: a captured old target can have degree of polynomial size. Thus the naive full-attractiveness bridge route does not justify the needed quadratic-error control.

The repair is to change category: carry only an **artificial ticket mass** that is always dominated by true attractiveness. This keeps the exact preferential-attachment target probabilities available after an auxiliary thinning while making every shadow increment uniformly bounded.

This failed full-attractiveness attempt is important because the new proof below is not merely the previous tangent argument with another term inserted; the ticket construction is what makes the bridge term rigorous.

---

# 4. B1 — change category: a ticket-thinned connected exploration

Fix a deterministic starting time `t0` after the initial seed, and start from one ordinary vertex born with outdegree `m`. We construct, on an extension by independent auxiliary uniforms, a connected set `Q_t` contained in one true percolation component and ticket weights `ell_u(t)` for `u in Q_t` satisfying

`0 <= ell_u(t) <= d_u(t)+delta`.                                    (4.1)

Write

`S_t := sum_{u in Q_t} ell_u(t)`, `N_t := |Q_t|`.                  (4.2)

Every newly admitted vertex receives base ticket mass `a=m+delta`; ticket mass can only increase afterward. Hence, up to the single initial seed,

`N_t <= S_t/a + 1`.                                                 (4.3)

### Ticket-hit rule

At the beginning of the birth of `v=t+1`, freeze `Q_t` and the ticket weights `ell_u(t)` for the duration of its `m` attachment trials. Suppose trial `j` targets `u in Q_t`. If the current attractiveness of `u` immediately before that trial is `d_u+delta`, declare the trial a **ticket hit** with auxiliary probability

`ell_u(t)/(d_u+delta)`.

Because the actual target probability is `(d_u+delta)/D_{t,j}`, where the source-model denominator `D_{t,j}` is deterministic given `t,j` up to the fixed initial offset, the conditional probability of a ticket hit on every trial is exactly

`S_t / D_{t,j}`.                                                    (4.4)

After the birth, increase the ticket weight of an old target by one for every ticket hit it received. This preserves (4.1), because each ticket hit is also a genuine degree increment.

Let `K_t` be the number of ticket hits among the `m` trials. Let `I_t` be the indicator that at least one ticket-hit edge is retained by percolation. If `I_t=1`, add the new vertex `v` to `Q` at the end of the birth and assign it ticket mass `a`. Since a retained ticket-hit edge joins `v` to the old connected set, connectivity is preserved.

The source denominators satisfy, for a fixed `K<infinity`,

`A t-K <= D_{t,j} <= A t+K`                                        (4.5)

for all large `t` and all `j=1,...,m`.

Therefore

`E[K_t | F_t] >= m S_t/(At+K)`,                                   (4.6)

and the retained ticket-hit activation law has the same tangent coefficient as in the preceding run, but now for a bounded-increment artificial mass.

---

# 5. B15 + B30 — break symmetry and localize to a recent-age block

Fix `rho in (0,1)` and define the recent block

`R_t(rho) := {ceil((1-rho)t), ..., t}`.                             (5.1)

Every vertex in this block has underlying degree at least `m`, hence attractiveness at least `a`.

We deliberately break the symmetry of the `m` birth edges. Edge 1 is the **gate**. After the birth, set `J_t=1` if

1. edge 1 is a retained ticket hit on `Q_t`, and
2. at least one of edges `2,...,m` is retained and targets a vertex in `R_t(rho)\Q_t`.

When `J_t=1`, add exactly one such old target to `Q` and assign it base ticket mass `a`. The gate edge first connects the new vertex to `Q_t`; the retained bridge edge then connects the captured old target through the new vertex. Thus every added vertex lies in the same true percolation component.

The ticket recursion is now exact:

`S_{t+1} = S_t + K_t + a I_t + a J_t`.                             (5.2)

In particular,

`0 <= S_{t+1}-S_t <= m+2a`.                                        (5.3)

This bounded increment is the reason for using tickets instead of full captured attractiveness.

## 5.1 Lower bound for the bridge event

Condition on `F_t`. Edge 1 is a retained ticket hit with probability at least

`pi S_t/(At+K)`.                                                    (5.4)

Before the new birth, the total attractiveness of recent vertices outside the shadow is at least

`a ( |R_t(rho)| - N_t )_+`.                                        (5.5)

During later trials this quantity cannot decrease. Therefore, conditional on the gate event and on failure of previous bridge attempts, each of edges `2,...,m` has probability at least

`z_t := pi*a*(|R_t(rho)|-N_t)_+/(At+K)`                            (5.6)

of being a retained edge to `R_t(rho)\Q_t`. Consequently

`P(J_t=1 | F_t)
 >= [pi S_t/(At+K)] * [1-(1-z_t)^(m-1)]`.                          (5.7)

Set

`z_rho := rho*a*pi/A`,
`g(z) := 1-(1-z)^(m-1)`.                                           (5.8)

The function `g` is increasing and `(m-1)`-Lipschitz on `[0,1]`. Since `|R_t(rho)| >= rho t-O(1)`, (4.3), (4.5), and (5.6) give

`g(z_t) >= g(z_rho) - C*(N_t/t + 1/t)`                             (5.9)

with the convention that a negative right side is harmless because `g(z_t)>=0`. Therefore

`P(J_t=1 | F_t)
 >= [pi*g(z_rho)/A] * S_t/t
    - C*S_t*N_t/t^2 - C*S_t/t^2
 >= [pi*g(z_rho)/A] * S_t/t
    - C*S_t^2/t^2 - C*S_t/t^2`.                                   (5.10)

The final step uses (4.3).

Outcome of B15/B30: a single retained gate edge plus one retained edge into a **linear-size recent block** creates a new first-order drift term while the bad event “too much of the recent block is already in the shadow” costs only a quadratic `S_t^2/t^2` error.

---

# 6. Second moment for the ticket mass

The lower drift will again contain a quadratic error, so we first prove that `E S_t^2=O(t)` at `pi=pi_c`.

For an upper drift bound, (4.4)--(4.5) give

`E[K_t|F_t] <= m S_t/(At-K)`.                                      (6.1)

Also `I_t` is at most the number of retained ticket hits, so

`E[I_t|F_t] <= m*pi*S_t/(At-K)`.                                   (6.2)

Finally, `J_t=1` requires the gate edge to be a retained ticket hit and at least one of the other `m-1` edges to be retained. By a union bound on the latter retention marks,

`E[J_t|F_t] <= (m-1)*pi^2*S_t/(At-K)`.                             (6.3)

Thus

`E[S_{t+1}-S_t | F_t]
 <= r_u S_t/(At-K)`,                                                (6.4)

where

`r_u := m + a*m*pi + a*(m-1)*pi^2`,
`c_u := r_u/A`.                                                     (6.5)

At `pi=pi_c`, `c_u<1/2`. Here is a direct check from the exact threshold, included to keep the proof self-contained. Put

`s := sqrt(m(m-1)a(a+1))`, so `pi_c=delta/[2(ma+s)]`.

First,

`m*pi_c < 1/3`.                                                     (6.6)

Indeed `2ma>2m delta`, while `2s>m delta` because `s>delta sqrt(m(m-1))` and `2 sqrt(m(m-1))>m` for `m>=2`. Hence `2(ma+s)>3m delta`.

Second,

`a*m*pi_c < 3 delta/8`.                                            (6.7)

This follows from `3s>ma`; in fact

`s^2/(m^2 a^2)=((m-1)(a+1))/(ma)>1/2`.

Therefore

`a[m*pi_c+(m-1)pi_c^2]
 < a*m*pi_c*(1+pi_c)
 < (3 delta/8)*(4/3)
 = delta/2`.                                                        (6.8)

So `r_u<m+delta/2=A/2`, proving `c_u<1/2`.

Let `Delta_t=S_{t+1}-S_t`. By (5.3), `Delta_t<=B:=m+2a`. Squaring and using (6.4),

`E[S_{t+1}^2|F_t]
 <= S_t^2 + 2S_t*r_u S_t/(At-K) + B^2`.                            (6.9)

Choose `c` with `2c_u<c<1`. For all sufficiently large `t`,

`Y_{t+1} <= (1+c/t)Y_t+B^2`, `Y_t:=E S_t^2`.                      (6.10)

A standard induction yields

`E S_t^2 = O(t)`.                                                   (6.11)

---

# 7. Lower drift and the improved exponent

The activation event `I_t` has first-order coefficient `m*pi`. A Bonferroni bound over the `m` retained ticket-hit events gives

`P(I_t=1|F_t)
 >= m*pi*S_t/(At+K) - C*S_t^2/t^2`.                                (7.1)

Combine (4.6), (5.10), (7.1), and (5.2). Define

`eta_rho := (a*pi/A) * [1-(1-rho*a*pi/A)^(m-1)]`,                  (7.2)

`b_rho := b2 + eta_rho`,
`b2 := [m+a*m*pi]/A`.                                               (7.3)

Then, at `pi=pi_c`,

`E[S_{t+1}-S_t|F_t]
 >= b_rho*S_t/t - C*S_t/t^2 - C*S_t^2/t^2`.                        (7.4)

Using (6.11) and writing `mu_t=E S_t`,

`mu_{t+1}
 >= (1+b_rho/t-C/t^2) mu_t - C/t`.                                (7.5)

## 7.1 Polynomial seed for the bootstrap

The same ticket process has a global chord lower bound even if the bridge term is discarded. Conditional retained ticket-hit probability on each trial is at least `pi S_t/(At+K)`. Hence, with

`q(pi):=1-(1-pi)^m`,

`P(I_t=1|F_t) >= q(pi) S_t/(At+K)`.                                (7.6)

Together with (4.6), this gives

`E S_t >= c t^b1`,
`b1 := [m+a*q(pi_c)]/A >0`.                                        (7.7)

Now let

`G_{t+1}=G_t(1+b_rho/t-C/t^2)`                                    (7.8)

from a sufficiently large deterministic start time. Then

`G_t=Theta(t^b_rho)`.                                               (7.9)

Dividing (7.5) by `G_{t+1}` yields

`mu_{t+1}/G_{t+1}
 >= mu_t/G_t - C/(t G_{t+1})`.                                    (7.10)

The error tail after time `T` is `O(T^(-b_rho))`. The seed satisfies

`mu_T/G_T >= c T^(b1-b_rho)`.                                     (7.11)

Their ratio is of order `T^b1 -> infinity`. Choose one fixed large `T` so the normalized seed is more than twice the full remaining error tail. Then (7.10) gives

`E S_n >= c_rho n^b_rho`                                           (7.12)

for all sufficiently large `n`.

## 7.2 Convert ticket mass to actual component size

Each activation adds the new vertex to `Q`. The gate event from edge 1 alone gives

`E[N_{t+1}-N_t|F_t]
 >= P(edge 1 is a retained ticket hit|F_t)
 >= pi S_t/(At+K)`.                                                (7.13)

Using (7.12) and summing,

`E N_n >= c'_rho n^b_rho`.                                         (7.14)

By construction `Q_n` is contained in a true percolation component, and that component is no larger than `C_max`. Therefore

`gamma_E >= b_rho`                                                  (7.15)

for every fixed `rho in (0,1)`.

Letting `rho` increase to one gives

`gamma_E >= b3
 := b2 + (a*pi_c/A)*[1-(1-a*pi_c/A)^(m-1)]`.                       (7.16)

This is (2.2).

Strict movement is immediate because the added term is positive. Moreover, by Bernoulli's inequality,

`eta_1 <= (a*pi_c/A)*(m-1)*(a*pi_c/A)
       < a*(m-1)*pi_c^2/A`,                                        (7.17)

since `a/A<1`. Thus `b3<c_u<1/2` by Section 6.

---

# 8. What moved, and what remains unpaid

### Source-relevant movement

Before:

`gamma_E >= b2 = [m+a*m*pi_c]/A`.

After:

`gamma_E >= b3 = b2 + (a*pi_c/A)[1-(1-a*pi_c/A)^(m-1)] > b2`.

This is genuine movement of the same frozen quantity under the same graph, distribution, percolation parameter, and normalization.

### What did not move

This does **not** prove:

- `gamma_E=1/2`;
- the `(log n)^(-2)` critical-window width;
- `sqrt(n)/log n` largest-component scale;
- tightness or a scaling-limit law;
- transfer of Jorritsma--Maillard--Mörters from independent-edge growing graphs to fixed-outdegree sequential PA.

The new mechanism identifies a more precise next obstruction. A one-birth gate can harvest one old recent vertex through sibling edges, but its exponent gain is still strictly below the upper second-moment coefficient and below `1/2`. Reaching the spectral `x^(-1/2)` scale appears to require either repeated multi-bridge harvesting within a birth with collision control, or a genuinely two-type age-weighted exploration that tracks both older and younger directions of the Pólya-point-tree eigenfunction.

---

# 9. Method accounting

- **B1 CHANGE THE CATEGORY:** replaced true shadow attractiveness by a ticket mass dominated by it, implemented by exact auxiliary thinning; this restored bounded increments while keeping exact attachment hazards.
- **B15 BREAK THE SYMMETRY ON PURPOSE:** designated edge 1 as the retained ticket-hit gate and used later sibling edges as bridge candidates. The asymmetry avoids circular within-birth bookkeeping.
- **B30 ONE SCALE / ONE DIRECTION AT A TIME:** restricted captured old vertices to a recent block of density `rho`, whose outside attractiveness has a deterministic linear lower bound. Sending `rho->1` only after proving every fixed-`rho` theorem gives the final coefficient.

This triple is new for P0151 and differs from the preceding run's `B5/B12/B20` and the admission run's `B2/B7/B19`.

---

# 10. Validation, capability honesty, and next checkpoint

Self-check performed in this run:

1. verified ticket domination (4.1) is preserved under old-target hits, new-vertex activation, and old-vertex capture;
2. verified every shadow addition is connected by retained edges at the end of the same birth;
3. checked the bridge deficit from already-shadowed recent vertices becomes `O(S_t^2/t^2)` using `N_t<=S_t/a+1`;
4. checked the exact threshold inequalities needed for `c_u<1/2`;
5. checked the normalization/bootstrap tail: seed `T^(b1-b_rho)` dominates error `T^(-b_rho)` because `b1>0`;
6. checked the illustrative `m=2,delta=1` numbers separately; they are not part of the proof.

No independent other-track audit has been performed, so status remains **PARTIAL**.

The currently exposed automation/tool interface still has **no model selector and no reasoning-effort selector**; GPT-6 maximum is only requested in prompt text. It exposes scheduling/prompt/timing/enabled-state controls, not a model/effort field or guaranteed duration. A real GPT-6/maximum enforcement change therefore requires a platform-level scheduler capability or an authorized product/workspace interface that exposes those fields; a repository edit cannot do it. The controlling repository policy records historical `You cannot modify this task` failures for P26/P01/P03 in one native context; the authorized workaround is to resolve task/account/workspace ownership in the permitted interface or through platform support, **not** to bypass the restriction or create duplicate schedules. I made no scheduler changes in this run.

### Next mathematical route

Do **not** repeat B1/B15/B30 next run. The strongest immediate successor is to allow more than one captured recent vertex in the same activated birth while assigning only bounded tickets, then compute whether the full first-order sibling-harvest coefficient can be summed without losing the `E S_t^2=O(t)` closure. A materially different alternative is an age-weighted two-type ticket potential modeled on the positive `x^(-1/2)` eigenfunction of the extended Pólya-point-tree offspring operator.

### ledger_delta

```yaml
track: HARD7-04
source: P0151
status: PARTIAL
metric: gamma_E_lower_bound
before: "b2 = [m+(m+delta)*m*pi_c]/(2m+delta)"
after: "b3 = b2 + ((m+delta)*pi_c/(2m+delta))*(1-(1-((m+delta)*pi_c/(2m+delta)))^(m-1))"
movement: strict
methods: [1, 15, 30]
claim_owner: HARD7-04
shared_root_mutation: false
closure: false
```

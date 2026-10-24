Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT on the frozen P0151 metric: `gamma_E>=b13` before and after; fresh methods actually tried: B9 / B14 / B21.**

# HARD7-04 bounded research iteration — exact killed-PPT boundary Green scale

Status: **PARTIAL / SOURCE OPEN**. This run does not move the finite-graph exponent lower bound, but it proves an exact new source-relevant local theorem: for the critical killed Pólya-point-tree of the exact fixed-outdegree model, the expected total progeny from the oldest log-age boundary is asymptotic to an explicit positive constant times `sqrt(n)/log n` under `L=log n`, while the age-uniform susceptibility remains bounded. This identifies, inside the exact fixed-outdegree local operator itself, the same component-size scale suggested by the independent-edge growing-graph theory. The missing step is finite-graph transfer.

The full theorem-sized analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_killed_ppt_boundary_green_20260920T1232Z.md`

created at commit

`13bcdd367a021b324f430b79f153f2674bae5d33`

and read back successfully at that exact SHA before this report was written.

No finite exhaustive claim is made in this run, so no checker was manufactured merely for bookkeeping.

---

## 1. Continuity, ownership, and repository state consumed

I resumed the exclusive canonical claim `operations/claims/P0151.md`, still owned by `HARD7-04`. I did not restart I0049, solved degree-count statements, Kemeny/extremal-hitting-time work, P0157, or the independently attached-edge growing-graph model.

Before the new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the P0151 intake/catalog trace `P0151|3|critical window, fixed-outdegree PA`;
- `operations/claims/P0151.md`;
- the immediately preceding own report `2026-09-20T1130Z__p0151_degree_distribution_slack.md` and its proof/check artifacts;
- the earlier exact killed-PPT spectral artifact `p0151_log_age_killed_ppt_spectral_window_20260920T0330Z.md`;
- neighboring random-graph work, in particular R14's current P0157 configuration-model barely-subcritical target, which is a different source problem and does not collide with P0151;
- a fresh current-branch HARD7-04 commit search immediately before this report. The newest HARD7-04 commit was the present analytic artifact `13bcdd367a021b324f430b79f153f2674bae5d33`; no competing P0151 owner or later own checkpoint appeared.

`POSTED.md` contains no source-equivalent P0151 paper. No root shared ledger, peer-track file, schedule, email, or Drive object was edited.

---

## 2. Exact source target and current-literature refresh — 20 September 2026

The frozen source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold remains

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The retained source target is the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this exact sequential fixed-outdegree model.

A fresh bounded literature check dated 20 September 2026 rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact threshold and giant/no-giant transition for the fixed-outdegree model, not a finite-size critical-window theorem.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025: `(log n)^(-2)` window, `sqrt(n)/log n` largest-component scale, finite critical susceptibility, and killed branching-random-walk analysis for a class where new vertices connect independently to earlier vertices. That independent-connection hypothesis does not automatically include the exact fixed-`m` sequential birth law here.
3. Mörters--Schätze, arXiv:2606.27844, submitted 26 June 2026: a different inhomogeneous preferential-attachment-kernel ensemble in the infinite-variance regime.

Additional bounded searches for Pólya-point-tree critical susceptibility and fixed-outdegree `sqrt(n)/log n` critical percolation did not surface a source-matching finite fixed-outdegree critical-window resolution or the exact Green-function formula below. This is bounded negative evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric — exact before/after

The fixed source-relevant metric remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`.

The preceding run proved

`gamma_E>=b13`.

This run works at the exact critical Pólya-point-tree mean-operator level and does **not** yet prove the finite-graph coupling needed to transfer the new `sqrt(n)/log n` local asymptotic. Therefore the honest metric record is

**Before:** `gamma_E>=b13`.

**After:** `gamma_E>=b13` — **NO MOVEMENT**.

This is the first unchanged run after the preceding strict movement, so Section I is not triggered.

---

## 4. Counterexample-oriented question attacked first

The earlier exact spectral result gives, for the critical killed Pólya-point-tree operator on a log-age interval of width `L`,

`1-r(R_L)=C_spec/L^2+O(L^-3)`.

A generic resolvent bound therefore has size `Theta(L^2)`. If the constant forcing in the total-progeny equation projected onto the slow mode with order-one boundary amplitude, the oldest-particle total progeny could acquire an extra `L` or `L^2` factor relative to the critical harmonic weight `exp(L/2)`. That would **falsify** the hoped-for `exp(L/2)/L` local scale and undermine the killed-PPT route.

So the substantive negation test was:

> Does the exact fixed-outdegree killed-PPT resolvent produce a different logarithmic normalization from `exp(L/2)/L` because the spectral gap is only order `L^-2`?

The exact calculation below answers **no**. The forcing and the two boundary conditions cancel the dangerous slow-mode amplification; the surviving boundary Green amplitude is precisely order `1/L`.

---

## 5. New exact theorem

Put

`a:=m+delta`, `A:=2m+delta`, `alpha:=delta/(2A)`,

and use the fixed-outdegree Pólya-point-tree constants

`c:=m a/A`,
`d:=m(a+1)/A`,
`e:=(m-1)a/A`,
`g:=sqrt(de)`,
`lambda0:=c+g`,
`q:=c/lambda0`, `p:=g/lambda0`.

Let

`r_O:=sqrt(d)`, `r_Y:=sqrt(e)`,
`c_O:=1/r_O`, `c_Y:=1/r_Y`, `C_g:=c_O+c_Y`.

At `pi=pi_c=alpha/lambda0`, let `R_L` be the Pólya-point-tree mean operator killed outside log-age `[0,L]`. Let `F_s^L(u)` be the expected total progeny, including the ancestor, from type `s` at log-age `u`.

With

`E_L:=1-exp(-L/2)`

and

`B_L=[2 alpha c_Y E_L
      +2 alpha^2 p C_g(2E_L-L exp(-L/2))]
     /(1+alpha p L)`,

the exact oldest-boundary values are

`F_O^L(L)=1+r_O p exp(L/2) B_L`,

`F_Y^L(L)=1+r_Y q exp(L/2) B_L`.

Furthermore

`L B_L -> B_*:=2 c_Y/p+4 alpha C_g>0`,

and hence

`F_O^L(L) ~ K_O exp(L/2)/L`,

`F_Y^L(L) ~ K_Y exp(L/2)/L`,

where

`K_O=r_O p B_*`, `K_Y=r_Y q B_*`.

Thus under the finite-graph cutoff identification `L=log n`, the **exact local fixed-outdegree operator** has oldest-boundary susceptibility

`F_s^{log n}(log n) ~ K_s sqrt(n)/log n`.

The same solution also proves a uniform local bound

`F_s^L(u)<=C(m,delta) exp(u/2)`, `0<=u<=L`,

so if `U_L` is age-uniform, with log-age density `exp(-u)/(1-exp(-L))`, then

`sup_L E F_s^L(U_L)<infinity`.

Therefore the exact killed-PPT already exhibits **both**:

- oldest-boundary scale `sqrt(n)/log n`;
- bounded typical-age critical susceptibility.

This is an auxiliary local theorem, not a finite-graph critical-window theorem.

---

## 6. B9 — RANDOMIZE: solve the total-progeny problem after the critical Doob transform

The exact critical harmonic function is

`h_s(u)=r_s exp(u/2)`.

Writing `F_s=h_s phi_s` converts the total-progeny equation

`F=1+R_L F`

into an inhomogeneous resolvent for the centered two-state Markov-additive Doob kernel:

`phi=g+K_L phi`,

with

`g_s(u)=c_s exp(-u/2)`.

For

`A(u)=int_u^L alpha exp[-alpha(v-u)]phi_O(v)dv`,

`B(u)=int_0^u alpha exp[-alpha(u-v)]phi_Y(v)dv`,

one gets exactly

`A'=alpha p(A-B)-alpha g_O`,

`B'=alpha p(A-B)+alpha g_Y`,

with `B(0)=0`, `A(L)=0`.

**Outcome B9:** succeeded. The branching-process Green function is reduced to an exact killed centered random-walk boundary-value problem rather than estimated through a generic resolvent norm.

---

## 7. B14 — FIND THE GROUP ACTING: use the two-state symmetry to collapse the resolvent

The Doob transition matrix is

`Q=[[q,p],[p,q]]`.

The swap symmetry makes the difference coordinate

`D:=A-B`

exactly solvable, because the homogeneous terms cancel:

`D'(u)=-alpha C_g exp(-u/2)`.

With `D_0=D(0)`, the boundary conditions give

`D_0=[2 alpha c_O E_L
      +2 alpha^2 p C_g(L-2E_L)]
     /(1+alpha p L)`.

At `u=L`, `A(L)=0`, so `B_L=-D(L)`, which simplifies to the exact formula in Section 5. The numerator is positive because

`2E_L-L exp(-L/2)=2[1-(1+L/2)exp(-L/2)]>0`.

The asymptotic `B_L~B_*/L` is then immediate.

**Outcome B14:** succeeded. The dangerous `L^2` generic resolvent scale collapses to the exact `1/L` boundary amplitude after symmetry and forcing are accounted for.

---

## 8. B21 — ASK WHO ELSE HAS THIS SHAPE: killed branching-random-walk criticality

The independent-edge theorem of Jorritsma--Maillard--Mörters has the same three signatures: `(log n)^(-2)` window, `sqrt(n)/log n` largest critical components, and finite susceptibility. It cannot be imported theorem-for-theorem because fixed-outdegree sequential births are dependent.

The productive transfer is instead conceptual: compute the analogous killed Green function **inside the exact fixed-outdegree Pólya-point-tree**. The calculation above does that directly and recovers the same two local scaling signatures without assuming independent birth edges.

**Outcome B21:** succeeded. The finite-to-local transfer target is now sharper: a coupling must preserve not merely the Perron root but the exact boundary Green factor

`exp(L/2)B_L ~ B_* exp(L/2)/L`.

A coupling that preserves only the `L^-2` spectral gap but loses the `1/L` boundary amplitude is insufficient.

---

## 9. Uniform typical-age susceptibility calculation

The exact solution gives

`D_0-2 alpha C_g
 =[-2 alpha(c_Y+c_O exp(-L/2))
   -4 alpha^2 p C_g E_L]
  /(1+alpha pL)=O((1+L)^-1)`.

Hence

`D(u)=O((1+L)^-1)+2 alpha C_g exp(-u/2)`.

Therefore `int_u^L D(v)dv=O(1)` uniformly in `L,u`. Integrating the `A` equation backward from `A(L)=0` gives `A(u)=O(1)` uniformly; then `B=A-D=O(1)` and finally `phi_s(u)=O(1)`.

Thus

`F_s^L(u)=h_s(u)phi_s(u)<=C exp(u/2)`.

Age-uniform averaging contributes density `exp(-u)`, so the integrand is `O(exp(-u/2))` and the total expectation is uniformly finite.

This bounded-typical / divergent-oldest split is exactly the kind of non-uniformity a finite-graph proof must retain.

---

## 10. What remains to solve the source problem

The source remains **OPEN**. The exact local calculations now supply:

1. a `(log n)^(-2)` spectral crossing scale for the fixed-outdegree killed PPT;
2. an oldest-boundary `sqrt(n)/log n` total-progeny scale;
3. bounded age-uniform critical susceptibility.

The remaining obligation is a finite-graph exploration theorem strong enough to transfer these facts through the relevant component scale. Concretely, for one of the oldest `O(1)` vertices one needs a coupling/comparison valid to explored mass `Theta(sqrt(n)/log n)` such that:

- within-birth sequential dependence perturbs the killed-PPT Green mass by `o(sqrt(n)/log n)`;
- depletion and collisions do not erase a positive fraction of the boundary amplitude;
- second-moment/tail control converts expected path/progeny mass into distinct vertices in one true percolation component.

The exact quantity that must be preserved is now explicit:

`exp(L/2)B_L ~ B_* exp(L/2)/L`.

This is materially sharper than the earlier generic instruction “couple the finite graph to the killed PPT”.

---

## 11. Validation and closure honesty

No finite exhaustive statement is asserted, so no exact checker is warranted. The validation is the all-parameter derivation in the artifact: exact Doob transform, exact inhomogeneous two-state ODE, exact boundary conditions, exact positive Green formula, asymptotics, and uniform susceptibility bound.

This is a **self-check**, not one of the two independent audits required for closure. No source-level closure is claimed.

---

## 12. Model / scheduler capability honesty

The requested `GPT-6 / maximum` remains prompt text only. The exposed task interface offers title, prompt, schedule, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. This run actually identifies as **GPT-5.6 Sol**, with reasoning effort **UNVERIFIED**.

Changing that requires a platform/workspace runtime capability that exposes scheduled-execution model-family and reasoning-effort controls; a GitHub edit cannot enforce it.

The repository records earlier `You cannot modify this task` responses for P26/P01/P03 from one authorization context; P26 was later successfully updated from an authorized context. For any task that still returns that denial, the compliant workaround is the owning/authorized account or workspace interface, an authorized ownership/admin transfer, or platform support. Creating a duplicate task, bypassing the permission boundary, or reactivating a disabled task is not an authorized workaround. No scheduler modification was attempted here.

---

## 13. Ledger delta for the designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b13 -> b13 (NO MOVEMENT) | PARTIAL / SOURCE OPEN | methods B9,B14,B21 | auxiliary exact killed-PPT oldest-boundary progeny ~ K_s sqrt(n)/log n; age-uniform susceptibility uniformly bounded | artifact 13bcdd367a021b324f430b79f153f2674bae5d33`

No root shared ledger was edited; this delta is for the designated maintainer only.

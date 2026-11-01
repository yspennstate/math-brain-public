Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT on the frozen P0151 metric: `gamma_E>=b14` before and after. Methods actually tried: B7 / B11 / B30.**

# HARD7-04 bounded research iteration — off-harmonic Perron slab route

Status: **PARTIAL / SOURCE OPEN**. This run does not manufacture another scalar bridge correction. It changes route to the exact two-type age/orientation operator and derives a fixed-buffer Perron certificate for every target exponent `beta<1/2`. The frozen finite-graph exponent does not move because the actual finite-graph transfer remains unproved.

The full theorem-sized analytic artifact is

`artifacts/hard7_2026-09-18/HARD7-04/p0151_offharmonic_perron_slab_20260920T1430Z.md`

created at commit

`e77c8335f5f3bcde34b3f99b033e94288c49685f`

and read back successfully at that exact SHA before this report was written.

No finite exhaustive claim is made, so no checker was manufactured.

---

## 1. Continuity, repository state, ownership, and exclusions consumed

I resumed the canonical exclusive claim `operations/claims/P0151.md`, still owned by `HARD7-04`. I did not restart I0049, a solved degree-count statement, Kemeny/extremal-hitting-time work, the independently attached-edge growing-graph model, or any released predecessor target.

Before new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active intake trace `P0151|3|critical window, fixed-outdegree PA` in the `probability_1000_intake_*` material;
- `operations/claims/P0151.md`;
- the newest own checkpoint `2026-09-20T1330Z__p0151_failure_cap_layer.md` and its proof/check artifacts;
- the exact killed-PPT spectral artifact `p0151_log_age_killed_ppt_spectral_window_20260920T0330Z.md`;
- the exact killed-PPT Green artifact `p0151_killed_ppt_boundary_green_20260920T1232Z.md`;
- the neighboring P0157/R14 terminal-handoff state, which is released after Section-I exhaustion and does not collide with P0151;
- the current queue entry for I0049, which remains a separate uniformly-grown-graph problem and is not the active target;
- a fresh path-scoped HARD7-04 commit read immediately before persistence, which still showed `8b5e5a1dca1f023f2d729bd68aa2b6fff4e28244` as the newest prior own report commit.

The current posting registry contains no source-equivalent P0151 paper. No root shared ledger or peer-track file was edited.

---

## 2. Frozen source statement and fresh current-literature check

The retained source model is the exact sequential fixed-outdegree affine preferential-attachment graph:

- fixed integer `m>=2` and fixed `delta>0`;
- exactly `m` out-edges per arriving vertex;
- edges attached sequentially to older vertices with probability proportional to current degree plus `delta`, including within-birth updates;
- no self-loop for the arriving vertex;
- independent bond percolation with retention probability `pi` after graph generation.

The exact threshold is

`pi_c
 =delta/[2( m(m+delta)
             +sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The source target remains the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components in this exact fixed-outdegree sequential model.

A fresh bounded search on **20 September 2026** rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact threshold and giant/no-giant transition for the fixed-outdegree affine model, not a finite-size critical-window theorem.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025: `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale for a class in which new vertices connect **independently** to earlier vertices. That hypothesis does not automatically contain the exact fixed-`m` sequential model here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026: a different inhomogeneous preferential-attachment-kernel ensemble with `tau in (2,3)` and a moving threshold.

No source-matching fixed-outdegree critical-window resolution surfaced in the bounded refresh. This is negative search evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric: before and after

The fixed source-relevant metric is

`gamma_E
 :=liminf_{n->infinity}
   log E|C_max(n,pi_c)|/log n`.

The immediately preceding run proved

`gamma_E>=b14`,

where `b14>b13` is the exact one-unit cap-layer coefficient recorded in the 13:30Z report and proof artifact.

This run establishes a new local-operator theorem and a quantified transfer target, but it does **not** complete the finite-graph comparison needed to turn that theorem into a new exponent.

Therefore:

**Before:** `gamma_E>=b14`.

**After:** `gamma_E>=b14`.

**NO MOVEMENT.** The unchanged-run count on P0151 is now `1`; Section I is not triggered because the preceding run moved the metric strictly.

---

## 4. Idea before bookkeeping: stop optimizing scalar caps and tilt the Perron exponent

The latest checkpoint explicitly recommended a fixed-width Perron-weighted age/type route. I therefore did not add another bridge ticket or degree cap.

The counterexample-oriented question was:

> At the exact critical threshold, if one asks only for a polynomial exponent `beta<1/2` rather than the full window, does the two-type Pólya-point-tree operator still sit at criticality, or is there a positive margin that a finite-graph comparison could spend?

The answer is favorable and exact. The critical operator is neutral only at the harmonic exponent `1/2`. At every fixed exponent below `1/2` it has a strictly positive Perron margin of quadratic size in `1/2-beta`.

That observation materially changes the transfer problem: an exponent-only proof need not first reproduce the full `(log n)^(-2)` window precision.

---

## 5. B7 — take the off-harmonic limit

Put

`a:=m+delta`, `A:=2m+delta`,
`chi:=a/A`, `alpha:=chi-1/2=delta/(2A)`,

and use the exact PPT constants

`c:=ma/A`,
`d:=m(a+1)/A`,
`e:=(m-1)a/A`,
`g:=sqrt(de)`,
`lambda0:=c+g`.

Fix

`beta in (m/A,1/2)`

and write

`epsilon:=1/2-beta in (0,alpha)`.

For the power vector `x^-beta`, the extended two-type mean operator reduces exactly to

`B_beta
 =[[c/(alpha+epsilon), d/(alpha-epsilon)],
   [e/(alpha+epsilon), c/(alpha-epsilon)]]`.

If

`Lambda_beta:=pi_c r(B_beta)`,

then the artifact proves the closed form

`Lambda_beta
 = alpha/[lambda0(alpha^2-epsilon^2)]
   [c alpha
    +sqrt(g^2 alpha^2+(c^2-g^2)epsilon^2)]`.

Since

`c^2-g^2=m(m+delta)(delta+1)/(2m+delta)^2>0`,

one gets

`Lambda_beta>1`

for every fixed `beta<1/2` in the admissible power range.

Even more precisely,

`Lambda_(1/2-epsilon)
 =1+(sigma^2/2)epsilon^2+O(epsilon^4)`,

with

`sigma^2=lambda0/(alpha^2 g)`.

**B7 outcome:** succeeded. The negation route — that criticality stays neutral when the exponent is tilted below `1/2` — is false. There is an exact positive margin.

---

## 6. B11 — dualize the previous Fourier/spectral calculation

The earlier killed-PPT artifact had the real Fourier dispersion

`lambda_+(xi)
 =1-(sigma^2/2)xi^2+O(xi^4)`.

The new power tilt is the hyperbolic side of the same calculation:

`xi -> i epsilon`

gives the sign-reversed quadratic curvature

`1+(sigma^2/2)epsilon^2+O(epsilon^4)`.

The artifact proves this directly from a positive `2x2` matrix, so no formal analytic continuation is being assumed.

There is also an exact algebraic explanation for why the current scalar connected shadow stalls below `1/2`. Its tangent exponent is

`b2=m/A+pi_c c`.

Criticality gives

`pi_c(c+g)=alpha=1/2-m/A`,

hence

`1/2-b2=pi_c g`.                                                  (6.1)

Thus the entire tangent-shadow gap is exactly the geometric-mean off-diagonal Perron contribution. The natural two-type target matrix is

`G_target
 =(m/A)I+pi_c[[c,d],[e,c]]`,

whose Perron eigenvalue is exactly `1/2`.

This is **not** yet claimed as an actual finite-graph drift matrix. It identifies the missing directional structure that a valid two-type connected shadow must realize.

**B11 outcome:** succeeded. The old scalar gap and the killed-window spectral constant are now unified by one exact two-type Perron calculation.

---

## 7. B30 — localize in age and quantify both the usable margin and the failure of a crude coupling

Let `T_L` be the PPT mean operator killed to log ages `0<=u<=L`. For the positive Perron power vector `h_beta`, the artifact proves that finite-interval boundary loss is exponentially small away from the endpoints.

Define

`H_beta
 :=1/(alpha-epsilon)
   log[2Lambda_beta/(Lambda_beta-1)]`.

Then for every `L>=2H_beta` and every

`H_beta<=u<=L-H_beta`,

one has the componentwise slab inequality

`pi_c T_L h_beta
 >=[(Lambda_beta+1)/2]h_beta`.                                  (7.1)

For fixed `beta<1/2`, `H_beta` is a fixed constant independent of `n`. As `beta upward1/2`,

`H_beta=(2/alpha)log(1/(1/2-beta))+O(1)`.

The exact relative finite-graph comparison loss that can be spent while retaining strict gain is

`zeta_beta
 =(Lambda_beta-1)/(2(Lambda_beta+1))`.

Indeed, if a future finite connected exploration can establish

`K_n h_beta >=(1-zeta_beta)pi_cT_Lh_beta`,

then automatically

`K_n h_beta
 >=[1+(Lambda_beta-1)/4]h_beta`.

Near `1/2`,

`zeta_(1/2-epsilon)
 =(sigma^2/8)epsilon^2+O(epsilon^4)`.

So an exponent-only transfer for a fixed `beta` needs only fixed `Theta((1/2-beta)^2)` relative accuracy, not window-scale `o((log n)^-2)` accuracy.

I then stress-tested the simplest way of obtaining that comparison: impose one minimum birth time `s_n=n^q` and use only `E sum_v w_v(t)^2=O(t)` to control all collisions. This route has an exact strategy barrier.

For `R_n=O(n^beta)` relevant target exposures after time `s_n`, the crude repeated-target bound gives

`E[# collisions]=O(R_n^2/s_n)=O(n^(2beta-q))`,

so the method needs `q>2beta`. But the remaining killed-PPT interval has length `(1-q)log n`, whose exact oldest-boundary Green scale is only

`n^((1-q)/2)/log n`.

To support exponent `beta`, one needs `q<=1-2beta`. These conditions are compatible only for

`beta<1/4`.

Therefore a single hard age floor plus a uniform collision bound cannot approach the half exponent. The next transfer must use age-sensitive collision accounting or remain connected throughout rather than tree-couple the entire exploration.

A precise next quantity is the age-weighted collision energy

`E_coll:=sum_t R_t^2/t`,

not the worst-case replacement `R^2/s`.

**B30 outcome:** mixed. The fixed-buffer slab certificate succeeds, but the naive hard-floor finite coupling is rigorously rejected as an approach to `beta` near `1/2`.

---

## 8. Method-inventory honesty

P0151 had already used every numbered move B1--B30 before this run, so the instruction to select three labels never before used on this problem is now combinatorially impossible. I did not invent fresh labels.

This run uses the nonconsecutive triple **B7/B11/B30** in a materially new role:

- B7: off-harmonic Perron tilt rather than the admission-run scale comparison;
- B11: exact hyperbolic/Fourier duality rather than the previous parent-ticket budget;
- B30: a fixed-buffer slab certificate plus a proof-strategy collision barrier rather than the earlier repeated-birth proxy.

The triple differs from the immediately preceding `B16/B5/B18` and from every prior recorded P0151 triple located in the bounded repository search.

---

## 9. What was learned and the next finite-graph obligation

The source remains **OPEN**, but the finite-to-local obligation is now sharper.

It is not necessary to attack the exact critical window first in order to pursue the power exponent. For each fixed `beta<1/2`, the local operator supplies:

1. an explicit positive Perron margin `Lambda_beta-1`;
2. a fixed buffer `H_beta` independent of `n`;
3. an explicit admissible comparison loss `zeta_beta`;
4. the exact missing scalar-shadow term `pi_c g`;
5. a natural two-type target matrix with Perron exponent `1/2`;
6. a proof that minimum-age truncation plus a uniform collision estimate cannot reach the target range.

The next serious finite-graph route should therefore be:

- define an **orientation/type-resolved connected shadow** rather than a scalar one;
- organize it in fixed log-age slabs;
- realize the off-diagonal `d,e` mechanisms with thinning chosen to lose less than `zeta_beta`;
- bound duplicate/same-birth errors through the age-sensitive energy `sum_t R_t^2/t` rather than `R^2/s`;
- close a second moment at the deliberately sub-half target exponent `beta`;
- only after proving this for arbitrary fixed `beta<1/2` take the supremum `beta upward1/2`.

That is a genuinely different route from another scalar cap improvement.

---

## 10. Current runtime/model-control status

The requested `GPT-6 / maximum` remains prompt text only in the scheduler interface exposed to this run. The interface provides task prompt/title/schedule/timing/enabled controls but exposes **no model-family selector, no reasoning-effort selector, and no guaranteed-duration field**. This run actually identifies as **GPT-5.6 Sol**; reasoning telemetry is **UNVERIFIED**.

Changing that requires a platform/workspace scheduler capability that exposes model-family and reasoning-effort controls and authorizes this task to use them. A GitHub edit cannot create those scheduler fields.

The current compact repository ledger records that P26's full prompt update later succeeded in one authorized context; its earlier `You cannot modify this task` response was therefore authorization-context-specific rather than a mathematical or GitHub issue. For any task that still returns that denial, the compliant workaround is the owning/authorized account or workspace context, an authorized ownership/admin transfer, or platform support. Creating a duplicate task, bypassing permissions, or reactivating a disabled task is not an authorized workaround.

No scheduler modification was attempted in this run.

---

## 11. Validation and closure honesty

The new theorem is written in full in the analytic artifact. I algebraically rederived the Perron root, checked the strict sign `c^2-g^2>0`, checked the quadratic coefficient against the earlier `sigma^2`, and read the committed artifact back at its exact SHA.

There is no finite exhaustive claim, so no exact-arithmetic checker was warranted. This is a **self-check**, not either of the two independent outside audits required for closure.

No source-level closure is claimed. Status remains **PARTIAL / SOURCE OPEN**.

---

## 12. Ledger delta for the designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b14 -> b14 (NO MOVEMENT) | PARTIAL / SOURCE OPEN | methods B7,B11,B30 | auxiliary exact off-harmonic Perron margin Lambda_beta>1 for every beta in (m/A,1/2), fixed buffer H_beta, tolerance zeta_beta, hard-floor coupling barrier beta<1/4 | artifact e77c8335f5f3bcde34b3f99b033e94288c49685f`

No root shared ledger was edited; this delta is for the designated maintainer only.
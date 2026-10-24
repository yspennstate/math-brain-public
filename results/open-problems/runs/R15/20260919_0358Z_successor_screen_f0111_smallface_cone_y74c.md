Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the source’s four-obligation counterexample metric is not presently scoreable and the historical `2/4` remains a retirement carry rather than a live-candidate score. `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the repaired `theta=4/5` quadratic contact is now proved to dominate the cardinality-two hazard on the **entire arbitrary small-coordinate face**, not merely on two-coordinate faces and the homogeneous ray; the proof yields a dimension-free positive-quadratic cone theorem. Moves actually used: #3 PROVE SOMETHING STRONGER, #24 FIND THE EXTREMAL OBJECT, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — a universal quadratic cone for every small-coordinate face

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All newly derived Talagrand mathematics below is **SELF_CHECK_ONLY**. It does not reopen I0076, promote F0111 from `PENDING / NOT READY`, claim publication novelty, or satisfy the two-independent-auditor closure rule.

## 1. Continuity, source fidelity, admission, and exclusions

I continued from the newest complete own report

`runs/R15/20260919_0246Z_successor_screen_f0111_face_ray_repair_q73x.md`

rather than restarting. Before doing new mathematics I refreshed the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

the newest visible same-source neighboring R07 / I0077 report, and the newest strict admission evidence. The latter still supplies no source-current, ownership-clear free CLOSABLE successor for R15; the strict admission quantity remains

`E_READY_CLOSABLE: 0 -> 0`.

No new claim was created and no shared root was edited.

### Burdzy–Scheutzow Problem 7.2 remains exact and retired-handed-off

I rechecked the primary PDF, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

- FBM means that there are random origins tending to `-infinity` from each of which the complete centered future is standard Brownian motion.
- BBM means the time-reversed process is FBM.
- 2BM means that at one random time the complete centered forward and backward half-paths are **independent standard Brownian motions**.
- Problem 7.2 assumes only FBM + BBM and independence of the two complete centered half-paths at an arbitrary random time `T`; it does **not** assume that `T` is a stopping time and does not separately assume Brownianity of either seam half.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had the desired independent seam but was proved actually 2BM. Thus there is no surviving frozen counterexample candidate and I do not manufacture a new `3/4` or `4/4` score. Problem 7.5 remains excluded.

A fresh bounded public search on 2026-09-19 recovered the original paper/citation trail but no accessible later primary source explicitly announcing a solution of exact Problem 7.2. This is bounded negative evidence only.

### Retained screen and current literature

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 / Problem 10.9. For an up-class `A`, `A in C_gamma` means that at every base `q>=0` there is a zero-constant multilinear polynomial with nonnegative coefficients which globally majorizes the hazard `-log(1-zeta_t(A))` and obeys the scaled budget at `gamma q`. Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold `{|X|>=k}`.

Fresh dated searches recovered the August 11, 2026 Ascoli–He–Park–Talagrand `k`-threshold reformulation, Chen Li's September fractional result, and Park's September 13 dimension-free comparison *toward* the discrete conjecture. None of the retrieved primary statements claims the exact Definition-10.1 / Problem-10.9 theorem screened here. This is not a novelty certificate; **novelty remains UNVERIFIED**.

## 2. Carried candidate from the preceding run

For the cardinality-two threshold write

`F_m(x)=sum_i x_i - log(1+sum_i(exp(x_i)-1))`.                (2.1)

The preceding run studied the two-level interior bases

`q^(epsilon)=(epsilon,...,epsilon,b,b)`, `b=log 2`,           (2.2)

with fourteen small coordinates, and repaired the earlier globally failing quadratic contact by spending a fraction

`theta=4/5`                                                   (2.3)

of the small-coordinate diagonal curvature on small-small pair coefficients.

If `alpha_s(epsilon)` is the common small singleton coefficient and `beta_ss(epsilon)` the common small-small pair coefficient, that construction gives the exact limits

`alpha_s(epsilon) -> alpha_* := 2/3-(4/9)log 2`,             (2.4)
`beta_ss(epsilon) -> beta_* := 13/45`.                        (2.5)

The preceding report proved that for all sufficiently small positive `epsilon` the full candidate has positive coefficients, exact value/gradient contact, a strictly positive local Hessian gate, every two-small-coordinate face globally valid, and the entire homogeneous fourteen-small-coordinate ray globally valid.

What remained open was the **arbitrary heterogeneous fourteen-small-coordinate face**. This run closes that whole face, and in fact proves a stronger dimension-free theorem.

## 3. Method #3 — prove a stronger positive-quadratic cone theorem

### Theorem R15-F0111-SMALLFACE-CONE

Let `m>=1`, `x_i>=0`,

`X=sum_i x_i`,
`Q=sum_{i<j} x_i x_j`,                                      (3.1)

and let `alpha,beta>=0`. If

`(1-alpha)^2 <= 4 alpha beta`,                               (3.2)

then

`F_m(x) <= alpha X + beta Q`                                 (3.3)

for every dimension `m` and every nonnegative vector `x`.

If `alpha>=1`, (3.3) is immediate from `F_m(x)<=X`, so the only interesting case is `0<alpha<1`.

### Proof

Set

`S=1+sum_i(exp(x_i)-1)`,
`M=max_i x_i`,
`B=X-M`,
`A=X-log(1+X)`.                                              (3.4)

Two elementary lower bounds on `S` give two independent upper bounds on the target hazard.

First, `exp(u)-1>=u` gives

`S>=1+X`, hence `F_m(x)<=A`.                                 (3.5)

Second, `S>=exp(M)` gives

`F_m(x)<=X-M=B`.                                             (3.6)

Therefore

`F_m(x)<=min(A,B)`.                                          (3.7)

Now count the quadratic mass a second way:

`2Q=X^2-sum_i x_i^2`.                                        (3.8)

Since `x_i^2<=M x_i`,

`sum_i x_i^2<=MX`,

and therefore

`Q >= X(X-M)/2 = XB/2`.                                     (3.9)

Put `c=beta/2`. The proposed polynomial is bounded below by

`alpha X+beta Q >= alpha X+cXB`.                             (3.10)

It remains to compare this with `min(A,B)`.

If `B>=A`, the right side of (3.10) is increasing in `B`, so it suffices to test `B=A`. If `B<=A`, then we need

`alpha X+cXB>=B`.                                            (3.11)

When `cX>=1`, (3.11) is automatic. When `cX<1`, its right-side deficit is increasing in `B`, so again the worst case is `B=A`. Thus in all cases it suffices to prove

`alpha X+cXA>=A`.                                            (3.12)

For `X=0` there is nothing to prove. For `X>0`, use

`log(1+X)>=2X/(2+X)`.                                        (3.13)

Indeed the difference between the two sides vanishes at zero and has derivative

`X^2 / ((1+X)(2+X)^2) >=0`.                                  (3.14)

Consequently

`A/X = 1-log(1+X)/X <= X/(X+2)`.                            (3.15)

If `cX>=1`, (3.12) is automatic. If `cX<1`, equations (3.12) and (3.15) reduce to the sufficient inequality

`alpha >= X(1-cX)/(X+2)`,                                   (3.16)

or equivalently

`cX^2-(1-alpha)X+2alpha >=0`.                                (3.17)

The discriminant of the quadratic in (3.17) is

`(1-alpha)^2-8alpha c=(1-alpha)^2-4alpha beta`,              (3.18)

which is nonpositive by (3.2). Hence (3.17), then (3.12), then (3.3) hold for every `X>=0`. QED.

### What changed conceptually

The preceding report attacked selected coordinate faces one at a time. Theorem (3.3) makes the dimension and the detailed heterogeneity disappear. Only three aggregate quantities are needed: total mass `X`, extremal coordinate `M`, and quadratic pair mass `Q`; the extremal inequality `Q>=X(X-M)/2` then closes the whole family at once.

## 4. Methods #24 and #25 — the extremal coordinate plus two honest counts

The proof above identifies the relevant extremal object: the largest active coordinate `M`. It simultaneously controls the target through `F<=X-M` and the polynomial through the exact identity

`2Q=X^2-sum x_i^2 >=X(X-M)`.                                 (4.1)

This is the new mechanism. It is not an SDP statement, a local Taylor test, or a sampled path/ray computation. It turns an arbitrary-dimensional face into a scalar quadratic whose discriminant is the complete sufficient condition (3.2).

The theorem also shows why the earlier two-coordinate lemma was too narrow. A coefficient pair satisfying (3.2) automatically controls **every number of active coordinates at once**.

## 5. Apply the cone theorem to the actual `theta=4/5` repaired contact

For a strict, continuity-stable application I do not use the irrational limiting coefficients directly. Freeze the rational pair

`alpha_0=179/500`,
`beta_0=36/125`.                                             (5.1)

The exact checker

`artifacts/R15/f0111_smallface_cone_y74c.py`

was executed before archival, and its output is

`artifacts/R15/f0111_smallface_cone_y74c.out`.

It certifies

`exp(25/36) > sum_{j=0}^5 (25/36)^j/j!`
`            =2905893449/1451188224 >2`,                    (5.2)

so

`log 2 <25/36`.                                               (5.3)

Therefore

`alpha_* =2/3-(4/9)log2`
`        >2/3-(4/9)(25/36)=29/81>179/500=alpha_0`.           (5.4)

Also

`beta_*=13/45 >36/125=beta_0`.                               (5.5)

Finally the cone discriminant is exactly

`(1-alpha_0)^2-4alpha_0 beta_0`
` = -63/250000 <0`.                                          (5.6)

By the coefficient limits (2.4)-(2.5), there exists `epsilon_0>0` such that for every

`0<epsilon<epsilon_0`,                                       (5.7)

we have

`alpha_s(epsilon)>=alpha_0`,
`beta_ss(epsilon)>=beta_0`.                                  (5.8)

Let arbitrary nonnegative values `x_1,...,x_14` be placed on the fourteen small coordinates and set both big coordinates to zero. The restriction of the repaired polynomial is

`P_small(x)=alpha_s(epsilon) X+beta_ss(epsilon) Q`.           (5.9)

By positivity, (5.8), and Theorem R15-F0111-SMALLFACE-CONE,

`P_small(x)`
` >= alpha_0 X+beta_0 Q`
` >= F_14(x)`                                                 (5.10)

for **every** `x in R_+^14`.

### Corollary R15-F0111-ALL-SMALL-FACES

For every sufficiently small positive `epsilon`, the actual interior `theta=4/5` repaired contact from the preceding run globally majorizes `F_{16,2}` on the entire coordinate face on which the two big coordinates vanish.

This strictly contains the preceding certifications of every two-small-coordinate face and the homogeneous fourteen-small ray.

The same argument is dimension-free: for every fixed number `m` of small coordinates, any member of the analogous two-big-coordinate repaired family whose small coefficients are sufficiently close to `(alpha_*,beta_*)` has its full arbitrary small-only face globally certified by the same rational cone point `(179/500,36/125)`.

## 6. A second exact reduction: block gluing

There is a clean way to state the remaining obstruction.

Partition a cardinality-two system into disjoint blocks `A,B`. Write

`X=sum_{i in A} x_i`,
`Y=sum_{j in B} y_j`,
`S_A=1+sum_{i in A}(exp(x_i)-1)`,
`S_B=1+sum_{j in B}(exp(y_j)-1)`,                             (6.1)

and

`g_A=log S_A`, `g_B=log S_B`,
`F_A=X-g_A`, `F_B=Y-g_B`.                                    (6.2)

The combined failure partition function is exactly

`S_{A union B}=S_A+S_B-1`.                                   (6.3)

Hence

`F_{A union B}`
` =F_A+F_B+Phi(g_A,g_B)`,                                    (6.4)

where

`Phi(u,v)=u+v-log(exp(u)+exp(v)-1)`.                          (6.5)

This is an identity, not an estimate.

For the repaired two-level candidate, let `A` be the fourteen-small block and `B` the two-big block. Its limiting cross coefficient is `2/9`, so the global gap decomposes schematically as

`P-F`
` =(P_A-F_A)+(P_B-F_B)+(2/9)XY-Phi(g_A,g_B).                 (6.6)

The new theorem settles the first term on the **entire** small block. The remaining issue is therefore no longer an arbitrary sixteen-variable face problem: it is a two-block coupling problem involving the exact scalar hazards `g_A,g_B`, the big-block slack, and the cross budget `(2/9)XY`.

I do not claim (6.6) is nonnegative yet. This is the precise next obstruction.

## 7. Why this is real progress but not source closure

The parent source asks for a universal `gamma>0` covering all cardinality thresholds and all bases. This run proves neither that full statement nor even full heterogeneous `k=2` at `gamma=1`.

What it does prove is stronger than the previous face checks: a universal analytic cone condition on positive quadratic coefficients, and its exact application to the **whole 14-dimensional heterogeneous small face** of the current interior repaired candidate.

The remaining candidate failures, if any, must involve at least one of the two big coordinates. Equivalently, after (6.4), they must defeat the scalar block-coupling correction rather than hide inside the small block.

Status therefore remains

`F0111: PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED`.

No audit count is advanced.

## 8. Prior-art / literature log

Fresh bounded queries on 2026-09-19 included:

1. exact Burdzy–Scheutzow title/arXiv id + `Problem 7.2` + two-sided Brownian;
2. exact Talagrand title + `Problem 10.9` + `C_gamma` + cardinality thresholds;
3. `Talagrand discrete convexity conjecture` + 2026 `k-threshold`;
4. arXiv:2608.11183 (Ascoli–He–Park–Talagrand);
5. arXiv:2609.08967 (Chen Li, fractional version);
6. arXiv:2609.14681 (Park, dimension-free comparison toward the conjecture).

The retrieved current papers establish important reformulations / fractional or approximate progress; none of the accessible statements located in this bounded pass claims the exact positive-multilinear Problem 10.9 theorem or the quadratic cone lemma above. Negative search evidence is not a novelty proof. The ingredients of Theorem (3.3)—`exp x>=1+x`, a max-coordinate bound, and a quadratic-discriminant argument—are elementary and must be treated as potentially folklore until a dedicated prior-art audit says otherwise.

## 9. Model / scheduler control status

This runtime actually identifies as GPT-5.6 Sol. The reasoning level is not authenticated by the exposed scheduler/runtime surface, so it is reported as `UNVERIFIED`; I do not claim GPT-6 maximum.

The exposed scheduler API still provides prompt/title, schedule or relative-start, timing mode, and enabled-state controls. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution field**. Therefore the requested GPT-6/maximum setting remains prompt text only in this environment.

The historical P26 scheduler ID that once returned `You cannot modify this task` was blocked in that authorization context. Repository continuity later records a successful P26 update from a different authorized P/C context. The lawful remedy for any such refusal is the owning/authorized context or an owner/admin product/API/backend surface that exposes the needed routing fields; task duplication or permission bypass is not a workaround. No scheduler or permission change was attempted in this run.

## 10. Next route

The preceding triple was `#16/#19/#22`; it was not repeated. The next mathematically distinct attack should work directly on (6.6): differentiate the mixed block gap in one big coordinate, determine whether its minimum occurs at a boundary or at the contact point, and use the exact endpoint `Phi` geometry rather than another local SDP. A natural next triple is `#5 ADD A PARAMETER AND DIFFERENTIATE`, `#15 BREAK THE SYMMETRY ON PURPOSE`, `#20 FIND WHY THE ALGORITHM FAILS`.

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "no live frozen candidate; historical retirement carry 2/4"
  native_after: "no live frozen candidate; historical retirement carry 2/4"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_movement: false
  native_unchanged_count: "not advanced after mandatory retirement"
  admission_metric_before: 0
  admission_metric_after: 0
  admission_metric_name: E_READY_CLOSABLE
  retained_screen: "Talagrand F0111 / Problem 10.9, PENDING / NOT READY"
  retained_movement: "proved universal small-face quadratic cone; applied it to certify the full arbitrary fourteen-small-coordinate face of the theta=4/5 repaired interior candidate"
  tried_moves: [3, 24, 25]
  previous_moves: [16, 19, 22]
  remaining_obligation: "control the mixed small/big block correction in equation (6.6); do not infer full k=2 or Problem 10.9 closure"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260919_0246Z_successor_screen_f0111_face_ray_repair_q73x.md"
    - "artifacts/R15/f0111_smallface_cone_y74c.py"
    - "artifacts/R15/f0111_smallface_cone_y74c.out"
  audit_ids: []
  closure_claimed: false
  publication_novelty: UNVERIFIED
```

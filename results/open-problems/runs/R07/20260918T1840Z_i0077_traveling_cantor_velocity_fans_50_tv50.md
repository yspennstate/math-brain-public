Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `49 -> 50` genuinely distinct nonparabolic shape families; Section-B moves actually used: #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

# R07 CLOSABLE OUTSIDE — traveling Cantor velocity fans for Burdzy–Scheutzow Problem 7.8

Status: **PARTIAL** on the source problem. The theorem-sized claims T65/T66 below are proved on this page. They have `0/2` required independent OTHER-track audits. Publication novelty is **UNVERIFIED**.

## 1. Continuity, admission, ownership, and source recovery

This run continues R07/I0077 from the newest immutable report

`runs/R07/20260918T172901Z_i0077_countable_bv_fractal_gates_49_cbv49.md`

at commit `f99a12071e4af8cdcef768983d8a83249ec2cb5c`. The entering frozen metric is therefore `49`, not the stale root-ledger R07 placeholder.

Before new research I reread/rechecked the current repository controls and source state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and the current deployment policy;
- `operations/claims/I0077.md`;
- the newest R07 report and the I0077 report/commit history needed to preserve the frozen equivalence convention;
- the latest R15 state: R15 has moved to a distinct successor and does not own I0077;
- C29's explicit I0077 exclusion/rotation-hold report, which confirms that C29 must not duplicate R07's source;
- targeted intake/repository searches for `I0077`, the exact Problem-7.8 wording, prior attempts, and ownership.

The canonical claim still literally says **`PENDING_ADMISSION, not READY`** and provisionally reserves I0077 to R07. `INDEX.md` settles Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` does not exclude 7.8. The old R07 KPZ/FPP route remains preserved in its immutable handoff and was neither deleted nor reopened.

The intake's trailing forward-Levy text is not part of 7.8.

### Primary source recovered

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / PTRF 160 (2014), 95–126.

Definition 2.1 says that an FBM `X` admits random times `S_j -> -infinity` a.s. such that for each **fixed deterministic index** `j`,

\[
B^{(j)}_s:=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion.

For the parabolic strip

\[
\{(t,x):t<0,\ c_1\sqrt{|t|}<x<c_2\sqrt{|t|}\},
\]

Theorem 4.3 has three clauses: the universal obstruction when `lambda_0(c_1,c_2)>=1`, decomposable asymptotic confinement when `lambda_0<=1`, and decomposable pointwise confinement when `c_1<=0<=c_2` and `lambda_0<1`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

Problem 7.9 is the separate forward-Levy problem.

## 2. Fresh current-literature pass

Dated 2026-09-18, I searched the exact Problem-7.8 wording, later/citing work on *Forward Brownian Motion*, Brownian motion with deterministic drift, Brownian image/inverse-image dimension, and moving fractal targets.

The bounded search again recovered the original Burdzy–Scheutzow source but no accessible later primary paper explicitly claiming to resolve exact Problem 7.8. This is **bounded negative evidence only**, not a novelty certificate.

The decisive classical input for this run is Robert Kaufman, *Brownian Motion and Dimension of Perfect Sets*, Canad. J. Math. 22 (1970), 674–680. For one-dimensional Brownian motion `B`, Kaufman's theorem (A) says that almost surely, **simultaneously for every closed** `F subset [0,1]`,

\[
\boxed{\dim_H B(F)\ge 2\dim_HF-1.}
\tag{2.1}
\]

Kaufman explicitly notes that `F` need not be known in advance and may depend on the Brownian path. This universal quantifier is essential below.

For deterministic linear drift `s -> vs`, the Cameron--Martin theorem gives equivalence in law of `B_s+vs` and `B_s` on each fixed compact interval. Peres--Sousi, *Brownian motion with variable drift: 0-1 laws, hitting probabilities and Hausdorff dimension* (2012), is nearby modern drift literature and explicitly recalls this Cameron--Martin principle. Their paper does not state the FBM theorem below.

No novelty beyond this bounded literature statement is claimed.

## 3. Counterexample-first screen: why an arbitrary continuum of velocities is impossible

Before proving anything I tested the most tempting stronger statement: replace a countable family of traveling target packets by an arbitrary uncountable family.

That extension is false in the strongest possible way. Take the point target `A={0}` and all real velocities. At every age `u>0`,

\[
\bigcup_{v\in\mathbb R}(vu+A)=\mathbb R.
\]

Thus an uncountable velocity family can make the gate condition completely vacuous. This does **not** refute Problem 7.8; it only identifies a genuine boundary of the proposed route.

The proof below will use countability twice: first to take a countable intersection of probability-one drifted-Kaufman events, and second through countable stability of Hausdorff dimension.

## 4. T65 — countable traveling-fractal gate theorem

**Theorem T65 (traveling-fractal velocity-fan obstruction).** Fix `T>0` and `d in (1/2,1]`. Let `Z subset (0,infinity)` be deterministic and closed. Assume that for some `U_0<infinity`,

\[
\boxed{
\dim_H\bigl(Z\cap[U-T,U]\bigr)\ge d
\qquad\text{for every }U\ge U_0.
}
\tag{4.1}
\]

Let

\[
(v_m,b_m,A_m)_{m\ge1}
\]

be a countable deterministic family with `v_m,b_m in R` and each `A_m subset R` nonempty compact. Put

\[
a_*:=\sup_{m\ge1}\dim_H A_m
\]

and assume the uniform strict dimension gap

\[
\boxed{a_*<2d-1.}
\tag{4.2}
\]

Let deterministic fibers `K(u) subset R` satisfy only

\[
\boxed{
K(u)\subset
\bigcup_{m=1}^{\infty}\bigl(v_m u+b_m+A_m\bigr)
\qquad(u\in Z),
}
\tag{4.3}
\]

with **no restriction whatsoever** on `K(u)` for `u notin Z`.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T65}
\]

### Proof

Assume the event in T65 has positive probability. By the countable union over integer tail radii, choose a deterministic integer `R>=U_0` such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be the FBM witness sequence. Since `S_j -> -infinity` almost surely, choose one **deterministic index** `j` so far left that

\[
\mathbb P\{S_j\le -(R+T)\}>1-p/2.
\]

Hence

\[
G:=E_R\cap\{S_j\le-(R+T)\}
\]

has positive probability.

For this fixed `j`, define on `[0,T]`

\[
B_s=X_{S_j+s}-X_{S_j}.
\]

By Definition 2.1 of FBM, `B` is **unconditionally** standard Brownian motion.

For every deterministic `m`, set

\[
Y^{(m)}_s=B_s+v_m s.
\]

The drift `v_m s` belongs to the Cameron--Martin space on `[0,T]`, so `Y^{(m)}` has a law equivalent to standard Brownian motion. Consequently Kaufman's pathwise event

\[
\dim_HY^{(m)}(F)\ge 2\dim_HF-1
\quad\text{for every closed }F\subset[0,T]
\tag{4.4}
\]

has probability one for each `m`. Because the family is countable, the intersection of (4.4) over all `m` still has probability one.

Fix an outcome in `G` lying in that simultaneous probability-one event and put

\[
U=-S_j\ge R+T.
\]

Reflect the deterministic temporal gate into the witness window:

\[
F:=\{s\in[0,T]:U-s\in Z\}.
\tag{4.5}
\]

Since `s -> U-s` is an isometry,

\[
\dim_HF
=
\dim_H\bigl(Z\cap[U-T,U]\bigr)
\ge d.
\tag{4.6}
\]

For each `m`, let

\[
F_m:=\left\{s\in F:
X_{S_j+s}\in v_m(U-s)+b_m+A_m
\right\}.
\tag{4.7}
\]

Each `F_m` is closed: `F` is closed, `A_m` is compact, and the relevant path is continuous. On the confinement event, every `s in F` corresponds to an age `u=U-s>=R` in `Z`, so (4.3) gives

\[
F=\bigcup_{m=1}^{\infty}F_m.
\tag{4.8}
\]

For `s in F_m`,

\[
X_{S_j}+B_s
\in
v_mU-v_ms+b_m+A_m,
\]

or equivalently

\[
Y^{(m)}_s=B_s+v_ms
\in
A_m+c_m,
\qquad
c_m:=v_mU+b_m-X_{S_j}.
\tag{4.9}
\]

Therefore

\[
Y^{(m)}(F_m)\subset A_m+c_m.
\]

Translations preserve Hausdorff dimension, so Kaufman's lower bound (4.4) yields

\[
2\dim_HF_m-1
\le
\dim_HY^{(m)}(F_m)
\le
\dim_HA_m
\le a_*.
\]

Hence every `m` satisfies

\[
\dim_HF_m\le\frac{1+a_*}{2}=:q.
\tag{4.10}
\]

By (4.2), `q<d`. Countable stability of Hausdorff dimension and (4.8) now give

\[
\dim_HF
=
\sup_m\dim_HF_m
\le q<d,
\]

contradicting (4.6). Thus the eventual-confinement event has probability zero. `QED`

### Dependence audit

The proof never conditions on `S_j` and never assumes that `S_j` is independent of its Brownian future. The witness **index** `j` is fixed deterministically before the probability-one events are invoked. The reflected set `F`, branch sets `F_m`, and translations `c_m` may all depend on the outcome. Kaufman's theorem is strong enough because its quantifier is simultaneous over every closed time set; countability of the deterministic velocity family lets us impose that universal event simultaneously for every `m`.

## 5. The three Section-B moves

### #11 DUALIZE — success

The direct geometric question is whether a Brownian witness can keep selecting points from a moving union of fractal packets. I dualized this to an **image-dimension obstruction**. On a branch-selection set `F_m`, confinement is equivalent to saying that the drifted Brownian image `Y^{(m)}(F_m)` lies inside a low-dimensional compact target. Kaufman's inequality then bounds the dimension of the admissible time set from above.

This is the core proof of T65.

### #15 BREAK THE SYMMETRY ON PURPOSE — success

Run 45's strict-dimension curtain used one stationary spatial fractal. I deliberately broke that symmetry by giving each packet its own nonzero ballistic velocity `v_m`. The witness sees Brownian motion plus a deterministic linear drift; Cameron--Martin equivalence preserves Kaufman's path property. Countably many different velocities can therefore coexist without restoring a stationary target.

This produces the velocity-fan family below rather than another stationary pinning parameter.

### #27 SWAP THE QUANTIFIERS — success

The random witness phase makes the reflected gate set `F` random. A theorem of the form “for each fixed F, almost surely ...” would be unsafe here. Kaufman's result has the stronger order

\[
\mathbb P\{\text{for every closed }F,\ \dim B(F)\ge2\dim F-1\}=1.
\]

That quantifier order is precisely what permits inserting the random `F` and random branch sets `F_m` after the path is fixed. This closes the random-phase loophole rather than conditioning it away.

## 6. T66 — canonical traveling Cantor velocity fan

Let `C_3` be the middle-thirds Cantor set and periodize it:

\[
E:=C_3+\mathbb Z.
\]

For every `U`, the sliding unit window satisfies

\[
\dim_H(E\cap[U-1,U])
=
\frac{\log2}{\log3}
=:d.
\tag{6.1}
\]

Indeed, after reducing modulo one, the window cuts `C_3` into two closed pieces whose union is `C_3`; finite stability of Hausdorff dimension forces the larger piece to retain dimension `d`.

Now let `A_{32}` be the self-similar Cantor set generated by

\[
x\mapsto x/32,
\qquad
x\mapsto 31/32+x/32.
\]

The open-set condition gives

\[
\dim_HA_{32}=\frac{\log2}{\log32}=\frac15.
\tag{6.2}
\]

The T65 threshold is strict because

\[
\frac15<2\frac{\log2}{\log3}-1
\iff
\frac{\log2}{\log3}>\frac35
\iff
2^5>3^3,
\]

and the exact integer gap is

\[
32-27=5>0.
\tag{6.3}
\]

At age `u>0` define the ballistic Cantor velocity fan

\[
L(u):=\bigcup_{m\in\mathbb Z}(mu+A_{32}).
\tag{6.4}
\]

Thus at every gate age there are countably many **uncountable Cantor packets**, traveling with all integer velocities. Put

\[
r(u):=u^3\operatorname{dist}(u,E)
\]

and define the fiber

\[
K_*(u):=\{x:\operatorname{dist}(x,L(u))\le r(u)\}.
\tag{6.5}
\]

Finally define the backward space-time shape

\[
\mathcal V_*:=
\{(-u,x):u>0,\ x\in K_*(u)\}
\cup(\{0\}\times\mathbb R).
\tag{6.6}
\]

At every gate age `u in E`, `r(u)=0`, so

\[
K_*(u)=L(u)=\bigcup_{m\in\mathbb Z}(mu+A_{32}).
\]

This is exactly T65 with countably many velocities `v_m=m`, offsets zero, and identical targets `A_m=A_{32}`.

Therefore every FBM satisfies

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal V_*
\quad\forall u\ge R
\right)=0.
}
\tag{T66}
\]

### The chambers really open to all of space

This is not a narrow tube hidden behind fractal notation. At the centers

\[
u_n=n+\tfrac12
\]

of the largest complementary gaps of the periodized middle-thirds Cantor set,

\[
\operatorname{dist}(u_n,E)=\frac16,
\qquad
r(u_n)=\frac{u_n^3}{6}.
\]

For `n>=1`, `u_n>=3/2` and hence `r(u_n)>=9/16`. The largest first-level complementary gap of `A_{32}` has length `30/32=15/16`, so radius `9/16>15/32` already fills every internal Cantor gap in each unit cell. Between adjacent velocity cells the remaining gap has length `u_n-1`. Moreover for every `u>=1`,

\[
2r-(u-1)
=
\frac{u^3}{3}-(u-1)
=\frac{u^3-3u+3}{3}
=\frac{(u-1)^2(u+2)+1}{3}>0.
\]

Thus for every `n>=1`,

\[
\boxed{K_*(n+1/2)=\mathbb R.}
\tag{6.7}
\]

The shape alternates between unbounded ballistic Cantor fans on a recurrent fractal set of ages and literal full-space chambers at infinitely many intervening ages.

## 7. Exact finite self-check

The finite arithmetic used in the canonical representative was checked exactly and archived:

- `artifacts/R07/20260918T1840Z_tv50_exact_check_final.py`
- `artifacts/R07/20260918T1840Z_tv50_exact_check_final.out`

The executed output is:

```text
PASS
threshold_integer_gap=5
u=3/2: r=9/16, internal_half_gap=15/32, margin=3/32
u=3/2: intercell_margin=5/8
identity: u^3-3u+3=(u-1)^2(u+2)+1
```

This is a **self-check**, not an independent audit. An earlier exploratory arithmetic artifact with the same `tv50` stem checked only the inter-cell subclaim; the `_final` pair above is the authoritative finite-core artifact used by this report.

## 8. Frozen-equivalence audit: why point 50 is genuinely new

The new representative is not counted merely because a parameter changed.

- **Versus run 45 (stationary fractal-dimension pinning curtains):** run 45's gate fiber is one fixed bounded spatial fractal. Here every gate fiber is an **unbounded countable union** of positive-dimensional Cantor packets whose centers separate ballistically like `mu`. Fixed Brownian rescaling/reflection/translation cannot convert bounded stationary fibers into an infinite-diameter velocity fan.
- **Versus run 48 (critical-gauge affine pinholes):** run 48 has one moving singleton at each gate age and needs Perkins's critical logarithmic gauge. Here every velocity branch has Hausdorff dimension `1/5`, there are countably many velocities, and the proof uses Kaufman's strict image-dimension inequality.
- **Versus run 49 (countable finite-variation tracks):** run 49's gate fiber is countable and has spatial Hausdorff dimension zero. The present gate fiber is uncountable in every velocity packet and has Hausdorff dimension `1/5`; the proof is not a finite-variation restriction argument.
- **Versus the earlier moving Cantor laminations:** those use a compact Cantor fiber/selector mechanism. Here the gate fiber has infinite diameter and countably many ballistic packets, while the off-gate chambers become all of `R` infinitely often.

The invariants “bounded versus unbounded gate fiber,” “spatial gate-fiber Hausdorff dimension zero versus positive,” and “one stationary packet versus countably many distinct ballistic velocities” survive the frozen equivalences. Thus this is a new structural family, not a rescaling or a different numerical parameter inside an existing family.

Hence the fixed metric moves

\[
\boxed{49\longrightarrow50.}
\]

`unchanged_count` resets to `0`.

## 9. Prior-art/novelty status

The mechanism deliberately uses classical theorems rather than presenting them as new:

- Kaufman 1970 supplies the uniform one-dimensional Brownian image-dimension lower bound;
- Cameron--Martin equivalence for linear drift is classical; Peres--Sousi 2012 is nearby modern drift literature;
- countable stability of Hausdorff dimension is standard.

The source-specific synthesis is the FBM fixed-witness argument combined with a countable velocity decomposition of moving fractal gate fibers. I found no accessible later paper in the bounded search explicitly stating T65/T66 or resolving Burdzy–Scheutzow Problem 7.8 in full. That does **not** establish publication novelty. Publication novelty remains **UNVERIFIED** pending a broader expert-level prior-art review.

## 10. What failed / next frontier

The strongest natural overextension already failed: an arbitrary uncountable velocity set can make the gate fiber all of `R`, so no theorem can depend only on a uniform dimension bound for the individual packets.

The next genuinely new frontier is therefore an **uncountable but dimension-controlled velocity parameter set** `V`, where one would need an incidence/slicing theorem that quantitatively trades parameter dimension `dim_H V` against the temporal gate dimension and spatial packet dimension. A plausible target is a bound of schematic form

\[
\dim_HF
\le
\dim_HV
+
\sup_v\frac{1+\dim_HA_v}{2},
\]

under enough regularity/transversality to make it true. I have **not** proved this inequality and do not record it as a claim. It is the exact missing ingredient exposed by the counterexample-first screen.

A second frontier is the equality case `a_*=2d-1`, where dimension alone becomes silent and exact gauges/capacities would be needed.

## 11. Closure state

T65/T66 are complete theorem-sized arguments on this page. The concrete finite arithmetic has an executed exact self-check. The prior-art search is recorded. However the required independent audits are absent:

- P26 audit: `0/1` for T65/T66;
- second distinct OTHER-track audit: `0/1`.

Therefore the source status remains **PARTIAL**, not PROVED/closed. Problem 7.8 is open-ended and this report adds one further source-appropriate family; it does not claim to exhaust all other space-time shapes.

## 12. Model/scheduler control status

The model-control limitation is unchanged. The task-edit surface available here exposes prompt/title and ordinary timing/enabled controls, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-model receipt**. Consequently `GPT-6 / maximum` remains prompt text only, and this report truthfully identifies the actual model as GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository also records that P26's historical `You cannot modify this task` failure was authorization-context-specific: a later update succeeded from another authorized context. For any task that still refuses modification, the legitimate workaround is the owning/authorized account or workspace, an authorized ownership/admin correction, or platform support — not a duplicate task and not a permission bypass.

No scheduler change was attempted in this run.

## 13. Structured ledger_delta

```yaml
track: R07
allocation: CLOSABLE_OUTSIDE
source: Burdzy-Scheutzow Forward Brownian Motion Problem 7.8
intake: I0077
claim_status: PENDING_ADMISSION_NOT_READY
owner: R07
metric_name: number_of_genuinely_distinct_nonparabolic_shape_families_with_complete_source_appropriate_theorem
metric_before: 49
metric_after: 50
movement: true
unchanged_count_after: 0
new_claims:
  - I0077-R07-T65 traveling-fractal velocity-fan obstruction
  - I0077-R07-T66 canonical traveling Cantor velocity fan
status: PARTIAL
independent_audits_for_T65_T66: 0/2
finite_core:
  checker: artifacts/R07/20260918T1840Z_tv50_exact_check_final.py
  output: artifacts/R07/20260918T1840Z_tv50_exact_check_final.out
  self_check_only: true
section_B_moves:
  - 11
  - 15
  - 27
next_frontier: uncountable dimension-controlled velocity parameter family / incidence-slicing threshold
publication_novelty: UNVERIFIED
shared_roots_modified: false
peer_files_modified: false
email_drive_public_posting: none
scheduler_changes: none
```

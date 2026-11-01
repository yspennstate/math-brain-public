Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `47 -> 48` genuinely distinct nonparabolic shape families; Section-B moves actually used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #18 SAY IT IN ANOTHER LANGUAGE, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R07 — critical-gauge affine pinholes for Burdzy–Scheutzow Problem 7.8

Status: **PARTIAL** on the source problem. The theorem-sized claims below are proved on this page, but the new claims have `0/2` required independent OTHER-track audits. Publication novelty is **UNVERIFIED**.

## 1. Admission/read-in and continuation point

This run continued the current R07 I0077 state rather than restarting it.

Read/rechecked before research:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md` and `RESULTS.md`;
- `QUEUE.md`;
- `operations/claims/I0077.md`;
- current owner/new-method directive;
- the latest own report, `runs/R07/20260918T1525Z_i0077_sparse_block_portal_archipelagos_47_sb47.md`;
- code-search across the I0077 history to test collision with earlier R07 families, including the fat-Cantor fan, Cantor-parity shutter, critical-web and fractal-pinning routes;
- the current R15 directory/ownership history. R15 has long since rotated away from Burdzy–Scheutzow Problem 7.2 and does not own 7.8.

The canonical claim still says `PENDING_ADMISSION, not READY` and reserves I0077 provisionally to R07. The stale compact root ledger row naming the old R07 FPP assignment is historical configuration state, not a reset of the supported I0077 metric. The latest supported own value entering this run is `47`.

The old R07 KPZ/FPP route remains preserved in its immutable handoff; nothing was deleted or overwritten.

### Primary source recovery

I re-read the primary Burdzy–Scheutzow PDF (arXiv:1302.6958 / PTRF 2014), including page images.

Definition 2.1 says that an FBM admits random times `S_j -> -infinity` a.s. such that, **for every fixed deterministic index `j`**, the process

\[
B^{(j)}_s:=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion.

The full Theorem 4.3 is the three-clause parabolic `lambda_0(c_1,c_2)` theorem:

1. `lambda_0(c_1,c_2)>=1` gives the universal limsup/liminf escape obstruction;
2. `lambda_0(c_1,c_2)<=1` gives a decomposable FBM with the corresponding asymptotic bounds;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there is a decomposable FBM pointwise confined between the two parabolas for all negative times.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Levy sentence is Problem 7.9 and is not part of I0077.

## 2. Why the run-45 strict-dimension frontier suggests a different invariant

Run 45 proved the sliding Hausdorff-dimension pinning obstruction

\[
d>\frac{1+a}{2},
\]

where `d` is temporal pin-set dimension and `a` is the dimension of a fixed spatial target. For a point target (`a=0`) the strict threshold is `d>1/2`. At the exact equality `d=1/2`, Kaufman's dimension inequality gives no contradiction.

That equality is not an accident: one-dimensional Brownian level sets themselves live exactly at Hausdorff dimension `1/2`. So the new route is to stop asking for another dimension inequality and use the **exact Hausdorff gauge of Brownian level sets**.

This is the key research move of the run.

## 3. The classical exact-gauge input

For sufficiently small `r`, put

\[
\psi(r)=\sqrt{r\log\log(1/r)}.
\tag{3.1}
\]

Extend `psi` monotonically and continuously away from zero; the extension is irrelevant to Hausdorff measure.

Perkins, *The exact Hausdorff measure of the level sets of Brownian motion*, Z. Wahrscheinlichkeitstheorie verw. Gebiete **58** (1981), 373--388, DOI `10.1007/BF00542642`, proves the exact Brownian level-set gauge (up to the harmless normalization constant in `psi`) in terms of local time. In particular there is a Brownian probability-one event on which, **simultaneously for every real level `x`**, the level set on a compact time interval has finite `psi`-Hausdorff measure:

\[
\boxed{
\mathcal H^\psi\{s\in[0,1]:B_s=x\}<\infty
\quad\text{for every }x\in\mathbb R.
}
\tag{3.2}
\]

The simultaneous quantifier is essential below because the level produced by an FBM witness is random.

If `v in R` is deterministic, Cameron--Martin equivalence on `C[0,1]` shows that the law of `B_s+vs` is equivalent to Wiener measure. Therefore the path property (3.2) transfers verbatim:

\[
\boxed{
\mathcal H^\psi\{s\in[0,1]:B_s+vs=x\}<\infty
\quad\text{for every }x\in\mathbb R,
}
\tag{3.3}
\]

almost surely.

No exact value of the finite measure is needed; only finiteness, uniformly over levels.

## 4. I0077-R07-T61 — critical-gauge moving-pinhole obstruction

**Theorem T61.** Let `Z subset (0,infinity)` be deterministic and closed. Assume that for some `U_0<infinity`, every far unit age window has infinite critical Brownian gauge measure:

\[
\boxed{
\mathcal H^\psi\bigl(Z\cap[U-1,U]\bigr)=\infty
\qquad\forall U\ge U_0.
}
\tag{4.1}
\]

Fix constants `v!=0` and `b in R`. Let `K(u) subset R` be deterministic fibers satisfying

\[
\boxed{K(u)=\{vu+b\}\qquad(u\in Z),}
\tag{4.2}
\]

with **no restriction whatsoever** on `K(u)` for `u notin Z`.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T61}
\]

### Proof

Assume the eventual-confinement event has positive probability. By a countable union over integer tail radii, choose deterministic `R>=U_0` such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be an FBM witness sequence. Since `S_j->-infinity` a.s., choose one **deterministic index** `j` sufficiently far left that

\[
\mathbb P(S_j\le-R-1)>1-p/2.
\tag{4.3}
\]

Thus

\[
G:=E_R\cap\{S_j\le-R-1\}
\]

has probability at least `p/2>0`.

For this fixed index define

\[
B^{(j)}_s=X_{S_j+s}-X_{S_j},\qquad0\le s\le1.
\tag{4.4}
\]

By Definition 2.1, `B^(j)` is unconditionally standard Brownian motion. Hence by (3.3), with probability one, **all** level sets of `B^(j)_s+vs` have finite `psi`-Hausdorff measure.

Now fix an outcome in `G` lying in that probability-one event and put

\[
U=-S_j\ge R+1.
\]

Define the reflected pin-time set in the witness window

\[
F_U:=\{s\in[0,1]:U-s\in Z\}.
\tag{4.5}
\]

The map `s -> U-s` is an isometry from `F_U` onto `Z cap [U-1,U]`. Hence (4.1) gives

\[
\boxed{\mathcal H^\psi(F_U)=\infty.}
\tag{4.6}
\]

For `s in F_U`, the age `u=U-s` belongs to `Z` and is at least `R`, so confinement and (4.2) imply

\[
X_{S_j+s}=v(U-s)+b.
\tag{4.7}
\]

Subtracting `X_{S_j}` and adding `vs`,

\[
B^{(j)}_s+vs
=vU+b-X_{S_j},
\qquad s\in F_U.
\tag{4.8}
\]

Thus `F_U` is contained in the single level set

\[
\left\{s\in[0,1]:
B^{(j)}_s+vs=vU+b-X_{S_j}
\right\}.
\tag{4.9}
\]

The level on the right is random and may depend on the witness, but (3.3) is simultaneous over **every** real level. Therefore the set in (4.9) has finite `psi`-Hausdorff measure, contradicting (4.6).

Hence `p=0`, proving T61. `QED`

### Dependence audit

The proof never conditions on `S_j` and never assumes independence between `S_j` and the Brownian future. The index `j` is fixed deterministically before invoking the Brownian path property. Randomness of the resulting level is harmless because Perkins' conclusion is uniform in the level.

## 5. Section-B move #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The strict run-45 threshold left the exact number `1/2`. Rather than perturbing the old dimension proof, I searched where `1/2` is itself an exact Brownian geometric scale. The answer is the level set: dimension `1/2`, but with a nontrivial logarithmic correction in its exact Hausdorff gauge.

**Outcome: success.** The equality case is separated by `psi`-measure even though dimension cannot separate it.

## 6. Section-B move #18 — SAY IT IN ANOTHER LANGUAGE

A moving pin condition

\[
X_{-u}=vu+b\quad(u\in Z)
\]

looks like a space-time confinement problem. On a fixed FBM witness, however, it becomes

\[
B_s+vs=\text{one constant}
\quad(s\in F_U).
\]

So the whole question becomes:

> can an infinite-`H^psi` deterministic reflected pin set fit inside one level set of a drifted Brownian path?

Perkins says no.

**Outcome: success.** This translation removes both the parabolic geometry and the random witness level from the difficult part of the proof.

## 7. Section-B move #21 — ASK WHO ELSE HAS THIS SHAPE

The nearby literature is not FBM confinement literature but exact random-fractal measure theory. The decisive classical source is Perkins (1981). Related exact-level-set work includes Taylor--Wendel on stable-process zero sets and later Gaussian/fractional-Brownian extensions. Those works supply the gauge technology, not an FBM answer.

**Outcome: success.** The exact-gauge theorem supplies a critical statement that the run-45 dimension route structurally cannot see.

### Two routes that were tested and rejected during this move

1. **Dimension-only equality.** Replacing `>` by `>=` in run 45 does not create a proof: Brownian level sets themselves have dimension `1/2`, so dimension gives equality, not contradiction.
2. **General nonlinear moving pin track.** If the pin track is an arbitrary locally Cameron--Martin function `f(u)`, the witness-window drift is `s -> f(U-s)-f(U)` and depends on the random phase `U=-S_j`. Pointwise Cameron--Martin equivalence for each deterministic `U` is not by itself a uniform theorem over a path-dependent continuum of `U`. I therefore do **not** claim that extension. The affine track is exactly the nontrivial class for which the witness-window drift `vs` is independent of `U`.

This is why T61 is stated for affine moving pinholes rather than hiding a random-phase gap.

## 8. Canonical metric family: quarter-Cantor affine pinhole curtain

Let

\[
C_4
=
\left\{
\sum_{k=1}^{\infty}3\varepsilon_k4^{-k}:
\varepsilon_k\in\{0,1\}
\right\}\subset[0,1]
\tag{8.1}
\]

be the two-map quarter Cantor set, and periodize it:

\[
E=C_4+\mathbb Z.
\tag{8.2}
\]

It is closed, Lebesgue-null, and

\[
\dim_H C_4=\frac12,
\qquad
0<\mathcal H^{1/2}(C_4)<\infty.
\tag{8.3}
\]

The second statement can be obtained directly from the natural Bernoulli mass distribution (lower bound) and the `2^n` level-`n` intervals of length `4^{-n}` (upper bound); no numerical computation is involved.

Because

\[
\frac{\psi(r)}{r^{1/2}}
=\sqrt{\log\log(1/r)}\longrightarrow\infty,
\tag{8.4}
\]

(8.3) implies

\[
\boxed{\mathcal H^\psi(C_4)=\infty.}
\tag{8.5}
\]

For any real `U`, the unit window `[U-1,U]` cuts at most two neighboring translates of `C_4`; after translation the two pieces partition `C_4` at the phase of `U`. If both pieces had finite `H^psi`, their union would have finite `H^psi`, contradicting (8.5). Hence

\[
\boxed{
\mathcal H^\psi(E\cap[U-1,U])=\infty
\quad\text{for every }U.
}
\tag{8.6}
\]

Now define the aperture

\[
r(u)=u^2\operatorname{dist}(u,E)
\tag{8.7}
\]

and fibers

\[
K_*(u)=[u-r(u),\,u+r(u)].
\tag{8.8}
\]

The associated backward shape is

\[
\boxed{
\mathcal P_*
=
\{(-u,x):u>0,\ x\in K_*(u)\}\cup\{(0,0)\}.
}
\tag{8.9}
\]

At every `u in E`, `r(u)=0`, so the entire fiber collapses to the **moving singleton**

\[
K_*(u)=\{u\}.
\tag{8.10}
\]

Thus T61 applies with `v=1,b=0`, giving the source-appropriate theorem

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal P_*
\quad\forall u\ge R
\right)=0
}
\tag{T62}
\]

for every FBM.

### The shape is genuinely wide between pinholes

The largest complementary gap of `C_4` is `(1/4,3/4)`. At

\[
u_n=n+\frac12,
\]

we have `dist(u_n,E)=1/4`, hence

\[
r(u_n)=\frac{u_n^2}{4}
\]

and the admissible fiber has diameter

\[
\boxed{2r(u_n)=\frac{u_n^2}{2}.}
\tag{8.11}
\]

So between critical fractal pinning epochs the corridor opens **quadratically**, far wider than the source's `sqrt(u)` parabolic scale. The obstruction is not a thin-tube estimate.

The shape is closed after adjoining `(0,0)`: `u -> u^2 dist(u,E)` is continuous; because `0 in E`, as `u downarrow0` both the center `u` and aperture tend to zero.

A deterministic continuous selector exists trivially, namely `h(u)=u`. Therefore T62 is not a topological no-selector result.

## 9. Why this earns metric point 48 rather than recounting run 45

This run does **not** count the same fractal-pinning family merely with the parameter changed to equality.

The structural differences are invariant under the frozen equivalence convention:

- **Run 45:** the pin fibers are contained in one fixed bounded spatial fractal `A`; the obstruction is strict Hausdorff-dimension expansion `2d-1>a`.
- **This run:** each pin fiber is a singleton whose location moves along the unbounded affine track `x=u`; the temporal set is exactly critical, `dim_H E=1/2`, so run 45's strict theorem is silent.
- A constant Brownian scaling/reflection/translation sends a nonzero affine slope to another nonzero affine slope; it cannot turn the unbounded moving pin track into a fixed bounded target.
- Run 44 uses **positive temporal Lebesgue measure** and occupation-density absolute continuity. Here `E` has Lebesgue measure zero.
- Run 30's Cantor-parity shutters have a deterministic continuity obstruction. Here `h(u)=u` is a continuous selector, so topology alone permits confinement.
- Run 39's global `dim_H<3/2` theorem is silent: `P_*` has ordinary two-dimensional interior on every complementary time gap with positive aperture.
- Runs 46--47 use discrete/arithmetic gate blocks and Gaussian persistence. Here every unit age window contains uncountably many critical pin times.

The counted family is therefore **critical-gauge affine moving-pinhole curtains**, counted once. Changing slope `v`, intercept `b`, or the particular self-similar representative does not earn another point.

## 10. Prior-art search

Fresh bounded searches in this run included:

- exact-title / arXiv-ID searches for later work mentioning Burdzy--Scheutzow Problem 7.8;
- `Forward Brownian Motion Problem 7.8 Hausdorff level set`;
- `Forward Brownian Motion Burdzy Scheutzow space-time shapes level sets`;
- `Brownian exact Hausdorff measure level sets Perkins 1981`;
- related exact-level-set / Gaussian-fractal references.

The primary paper remains the only located source explicitly posing exact Problem 7.8. I found no accessible later paper in this bounded search explicitly stating T61/T62 or resolving Problem 7.8 by critical Hausdorff-gauge pinning. This is **bounded negative evidence only, not a novelty certificate**.

The core exact-gauge mechanism is classical and is explicitly attributed to Perkins. Cameron--Martin equivalence is also classical. Any eventual publication claim would need a fuller MathSciNet/zbMATH/Crossref/citation-chain search and independent expert review.

## 11. Audit / checker status

There is no finite arithmetic core in T61/T62. I therefore did **not** manufacture an exact checker merely to create a certificate. The analytic proof is fully written on this page.

Independent OTHER-track audits for the new claims: `0/2`.

Therefore:

- T61: **PROVED on this page, unaudited externally**;
- T62: **PROVED on this page, unaudited externally**;
- source Problem 7.8: **PARTIAL**, not `PROVED` or `CLOSED`;
- publication novelty: **UNVERIFIED**.

## 12. Next research frontier

The affine restriction exposes the next genuinely difficult problem cleanly.

For a nonlinear pin track `f`, a witness at random age `U` produces the family of drifts

\[
h_U(s)=f(U-s)-f(U).
\]

A theorem uniform over this continuum of random phases would extend T61 beyond affine tracks. The natural next question is whether one can prove a **uniform exact level-set gauge theorem** for Brownian motion plus a compact family of Cameron--Martin drifts, or else construct a nonlinear track showing that such uniformity fails.

That is materially different from adding another Cantor parameter.

## 13. Scheduler/model-control fact

The exposed scheduler control surface still provides prompt/title, schedule/start-offset, enabled state and timing mode, but no binding model-family selector, reasoning-effort selector, guaranteed hour-long runtime field, or authenticated applied-model receipt. Thus `GPT-6 / maximum` remains prompt-only in this environment. This report therefore states the actual visible model honestly as GPT-5.6 Sol and leaves reasoning as UNVERIFIED.

The historical P26 `You cannot modify this task` error was authorization-context-specific; current repository state records that P26 was later updated successfully from an authorized context. For a task that still rejects modification, the legitimate remedies are the owning/authorized account or workspace, an authorized ownership/admin correction, or platform support. There is no worker-side permission bypass. No scheduler modification was attempted in this run.

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shapes"
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, frozen equivalence convention"
  before: 47
  after: 48
  movement: true
  new_family: "critical-gauge affine moving-pinhole curtains"
  new_claims:
    - "T61 critical-gauge moving-pinhole obstruction"
    - "T62 quarter-Cantor affine pinhole curtain"
  status: PARTIAL
  source_closed: false
  independent_other_track_audits: "0/2"
  finite_core: false
  checker: "not applicable; no finite computational core"
  publication_novelty: UNVERIFIED
  methods: [17, 18, 21]
  stagnation_count: 0
  next_obligation: "uniform critical-gauge level-set control for a nontrivial compact family of nonlinear Cameron--Martin witness drifts"
```

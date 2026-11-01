Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric `D_MI: 2 -> 2`. Methods tried: B4 / B14 / B25.**

# HARD7-01 — STUCK1 recovery completed: the full three-dimensional cube window

**Status:** PARTIAL / source OPEN. This execution carries out the single Section-I recovery selected in the preceding STUCK1 report: prove the simplest unproved source-shaped special case completely. The recovery succeeds for the full three-dimensional cube intermediate window, but it does **not** prove the source theorem for every centrally symmetric body in dimension three, so the frozen source metric does not move.

## 1. Continuity, required reads, ownership, and capability honesty

I resumed from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T19-12-00Z__stuck1_cube_overlap_route.md`

and the exclusive claim

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md`.

At run start I reread the controlling HARD7 policy, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest own checkpoint, the canonical claim, and current target/alias searches. Repository searches also recovered neighboring admission/ownership reports (`R20`, `NM13-*`, `R7-*`) that continue to identify the maximal-intersection uniqueness question as exclusively owned by HARD7-01. No conflicting owner or alias release was found. The current intake/reserve state was reopened; no absence from a queue or intake rendering was treated as permission to restart or duplicate a target.

Pre-artifact `master` was observed at `a9d253ccb4c23e4c233268ee50dfdd5b41661d69`. I make no shared-root ledger edit in this run.

**Scheduler/model capability:** the actual run self-identifies as GPT-5.6 Sol; the reasoning level is not exposed, so it is `UNVERIFIED`. The exposed scheduler schema available to these workers still does not provide a model selector or reasoning-effort selector; GPT-6/maximum remains prompt text only. Changing the actual runtime model/effort would require an authorized product/scheduler surface that exposes those controls, or platform support; a GitHub edit cannot do it. The repository contains both historical `You cannot modify this task` denials for P26/P01/P03 in one native context and a later `RESULTS.md` reconciliation saying P26 was successfully updated in a different exposed context. I did **not** probe or modify P26 here, because this worker is explicitly prohibited from modifying other schedules. The safe workaround remains to use the authorized native context/account/workspace that owns the task or platform support, never to create a duplicate job to bypass permissions.

## 2. Source statement and frozen metric

Primary source: Shiri Artstein-Avidan and David Katzin, *Isotropic Measures and Maximizing Ellipsoids: Between John and Loewner*, Proc. Amer. Math. Soc. 146 (2018), Section 4, arXiv:1612.01128.

For a centrally symmetric convex body `K subset R^n` and a prescribed ellipsoid volume corresponding to an intermediate radius

`r_J < r < r_L`, 

the source asks whether the ellipsoid maximizing

`Vol_n(K cap E)`

among ellipsoids `E` of that prescribed volume is unique.

The frozen metric remains

`D_MI = largest d such that uniqueness is proved for every centrally symmetric K and every intermediate prescribed radius in every n<=d.`

Bochi proves the source statement in dimension two.

**Before:** `D_MI=2`.  
**After:** `D_MI=2`.  
**Movement:** none.  
**Current unchanged source-metric streak on this admitted target:** `4`.

This execution is the **first STUCK1 recovery**, and it succeeds on the selected special case. It does not reset the source metric.

## 3. Fresh current-literature delta, 2026-09-19

A fresh bounded web check used the canonical aliases `maximal intersection ellipsoid`, `maximum intersection position`, `strong B equality`, and the exact Artstein-Avidan--Katzin title.

- Artstein-Avidan--Katzin, arXiv:1612.01128: https://arxiv.org/abs/1612.01128 . The paper defines maximal-intersection position and is the primary source.
- Jairo Bochi, arXiv:1702.03808: https://arxiv.org/abs/1702.03808 . The abstract explicitly says general uniqueness is open and proves the positive answer in dimension `2`.
- Dario Cordero-Erausquin and Liran Rotem, arXiv:2111.05110: https://arxiv.org/abs/2111.05110 . Their rotationally invariant strong `(B)` theorem supplies the global log-concavity used below, including the uniform-ball measure.
- Orli Herscovici, Galyna V. Livshyts, Liran Rotem and Alexander Volberg, arXiv:2305.17794: https://arxiv.org/abs/2305.17794 . This is the correct authorship of *Stability and the equality case in the B-theorem*; it treats Gaussian strong-`(B)` equality/stability, not the uniform-ball maximal-intersection source theorem.
- Eli Putterman, arXiv:2608.08472, submitted 2026-08-09 and updated 2026-08-11: https://arxiv.org/abs/2608.08472 . The abstract states sharp dimension-free Gaussian/`1`-log-concave stability and strong/functional extensions, but does not state the present uniform-ball maximal-intersection uniqueness theorem.

No checked current source in this bounded search states the full `n=3` Artstein-Avidan--Katzin theorem or the cube theorem below. This is bounded negative evidence, **not** a worldwide novelty certificate.

## 4. Result of the selected Section-I recovery

### Theorem (full three-dimensional cube intermediate window)

Let

`K_a=[-a,a]^3`, `a>0`,

and let the prescribed ellipsoid volume be `kappa_3 r^3` with

`a < r < sqrt(3) a`.

Among all origin-centered ellipsoids of that prescribed volume, the Euclidean ball `r B_2^3` is the **unique** maximizer of

`Vol_3(K_a cap E)`.

Equivalently, after scaling `r=1` and setting `s=a/r`, for every

`1/sqrt(3) < s < 1`

and every nonzero symmetric trace-zero `3 x 3` matrix `A`,

`F_A(t)=Vol_3([-s,s]^3 cap e^{tA}B_2^3)`

satisfies

`F_A'(0)=0`, `F_A''(0)<0`,

and therefore, by the strong `(B)` theorem,

`F_A(t)<F_A(0)` for every `t != 0`.

The previously proved disjoint-cap argument covers `s>1/sqrt(2)`. The new work below closes the entire remaining overlap layer

`1/sqrt(3) < s <= 1/sqrt(2)`.

This is a theorem for one symmetric body family. It is **not** the full source theorem in `n=3` and does not move `D_MI`.

## 5. B4 — prove the weaker special case completely: rigorous switching-interface second variation

Fix

`1/sqrt(3) < s <= 1/sqrt(2)`

and put

`K_s=[-s,s]^3`.

For `omega in S^2`, define

`m(omega)=max_i |omega_i|`,

`rho_K(omega)=s/m(omega)`,

`rho_t(omega)=(omega^T e^{-2tA}omega)^(-1/2)`.

Radial integration gives

`F_A(t)=(1/3) int_{S^2} min{rho_K(omega)^3,rho_t(omega)^3} d sigma(omega)`.

At `t=0`, `rho_0=1`. Set

`Omega_s={omega in S^2: m(omega)<s}`,

`delta(omega)=rho_K(omega)^3-1`,

`q_t(omega)=rho_t(omega)^3-1`.

Then `delta>0` on `Omega_s`, `delta<0` outside its closure, and

`min{rho_K^3,rho_t^3}=1+min{delta,q_t}`.

### Lemma (piecewise-smooth switching formula)

Let `delta` be as above. Its zero set is a finite union of smooth circular arcs; the only nonsmooth points are the finitely many arc endpoints where two coordinates have absolute value `s`. On every smooth arc,

`|grad_{S^2} delta| = 3 sqrt(1-s^2)/s >0`.

If

`q_t=t u + (t^2/2)v + o(t^2)`

uniformly with the same expansion for the first spatial derivatives on each smooth cell, then

`d/dt|_0 int min{delta,q_t} d sigma = int_{Omega_s} u d sigma`,

and

`d^2/dt^2|_0 int min{delta,q_t} d sigma
 = int_{Omega_s} v d sigma
   - int_{partial Omega_s} u^2/|grad_{S^2}delta| dH^1`.      (1)

#### Proof of the lemma

Away from `partial Omega_s`, the active branch of the minimum is fixed for all sufficiently small `t`, so ordinary dominated differentiation applies. Near a smooth boundary arc, use local coordinates `(y,z)` with `y=delta`; the coarea formula writes surface area as

`w(y,z) dy dz`, `w(0,z)=1/|grad delta|`.

The switch can occur only for `|y|=O(|t|)`. Freezing `u`, `v` and `w` at `y=0` changes the integral by `o(t^2)`. For fixed `z`, the one-dimensional identity for `min{y,t u + t^2 v/2}` gives the first-order contribution from `y>0` and the exact second-order interface correction `-u^2 w(0,z)`. Integrating in `z` yields (1).

At a corner where two smooth arcs meet, the relevant `O(|t|)` neighborhood has surface area `O(t^2)` while the perturbation of the integrand is `O(|t|)`, hence its contribution is `O(t^3)`. Thus the finitely many arc endpoints contribute no second-order term. This proves (1).

### Apply the lemma

Write

`a(omega)=omega^T A omega`,

`b(omega)=omega^T A^2 omega`.

Since

`omega^T e^{-2tA}omega = 1-2t a + 2t^2 b + O(t^3)`,

the exact Taylor coefficients of `rho_t^3` are

`u=3a`,

`v=15a^2-6b`.      (2)

On a smooth face arc, say `|omega_1|=s`,

`rho_K^3=s^3/|omega_1|^3`,

and the spherical gradient magnitude at the boundary is

`|grad_{S^2}delta|=(3/s)sqrt(1-s^2)`.      (3)

Combining (1)--(3) and the factor `1/3` from radial volume gives the exact second-variation formula

`F_A''(0)
 = (1/3) int_{Omega_s}(15a^2-6b)d sigma
   - [s/sqrt(1-s^2)] int_{partial Omega_s}a^2 dH^1`.      (4)

The first variation is

`F_A'(0)=int_{Omega_s} a d sigma`.      (5)

Because `Omega_s` is invariant under all coordinate sign changes and permutations,

`int_{Omega_s} omega omega^T d sigma = (|Omega_s|/3) I`,

so `tr A=0` implies

`F_A'(0)=0`.      (6)

This removes the precise gap left in the preceding STUCK1 report: the nonsmooth radial switching formula is now proved, and the arc endpoints produce no hidden second-order term.

## 6. B14 — use the hyperoctahedral group to reduce the Hessian to diagonal and shear modes

Set

`Area=|Omega_s|`,

`p=int_{Omega_s} omega_1^4 d sigma`,

`q=int_{Omega_s} omega_1^2 omega_2^2 d sigma`,

`D=sum_i A_ii^2`,

`O=sum_{i != j} A_ij^2`.

Since `(omega_1^2+omega_2^2+omega_3^2)^2=1`, symmetry gives

`Area=3p+6q`.      (7)

Also

`int_{Omega_s} a^2 d sigma = (p-q)D + 2q O`,

while

`int_{Omega_s} b d sigma = (Area/3)(D+O)`.

Therefore the interior part of (4) is exactly

`I(A):=(1/3)int_{Omega_s}(15a^2-6b)d sigma
      =(p-3q)(3D-2O)`.      (8)

On `Omega_s`, `|omega_1|<s`, hence strictly

`p < s^2 int_{Omega_s}omega_1^2 d sigma
   = (s^2/3)Area`.

Because `s^2<=1/2`,

`5p < (5/6)Area < Area`.

Using (7),

`p-3q=(5p-Area)/2 <0`.      (9)

Thus every nonzero trace-zero **diagonal** mode already has negative interior Hessian, before the nonpositive boundary term in (4) is used.

The sign-change symmetry kills every cross term between diagonal and off-diagonal modes and every cross term between distinct shears. Permutation symmetry makes the three shear coefficients equal. Hence it remains only to prove strict negativity for the representative shear

`A_12=A_21=1`, all other entries zero.      (10)

This is the full quadratic-form reduction; no finite sampling over matrices is used.

## 7. B25 — count the overlap region and the switching boundary in two ways

For the shear (10), define

`r0=sqrt(1-s^2)`,

`h=sqrt(1-2s^2)`,

`alpha=arccos(s/r0)`,

`M=2pi-8alpha`.

Here `M` is the total allowed angular measure on any one face circle. Since

`1/sqrt(3)<s<=1/sqrt(2)`,

we have `0<=alpha<pi/4` and `M>0`.

### 7.1 Boundary count

On the face `x=+/-s`, parameterize

`y=r0 cos(phi)`, `z=r0 sin(phi)`.

The allowed angles satisfy `|y|,|z|<=s`, and the line element is `r0 dphi`. For the shear,

`a(omega)=2 omega_1 omega_2`.

The four faces with `x` or `y` fixed contribute

`8 s^2 r0^3 M`.

On the two `z`-faces, the contribution is

`2 r0^5 S2`,

where

`S2=int_allowed sin^2(2phi)dphi
   = M/2 + sin(4alpha)
   >= M/2`.      (11)

Thus

`J_shear:=int_{partial Omega_s}a^2 dH^1
 =8s^2 r0^3 M + 2r0^5 S2`.      (12)

### 7.2 Interior area count

For fixed first coordinate `x>=0`, the allowed angular width of the cross-section of `Omega_s` is

`M(x)=2pi-8 arccos[s/sqrt(1-x^2)]`,

for `h<=x<=s`. Therefore

`Area=2 int_h^s M(x) dx`.      (13)

We have `M(h)=0`, `M(s)=M`, and

`M'(x)=8sx / [(1-x^2)sqrt(r0^2-x^2)]`,

`M''(x)/M'(x)
 =1/x + 2x/(1-x^2) + x/(r0^2-x^2) >0`.      (14)

So `M(x)` is convex. A convex function lies below its endpoint chord, hence

`Area <= (s-h)M`.      (15)

Equations (12) and (11) give

`[s/r0] J_shear /2
 >= [4s^3 r0^2 + (1/2)s r0^4] M`.      (16)

It remains to compare the coefficient in (16) with `s-h`. Set

`c=s/r0`, `d=h/r0`.

Then `c^2 in (1/2,1]`, `0<=d<c`, and `r0^2=1/(1+c^2)`. The strict inequality

`4s^3 r0^2 + (1/2)s r0^4 > s-h`      (17)

is equivalent to

`c(4c^2+1/2) > (c-d)(1+c^2)^2`.

But `c-d<c`, and

`4c^2+1/2-(1+c^2)^2
 =2c^2-c^4-1/2
 >=1/4`      (18)

for `c^2 in [1/2,1]`. Thus (17) holds with strict slack. Combining (15)--(17),

`[s/r0]J_shear > 2 Area`.      (19)

For the shear, `D=0`, `O=2`, and (8)--(9) give

`I(A)=2(Area-5p)<2Area`.      (20)

Therefore (4), (19), and (20) imply

`F_A''(0)<0`      (21)

for the representative shear. By the symmetry decomposition, (21) holds for every nonzero off-diagonal mode as well. Together with the diagonal case, we have

`F_A''(0)<0`

for every nonzero symmetric trace-zero `A` throughout the full overlap layer.

This B25 route is the useful double count: the *same* terminal face width `M` bounds the interior area from above and the switching-boundary shear dissipation from below, so exact evaluation of the fourth moment `p` is unnecessary.

## 8. Global uniqueness from strong `(B)`

The Cordero-Erausquin--Rotem strong `(B)` theorem for rotationally invariant log-concave measures implies that

`t -> F_A(t)`

is log-concave for every symmetric `A`.

By (6), `(log F_A)'(0)=0`; hence `t=0` is a global maximum along the entire one-parameter determinant-one deformation. Since

`(log F_A)''(0)=F_A''(0)/F_A(0)<0`,

no nonzero `t` can have `F_A(t)=F_A(0)`: if equality held at another point, concavity together with the global maximum at zero would force `log F_A` to be constant on the segment joining them, contradicting the strictly negative second derivative at zero.

Every origin-centered ellipsoid with the same volume as `B_2^3` can be written as

`e^A B_2^3`

for a symmetric trace-zero `A` (take its positive-definite shape operator and matrix logarithm). Thus the unit ball is the unique prescribed-volume centered MI ellipsoid for `K_s`.

Scaling back from `r=1` gives uniqueness for the cube whenever

`a<r<sqrt(3)a`.

The old disjoint-cap theorem handled `a<r<sqrt(2)a`; the present switching argument handles `sqrt(2)a<=r<sqrt(3)a`. Together they cover the entire strict John--Loewner interval for the three-dimensional cube.

## 9. Exact self-check artifact

After the analytic route was complete, I ran one exact symbolic self-check, limited to identities that are genuinely algebraic:

- the radial Taylor coefficients `3a` and `15a^2-6b`;
- the hyperoctahedral interior decomposition `(p-3q)(3D-2O)`;
- the face-arc identity `S2=M/2+sin(4alpha)`;
- the scalar slack decomposition behind (18);
- the shear boundary-energy bookkeeping.

Artifacts:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T20-10-00Z__cube_overlap_exact_check.py`

creation commit `1a44adcf8572498dffef750aa52256ebbd898b7c`;

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T20-10-00Z__cube_overlap_exact_check.out`

creation commit `d060d474fc7a71219aeb5d1e2e6100b37d23544d`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

Both artifact commits were read back successfully. This is a **self-check**, not an independent audit, and it does not certify the analytic switching lemma by itself.

## 10. What moved mathematically, and what did not

### New proved special-family statement

The exact centered maximal-intersection uniqueness theorem for the three-dimensional cube now covers the **entire** intermediate radius interval

`a<r<sqrt(3)a`.

The previous theorem covered only

`a<r<sqrt(2)a`.

So the cube-family radius coverage moves from the collar

`r/a in (1,sqrt(2))`

to the full source-relevant cube interval

`r/a in (1,sqrt(3))`.

This is genuine mathematical movement on the Section-I recovery, not source-level closure.

### Frozen source metric

`D_MI: 2 -> 2`.

No movement. The full `n=3` source theorem still asks for **every** centrally symmetric convex body, not merely the cube.

## 11. Remaining source obstruction after the successful recovery

The remaining statement is still

> If `B_2^3` is a global maximal-intersection ellipsoid of an arbitrary centrally symmetric convex body `K` at an intermediate prescribed volume, prove that every nonzero symmetric trace-zero deformation decreases the intersection somewhere strictly, equivalently that a second distinct determinant-one ellipsoid cannot attain the same global maximum.

The cube calculation reveals a useful general template:

`second variation = interior fourth-moment term - switching-boundary square energy`.

For the cube, group symmetry reduces the potentially positive interior direction to one shear coefficient and a geometric double count forces the boundary energy to dominate it. For a general `K`, stationarity gives the second-moment isotropy condition, but there is no checked source-wide inequality relating the fourth-moment interior term to the moving switching boundary with enough strictness.

That is the actual missing ingredient; another cube lemma would not move `D_MI`.

## 12. Section-I accounting and next run

The previous report was **STUCK1** and selected exactly one recovery: prove the simplest unproved special case. This run executes and completes that recovery. Because the frozen source metric nevertheless remains unchanged and the source-wide obstruction is unchanged, the next execution should be treated as the **STUCK2 thinking run**, not as an excuse to accumulate another special-family lemma.

That next run should contain the full five-part Section-I obstruction map and select exactly one second recovery. A different method triple is reserved for that thinking run:

**B1 / B11 / B27**.

- **B1:** change category from convex-body intersection geometry to a quadratic-form/measure inequality for the isotropic spherical region and its switching boundary;
- **B11:** dualize the missing strictness into an operator/Poincare or covariance-defect inequality for the uniform-ball restriction;
- **B27:** swap the quantifiers to ask for a source-wide equality classifier at global MI stationarity rather than direct strictness body-by-body.

A hard target may consume at most one further Section-I recovery after STUCK2; a third stuck episode requires handoff/rotation under the owner directive.

## 13. Honest label and closure status

**Source:** OPEN.  
**Research status:** PARTIAL.  
**Cube special case:** proved on the page for the full three-dimensional intermediate window; candidate novelty only, no worldwide novelty certification.  
**Finite/algebraic self-check:** PASS.  
**Independent audits:** none requested or claimed in this run.  
**Paper package:** not created, because the externally posed source is not closed.

```yaml
ledger_delta:
  track: HARD7-01
  source_target: MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS
  status: PARTIAL
  frozen_metric: D_MI
  before: 2
  after: 2
  movement: false
  unchanged_streak: 4
  section_I_state: STUCK1_RECOVERY_COMPLETED
  methods_this_run: [B4, B14, B25]
  new_special_case: "3D cube full intermediate window a<r<sqrt(3)a"
  previous_special_case: "3D/all-dim cube collar a<r<sqrt(2)a"
  artifact_check: PASS
  source_closed: false
  next_run: STUCK2_THINKING
  next_methods: [B1, B11, B27]
```

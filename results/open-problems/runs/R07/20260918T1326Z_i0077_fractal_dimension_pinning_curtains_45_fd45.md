Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `44 -> 45` genuinely distinct nonparabolic shape families; Section-B moves actually used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #18 SAY IT IN ANOTHER LANGUAGE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9 is the separate forward-Lévy question and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 45: zero-measure fractal pinning and Brownian image dimension

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and metric

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative R07 report is

`runs/R07/20260918T1225Z_i0077_fat_cantor_occupation_curtains_44_oc44.md`,

with the seam-only closure correction preserved separately at

`artifacts/R07/20260918T1225Z_oc44_seam_closure_correction.md`.

That run moved `43 -> 44` and used `#2,#1,#24`. The present triple `#17,#18,#30` is different. All thirty Section-B labels have already appeared somewhere in the long I0077 chain, as recorded in earlier immutable R07 reports; therefore the literal stock of labels “never tried on this problem” is exhausted and I do not invent an unused label. The mathematical route below is new.

Before new research I reread/recovered current state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest R07 report and targeted earlier R07 reports with possible equivalence collisions, especially runs 30, 39, 43, and 44;
- the newest visible neighboring R15 report. R15's distinct Burdzy--Scheutzow Problem 7.2 / I0076 remains a retired handoff and its current work is on a separate successor, so there is no ownership collision;
- targeted repository/intake searches for `I0077`, `1302.6958`, `Problem 7.8`, and related shape labels.

`INDEX.md` and `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no exact Problem-7.8 closure. The canonical claim still reserves I0077 provisionally to R07 and literally says `PENDING_ADMISSION, not READY`; I preserve that operational label rather than silently promoting it. The old R07 KPZ/FPP route remains preserved by immutable handoff and is not reopened or deleted.

The very large `probability_1000_intake_*/problems.jsonl` corpus cannot be rendered byte-for-byte through this connector without truncation. I therefore record the intake reread honestly as **targeted/partial due connector limits**: the exact I0077 source, ownership, exclusions, and searchable previous attempts were recovered; I do not claim a visual reread of hundreds of unrelated rows.

Entering metric: **44**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark recovered again

I reopened the primary paper and checked Definition 2.1, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM has random witness times `S_j -> -infinity` such that for each fixed deterministic witness index `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion.

Theorem 4.3 is the parabolic benchmark:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized escape obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the opposite normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the parabolic strip for every negative time.

Problem 7.8 is exactly the one-sentence question whether Theorem 4.3 can be generalized from parabolas to other space-time shapes. Problem 7.9 is separately the forward-Lévy problem.

The theorem below is a complete universal-obstruction theorem for a new family, not a classification of all shapes. Hence the source remains PARTIAL.

## 3. Fresh current-status / prior-art pass

Fresh bounded searches on 2026-09-18 included:

- exact `Forward Brownian Motion` / `Problem 7.8` / `other space-time shapes` queries;
- later/citing-paper searches around Burdzy--Scheutzow;
- Brownian image-dimension and inverse-image-dimension searches;
- `Brownian motion dimension perfect sets Kaufman` and related level-set threshold searches;
- temporal Cantor pinning and fractal hitting formulations.

I found no accessible later paper in this bounded pass explicitly resolving exact Problem 7.8 or stating the source-specific theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The main probabilistic input is classical and is emphatically **not claimed new**. Robert Kaufman, *Brownian Motion and Dimension of Perfect Sets*, Canadian J. Math. 22 (1970), 674–680, Theorem (A), proves for one-dimensional Brownian motion on `[0,1]` that, almost surely, **simultaneously for every closed set** `F subset [0,1]`,

\[
\boxed{\dim_H B(F)\ge -1+2\dim_H F.}
\tag{3.1}
\]

Kaufman's paper explicitly emphasizes that `F` need not be known in advance and may depend on the Brownian path. That uniform quantifier is exactly what is needed here because the FBM witness time is random. Brownian scaling transports (3.1) to every deterministic compact interval `[0,T]`.

## 4. #17 — look for your numbers somewhere else

Run 44 left the natural frontier: can a **zero-Lebesgue-measure** temporal pinning set still obstruct every FBM? Occupation density cannot answer that because it only sees positive clock-time mass.

The number `1/2` appears elsewhere as the natural Brownian level-set scale. Looking for the corresponding uniform theorem leads to Kaufman's lower image-dimension bound `2d-1`. That converts a temporal fractal of dimension `d` into a spatial Brownian image that must have dimension at least `2d-1`.

This immediately suggests comparing the temporal pinning dimension with the Hausdorff dimension `a` of the admissible spatial pin set. The natural strict obstruction becomes

\[
2d-1>a
\quad\Longleftrightarrow\quad
\boxed{d>\frac{1+a}{2}.}
\tag{4.1}
\]

**Outcome #17: successful.** It supplied a genuinely different threshold mechanism rather than another occupation-time lemma.

## 5. #18 — say it in another language

The original confinement statement is a path-in-space-time statement. Rephrase the pinning part as an image-set inclusion for one fixed Brownian witness:

\[
B^{(j)}(F)\subset A-X_{S_j}.
\tag{5.1}
\]

Now confinement is impossible whenever the left side is forced to have larger Hausdorff dimension than the right side. Crucially, Kaufman's theorem is simultaneous over all closed `F`, so the fact that `F` is generated from the random witness age does not require conditioning on that age.

**Outcome #18: successful.** The random-time dependence problem disappears into a pathwise uniform geometric theorem.

## 6. I0077-R07-T55 — uniform sliding Hausdorff-pinning obstruction

### Theorem T55

Let `Z subset (0,infinity)` be a deterministic **closed** set. Suppose there exist constants

\[
T>0,\qquad U_0<\infty,\qquad d\in[0,1]
\tag{6.1}
\]

such that every sufficiently far sliding age window has temporal Hausdorff dimension at least `d`:

\[
\boxed{
\dim_H\bigl(Z\cap[U-T,U]\bigr)\ge d
\qquad\forall U\ge U_0.
}
\tag{6.2}
\]

Let `A subset R` be a fixed Borel set with

\[
a:=\dim_H A<1,
\tag{6.3}
\]

and assume

\[
\boxed{d>\frac{1+a}{2}.}
\tag{6.4}
\]

For each `u>0`, let `K(u) subset R` be an arbitrary deterministic fiber satisfying only

\[
\boxed{K(u)\subset A\qquad(u\in Z).}
\tag{6.5}
\]

There is no restriction on `K(u)` for `u notin Z`; it may equal the whole real line.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T55}
\]

### Proof

Assume the displayed eventual-confinement event has positive probability. By a countable union over integer tail radii, choose a deterministic integer `R>=U_0` such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be an FBM witness sequence. Since `S_j->-infinity` almost surely, choose one **deterministic witness index** `j` far enough left that

\[
\mathbb P(S_j\le -R-T)>1-p/2.
\tag{6.6}
\]

Hence

\[
G:=E_R\cap\{S_j\le-R-T\}
\tag{6.7}
\]

has probability at least `p/2>0`.

Fix an outcome in `G` and put `U=-S_j`. Define the closed subset of the witness-time interval

\[
F_U:=\{s\in[0,T]:U-s\in Z\}.
\tag{6.8}
\]

Because `Z` is closed, `F_U` is closed. Reflection/translation preserve Hausdorff dimension, so (6.2) gives

\[
\dim_H F_U
=
\dim_H\bigl(Z\cap[U-T,U]\bigr)
\ge d.
\tag{6.9}
\]

For every `s in F_U`, the corresponding age `U-s` is at least `R` and belongs to `Z`. Therefore eventual confinement and (6.5) yield

\[
X_{S_j+s}\in A.
\tag{6.10}
\]

Subtracting `X_{S_j}`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j}
\in A-X_{S_j}
\qquad(s\in F_U),
\]

so

\[
B^{(j)}(F_U)\subset A-X_{S_j}.
\tag{6.11}
\]

Now `j` is deterministic, so Definition 2.1 says `B^{(j)}` is unconditionally standard Brownian motion. On Kaufman's probability-one event, after deterministic time scaling from `[0,T]` to `[0,1]`, inequality (3.1) holds **simultaneously for every closed subset of `[0,T]`**. In particular it applies to the possibly random/dependent set `F_U`. Thus

\[
\dim_H B^{(j)}(F_U)
\ge
2\dim_H F_U-1
\ge 2d-1.
\tag{6.12}
\]

On the other hand, translation preserves Hausdorff dimension and (6.11) implies

\[
\dim_H B^{(j)}(F_U)
\le
\dim_H(A-X_{S_j})
=a.
\tag{6.13}
\]

But (6.4) says `2d-1>a`, contradicting (6.12)--(6.13). The event `G` therefore cannot have positive probability, so (T55) follows. `QED`

### Dependence audit

The proof never conditions on the random witness time `S_j` and never assumes independence between `S_j` and the witness Brownian path. The only random closed set is `F_U`; Kaufman's theorem was chosen precisely because its almost-sure statement is uniform over **all** closed sets on the interval, including path-dependent ones.

## 7. Boundary / falsification audit

The theorem is intentionally strict. At equality

\[
2d-1=a
\tag{7.1}
\]

the dimension comparison alone gives no contradiction. Below equality it is also silent. This is a limitation of the route, not evidence that an FBM exists.

Likewise, zero Lebesgue measure of `Z` by itself is not enough for this proof. Run 44 already supplied the deterministic warning that a null perfect pinning set can admit nontrivial continuous selectors. The present theorem succeeds because it measures the **Hausdorff size** of each sliding pinning window, not because the set is merely uncountable or perfect.

## 8. #30 — one scale / one direction at a time: exact self-similar test family

Choose two exact self-similar Cantor sets.

### Temporal Cantor set

Let `C_3 subset [0,1]` be the middle-thirds Cantor set and periodize it:

\[
E=C_3+\mathbb Z.
\tag{8.1}
\]

It is closed and Lebesgue-null. Write

\[
d_t=\dim_H C_3=\frac{\log2}{\log3}.
\tag{8.2}
\]

For every real `U`, the unit interval `[U-1,U]` cuts two adjacent translates of `C_3`. After translation, the two pieces are `C_3 cap [theta,1]` and `C_3 cap [0,theta]` for the phase `theta`. Their union is all of `C_3`, and Hausdorff dimension of a finite union is the maximum of the component dimensions. Hence

\[
\boxed{
\dim_H(E\cap[U-1,U])=d_t
\quad\text{for every }U.
}
\tag{8.3}
\]

### Spatial Cantor set

Let `A_{16}` be the self-similar compact set generated by

\[
f_0(x)=\frac{x}{16},
\qquad
f_1(x)=\frac{15}{16}+\frac{x}{16}.
\tag{8.4}
\]

The open-set condition gives

\[
a=\dim_H A_{16}=\frac{\log2}{\log16}=\frac14.
\tag{8.5}
\]

The T55 threshold becomes

\[
\frac{\log2}{\log3}>\frac{1+1/4}{2}=\frac58.
\tag{8.6}
\]

This inequality has an exact integer certificate:

\[
8\log2>5\log3
\iff
2^8>3^5
\iff
\boxed{256>243.}
\tag{8.7}
\]

The exact checker was executed and archived at

- `artifacts/R07/20260918T1326Z_fractal_pinning_dimension_gap_checker.py`, creation commit `a1c45efea91fd1e709ef27d1c0e48aa9713f36ae`;
- `artifacts/R07/20260918T1326Z_fractal_pinning_dimension_gap_checker.out`, creation commit `033539803299f176498ca43a3df18e018f71426a`.

Its output is exactly

`PASS: 2^8=256 > 3^5=243; exact gap integer=13`.

**Outcome #30: successful.** The abstract threshold has a completely explicit exact self-similar instance.

## 9. I0077-R07-T56 — zero-measure Cantor pinning with ballistic chambers

Define

\[
r(u)=u\,\operatorname{dist}(u,E),
\qquad u>0,
\tag{9.1}
\]

and the spatial fiber

\[
K_*(u)=\{x\in\mathbb R:\operatorname{dist}(x,A_{16})\le r(u)\}.
\tag{9.2}
\]

Set

\[
\boxed{
\mathcal S_*
=
\{(-u,x):u>0,\ x\in K_*(u)\}
\cup
(\{0\}\times A_{16}).
}
\tag{9.3}
\]

### T56

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal S_*
\quad\forall u\ge R
\right)=0.
}
\tag{T56}
\]

### Proof

At every `u in E`, `dist(u,E)=0`, hence `r(u)=0` and

\[
K_*(u)=A_{16}.
\]

Equations (8.3), (8.5), and the exact strict inequality (8.7) verify every hypothesis of T55 with `T=1`, `Z=E`, `A=A_{16}`. T56 follows immediately. `QED`

### Closedness and chamber size

The map `(u,x) -> dist(x,A_{16})-u dist(u,E)` is continuous for `u>0`. Also `0 in E`, so as `u downarrow 0`,

\[
0\le r(u)=u\,dist(u,E)\le u^2\to0.
\]

Adding the seam `{0} x A_{16}` therefore makes (9.3) closed at time zero as well.

At the midpoint

\[
u_n=n+\frac12
\]

of the largest middle-third gap `(n+1/3,n+2/3)` in each period,

\[
\operatorname{dist}(u_n,E)=\frac16,
\qquad r(u_n)=\frac{u_n}{6}.
\tag{9.4}
\]

The largest gap of `A_{16}` has length `7/8`, so once `r(u_n)>=7/16` (equivalently `u_n>=21/8`) all its gaps are filled and

\[
K_*(u_n)=\left[-\frac{u_n}{6},1+\frac{u_n}{6}\right].
\tag{9.5}
\]

Thus along these epochs the admissible chamber has diameter

\[
\boxed{1+\frac{u_n}{3},}
\tag{9.6}
\]

which is ballistic in age and far wider than the parabolic `O(sqrt(u))` scale. The obstruction comes entirely from the fractal set of pinning ages.

A continuous selector certainly exists: because `0 in A_{16}`, the constant path `h(u)=0` belongs to every fiber. Therefore T56 is not a deterministic continuity impossibility in disguise.

## 10. Frozen-equivalence audit: why this earns metric point 45

This family is structurally distinct from the nearest earlier R07 classes.

- **Versus run 44 (positive-density occupation curtains):** the new pinning-time set `E` has **Lebesgue measure zero in every window**, so T53's occupation-time argument is completely silent. The new invariant is Hausdorff image dimension, not clock-time mass.
- **Versus run 30 (Cantor-parity shutters):** run 30 restricts an open dense collection of complementary gaps and has a purely deterministic continuity contradiction. Here restrictions occur only on a closed nowhere-dense null Cantor set; a continuous selector exists.
- **Versus run 39 (global shape dimension `<3/2`):** the new shape has two-dimensional interior in every nonpinning chamber, so its global Hausdorff dimension is 2. Run 39 cannot apply.
- **Versus run 43 (pinching Cantor critical lamination):** run 43 constrains the path to a moving Cantor fiber at all times. Here the fiber becomes an ordinary ballistic interval on large portions of each gap and is thin only at the fractal pinning ages.
- **Versus cage/ribbon families:** no subdiffusive or bounded-lag width condition holds; chamber diameter is linear in `u` along (9.6).

Brownian scaling, reflection, and constant translation preserve the distinction between zero temporal Lebesgue mass and positive temporal Lebesgue mass, preserve Hausdorff dimension, and cannot turn a shape with two-dimensional interior between fractal pinning times into the earlier zero-width web/skeleton classes. Therefore this is not a parameter variant of a prior family.

Exiting metric: **45**.  
Movement: **+1**.  
Unchanged streak: **0**.

## 11. Prior-art and novelty status

The Brownian image-dimension inequality is classical Kaufman 1970 and must be cited as such. The self-similar Cantor dimensions are classical. The finite arithmetic inequality is elementary.

What may be new is only the source-specific synthesis: using Kaufman's **uniform-over-all-closed-sets** theorem to handle the random FBM witness window and derive T55/T56 for deterministic space-time confinement. I found no accessible later paper in the bounded search that states this result or resolves exact Problem 7.8, but a negative search is not a novelty certificate.

**Publication novelty: UNVERIFIED.**

## 12. Closure status and next frontier

T55 and T56 are fully written on the page. The only finite core used in the canonical example, the strict dimension gap, has an exact checker and archived output. However the required independent OTHER-track audits have not yet occurred:

- P26 audit: **0/1**;
- second distinct OTHER-track audit: **0/1**.

Therefore the honest source status remains

\[
\boxed{\text{PARTIAL, not closed.}}
\]

No paper folder is created before the closure protocol is met.

The next genuinely new mathematical frontier is the **critical equality**

\[
\dim_H Z=\frac{1+\dim_H A}{2},
\]

where pure Hausdorff dimension no longer separates the Brownian image from the admissible spatial set. A source-appropriate improvement would need gauge Hausdorff measure, capacity, exact local dimension, or a sharper inverse-image theorem rather than another strict-dimension corollary.

## 13. Model / scheduler control issue

The requested `GPT-6 / maximum` setting remains **unenforceable from the exposed task-control surface available to this worker**. The current interface exposes title/prompt, schedule or start-offset, enabled state, and timing mode; it exposes no binding model-family selector, no reasoning-effort selector, no guaranteed one-hour execution control, and no authenticated applied-runtime model receipt. Thus `GPT-6 / maximum` remains prompt text, not verified runtime configuration.

The current repository ledger also records that the historical P26 response `You cannot modify this task` was authorization-context-specific: the same existing task was later successfully updated from a different authorized context. The legitimate workaround for a task that still refuses modification is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support. A permission bypass or duplicate task is not legitimate.

To make the requested model setting genuinely enforceable, the platform would need to expose a scheduler/task field that persists model family and reasoning effort (or an owning-workspace policy that pins them) and return authenticated runtime metadata showing what actually ran. This run did **not** attempt a scheduler mutation because the controlling owner instruction explicitly prohibits scheduler changes.

## 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric_name: "genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 44
  after: 45
  movement: +1
  unchanged_runs: 0
  source_status: PARTIAL
  canonical_claim_status: "PENDING_ADMISSION, not READY"
  methods: [17, 18, 30]
  new_claims:
    - I0077-R07-T55
    - I0077-R07-T56
  new_family: zero_measure_fractal_pinning_curtains
  canonical_example: "periodic middle-thirds temporal Cantor pinned to a ratio-1/16 spatial Cantor, with ballistic gap chambers"
  finite_core:
    statement: "log(2)/log(3) > 5/8"
    exact_equivalent: "2^8 > 3^5"
    checker: "artifacts/R07/20260918T1326Z_fractal_pinning_dimension_gap_checker.py"
    checker_creation_commit: a1c45efea91fd1e709ef27d1c0e48aa9713f36ae
    output: "artifacts/R07/20260918T1326Z_fractal_pinning_dimension_gap_checker.out"
    output_creation_commit: 033539803299f176498ca43a3df18e018f71426a
    result: "PASS: 256 > 243"
  external_prior_art:
    - "Kaufman 1970, Brownian Motion and Dimension of Perfect Sets, Theorem (A): uniform image-dimension lower bound"
  publication_novelty: UNVERIFIED
  outside_audits: "0/2"
  paper_package: false
  shared_roots_edited: false
  email_or_drive: false
  scheduler_changed: false
```

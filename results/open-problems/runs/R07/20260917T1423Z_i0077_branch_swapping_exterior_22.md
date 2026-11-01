Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 21 -> 22 genuinely distinct nonparabolic shape families; Section-B moves tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 22: crossed two-ended exterior fans

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and the fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative R07 report is

`runs/R07/20260917T1324Z_i0077_exterior_parabolic_fans_21.md`,

which moved the metric `20 -> 21` and used Section-B moves `#9,#14,#24`. All thirty Section-B moves had already appeared at least once before run 21, so this run is explicitly in the second cycle and uses the different triple `#6,#12,#27`; it does not pretend these numbers have never appeared in the I0077 history.

Before research I recovered/read current `master` evidence from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest R07 report and the searchable I0077 chain;
- the newest neighboring R06 report, including its independent scoped PASS on the preceding R07 claim `I0077-R07-T22`;
- the newest visible R15 report, which keeps distinct Burdzy--Scheutzow Problem 7.2 / I0076 retired/frozen and does not compete for I0077;
- the prior C29 duplicate-exclusion record, which explicitly left I0077 to R07.

`INDEX.md` and `RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 exclusion. The canonical claim remains owned by R07 and literally says `PENDING_ADMISSION, not READY`; this is a create-only reservation, not a statement of worldwide openness. The owner's repeated current assignment of exact I0077 to R07 is the operative worker instruction. The intake trailing text from Problem 7.9 is again excluded.

The large intake JSONL corpus cannot be rendered literally in one connector response without truncation; the exact I0077 record, source statement, ownership, exclusions, and all prior R07 attempts were recovered by targeted repository reads/searches. I do not claim a literal full-file byte reread of every JSONL line.

## 2. Primary-source benchmark recovered again

The source defines FBM by Brownian forward views from random origins tending to `-infinity`, and decomposable FBM by concatenating independent Brownian pieces at stopping times.

For `-infinity <= c_1 < c_2 <= infinity`, the source writes `lambda_0(c_1,c_2)` for the positive principal killed Ornstein--Uhlenbeck exponent associated with

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Remark 4.1 gives continuity and strict domain monotonicity. Remark 4.2 records the exact critical identities

\[
\boxed{
\lambda_0(-\infty,-1)
=\lambda_0(-1,1)
=\lambda_0(1,\infty)=1.
}
\tag{2.1}
\]

Theorem 4.3 states, in the source's full infinite-endpoint convention:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, there exists a decomposable FBM whose normalized far-past liminf/limsup lie inside the interval;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

The source proof also quotes Perkins' slow-point theorem in the pathwise form

\[
\mathbb P\bigl(\exists t\ge0,\Delta>0:
B(t+h)-B(t)\in[c_1\sqrt h,c_2\sqrt h]\ \forall h\in[0,\Delta]\bigr)
=
\begin{cases}
0,&\lambda_0(c_1,c_2)>1,\\
1,&\lambda_0(c_1,c_2)<1,
\end{cases}
\tag{2.2}
\]

and immediately invokes Brownian time-reversal to obtain the corresponding backward-cone statement. This is the dependence-safe local input below: it forbids existence of *any* Brownian cone point, so no independence between an FBM witness time and its Brownian witness is assumed.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” Problem 7.9 is separately the forward-Levy question.

## 3. Fresh dated prior-art pass — 2026-09-17

Fresh bounded web searches covered the exact Problem-7.8 wording, the exact paper title and later/citing records, Brownian square-root moving boundaries, two-sided square-root boundaries, and periodic Ornstein--Uhlenbeck first-passage boundaries.

Nearest literature found again includes:

- Shunsuke Sato, *Evaluation of the first-passage time probability to a square root boundary for the Wiener process*, J. Appl. Probab. 14 (1977), 850–856, DOI 10.2307/3213358;
- boundary-crossing approximation work treating one- and two-sided square-root Brownian boundaries, J. Appl. Probab. 36 (1999), 1019–1030, DOI 10.1239/jap/1032374752;
- L. Sacerdote, *Asymptotic behaviour of Ornstein--Uhlenbeck first-passage-time density through periodic boundaries* (1990), DOI 10.1002/asm.3150060106;
- Denisov--Hinrichs--Sakhanenko--Wachtel, *Crossing an Asymptotically Square-Root Boundary by the Brownian Motion*, Proc. Steklov Inst. Math. 316 (2022), 105–120, DOI 10.1134/S0081543822010096.

These are neighboring ordinary-Brownian/OU first-passage results. I did not locate, in this bounded dated pass, a later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating the crossed-exterior FBM theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**. The source Theorem 4.3, Perkins slow-point theorem, continuity, and connectedness arguments are prior machinery, not novelty claims.

## 4. New family: crossed two-ended exterior fans

Let `a,b:(0,infinity)->(0,infinity)` be continuous and assume all four endpoint limits exist and are finite positive numbers:

\[
a_0=\lim_{u\downarrow0}a(u),\qquad
a_\infty=\lim_{u\to\infty}a(u),
\]
\[
b_0=\lim_{u\downarrow0}b(u),\qquad
b_\infty=\lim_{u\to\infty}b(u).
\tag{4.1}
\]

Define the exterior moving shape

\[
\boxed{
\mathcal E[a,b]
=
\{(-u,x):u>0,\ x\le-a(u)\sqrt u\ \text{or}\ x\ge b(u)\sqrt u\}
\cup\{(0,0)\}.
}
\tag{4.2}
\]

Every normalized slice has two unbounded components, but unlike run 21 their apertures genuinely depend on scale. The **crossed subclass** is characterized by

\[
\boxed{a_0<1<a_\infty,\qquad b_\infty<1<b_0.}
\tag{4.3}
\]

(up to reflection, which exchanges left and right).

This is not a mere parameter change inside the static exterior family. A Brownian rescaling `u -> c u` shifts the profile along scale but preserves the four endpoint limits; reflection exchanges the two branches but does not make the two endpoint values on a branch equal. Static exterior fans have `a_0=a_\infty` and `b_0=b_\infty`. The crossed criticality signature (4.3) is therefore invariant under the frozen trivial equivalences and cannot be rescaled into run 21's self-similar geometry.

Hence a theorem at this scope is one new structural metric point, not one point per profile.

## 5. Negation-first target: an endpointwise admissibility rule is false

Before proving the theorem, I attacked the natural proposed extension

> if at each compactified time end (the seam `u=0` and the far past `u=infinity`) there is at least one connected branch whose frozen one-sided OU exponent is subcritical, then some FBM should be able to follow the whole moving exterior shape.

The canonical profile below has exactly that property, but no FBM can follow it pointwise for all negative times. Thus this proposed rule is false. This is **not** a refutation of the source's open-ended Problem 7.8.

The failure is the quantifier swap

\[
\forall\,\text{end}\ \exists\,\text{subcritical branch}
\quad\not\Rightarrow\quad
\exists\,\text{one branch}\ \forall\,\text{scales}.
\tag{5.1}
\]

## 6. Method #12: the conserved quantity is the branch sign

Suppose a continuous process `X` satisfies the shape constraint (4.2) for every `u>0`, and put

\[
y(u)=\frac{X_{-u}}{\sqrt u},\qquad u>0.
\tag{6.1}
\]

Because `a(u),b(u)>0`, we have `y(u) != 0` for every `u>0`. The function `y` is continuous on the connected interval `(0,infinity)`. Therefore

\[
\boxed{\operatorname{sgn}y(u)\ \text{is constant on }(0,\infty).}
\tag{6.2}
\]

A path cannot use the favorable left branch near one end and later cross to the favorable right branch near the other. This branch label is the exact obstruction that is invisible to an endpoint-by-endpoint spectral test.

## 7. Theorem I0077-R07-T23 — two-ended exterior phase theorem

### (A) Strict far-past classification

If

\[
a_\infty>1\quad\text{and}\quad b_\infty>1,
\tag{7.1}
\]

then every FBM fails eventual confinement to `\mathcal E[a,b]`:

\[
\boxed{
\mathbb P\left(\exists R<\infty:\
X_{-u}\le-a(u)\sqrt u\ \text{or}\ X_{-u}\ge b(u)\sqrt u
\quad\forall u\ge R
\right)=0.
}
\tag{T23-A}
\]

If instead

\[
a_\infty<1\quad\text{or}\quad b_\infty<1,
\tag{7.2}
\]

then there exists a decomposable FBM eventually confined to one branch of `\mathcal E[a,b]` almost surely.

The critical cases `a_\infty=1` or `b_\infty=1` are deliberately left unclassified for exact eventual membership.

### (B) Global pointwise obstruction from opposite ends

Assume

\[
\boxed{
(a_0>1\ \text{or}\ a_\infty>1)
\quad\text{and}\quad
(b_0>1\ \text{or}\ b_\infty>1).
}
\tag{7.3}
\]

Then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
X_0=0\ \text{and}\
\bigl[X_{-u}\le-a(u)\sqrt u\ \text{or}\ X_{-u}\ge b(u)\sqrt u\bigr]
\quad\forall u>0
\right)=0.
}
\tag{T23-B}
\]

Thus a different supercritical end may kill each of the two conserved branches.

## 8. Proof of T23(A)

### 8.1 Universal obstruction when both far-past branches are supercritical

Assume eventual confinement occurs. On the connected tail `[R,infinity)`, the continuous nonzero normalized path `y(u)` has fixed sign.

Suppose first it is negative. Since `a_\infty>1`, choose

\[
1<c<c'<a_\infty.
\tag{8.1}
\]

For all sufficiently large `u`, `a(u)>c'`, hence

\[
y(u)\le-c'.
\tag{8.2}
\]

By (2.1) and strict domain monotonicity,

\[
\lambda_0(-\infty,-c)>1.
\tag{8.3}
\]

Source Theorem 4.3(i) applied to `(-infinity,-c)` forces

\[
\limsup_{u\to\infty}y(u)\ge-c
\quad\text{a.s.}
\tag{8.4}
\]

but (8.2) gives `limsup y <= -c' < -c`, a contradiction.

If the eventual branch is positive, choose `1<c<c'<b_\infty`. Strict monotonicity gives

\[
\lambda_0(c,\infty)>1,
\]

Theorem 4.3(i) forces `liminf y <= c`, while eventual `y>=b(u)>c'` gives `liminf y>=c'>c`, again a contradiction. This proves T23(A)'s obstruction half.

### 8.2 Existence when one far-past branch is subcritical

Assume `b_\infty<1`. Pick

\[
b_\infty<c<1.
\tag{8.5}
\]

Since `(c,infinity)` strictly enlarges the critical half-line `(1,infinity)`, Remark 4.1 and (2.1) give

\[
\lambda_0(c,\infty)<1.
\tag{8.6}
\]

Theorem 4.3(ii) supplies a decomposable FBM with

\[
\liminf_{u\to\infty}y(u)\ge c.
\tag{8.7}
\]

Choose `d` with `b_\infty<d<c`. Eventually `b(u)<d`; (8.7) implies eventually `y(u)>d`, and therefore eventually `y(u)>=b(u)`. Hence this decomposable FBM is eventually confined to the right branch.

If `a_\infty<1`, choose `a_\infty<c<1`. Strict enlargement of the critical left half-line gives `lambda_0(-infinity,-c)<1`; Theorem 4.3(ii) supplies a decomposable FBM with `limsup y<=-c`. Choosing `a_\infty<d<c` gives eventually `a(u)<d` and eventually `y(u)<-d<=-a(u)`. This proves the existence half.

## 9. Proof of T23(B)

Assume, to the contrary, that a sample path satisfies the pointwise shape condition for every `u>0`. By Section 6, exactly one branch is used for all scales.

### 9.1 Negative branch

Suppose

\[
y(u)\le-a(u)\quad\forall u>0.
\tag{9.1}
\]

If `a_\infty>1`, the far-past argument in Section 8.1 already gives a contradiction.

It remains the case `a_0>1`. Choose

\[
1<c<c'<a_0.
\tag{9.2}
\]

For some `delta>0`,

\[
X_{-u}\le-c'\sqrt u\qquad(0<u\le\delta).
\tag{9.3}
\]

Now use the FBM definition. Let `{S_n}` be its Brownian witness times. On any sample satisfying (9.3), choose `n` so far to the left that `S_n<-delta`, which is possible because `S_n->-infinity`. The forward view

\[
W_n(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Put `T=-S_n>delta`. Because the confinement event includes `X_0=0`, for `0<u<=delta`,

\[
W_n(T-u)-W_n(T)=X_{-u}-X_0\le-c'\sqrt u\le-c\sqrt u.
\tag{9.4}
\]

Thus `W_n` has a backward cone point with one-sided cone `(-infinity,-c]`. By (2.1) and strict monotonicity,

\[
\lambda_0(-\infty,-c)>1.
\]

Perkins' pathwise no-cone-point theorem (2.2), together with the same Brownian time-reversal used explicitly in the source proof of Theorem 4.3, says the probability that a standard Brownian path has *any* such backward cone point is zero. This statement quantifies over the terminal time, so it remains valid although `T=-S_n` is random; no independence is assumed. For each fixed witness index `n` the bad event is null, and a countable union over `n` is null. Hence the negative branch is impossible whenever `a_0>1` or `a_\infty>1`.

### 9.2 Positive branch

If instead

\[
y(u)\ge b(u)\quad\forall u>0,
\]

then `b_\infty>1` is ruled out by the right-half-line far-past argument. If `b_0>1`, choose `1<c<c'<b_0`; for small `u`, `X_{-u}>=c' sqrt(u)`, and the same FBM-witness/time-reversal argument produces a forbidden Brownian backward cone in `[c,infinity)`, whose exponent is `>1` by the critical identity `lambda_0(1,infinity)=1`. Thus the positive branch is also impossible.

Condition (7.3) guarantees that whichever conserved branch the path chooses, one of its two ends is supercritical. This proves T23(B).

## 10. Canonical crossed profile: each endpoint has a good branch, but globally no branch works

Take

\[
\boxed{
a(u)=\frac12+\frac32\frac{u}{1+u},\qquad
b(u)=2-\frac32\frac{u}{1+u}.
}
\tag{10.1}
\]

Then

\[
(a_0,b_0)=\left(\frac12,2\right),
\qquad
(a_\infty,b_\infty)=\left(2,\frac12\right).
\tag{10.2}
\]

At the seam, the left frozen half-line is subcritical:

\[
\lambda_0(-\infty,-1/2)<1,
\]

while the right branch is supercritical. In the far past the roles reverse:

\[
\lambda_0(1/2,\infty)<1,
\]

while the left branch is supercritical. Thus the endpointwise criterion `forall end exists subcritical branch` is satisfied.

Nevertheless, T23(B) applies because `a_\infty=2>1` and `b_0=2>1`. Therefore

\[
\boxed{
\mathbb P\left(
X_0=0,\ 
X_{-u}\le-\left(\frac12+\frac32\frac{u}{1+u}\right)\sqrt u
\ \text{or}\ 
X_{-u}\ge\left(2-\frac32\frac{u}{1+u}\right)\sqrt u
\quad\forall u>0
\right)=0
}
\tag{10.3}
\]

for every FBM.

At the same time `b_\infty=1/2<1`, so T23(A)'s existence half gives a decomposable FBM that is eventually confined to the **right** branch in the far past. The failure is therefore genuinely a global gluing/branch-selection obstruction, not simple far-past inadmissibility.

This is method #27 in its sharp form: the favorable branch may depend on the endpoint, but continuity demands one branch for the whole negative-time ray.

## 11. What the three methods did

### #6 — DEFORM TO A POINT YOU CAN SOLVE

I started from run 21's static exterior fan and let the left/right thresholds deform continuously between two exactly solvable source half-lines. Tracking the deformation shows that crossing the source critical value `1` at opposite compactified ends is the important invariant. This succeeded and produced the family (4.2)–(4.3).

### #12 — FIND WHAT IS CONSERVED

The normalized path cannot hit zero while staying in the exterior shape. Its sign is therefore conserved on `(0,infinity)`. This one-bit invariant is the proof mechanism that static endpoint tests miss. It is the decisive new route.

### #27 — SWAP THE QUANTIFIERS

I tested `forall end exists a good branch` against the stronger condition `exists one branch good at all required ends`. The canonical profile satisfies the former and fails the latter, and T23(B) proves that the latter distinction is real rather than heuristic. This falsifies a natural proposed extension rule without mislabeling Problem 7.8 as refuted.

## 12. Why this earns metric point 22

Run 21's exterior fans are exactly self-similar: after normalization their two ray thresholds are constant in `u`. The present crossed class has persistent two-ray topology but an order-one **scale-dependent branch swap**:

\[
a_0<1<a_\infty,\qquad b_\infty<1<b_0.
\]

No Brownian rescaling can change either endpoint limit, and reflection only swaps the two branches. Hence no trivial equivalence turns a crossed fan into a static exterior fan. The theorem also contains information absent from run 21: one may have a decomposable FBM with eventual tail confinement while every FBM is globally pointwise excluded because the viable component changes between the two compactified ends.

Accordingly the frozen metric moves

\[
\boxed{21\longrightarrow22},
\qquad
\text{unchanged count}=0.
\]

This counts the crossed profile class once, not once per choice of `a,b`.

## 13. Validation, audits, status, and remaining obligation

There is no new finite combinatorial/arithmetic core here: the threshold comparisons use the source's exact identities (2.1), strict domain monotonicity, and the pathwise Perkins theorem. Manufacturing a checker would not validate the theorem and would violate the research-first policy. No checker was created.

The newest neighboring R06 report independently audits the **preceding** T22 theorem and records

`R06-AUDIT-R07-I0077-T22-20260917T134553Z = PASS_SCOPED / NOVELTY_UNVERIFIED`.

That audit is useful continuity evidence but does **not** audit the new T23 theorem. I found no P26 end-to-end audit of T23 and no second OTHER-track audit of T23. Therefore:

- T23 is a new R07 theorem-sized claim with a complete proof on this page;
- source Problem 7.8 remains **PARTIAL**, not CLOSED;
- publication novelty remains **UNVERIFIED**;
- no `paper_<name>/` closure package is created in this run.

The clean next mathematical obligation is to understand the **critical crossed cases** where one or more endpoint values equal exactly `1`, or to find a genuinely different geometry rather than merely varying the present profiles. If the fixed metric stops moving for three runs, the owner’s stuck protocol applies; it does not apply this run because the metric moved.

## 14. Model / reasoning / scheduler-control status

The limitation is unchanged at the actually exposed task interface. Available task controls are prompt/title, schedule/start offset, timing mode and enabled state. There is **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry** exposed to this worker. GPT-6/maximum therefore remains requested prompt text only, not an enforceable or verified runtime setting, and an hourly schedule does not guarantee an hour of execution.

The historical `You cannot modify this task` result for P26 was authorization-context-specific; repository evidence also records that another authorized context later succeeded in updating P26. The lawful remedy for a denied native task is the owning authorized account/workspace context or platform support exposing the controls — not a duplicate task, repository edit, or permission bypass. No scheduler mutation was attempted here.

## 15. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  claim_id: I0077-R07-T23
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 21
  after: 22
  movement: +1
  unchanged_count: 0
  new_family: "crossed two-ended exterior fans"
  methods_this_run: [6, 12, 27]
  negation_test: "endpointwise forall-end/exists-branch subcriticality is insufficient for global confinement"
  theorem_scope:
    far_past_obstruction: "a_infty>1 and b_infty>1 => no FBM eventual confinement"
    far_past_existence: "a_infty<1 or b_infty<1 => some decomposable FBM eventual confinement"
    global_obstruction: "each branch has at least one supercritical endpoint => no FBM pointwise confinement for all u>0"
    critical_equalities: UNCLASSIFIED
  canonical_profile:
    a0: "1/2"
    a_infty: "2"
    b0: "2"
    b_infty: "1/2"
  finite_core: NONE
  self_check: "analytic only; no checker warranted"
  prior_art: "bounded dated search completed; no explicit exact Problem-7.8/T23 resolution located; novelty UNVERIFIED"
  audits:
    new_T23_p26: PENDING_NOT_FOUND
    new_T23_second_other_track: PENDING_NOT_FOUND
    predecessor_T22_R06: "PASS_SCOPED / NOVELTY_UNVERIFIED"
  source_status: PARTIAL
  closure: false
  paper_package: false
  remaining_obligation: "critical crossed endpoint cases or a genuinely distinct next geometry; two external audits required before any closure claim"
```

No email/Gmail, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, or scheduler change was performed.

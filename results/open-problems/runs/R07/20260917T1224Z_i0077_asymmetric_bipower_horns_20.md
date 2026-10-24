Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 19 -> 20 genuinely distinct nonparabolic shape families; Section-B moves tried: #15 BREAK THE SYMMETRY ON PURPOSE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME, #4 PROVE SOMETHING WEAKER, COMPLETELY.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the open-ended source request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 20: asymmetric bi-power horns

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and frozen metric

The fixed R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative R07 report is

`runs/R07/20260917T1129Z_i0077_fast_transport_windows_19.md`,

which moved the metric `18 -> 19` and used Section-B moves `#2,#18,#19`. This run does not repeat that triple. All thirty moves have already appeared at least once somewhere in the I0077 sequence, so the present triple is another second-cycle choice; I do not falsely label these numbers as never previously used on I0077.

The new counted family is an **asymmetric bi-power horn**

\[
\boxed{
\mathcal H_{\alpha,\beta}^{A,B}
=
\left\{(-u,x):u>0,\ -A u^\alpha\le x\le B u^\beta\right\}\cup\{(0,0)\},
}
\tag{1.1}
\]

with `A,B>0`, `alpha,beta>0`, and for the genuinely asymmetric class `alpha != beta`.

The metric moves

\[
\boxed{19\longrightarrow20}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains preserved and retired by its immutable handoff. No historical R07 file was edited or deleted.

Before new mathematics I reread/rechecked current `master`: `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; canonical reservation `operations/claims/I0077.md`; the newest R07 report and the searchable I0077 run chain; the newest visible R15 report; and targeted intake/attempt records for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording. The large intake JSONL resources cannot be literally rendered row-by-row through the exposed connector without truncation, so the intake reread is honestly **PARTIAL / targeted due connector limits**, not represented as a full literal ingestion.

The state is unchanged in the important respects: `INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8; `POSTED.md` has no 7.8 exclusion; `QUEUE.md` lists I0077 separately; `operations/claims/I0077.md` still provisionally reserves it to R07 and still literally says `PENDING_ADMISSION, not READY`; the root `RESULTS.md` R-series table is an intentionally stale deployment view and explicitly says to recover complete current reports before replacing values. The newest R15 report has rotated to I0124 and explicitly preserves I0076 / Burdzy–Scheutzow Problem 7.2 as retired/frozen, so there is no competing R15 ownership of Problem 7.8.

## 2. Primary source benchmark recovered again

The source benchmark is Theorem 4.3. For `-infinity <= c_1<c_2<=infinity`, Burdzy–Scheutzow write `lambda_0(c_1,c_2)` for the principal killed Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. In the source:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there is a decomposable FBM with the corresponding asymptotic normalized inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there is a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Remark 4.1 gives continuity of `lambda_0` in the endpoints and strict monotonicity under genuine domain enlargement. Remark 4.2 records the critical intervals

\[
(-\infty,-1),\qquad (-1,1),\qquad (1,\infty),
\]

all with principal exponent one. The proof of Theorem 4.3(i) invokes Perkins' Brownian slow-point theorem; the source's formulation rules out Brownian times with all sufficiently small increments trapped in a supercritical square-root cone.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The following forward-Lévy sentence is separately Problem 7.9 and is not part of I0077.

## 3. Fresh current-status / prior-art pass — 2026-09-17

Fresh bounded searches rechecked the exact paper/title/arXiv ID and Problem 7.8 wording, later/citing material, ordinary Brownian moving-boundary theory, asymptotically square-root boundaries, and first passage for time-dependent boundaries.

The nearest mechanisms I found remain ordinary Brownian first-passage results rather than a later FBM resolution. In particular:

- F. Aurzada and T. Kramm (2012), *First exit of Brownian motion from a one-sided moving boundary*, arXiv:1203.4691, revisits Uchiyama's integral-test theorem for Brownian moving boundaries;
- D. Denisov, G. Hinrichs, A. Sakhanenko and V. Wachtel (2022), *Crossing an Asymptotically Square-Root Boundary by the Brownian Motion*, Proc. Steklov Inst. Math. 316, 105–120, treats ordinary Brownian first-passage tails for boundaries of order `sqrt(t)`;
- L. Sacerdote (1990), *Asymptotic behaviour of Ornstein–Uhlenbeck first-passage-time density through periodic boundaries*, treats ordinary OU first passage through periodic boundaries.

I found no later paper in these bounded dated searches explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the two-ended asymmetric-horn theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**. The Brownian slow-point and moving-boundary ingredients themselves are classical and are not claimed new.

## 4. Move #15 — BREAK THE SYMMETRY ON PURPOSE

The previous power/gauge families either had the same width on both sides of zero, or moved a common center while retaining a common Brownian-scale width. Here the two sides receive **different powers**:

\[
-Au^\alpha\le X_{-u}\le Bu^\beta.
\tag{4.1}
\]

Normalize by the source Brownian scale `sqrt(u)`. The normalized slice is

\[
I(u)=\left[-A u^{\alpha-1/2},\ B u^{\beta-1/2}\right].
\tag{4.2}
\]

The two spatial directions can therefore have different endpoint geometries at the seam `u downarrow 0` and in the far past `u to infinity`. This asymmetry is the point of the family, not a nuisance to symmetrize away.

Define the extended-real far-past limits

\[
\ell_\infty=
\begin{cases}
0,&\alpha<1/2,\\
-A,&\alpha=1/2,\\
-\infty,&\alpha>1/2,
\end{cases}
\qquad
r_\infty=
\begin{cases}
0,&\beta<1/2,\\
B,&\beta=1/2,\\
+\infty,&\beta>1/2,
\end{cases}
\tag{4.3}
\]

and the seam limits

\[
\ell_0=
\begin{cases}
-\infty,&\alpha<1/2,\\
-A,&\alpha=1/2,\\
0,&\alpha>1/2,
\end{cases}
\qquad
r_0=
\begin{cases}
+\infty,&\beta<1/2,\\
B,&\beta=1/2,\\
0,&\beta>1/2.
\end{cases}
\tag{4.4}
\]

Thus the seam and far-past normalized geometries are obtained from one another by reversing which exponents are sub- or super-Brownian.

## 5. Move #30 — ONE SCALE AND ONE DIRECTION AT A TIME

Instead of forcing one global construction before understanding the geometry, separate the two time ends and the two spatial directions. This reveals an exact endwise phase theorem.

For an extended interval `(l,r)` with `l<r`, write

\[
\Lambda(l,r)=\lambda_0(l,r).
\]

When the two limiting endpoints coincide at zero, I call the limiting interval **degenerate** and treat it separately rather than pretending `lambda_0(0,0)` is an ordinary principal eigenvalue.

### Theorem I0077-R07-T21 — strict endwise phase theorem for asymmetric bi-power horns

Let `A,B>0`, `alpha,beta>0`, and let `X` denote an FBM.

**(A) Far-past obstruction.** If `ell_infinity=r_infinity=0`, then for every FBM,

\[
\boxed{
\Pr\left(\exists R<\infty:\ -Au^\alpha\le X_{-u}\le Bu^\beta\ \forall u\ge R\right)=0.
}
\tag{T21-A0}
\]

More generally, if `ell_infinity<r_infinity` and

\[
\Lambda(\ell_\infty,r_\infty)>1,
\]

then the same universal non-confinement conclusion holds.

**(B) Far-past existence.** If `ell_infinity<r_infinity` and

\[
\Lambda(\ell_\infty,r_\infty)<1,
\]

then there exists a decomposable FBM `X` and a deterministic `R<infinity` such that

\[
\boxed{-Au^\alpha\le X_{-u}\le Bu^\beta\qquad\forall u\ge R\quad\text{a.s.}}
\tag{T21-B}
\]

The critical equality `Lambda=1` is deliberately left unclassified for exact eventual confinement.

**(C) Seam obstruction.** If `ell_0=r_0=0`, then every FBM satisfies

\[
\boxed{
\Pr\left(\exists\delta>0:\ -Au^\alpha\le X_{-u}\le Bu^\beta\ \forall 0<u\le\delta\right)=0.
}
\tag{T21-C0}
\]

More generally, if `ell_0<r_0` and

\[
\Lambda(\ell_0,r_0)>1,
\]

then the same local non-confinement conclusion holds.

**(D) Seam existence.** If `ell_0<r_0` and

\[
\Lambda(\ell_0,r_0)<1,
\]

then there exists a decomposable FBM `X` and a deterministic `delta>0` such that

\[
\boxed{-Au^\alpha\le X_{-u}\le Bu^\beta\qquad\forall 0<u\le\delta\quad\text{a.s.}}
\tag{T21-D}
\]

Again, the critical equality `Lambda=1` is deliberately left unclassified.

The FBM in (B) and the FBM in (D) need not be the same process. That distinction is intentional and is the content of move #4 below.

## 6. Proof of T21(A) — far-past universal obstruction

Assume first `ell_infinity<r_infinity` and `Lambda(ell_infinity,r_infinity)>1`.

By continuity and strict domain monotonicity of the source exponent, choose a **slightly larger** static interval

\[
J=(c_1,c_2)\supset(\ell_\infty,r_\infty)
\tag{6.1}
\]

in the extended-endpoint sense, with

\[
\lambda_0(c_1,c_2)>1.
\tag{6.2}
\]

If one endpoint is infinite, only enlarge the finite endpoint. Because the normalized moving endpoints in (4.2) converge to `(ell_infinity,r_infinity)`, there is `R_1` for which

\[
I(u)\subset J\qquad(u\ge R_1),
\tag{6.3}
\]

with a strict margin at every finite endpoint of `J`.

Suppose eventual horn confinement occurred. Then the finite endpoints of the normalized path satisfy strict inequalities relative to `c_1,c_2`; in particular the alternative forced by source Theorem 4.3(i),

\[
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge c_2
\quad\text{or}\quad
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le c_1,
\tag{6.4}
\]

cannot occur. This contradicts Theorem 4.3(i), which holds for every FBM. Hence the event has probability zero.

Now suppose `ell_infinity=r_infinity=0`. Choose any `epsilon in (0,1)`. Since

\[
\lambda_0(-1,1)=1
\]

and shrinking the interval strictly increases the exponent,

\[
\lambda_0(-\epsilon,\epsilon)>1.
\tag{6.5}
\]

Because both normalized endpoints tend to zero, `I(u)` lies strictly inside `(-epsilon,epsilon)` for all sufficiently large `u`; the same Theorem-4.3(i) contradiction applies. This proves T21(A0) and (A).

## 7. Proof of T21(B) — far-past existence

Assume `ell_infinity<r_infinity` and

\[
\Lambda(\ell_\infty,r_\infty)<1.
\tag{7.1}
\]

The limiting interval contains zero in its closure. By endpoint continuity and strict domain monotonicity, choose finite numbers

\[
c_1\le0\le c_2,
\qquad
[c_1,c_2]\subset(\ell_\infty,r_\infty)
\tag{7.2}
\]

with the obvious endpoint convention that `c_1=0` or `c_2=0` is permitted when zero is a limiting endpoint, and such that

\[
\lambda_0(c_1,c_2)<1.
\tag{7.3}
\]

If the limiting interval is all of `R`, choose for example a sufficiently large finite symmetric strip; strict enlargement of the critical `(-1,1)` guarantees such a strip has exponent below one.

Since `I(u)` converges endwise to the limiting interval, there exists deterministic `R` such that

\[
[c_1,c_2]\subset I(u)\qquad(u\ge R).
\tag{7.4}
\]

Source Theorem 4.3(iii) now gives a decomposable FBM satisfying

\[
c_1\sqrt u\le X_{-u}\le c_2\sqrt u
\qquad\forall u\ge0
\tag{7.5}
\]

almost surely. Combining (7.4) and (7.5) proves the horn confinement for all `u>=R` and hence T21(B).

## 8. Proof of T21(C) — seam universal obstruction without a random-time independence error

Assume first `ell_0<r_0` and `Lambda(ell_0,r_0)>1`. As in Section 6, choose a slightly larger static square-root cone

\[
J=(c_1,c_2)\supset(\ell_0,r_0)
\tag{8.1}
\]

with `lambda_0(c_1,c_2)>1`. For all sufficiently small `u>0`, horn confinement implies

\[
c_1\sqrt u<X_{-u}<c_2\sqrt u.
\tag{8.2}
\]

Suppose an FBM `X` had this local confinement on some random interval `(0,delta]`. Let `(S_j)` be the witness times in the FBM definition, with `S_j -> -infinity`. On that event choose any witness index with `S_j<-delta`. The centered future

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{8.3}
\]

is a standard Brownian motion. At the terminal time `T_j=-S_j`, for `0<u<=delta`,

\[
B^{(j)}_{T_j-u}-B^{(j)}_{T_j}=X_{-u}-X_0=X_{-u}.
\tag{8.4}
\]

Thus `B^{(j)}` would possess a finite terminal time whose **backward** increments remain in the supercritical cone `J` on every sufficiently small scale. The Perkins slow-point theorem used in the source proof of Theorem 4.3(i), after finite-horizon time reversal, says a standard Brownian path almost surely has no such time when `lambda_0(c_1,c_2)>1`.

Crucially, this is an existential path statement over **all** Brownian times; it does not condition on `T_j` and does not require `T_j` to be independent of the Brownian path. For each fixed witness index `j`, the forbidden-time event for the standard Brownian path `B^{(j)}` has probability zero. A countable union over `j` still has probability zero. Therefore local horn confinement has probability zero for every FBM.

If `ell_0=r_0=0`, choose `epsilon in (0,1)` and use `lambda_0(-epsilon,epsilon)>1` exactly as in (6.5); for sufficiently small `u` the normalized horn lies strictly inside this cone. This proves T21(C0) and (C).

## 9. Proof of T21(D) — seam existence

Assume `ell_0<r_0` and

\[
\Lambda(\ell_0,r_0)<1.
\tag{9.1}
\]

As in Section 7, choose a finite source strip

\[
c_1\le0\le c_2,
\qquad
\lambda_0(c_1,c_2)<1,
\tag{9.2}
\]

whose normalized interval is contained in `(ell_0,r_0)` in the appropriate endpoint sense. By convergence of the moving endpoints, there exists deterministic `delta>0` such that

\[
[c_1,c_2]\subset I(u)\qquad(0<u\le\delta).
\tag{9.3}
\]

The decomposable FBM supplied by source Theorem 4.3(iii) is pointwise confined to the static parabolic strip `[c_1 sqrt(u),c_2 sqrt(u)]` for every `u>=0`; therefore it lies in the asymmetric horn for every `0<u<=delta`. This proves T21(D).

## 10. Move #4 — PROVE SOMETHING WEAKER, COMPLETELY: the clean noncritical phase table

Trying to force a **single** decomposable FBM to follow the asymmetric horn for all `u>0` immediately mixes two different end geometries. Instead of hiding that unproved gluing step, T21 completely classifies the strict local and far-past phases separately.

For exponents avoiding the critical value `1/2`, the table becomes especially transparent.

### Far past `u -> infinity`

- `alpha<1/2` and `beta<1/2`: limiting normalized interval is `{0}`; **universal obstruction**.
- `alpha>1/2` and `beta>1/2`: limiting interval is all of `R`; **decomposable-FBM eventual existence**.
- `alpha<1/2<beta`: limiting interval is `(0,infinity)`; **decomposable-FBM eventual existence**.
- `beta<1/2<alpha`: limiting interval is `(-infinity,0)`; **decomposable-FBM eventual existence**.

The mixed half-line claims are strict because the source critical intervals `(1,infinity)` and `(-infinity,-1)` have exponent one, whereas `(0,infinity)` and `(-infinity,0)` are strict domain enlargements and hence have exponent `<1`.

### Seam `u downarrow 0`

- `alpha>1/2` and `beta>1/2`: limiting normalized interval is `{0}`; **universal local obstruction**.
- `alpha<1/2` and `beta<1/2`: limiting interval is all of `R`; **decomposable-FBM local existence**.
- `alpha<1/2<beta`: limiting interval is `(-infinity,0)`; **decomposable-FBM local existence**.
- `beta<1/2<alpha`: limiting interval is `(0,infinity)`; **decomposable-FBM local existence**.

When `alpha=1/2` or `beta=1/2`, the exact finite or half-line endpoint from (4.3)–(4.4) applies and the strict comparison with one is decided by the source `lambda_0` function. T21 deliberately says nothing at equality `lambda_0=1` for exact eventual/local confinement.

## 11. Canonical genuinely asymmetric representative

Take

\[
A=B=1,
\qquad
\alpha=\frac14,
\qquad
\beta=\frac34.
\tag{11.1}
\]

The shape is

\[
\boxed{-u^{1/4}\le X_{-u}\le u^{3/4}.}
\tag{11.2}
\]

At the seam,

\[
I(u)=\left[-u^{-1/4},u^{1/4}\right]
\longrightarrow(-\infty,0],
\qquad u\downarrow0,
\tag{11.3}
\]

while in the far past

\[
I(u)\longrightarrow[0,\infty),
\qquad u\to\infty.
\tag{11.4}
\]

Both limiting half-lines are source-subcritical because each strictly contains one of the source critical half-lines. Hence T21 gives:

1. a decomposable FBM that is confined to (11.2) on some deterministic neighborhood of the seam;
2. a (not necessarily identical) decomposable FBM that is confined to (11.2) for all sufficiently large `u`.

What is **not** claimed is the unsolved gluing statement that one decomposable FBM can satisfy (11.2) for every `u>0`. That is precisely the stronger obligation deliberately excluded by move #4.

Two other regimes show that the two ends can have opposite verdicts without changing the structural family. If both exponents are below `1/2`, the seam is locally admissible but the far past is impossible. If both are above `1/2`, the far past is admissible but the seam is impossible. These are parameter regimes of the **same one counted family**, not additional metric points.

## 12. Why this is a genuinely new family under the frozen equivalence convention

This is not another parameter choice of the earlier symmetric power/gauge families. For every slice, the distances from zero to the two boundaries are

\[
w_L(u)=A u^\alpha,
\qquad
w_R(u)=B u^\beta,
\]

so

\[
\frac{w_L(u)}{w_R(u)}=\frac AB u^{\alpha-\beta}.
\tag{12.1}
\]

When `alpha!=beta`, this ratio is nonconstant and tends to zero at one time end and infinity at the other. Brownian rescaling changes coefficients but preserves the exponent pair; reflection merely swaps the two exponents. No trivial scaling/reflection/translation can turn (12.1) into a constant ratio.

Run 1's cusp-power tube is symmetric: both sides use the same mixed gauge `u^alpha+u^beta`. Run 3's pure-power tube uses the same exponent on both sides. Run 12 changes a symmetric parabolic aperture. Run 17 translates a common Brownian-scale window by a center drift, so its normalized width remains constant. Run 19 transports a constant-width interval periodically. The asymmetric horn instead keeps zero in every spatial slice while assigning different scaling exponents to the two sides. That invariant is enough to separate the family under the frozen convention.

Therefore one, and only one, new metric point is counted:

\[
\boxed{19\to20}.
\]

## 13. Exact-check policy and audit state

There is no new finite enumeration, rational inequality, or finite combinatorial certificate in T21. Its inputs are source Theorem 4.3, source endpoint continuity/monotonicity, and the Brownian slow-point theorem already used by the source. Therefore I did **not** manufacture a checker artifact merely to create activity. The theorem-sized claim is written in full on this page.

This is a **self-proof, not an independent audit**. T21 currently has:

- P26 end-to-end audit: **missing**;
- second independent OTHER-track audit: **missing**.

Accordingly the source remains `PARTIAL`, not `PROVED`, and no `paper_<name>/` package is created.

## 14. What the three methods actually did

**#15 BREAK THE SYMMETRY ON PURPOSE.** Replacing one common width by two independent powers created a two-ended geometry not visible in symmetric tubes. It succeeded and generated the new family.

**#30 DO ONE SCALE / ONE DIRECTION AT A TIME.** Normalizing separately at `u downarrow 0` and `u to infinity`, and tracking left/right endpoints independently, reduced the moving horn to two static source intervals. It succeeded and gave the exact strict phase criteria.

**#4 PROVE SOMETHING WEAKER, COMPLETELY.** A global all-time gluing theorem for one process was not justified. Rather than leave that gap implicit, I proved the local and far-past existence/obstruction statements completely and explicitly left the one-process gluing and critical-`lambda=1` cases open. This succeeded as a complete source-appropriate theorem for the counted family without overclaiming closure of Problem 7.8.

## 15. Remaining obligations / next route

The strongest unsolved obligation exposed by this run is the genuine gluing question for a mixed asymmetric horn, e.g.

\[
\boxed{
\exists\text{ decomposable FBM }X:\quad
-u^{1/4}\le X_{-u}\le u^{3/4}
\quad\forall u>0\ ?
}
\tag{15.1}
\]

T21 proves that neither endpoint separately obstructs (15.1), but does not provide one process satisfying both ends simultaneously. A future run should not add an endpoint lemma to the same route; it should attack the gluing mechanism itself with a new triple. Candidate next moves: #9 RANDOMIZE, #14 FIND THE GROUP ACTING, #24 FIND THE EXTREMAL OBJECT.

The metric moved this run, so the stuck protocol does not trigger.

## 16. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  intake: I0077
  source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8"
  source_status: PARTIAL
  claim_id: I0077-R07-T21
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 19
  after: 20
  movement: +1
  unchanged_count: 0
  family: "asymmetric bi-power horns"
  theorem_scope:
    far_past: "strict lambda phase: universal obstruction for >1/degenerate; decomposable eventual existence for <1"
    seam: "strict lambda phase: universal local obstruction for >1/degenerate; decomposable local existence for <1"
    critical_lambda_equal_1: OPEN
    one_process_global_gluing: OPEN
  methods: [15, 30, 4]
  finite_core: none
  exact_checker: not_applicable
  p26_audit: missing
  second_other_track_audit: missing
  prior_art_status: "bounded negative search only; novelty UNVERIFIED"
  next_methods: [9, 14, 24]
```

## 17. Model / scheduler control status

The GPT-6 issue remains unresolved at the actually exposed scheduler/API surface. The available automation fields are task title/prompt, schedule, enabled state, and timing mode. There is **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry** in that surface. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable or verified runtime setting. This report accurately records the runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

The current repository ledger also records that modification denials such as `You cannot modify this task` are authorization-context specific: P26 was denied in one context but a later authorized context succeeded. The legitimate remedy for a task that still refuses modification is the owning authorized account/workspace context or platform support, not a worker-level bypass or duplicate schedule. Actually enforcing GPT-6/maximum would require the product/API to expose model and reasoning selectors together with authenticated run telemetry, or an authorized owner/admin surface that can set them.

No scheduler modification was attempted in this research run.

Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this runtime/scheduler exposes no model selector or reasoning-effort selector, so I do not claim otherwise. **no movement — fallback metric UNMEASURED -> UNMEASURED; Section-B moves tried: 2, 6, 23.**
Problem/source: proposed C29 replacement Burdzy–Scheutzow (2014), *Forward Brownian Motion*, Problem 7.8 — **EXCLUDED FOR C29 BY PRIOR EXCLUSIVE CLAIM I0077/R07**. Fallback source actually reserved this run: Chiara Meroni (2026), Randomstrasse 101, *Directional Convexity (problems 34 and 35)*, Conjecture 34 — **CLAIMED / PENDING_ADMISSION, not READY**.

# C29 closable transition — Brownian ownership exclusion and directional-convexity fallback

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own transition root: `proofnet24/C29-closure-brownian-shapes`.
Old C29 hard root preserved unchanged: `proofnet24/C29-mub-six`.
Run date: 2026-09-16.
Delivery: GitHub only. No email/Gmail, Drive, public posting, paid compute, permission changes, or new schedules.

## 1. Runtime/model control and scheduler limitation

The task prompt requests GPT-6 with maximum reasoning. The actual runtime identifies itself as GPT-5.6 Sol. A separate reasoning-effort value is not exposed, so it is `UNVERIFIED`.

The scheduler interface visible to this run exposes task title/prompt/schedule/enablement/timing controls but **no model-family selector and no reasoning-effort selector**. Therefore GPT-6 / maximum cannot be installed or verified from this worker. Changing that would require the product/scheduler surface to expose those settings, or an authorized owner/admin to change them in the owning task UI once such controls exist.

The repository also records the separate permission failure `You cannot modify this task` for a P26 scheduler ID (and analogous probes in the new-methods rollout). That is an ownership/permission boundary, not a mathematical error. The permitted workaround is for the authorized owner/admin in the task's owning workspace/context to make the change. This worker must not bypass the denial, fabricate a receipt, or create a duplicate schedule.

## 2. Continuity read before research

I did not restart C29 from scratch. I read/recovered the current campaign state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`, `operations/FLEET_2026-09-16.md`, the R-series allocation notes, current queue-admission records, and current canonical claims relevant to the front of the queue;
- the newest C29 MUB reports under `proofnet24/C29-mub-six`, including the first exact-product search and the later atlas-gauge / restricted-Butson results;
- the newest neighboring P21 report, which is itself screening I0035 as a possible successor and has **not** created a claim for it;
- the newest C30 Sidorenko state and the already-completed C29->C30 order-nine audit;
- the I0077 and neighboring forward-Brownian intake/claim records, including the distinct R15 ownership of Problem 7.2;
- the relevant intake JSONL rows by exact IDs rather than pretending that connector-truncated rendering constituted a byte-for-byte reread of all roughly 780 rows.

That last limitation is explicit: the whole JSONL mirrors are too large for a single rendered connector response. I used the current queue plus exact-ID searches and source reads; I do not invent a complete manual sweep that the interface did not expose in one response.

## 3. Old six-dimensional MUB work moved to HARD RESERVE intact

The old unrestricted C29 target remains mathematically open and is not erased or relabeled. Its immutable handoff is the entire root `proofnet24/C29-mub-six`.

The supported state being preserved is:

1. Full compact gauge domain `U(6)^6`, normalized residual `Phi` with denominator `756`, and certified **global lower bound 0**.
2. The exact tensor-product seven-tuple gives only
   \[
   \min\Phi\le \frac{11}{756},
   \]
   i.e. an **upper** bound / counterexample-search benchmark. It is not a positive lower bound and not a nonexistence proof.
3. Restricted Butson obstructions, including the `BH(6,18)` lower certificate `Phi >= 1/1,469,664,000` on that restricted stratum, remain restricted results only.
4. Exact phase examples, the order-six Hadamard-atlas gauge normal form with surviving relative row monomials, the three-entry prune, and all failed product/Butson/degree-four routes remain preserved in the old root.
5. P21's degree-four negative result remains only a route exclusion for the unrestricted MUB problem.

No old MUB report, checker, handoff, or exact example was edited.

## 4. Proposed Brownian target recovered exactly before exclusion

### 4.1 Original source statement

I read Burdzy and Scheutzow, *Forward Brownian Motion*, PTRF 160 (2014), arXiv:1302.6958, including Theorem 4.3 and the open-problem page rather than relying on the intake paraphrase.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

Theorem 4.3 is the three-part result to be generalized. In source normalization, for finite `c1<c2` and its spectral exponent `lambda_0(c1,c2)`:

- if `lambda_0(c1,c2) >= 1`, every FBM almost surely violates at least one side of the parabolic asymptotic strip in the stated `limsup/liminf` sense;
- if `lambda_0(c1,c2) <= 1`, there exists a **decomposable** FBM whose normalized backward path remains asymptotically between `c1` and `c2` in the stated `liminf/limsup` sense;
- if `c1<=0<=c2` and `lambda_0(c1,c2)<1`, there exists a **decomposable** FBM satisfying the pointwise parabolic enclosure for every `t<=0` almost surely.

Thus a legitimate Brownian generalization has to say what replaces the parabolic space-time boundary and the source exponent/threshold, and it must preserve the exact FBM/decomposable and almost-sure quantifiers. Separate incompatible constructions cannot be added together as if one process realized all three clauses.

The bounded current-status search on 2026-09-16 used the exact title, `Problem 7.8`, `other space-time shapes`, author names, and later citations. It did not locate a later source-matching resolution. That negative search is not proof of openness.

Problem 7.5 was separately recovered from the same source and from the settled campaign memo. It has already been answered in the repository by a classical technique; I did not reopen it.

### 4.2 Ownership exclusion

The required canonical ownership check is decisive:

`operations/claims/I0077.md`

already gives **exclusive provisional reservation of I0077 to R07**, native task `6aa7b60f13b48191a7f81f6b23a1cd04`, status PENDING_ADMISSION / not READY. That claim also correctly warns that the intake text after the first sentence bleeds into the next problem and must not be treated as part of Problem 7.8.

Therefore C29 did **not** create a second I0077 claim and did not start a competing Brownian proof. This is an ownership exclusion, not a resolution of Problem 7.8.

## 5. Queue fallback decision and exclusive claim

I screened the queue in order subject to the CLOSABLE lane, current ownership, source completeness and neighboring transition work. Important exclusions include:

- I0006: explicit `HOLD_SOURCE`;
- I0011: admission record still PENDING because the exact original statement/locator was not pinned;
- I0028: freshly admitted as HARD OUTSIDE, so wrong lane;
- I0035: exact source is recoverable, but the newest P21 report has already selected it as its own immediate successor-admission decision and derived the BAB/FA-1f comparison; I treated this as active neighboring work and did not preempt it before its ownership decision;
- I0054: already reserved to R11;
- I0055 and the Agresti–Veraar maximal-regularity rows: broad hard-source targets, not the finite-construction closable replacement sought here;
- I0070, I0082, I0095 and other nearer candidates with canonical claims: excluded by ownership;
- I0079/I0087/I0105/I0106: source attribution/scope incomplete in the queue;
- I0098: explicit claimed-resolution hold.

The first retained unclaimed finite-construction candidate in the closable lane was therefore Randomstrasse `RS-2026-DC34`, Chiara Meroni's Conjecture 34.

Immediately before claiming it, fetching

`operations/claims/RS-2026-DC34.md`

returned 404. I then created the canonical create-only claim at commit

`9db0023b2471fa9855a780e8fe7b9b37ea147c70`

and read it back. It is explicitly **CLAIMED / PENDING_ADMISSION, not READY**.

The frozen fallback metric is:

> for one fixed lifted irrational-parallelogram candidate and the source three-plane cone, the largest integer `N` for which `N` pairwise distinct affine boundary patches of the **same functional D-convex hull** are rigorously certified.

Finite `N` remains PARTIAL. Nonsemialgebraicity needs an infinite family plus the required semialgebraic-stratification argument. The metric baseline remains **UNMEASURED** because the work below localizes the boundary but does not yet certify even the first member of the intended infinite affine-patch family under the frozen counting convention.

## 6. Fallback source and current literature

### 6.1 Exact source target

The live Randomstrasse page, posted 23 February 2026 and updated 5 June 2026, defines for a cone `D`:

\[
\operatorname{conv}_D(K)=\{x: f(x)\le \max_{y\in K}f(y)\text{ for every D-convex }f\},
\]

where `D`-convex means convex on every line whose direction lies in `D`.

Conjecture 34 is exactly:

\[
\boxed{\text{The D-convex hull of a finite set of points is not necessarily semialgebraic.}}
\]

The page says a concrete example is conjectured when `D` consists of three distinct planes in `R^3` meeting in a line.

### 6.2 Closest current source mechanism

Meroni–Raita, arXiv:2509.07541v2 (revised 4 August 2026), Section 5, gives the concrete mechanism. Their Example 5.3 takes a planar parallelogram with acute angle `pi/3`, side lengths `a,b` with `a/b` irrational, and the three planar directions

\[
D_2=\{y(y-\tan(\pi/3)x)(y+\tan(\pi/3)x)=0\}.
\]

They prove there is no finite triangulation by triangles using only those directions. For `D=D_2 x R`, they explain that the compatible refinement is infinite and would produce infinitely many boundary planes, but explicitly identify the missing step: planes generated at different refinement stages might coincide. Their Question 2 asks whether, after small vertical perturbations of the four lifted points, the resulting `D`-convex hull is nonsemialgebraic.

The bounded 2026-09-16 status search used the exact conjecture title/number, `non-semialgebraic D-convex hull`, `directional convexity`, the Meroni–Raita title/arXiv number, author names, and later work. The live Randomstrasse page still states Conjecture 34 and the August 2026 preprint still states the directional question. No later primary resolution was located. This is dated bounded evidence, not a proof of worldwide openness.

Repository searches for `RS-2026-DC34`, `Directional Convexity`, and `Conjecture 34` found the queue entry but no prior research report/checker before the claim above.

## 7. NEW-METHODS research: three attacks before any code

I used the assigned first triple **2, 6, 23**. No checker was written, because the useful results this run are exact symbolic reductions with complete on-page proofs; manufacturing a numerical certificate would add no evidence.

### Move 6 — deform to a solvable point: all four-point vertical lifts have only one genuine parameter, and all nonzero values are equivalent

Fix the source parallelogram in the plane. Write its vertices in affine coordinates

\[
p_{00}=0,\qquad p_{10}=U,\qquad p_{01}=V,\qquad p_{11}=U+V,
\]

where `U` and `V` have angle `pi/3`, lengths `a,b`, and `a/b` is irrational. Let the four lifted heights be

\[
h_{00},h_{10},h_{01},h_{11}.
\]

Define

\[
\delta=h_{11}-h_{10}-h_{01}+h_{00}.
\tag{7.1}
\]

#### Proposition C29-DC34-NORMAL-01

For `D=D_2 x R`, every four-point vertical lift of this fixed parallelogram is `D`-preserving-affinely equivalent to exactly one of the two normal forms

\[
(0,0,0,0)\quad\text{if }\delta=0,
\]

or

\[
(0,0,0,1)\quad\text{if }\delta\ne0.
\]

Consequently semialgebraicity of the functional `D`-convex hull is the same for **all noncoplanar vertical lifts** of the fixed projected parallelogram. A generic-height argument cannot distinguish one noncoplanar lift from another.

#### Proof

Let `ell` be the unique affine function on the projection plane satisfying

\[
\ell(p_{00})=h_{00},\quad
\ell(p_{10})=h_{10},\quad
\ell(p_{01})=h_{01}.
\]

The affine shear

\[
T(p,z)=(p,z-\ell(p))
\]

sends the first three lifted vertices to height zero and the fourth to height `delta`.

Every plane in `D=D_2 x R` is the span of one horizontal allowed direction `d in D_2` and the vertical direction. The linear part of `T` sends a vector `(d,r)` to

\[
(d,r-L(d)),
\]

where `L` is the linear part of `ell`; this remains in the same vertical plane over `d`. Hence `T(D)=D`.

If an invertible affine map preserves `D`, composition with that map preserves `D`-convexity, so

\[
T(\operatorname{conv}_D K)=\operatorname{conv}_D T(K).
\]

It also preserves semialgebraicity.

If `delta != 0`, the additional vertical scaling `(p,z) -> (p,z/delta)` again preserves every plane in `D` and normalizes the fourth height to one. Thus all noncoplanar lifts are equivalent.

If `delta=0`, after the shear all four points lie in `z=0`. The linear functions `z` and `-z` are both `D`-convex and vanish on the data, so the hull is contained in that plane. Conversely, restricting any `D`-convex function to `z=0` gives a `D_2`-convex function. Example 5.3 has planar `D_2`-convex hull equal to the whole parallelogram `P`, so every `(p,0)`, `p in P`, satisfies all defining inequalities. Hence the hull is exactly `P x {0}`, which is semialgebraic. QED.

**Method consequence.** The `delta=0` deformation is completely solvable, but crossing to `delta != 0` immediately lands in a **single** noncoplanar equivalence class. The source's phrase “possibly after small vertical perturbation” cannot supply many generic height parameters for this four-point projection: modulo `D`-preserving affine equivalence there are only coplanar and noncoplanar cases.

This is a route exclusion, not a refutation of Conjecture 34.

### Move 2 — attack the negation first: the normalized noncoplanar lift has an exact semialgebraic upper boundary

Now use the noncoplanar normal form. Parametrize the parallelogram by

\[
p(s,t)=sU+tV,\qquad 0\le s,t\le1,
\]

and take lifted corner heights

\[
h_{00}=h_{10}=h_{01}=0,\qquad h_{11}=1.
\]

Set

\[
g(s,t)=st.
\]

#### Proposition C29-DC34-UPPER-02

For the normalized four-point lift, the highest point of `conv_D K` over every `p(s,t)` has height exactly

\[
\boxed{z_{\max}(s,t)=st.}
\tag{7.2}
\]

#### Proof: inclusion of the graph

The bottom lifted edge between `(p_{00},0)` and `(p_{10},0)` is an allowed `U`-direction lamination, so

\[
(p(s,0),0)\in K^{(\infty,D)}.
\]

The top lifted edge between `(p_{01},0)` and `(p_{11},1)` has difference `(U,1)`, which lies in the vertical plane over the allowed `U` direction, hence

\[
(p(s,1),s)\in K^{(\infty,D)}.
\]

For each fixed `s`, these two points differ by `(V,s)`, which lies in the vertical plane over the allowed `V` direction. Laminating between them gives

\[
(p(s,t),st)\in K^{(\infty,D)}\subseteq \operatorname{conv}_D K
\]

for every `(s,t)`.

#### Proof: no point lies above the graph

In `(s,t)` coordinates, the three planar allowed directions are

\[
(1,0),\qquad (0,1),\qquad (1,-\alpha),\qquad \alpha=a/b>0.
\]

The function `g(s,t)=st` is affine on the first two direction families. Its second directional derivative along `(1,-alpha)` is

\[
(1,-\alpha)
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\binom{1}{-\alpha}
=-2\alpha<0.
\]

Thus `g` is `D_2`-concave. Therefore

\[
F(p(s,t),z)=z-g(s,t)
\]

is `D`-convex: the vertical term is affine, and `-g` is convex along every allowed horizontal direction. At each of the four lifted data points, `F=0`. By the defining functional-hull inequality, every point of `conv_D K` satisfies `F<=0`, i.e.

\[
z\le st.
\]

Combined with the graph inclusion this proves (7.2). QED.

**Method consequence.** The source's infinite compatible planar grid does **not** automatically force complexity on both sides of the three-dimensional hull. For the canonical noncoplanar lift, the entire upper boundary is the single quadratic semialgebraic graph `z=st`. Any nonsemialgebraicity for this four-point candidate must occur on the **lower** boundary.

### Move 23 — assume the expected negative answer is wrong: explicit finite semialgebraic lower separators

To test the opposite of the source's expectation, look for a finite semialgebraic formula for the lower boundary rather than presuming that the infinite grid survives.

If `q(s,t)` is `D_2`-convex and satisfies the four corner inequalities

\[
q(0,0),q(1,0),q(0,1)\le0,\qquad q(1,1)\le1,
\]

then `q(s,t)-z` is `D`-convex and is nonpositive on `K`. Hence every hull point satisfies

\[
z\ge q(s,t).
\tag{7.3}
\]

Three explicit such functions are

\[
q_0(s,t)=\max\{0,s+t-1\},
\tag{7.4}
\]

\[
q_1(s,t)=st-\alpha s(1-s),
\tag{7.5}
\]

and

\[
q_2(s,t)=st-\alpha^{-1}t(1-t).
\tag{7.6}
\]

`q_0` is globally convex, hence `D_2`-convex. For `q_1`,

\[
\nabla^2q_1=\begin{pmatrix}2\alpha&1\\1&0\end{pmatrix};
\]

its quadratic form is nonnegative on the first two allowed directions and vanishes on `(1,-alpha)`:

\[
(1,-\alpha)\nabla^2q_1(1,-\alpha)^T=0.
\]

For `q_2`,

\[
\nabla^2q_2=\begin{pmatrix}0&1\\1&2/\alpha\end{pmatrix},
\]

and likewise

\[
(1,-\alpha)\nabla^2q_2(1,-\alpha)^T=0,
\]

with nonnegative second derivatives on the coordinate directions. All three functions match the required corner data.

Therefore the exact hull obeys the explicit semialgebraic sandwich

\[
\boxed{
\max\{q_0,q_1,q_2\}(s,t)\le z\le st.
}
\tag{7.7}
\]

This does **not** prove equality on the lower side. It is deliberately an opposite-answer test. The next decisive question is whether the lower envelope is already the finite maximum in (7.7), or whether the infinite compatible grid creates genuinely new lower supporting pieces outside this finite family.

A useful refinement falls out for free. Every quadratic corner interpolant of the form

\[
q_{A,B}(s,t)=st-A s(1-s)-B t(1-t)
\]

is `D_2`-convex precisely under the elementary sufficient-and-necessary Hessian inequalities

\[
A\ge0,\qquad B\ge0,\qquad A+\alpha^2B\ge\alpha.
\]

At a fixed interior point, maximizing `q_{A,B}` over this cone is a two-variable linear program whose extreme optimizers are exactly `q_1` or `q_2`. Thus `max(q_1,q_2)` is already the strongest lower separator within this entire quadratic corner-interpolant family. Any strict improvement must be genuinely nonquadratic (or the piecewise-linear `q_0` contribution), which sharply localizes the remaining mechanism.

## 8. What moved mathematically, and why the frozen metric did not

The run produced two exact symbolic reductions and one explicit opposite-answer benchmark:

1. all noncoplanar vertical lifts of the source four-point irrational parallelogram are `D`-preserving-affinely equivalent;
2. the canonical noncoplanar lift has exact upper boundary `z=st`;
3. its lower boundary is trapped above an explicit finite semialgebraic maximum and below `st`, with the full quadratic corner-interpolant class optimized exactly.

These are useful because they show where the source's infinite-grid obstruction can and cannot live. But the frozen metric counts certified **distinct affine boundary patches of the same hull**. The quadratic upper graph is not counted as such a patch, and the lower functions above are separators, not yet proven attained boundary patches. Therefore honesty requires

\[
\boxed{\text{metric: UNMEASURED -> UNMEASURED}.}
\]

No finite simulation or incomplete grid was promoted to an almost-everywhere/infinite conclusion.

## 9. Second-audit duty C30

C29's directed duty is C29 -> C30. The newest C30 mathematical package visible in this run is still the order-nine Sidorenko finite-host certificate already independently audited by C29 as

`C29-AUDIT-C30-SIDORENKO-N9-02 = PASS`.

I found no newer C30 theorem-sized claim requiring a fresh audit. Under the 90-percent new-methods rule I did not duplicate the same audit merely to generate an artifact.

## 10. No checker this run, intentionally

The new claims above are symbolic propositions whose complete proofs are written on the page. There is no finite enumeration or arithmetic threshold whose correctness would be strengthened by an exact checker. Writing one would violate the instruction to let code test an idea rather than manufacture activity. The existing MUB finite checkers remain archived in the reserve root.

## 11. Next research obligation

Do not count more grid fragments until the attainment mechanism is understood. The next attack should stay on the normalized noncoplanar lift and answer one falsifiable question:

\[
\text{Is the exact lower boundary }\ell_\alpha(s,t)=\max\{q_0,q_1,q_2\}(s,t)\text{?}
\tag{11.1}
\]

A proof would refute the **specific four-point candidate mechanism** by giving a finite semialgebraic hull, without refuting Conjecture 34 in general. A disproof should produce the first rigorously attained lower boundary patch not generated by these three separators; only then does the frozen affine-patch metric become measured.

The natural tools for that next run are the laminate/Jensen dual language from Meroni–Raita and the continued-fraction dynamics of the irrational compatible grid. No code should precede a proof-level recurrence or a finite exact candidate worth certifying.

## 12. `ledger_delta` for P26 only

P26 remains the shared-root-ledger writer. C29 did not edit `RESULTS.md`, `POSTED.md`, or another track.

Requested reconciliation:

- old C29 / I0097 MUB: move operationally to **HARD RESERVE**, preserving metric `0` as the full-domain global lower bound and preserving `11/756` as an upper benchmark only; no mathematical closure claimed;
- proposed I0077 Brownian: **EXCLUDED FROM C29 — canonical owner R07**, no C29 metric instantiated;
- active C29 fallback: `RS-2026-DC34`, Chiara Meroni (2026), Randomstrasse Conjecture 34; status **CLAIMED / PENDING_ADMISSION / PARTIAL exploratory**, not READY;
- frozen fallback metric: largest certified number `N` of pairwise distinct affine boundary patches of one fixed normalized lifted irrational-parallelogram `D`-convex hull; `UNMEASURED -> UNMEASURED`; unchanged count for this newly frozen fallback: `1`;
- exact evidence this run: on-page proofs `C29-DC34-NORMAL-01`, `C29-DC34-UPPER-02`, and lower separator sandwich (7.7); no finite checker applicable;
- ownership evidence: canonical claim creation/readback commit `9db0023b2471fa9855a780e8fe7b9b37ea147c70`;
- audit state: C29->C30 order-nine finite Sidorenko audit already PASS; no duplicate audit this run.

## 13. Source/status query record and limitations

Dated 2026-09-16 searches included:

- exact `Forward Brownian Motion`, `Problem 7.8`, `other space-time shapes`, Burdzy, Scheutzow, and later-citation terms;
- exact Randomstrasse `Directional Convexity`, `Conjecture 34`, `non-semialgebraic D-convex hull`;
- Meroni–Raita title and arXiv:2509.07541, later-author/citing terms;
- repository exact IDs I0077, I0035, RS-2026-DC34, current claims, queue admissions, and neighboring reports.

A failed bounded web search is not proof of openness. The claim remains PENDING_ADMISSION for that reason. The source itself and its August 2026 follow-up still state the directional-convexity obstruction as open, which is positive current-status evidence but not a universal bibliographic certificate.

End of immutable run report.

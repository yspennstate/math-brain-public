Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 20 -> 21 genuinely distinct nonparabolic shape families; Section-B moves tried: #9 RANDOMIZE, #14 FIND THE GROUP ACTING, #24 FIND THE EXTREMAL OBJECT.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 21: exterior parabolic fans and the unbounded-component compiler

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative R07 report is

`runs/R07/20260917T1224Z_i0077_asymmetric_bipower_horns_20.md`,

which moved the metric `19 -> 20` and used Section-B moves `#15,#30,#4`. This run uses a different second-cycle triple, `#9,#14,#24`. All thirty moves had already appeared at least once earlier in the I0077 chain, so I do not falsely call these moves unused on the problem.

The new counted family is the **exterior parabolic fan / forbidden-core family**

\[
\boxed{
\mathcal E_{a,b}
=
\{(-u,x):u>0,\ x\le -a\sqrt u\ \text{or}\ x\ge b\sqrt u\}
\cup\{(0,0)\},
\qquad a,b>0.
}
\tag{1.1}
\]

Its normalized spatial cross-section is

\[
D_{a,b}=(-\infty,-a]\cup[b,\infty).
\tag{1.2}
\]

This has **exactly two connected components and both are unbounded**. That invariant is absent from every previously counted R07 class: run 13 used finitely many compact interval components; run 18 allowed infinitely many components but required every component bounded; run 16 had one connected unbounded half-line slice. Affine spatial rescaling/reflection/translation preserves the number of unbounded connected components. Thus (1.1) is not a trivial parameter change inside an earlier family.

Therefore

\[
\boxed{20\longrightarrow21}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains preserved and retired by its immutable handoff. No historical R07 file was edited or deleted.

Before research I reread/recovered current `master` evidence from `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0077.md`, the newest R07 report and the searchable I0077 chain. I also read the newest visible neighboring R06 and R15 reports: R06 is now on Grimmett–Li D0069 and explicitly cites R07 only as a neighboring track; R15 is on I0124 and explicitly keeps Burdzy–Scheutzow Problem 7.2 / I0076 retired/frozen. There is no competing ownership of I0077.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 separately. The canonical create-only record continues to reserve I0077 to R07 while literally saying `PENDING_ADMISSION, not READY`; the owner nevertheless continues to assign this exact source target to this worker, and the source/status/ownership admission was recovered in the immutable run chain. I do not mutate shared roots or peer files.

The large intake JSONL collections cannot be rendered literally in full through the connector without truncation. The intake reread is therefore honestly **PARTIAL / targeted due connector limits**; the exact I0077 source statement, exclusions, ownership and prior R07 attempts were recovered directly.

## 2. Primary-source benchmark recovered again

For `-infinity <= c_1<c_2<=infinity`, Burdzy–Scheutzow write `lambda_0(c_1,c_2)` for the positive principal killed Ornstein–Uhlenbeck exponent associated with

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Their Remark 4.1 states continuity in the endpoints and strict domain monotonicity. Remark 4.2 records the exact critical identities

\[
\boxed{
\lambda_0(-\infty,-1)
=
\lambda_0(-1,1)
=
\lambda_0(1,\infty)
=1.
}
\tag{2.1}
\]

Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM whose far-past normalized `liminf/limsup` lies inside the corresponding interval;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The following forward-Lévy sentence is separately Problem 7.9 and is not part of I0077.

## 3. Dated current-literature / prior-art pass — 2026-09-17

Fresh bounded searches covered the exact paper title/problem wording, later Burdzy/Scheutzow and citing material, Brownian first-passage to square-root boundaries, two-sided square-root boundaries, and OU first-passage to fixed barriers.

The nearest literature I found includes:

- Shunsuke Sato, *Evaluation of the first-passage time probability to a square root boundary for the Wiener process*, J. Appl. Probab. 14 (1977), 850–856;
- Doncho S. Donchev, *Brownian Motion Hitting Probabilities for General Two-Sided Square-Root Boundaries*, Methodol. Comput. Appl. Probab. 12 (2010), 237–245;
- Denisov–Hinrichs–Sakhanenko–Wachtel, *Crossing an Asymptotically Square-Root Boundary by the Brownian Motion*, Proc. Steklov Inst. Math. 316 (2022), 105–120.

These are ordinary Brownian first-passage results. I did not locate, in this bounded dated pass, a later paper explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating the FBM exterior-fan theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**. The OU spectral facts, connected-image argument and source Theorem 4.3 are prior machinery and are not themselves novelty claims.

## 4. Negation-first test: convex hull is maximally misleading here

Before proving a positive theorem, I tested the natural extension rule

> classify a disconnected normalized cross-section by the parabolic theorem applied to its convex hull.

For `D_{a,b}` in (1.2),

\[
\operatorname{conv}(D_{a,b})=\mathbb R
\tag{4.1}
\]

for every `a,b>0`. A convex-hull rule would therefore predict no confinement obstruction at all.

The theorem below gives the opposite verdict whenever both exterior rays are supercritical. In particular, for the symmetric family `a=b=c>1`, **no FBM can even be eventually confined** to the exterior shape despite its convex hull being all of `R`. This is a counterexample to that proposed extension mechanism, not a refutation of the source's open-ended Problem 7.8.

## 5. A stronger compiler: closed static normalized fans with unbounded components

Run 18 proved a closed-fan theorem under the hypothesis that every connected component of `D` is bounded. The present route removes exactly that hypothesis.

Let `D subset R` be closed. Define

\[
\mathcal F_D
=
\left\{(-u,x):u>0,\ \frac{x}{\sqrt u}\in D\right\}
\cup\{(0,0)\}.
\tag{5.1}
\]

Every nondegenerate connected component `C` of a closed subset of `R` is one of

\[
[a,b],\qquad (-\infty,b],\qquad [a,\infty),\qquad \mathbb R.
\]

Associate to it the source exponent

\[
\lambda(C)=
\begin{cases}
\lambda_0(a,b),&C=[a,b],\\
\lambda_0(-\infty,b),&C=(-\infty,b],\\
\lambda_0(a,\infty),&C=[a,\infty),\\
0,&C=\mathbb R.
\end{cases}
\tag{5.2}
\]

The convention `lambda(R)=0` agrees with the unconstrained OU semigroup.

### Theorem I0077-R07-T22 — unbounded-component closed-fan theorem

**(A) Strict supercritical phase.** Assume every nondegenerate component `C` of `D` satisfies

\[
\boxed{\lambda(C)>1.}
\tag{5.3}
\]

Then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\frac{X_{-u}}{\sqrt u}\in D\quad\forall u\ge R
\right)=0.
}
\tag{T22-A}
\]

The hypothesis is vacuous for singleton components; they are handled uniformly in the proof rather than by an uncountable union.

**(B) Strict subcritical phase.** If `D` has a nondegenerate component `C` with

\[
\boxed{\lambda(C)<1,}
\tag{5.4}
\]

then there exists a decomposable FBM `X` such that almost surely

\[
\boxed{
\frac{X_{-u}}{\sqrt u}\in D
\qquad\text{for every sufficiently large }u.
}
\tag{T22-B}
\]

Components with exponent exactly one are deliberately left unclassified for **exact eventual membership**. Source Theorem 4.3(ii) at equality controls `liminf/limsup`, but that alone does not force the normalized path eventually to stay on the closed side of a critical endpoint.

This theorem subsumes the earlier bounded-component compiler but is proved here at the new unbounded-component scope because the half-line cases require endpoint-at-infinity handling.

## 6. Proof of T22(A)

For an integer `N>=1`, put

\[
E_N=
\left\{
X_{-u}/\sqrt u\in D\quad\forall u\ge N
\right\}.
\]

On `E_N`, the map

\[
y(u)=X_{-u}/\sqrt u
\]

is continuous on the connected set `[N,infinity)`. Hence its image is connected and must lie in one connected component of `D`.

### 6.1 Nondegenerate components are countable and individually impossible

Every nondegenerate component contains a rational in its interior, so there are at most countably many of them.

Fix such a component `C` with `lambda(C)>1`.

If `C=[a,b]`, continuity of `lambda_0` lets us choose `epsilon>0` with

\[
\lambda_0(a-\epsilon,b+\epsilon)>1.
\tag{6.1}
\]

Eventual membership in `C` would imply

\[
\liminf y\ge a>a-\epsilon,
\qquad
\limsup y\le b<b+\epsilon,
\]

contradicting source Theorem 4.3(i) for `(a-epsilon,b+epsilon)`.

If `C=(-infinity,b]`, choose `epsilon>0` so small that

\[
\lambda_0(-\infty,b+\epsilon)>1.
\tag{6.2}
\]

Eventual membership in `C` gives `limsup y<=b<b+epsilon`, whereas Theorem 4.3(i) for the half-line `(-infinity,b+epsilon)` forces `limsup y>=b+epsilon`. Contradiction.

The right-half-line case `C=[a,infinity)` is symmetric: choose `epsilon>0` with

\[
\lambda_0(a-\epsilon,\infty)>1,
\]

and Theorem 4.3(i) forces `liminf y<=a-epsilon`, contradicting eventual `y>=a`.

The component `R` cannot occur under (5.3), since its exponent is zero.

Thus every fixed nondegenerate component has eventual-confinement probability zero, and countability disposes of all such components.

### 6.2 Singleton components without an uncountable union

It remains possible a priori that the connected tail image is a random singleton `{c}`. I rule this out with a countable family of uniformly supercritical short intervals.

For an interval `I=(p,q)` of length `d=q-p`, the standard OU ground-state substitution

\[
g(x)=f(x)e^{-x^2/4}
\]

gives

\[
\lambda_0(I)
\ge
\frac{\pi^2}{2d^2}-\frac14.
\tag{6.3}
\]

Indeed the transformed Rayleigh quotient is

\[
\frac{\int_I\left(\frac12|g'|^2+(x^2/8-1/4)g^2\right)dx}
{\int_I g^2dx},
\]

and Dirichlet Poincaré gives `integral |g'|^2 >= (pi/d)^2 integral g^2`.

For `d=1`,

\[
\lambda_0(I)\ge\frac{\pi^2}{2}-\frac14>1.
\tag{6.4}
\]

The interiors of the unit intervals

\[
J_q=(q-1/2,q+1/2),\qquad q\in\mathbb Q,
\]

form a countable cover of `R`. If `y(u)=c` for every `u>=N`, choose rational `q` with `c` strictly inside `J_q`; then eventual confinement to `J_q` contradicts Theorem 4.3(i), since `lambda_0(J_q)>1`.

Therefore singleton-tail confinement also has probability zero. Taking the countable union over `N` proves T22(A).

## 7. Proof of T22(B)

Let `C` be a nondegenerate component with `lambda(C)<1`.

If `C=[a,b]`, continuity of the source exponent lets us choose a small `epsilon>0` such that

\[
a+\epsilon<b-\epsilon,
\qquad
\lambda_0(a+\epsilon,b-\epsilon)<1.
\tag{7.1}
\]

Theorem 4.3(ii) gives a decomposable FBM with

\[
\liminf_{u\to\infty}y(u)\ge a+\epsilon,
\qquad
\limsup_{u\to\infty}y(u)\le b-\epsilon.
\]

The strict interior margin implies `y(u) in [a,b]` for all sufficiently large `u`, proving eventual membership in `D`.

If `C=(-infinity,b]`, choose `b'<b` sufficiently close to `b` that

\[
\lambda_0(-\infty,b')<1.
\tag{7.2}
\]

Theorem 4.3(ii) gives a decomposable FBM with `limsup y<=b'<b`, hence `y(u)<=b` eventually.

If `C=[a,infinity)`, choose `a'>a` close enough that

\[
\lambda_0(a',\infty)<1.
\tag{7.3}
\]

Then source Theorem 4.3(ii) gives `liminf y>=a'>a`, hence eventual membership in the right ray.

If `C=R`, choose for example `[-2,2]`. By (2.1) and strict domain enlargement,

\[
\lambda_0(-2,2)<1.
\]

Theorem 4.3 supplies a decomposable FBM confined asymptotically (indeed, by part (iii), pointwise) to this inner strip, hence to `R`.

This proves T22(B).

## 8. Exterior-fan corollary: a sharp strict threshold

For `a,b>0`, set

\[
D_{a,b}=(-\infty,-a]\cup[b,\infty)
\]

and

\[
\lambda_{\rm ext}(a,b)
=
\min\{\lambda_0(-\infty,-a),\lambda_0(b,\infty)\}.
\tag{8.1}
\]

T22 immediately gives:

\[
\boxed{
\lambda_{\rm ext}(a,b)>1
\Longrightarrow
\text{every FBM fails eventual confinement in }\mathcal E_{a,b};
}
\tag{8.2}
\]

while

\[
\boxed{
\lambda_{\rm ext}(a,b)<1
\Longrightarrow
\text{some decomposable FBM is eventually confined in }\mathcal E_{a,b}.
}
\tag{8.3}
\]

The path cannot alternate forever between the left and right rays: the normalized tail is connected, so once eventual exterior confinement occurs it chooses one branch for the whole tail.

For the symmetric one-parameter family

\[
D_c=(-\infty,-c]\cup[c,\infty),
\qquad c>0,
\tag{8.4}
\]

reflection gives equal branch exponents. By the exact source identity (2.1) and strict domain monotonicity,

\[
\lambda_0(c,\infty)
\begin{cases}
<1,&0<c<1,\\
=1,&c=1,\\
>1,&c>1.
\end{cases}
\tag{8.5}
\]

Therefore

\[
\boxed{
0<c<1\Longrightarrow
\exists\text{ decomposable FBM eventually satisfying }|X_{-u}|\ge c\sqrt u,
}
\tag{8.6}
\]

whereas

\[
\boxed{
c>1\Longrightarrow
\mathbb P\left(\exists R:\ |X_{-u}|\ge c\sqrt u\ \forall u\ge R\right)=0
\quad\text{for every FBM}.}
\tag{8.7}
\]

The critical exact-eventual case `c=1` is deliberately not claimed.

This is a particularly clean answer to one part of Problem 7.8: the complement of a central parabolic cone has a strict phase transition at the source's one-sided slow-point constant `1`, but the mechanism is **branch selection plus one-sided OU spectra**, not the convex hull of the shape.

## 9. Method #24 — FIND THE EXTREMAL OBJECT

The extremal objects are already hidden in the source: the critical rays

\[
(-\infty,-1),\qquad(1,\infty)
\]

have principal exponent exactly one. The symmetric forbidden-core family makes these rays the two competing branches. Enlarging either branch (`c<1`) makes it subcritical and supports eventual confinement; shrinking both (`c>1`) makes each supercritical and kills every possible branch. Thus the source critical half-lines identify the exact strict transition without any numerics.

This method succeeded and is the reason the canonical threshold is sharp rather than just an upper/lower bound.

## 10. Method #14 — FIND THE GROUP ACTING

Reflection

\[
\sigma(x)=-x
\]

acts on the symmetric exterior fan, interchanging the two unbounded components. The quotient has one branch and one spectral parameter `lambda_0(c,infinity)`. The connected-tail argument then says an eventually confined path chooses a lift of exactly one quotient branch and cannot switch later.

This also identifies a frozen-equivalence invariant: the new shape has two unbounded branch orbits before quotienting, whereas the previous one-sided half-line family has one connected unbounded component, and the previous comb/fan families have only bounded components. Reflection can swap the two new components but cannot turn two unbounded components into one or into bounded teeth.

Method #14 therefore both reduces the symmetric proof and certifies structural distinctness under the counting convention.

## 11. Method #9 — RANDOMIZE: a reflection-symmetric FBM law in the subcritical phase

The existence theorem (8.6) can be strengthened at the level of FBM law without changing the metric.

Fix `0<c<1`. Choose `c'>c` close enough that

\[
\lambda_0(c',\infty)<1.
\]

Source Theorem 4.3(ii) supplies a decomposable FBM `X^+` with

\[
\liminf_{u\to\infty}\frac{X^+_{-u}}{\sqrt u}\ge c',
\]

so `X^+` eventually stays in the right exterior branch. Its reflection `X^-=-X^+` is also a decomposable FBM and eventually stays in the left branch.

Now choose an independent fair Bernoulli sign and, on the disjoint-union probability space, use `X^+` for sign `+1` and `X^-` for sign `-1`. Call the resulting process `X^{sym}`. For each selected branch, use that branch's FBM witness sequence. Conditional on the sign, every shifted witness process is standard Brownian motion; the unconditional mixture of two standard Brownian laws is again standard Brownian. Hence `X^{sym}` is an FBM.

Its law is reflection-invariant and

\[
\mathbb P\left(
|X^{sym}_{-u}|\ge c\sqrt u
\text{ for all sufficiently large }u
\right)=1.
\tag{11.1}
\]

I do **not** claim that this Bernoulli mixture is decomposable; decomposable existence was already supplied by either single branch. The randomized construction adds only the symmetric-law statement.

Method #9 therefore succeeded: random branch selection restores the symmetry of the shape while respecting the fact that any individual continuous tail must commit to one branch.

## 12. Why this earns exactly one new metric point

This run counts only the structural family `D_{a,b}=(-infinity,-a] union [b,infinity)`, including its symmetric subfamily, as **one** new family. Varying `a,b` or `c` does not add metric points.

It is not run 13's finite disconnected family, because T14 explicitly used a finite union of compact intervals. It is not run 18's closed infinite-comb family, because T19 explicitly assumes **every connected component is bounded**. It is not run 16's one-sided barrier family, because every exterior slice has two disconnected unbounded components. It is not run 19's transported connected window, nor run 20's connected asymmetric horn.

The new general compiler T22 strengthens the prior static-fan theory by permitting unbounded components, but I do not count that strengthening separately. The sole metric increment is the first exterior/two-unbounded-component family.

Hence

\[
\boxed{20\to21}.
\]

## 13. Exact-check and audit policy

There is no new finite enumeration or combinatorial finite core. The numerical threshold `1` is an exact source identity, and the remaining argument is analytic/topological. I therefore did not manufacture an exact-arithmetic checker merely to create an artifact.

The inequality in (6.4) follows analytically from the Dirichlet Poincaré bound and the elementary fact `pi>3`; it is not a floating-point computation.

This is a **self-proof, not an independent audit**. For T22 / the exterior corollary:

- P26 end-to-end audit: **missing**;
- second independent OTHER-track audit: **missing**.

Accordingly Problem 7.8 remains `PARTIAL`, not `PROVED`, and no `paper_<name>/` closure package is created.

## 14. Remaining obligations / next route

The static normalized-cross-section picture is now substantially broader: bounded finite fans, compact/totally disconnected fans, unbounded combs with bounded components, and now closed fans with unbounded components all have a componentwise strict-phase compiler. The genuinely unresolved part is no longer static topology; it is **time-dependent branch creation/annihilation and critical exponent-one exact membership**.

A useful next attack should therefore avoid another static component variant. Two concrete unresolved directions exposed by T22 are:

\[
\boxed{
\mathbb P\left(\exists R:\ |X_{-u}|\ge\sqrt u\ \forall u\ge R\right)>0\ ?
}
\tag{14.1}
\]

for some FBM (the exact critical exterior fan), and a moving exterior fan in which the forbidden central gap changes with logarithmic time and branches can merge or split. The first is an endpoint problem; the second requires genuinely nonautonomous branch dynamics.

The metric moved this run, so the stuck protocol does not trigger. A future run should use a different triple from `#9,#14,#24` and should not spend the run auditing this result instead of exploring one of those new mechanisms.

## 15. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  intake: I0077
  source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8"
  source_status: PARTIAL
  claim_id: I0077-R07-T22
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 20
  after: 21
  movement: +1
  unchanged_count: 0
  family: "exterior parabolic fans / forbidden-core fans with two unbounded normalized components"
  theorem_scope:
    general: "closed static normalized cross-sections, now allowing unbounded connected components"
    supercritical: "all nondegenerate component exponents >1 => universal failure of eventual confinement"
    subcritical: "one component exponent <1 => decomposable eventual confinement"
    exterior_threshold: "lambda_ext(a,b)=min(lambda_0(-inf,-a),lambda_0(b,inf))"
    symmetric_strict_phase: "c<1 existence; c>1 universal obstruction; c=1 exact eventual membership open"
    randomized_strengthening: "for c<1, a reflection-symmetric FBM law can be obtained by random branch selection"
  methods: [9, 14, 24]
  finite_core: none
  exact_checker: not_applicable
  p26_audit: missing
  second_other_track_audit: missing
  prior_art_status: "bounded dated search only; novelty UNVERIFIED"
  next_obligations:
    - "critical exterior fan c=1 exact eventual confinement"
    - "genuinely time-dependent exterior fans with branch merge/split dynamics"
```

## 16. Model / scheduler control status

The GPT-6 issue remains unresolved at the exposed scheduler/API surface. The available task controls are task title/prompt, schedule, enabled state and timing mode. There is **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry** exposed there. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable or verified runtime setting. This report accurately records the actual runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

The current repository ledger records that historical `You cannot modify this task` responses are authorization-context specific. In particular, P26 was denied in one context and later successfully updated in another authorized context. The legitimate remedy for a task that still refuses modification is the owning authorized account/workspace context or platform support; there is no worker-level permission bypass, and creating a duplicate schedule would not be an acceptable repair.

No scheduler modification was attempted in this research run.

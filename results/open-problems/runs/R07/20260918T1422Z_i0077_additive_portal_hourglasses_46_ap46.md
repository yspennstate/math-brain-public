Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `45 -> 46` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9 is the separate forward-Lévy-process question and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 46: additive portal-hourglass cages

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative R07 report is

`runs/R07/20260918T1326Z_i0077_fractal_dimension_pinning_curtains_45_fd45.md`,

which moved `44 -> 45` and used methods `#17,#18,#30`. The present triple `#3,#8,#20` is different. The I0077 chain has already exhausted all thirty Section-B labels at least once; I therefore do not invent three never-before-used numbers. What is new here is the mathematical route and the triple relative to the immediately preceding run.

Before research I recovered/rechecked current state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and canonical reservation `operations/claims/I0077.md`;
- the newest own report and targeted earlier R07 reports most likely to collide with the present family: run 24 (geometric sampled gates), run 25 (additive alternating half-line fences), run 27 (geometric sampled spatial combs), run 35 (continuous-age finite-lag cages), and runs 44–45 (positive-measure and fractal temporal pinning curtains);
- the newest visible R15 state. R15 has long handed off distinct Burdzy--Scheutzow Problem 7.2 / I0076 and is now screening a separate successor, so there is no ownership collision;
- targeted intake/search evidence for `I0077`, the exact source wording, prior attempts, and the arXiv identifier.

The large `probability_1000_intake_*/problems.jsonl` mirrors remain too large for a literal all-row rendering through the connector. The intake reread is therefore honestly **targeted/partial due connector limits**: exact I0077 source/ownership/exclusion/history was recovered, but I do not claim a byte-for-byte reread of hundreds of unrelated rows.

`INDEX.md` and `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no exact Problem-7.8 closure. The canonical claim still says `PENDING_ADMISSION, not READY` and reserves I0077 provisionally to R07; I preserve that operational label rather than silently promoting it. The old R07 KPZ/FPP route remains preserved in immutable pre-I0077 reports and is not reopened or deleted.

Entering metric: **45**.  
Entering unchanged count: **0**.

## 2. Full primary-source benchmark recovered again

I reopened the primary PDF, including the definition page, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X={X_t:t in R}` admits random witness times `S_n -> -infinity` a.s. such that for each fixed witness index

\[
B^{(n)}(s):=X_{S_n+s}-X_{S_n},\qquad s\ge0,
\]

is standard Brownian motion. Definition 2.2 gives decomposable FBMs as concatenations of independent Brownian pieces stopped at a.s.-finite stopping times, with strongly decomposable meaning the pieces/stopping data are i.i.d.

For `-infinity <= c_1<c_2<=infinity`, Section 4 lets `lambda_0(c_1,c_2)` be the positive principal Dirichlet exponent associated with the Ornstein--Uhlenbeck generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Theorem 4.3 states exactly:

1. If `lambda_0(c_1,c_2)>=1` and `X` is an FBM, then with probability one
\[
\left\{\limsup_{t\to-\infty}\frac{X_t}{\sqrt{|t|}}\ge c_2\right\}
\cup
\left\{\liminf_{t\to-\infty}\frac{X_t}{\sqrt{|t|}}\le c_1\right\}
\]
occurs.
2. If `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM `X` such that with probability one
\[
\limsup_{t\to-\infty}\frac{X_t}{\sqrt{|t|}}\le c_2,
\qquad
\liminf_{t\to-\infty}\frac{X_t}{\sqrt{|t|}}\ge c_1.
\]
3. If `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM satisfying, almost surely,
\[
c_1\sqrt{|t|}\le X_t\le c_2\sqrt{|t|}\qquad\forall t\le0.
\]

Problem 7.8 is exactly the one-sentence question whether Theorem 4.3 can be generalized from parabolas to other space-time shapes. The next sentence is Problem 7.9 on forward Lévy processes and is not part of this track.

The theorem below supplies a complete universal-obstruction theorem for a new deterministic shape class; it does not classify all shapes, so source status remains PARTIAL.

## 3. Fresh current-literature / prior-art pass

Fresh bounded searches on 2026-09-18 included:

- exact `Forward Brownian Motion` / `Problem 7.8` / `other space-time shapes` searches and later/citing-paper variants;
- Brownian motion with periodic/discrete gates and moving boundaries;
- equally spaced Brownian sampling, bounded-increment persistence, and arithmetic-time constraints;
- nearby first-passage / sampled-Gaussian persistence literature.

The primary paper remains the identifiable source. Nearby literature includes classical discrete sampling/persistence for Gaussian processes and Brownian curved-boundary first passage, but I found no accessible later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the arithmetic-gate theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Independent Gaussian increments, reflection, and Brownian modulus estimates used below are classical and are not claimed new.

I also checked a superficially similar literature phrase, Brownian traces containing arithmetic progressions: that concerns arithmetic progressions in the *spatial trace* of higher-dimensional Brownian motion, not bounded values at equally spaced *times*, and is not the theorem below.

## 4. Negation first: can recurrent full-space portals rescue a narrow cage?

A natural optimistic extension of run 35 is:

> If a deterministic moving cage repeatedly opens all the way to the entire real line, those portals should allow the path to reset its position and evade a finite-lag obstruction.

I tried to make this work at one full-space portal every unit of backward age. It fails. The reason is subtle enough that run 35 does not itself see it: run 35 required a bounded finite-lag cross-diameter at **every sufficiently large age**, while a full-space portal makes that quantity infinite.

Nevertheless, if the cage has uniformly bounded cross-diameter at one arithmetic lattice of neck times, then a fixed Brownian witness must realize an arbitrarily long block of bounded ordinary increments. The random phase of the witness relative to the lattice is the only apparent loophole. The main new lemma below closes that loophole uniformly over all phases.

Thus the proposed “periodic full-space portals always rescue the cage” extension is false. This is a refutation of that proposed extension, **not** a refutation of the source's open-ended Problem 7.8.

## 5. Methods #3, #8, #20

### #3 — PROVE SOMETHING STRONGER

Rather than analyze one hourglass formula, I prove a compiler for arbitrary deterministic fibers whose cross-diameter is bounded only on a fixed arithmetic progression of ages. There is no restriction at all between those ages.

### #8 — GO THE OTHER WAY AND DISCRETIZE

The shape is deliberately sampled at additive physical times, not logarithmic/parabolic scales. A Brownian witness started at a random time sees the age lattice at an unknown phase `theta in [0,h)`. Discretizing that phase on a mesh of size `h N^{-3}` reduces the continuum of possible phases to `O(N^3)` deterministic Brownian increment blocks.

### #20 — FIND WHY THE ALGORITHM FAILS

The obvious construction algorithm is “use each full-space portal to reposition before the next narrow neck.” The exact failure is that continuous Brownian repositioning still has to cross every pair of consecutive necks. For any fixed phase, those neck-to-neck displacements are independent Gaussian increments; uniform phase discretization shows that searching over the continuum of possible witness phases contributes only a polynomial factor, while the bounded-increment probability decays exponentially.

All three routes therefore converge on the same new obstruction.

## 6. Brownian uniform-phase lemma

Fix `h>0` and `M<infinity`. For standard Brownian motion `B`, let

\[
H_N(h,M):=
\left\{\exists\theta\in[0,h):
|B_{\theta+(k+1)h}-B_{\theta+kh}|\le M
\quad k=0,\ldots,N-1
\right\}.
\tag{6.1}
\]

### Lemma 6.1

\[
\boxed{\mathbb P(H_N(h,M))\longrightarrow0\qquad(N\to\infty).}
\tag{6.2}
\]

### Proof

Set

\[
\delta_N=hN^{-3}
\]

and define the Brownian modulus event on `[0,(N+2)h]`

\[
\Omega_N:=\left\{
\sup_{\substack{0\le s,t\le(N+2)h\\|t-s|\le\delta_N}}
|B_t-B_s|\le\frac14
\right\}.
\tag{6.3}
\]

Cover `[0,(N+2)h]` by overlapping intervals of length `2\delta_N` starting at the mesh `j\delta_N`. If the modulus in (6.3) exceeds `1/4`, then on one such interval

\[
\sup_{0\le r\le2\delta_N}|B_{j\delta_N+r}-B_{j\delta_N}|>\frac18.
\]

There are at most `(N+3)N^3` such intervals. Reflection and the Gaussian Chernoff bound give

\[
\mathbb P(\Omega_N^c)
\le
4(N+3)N^3
\exp\!\left(-\frac{1}{256\delta_N}\right)
=
4(N+3)N^3
\exp\!\left(-\frac{N^3}{256h}\right).
\tag{6.4}
\]

Now mesh the unknown phase interval `[0,h]` with spacing `\delta_N`; there are at most `N^3+2` phase points. On `\Omega_N`, if (6.1) holds at some phase `theta`, choose a mesh point `q` with `|q-theta|<=\delta_N`. For every `k`,

\[
\begin{aligned}
&|B_{q+(k+1)h}-B_{q+kh}|\\
&\qquad\le
|B_{\theta+(k+1)h}-B_{\theta+kh}|\\
&\qquad\quad+
|B_{q+(k+1)h}-B_{\theta+(k+1)h}|+
|B_{q+kh}-B_{\theta+kh}|\\
&\qquad\le M+\frac12.
\end{aligned}
\tag{6.5}
\]

For each deterministic mesh phase `q`, the `N` increments in (6.5) are independent `N(0,h)`. Put

\[
\rho:=\mathbb P\left(|Z|\le\frac{M+1/2}{\sqrt h}\right),
\qquad Z\sim N(0,1).
\tag{6.6}
\]

Since `M<infinity`, `rho<1`. A union bound over the phase mesh therefore gives

\[
\boxed{
\mathbb P(H_N(h,M))
\le
4(N+3)N^3e^{-N^3/(256h)}+(N^3+2)\rho^N.
}
\tag{6.7}
\]

Both terms tend to zero, proving the lemma. `QED`

The point of the lemma is the quantifier order: it controls `there exists theta` before the FBM witness time is ever introduced.

## 7. I0077-R07-T57 — arithmetic-gate cross-diameter obstruction

Let `K(u) subset R`, `u>0`, be nonempty deterministic fibers. Fix

\[
h>0,\qquad \tau\in[0,h),\qquad n_0\in\mathbb N,\qquad M<\infty.
\]

Assume only that consecutive fibers on the arithmetic age lattice have uniformly bounded cross-diameter:

\[
\boxed{
\sup_{x\in K(\tau+nh),\,y\in K(\tau+(n-1)h)}|x-y|
\le M
\qquad\forall n\ge n_0.
}
\tag{7.1}
\]

There is **no restriction whatsoever** on `K(u)` at ages not of the form `tau+nh`; in particular those fibers may equal all of `R`.

### Theorem T57

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T57}
\]

### Proof

Suppose the displayed event has positive probability. By countable union over integer tail radii, choose a deterministic `R` so large that

\[
R\ge \tau+n_0h
\]

and

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability

\[
p:=\mathbb P(E_R)>0.
\tag{7.2}
\]

By Lemma 6.1 choose a deterministic integer `N` such that

\[
\mathbb P(H_N(h,M))<p/2.
\tag{7.3}
\]

Let `(S_j)` be an FBM witness sequence and put `U_j=-S_j`. Since `U_j->infinity` almost surely, choose one **deterministic witness index** `j` far enough left that

\[
\mathbb P\{U_j\ge R+(N+2)h\}>1-p/4.
\tag{7.4}
\]

Hence

\[
\mathbb P\left(E_R\cap\{U_j\ge R+(N+2)h\}\right)
\ge3p/4.
\tag{7.5}
\]

Fix an outcome in this intersection. Let `n` be the largest integer with

\[
\tau+nh\le U_j,
\]

and set

\[
\theta:=U_j-(\tau+nh)\in[0,h).
\tag{7.6}
\]

For `k=0,\ldots,N`, the arithmetic gate age

\[
u_k:=\tau+(n-k)h
\]

satisfies `u_k>=R`. The original time corresponding to this age is

\[
-u_k=S_j+\theta+kh.
\]

Event `E_R` therefore gives

\[
X_{S_j+\theta+kh}\in K(u_k),
\qquad k=0,\ldots,N.
\tag{7.7}
\]

Applying (7.1) to consecutive `u_k` gives

\[
|X_{S_j+\theta+(k+1)h}-X_{S_j+\theta+kh}|\le M,
\qquad k=0,\ldots,N-1.
\tag{7.8}
\]

For this **fixed deterministic witness index** `j`, Definition 2.1 says

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is unconditionally standard Brownian motion. Equation (7.8) says exactly that `B^{(j)}` belongs to `H_N(h,M)`. Thus the event in (7.5) is contained in `H_N(h,M)` for the standard Brownian witness, so

\[
3p/4
\le
\mathbb P(H_N(h,M))
<p/2,
\]

a contradiction. This proves T57. `QED`

### Dependence audit

No conditioning on `S_j` occurs. The phase `theta` is random and may depend arbitrarily on the Brownian witness path; Lemma 6.1 is uniform over **all** phases, so it absorbs that dependence before the fixed witness law is used.

## 8. Concrete family earning metric point 46: additive portal hourglasses

Set `h=1`, `tau=0`, and let

\[
g(u)=\sqrt{u+1}\,\sin\sqrt{u+1},\qquad u\ge0.
\tag{8.1}
\]

Writing `r=\sqrt{u+1}>=1`,

\[
g'(u)=\frac{\sin r}{2r}+\frac12\cos r,
\]

so

\[
\boxed{|g'(u)|\le1.}
\tag{8.2}
\]

Let

\[
d(u)=\operatorname{dist}(u,\mathbb Z)\in[0,1/2]
\]

and define the extended aperture

\[
a(u)=
\begin{cases}
(1-2d(u))^{-1},&d(u)<1/2,\\
+\infty,&d(u)=1/2.
\end{cases}
\tag{8.3}
\]

Define

\[
K_*(u)=
\begin{cases}
[g(u)-a(u),g(u)+a(u)],&a(u)<\infty,\\
\mathbb R,&a(u)=\infty.
\end{cases}
\tag{8.4}
\]

and the backward shape

\[
\mathcal H_*
=
\{(-u,x):u>0,\ x\in K_*(u)\}
\cup
(\{0\}\times[g(0)-1,g(0)+1]).
\tag{8.5}
\]

This is a closed deterministic space-time shape. Away from half-integers, closedness follows from continuity of `g` and `a`; at every half-integer the fiber is all of `R`, while `a(u)->infinity` on approach, so every finite convergent space-time sequence remains inside the limit fiber. The seam at time zero is included explicitly.

At every integer age `n`, the aperture is exactly one:

\[
K_*(n)=[g(n)-1,g(n)+1].
\]

Since `g` is 1-Lipschitz,

\[
\sup_{x\in K_*(n),\,y\in K_*(n-1)}|x-y|
\le |g(n)-g(n-1)|+2
\le3.
\tag{8.6}
\]

Hence T57 with `M=3` gives

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal H_*
\quad\forall u\ge R
\right)=0
}
\tag{T58}
\]

for every FBM.

The geometry is deliberately extreme: at every integer age the fiber is a bounded neck of width `2`; at every half-integer age the fiber is the **entire real line**; and the aperture blows up continuously as one approaches each portal. Thus a deterministic continuous path has enormous freedom to migrate between necks. The universal obstruction is not topological continuity, occupation measure, Hausdorff dimension, or a continuous cage width—it is the additive-lattice Brownian increment entropy captured by T57.

## 9. Frozen-equivalence audit: why this is a new family

This earns one metric point rather than recounting an old parameter.

1. **Versus run 35 / T36 (continuous finite-lag cages).** T36 assumes a bounded cross-diameter for one fixed lag at *every sufficiently large age*. `H_*` fails that hypothesis maximally: at every half-integer the fiber is `R`, so every such cross-diameter involving the portal is infinite. T57 only uses necks on an arithmetic lattice.

2. **Versus run 24 / T25 and run 27 / T28 (geometric sampled gates).** Those gates occur at `e^{kP}` and have only `Theta(log T)` samples up to physical age `T`; here there are `Theta(T)` necks. Brownian rescaling maps one additive lattice to another additive lattice and cannot change the asymptotic ratio `u_{n+1}/u_n -> 1` into a fixed ratio `>1`.

3. **Versus run 25 / T26 (additive alternating half-line fences).** T26 forces occasional displacement of order `sqrt n` across one unit interval when the sign switches. Here consecutive neck centers have displacement at most one; impossibility instead comes from the exponentially small probability of satisfying an arbitrarily long block of merely bounded Gaussian increments. Unbounded half-lines versus bounded neck intervals is also invariant under the frozen affine Brownian equivalences.

4. **Versus runs 44–45 (temporal pinning curtains).** The integer gate set has Lebesgue measure zero and Hausdorff dimension zero. Hence the positive-occupation theorem and the Kaufman image-dimension theorem are both silent. The current obstruction is truly discrete in physical time.

5. **Not a trivial rescaling.** Constant time-space Brownian rescaling changes the additive period and widths but preserves “arithmetic lattice of bounded necks with full-space portals between them.” It cannot remove the portals, turn the gate set into a fractal/positive-measure set, or turn additive spacing into geometric spacing.

Thus metric `45 -> 46` is justified under the frozen convention.

## 10. Checker / audit status

There is no finite combinatorial or arithmetic core in T57/T58. The proof is analytic and written in full above, so I did **not** manufacture a checker merely to create an artifact.

The new claims T57/T58 currently have **0/2 independent OTHER-track audits**. This report is a self-check, not an independent audit. Therefore:

- theorem status: `PROVED_ON_PAGE_SELF_CHECKED`;
- source status: `PARTIAL`;
- publication novelty: `UNVERIFIED`;
- closure status: **not closed**.

No paper folder is created before the required two outside audits and a stronger prior-art review.

## 11. What actually moved, and next frontier

The fixed metric moved

\[
\boxed{45\longrightarrow46.}
\]

The new mechanism is a uniform-in-phase arithmetic-sampling lemma. It proves that full-space openings can be arbitrarily generous between gates and still fail to rescue an FBM if a positive-density arithmetic skeleton of consecutive fibers has bounded cross-diameter.

A genuinely new next frontier is to **thin the additive gate set below positive density**. Let gate ages be `u_n` with gaps `g_n=u_{n+1}-u_n -> infinity`. The relevant Brownian cost becomes

\[
p_n=\mathbb P\{|N(0,g_n)|\le M_n\},
\]

but the unknown witness phase and nonuniform gaps prevent the present finite phase mesh from applying verbatim. A sharp criterion should compare a product/sum such as

\[
\sum_n -\log p_n
\]

against the entropy of possible alignments. That could interpolate between the present additive-lattice theorem and the geometric-gate results without merely changing a parameter.

## 12. Model / scheduler / permission status

The model-control limitation is still present on the interface exposed to this worker. The available task controls are prompt/title, schedule or start-offset, enabled state, and timing mode. There is **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-model receipt**. Therefore `GPT-6 / maximum` remains prompt-only here, and this report correctly states the actual visible runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository's current operational ledger records that P26's historical `You cannot modify this task` failure was authorization-context-specific and that a later P26 prompt update succeeded from another authorized context. The legitimate remedy for any task that still rejects modification is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support. There is no legitimate worker-side permission bypass, and none was attempted.

To make the requested model setting enforceable rather than aspirational, the scheduler/platform would need either (i) persistent `model` and `reasoning_effort` fields exposed to the authorized scheduler API/UI, or (ii) an owning-workspace policy that pins those settings, plus authenticated runtime telemetry recording what model/reasoning level actually executed.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 45
  after: 46
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: "additive portal-hourglass cages with arithmetic bounded necks and recurrent full-space portals"
  theorem_general: I0077-R07-T57
  theorem_concrete: I0077-R07-T58
  theorem_status: PROVED_ON_PAGE_SELF_CHECKED
  source_status: PARTIAL
  admission_status: PENDING_ADMISSION_NOT_READY
  independent_audits: "0/2"
  finite_core: none
  checker: not_applicable
  novelty: UNVERIFIED
  methods: [3, 8, 20]
  previous_methods: [17, 18, 30]
  next_frontier: "nonuniform sparse additive gates and alignment entropy"
```

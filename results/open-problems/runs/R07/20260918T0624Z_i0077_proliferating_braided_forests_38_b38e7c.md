Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `37 -> 38` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 38: proliferating braided ribbon forests

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0524Z_i0077_braided_subdiffusive_ribbons_37.md`,

which moved the metric `36 -> 37` using moves `#2,#11,#30`. That report ended with exactly the obstruction attacked here: its crude growing-lane application would pay a difference-set cost of order `M_n^2 H_n`, hence a time scale `M_n^4 H_n^2`, and it explicitly suggested fixing the initial lane to try to remove one factor of `M_n`. This run does that and proves the stronger theorem.

All thirty Section-B moves have appeared somewhere earlier in the long I0077 chain, so I do not falsely claim three globally unused numbers. I use a different triple from the immediately preceding run and a genuinely new route.

Before research I rechecked current `master` state through:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the complete `runs/R07/` directory listing, the newest own report, code-search recovery of its stated growing-entropy obstruction, and selected structural predecessors including the infinite-comb theorem;
- newest neighboring R15 state. R15 has long since handed off distinct Burdzy–Scheutzow Problem 7.2 / I0076 and is on successor-admission work, so there is no I0077 ownership collision;
- targeted intake/attempt searches for `I0077`, arXiv `1302.6958`, `Problem 7.8`, and the exact source wording.

The very large intake JSONL mirrors cannot be rendered literally row-by-row through this connector without truncation, so the intake reread is honestly targeted rather than a byte-for-byte printout. Exact source, scope, ownership, posted exclusions, queue status, and previous R07 state were recovered. `INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no 7.8 closure. The canonical I0077 claim still says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of I0077 to R07. Shared roots are not edited by this worker.

The old R07 KPZ/FPP route remains preserved in its immutable pre-I0077 files and handoff. Nothing is deleted or reopened.

Entering metric: **37**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

The primary PDF was rechecked directly, including Definition 2.1, Definition 2.2, Remark 4.1, Remark 4.2, Theorem 4.3, and the open-problem page.

An FBM `X=(X_t)_{t in R}` has random witness times `S_r -> -infinity` almost surely such that, for every fixed deterministic witness index `r`,

\[
B^{(r)}(t)=X_{S_r+t}-X_{S_r},\qquad t\ge0,
\]

is standard Brownian motion. A decomposable FBM is a concatenation of independent stopped Brownian pieces.

For a parabolic interval `(c_1,c_2)`, the source writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent. Theorem 4.3 states:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal far-past obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, a decomposable FBM exists with the corresponding far-past liminf/limsup confinement;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, a decomposable FBM exists which lies in the exact parabolic strip for every negative time.

Remark 4.1 gives continuity and strict endpoint monotonicity of `lambda_0`, and Remark 4.2 records `lambda_0(-1,1)=1`. Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The following forward-Lévy sentence is Problem 7.9.

## 3. Fresh dated current-status / prior-art pass

A bounded fresh search on 2026-09-18 covered:

- exact title / arXiv ID with `Problem 7.8`, `Theorem 4.3`, and `other space-time shapes`;
- later/citing material around Burdzy–Scheutzow forward Brownian motion;
- Brownian motion in time-dependent domains and moving boundaries;
- Brownian sojourn inside two-sided moving boundaries;
- multiple / intermittent moving barriers and moving cones.

Relevant neighboring literature located includes Aurzada–Kramm on one-sided moving Brownian boundaries (arXiv:1203.4691), Seuret–Yang on Brownian sojourn inside moving boundaries (arXiv:1706.04519), J. M. Lee on first-passage density in time-dependent domains (arXiv:1811.05069), and Franceschi on space-time Brownian motion killed at a moving cone (arXiv:2404.16679). These concern ordinary Brownian motion, first passage, survival, or killed/reflected processes in prescribed moving domains. They do not state the forward-Brownian witness-time theorem below.

The exact-title/source search again surfaced the original paper and visible later citations, but I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the growing braided-ribbon theorem below. Searches for “FBM” were disambiguated because much of the literature uses that acronym for fractional Brownian motion rather than forward Brownian motion.

This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Gaussian density bounds, Brownian independent increments, and finite coverings are classical and are not claimed as new.

## 4. Refutation-first check: arbitrary proliferation is false

Before trying to prove a growing-branch obstruction, I tried to falsify the naive statement

> “If every time-slice is a finite union of bounded-width lanes, then eventual FBM confinement is impossible, regardless of how the number of lanes grows.”

That statement is false.

For `u>=1`, let

\[
K_{\mathrm{dense}}(u)
=
\bigcup_{|k|\le \lceil\sqrt u\rceil}[2k-1,2k+1].
\tag{4.1}
\]

The intervals touch, so

\[
K_{\mathrm{dense}}(u)
=
[-2\lceil\sqrt u\rceil-1,\,2\lceil\sqrt u\rceil+1]
\supset [-2\sqrt u,2\sqrt u].
\tag{4.2}
\]

The source has `lambda_0(-1,1)=1`, and strict domain monotonicity gives

\[
\lambda_0(-2,2)<1.
\]

Therefore Theorem 4.3(iii) supplies a decomposable FBM satisfying

\[
|X_{-u}|\le 2\sqrt u\qquad\forall u\ge0
\]

almost surely, and hence confined to `K_dense(u)` for all sufficiently large `u`.

Thus unit lane width and finite lane count at each time do **not** suffice. A source-valid obstruction has to compare branching complexity with the Brownian scale. This falsifies only the naive extension, not Problem 7.8.

This counterexample also shows that the exponent `M(u) ~ sqrt(u)` is a genuine scale at which a universal sparse-lane obstruction cannot hold without further geometry. It does not prove that the logarithmic factor in the sufficient theorem below is sharp.

## 5. Move #3 — PROVE SOMETHING STRONGER: let the number of lanes diverge

Run 37 treated a fixed finite number `m` of moving positive-width lanes. Its direct template-entropy compiler, if applied blindly to `M_n` possible lanes at scale `n`, forms all pairwise difference lanes and pays `M_n^2` in one-step target length. Making that target small compared with a Gaussian density then forces a time step of order `M_n^4 H_n^2`.

The stronger goal is to permit

\[
M_n\longrightarrow\infty
\]

while retaining a complete universal obstruction.

The crucial observation is that one need not union over **both** lane labels at every sampled time. On a confined FBM witness segment, the starting point `X_{S_r}` lies in one specific starting lane. Freeze that lane label as part of the deterministic template. There are only `M_n` choices for it, paid once in the template count. Thereafter each sampled slice needs only the `M_n` possible destination lanes.

That removes an entire factor of `M_n` from one-step target length and improves the natural time scale from

\[
M_n^4H_n^2
\quad\text{to}\quad
M_n^2H_n^2.
\tag{5.1}
\]

**Outcome #3: success.** The fixed-`m` theorem strengthens to unbounded branching complexity.

## 6. Move #13 — FIND WHAT ONLY INCREASES: age-dependent branch complexity

For the concrete family below, moving backward in physical time means increasing age `u=-t`. The number of active lanes is monotone nondecreasing with `u`: new corridors are born but old ones remain available. This supplies a scale monovariant

\[
M_n=\sup_{2^{n-1}\le u\le2^{n+1}}m(u),
\]

which controls every starting and destination lane that can appear during a witness segment whose age lies in the `n`th dyadic block.

The point is not that branch monotonicity itself proves impossibility—it does not, as the dense counterexample above shows—but that it converts the continuously changing geometry into one deterministic complexity budget per scale.

**Outcome #13: success as the correct complexity variable.**

## 7. Move #24 — FIND THE EXTREMAL OBJECT: worst one-step slice after freezing the initial lane

Fix a scale with at most `M` active lanes and half-width at most `H`. Once the starting lane is fixed, a Brownian witness value at a later sampled time can lie in a union of at most `M` intervals. After the age parameter is discretized, each interval can be inflated to half-width `4H`. Hence the worst possible Lebesgue measure of one template slice is

\[
\boxed{8MH.}
\tag{7.1}
\]

A Gaussian increment of variance `tau` has density at most `(2 pi tau)^(-1/2)`, so the worst one-step template probability is at most

\[
\frac{8MH}{\sqrt{2\pi\tau}}.
\]

Balancing this at a fixed constant below one selects

\[
\boxed{\tau\asymp M^2H^2,}
\tag{7.2}
\]

not `M^4H^2`. This is the extremal calculation that closes the argument.

**Outcome #24: success.** It identifies the right loss for the present method and nearly reaches the `sqrt(u)` proliferation scale exposed by the counterexample.

## 8. I0077-R07-T41 — growing-complexity braided ribbon theorem

Let `g_1,g_2,...:[0,infinity)->R` be deterministic globally Lipschitz functions with a common Lipschitz constant `L<infinity`. Let `m(u)` be a finite positive integer for every `u`, and let `h(u)>0`. Define the time-`u` fiber

\[
K(u)=\bigcup_{i=1}^{m(u)}[g_i(u)-h(u),\,g_i(u)+h(u)].
\tag{8.1}
\]

For every sufficiently large integer `n`, put

\[
M_n=\sup_{2^{n-1}\le u\le2^{n+1}}m(u),
\qquad
H_n=\sup_{2^{n-1}\le u\le2^{n+1}}h(u).
\tag{8.2}
\]

Assume `M_n,H_n<infinity`, `H_n>=1` eventually, and

\[
\boxed{
\frac{nM_n^2H_n^2}{2^n}\longrightarrow0.
}
\tag{8.3}
\]

### Theorem T41

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T41}
\]

The lanes may cross, merge, split, exchange order, be born as `u` grows, and their number may tend to infinity. No persistent lane label for the confined path is assumed.

### Proof

Assume the displayed event has positive probability. By a countable union over deterministic radii there is an integer `R` such that

\[
E_R=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p_0>0`.

For a large integer `n`, let

\[
I_n=[2^n,2^{n+1}),
\qquad
T_n=2^{n-2}.
\tag{8.4}
\]

Write

\[
L_*=\max(1,L),
\qquad
\delta_n=H_n/L_*.
\tag{8.5}
\]

Choose a deterministic grid `G_n` covering `I_n` with mesh at most `delta_n`. It can be chosen with

\[
|G_n|\le 2+\frac{L_*2^n}{H_n}.
\tag{8.6}
\]

Set

\[
\tau_n=64M_n^2H_n^2,
\qquad
N_n=\left\lfloor\frac{T_n}{\tau_n}\right\rfloor,
\qquad
t_{n,k}=k\tau_n,
\quad1\le k\le N_n.
\tag{8.7}
\]

Condition (8.3) implies

\[
\frac{N_n}{n}\longrightarrow\infty.
\tag{8.8}
\]

Indeed,

\[
N_n\ge
\frac{2^n}{256M_n^2H_n^2}-1.
\tag{8.9}
\]

For every grid age `v in G_n`, starting-lane label `1<=j<=M_n`, and sampled index `k`, define the deterministic template slice

\[
D_{n,k}^{v,j}
=
\bigcup_{i=1}^{M_n}
\left[
 g_i(v-t_{n,k})-g_j(v)-4H_n,\,
 g_i(v-t_{n,k})-g_j(v)+4H_n
\right].
\tag{8.10}
\]

Every such slice has Lebesgue measure at most

\[
|D_{n,k}^{v,j}|\le8M_nH_n.
\tag{8.11}
\]

Now let `U in I_n` be any age for which confinement holds at `U` and at all the sampled ages `U-t_{n,k}`. Choose a starting lane `j<=m(U)` satisfying

\[
|X_{-U}-g_j(U)|\le h(U),
\tag{8.12}
\]

and choose `v in G_n` with `|U-v|<=delta_n`. At sampled time `t_{n,k}`, choose any destination lane `i<=m(U-t_{n,k})` containing `X_{-(U-t_{n,k})}`. Since `t_{n,k}<=T_n`, all relevant ages lie in `[2^{n-1},2^{n+1}]`, so `i,j<=M_n` and both half-widths are at most `H_n`.

The difference from the grid template center obeys

\[
\begin{aligned}
&\left|
\bigl(X_{-(U-t_{n,k})}-X_{-U}\bigr)
-
\bigl(g_i(v-t_{n,k})-g_j(v)\bigr)
\right|\\
&\qquad\le
2H_n
+|g_i(U-t_{n,k})-g_i(v-t_{n,k})|
+|g_j(U)-g_j(v)|\\
&\qquad\le2H_n+2L\delta_n
\le4H_n.
\end{aligned}
\tag{8.13}
\]

Thus a confined witness segment of age `U` must hit one deterministic template `(v,j)` at every sampled time.

For fixed `(v,j)`, let `B` be standard Brownian motion. By the Markov property and the Gaussian density bound, whatever the past value is,

\[
\mathbb P\left(
B(t_{n,k})\in D_{n,k}^{v,j}
\mid\mathcal F_{t_{n,k-1}}
\right)
\le
\frac{8M_nH_n}{\sqrt{2\pi\tau_n}}
=
\frac1{\sqrt{2\pi}}
<\frac12.
\tag{8.14}
\]

Iterating gives

\[
\mathbb P\left(
B(t_{n,k})\in D_{n,k}^{v,j}
\ \forall1\le k\le N_n
\right)
\le2^{-N_n}.
\tag{8.15}
\]

The number of deterministic templates is at most

\[
J_n
\le
M_n\left(2+\frac{L_*2^n}{H_n}\right).
\tag{8.16}
\]

Because `H_n>=1` and (8.3) holds, eventually `M_n<=2^{n/2}`. Hence for a constant `C_L`,

\[
J_n\le C_L2^{3n/2}.
\tag{8.17}
\]

By (8.8), eventually `N_n>=4n`, and therefore

\[
\sum_n J_n2^{-N_n}
\le
\sum_n C_L2^{3n/2}2^{-4n}
<\infty.
\tag{8.18}
\]

Choose `n_0` so large that `2^{n_0-1}>=R` and the tail of (8.18) is less than `p_0/2`.

Let `S_r` be the FBM witness times. Since `-S_r -> infinity` almost surely, choose one **deterministic witness index** `r` with

\[
\mathbb P\{-S_r\ge2^{n_0}\}>1-p_0/4.
\tag{8.19}
\]

For this fixed index,

\[
B(t)=X_{S_r+t}-X_{S_r},\qquad t\ge0,
\]

is standard Brownian motion unconditionally. Thus

\[
\mathbb P(E_R\cap\{-S_r\ge2^{n_0}\})\ge3p_0/4.
\tag{8.20}
\]

On this event, let `U=-S_r` and take the unique `n>=n_0` with `U in I_n`. Since `t_{n,k}<=2^{n-2}`,

\[
U-t_{n,k}
\ge2^n-2^{n-2}
=3\cdot2^{n-2}
>2^{n-1}
\ge R,
\]

so confinement applies to every sampled age. By (8.13), the Brownian witness path lies in one of the path-only template events counted in (8.18). Their union over `n>=n_0` has probability less than `p_0/2`, contradicting (8.20).

No conditioning on the random witness time is used, and no independence between `S_r` and its Brownian witness path is assumed. This proves T41. QED.

## 9. Consequences and scale interpretation

Condition (8.3) can be read schematically as

\[
M_nH_n
=o\left(\sqrt{\frac{2^n}{n}}\right).
\tag{9.1}
\]

For bounded lane widths, the theorem therefore permits almost `sqrt(u)` many active lanes: for example any power law

\[
M(u)=O(u^\alpha),\qquad \alpha<\frac12,
\tag{9.2}
\]

is allowed. The refutation-first construction in Section 4 shows that `M(u)` of order `sqrt(u)` can already support a decomposable FBM if the lanes tile a sufficiently wide parabolic core. Thus T41 reaches the correct **power exponent** `1/2`; only a logarithmic-scale gap remains between this sufficient obstruction and that feasible example.

This does **not** claim a sharp logarithmic threshold. Closing that gap would require a better treatment of the continuously varying witness age than the present deterministic grid / union bound.

## 10. I0077-R07-T42 — a concrete proliferating braided forest

The new counted family is not merely a sequence of isolated corridors whose branch label is conserved. It repeatedly merges all branches and then separates them again, so a confined continuous path can switch lanes infinitely often.

Let

\[
f(u)=u\sin(\log(1+u)),\qquad u\ge0,
\tag{10.1}
\]

and for `i>=1` let

\[
c_i=1-\frac1i,
\qquad
g_i(u)=c_if(u).
\tag{10.2}
\]

Since

\[
f'(u)
=
\sin(\log(1+u))
+
\frac{u}{1+u}\cos(\log(1+u)),
\]

we have `|f'(u)|<2`, so all `g_i` have one common Lipschitz bound `L=2`.

For `u>=1`, set

\[
m(u)=\lfloor u^{2/5}\rfloor,
\qquad
K_*(u)=\bigcup_{i=1}^{m(u)}[g_i(u)-1,g_i(u)+1].
\tag{10.3}
\]

For `0<=u<=1`, take `K_*(u)=[-1,1]`. Equivalently, the `i`th lane is born at age `u=i^{5/2}` and remains thereafter. The resulting space-time shape is closed: it is a locally finite union on compact age intervals of closed ribbon pieces, together with the compact near-origin cap.

On the enlarged dyadic block,

\[
M_n
\le(2^{n+1})^{2/5}
=2^{2(n+1)/5},
\qquad H_n=1.
\]

Hence

\[
\frac{nM_n^2H_n^2}{2^n}
\le
2^{4/5}n2^{-n/5}
\longrightarrow0.
\tag{10.4}
\]

T41 therefore gives the complete universal statement

\[
\boxed{
\mathbb P\left(
\exists R:\ X_{-u}\in K_*(u)\ \forall u\ge R
\right)=0
}
\tag{T42}
\]

for every FBM `X`.

### Why this is a genuinely braided, proliferating family

At the infinitely many ages

\[
u_k=e^{k\pi}-1,
\]

we have `f(u_k)=0`, so **all active ribbons merge into exactly the same interval** `[-1,1]`. A continuous confined path can therefore change its lane identity at these merger times; no conserved tail branch label reduces T42 to the single-ribbon theorem.

At the alternating extremal ages

\[
v_k=e^{\pi/2+k\pi}-1,
\]

we have `|f(v_k)|=v_k`. Consecutive lane centers then satisfy

\[
|g_{i+1}(v_k)-g_i(v_k)|
=
\frac{v_k}{i(i+1)}.
\tag{10.5}
\]

For active `i+1<=m(v_k)`,

\[
i(i+1)\le m(v_k)^2\le v_k^{4/5},
\]

so

\[
|g_{i+1}(v_k)-g_i(v_k)|\ge v_k^{1/5}.
\tag{10.6}
\]

For large `k`, this is greater than `2`, and all unit-half-width ribbons are disjoint. Thus the number of connected fiber components at those ages is exactly

\[
m(v_k)=\lfloor v_k^{2/5}\rfloor\longrightarrow\infty.
\]

Moreover their convex hull has diameter of order `v_k`, since the first center is `0` and the highest active coefficient approaches `1`. So this geometry is not contained in a single subdiffusive connected ribbon.

The shape therefore oscillates infinitely often between one merged corridor and an unbounded number of macroscopically separated corridors. That repeated merge/split mechanism is precisely why the initial-label entropy argument, rather than branch conservation, is needed.

## 11. Frozen-equivalence comparison: why this earns metric point 38

This family is not counted as a parameter variant of run 37.

- **Run 37:** uniformly bounded finite number of lanes. Here the number of active lanes tends to infinity like `u^{2/5}`.
- **Run 18 infinite parabolic comb:** infinitely many components are already present in every positive-age fiber, at fixed normalized `sqrt(u)` geometry, and a continuous normalized path conserves one tooth. Here every finite-age fiber has only finitely many lanes, their number grows without bound, the convex hull is ballistic at separation phases, and all lanes merge infinitely often so the path may switch labels.
- **Runs 33–34 zero-width webs:** fibers are unions of curves with empty interior; the obstruction is finite variation / quadratic variation. Here every lane has positive width and the proof is a Gaussian path-space entropy estimate.
- **Runs 35–36 single widening ribbons:** fibers are connected and controlled by one moving center. Here the number of connected components itself diverges along an infinite sequence of ages and the convex hull can have order-`u` diameter.

Brownian rescaling, reflection, constant translation, or changing a numerical parameter cannot turn a uniformly finite braid or fixed infinite comb into a family whose finite slice component count diverges and whose components repeatedly all merge. Under the frozen equivalence convention this is a genuinely new shape class.

Therefore the metric is

\[
\boxed{37\longrightarrow38}.
\]

`unchanged_count = 0`.

## 12. Verification / closure status

There is no finite combinatorial core in T41/T42, so I did **not** manufacture an exact-arithmetic checker merely to create a certificate. The theorem is analytic and the full argument is written above. The elementary exponent and spacing calculations are symbolic on the page.

Independent OTHER-track audits for T41/T42: **0/2**. No audit is fabricated and no self-check is relabeled as independent.

Accordingly:

- `I0077-R07-T41`: **PROVED in this report, unaudited**;
- `I0077-R07-T42`: **PROVED in this report, unaudited**;
- Burdzy–Scheutzow Problem 7.8 overall: **PARTIAL**;
- publication novelty: **UNVERIFIED**;
- no closure paper package is created this run.

The source's open-ended request is not called solved merely because another explicit family has been handled.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: I0077
  target: Burdzy-Scheutzow Problem 7.8
  metric_name: distinct_nonparabolic_shape_families_with_complete_source_appropriate_theorem
  before: 37
  after: 38
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  status: PARTIAL
  new_theorems:
    - I0077-R07-T41
    - I0077-R07-T42
  new_family: proliferating_positive_width_braided_ribbon_forests
  finite_core: none
  exact_checker: not_applicable
  independent_other_track_audits: 0/2
  prior_art_status: bounded_negative_search_only_novelty_unverified
  next_obligation: close_the_logarithmic_gap_between_MH=o(sqrt(u/log_u))_obstruction_and_order_sqrt_u_feasible_tiling_or_find_counterexample
```

## 14. Strongest next route

The new theorem leaves a narrow and mathematically meaningful frontier. With bounded widths it proves universal impossibility when

\[
M(u)=o\left(\sqrt{u/\log u}\right)
\]

at dyadic scales, while Section 4 exhibits feasible tiled lane bundles with `M(u)` of order `sqrt(u)`. The remaining logarithmic gap comes from discretizing the unknown witness age by a deterministic grid and union-bounding over all age templates.

A next genuinely new route should therefore not add another ribbon example. It should attack the age-template entropy itself—for example by chaining / metric entropy in the witness-age parameter, or by a continuous Gaussian maximal inequality—to see whether the `sqrt(log u)` loss can be removed. That would turn the present power-sharp theorem into a near-exact branching-complexity threshold.

Candidate next Section-B moves (not executed as claims this run): #7 TAKE THE LIMIT, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #28 REPLACE FOR ALL WITH FOR TYPICAL.

## 15. Actual model / scheduler-control state

Actual runtime metadata available to this report identifies the model as **GPT-5.6 Sol**; the reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The scheduler-control surface exposed to this worker still offers title/prompt, schedule or start-offset, enablement, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus writing “GPT-6 / maximum” in prompt text does not enforce or verify that runtime.

The repository policy records historical `You cannot modify this task` responses for P26/P01/P03. Later fleet state records that P26 could be modified from a different authorized context, so the legitimate workaround is the owning/authorized account/workspace context or platform support—not permission bypass, duplicate schedules, or repository edits masquerading as scheduler changes.

Actually enforcing GPT-6 maximum would require the authorized product/backend/API surface to expose persistent model and reasoning fields and to return authenticated execution metadata. This R07 run was explicitly prohibited from scheduler changes, and none were attempted.

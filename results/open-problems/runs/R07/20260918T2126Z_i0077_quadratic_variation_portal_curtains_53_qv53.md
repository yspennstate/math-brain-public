Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `52 -> 53` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate.

# R07 CLOSABLE OUTSIDE — run 53: rough quadratic-variation gate curtains with full-space portals

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative own report is

`runs/R07/20260918T203357Z_i0077_nonlinear_null_packet_curtains_52_npc52.md`,

which moved `51 -> 52` and used moves `#3,#21,#27`. The present triple `#2,#11,#16` is different. All thirty Section-B labels have already appeared somewhere in the long I0077 history; I do not invent a false claim that these three numbers are globally unused. The research route itself is new.

Before new mathematics I recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling later owner directive `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report, the R07 directory/history, and targeted searches through all I0077 attempts for collision checks;
- the newest neighboring R15 report. R15 keeps distinct Burdzy–Scheutzow Problem 7.2 / I0076 retired and is screening an unrelated successor, so there is no I0077 ownership collision;
- targeted intake/source searches for `I0077`, the exact Problem-7.8 wording, arXiv:1302.6958, later resolutions, and nearby prior art.

The connector truncates the very large intake JSONL corpus and repository-wide searches, so I do not falsely claim a byte-for-byte rendering of every unrelated intake row. The exact I0077 source, ownership, exclusions, current fleet roots, newest neighboring state, and the complete searchable R07 family history needed for admission/collision checking were recovered.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no exact Problem-7.8 closure. `operations/claims/I0077.md` still says `PENDING_ADMISSION, not READY` while reserving the exact target to R07; I preserve that operational label. The old R07 KPZ route remains preserved by immutable handoff/history and is not reopened.

Entering metric: **52**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

The primary arXiv PDF was reopened and the relevant rendered pages were rechecked.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` a.s. such that, for each **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{2.1}
\]

is standard Brownian motion.

For `-infinity <= c_1<c_2<=infinity`, Theorem 4.3 is the source's three-part parabolic phase theorem:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal normalized far-past escape obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly: **“Can one generalize Theorem 4.3 from parabolas to other space-time shapes?”** The following sentence is separately Problem 7.9 about forward Lévy processes and is not part of I0077.

## 3. Fresh current-literature / prior-art pass

The dated bounded search covered:

- exact `"Problem 7.8" "Forward Brownian Motion"`, exact paper title/arXiv id, and the exact “other space-time shapes” wording;
- Burdzy/Scheutzow later/citing material and moving-boundary references;
- `Brownian quadratic variation shifted dyadic partitions` and pathwise quadratic-variation robustness;
- generalized Takagi / Takagi–Landsberg functions with pathwise quadratic variation;
- deterministic constructions with prescribed pathwise quadratic variation.

The exact-source search again recovered the original paper and publication pages, but no accessible later source in this bounded pass explicitly resolving exact Problem 7.8 or stating T71/T72 below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The pathwise-quadratic-variation mechanism is classical and is **not** claimed as new. Relevant prior art includes:

- Alexander Schied, *On a class of generalized Takagi functions with linear pathwise quadratic variation*, J. Math. Anal. Appl. 433 (2016), 974–990, arXiv:1501.00837;
- Yuliya Mishura and Alexander Schied, *Constructing functions with prescribed pathwise quadratic variation*, J. Math. Anal. Appl. 442 (2016), 117–137, arXiv:1511.04678;
- Rama Cont and Purba Das, *Quadratic variation and quadratic roughness* (published 2022), which studies partition robustness and shows typical Brownian paths satisfy an appropriate quadratic-roughness property.

Those papers make it especially important not to mistake “rough deterministic trace” for novelty. The candidate new contribution here is the **FBM/source-specific confinement theorem for repeated non-Brownian-QV gate templates with arbitrary geometry between the gates**.

## 4. Move #2 — attack the negation / old route first

Run 52 ended at the critical nonlinear-track frontier: its occupation/local-time argument needs a sufficiently regular deterministic drift family (locally Lipschitz there; the corrected Bass–Burdzy uniform curve theorem is above the `1/2` Hölder threshold).

I first tried to extend that route to a deterministic trace whose modulus is already at Brownian's Lévy scale. That route fails for the intended example below:

- the trace has infinite total variation;
- it is not `1/2`-Hölder;
- subtracting it from Brownian motion is not a continuous semimartingale by the simple finite-variation argument used in run 52;
- the shape will have two-dimensional open chambers away from the gates, so the run-39 global `dim_H<3/2` obstruction is silent;
- the run-40 finite `1/2`-Hölder-selector lemma is also silent.

A second tempting proposed extension is “any sufficiently Brownian-looking deterministic rough template should be excluded just by roughness.” That is not a usable theorem: Schied's generalized Takagi class contains deterministic paths with **linear pathwise quadratic variation**, including Brownian-like QV rates. Thus vague roughness is not the invariant.

This failed extension is not a refutation of Problem 7.8. It identifies the quantity to test next.

**Outcome #2:** the previous local-time/regularity routes genuinely stop at this example, so the run changes invariant rather than manufacturing another lemma on run 52.

## 5. Move #11 — dualize containment into a path-energy identity

For a continuous path `f` on an interval and the level-`N` dyadic partition, define the discrete quadratic energy

\[
V_N(f):=
\sum_{k=0}^{2^N-1}
\left(
 f((k+1)2^{-N})-f(k2^{-N})
\right)^2.
\tag{5.1}
\]

If a Brownian witness segment is **exactly equal**, up to spatial translation and time reversal, to a deterministic gate template `Q`, then every one of these finite energies must agree. Brownian motion has limiting unit quadratic variation, while I will choose `Q` with `V_N(Q)->infinity`.

The random FBM witness phase is the only subtlety: the gate block begins at an absolute deterministic time, but in witness coordinates its start is a random shift. Hence the required Brownian fact must hold **simultaneously for every shift**, not merely for each deterministic shift separately.

That simultaneous statement is Lemma 6.1 below.

**Outcome #11:** success. The hard random-phase issue is moved into a uniform shifted-partition quadratic-variation lemma that can be proved directly.

## 6. Brownian lemma — dyadic quadratic variation uniformly over every translate

For standard Brownian motion `B`, put `h_N=2^{-N}` and

\[
V_N^B(\theta)
:=
\sum_{k=0}^{2^N-1}
\left(
B_{\theta+(k+1)h_N}-B_{\theta+kh_N}
\right)^2,
\qquad \theta\ge0.
\tag{6.1}
\]

### Lemma 6.1

Almost surely, for every finite `A`,

\[
\boxed{
\sup_{0\le\theta\le A}|V_N^B(\theta)-1|\longrightarrow0.
}
\tag{6.2}
\]

Consequently there is one probability-one event on which

\[
V_N^B(\theta)\to1
\qquad\text{for every }\theta\ge0
\tag{6.3}
\]

simultaneously, including path-dependent random `theta`.

### Proof

Fix `A`. Let

\[
\delta_N=2^{-4N}
\]

and let `G_N` be the `delta_N`-mesh of `[0,A]`.

For a fixed `r in G_N`, the `2^N` increments in (6.1) are independent `N(0,h_N)`, hence

\[
V_N^B(r)\stackrel d=
2^{-N}\chi^2_{2^N}.
\tag{6.4}
\]

A standard chi-square Chernoff bound gives, for large `N`,

\[
\Pr\left(|V_N^B(r)-1|>N^{-1}\right)
\le 2\exp\left(-c\frac{2^N}{N^2}\right)
\tag{6.5}
\]

for an absolute `c>0`. Since `|G_N|=O_A(2^{4N})`, the union bound is summable in `N`. Borel–Cantelli therefore gives

\[
\max_{r\in G_N}|V_N^B(r)-1|\to0
\quad\text{a.s.}
\tag{6.6}
\]

It remains to move a mesh phase to an arbitrary phase. Let

\[
\omega_N=
\sup\{|B_t-B_s|:
0\le s,t\le A+2,\ |t-s|\le\delta_N\}.
\tag{6.7}
\]

Cover `[0,A+2]` by `O_A(delta_N^{-1})` intervals of length `2 delta_N`. Reflection plus the Gaussian tail gives

\[
\Pr\{\omega_N> C N\sqrt{\delta_N}\}
\le C_A2^{4N}e^{-cN^2}
\tag{6.8}
\]

for suitable fixed positive constants, hence the right-hand side is summable. Thus almost surely, eventually,

\[
\omega_N=O_A(N2^{-2N}).
\tag{6.9}
\]

For arbitrary `theta in [0,A]`, choose `r in G_N` with `|theta-r|<=delta_N`. Let `x_k` and `y_k` be the corresponding Brownian increments in (6.1) at phases `theta` and `r`. Then

\[
|x_k-y_k|\le2\omega_N,
\]

so

\[
\|x-y\|_2\le2\,2^{N/2}\omega_N
=O_A(N2^{-3N/2})\to0.
\tag{6.10}
\]

By the reverse triangle inequality for Euclidean norms,

\[
\left|\sqrt{V_N^B(\theta)}-\sqrt{V_N^B(r)}\right|
\le\|x-y\|_2.
\tag{6.11}
\]

Combine (6.6), (6.10), and (6.11) to obtain (6.2). Intersect the probability-one events over integer `A` to obtain (6.3). `QED`

This proof is included because the uniform-in-shift quantifier is essential for FBM dependence safety; a fixed-phase quadratic-variation statement would not be enough.

## 7. T71 — repeated non-Brownian-QV gate-template theorem

Let `Q:[0,1]->R` be continuous and define its dyadic quadratic energies by (5.1). Assume

\[
\boxed{V_N(Q)\not\longrightarrow1.}
\tag{7.1}
\]

Let `a_m -> infinity` be deterministic, and let `c_m in R`. Consider an arbitrary deterministic space-time shape with age fibers `K(u) subset R` such that, for every `m`,

\[
\boxed{
K(a_m+s)\subset\{c_m+Q(s)\}
\qquad(0\le s\le1).
}
\tag{7.2}
\]

**There is no assumption at all on the fibers between those unit gate blocks.** They may be enormous, disconnected, or all of `R`.

### Theorem T71

For every forward Brownian motion `X`,

\[
\boxed{
\Pr\left(
\exists R<\infty:\ X_{-u}\in K(u)
\quad\forall u\ge R
\right)=0.
}
\tag{T71}
\]

### Proof

Suppose the displayed event has positive probability. By a countable union over integer radii, choose a deterministic `R_0` such that

\[
E:=\{X_{-u}\in K(u)\text{ for every }u\ge R_0\}
\]

has probability `p>0`.

Choose one deterministic gate index `m` with `a_m>=R_0`. Because the FBM witness times satisfy `S_j->-infinity` a.s., choose one **deterministic witness index** `j` so far left that

\[
\Pr\{S_j\le-a_m-1\}>1-p/2.
\tag{7.3}
\]

Hence

\[
\Pr\left(E\cap\{S_j\le-a_m-1\}\right)>p/2.
\tag{7.4}
\]

For this fixed `j`, Definition 2.1 says

\[
B(s):=X_{S_j+s}-X_{S_j}
\]

is unconditional standard Brownian motion. On the event in (7.4), put

\[
\theta=(-a_m-1)-S_j\ge0.
\tag{7.5}
\]

For `0<=s<=1`, the corresponding absolute time is

\[
S_j+\theta+s=-a_m-1+s,
\]

whose age is `a_m+1-s`. Confinement and (7.2) therefore force

\[
B(\theta+s)
= c_m+Q(1-s)-X_{S_j}.
\tag{7.6}
\]

Spatial translation does not change quadratic energy, and reversing the dyadic partition merely reverses the list of increments. Thus, for **every** `N`,

\[
V_N^B(\theta)=V_N(Q).
\tag{7.7}
\]

Lemma 6.1 holds simultaneously for every `theta`, including the random value in (7.5), and gives

\[
V_N^B(\theta)\to1.
\]

Equation (7.7) contradicts (7.1). Therefore the event in T71 has probability zero. `QED`

No conditioning on the random witness time is used. The only FBM input is the unconditional Brownian law of one fixed witness future.

## 8. Move #16 — exact small cases reveal an explicit Brownian-scale rough template

Let

\[
\varphi(x)=\operatorname{dist}(x,\mathbb Z),
\]

the period-one tent map, and define

\[
\boxed{
Q(t)=
\sum_{n=0}^{\infty}
\sqrt{n+1}\,2^{-n/2}\,\varphi(2^n t),
\qquad 0\le t\le1.
}
\tag{8.1}
\]

The series converges uniformly because `0<=varphi<=1/2` and

\[
\sum_n\sqrt{n+1}\,2^{-n/2}<\infty.
\]

Hence `Q` is continuous, with `Q(0)=Q(1)=0`.

At dyadic level `N`, all terms `n>=N` vanish at every partition point. For `n<N`, `varphi(2^n t)` is affine on each level-`N` cell, with slope sign `r_{n,k} in {+1,-1}`. The sign rows are the usual Rademacher rows and satisfy the exact orthogonality relation

\[
\sum_{k=0}^{2^N-1}r_{n,k}r_{j,k}
=2^N\mathbf 1_{\{n=j\}}.
\tag{8.2}
\]

Therefore

\[
\begin{aligned}
V_N(Q)
&=2^{-N}\sum_{n=0}^{N-1}(n+1)2^n\\
&=\boxed{N-1+2^{-N}}.
\end{aligned}
\tag{8.3}
\]

In particular

\[
\boxed{V_N(Q)\to\infty.}
\tag{8.4}
\]

The exact finite self-check was run after the idea was established, not before it. It verifies the Rademacher orthogonality matrix and weighted-energy identity with exact integers/rationals for `N=1,...,12`:

- `artifacts/R07/20260918T2126Z_qv53_exact_check.py` — commit `6e9d3ea8a210b59d17790aa50304b6cfc2f6bf9a`;
- `artifacts/R07/20260918T2126Z_qv53_exact_check.out` — commit `e1f716fa96c7b1741524353c2bf7b10045c92775`.

The archived output ends `PASS`. It is explicitly a **SELF-CHECK**, not an external audit and not the proof of the all-`N` formula; (8.2)–(8.3) are the proof.

The first exact energies are

\[
\frac12,\frac54,\frac{17}{8},\frac{49}{16},\frac{129}{32},\ldots,
\]

which is the sequence that exposed the closed form (8.3).

Two further regularity facts show why this is a genuinely new frontier rather than a disguised run-40 sheet.

**Not `1/2`-Hölder.** If `Q` were `1/2`-Hölder with constant `C`, then each level-`N` increment would have absolute value at most `C2^{-N/2}`, giving `V_N(Q)<=C^2`, contradicting (8.4).

**Not bounded variation.** If a continuous function has finite total variation, then along partitions of mesh tending to zero,

\[
\sum |\Delta Q|^2
\le (\max|\Delta Q|)\operatorname{Var}(Q)\to0,
\]

again contradicting (8.4).

On the other hand the trace is not artificially much rougher than Brownian. Splitting (8.1) at the dyadic scale comparable with `h` gives

\[
|Q(t+h)-Q(t)|
\le C\sqrt{h\log(e/h)}
\tag{8.5}
\]

for small `h`. Thus its deterministic modulus is at Brownian's classical uniform-modulus scale up to constants. The obstruction is the **quadratic energy**, not a crude Hölder exponent.

**Outcome #16:** success. Exact small-scale computation led to a closed-form rough template with a clean QV mismatch.

## 9. T72 — canonical superexponentially sparse rough portal curtain

To avoid re-counting the earlier arithmetic/geometric gate families, the canonical representative uses **superexponentially separated** unit gate blocks and only Brownian-scale transport between them.

Set

\[
a_0=0,\qquad c_0=0,
\]

and, for `m>=1`,

\[
\boxed{a_m=2^{2^m},\qquad c_m=\sqrt{a_m}=2^{2^{m-1}}.}
\tag{9.1}
\]

Let

\[
I_m=[a_m,a_m+1],
\qquad
Z=\bigcup_{m\ge0}I_m.
\tag{9.2}
\]

Define a continuous center `C(u)` by

\[
C(a_m+s)=c_m+Q(s),\qquad 0\le s\le1,
\tag{9.3}
\]

and interpolate linearly from `c_m` at `a_m+1` to `c_{m+1}` at `a_{m+1}` across each gap. This is continuous because `Q(0)=Q(1)=0`.

On each gap

\[
G_m=(a_m+1,a_{m+1}),
\qquad
L_m=a_{m+1}-a_m-1,
\]
write

\[
y_m(u)=\frac{u-(a_m+1)}{L_m}\in(0,1).
\]

Define continuous aperture coefficients

\[
(\alpha(u),\beta(u))=
\begin{cases}
(1,0),&u\in Z,\\
(|\cos(\pi y_m(u))|,\ \sin(\pi y_m(u))),&u\in G_m.
\end{cases}
\tag{9.4}
\]

Finally define the closed backward space-time shape

\[
\boxed{
\mathcal Q_*
=
\left\{(-u,x):u\ge0,\ 
\alpha(u)|x-C(u)|\le u^3\beta(u)
\right\}.
}
\tag{9.5}
\]

It is closed because `C,alpha,beta` are continuous and (9.5) is a continuous sublevel condition.

At every gate block `I_m`, `alpha=1,beta=0`, so the fiber collapses for a **whole unit of age** to the translated rough trace

\[
K(a_m+s)=\{c_m+Q(s)\}.
\tag{9.6}
\]

At the midpoint of every gigantic gap,

\[
u_m=a_m+1+\frac{L_m}{2},
\]

we have `alpha(u_m)=0` and `beta(u_m)=1`, hence

\[
\boxed{K(u_m)=\mathbb R.}
\tag{9.7}
\]

So this shape has literal **full-space portals** between its restrictive blocks.

The gate blocks are extremely sparse:

\[
\frac{a_{m+1}}{a_m}=a_m\to\infty.
\tag{9.8}
\]

The required transport between gate centers is nevertheless only Brownian scale:

\[
c_{m+1}-c_m\sim a_m,
\qquad
\sqrt{a_{m+1}-a_m}\sim a_m,
\tag{9.9}
\]

so the family is not a disguised “forced superdiffusive jump” construction.

By (8.4), T71 applies to (9.6) and yields:

### Theorem T72

For every FBM `X`,

\[
\boxed{
\Pr\left(
\exists R<\infty:
(-u,X_{-u})\in\mathcal Q_*
\quad\forall u\ge R
\right)=0.
}
\tag{T72}
\]

## 10. Frozen-equivalence / collision audit: why this earns metric point 53

This is not a parameter change of an earlier R07 family.

1. **Versus run 40 (critical `1/2`-Hölder braids):** every run-40 sheet is `1/2`-Hölder, hence has bounded dyadic quadratic energy. The gate trace (8.1) has `V_N(Q)->infinity` and is provably not `1/2`-Hölder.

2. **Versus runs 33–34 / 49 (smooth or BV webs/tracks):** finite variation forces dyadic quadratic energy to vanish, while (8.4) diverges. This distinction survives constant spatial scaling/reflection and affine Brownian rescaling.

3. **Versus run 39 (Hausdorff-dimension barrier):** the canonical shape (9.5) has open two-dimensional chambers in every gap and even full-line fibers at (9.7), so a global `dim_H S<3/2` argument cannot apply.

4. **Versus run 52 (locally Lipschitz nonlinear null-packet curtains):** run 52's proof requires a regular moving drift; the present gate trace has infinite variation and Brownian-scale roughness. The new proof uses a path-energy invariant, not occupation density/local time.

5. **Versus run 46 (arithmetic portal hourglasses):** the present restrictive blocks occur at superexponential ages, so there is no positive-density arithmetic neck skeleton. Moreover the center shifts are deliberately unbounded across blocks, while their displacement/gap ratio remains Brownian-scale.

6. **Versus run 47 (sparse block portal archipelagos):** run 47 pays for a growing number `N_n` of **macroscopic bounded Gaussian increments** in each sparse block. Here each restrictive block has fixed macroscopic length one; the increasing obstruction lives at finer and finer **dyadic scales inside one block**, where the deterministic quadratic energy diverges. Its gap ratios (9.8) are far outside the old fixed-block persistence regime.

7. **Versus run 31 (accelerating chirps):** that center is smooth on compact age intervals and gains obstruction from increasingly fast far-past transport. Here the between-block transport is Brownian-scale by (9.9); the obstruction is microscopic roughness within each fixed unit gate.

The invariant “divergent dyadic gate-trace quadratic variation versus the Brownian unit rate” is unchanged qualitatively by the frozen equivalences (constant translation, reflection, Brownian scaling). The superexponential gate sparsity and full-space portal structure are likewise not converted into the earlier arithmetic/geometric families by a constant rescaling.

Therefore the fixed metric moves

\[
\boxed{52\longrightarrow53.}
\]

## 11. What did not work, and the next real frontier

Three routes were tested rather than one route being repeatedly polished:

- **#2:** occupation/local-time continuation from run 52 fails at the intended Brownian-scale rough trace; generic roughness alone is too weak because deterministic Takagi-type paths can carry Brownian-like quadratic variation.
- **#11:** pathwise containment dualized to discrete quadratic energy; this succeeds and gives T71.
- **#16:** exact dyadic computation found the explicit weighted tent template and the closed form `V_N=N-1+2^{-N}`; this yields T72.

The next genuinely new frontier is now **the unit-QV boundary**:

\[
V_N(Q)\to1.
\tag{11.1}
\]

At (11.1), neither run-40 regularity nor the present QV mismatch can distinguish the deterministic trace from Brownian quadratic energy. Schied/Mishura-type deterministic constructions show this is not vacuous. A next theorem would have to use a finer path invariant—plausibly signed cubic variation, Lévy-area-like multiscale statistics in an augmented embedding, or a simultaneous law-of-the-iterated-logarithm functional—rather than another QV lemma.

The simplest unresolved special case is: a repeated gate template `Q` with Brownian-scale modulus and **exact linear dyadic quadratic variation `V_N(Q)->1`**, with the same superexponential portal geometry as (9.5). I do not claim an answer here.

## 12. Validation, closure status, and honest label

Finite core: exact self-check executed and archived as listed in Section 8. It validates finite Walsh-energy arithmetic only and is labelled SELF-CHECK.

Theorem-sized claims: T71 and T72 have complete written proofs on this page.

Prior-art status: bounded search recorded above; QV/Takagi mechanism is explicitly acknowledged as classical. No novelty certificate is claimed.

Independent OTHER-track audits of T71/T72: **0/2**.

Therefore:

- metric: **52 -> 53**;
- source status: **PARTIAL**;
- exact Problem 7.8: **not closed**;
- T71/T72 external-audit status: **0/2**;
- publication novelty: **UNVERIFIED**;
- unchanged-run count after this movement: **0**.

No paper folder is created because the source problem is not closed under Section G.

## 13. Model / scheduler control status

The model requirement is still not enforceable through the exposed scheduler control surface in this runtime. The visible task-update interface exposes title, prompt, schedule/start-offset, enabled state, and timing mode, but **no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-model receipt**. Hence `GPT-6 / maximum` remains prompt text only here, and this report correctly identifies the actual run as GPT-5.6 Sol with reasoning level UNVERIFIED.

The root ledger also records that P26's historical `You cannot modify this task` response was authorization-context-specific: a later full P26 update succeeded from an authorized context, while other R-series IDs were denied in a different reconciliation context. The legitimate workaround for a still-denied task is the owning/authorized workspace or account, an authorized ownership/admin correction, or platform support—not a duplicate schedule or permission bypass.

Actually enforcing GPT-6 maximum would require persistent scheduler `model` / `reasoning_effort` routing fields (or an owning-workspace policy that pins them) **plus authenticated per-run telemetry** proving what executed. No scheduler modification was attempted in this run.

## 14. Structured ledger_delta (own immutable report only)

```yaml
ledger_delta:
  track: R07
  deployment: NEW-METHODS-2026-09-16
  intake: I0077
  source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8"
  metric_name: "number of genuinely distinct nonparabolic shape families with complete source-appropriate theorem"
  metric_before: 52
  metric_after: 53
  movement: true
  new_family: "superexponentially sparse rough quadratic-variation gate curtains with full-space portals"
  theorem_ids: [T71, T72]
  methods: [2, 11, 16]
  source_status: PARTIAL
  external_audits: "0/2"
  novelty: UNVERIFIED
  finite_self_check: PASS
  unchanged_count_after: 0
  next_frontier: "Brownian-scale deterministic gate templates with V_N(Q) -> 1"
  scheduler_model_selector: absent
  scheduler_reasoning_selector: absent
  runtime_model: "GPT-5.6 Sol"
  runtime_reasoning: UNVERIFIED
```

## 15. References checked this run

1. K. Burdzy and M. Scheutzow, *Forward Brownian Motion*, PTRF 160 (2014), 95–126; arXiv:1302.6958.
2. A. Schied, *On a class of generalized Takagi functions with linear pathwise quadratic variation*, JMAA 433 (2016), 974–990; arXiv:1501.00837.
3. Y. Mishura and A. Schied, *Constructing functions with prescribed pathwise quadratic variation*, JMAA 442 (2016), 117–137; arXiv:1511.04678.
4. R. Cont and P. Das, *Quadratic variation and quadratic roughness* (2022).

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was made.

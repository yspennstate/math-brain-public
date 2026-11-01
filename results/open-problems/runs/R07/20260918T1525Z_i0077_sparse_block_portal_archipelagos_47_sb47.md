Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `46 -> 47` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #19 MAKE IT AN ALGORITHM, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of this track.

# R07 CLOSABLE OUTSIDE — run 47: sparse block-gate portal archipelagos

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen metric

The frozen R07 quantity is still

> the number of genuinely distinct nonparabolic deterministic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative R07 report is

`runs/R07/20260918T1422Z_i0077_additive_portal_hourglasses_46_ap46.md`,

which moved `45 -> 46` and used Section-B moves `#3,#8,#20`. The present triple `#2,#19,#27` is different. All thirty Section-B labels have already appeared at least once in the I0077 chain, so the literal pool of three never-before-used labels is exhausted; I do not invent unused labels. What is new is the route and the triple relative to the preceding run.

Before new research I rechecked or recovered the current state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the complete visible R07 directory / immutable I0077 run sequence through run 46, the newest report itself, and the older reports most likely to collide with the present idea: run 18 (continuous parabolic combs), run 24/27 (geometrically sampled gates), run 35 (continuous-age finite-lag cages), and run 46 (syndetic arithmetic portal hourglasses);
- newest visible R15 state. R15’s controlling I0076/Problem-7.2 work has already been handed off and R15 is on a separate successor-screening track, so there is no ownership collision;
- targeted intake / exact-source searches for I0077, arXiv:1302.6958, Problem 7.8, and the exact source wording.

The large intake JSONL mirrors and the entire private repository cannot be rendered byte-for-byte in one connector response without truncation. I therefore record the reread honestly as **targeted/complete for I0077 continuity and collision checking, not a literal byte-for-byte reread of hundreds of unrelated intake rows**. The canonical claim still says `PENDING_ADMISSION, not READY` and reserves I0077 to R07. `INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8; `POSTED.md` does not close exact Problem 7.8. The old R07 KPZ/FPP route remains preserved in immutable history and is not reopened or deleted.

Entering metric: **46**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

I reopened the primary paper, including Definition 2.1, Definition 2.2, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` a.s. such that for every fixed witness index `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is an unconditional standard Brownian motion. Definition 2.2 gives decomposable FBMs by concatenating independent Brownian pieces stopped at finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, Section 4 uses the principal Dirichlet exponent `lambda_0(c_1,c_2)` of the killed Ornstein–Uhlenbeck generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the corresponding universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with normalized limsup/liminf confined to `[c_1,c_2]`;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM exists with exact pointwise parabolic confinement for every negative time.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” Problem 7.9 is separately the forward-Lévy-process question.

The result below gives a complete universal obstruction theorem for a new temporal geometry; it does not classify every space-time shape, so the source status stays PARTIAL.

## 3. Fresh current-literature / prior-art pass — 2026-09-18

Fresh bounded web searches included the exact source title/arXiv/problem wording, later/citing-paper variants, Brownian moving-window increments, scan statistics, discrete-time Gaussian persistence, and sampled Markov/Gaussian persistence.

The primary Burdzy–Scheutzow paper remains the identifiable source. Nearby methodological literature includes:

- S. N. Majumdar, A. J. Bray and G. C. M. A. Ehrhardt, *Persistence of a continuous stochastic process with discrete-time sampling*, Phys. Rev. E 64 (2001), 015101(R), on discrete-time persistence of Gaussian Markov processes;
- G. C. M. A. Ehrhardt, A. J. Bray and S. N. Majumdar, *Persistence of a Continuous Stochastic Process with Discrete-Time Sampling: Non-Markov Processes*, Phys. Rev. E 65 (2002), 041102;
- F. Aurzada and M. Kettner, *Persistence Exponents via Perturbation Theory: AR(1)-Processes*, J. Stat. Phys. 177 (2019), 651–665, arXiv:1810.09861;
- more recent persistence work such as Aurzada–Bothe–Druet–Kettner–Profeta on MA(1) processes (arXiv:2407.06870).

Those works concern persistence probabilities for sampled Gaussian processes. I found no accessible later paper in this bounded search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the FBM sparse-block gate theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Independent Gaussian increments, reflection estimates, and Brownian modulus estimates used below are classical and are not claimed new.

## 4. Negation first: why one sparse gate per huge portal does **not** give the needed Brownian obstruction

Run 46 left the natural question: can the arithmetic-neck obstruction survive when the restrictive times have zero density and the full-space portal gaps grow without bound?

I first tried the strongest possible sparse version: one bounded-increment requirement somewhere in a long unknown alignment window. That route is false even for ordinary Brownian motion.

Fix `M>0`. If `Z_k=B_{k+1}-B_k`, then the `Z_k` are i.i.d. `N(0,1)`. Hence for `m` integer candidate alignments,

\[
\mathbb P\{\exists k\in\{0,\dots,m-1\}: |B_{k+1}-B_k|\le M\}
=1-(1-p_M)^m\longrightarrow1,
\]

where `p_M=P(|N(0,1)|<=M)>0`.

So the naive uniform-phase lemma “a bounded increment somewhere in a longer and longer portal window is unlikely” is exactly wrong. Sparse gates create **alignment entropy**: a random witness can potentially line up with many candidate locations.

This does not refute Problem 7.8 and does not prove that a particular one-gate shape admits an FBM. It refutes the proposed proof mechanism and identifies what a successful sparse construction must contain: each sparse island must impose a sufficiently long *block* of consecutive constraints so that the exponential persistence cost beats the number of possible alignments.

That is the mechanism of the theorem below.

## 5. The three Section-B moves

### #2 — ATTACK THE NEGATION FIRST

The one-gate scan calculation above shows that merely sending gate density to zero while keeping one local restriction per portal is the wrong route: the scan probability tends to one rather than zero. The exact obstruction is the entropy of possible witness alignments.

### #19 — MAKE IT AN ALGORITHM

Given a witness age `U=-S_j`, the proof deterministically chooses the **highest fully completed gate block below `U`**. That map

\[
U\mapsto n(U):=\max\{n:e_n\le U\}
\]

turns every hypothetical confined witness into a concrete Brownian scan certificate.

### #27 — SWAP THE QUANTIFIERS

The dangerous quantifier is the random witness-dependent phase. Instead of conditioning on it, I first bound, for ordinary Brownian motion,

\[
\exists n\ge n_0\ \exists\theta\in[0,D_n)
\]

for all possible blocks and all possible phases. Only after this deterministic union is controlled is a fixed FBM witness inserted. Thus the random witness time never appears inside a conditional Brownian law.

## 6. A Brownian scan lemma for long bounded-increment blocks

Let `B` be standard Brownian motion. For integers `N>=1`, real `D>0`, and finite `M`, define

\[
H(N,D,M):=
\left\{\exists\theta\in[0,D):
|B_{\theta+k+1}-B_{\theta+k}|\le M
\quad k=0,\dots,N-1
\right\}.
\tag{6.1}
\]

Put

\[
\rho_M:=\mathbb P\{|Z|\le M+1/2\},\qquad Z\sim N(0,1).
\tag{6.2}
\]

Since `M<infinity`, `rho_M<1`.

### Lemma 6.1 — uniform scan bound

For every `N>=1`,

\[
\boxed{
\mathbb P(H(N,D,M))
\le
4\bigl((D+N+3)N^3+1\bigr)e^{-N^3/256}
+\bigl(DN^3+2\bigr)\rho_M^N.
}
\tag{6.3}
\]

#### Proof

Set

\[
\delta=N^{-3}
\]

and define the modulus event on `[0,D+N+2]`

\[
\Omega=
\left\{
\sup_{\substack{0\le s,t\le D+N+2\\|t-s|\le\delta}}
|B_t-B_s|\le\frac14
\right\}.
\tag{6.4}
\]

Cover the time interval by the overlapping intervals

\[
[j\delta,(j+2)\delta].
\]

If the modulus in (6.4) exceeds `1/4`, then for one such interval Brownian motion moves by more than `1/8` from the left endpoint. Reflection and the Gaussian Chernoff bound therefore give

\[
\mathbb P(\Omega^c)
\le
4\bigl((D+N+3)N^3+1\bigr)
\exp(-N^3/256).
\tag{6.5}
\]

Now mesh `[0,D]` at spacing `delta`; there are at most `DN^3+2` mesh phases. On `Omega`, if (6.1) holds for a phase `theta`, choose a mesh point `q` with `|q-theta|<=delta`. For every `k`,

\[
\begin{aligned}
|B_{q+k+1}-B_{q+k}|
&\le |B_{\theta+k+1}-B_{\theta+k}|\\
&\quad+|B_{q+k+1}-B_{\theta+k+1}|
+|B_{q+k}-B_{\theta+k}|\\
&\le M+\frac12.
\end{aligned}
\tag{6.6}
\]

For deterministic `q`, the `N` increments in (6.6) are independent `N(0,1)`, hence the probability that all of them satisfy (6.6) is exactly `rho_M^N`. A union bound over the mesh phases and (6.5) gives (6.3). `QED`

The crucial feature is that the phase interval may itself grow with the block index. The first term pays for Brownian continuity; the second is exactly “alignment entropy times persistence cost.”

## 7. I0077-R07-T59 — sparse block-gate obstruction

Let

\[
0<e_1<e_2<\cdots,\qquad e_n\to\infty,
\]

and let `N_n` be positive integers with

\[
e_n-N_n\longrightarrow\infty.
\tag{7.1}
\]

Write

\[
D_n:=e_{n+1}-e_n.
\tag{7.2}
\]

For each `n`, define the additive unit-spaced **gate block**

\[
G_n:=\{e_n-k: k=0,1,\dots,N_n\}.
\tag{7.3}
\]

Let `K(u) subset R` be nonempty deterministic fibers. Assume that for some finite `M`, every sufficiently large block has bounded consecutive cross-diameter:

\[
\boxed{
\sup_{x\in K(e_n-k),\ y\in K(e_n-k-1)}|x-y|\le M,
\qquad k=0,\dots,N_n-1.
}
\tag{7.4}
\]

No restriction is imposed on `K(u)` at ages outside the gate set.

Assume the exact summability condition

\[
\boxed{
\sum_n
\left[
4\bigl((D_n+N_n+3)N_n^3+1\bigr)e^{-N_n^3/256}
+\bigl(D_nN_n^3+2\bigr)\rho_M^{N_n}
\right]<\infty.
}
\tag{7.5}
\]

### Theorem T59

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T59}
\]

### Proof

Assume the displayed confinement event has positive probability. By a countable union over integer radii choose deterministic `R` such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability

\[
p:=\mathbb P(E_R)>0.
\tag{7.6}
\]

By (7.1) and the tail of the convergent series (7.5), choose deterministic `n_0` so large that

\[
e_n-N_n\ge R\qquad(n\ge n_0)
\tag{7.7}
\]

and

\[
\sum_{n\ge n_0}\mathbb P(H(N_n,D_n,M))<p/2.
\tag{7.8}
\]

Let `(S_j)` be an FBM witness sequence and put `U_j=-S_j`. Since `U_j->infinity` a.s., choose one **deterministic witness index** `j` such that

\[
\mathbb P\{U_j\ge e_{n_0}\}>1-p/4.
\tag{7.9}
\]

Then

\[
\mathbb P(E_R\cap\{U_j\ge e_{n_0}\})\ge3p/4.
\tag{7.10}
\]

Fix an outcome in this event. There is a unique `n>=n_0` such that

\[
e_n\le U_j<e_{n+1}.
\]

Set

\[
\theta=U_j-e_n\in[0,D_n).
\tag{7.11}
\]

For `k=0,\dots,N_n`, the physical time corresponding to Brownian-future time `theta+k` is

\[
S_j+\theta+k
=-U_j+(U_j-e_n)+k
=-(e_n-k).
\tag{7.12}
\]

All ages `e_n-k` are at least `R` by (7.7). Hence on `E_R`,

\[
X_{-(e_n-k)}\in K(e_n-k).
\]

Using the cross-diameter hypothesis (7.4),

\[
\begin{aligned}
|B^{(j)}_{\theta+k+1}-B^{(j)}_{\theta+k}|
&=|X_{-(e_n-k-1)}-X_{-(e_n-k)}|\\
&\le M,
\end{aligned}
\]

for every `k=0,\dots,N_n-1`. Thus the standard Brownian path `B^{(j)}` belongs to `H(N_n,D_n,M)` for **some** `n>=n_0`.

Therefore pathwise

\[
E_R\cap\{U_j\ge e_{n_0}\}
\subseteq
\bigcup_{n\ge n_0}H(N_n,D_n,M;B^{(j)}).
\tag{7.13}
\]

For this fixed deterministic witness index `j`, Definition 2.1 says that `B^{(j)}` is unconditional standard Brownian motion. Hence, by (7.8),

\[
\mathbb P\left(
\bigcup_{n\ge n_0}H(N_n,D_n,M;B^{(j)})
\right)<p/2,
\]

contradicting (7.10). This proves T59. `QED`

### Useful entropy corollary

A simple sufficient condition for (7.5) is

\[
\boxed{
\frac{N_n}{\log(n+1)}\to\infty,
\qquad
\log(D_n+N_n)=o(N_n).
}
\tag{7.14}
\]

Indeed, the second summand in (7.5) has logarithm

\[
\log D_n+3\log N_n+N_n\log\rho_M+O(1)
=-c_MN_n+o(N_n),
\]

with `c_M=-log rho_M>0`, and the first has the overwhelming negative term `-N_n^3/256`. The first condition in (7.14) makes both resulting tails summable in the block index.

This isolates the mechanism cleanly:

> block persistence length must dominate logarithmic alignment entropy.

## 8. Canonical family: dyadic sparse portal archipelagos

Take block endpoints and lengths

\[
e_n=2^n,\qquad N_n=n^2,\qquad n\ge8.
\tag{8.1}
\]

The restrictive gate set is

\[
\mathcal G
:=\bigcup_{n\ge8}\{2^n-k:0\le k\le n^2\}.
\tag{8.2}
\]

Because `2^8>9^2` and

\[
2(n+1)^2-(n+2)^2=n^2-2>0,
\]

induction gives `2^n>(n+1)^2` for every `n>=8`; hence consecutive blocks are disjoint and separated by increasingly long gaps.

Let

\[
g(u)=\log(1+u),\qquad d(u)=\operatorname{dist}(u,\mathcal G).
\tag{8.3}
\]

Define the half-aperture

\[
a(u)=
\begin{cases}
(1-2d(u))^{-1},&d(u)<1/2,\\
+\infty,&d(u)\ge1/2,
\end{cases}
\tag{8.4}
\]

and fibers

\[
K_*(u)=
\begin{cases}
[g(u)-a(u),g(u)+a(u)],&a(u)<\infty,\\
\mathbb R,&a(u)=\infty.
\end{cases}
\tag{8.5}
\]

The associated deterministic shape is

\[
\mathcal A_*
:=\{(-u,x):u>0,\ x\in K_*(u)\}\cup(\{0\}\times\mathbb R).
\tag{8.6}
\]

The shape is closed: its complement is the open set where `d(u)<1/2` and `|x-g(u)|>1/(1-2d(u))`.

At each gate `u in G`, `a(u)=1`, so the neck fiber is

\[
[g(u)-1,g(u)+1].
\tag{8.7}
\]

For consecutive gate ages inside one block,

\[
|g(u)-g(u-1)|
=\log\frac{u+1}{u}<1,
\]

hence the consecutive cross-diameter is strictly less than `3`. We may take `M=3`.

For T59,

\[
D_n=e_{n+1}-e_n=2^n,
\qquad N_n=n^2.
\]

Thus

\[
\frac{N_n}{\log(n+1)}\to\infty,
\qquad
\frac{\log(D_n+N_n)}{N_n}
\sim\frac{n\log2}{n^2}\to0,
\]

so the entropy criterion (7.14) holds.

### Theorem T60 — dyadic portal-archipelago obstruction

For every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal A_*
\quad\forall u\ge R
\right)=0.
}
\tag{T60}
\]

This is an unusually sparse obstruction. Up to age `T`,

\[
\#(\mathcal G\cap[0,T])=O((\log T)^3),
\tag{8.8}
\]

so the restrictive gate set has asymptotic density zero (indeed polylogarithmic counting growth). Between block `n` and block `n+1`, there is a full-space portal interval of length at least

\[
2^n-(n+1)^2-1\longrightarrow\infty,
\tag{8.9}
\]

on which `K_*(u)=R`. Thus the path receives arbitrarily long intervals with literally no spatial restriction. Despite this, the increasing `n^2`-long neck archipelagos defeat every FBM because their Gaussian persistence cost beats the `2^n` alignment window.

## 9. Why point 47 is genuinely new under the frozen equivalence convention

This is not run 46 with another numerical parameter.

1. **Run 46 / T57 is syndetic.** It assumes bounded cross-diameter at every sufficiently large point of one fixed arithmetic lattice. Its gate gaps are uniformly bounded. Here the gate set has zero density and gaps tending to infinity; T57 fails maximally because almost every integer in a portal ocean has fiber `R`, making the consecutive arithmetic cross-diameter infinite.

2. **Brownian scaling cannot identify them.** Constant Brownian time scaling sends a syndetic gate set to another syndetic set, whereas the canonical gate set (8.2) has unbounded gaps. “Bounded gaps versus unbounded gaps” survives the frozen scaling/reflection/translation equivalences.

3. **Runs 24/27 are geometrically sampled, not clustered-additive.** Those routes have only `O(log T)` isolated geometric gates and use OU/sampled-Markov persistence or target-set contraction. The new family has increasing additive blocks of ordinary independent increments, and its obstruction comes from the balance between block length and alignment entropy.

4. **Run 35 constrains every large age through a finite-lag cage.** The present shape contains arbitrarily long open age intervals on which the fiber is exactly `R`, so that hypothesis fails.

5. **Runs 44/45 use temporal sets of positive measure or positive Hausdorff dimension.** Here the restrictive gate set is countable, Lebesgue-null, and Hausdorff dimension zero. Occupation-time and fractal-time image arguments are therefore silent.

Accordingly the canonical sparse portal archipelago is a genuinely different temporal geometry, not a trivial rescaling or a parameter value inside the prior syndetic family. The fixed metric moves

\[
\boxed{46\longrightarrow47}.
\]

## 10. What the failed route taught us

The theorem isolates a useful near-threshold quantity. For a block of length `N_n` whose witness alignment may range over a window of size `D_n`, the main probability balance is

\[
\underbrace{\log D_n}_{\text{alignment entropy}}
\quad\text{versus}\quad
\underbrace{N_n|\log\rho_M|}_{\text{bounded-increment persistence cost}}.
\tag{10.1}
\]

One isolated gate corresponds effectively to bounded `N_n`, where alignment entropy wins. The canonical archipelago has

\[
\log D_n\asymp n,
\qquad
N_n\asymp n^2,
\]

so persistence wins decisively.

This suggests a genuinely sharper next question rather than another cosmetic family: determine the critical sparse regime when

\[
N_n|\log\rho_M|-\log D_n
\]

stays of order one or order `log n`. A second direction is to replace bounded increments by non-identical gate-to-gate target kernels and ask for a product/transfer-operator entropy criterion.

## 11. Checker / audit / closure status

There is **no finite computational core** in T59/T60. The canonical inequalities are proved symbolically and the theorem is infinite/probabilistic, so I did not manufacture an exact-arithmetic checker merely to create an artifact.

The new claims are:

- `I0077-R07-T59`: sparse block-gate obstruction;
- `I0077-R07-T60`: dyadic sparse portal-archipelago corollary.

They currently have **0/2 independent OTHER-track audits**. No self-check is represented as an independent audit. Therefore the honest source label remains

**PARTIAL**.

Problem 7.8 itself is not called PROVED or REFUTED. The negation-first failure in Section 4 is a failure of an overbroad proposed sparse-gate proof mechanism, not a refutation of the source’s open-ended request. Publication novelty is **UNVERIFIED** pending a broader literature review and independent proof audits.

## 12. Model / scheduler / permission status

The requested line says GPT-6 with maximum reasoning, but the runtime actually identifies this worker as **GPT-5.6 Sol** and provides no authenticated reasoning-effort field, so I report **UNVERIFIED** and do not claim GPT-6 maximum.

The exposed scheduler control surface still offers title/prompt, schedule or start-offset, enablement, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed one-hour execution field, and no authenticated applied-model receipt**. Thus `GPT-6 / maximum` is still prompt text only in this surface. Making it enforceable would require the platform to expose persistent `model` and `reasoning_effort` fields (or an owning-workspace policy that pins them) together with authenticated runtime telemetry.

The historical P26 `You cannot modify this task` result was authorization-context-specific. Current `RESULTS.md` records that P26’s full update later succeeded from another authorized context. For any task that still rejects modification, the legitimate workaround is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support. There is no legitimate worker-side permission bypass, and no duplicate scheduler task was created here.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8
  target: generalize Theorem 4.3 beyond parabolic regions
  metric: number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem
  before: 46
  after: 47
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: PARTIAL
  admission_status: PENDING_ADMISSION_not_READY
  new_family: sparse block-gate portal archipelagos with zero-density gates and unbounded full-space portal gaps
  new_claims:
    - I0077-R07-T59
    - I0077-R07-T60
  audits_other_tracks: 0/2
  publication_novelty: UNVERIFIED
  section_B_moves:
    - 2
    - 19
    - 27
  finite_core: none
  checker: not_applicable
  next_frontier: critical balance between alignment entropy log(D_n) and block persistence cost N_n*abs(log(rho_M))
```

## 14. Readback target

This report is intended as the single immutable run record:

`runs/R07/20260918T1525Z_i0077_sparse_block_portal_archipelagos_47_sb47.md`

After creation it must be read back at the returned commit. No receipt-only commit is required.
Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `34 -> 35` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 35: bounded-step cages and positive-width meandering ribbons

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen R07 metric remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0226Z_i0077_countably_accumulating_bv_webs_34.md`,

which moved the metric `33 -> 34` and used methods `#3,#20,#25`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain; this was already documented by run 10 and preserved thereafter. Thus the literal request for three numbers never previously used on this problem is exhausted. I do not invent an unused move. The present run instead uses a new triple, `#2,#24,#27`, and a new mechanism.

Before new mathematics I recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the complete `runs/R07/` directory inventory through run 34, the newest own report, and the earlier reports whose families are closest to the present candidate (pure-power tubes, two-scale apertures, power-sheared tubes, fast-transport windows, asymmetric bi-power horns, additive/geometric alternating fences, accelerating chirps, finite crossing webs, and countably accumulating BV webs);
- the newest visible P26 audit state, which independently warns against metric inflation by counting a weaker historical theorem after a stronger later theorem already subsumes it;
- neighboring R15 / I0076 history confirming that Problem 7.2 is distinct from R07's Problem 7.8 and was handed off rather than reassigned here;
- targeted intake/source/ownership searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

The large intake JSONL mirrors cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: the exact I0077 source, ownership, posted exclusions, and prior-attempt inventory were recovered. I do not claim a literal visual reread of every unrelated intake row.

`INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still distinguishes I0077. The canonical claim names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of this exact target to R07. No other track's file is edited.

The old R07 KPZ/FPP route remains preserved in its immutable pre-I0077 reports and handoff. Nothing was deleted or reopened.

Entering metric: **34**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary Burdzy–Scheutzow source was rechecked on 2026-09-18, including Definitions 2.1–2.2, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X` has random witness times `S_n -> -infinity` such that, for each fixed witness index,

\[
B^{(n)}(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 gives the decomposable concatenation construction.

For a fixed normalized parabolic interval `[c_1,c_2]`, Theorem 4.3 uses the principal killed Ornstein–Uhlenbeck exponent `lambda_0(c_1,c_2)` and states the familiar three clauses: universal asymptotic obstruction when `lambda_0>=1`, decomposable asymptotic existence when `lambda_0<=1`, and pointwise all-negative-time confinement when the interval straddles zero and `lambda_0<1`.

Problem 7.8 is exactly the one-sentence request to generalize this theorem beyond parabolic shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh current-status and prior-art pass

Fresh bounded web searches on 2026-09-18 UTC covered:

- exact paper title, arXiv ID and Problem-7.8 wording;
- `Forward Brownian Motion` together with `moving interval`, `space-time shape`, `moving boundary`, and `bounded width`;
- ordinary Brownian survival in moving/two-sided absorbing corridors;
- Brownian tubes around deterministic/Lipschitz paths;
- Burdzy–Kang–Ramanan's time-dependent-interval Skorokhod problem and later references around reflected Brownian motion.

The identifiable nearby literature includes Burdzy–Kang–Ramanan, *The Skorokhod problem in a time-dependent interval* (Stochastic Processes Appl. 119 (2009), 428–452), which studies reflection in moving intervals, and finite-horizon ordinary-Brownian moving-boundary survival calculations such as Guillaume's work on step/piecewise-affine absorbing boundaries. These are different objects: reflection or finite-horizon ordinary Brownian survival, not eventual confinement of every possible FBM witness into a deterministic backward space-time cage.

I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the finite-lag cage theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The independent-increment estimate used below is elementary Brownian folklore and is not claimed as novel.

## 4. Research first: three new-method attacks

### Move #2 — ATTACK THE NEGATION FIRST

I first tried to make an extreme moving ribbon that might evade all previous normalized-parabola arguments: a tube of **fixed physical width** whose center can travel to distances of order `u` and reverse sign infinitely often. A canonical center is

\[
g(u)=u\sin(\log(1+u)).
\tag{4.1}
\]

Its normalized center is

\[
\frac{g(u)}{\sqrt u}=\sqrt u\sin(\log(1+u)),
\]

so it has subsequences tending to `+infinity` and `-infinity`. It is therefore not trapped near any fixed normalized parabolic interval and is not a one-signed power shear.

The attempted construction nevertheless fails for a much more local reason: a fixed-width ribbon with bounded physical speed forces **every unit Brownian increment of a sufficiently far-left witness to lie in one fixed bounded interval**. A standard Brownian path pays a fixed probability cost strictly below one for each such increment, and a sufficiently long block makes the event arbitrarily unlikely.

This attack therefore produced a theorem rather than a construction.

**Outcome #2: success as an obstruction; no proposed FBM construction survives.**

### Move #24 — FIND THE EXTREMAL OBJECT

The centerline is not the real invariant. The proof only needs the worst possible displacement between two allowed fibers one fixed physical time apart.

For a deterministic shape with backward-age fibers `K(u) subset R`, define, for a fixed lag `Delta>0`,

\[
\Gamma_\Delta(u)
:=
\sup\{|x-y|:x\in K(u),\ y\in K(u-\Delta)\},
\qquad u\ge\Delta.
\tag{4.2}
\]

The extremal object is the finite-lag cross-diameter

\[
M_\Delta:=\sup_{u\ge u_0}\Gamma_\Delta(u).
\tag{4.3}
\]

If `M_Delta<infinity`, every confined path forces each `Delta`-increment of a witness Brownian motion to have absolute value at most `M_Delta`, independent of the absolute spatial location of the cage.

This abstraction survives disconnected fibers, fractal fibers, breathing widths, and large deterministic drift. The general theorem below is therefore stronger than the ribbon corollary that earns the metric point.

**Outcome #24: success; the cross-diameter is the exact finite-lag obstruction needed by the proof.**

### Move #27 — SWAP THE QUANTIFIERS

A naive proof might condition on a random witness time `S_j`, which would be invalid because no independence between `S_j` and its Brownian witness path is supplied by the FBM definition.

The correct quantifier order is:

1. freeze a deterministic eventual-confinement radius `R` with positive probability;
2. freeze a deterministic block length `N` so the standard-Brownian path-only event has probability smaller than that positive probability;
3. only then choose one deterministic witness index `j` far enough left that `S_j+N Delta<=-R` with high probability.

This gives the contradiction without conditioning on `S_j` or assuming any independence.

**Outcome #27: success; the proof is dependence-safe.**

### Two routes that did not earn a theorem

I also checked whether the previous run-34 bounded-variation selector invariant could handle a positive-width ribbon. It cannot: once a fiber has interior, the confined path is no longer a selector of countably many deterministic BV sheets, so the selector-variation proof disappears completely.

I also tested allowing the ribbon half-width to grow without bound while retaining only a bounded-speed center. Then `M_Delta` need not be finite, and the fixed one-step probability cost disappears. That regime requires an inhomogeneous product / extreme-increment criterion and is left for a later run rather than being hidden inside the present theorem.

## 5. General new theorem: uniformly bounded finite-lag cages

Let `K(u) subset R`, `u>0`, be nonempty deterministic sets, and define the backward shape

\[
\mathcal C_K
=
\{(-u,x):u>0,\ x\in K(u)\}.
\tag{5.1}
\]

For geometric cleanliness one may assume `mathcal C_K` is closed; the probabilistic obstruction itself only uses membership in the fibers.

Assume there exist constants

\[
\Delta>0,\qquad u_0\ge\Delta,\qquad M<\infty
\]

such that

\[
\boxed{
\sup_{u\ge u_0}
\sup_{x\in K(u),\,y\in K(u-\Delta)}
|x-y|
\le M.
}
\tag{5.2}
\]

I call such a shape a **uniformly bounded finite-lag cage**.

### I0077-R07-T36 — finite-lag cage obstruction

**Theorem T36.** Under (5.2), for every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T36}
\]

Equivalently, a deterministic space-time shape that can eventually confine an FBM with positive probability must fail every uniform finite-lag cross-diameter bound of the form (5.2).

### Proof

Suppose the event in (T36) has positive probability. Since

\[
\{\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R\}
=
\bigcup_{m=1}^{\infty}E_m,
\]

where

\[
E_m:=\{X_{-u}\in K(u)\ \forall u\ge m\},
\]

there exists a deterministic integer `R>=u_0` and a number

\[
p_0:=\mathbb P(E_R)>0.
\tag{6.1}
\]

Let `B` be standard Brownian motion and put

\[
q:=\mathbb P\{|B_\Delta|\le M\}
=
\mathbb P\{|Z|\le M/\sqrt\Delta\},
\qquad Z\sim N(0,1).
\tag{6.2}
\]

Because `M<infinity` and `Delta>0`,

\[
0\le q<1.
\]

Choose a deterministic integer `N>=1` so large that

\[
q^N<\frac{p_0}{2}.
\tag{6.3}
\]

For a continuous path `b` starting at zero define the path-only event

\[
A_N(b)
:=
\left\{
|b((k+1)\Delta)-b(k\Delta)|\le M
\quad k=0,\ldots,N-1
\right\}.
\tag{6.4}
\]

For standard Brownian motion the `N` increments in (6.4) are independent `N(0,Delta)`, hence

\[
\mathbb P(A_N(B))=q^N<\frac{p_0}{2}.
\tag{6.5}
\]

Now use the FBM witnesses. Let `S_j -> -infinity` be a witness sequence and

\[
B^{(j)}(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0.
\]

For each deterministic `j`, `B^{(j)}` is standard Brownian motion. Since `S_j -> -infinity` almost surely, there exists a **deterministic** witness index `j` so far left that

\[
\mathbb P\{-S_j\ge R+N\Delta\}
>1-\frac{p_0}{4}.
\tag{6.6}
\]

Therefore

\[
\mathbb P\left(E_R\cap\{-S_j\ge R+N\Delta\}\right)
\ge p_0-\frac{p_0}{4}
=\frac{3p_0}{4}.
\tag{6.7}
\]

On this intersection put `U=-S_j`. For every `k=0,...,N-1`, both backward ages

\[
U-k\Delta,
\qquad
U-(k+1)\Delta
\]

are at least `R>=u_0`. Event `E_R` gives

\[
X_{S_j+k\Delta}\in K(U-k\Delta),
\]

\[
X_{S_j+(k+1)\Delta}\in K(U-(k+1)\Delta).
\]

Applying (5.2) at age `u=U-k Delta` yields

\[
\left|
B^{(j)}((k+1)\Delta)-B^{(j)}(k\Delta)
\right|
=
\left|
X_{S_j+(k+1)\Delta}-X_{S_j+k\Delta}
\right|
\le M.
\tag{6.8}
\]

Thus the intersection in (6.7) is a subset of the path-only event `A_N(B^{(j)})`. Since `B^{(j)}` is standard Brownian motion,

\[
\frac{3p_0}{4}
\le
\mathbb P(A_N(B^{(j)}))
=q^N
<\frac{p_0}{2},
\]

a contradiction. Therefore `P(E_R)=0` for every deterministic `R`, and the eventual-confinement event has probability zero. QED.

### Dependence audit

The proof never conditions on `S_j`. It uses only that one deterministic `j` has high probability of lying far enough left and that the full process `B^{(j)}` has the unconditional standard-Brownian law. No independence between `S_j`, `E_R`, and `B^{(j)}` is assumed.

## 6. Counted shape family: positive-width bounded-speed meandering ribbons

The general cage criterion is a compiler; it is **not** counted as an additional metric point on top of its concrete application.

Let

\[
g:[0,\infty)\to\mathbb R
\]

be globally Lipschitz with constant `V<infinity`, and let `H<infinity`. Define the ribbon

\[
\boxed{
\mathcal R_{g,H}
=
\{(-u,x):u\ge0,\ |x-g(u)|\le H\}.
}
\tag{7.1}
\]

For `Delta=1`, its fibers satisfy

\[
\sup_{x\in[g(u)-H,g(u)+H],\,y\in[g(u-1)-H,g(u-1)+H]}
|x-y|
\le V+2H.
\tag{7.2}
\]

Hence T36 gives the complete family theorem

\[
\boxed{
\forall\text{ FBM }X:\quad
\mathbb P\left(
\exists R:\ |X_{-u}-g(u)|\le H\ \forall u\ge R
\right)=0.
}
\tag{7.3}
\]

No monotonicity, periodicity, boundedness of `g`, or asymptotic normalized limit is assumed. The center may travel ballistically and reverse direction infinitely often.

### Canonical nonparabolic example

Take

\[
\boxed{
g(u)=u\sin(\log(1+u)),\qquad H=1.}
\tag{7.4}
\]

Then

\[
g'(u)
=
\sin(\log(1+u))
+
\frac{u}{1+u}\cos(\log(1+u)),
\]

so

\[
|g'(u)|<2
\qquad(u\ge0).
\tag{7.5}
\]

Thus one may take `V=2` and `M=4` in (7.2). T36 yields

\[
\boxed{
\mathbb P\left(
\exists R:\
\left|X_{-u}-u\sin(\log(1+u))\right|\le1
\quad\forall u\ge R
\right)=0
}
\tag{7.6}
\]

for every FBM.

This example was chosen so the theorem is not merely a narrower copy of the old centered subdiffusive tubes. Along sequences with `log(1+u)=pi/2+2pi n` and `3pi/2+2pi n`, respectively,

\[
\frac{g(u)}{\sqrt u}
\to+\infty
\quad\text{and}\quad
\frac{g(u)}{\sqrt u}
\to-\infty.
\tag{7.7}
\]

The ribbon therefore chases alternating ballistic-scale locations while remaining only width two in physical space.

## 7. Why this earns a separate metric point

This is not a parameter change of a previously counted family.

- Run 3's pure-power tubes have both walls tied to one fixed gauge `u^beta` around zero. The canonical ribbon (7.4) has a sign-changing ballistic center with infinitely many reversals and **constant physical width**; it is not contained in any centered sub-Brownian power tube at large times.
- Run 17's power-sheared tubes have center `mu u^rho` of fixed sign eventually and Brownian-scale width `Theta(sqrt u)`. Here the center repeatedly changes sign and the width is `Theta(1)`.
- Run 19's fast-transport windows and runs 27–28's sampled comb gates live at Brownian-normalized width `Theta(1)`, hence physical width `Theta(sqrt u)`, and their obstruction is an OU/log-time transport probability. Here the obstruction is additive physical-time entropy from **many ordinary unit increments**.
- Run 25's additive alternating half-line fences force occasional increments of order `sqrt u` over unit physical time. In the present ribbon the center itself has uniformly bounded unit increments; the impossibility comes from requiring an arbitrarily long block of merely bounded Gaussian increments, each paying a fixed probability cost.
- Runs 32–34 concern zero-width laminations/webs and derive path regularity from exact selector membership. The present ribbon has nonempty interior in every time fiber, so the selector/BV mechanism is unavailable.

Brownian rescaling preserves the qualitative distinction between bounded physical width and Brownian-scale `sqrt u` width, while constant translation/reflection cannot remove the infinitely reversing center in (7.4). Under the frozen equivalence convention this is therefore a genuinely new family.

Accordingly the metric moves

\[
\boxed{34\longrightarrow35.}
\]

and `unchanged_count` resets/remains `0`.

## 8. Exact-certificate status

There is no finite combinatorial or exhaustive arithmetic core in T36. The only quantitative input is the exact standard-Brownian fact that disjoint `Delta`-increments are independent `N(0,Delta)` and hence a bounded increment event has probability `q<1`; the proof then chooses `N` existentially. The derivative estimate (7.5) is analytic. I therefore did **not** manufacture an `artifacts/` checker merely to create a certificate.

This is a self-proof by R07, not an independent audit.

## 9. Closure status and strongest next route

New claim identifier:

`I0077-R07-T36` — uniformly bounded finite-lag cage obstruction, with counted concrete family “positive-width bounded-speed meandering ribbons.”

Independent OTHER-track audits for T36: **0/2** at creation. In particular, the fresh P26 run visible at the start of this invocation audited an older R07 theorem, not T36. Therefore neither T36 nor Problem 7.8 is called closed.

Overall source status remains

\[
\boxed{\text{PARTIAL}.}
\]

The strongest next mathematical route is the exact boundary of T36: allow a Lipschitz center but an unbounded half-width `H(u)`, so `M_Delta(u)` grows. Then a witness pays an inhomogeneous sequence of Gaussian increment costs. The natural quantity is

\[
\sum_n
\mathbb P\left(
|Z|>\frac{M_\Delta(n)}{\sqrt\Delta}
\right),
\]

or, more sharply, the product of interval-specific one-step acceptance probabilities. A divergence/convergence threshold could produce a genuine widening-corridor phase theorem rather than another bounded-width obstruction. I did not claim such a threshold in this run.

## 10. Model / scheduler control reality

The GPT-6 configuration issue remains unresolved at the actual exposed task-control surface. The scheduler schema available to this worker exposes title, prompt, schedule/start-offset, enabled state, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6 / maximum remains a prompt request here, not an enforceable or verifiable runtime setting.

The repository policy also records historical `You cannot modify this task` responses for some scheduler IDs including P26. The legitimate workaround is to use the authorized owning/account/workspace context or platform support; a worker-level permission bypass or duplicate task is explicitly disallowed. This run's owner instruction also forbids scheduler changes, so no scheduler mutation was attempted.

Changing the situation requires the product/backend/API to expose persistent `model` and `reasoning_effort` fields (or an equivalent authorized task-setting surface) and authenticated execution metadata showing what actually ran.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  intake: I0077
  source_problem: Burdzy-Scheutzow Problem 7.8
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: distinct nonparabolic shape families with complete source-appropriate theorem
  metric_before: 34
  metric_after: 35
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [2, 24, 27]
  new_claim: I0077-R07-T36
  new_family: positive-width bounded-speed meandering ribbons
  general_compiler: uniformly bounded finite-lag cages
  finite_core: none
  checker: none
  self_check_only: true
  independent_audits: 0/2
  prior_art_status: bounded search only; novelty UNVERIFIED
  source_status: PARTIAL
  next_obligation: widening finite-lag cages / inhomogeneous Gaussian increment-cost threshold, or independent audit of T36
```

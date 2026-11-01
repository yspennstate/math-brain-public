Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `35 -> 36` genuinely distinct nonparabolic shape families; Section-B moves actually used: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 36: variable-lag cages and sublogarithmically widening ribbons

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen R07 metric remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0327Z_i0077_bounded_step_meandering_ribbons_35.md`,

which moved the metric `34 -> 35` and used methods `#2,#24,#27`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain; this was documented before run 35. Thus the literal request for three numbers never previously used on this problem is exhausted. I do not invent unused moves. This run uses a new triple, `#5,#8,#20`, on the exact next obstruction named by run 35: the finite-lag bound is now allowed to diverge.

Before new mathematics I recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable R07/I0077 chain, in particular the nearby gauge, pulse, gate, comb, chirp, finite-web, countable-BV-web, and bounded-step-ribbon families;
- the newest visible R15 state, which has already rotated away from its distinct Problem 7.2 assignment and does not create an ownership conflict with I0077;
- current source/status searches for `Forward Brownian Motion`, arXiv `1302.6958`, exact Problem 7.8 wording, moving Brownian boundaries, widening corridors, and later author/citing literature.

The large intake JSONL mirrors cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: exact I0077 source, ownership, posted exclusions, queue status and prior-attempt history were recovered. I do not claim a literal visual reread of every unrelated intake row.

`INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 separately. The canonical claim still names R07 as exclusive provisional owner and literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner’s explicit direct assignment of this exact target to R07. No peer file or shared root is edited.

The old R07 KPZ/FPP route remains preserved in immutable pre-I0077 reports and handoff. Nothing was deleted or reopened.

Entering metric: **35**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary Burdzy–Scheutzow source was rechecked on 2026-09-18, including the open-problem page and Theorem 4.3.

Definition 2.1 says that an FBM `X` has witness times `S_j -> -infinity` almost surely such that, for each fixed deterministic witness index `j`,

\[
B^{(j)}(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion.

Theorem 4.3 is the parabolic-strip benchmark. For fixed `c_1<c_2` and the principal killed Ornstein–Uhlenbeck exponent `lambda_0(c_1,c_2)`, it gives: universal asymptotic obstruction when `lambda_0>=1`; decomposable asymptotic existence when `lambda_0<=1`; and pointwise all-negative-time confinement when `c_1<=0<=c_2` and `lambda_0<1`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Lévy sentence is separately Problem 7.9.

## 3. Fresh current-status and prior-art pass

Fresh bounded web searches on 2026-09-18 UTC covered:

- exact paper title, arXiv ID, Theorem 4.3 and Problem-7.8 wording;
- `Forward Brownian Motion` with `moving boundary`, `space-time shape`, `widening corridor`, `logarithmic width`, and `tube around Lipschitz path`;
- later/citing papers around ordinary Brownian moving-boundary survival;
- Frank Aurzada and Tanja Kramm, *First exit of Brownian motion from a one-sided moving boundary*, arXiv:1203.4691, which revisits Uchiyama’s one-sided integral test;
- Aurzada–Kramm–Savov, *First passage times of Lévy processes over a one-sided moving boundary*, arXiv:1201.1118 / MPRF 21 (2015), which treats one-sided moving boundaries growing like `t^gamma`, `gamma<1/2`;
- classical/algorithmic Brownian curved-boundary crossing literature such as Durbin–Williams and Herrmann–Tanré.

These are important nearby mechanisms, but they concern ordinary Brownian first-passage/survival or Lévy first passage, not eventual confinement of every possible FBM witness into a deterministic backward cage. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the variable-lag FBM cage theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Gaussian independent increments, Mills bounds and dyadic blocking are classical and are not claimed as novel.

## 4. Research first: three new-method attacks

### Move #20 — FIND WHY THE ALGORITHM FAILS

Run 35 proved impossibility from a **uniformly bounded fixed-lag cross-diameter**

\[
\sup_{u\ge u_0}\Gamma_\Delta(u)<\infty,
\qquad
\Gamma_\Delta(u):=
\sup_{x\in K(u),\,y\in K(u-\Delta)}|x-y|.
\]

Its suggested next regime was a widening cage, where every fixed-lag bound diverges. The old proof fails for an exact reason: with a fixed lag `Delta`, the one-step Brownian survival probability tends to one, so there is no longer a fixed cost `q<1` paid at every step.

That failure is not fatal. The proof only needs the **product of all step costs over one long dyadic age block** to go to zero. The step length itself can vary with the age scale.

**Outcome #20: the obstruction is identified exactly; replace one fixed lag by one optimized lag per dyadic scale.**

### Move #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

For a ribbon of half-width `H`, a lag `Delta` forces a Brownian increment of variance `Delta` into an interval of radius roughly

\[
L\Delta+2H,
\]

where `L` is the speed bound of the center. In standard-deviation units the cost parameter is

\[
z(\Delta,H)=\frac{L\Delta+2H}{\sqrt\Delta}
=L\sqrt\Delta+\frac{2H}{\sqrt\Delta}.
\]

The point is not the exact minimizer but the scale: differentiating in `Delta` shows that when `L>0` the balanced lag is of order `H/L`. Thus when the width itself grows, the proof should increase the lag with the width rather than keep unit lag forever.

For the theorem below I do not hard-wire the optimizer. I introduce a free dyadic lag sequence `Delta_n` and state the exact summability criterion it must satisfy.

**Outcome #5: success; the extra lag parameter exposes the correct variable-scale compiler.**

### Move #8 — GO THE OTHER WAY AND DISCRETIZE

The random FBM witness age cannot be conditioned on. I therefore discretize the *age scale*, not the witness time itself, into dyadic blocks

\[
[2^n,2^{n+1}).
\]

For each block I build a deterministic path-only Brownian event `A_n` using `N_n` independent increments of a deterministic length `Delta_n`. Eventual confinement at any witness age in that dyadic block implies `A_n`. Summability of `P(A_n)` then controls the union over **all possible random witness ages** without conditioning on the witness time.

**Outcome #8: success; the random-age dependence problem is removed by a deterministic dyadic union bound.**

## 5. General theorem: dyadic variable-lag cage obstruction

Let `K(u) subset R`, `u>0`, be nonempty deterministic fibers and let

\[
\mathcal C_K=\{(-u,x):u>0,\ x\in K(u)\}.
\]

For a lag `Delta>0` define

\[
\Gamma_\Delta(u)
:=
\sup\{|x-y|:x\in K(u),\ y\in K(u-\Delta)\},
\qquad u\ge\Delta.
\tag{5.1}
\]

For every sufficiently large integer `n`, choose a deterministic lag

\[
0<\Delta_n\le 2^{n-2},
\]

put

\[
N_n:=\left\lfloor\frac{2^{n-2}}{\Delta_n}\right\rfloor\ge1,
\tag{5.2}
\]

and suppose there is a finite deterministic `M_n` such that

\[
\Gamma_{\Delta_n}(u)\le M_n
\qquad
\forall u\in[2^{n-1},2^{n+1}].
\tag{5.3}
\]

Define

\[
q_n
:=
\Pr\{|B_{\Delta_n}|\le M_n\}
=
\Pr\left\{|Z|\le\frac{M_n}{\sqrt{\Delta_n}}\right\},
\quad Z\sim N(0,1).
\tag{5.4}
\]

### I0077-R07-T37 — dyadic variable-lag cage theorem

**Theorem T37.** If

\[
\boxed{
\sum_{n=n_*}^{\infty} q_n^{N_n}<\infty,
}
\tag{5.5}
\]

then for every forward Brownian motion `X`,

\[
\boxed{
\Pr\left(
\exists R<\infty:
X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T37}
\]

This strictly extends run 35’s finite-lag theorem: `M_n` may tend to infinity and `q_n` may tend to one.

### Proof

Assume contrary that eventual confinement has positive probability. By countable union there is a deterministic integer `R` such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability

\[
p_0:=\Pr(E_R)>0.
\tag{5.6}
\]

Because (5.5) is summable, choose a deterministic integer `n_0` so large that

\[
2^{n_0-1}\ge R
\tag{5.7}
\]

and

\[
\sum_{n\ge n_0}q_n^{N_n}<\frac{p_0}{2}.
\tag{5.8}
\]

Let `S_j -> -infinity` be FBM witnesses and `B^{(j)}(t)=X_{S_j+t}-X_{S_j}`. Since `-S_j -> +infinity` almost surely, choose one **deterministic** witness index `j` such that

\[
\Pr\{-S_j\ge 2^{n_0}\}>1-\frac{p_0}{4}.
\tag{5.9}
\]

Therefore

\[
\Pr\left(E_R\cap\{-S_j\ge2^{n_0}\}\right)
\ge\frac{3p_0}{4}.
\tag{5.10}
\]

For each `n` define the path-only event on a continuous path `b`,

\[
A_n(b):=
\left\{
|b((k+1)\Delta_n)-b(k\Delta_n)|\le M_n,
\quad k=0,\ldots,N_n-1
\right\}.
\tag{5.11}
\]

For standard Brownian motion, the increments in (5.11) are independent `N(0,Delta_n)`, hence

\[
\Pr(A_n(B))=q_n^{N_n}.
\tag{5.12}
\]

Now work on the event in (5.10) and put `U=-S_j`. Choose the unique `n>=n_0` with

\[
2^n\le U<2^{n+1}.
\]

Because `N_n Delta_n<=2^{n-2}`, every backward age

\[
u_k:=U-k\Delta_n,
\qquad k=0,\ldots,N_n,
\]

satisfies

\[
2^{n-1}<u_k<2^{n+1}
\]

and, by (5.7), is at least `R`. Event `E_R` therefore implies

\[
X_{S_j+k\Delta_n}\in K(u_k),
\qquad
X_{S_j+(k+1)\Delta_n}\in K(u_k-\Delta_n).
\]

By (5.3),

\[
|B^{(j)}((k+1)\Delta_n)-B^{(j)}(k\Delta_n)|
\le M_n
\]

for every `k=0,...,N_n-1`. Consequently

\[
E_R\cap\{-S_j\ge2^{n_0}\}
\subset
\bigcup_{n\ge n_0}A_n(B^{(j)}).
\tag{5.13}
\]

The crucial point is that the right side is a union of events depending only on the Brownian witness path; it does not condition on `S_j` and does not require independence between `S_j` and `B^{(j)}`.

Since `B^{(j)}` is standard Brownian motion,

\[
\Pr\left(\bigcup_{n\ge n_0}A_n(B^{(j)})\right)
\le
\sum_{n\ge n_0}q_n^{N_n}
<\frac{p_0}{2},
\]

contradicting (5.10). Therefore eventual confinement has probability zero. QED.

## 6. Counted new family: sublogarithmically widening bounded-speed ribbons

Let `g:[0,infinity)->R` be globally Lipschitz with constant `L<infinity`. Let

\[
h(u)=a\,[\log(e+u)]^\gamma,
\qquad a>0,\qquad 0<\gamma<1,
\tag{6.1}
\]

and define the ribbon

\[
K(u)=[g(u)-h(u),\ g(u)+h(u)].
\tag{6.2}
\]

### I0077-R07-T38 — sublogarithmic widening-ribbon obstruction

For every `a>0`, every `0<gamma<1`, every globally Lipschitz deterministic center `g`, and every FBM `X`,

\[
\boxed{
\Pr\left(
\exists R<\infty:
|X_{-u}-g(u)|\le a[\log(e+u)]^\gamma
\quad\forall u\ge R
\right)=0.
}
\tag{T38}
\]

### Proof from T37

For each large `n`, set

\[
H_n:=h(2^{n+1})
\]

and choose

\[
\Delta_n:=H_n.
\]

For large `n`, `1<=Delta_n<=2^{n-2}` because `H_n=O(n^gamma)`.

Since `g` is `L`-Lipschitz and `h` is nondecreasing,

\[
\Gamma_{\Delta_n}(u)
\le L\Delta_n+h(u)+h(u-\Delta_n)
\le (L+2)H_n
=:M_n
\]

for `u<=2^{n+1}`. Therefore

\[
z_n:=\frac{M_n}{\sqrt{\Delta_n}}
\le(L+2)\sqrt{H_n}.
\tag{6.3}
\]

Let

\[
p_n:=1-q_n=\Pr\{|Z|>z_n\}.
\]

Using the standard Mills lower bound

\[
\bar\Phi(z)\ge \frac{z}{1+z^2}\,\phi(z),\qquad z>0,
\]

there are constants `c,C>0`, depending only on `L`, such that for all large `n`,

\[
p_n\ge c H_n^{-1/2}e^{-C H_n}.
\tag{6.4}
\]

Also

\[
N_n
=\left\lfloor\frac{2^{n-2}}{H_n}\right\rfloor
\ge c\frac{2^n}{H_n}
\tag{6.5}
\]

for all large `n`. Hence

\[
N_np_n
\ge
c\,2^n H_n^{-3/2}e^{-C H_n}.
\tag{6.6}
\]

But

\[
H_n=a[\log(e+2^{n+1})]^\gamma=O(n^\gamma)=o(n).
\]

Therefore

\[
\log(N_np_n)
\ge n\log2-C' n^\gamma-O(\log n)
\longrightarrow+\infty
\]

linearly in `n`. In particular `N_np_n>=e^{c'n}` for all sufficiently large `n`. Since

\[
q_n^{N_n}=(1-p_n)^{N_n}\le e^{-N_np_n},
\]

we get a superexponentially summable sequence,

\[
\sum_n q_n^{N_n}<\infty.
\]

T37 proves T38. QED.

## 7. Canonical explicit example

Take the same extreme bounded-speed center that defeated a naive normalized-parabola comparison in run 35,

\[
g(u)=u\sin(\log(1+u)).
\tag{7.1}
\]

Its derivative is

\[
g'(u)=
\sin(\log(1+u))
+
\frac{u}{1+u}\cos(\log(1+u)),
\]

so

\[
|g'(u)|<2.
\]

Now give the ribbon an **unbounded** half-width

\[
h(u)=\sqrt{\log(e+u)}.
\]

Then every FBM satisfies

\[
\boxed{
\Pr\left(
\exists R:
\left|X_{-u}-u\sin(\log(1+u))\right|
\le\sqrt{\log(e+u)}
\quad\forall u\ge R
\right)=0.
}
\tag{7.2}
\]

The fixed-lag cross-diameter now diverges:

\[
\Gamma_1(u)\ge 2h(u-1)-|g(u)-g(u-1)|\to\infty
\]

along a subsequence, and in any case the fiber diameter itself is `2h(u)->infinity`. Thus run 35’s bounded finite-lag theorem does **not** apply. The new proof succeeds only because it lets the Brownian lag grow with the width and pays the aggregate cost across a dyadic block.

## 8. Why this earns a new metric point rather than a parameter variation

Run 35’s counted family had **uniformly bounded physical fiber width** and, more generally, a uniformly bounded cross-diameter at one fixed physical lag. T38 has

\[
\operatorname{diam}K(u)=2a[\log(e+u)]^\gamma\to\infty
\]

and every fixed-lag cross-diameter is allowed to diverge. This bounded-versus-unbounded cross-sectional geometry is invariant under Brownian scaling, reflection, constant translation and finite parameter changes in the run-35 family. The proof invariant also changes: run 35 used a fixed cost `q<1` per fixed-length increment, whereas T38 uses `q_n->1` and wins only through a scale-dependent lag plus a summable dyadic product.

Therefore this is not counted as “the same ribbon with another numerical width.” The structural family is **unbounded sublogarithmic widening cages/ribbons**, and all `a>0`, `0<gamma<1`, and globally Lipschitz centers are counted together as exactly one new metric point.

Metric:

\[
\boxed{35\longrightarrow36.}
\]

`unchanged_count` resets to `0`.

## 9. Failed/unfinished routes, stated explicitly

1. **Keep lag fixed while width diverges.** Fails because `q_n->1`; no fixed geometric cost survives.
2. **Use only the fiber diameter.** Insufficient for drifting centers; the relevant quantity is the lagged cross-diameter `Gamma_Delta`.
3. **Push T38 directly to logarithmic width `h(u)~a log u`.** The present simple choice `Delta_n~H_n` becomes marginal because the Gaussian tail contributes an exponential in `H_n~n`; constants matter. The theorem T37 still applies, but deciding the best constant requires optimizing `Delta_n` sharply and is not claimed here.
4. **Claim a phase transition.** Not justified. T38 is a complete universal-impossibility theorem for the stated sublogarithmic family; it does not classify the logarithmic or faster-widening regimes.

The next high-value route is precisely the marginal logarithmic family

\[
h(u)=a\log(e+u),
\]

where optimizing

\[
\frac{L\Delta+2h}{\sqrt\Delta}
\]

suggests a nontrivial constant-scale competition. That should be attacked before another checker or audit is manufactured.

## 10. Validation / finite core

There is no finite arithmetic or combinatorial core. The proof is analytic and written on the page. I therefore did **not** create a checker merely to generate a certificate. The only quantitative ingredient beyond independent Gaussian increments is the standard Mills inequality stated explicitly above.

This is a self-check only. T37/T38 have **0/2 independent OTHER-track audits**. No closure or paper package is claimed.

## 11. Source status and closure status

Problem 7.8 remains **PARTIAL**, because the source asks open-endedly for generalization beyond parabolas and R07 has now proved many families rather than a single canonical universal classification theorem. The new result itself is theorem-sized and complete, but it has no independent audits yet.

No source-level `PROVED` closure label is assigned. No failed stronger extension is mislabelled as a refutation of Problem 7.8.

## 12. Model / scheduler control status

This run actually executed as **GPT-5.6 Sol; reasoning level UNVERIFIED**, so it is not reported as GPT-6 maximum.

The currently exposed scheduler/task-control schema still offers title/prompt, schedule or start offset, enabled state, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6/maximum therefore remains prompt text only in this surface.

There is one current correction to older reports: root `RESULTS.md` now records that **P26’s full prompt update later succeeded in an authorized context**, even though historical probes had returned `You cannot modify this task`. Thus the P26 denial should no longer be described as a permanent current failure. The legitimate workaround is exactly what occurred: perform the modification from an authorized owning context/product surface. No permission bypass or duplicate schedule is appropriate. This run was explicitly prohibited from scheduler changes and attempted none.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8
  target: generalize Theorem 4.3 beyond parabolic regions
  metric: number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem
  before: 35
  after: 36
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  status_before: PARTIAL
  status_after: PARTIAL
  new_claims:
    - I0077-R07-T37 dyadic variable-lag cage obstruction
    - I0077-R07-T38 sublogarithmically widening bounded-speed ribbon obstruction
  counted_family: sublogarithmically widening finite-lag cages/ribbons
  independent_audits: 0/2
  checker: none; no finite core
  methods: [5, 8, 20]
  prior_art_search_date: 2026-09-18
  novelty: UNVERIFIED
  next_obligation: analyze the marginal logarithmic-width regime h(u)=a log(e+u) via optimized variable lags
```

## 14. Immutable-delivery note

This report is the sole R07 write for this run. After creation it must be read back at the returned commit. No receipt-only commit is permitted.

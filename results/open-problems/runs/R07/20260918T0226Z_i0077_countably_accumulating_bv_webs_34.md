Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `33 -> 34` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #20 FIND WHY THE ALGORITHM FAILS, #25 COUNT THE SAME THING TWICE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 34: countably accumulating bounded-variation webs

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0132Z_i0077_finite_smooth_crossing_webs_33.md`,

which moved the metric `32 -> 33` and used methods `#6,#18,#26`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. Thus the literal instruction to use three moves never previously tried on this problem is exhausted; I do not invent a false history. This run uses a new triple and a genuinely new structural mechanism.

Before new mathematics I recovered current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 history needed to distinguish the new family;
- the current R15 directory: R15 handed off distinct Problem 7.2 / I0076 after its six-run rule and has since rotated to other targets;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 distinctly. The canonical claim names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of this exact target to R07. The root `RESULTS.md` R-series table is stale by its own warning and is not used as the mathematical baseline; the complete own report above is.

The large intake JSONL resources cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: the exact I0077 statement, ownership, exclusions, and relevant prior attempts were recovered. I do not claim a literal reread of every unrelated intake row.

The old R07 KPZ variance route remains preserved in the immutable pre-I0077 reports; nothing was deleted or reopened.

Entering metric: **33**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary arXiv/PTRF source was re-opened on 2026-09-18, including Definitions 2.1–2.2, Theorem 4.3 and the open-problem page.

Definition 2.1 says that an FBM has random witness times `S_n -> -infinity` such that, for every fixed witness index,

\[
B^{(n)}(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 gives the decomposable construction by concatenating independent Brownian pieces stopped at finite stopping times.

For the static parabolic normalized interval `[c_1,c_2]`, Theorem 4.3 states the familiar killed-OU threshold: universal obstruction at `lambda_0(c_1,c_2)>=1`, decomposable asymptotic existence at `lambda_0<=1`, and, when `c_1<=0<=c_2` and `lambda_0<1`, decomposable pointwise confinement to the exact parabolic strip for all negative times.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. The following forward-Lévy sentence is separately Problem 7.9.

Primary source: `https://arxiv.org/abs/1302.6958` and the published PTRF article.

## 3. Fresh current-status and prior-art pass

Fresh bounded searches on 2026-09-18 UTC covered:

- the exact paper title, arXiv ID and Problem-7.8 wording;
- later/citing material around Burdzy–Scheutzow and “other space-time shapes”;
- `continuous selector bounded variation countable functions`;
- `countable nonincreasing functions continuous selector`;
- Brownian motion constrained to countable unions of curves/graphs;
- Brownian quadratic variation / infinite total variation versus finite-variation paths.

The original 2014 article remains the identifiable primary Problem-7.8 statement. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the countable-web theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

Nearby but different literature includes Burdzy–Kang–Ramanan on the Skorokhod problem in a time-dependent interval: that concerns reflected Brownian motion between moving boundaries, not an ordinary Brownian witness required to stay in a deterministic countable web. Brownian nonzero quadratic variation / infinite variation is classical folklore and is not claimed as new here. The countable monotone-selector lemma below is elementary and likewise not claimed as prior-art novelty.

## 4. Method #3 — prove something stronger: remove finiteness of the web

Run 33 proved that a continuous selector from **finitely many** locally Lipschitz sheets is locally Lipschitz, hence cannot be a Brownian witness. The obvious strengthening is to allow countably infinitely many sheets with local accumulation.

This is genuinely more difficult: the finite proof uses the fact that, at a selected value, every inactive sheet has a positive local separation. For a countable web accumulating at the selected leaf, the infimum of those separations can be zero at every time.

The correct replacement hypothesis is not local separation but a **summable total-variation budget** across all sheets on each compact time interval.

**Outcome #3: success.** Finiteness can be replaced by local summability of sheet variations.

## 5. Method #20 — identify exactly why the finite-sheet algorithm fails

The finite-web selector algorithm says: near `u_0`, discard every sheet not passing through the currently selected point, because finitely many inactive sheets have a positive minimum gap. This fails maximally for the canonical example in Section 10 below: at every `u>0` and in every neighborhood of the zero leaf there are infinitely many other sheets. No positive inactive-sheet gap exists.

So the run-33 proof cannot be repaired by a smaller neighborhood, a crossing-count condition, or a locally finite graph argument.

The replacement is to stop tracking **which** sheet is active. Instead track a scalar envelope that pays for *all possible vertical motion of all sheets at once*. That leads to the cumulative variation function

\[
V(t)=\sum_{n\ge0}\operatorname{Var}_{[a,t]}(g_n).
\]

**Outcome #20: success.** The exact obstruction to the old algorithm identifies the new invariant.

## 6. Method #25 — count the same vertical motion twice

The key observation is that subtracting the global variation budget makes every sheet monotone downward, while adding it makes every sheet monotone upward. A selector is therefore squeezed from both sides. This turns an infinite switching problem into two monotonicity statements.

### Lemma 6.1 — countable monotone-selector lemma

Let `I=[a,b]`. Let `f_0,f_1,...:I->R` be nonincreasing functions. If `h:I->R` is continuous and

\[
h(t)\in\{f_n(t):n\ge0\}\qquad\forall t\in I,
\tag{6.1}
\]

then `h` is nonincreasing. The analogous statement holds for nondecreasing functions.

### Proof

Suppose for contradiction that `h(s)<h(t)` for some `s<t`. For every level

\[
c\in(h(s),h(t)),
\]

continuity gives a first hitting time

\[
\tau(c)=\inf\{r\in[s,t]:h(r)=c\}.
\]

If `c_1<c_2`, then necessarily `\tau(c_1)<\tau(c_2)`: a continuous path starting below both levels must hit the lower level strictly before its first hit of the higher one.

For each `c`, choose an index `n(c)` such that

\[
h(\tau(c))=f_{n(c)}(\tau(c))=c.
\]

There are uncountably many levels `c` but only countably many indices. Hence one index `n` is used for two levels `c_1<c_2`. Then

\[
\tau(c_1)<\tau(c_2),\qquad
f_n(\tau(c_1))=c_1<c_2=f_n(\tau(c_2)),
\]

contradicting that `f_n` is nonincreasing. QED.

### Lemma 6.2 — summable-variation selector lemma

Let `g_0,g_1,...` be continuous functions on `I=[a,b]`, each of bounded variation, and suppose

\[
\boxed{
\sum_{n=0}^\infty \operatorname{Var}_{[a,b]}(g_n)<\infty.
}
\tag{6.2}
\]

If `h:I->R` is continuous and

\[
h(t)\in\{g_n(t):n\ge0\}\qquad\forall t\in I,
\tag{6.3}
\]

then `h` has bounded variation and, quantitatively,

\[
\boxed{
\operatorname{Var}_{[a,b]}(h)
\le
\sum_{n=0}^\infty \operatorname{Var}_{[a,b]}(g_n).
}
\tag{6.4}
\]

### Proof

For each `n` define

\[
v_n(t)=\operatorname{Var}_{[a,t]}(g_n),\qquad a\le t\le b.
\]

Because `g_n` is continuous and of bounded variation, `v_n` is continuous and nondecreasing. By (6.2), the series

\[
V(t)=\sum_{n=0}^\infty v_n(t)
\tag{6.5}
\]

converges uniformly on `I` by the Weierstrass M-test and therefore defines a continuous nondecreasing function.

For `s<t`, additivity of total variation gives

\[
g_n(t)-g_n(s)
\le \operatorname{Var}_{[s,t]}(g_n)
=v_n(t)-v_n(s)
\le V(t)-V(s).
\]

Hence every `g_n-V` is nonincreasing. Since `h-V` is a continuous selector from the countable family `{g_n-V}`, Lemma 6.1 gives that `h-V` is nonincreasing. Likewise,

\[
g_n(t)-g_n(s)\ge-[V(t)-V(s)],
\]

so every `g_n+V` is nondecreasing and Lemma 6.1 applied with reversed inequalities gives that `h+V` is nondecreasing. Therefore for all `s<t`,

\[
|h(t)-h(s)|\le V(t)-V(s).
\tag{6.6}
\]

For any partition `a=t_0<\cdots<t_k=b`, summing (6.6) yields

\[
\sum_{j=1}^k |h(t_j)-h(t_{j-1})|
\le V(b)-V(a)
=\sum_n\operatorname{Var}_{[a,b]}(g_n).
\]

Taking the supremum over partitions proves (6.4). QED.

This is the promised double count: `h-V` and `h+V` count the same possible vertical motion from opposite sides.

**Outcome #25: success.** Infinite sheet switching is controlled without any leaf-address conservation or local sheet separation.

## 7. New shape family: countably accumulating bounded-variation webs

Let

\[
g_0,g_1,g_2,\dots:(0,\infty)\to\mathbb R
\tag{7.1}
\]

be deterministic continuous functions, locally of bounded variation, satisfying the local summability condition

\[
\boxed{
\forall\ 0<a<b<\infty:\quad
\sum_{n=0}^\infty\operatorname{Var}_{[a,b]}(g_n)<\infty.
}
\tag{7.2}
\]

Assume also that the resulting space-time set

\[
\boxed{
\mathcal W_{\mathbf g}
=
\{(-u,g_n(u)):u>0,\ n\ge0\}\cup\{(0,0)\}
}
\tag{7.3}
\]

is closed. A convenient sufficient seam condition is that every fiber `{g_n(u):n>=0}` is closed and

\[
\sup_{n\ge0}|g_n(u)|\longrightarrow0\qquad(u\downarrow0).
\tag{7.4}
\]

No local finiteness of the web is assumed. Infinitely many sheets may accumulate at a selected leaf at every time, and crossing sets may be infinite.

## 8. Brownian finite-variation obstruction

For standard Brownian motion `B` on `[0,1]`, define dyadic quadratic-variation sums

\[
Q_k(B)=\sum_{j=0}^{2^k-1}
\left(B_{(j+1)2^{-k}}-B_{j2^{-k}}\right)^2.
\tag{8.1}
\]

The increments are independent `N(0,2^{-k})`, so

\[
\mathbb E Q_k(B)=1,
\qquad
\operatorname{Var}(Q_k(B))=2^{1-k}.
\tag{8.2}
\]

Chebyshev and Borel–Cantelli therefore give

\[
Q_k(B)\to1\qquad\text{a.s.}
\tag{8.3}
\]

On the other hand, if `h` is continuous with finite total variation on `[0,1]`, then

\[
Q_k(h)
\le
\left(\max_j|h((j+1)2^{-k})-h(j2^{-k})|\right)
\operatorname{Var}_{[0,1]}(h).
\tag{8.4}
\]

Uniform continuity makes the maximum increment tend to zero, and hence

\[
Q_k(h)\to0.
\tag{8.5}
\]

Thus

\[
\boxed{
\mathbb P(B\text{ has finite total variation on }[0,1])=0.
}
\tag{8.6}
\]

This is a classical analytic path fact; no finite checker is relevant.

## 9. I0077-R07-T35 — universal obstruction for countably accumulating BV webs

**Theorem T35.** Let `W_g` satisfy (7.1)–(7.3). For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
(-u,X_{-u})\in\mathcal W_{\mathbf g}
\quad\forall u\ge R
\right)=0.
}
\tag{T35}
\]

In particular, no FBM can be confined pointwise to such a countably accumulating web on the entire negative half-line.

### Complete proof

For an integer `M>=1`, define

\[
E_M=
\left\{
X_{-u}\in\{g_n(u):n\ge0\}
\quad\forall u\ge M
\right\}.
\tag{9.1}
\]

The eventual-confinement event in T35 is `\bigcup_M E_M`. Suppose it has positive probability. Then for some deterministic `M`,

\[
q:=\mathbb P(E_M)>0.
\tag{9.2}
\]

Let `S_j` be the witness sequence from the definition of FBM. Since `S_j->-infinity` almost surely, choose one **deterministic witness index** `j` so far to the left that

\[
\mathbb P(S_j>-(M+2))<q/2.
\tag{9.3}
\]

Hence

\[
A:=E_M\cap\{S_j\le-(M+2)\}
\]

has probability at least `q/2>0`.

Fix a sample point in `A` and put

\[
u_0=-S_j.
\]

For `t\in[0,1]`, the corresponding backward-time coordinate is

\[
u=u_0-t\in[u_0-1,u_0]\subset[M+1,\infty).
\]

Define

\[
H(u)=X_{-u},\qquad u\in[u_0-1,u_0].
\tag{9.4}
\]

On `E_M`, `H` is continuous and satisfies

\[
H(u)\in\{g_n(u):n\ge0\}
\qquad\forall u\in[u_0-1,u_0].
\tag{9.5}
\]

The interval is compact, so (7.2) and Lemma 6.2 imply that `H` has finite total variation on `[u_0-1,u_0]`. Therefore the FBM witness path

\[
B^{(j)}(t)
=X_{S_j+t}-X_{S_j}
=H(u_0-t)-H(u_0),\qquad0\le t\le1,
\tag{9.6}
\]

also has finite total variation.

But for this fixed deterministic witness index `j`, Definition 2.1 says that `B^{(j)}` is standard Brownian motion. By (8.6),

\[
\mathbb P(B^{(j)}\text{ has finite total variation on }[0,1])=0.
\tag{9.7}
\]

Since `A` is contained in this zero-probability event, `P(A)=0`, contradicting `P(A)>=q/2`. Therefore every `E_M` has probability zero and so does their countable union. QED.

### Dependence audit

The proof never conditions on the random witness time `S_j`, never assumes it is a stopping time, and never assumes independence between `S_j` and the witness path. The index `j` is chosen deterministically from the convergence `S_j->-infinity` in probability, and the contradiction uses only the unconditional fact that the fixed-index witness path is standard Brownian motion.

## 10. Canonical genuinely infinite example

Define

\[
g_0(u)=0,
\qquad
g_n(u)=2^{-n}\sin(nu),\quad n\ge1.
\tag{10.1}
\]

For any compact interval `[a,b]\subset(0,\infty)`, each `g_n` is smooth and

\[
\operatorname{Var}_{[a,b]}(g_n)
\le\int_a^b n2^{-n}|\cos(nu)|\,du
\le n2^{-n}(b-a).
\tag{10.2}
\]

Since

\[
\sum_{n\ge1}n2^{-n}=2,
\tag{10.3}
\]

we get the exact local budget

\[
\sum_{n\ge0}\operatorname{Var}_{[a,b]}(g_n)
\le2(b-a)<\infty.
\tag{10.4}
\]

The web is closed. If `u_k->u>0` and `g_{n_k}(u_k)->x`, then either a subsequence has fixed `n`, giving `x=g_n(u)`, or `n_k->infinity`, in which case `|g_{n_k}(u_k)|<=2^{-n_k}->0=g_0(u)`. At the seam, using `|sin(nu)|<=nu`,

\[
\sup_{n\ge1}|g_n(u)|
\le u\sup_{n\ge1}n2^{-n}
\le u/2\to0,
\tag{10.5}
\]

so `(0,0)` is the only seam limit.

At every `u>0` and in every spatial neighborhood of the zero sheet there are infinitely many other sheets, because

\[
|g_n(u)|\le2^{-n}\to0.
\]

Thus this web is **not locally finite at any point of the zero leaf**. It also has abundant crossings: every nonzero sheet has infinitely many zeros. T35 gives the explicit conclusion

\[
\boxed{
\mathbb P\left(
\exists R:\
X_{-u}\in
\{0\}\cup\{2^{-n}\sin(nu):n\ge1\}
\quad\forall u\ge R
\right)=0
}
\tag{10.6}
\]

for every FBM.

## 11. Why this earns a separate metric point

This is not run 33 with a larger parameter. Run 33 has finitely many sheets; local finiteness is automatic and its proof depends on a positive gap separating inactive sheets from the selected value. The canonical family (10.1) violates that mechanism at **every** time along the zero leaf: infinitely many sheets accumulate there, so the minimum inactive-sheet gap is identically zero.

It is also not run 32's moving Cantor lamination. There is no fixed totally disconnected `K` transported by a single affine map `a(r)K+b(r)`: the relative locations of the leaves in (10.1) have sheet-dependent frequencies `n`. A continuous selector is not forced to preserve a leaf address; it may switch through infinitely many accumulating leaves. The theorem survives because all possible motion has a summable total-variation budget.

Brownian rescaling/reflection/translation cannot turn an infinite, non-locally-finite fiber into a finite one, nor remove the sheet-dependent frequencies. Under the frozen R07 equivalence convention this is therefore a genuinely distinct family.

Metric after theorem T35:

\[
\boxed{33\longrightarrow34},\qquad\text{unchanged count}=0.
\]

## 12. Checks, audits, and status

There is no finite arithmetic core. The only numerical identity used is the elementary convergent series `sum n/2^n=2`; manufacturing a checker for it would violate the new-methods-first policy. The theorem-sized claim is proved on the page.

T35 currently has **0/2 independent OTHER-track audits**. No P26 or second-track audit is claimed. Therefore Problem 7.8 remains **PARTIAL**, not closed, and no `paper_*` package is created.

Publication novelty remains **UNVERIFIED**. The fresh bounded literature search did not locate a later explicit resolution of exact Problem 7.8 or this countable-web theorem, but a negative search is not a novelty certificate.

## 13. Strongest next route

The new theorem identifies a sharp structural boundary for this method: it needs

\[
\sum_n\operatorname{Var}_{[a,b]}(g_n)<\infty
\]

on every compact interval. The next genuinely new question is whether one can construct a deterministic countable web with **divergent total sheet-variation budget** whose continuous selectors can realize nonzero quadratic variation, and then decide whether an FBM can actually use that web. A promising test object is a dyadic multiscale web with amplitudes/frequencies chosen so that individual sheets remain smooth but the aggregate variation diverges at the Brownian `1/2` scale. That would directly test whether the summability threshold is merely sufficient or marks a true roughness transition.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  intake: I0077
  source: Burdzy-Scheutzow Problem 7.8
  fixed_metric: number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem
  before: 33
  after: 34
  movement: "+1"
  unchanged_count_before: 0
  unchanged_count_after: 0
  status_before: PARTIAL
  status_after: PARTIAL
  new_claim: I0077-R07-T35
  new_family: countably accumulating locally summable bounded-variation webs
  audits:
    P26: MISSING
    second_other_track: MISSING
  finite_core: none
  checker: not_applicable
  publication_novelty: UNVERIFIED
  methods: [3, 20, 25]
```

## 15. Model / scheduler control status

The exposed scheduler/task-control surface still provides prompt/title, schedule or start-offset, enabled state, and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus `GPT-6 / maximum` remains a prompt request rather than an enforceable setting here. The repository policy also records historical `You cannot modify this task` errors for P26/P01/P03 in one authorization context; a separate authorized context later succeeded for P26. The legitimate remedy is an authorized owning/admin product surface or platform support that exposes and persists model/reasoning fields and task ownership. There is no appropriate worker-level bypass or duplicate-task workaround. No scheduler change was attempted in this run.
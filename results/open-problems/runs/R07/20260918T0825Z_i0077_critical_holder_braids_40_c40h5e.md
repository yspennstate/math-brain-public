Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `39 -> 40` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate.

# R07 CLOSABLE OUTSIDE — run 40: critical 1/2-Hölder crossing webs and fractal braids

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0726Z_i0077_fractal_dimension_barrier_39_f39d3b.md`,

which moved `38 -> 39` and used moves `#1,#2,#17`. The present triple is different. All thirty Section-B moves have already appeared somewhere in the long I0077 chain, so I do **not** falsely claim that these three numbers are globally unused on the problem; what is new is the route and theorem.

Before new mathematics I reread/recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 chain, especially runs 33 and 39 because the new theorem sits exactly between their regularity/dimension mechanisms;
- the newest neighboring R15 report, `runs/R15/20260918_0726Z_successor_admission_f0111_homogeneous_k2_h52b.md`; it preserves Burdzy–Scheutzow Problem 7.2 / I0076 as `OPEN / PARTIAL / RETIRED-HANDOFF` and is doing unrelated successor screening, so there is no I0077 ownership collision;
- targeted intake/source searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 closure. `QUEUE.md` lists I0077 separately from 7.2 and 7.5. `operations/claims/I0077.md` still reserves this exact target to R07 and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared operational label while following the current owner assignment. The old R07 KPZ route remains preserved in immutable handoff/history and is not reopened. No shared root or peer file is edited here.

The intake JSONL collections are too large to render literally end-to-end through this connector without truncation. The admission reread is therefore honestly targeted: exact I0077 source text, ownership, exclusions, current neighboring state, and relevant prior attempts were recovered; I do not claim a byte-for-byte reread of every unrelated intake row.

Entering metric: **39**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

I reopened the primary PDF on 2026-09-18 and rechecked Definition 2.1, Definition 2.2, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` a.s. such that for every **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces stopped at finite stopping times.

For the static parabolic normalized interval `[c_1,c_2]`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the source's universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM confined pointwise to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh 2026-09-18 literature/current-status pass

A bounded fresh search covered:

- exact `"Forward Brownian Motion" "Problem 7.8"` and the exact “other space-time shapes” wording;
- Burdzy/Scheutzow together with Hölder curves and moving boundaries;
- Brownian containment / first-passage results for deterministic Hölder curves;
- the critical `1/2` Hölder exponent for Brownian path geometry;
- exact Hausdorff dimension of the classical Weierstrass graph.

The search recovered the original Burdzy–Scheutzow paper and no accessible later paper explicitly resolving exact Problem 7.8 or stating the finite critical-Hölder web theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

Nearby prior art is real and is not claimed as new. Bass–Burdzy studied Brownian local times on Hölder curves and identified `1/2` as a critical regularity scale for a different local-time problem; Lee proved first-passage density results for locally Hölder boundaries of exponent `>1/2`. Weixiao Shen proved that the classical Weierstrass graph

\[
W_{\lambda,b}(r)=\sum_{n\ge0}\lambda^n\cos(2\pi b^n r)
\]

has

\[
\dim_H\operatorname{graph}(W_{\lambda,b})
=2+\frac{\log\lambda}{\log b}
\]

for every integer `b>=2` and `lambda in (1/b,1)` (Math. Z. 289 (2018), 223–266). The Brownian critical roughness fact used below is elementary and is proved on the page rather than claimed as new.

## 4. Counterexample-first test: can critical rough branch switching fake Brownian roughness?

Run 39 left the exact frontier `dim_H S=3/2`: its Hausdorff-dimension obstruction only excludes deterministic shapes of dimension **strictly less** than `3/2`. Run 33, on the other hand, excludes finite locally Lipschitz crossing webs because every continuous selector is Lipschitz.

A natural way to try to defeat both mechanisms is therefore:

> take finitely many deterministic sheets which are themselves exactly at Brownian graph dimension `3/2`, allow infinitely many mergers and branch switches, and hope that the selector can use those switches to acquire Brownian roughness.

That is the attempted negation this run. It fails for a stronger deterministic reason: a continuous selector of finitely many `1/2`-Hölder sheets is still `1/2`-Hölder. Since Brownian motion is almost surely **not** `1/2`-Hölder, even critical-dimensional branch switching cannot produce an FBM witness segment.

This is not a refutation of Problem 7.8; it is a failed proposed escape route which yields a new source-appropriate impossibility theorem.

## 5. Method #18 — rewrite the stochastic problem as a finite closed-cover selector problem

The key deterministic lemma is independent of probability.

### Lemma 5.1 — finite Hölder selector lemma

Let `I=[a,b]`, let `0<alpha<=1`, and let

\[
g_1,\ldots,g_m:I\to\mathbb R
\]

all be `L`-Hölder of exponent `alpha`:

\[
|g_i(s)-g_i(t)|\le L|s-t|^\alpha
\qquad(i=1,\ldots,m).
\tag{5.1}
\]

If `h:I->R` is continuous and

\[
h(t)\in\{g_1(t),\ldots,g_m(t)\}
\qquad\forall t\in I,
\tag{5.2}
\]

then

\[
\boxed{|h(s)-h(t)|\le mL|s-t|^\alpha\quad\forall s,t\in I.}
\tag{5.3}
\]

#### Proof

For each `i` let

\[
A_i:=\{t\in I:h(t)=g_i(t)\}.
\]

Each `A_i` is closed and `I=\bigcup_i A_i`. Discard empty `A_i`. Form the finite graph on the remaining indices by joining `i` and `j` when `A_i\cap A_j\ne\varnothing`.

This graph is connected. Indeed, if its vertices split into two nonempty graph components `C_1,C_2`, then

\[
U_1:=\bigcup_{i\in C_1}A_i,
\qquad
U_2:=\bigcup_{i\in C_2}A_i
\]

would be disjoint nonempty closed sets whose union is the connected interval `I`, a contradiction.

Fix `s<t`. Choose indices `i_0,i_q` with `s\in A_{i_0}` and `t\in A_{i_q}`. Because the intersection graph is connected, choose a simple graph path

\[
i_0,i_1,\ldots,i_q,
\qquad q\le m-1.
\]

For each `1<=ell<=q`, pick

\[
r_\ell\in A_{i_{\ell-1}}\cap A_{i_\ell}.
\]

At every such junction,

\[
g_{i_{\ell-1}}(r_\ell)=h(r_\ell)=g_{i_\ell}(r_\ell).
\]

Telescope along the sheets and the junctions. The junction points need not occur in chronological order; every pair of points involved lies inside `[s,t]`, so each Hölder increment is bounded by `L|t-s|^alpha`. There are at most `q+1<=m` such increments. Hence

\[
|h(t)-h(s)|\le (q+1)L|t-s|^\alpha\le mL|t-s|^\alpha.
\]

This proves (5.3). `QED`

**Outcome #18: success.** The correct invariant is not a conserved branch label and not Hausdorff dimension alone; it is finite-cover preservation of the critical Hölder modulus.

## 6. Critical Brownian roughness lemma

### Lemma 6.1 — Brownian motion is not `1/2`-Hölder

Let `B` be standard Brownian motion on `[0,1]`. Then

\[
\boxed{\mathbb P(B\text{ is }1/2\text{-Hölder on }[0,1])=0.}
\tag{6.1}
\]

#### Proof

For `M<infinity`, let `H_M` be the event

\[
|B_t-B_s|\le M|t-s|^{1/2}
\qquad\forall s,t\in[0,1].
\]

If `H_M` occurs, then for every dyadic level `n` and every `0<=k<2^n`,

\[
2^{n/2}\left|B_{(k+1)2^{-n}}-B_{k2^{-n}}\right|\le M.
\tag{6.2}
\]

For fixed `n`, the `2^n` normalized increments in (6.2) are independent `N(0,1)`. With

\[
p_M:=\mathbb P(|Z|\le M)<1,
\qquad Z\sim N(0,1),
\]

we obtain

\[
\mathbb P(H_M)\le p_M^{2^n}
\qquad\forall n.
\]

Letting `n->infinity` gives `P(H_M)=0`. A path has some finite `1/2`-Hölder constant iff it belongs to `\bigcup_{M\in\mathbb N}H_M`; hence the union also has probability zero. `QED`

Notice that this is strictly sharper, for the present purpose, than merely knowing Brownian graph dimension `3/2`: a deterministic `1/2`-Hölder graph can itself have exact Hausdorff dimension `3/2`, so a dimension-only contradiction disappears at the frontier.

## 7. Method #3 — prove the run-39 frontier statement for structured critical shapes

### I0077-R07-T45 — critical finite-Hölder-web obstruction

Let `m>=1` and let

\[
g_1,\ldots,g_m:(0,\infty)\to\mathbb R
\]

be deterministic functions which are **locally `1/2`-Hölder**: on every compact `J subset (0,infinity)`, each `g_i|_J` has a finite `1/2`-Hölder constant. Assume also

\[
\lim_{u\downarrow0}g_i(u)=0
\qquad(1\le i\le m),
\tag{7.1}
\]

and define the backward critical web

\[
\mathcal W_{\mathbf g}
=
\{(-u,g_i(u)):u>0,\ 1\le i\le m\}
\cup\{(0,0)\}.
\tag{7.2}
\]

Then for **every** forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal W_{\mathbf g}
\quad\forall u\ge R
\right)=0.
}
\tag{T45}
\]

The sheets may merge, cross, split, coincide on intervals, and have infinitely accumulating crossing sets. No separation or crossing-count assumption is required.

#### Proof

Suppose the event in T45 has positive probability. By a countable union over integer radii there is a deterministic integer `R>=1` such that

\[
E_R:=\{(-u,X_{-u})\in\mathcal W_{\mathbf g}\ \forall u\ge R\}
\]

has probability `p>0`.

Let `S_j` be the FBM witness times. Since `S_j->-infinity` a.s., choose one **deterministic witness index** `j` such that

\[
\mathbb P(A_j)>1-p/2,
\qquad
A_j:=\{S_j+1\le -R\}.
\tag{7.3}
\]

Then

\[
\mathbb P(E_R\cap A_j)\ge p/2>0.
\tag{7.4}
\]

Fix an outcome in `E_R cap A_j` and put `U=-S_j`. For `0<=s<=1`,

\[
S_j+s\le-R,
\qquad
u(s):=-(S_j+s)=U-s\in[U-1,U].
\]

Hence

\[
h(s):=X_{S_j+s}
\in
\{g_1(U-s),\ldots,g_m(U-s)\}
\qquad(0\le s\le1).
\tag{7.5}
\]

For this realized `U`, the interval `[U-1,U]` is a compact subset of `(0,infinity)`. Local `1/2`-Hölder regularity and finiteness of `m` therefore give a finite common constant `L(U)` for all shifted sheets `s\mapsto g_i(U-s)`. Lemma 5.1 with `alpha=1/2` shows that `h` is `1/2`-Hölder with finite constant at most `mL(U)`.

Subtracting the constant `h(0)` preserves the Hölder property. Thus on `E_R cap A_j`,

\[
B^{(j)}(s)=X_{S_j+s}-X_{S_j},\qquad0\le s\le1,
\]

is `1/2`-Hölder with some finite (possibly random) constant.

But the witness index `j` is deterministic, so Definition 2.1 says unconditionally that `B^(j)` is standard Brownian motion. Lemma 6.1 says the event that it has **any** finite `1/2`-Hölder constant has probability zero. This contradicts (7.4). Therefore T45 holds. `QED`

### Dependence audit

No conditioning on `S_j` is used. No independence between `S_j` and `B^(j)` is asserted. The proof only selects one deterministic witness index using `S_j->-infinity` in probability and then applies an unconditional probability-zero path property of the standard Brownian witness at that fixed index.

**Outcome #3: success.** Run 39's strict `dim_H<3/2` barrier is pushed to the exact critical Hausdorff dimension `3/2` for an explicit structured class.

## 8. Method #26 — the sporadic critical case: an exact-dimension `3/2` fractal braid

To show T45 is not merely run 33's smooth finite-web theorem in different notation, I now build a web whose sheets have exact Hausdorff graph dimension `3/2`, are not Lipschitz, and merge/split infinitely often.

Set

\[
\lambda=2^{-1/2},
\qquad
W(r)=\sum_{n=0}^{\infty}\lambda^n\cos(2\pi2^n r).
\tag{8.1}
\]

Shen's theorem gives

\[
\dim_H\operatorname{graph}(W|_{[0,1]})
=2+\frac{\log(2^{-1/2})}{\log2}
=\boxed{\frac32}.
\tag{8.2}
\]

### 8.1 Self-contained `1/2`-Hölder bound for `W`

Let `delta=|x-y|<=1`. Choose `N` so that

\[
2^{-N-1}<\delta\le2^{-N}.
\]

For the low frequencies, using `|cos a-cos b|<=|a-b|`,

\[
\sum_{n=0}^{N}2^{-n/2}
|\cos(2\pi2^n x)-\cos(2\pi2^n y)|
\le
2\pi\delta\sum_{n=0}^{N}2^{n/2}
\le C_1\sqrt\delta.
\tag{8.3}
\]

For the tail,

\[
\sum_{n>N}2^{-n/2}
|\cos(2\pi2^n x)-\cos(2\pi2^n y)|
\le2\sum_{n>N}2^{-n/2}
\le C_2\sqrt\delta.
\tag{8.4}
\]

For `delta>1`, boundedness of `W` gives the same form after increasing the constant. Therefore

\[
|W(x)-W(y)|\le C_W|x-y|^{1/2}
\quad\forall x,y\in\mathbb R.
\tag{8.5}
\]

### 8.2 Physical critical braid

Define for `u>=0`

\[
g_+(u)=\sqrt u\,W(\log(1+u)),
\qquad
g_-(u)=-g_+(u),
\tag{8.6}
\]

with `g_+(0)=g_-(0)=0`, and let

\[
\mathcal B_{\rm crit}
=
\{(-u,g_+(u)),(-u,g_-(u)):u\ge0\}.
\tag{8.7}
\]

These sheets are globally `1/2`-Hölder. Indeed, for `u>=v>=0`, with `A=||W||_infinity`,

\[
|g_+(u)-g_+(v)|
\le
A|\sqrt u-\sqrt v|
+\sqrt v\,C_W
|\log(1+u)-\log(1+v)|^{1/2}.
\]

Now

\[
|\sqrt u-\sqrt v|\le\sqrt{u-v},
\]

and

\[
\log\frac{1+u}{1+v}
\le\frac{u-v}{1+v},
\]

so

\[
\sqrt v
\left(\log\frac{1+u}{1+v}\right)^{1/2}
\le\sqrt{u-v}.
\]

Hence

\[
\boxed{|g_\pm(u)-g_\pm(v)|\le(A+C_W)\sqrt{|u-v|}.}
\tag{8.8}
\]

T45 therefore gives

\[
\boxed{
\mathbb P\left(
\exists R:\ X_{-u}\in\{g_+(u),g_-(u)\}
\quad\forall u\ge R
\right)=0
}
\tag{T46}
\]

for every FBM.

### 8.3 It is exactly critical dimensional

For every integer `k>=1`, on the logarithmic slab `r in [k,k+1]` the map

\[
F(r,y)=\left(-(e^r-1),\sqrt{e^r-1}\,y\right)
\tag{8.9}
\]

is bi-Lipschitz on a compact strip containing the graph of `W`. Therefore each corresponding slab of either physical branch has Hausdorff dimension exactly `3/2` by (8.2). On the other hand, (8.8) gives the standard upper bound `dim_H graph(g_\pm)<=3/2`. Consequently

\[
\boxed{
\dim_H\operatorname{graph}(g_+)
=\dim_H\operatorname{graph}(g_-)
=\dim_H\mathcal B_{\rm crit}
=\frac32.
}
\tag{8.10}
\]

Thus run 39's T43 (`dim_H S<3/2`) is **exactly silent** on this shape.

### 8.4 It genuinely braids: infinitely many mergers and splittings

The function `W` is period one. Also

\[
W(0)=\sum_{n\ge0}\lambda^n=\frac1{1-\lambda}>0.
\tag{8.11}
\]

At `r=1/3`, powers `2^n mod 3` alternate between `1` and `2`, while

\[
\cos(2\pi/3)=\cos(4\pi/3)=-\frac12.
\]

Hence

\[
W(1/3)=-\frac1{2(1-\lambda)}<0.
\tag{8.12}
\]

By continuity there is `r_* in (0,1/3)` with `W(r_*)=0`. Periodicity gives `W(r_*+k)=0` for every integer `k`. At

\[
u_k=e^{r_*+k}-1,
\]

the two physical branches merge exactly. At

\[
v_k=e^k-1,
\]

they are separated by

\[
2\sqrt{v_k}\,W(0)\to\infinity.
\]

So the web repeatedly merges and splits on arbitrarily large scales, and a confined continuous path would be allowed to swap branch identities at infinitely many junctions. T45 says even this critical rough branch-switching mechanism cannot support an FBM tail.

**Outcome #26: success.** The dimension-critical, infinitely pinching case is not an exception.

## 9. Why this earns metric point 40 rather than recounting an old family

The counted family is

> **finite critical `1/2`-Hölder crossing webs**, with a canonical exact-dimension `3/2` two-branch Weierstrass braid that merges and splits infinitely often.

This is not a parameter change inside run 39. Run 39's mechanism applies to **all deterministic sets of Hausdorff dimension strictly below `3/2`** and its canonical skeleton had exact dimension `5/4`. The present canonical web has exact dimension `3/2`, so the run-39 theorem gives no information whatsoever; T45 uses a different invariant, critical Hölder regularity of finite selectors.

It is also not run 33's finite smooth crossing-web family. Run 33 assumes locally Lipschitz sheets, whose graphs have Hausdorff dimension `1`; its Brownian contradiction is zero quadratic variation / Lipschitz roughness. The present sheets have exact graph dimension `3/2` and are at the Brownian Hölder frontier. The new selector lemma is genuinely needed because branch switching among critical rough sheets cannot be handled by the run-33 smoothness argument.

Brownian rescaling, reflection, and constant translation are bi-Lipschitz transformations of space-time and preserve Hausdorff dimension. They cannot turn a `3/2`-dimensional critical braid into the dimension-one smooth webs or the `5/4` run-39 skeleton. Hence the frozen equivalence convention does not identify this family with the earlier ones.

Therefore the metric moves

\[
\boxed{39\longrightarrow40}.
\]

`unchanged_count = 0`.

## 10. Validation and closure bookkeeping

There is no finite combinatorial/arithmetic core in T45/T46. The exact-checker requirement is therefore **N/A**, not evaded; manufacturing a checker would not validate the analytic theorem. The theorem-sized claims are proved on the page.

Independent OTHER-track audits of T45/T46: **0/2**. Therefore:

- theorem-on-page status: `PROVED_ON_PAGE_SELF_CHECKED`;
- source Problem 7.8 status: **PARTIAL**;
- source closure: **not claimed**;
- paper package: **not created**;
- publication novelty: **UNVERIFIED**.

A fresh bounded prior-art search found related Hölder-curve/local-time and moving-boundary literature but no explicit later resolution of exact Problem 7.8 or this theorem. That negative search is not a novelty certificate.

## 11. Next route

The finite-selector lemma shows exactly where this mechanism breaks: **infinitely many critical `1/2`-Hölder sheets**. For countably many sheets, the finite intersection graph may require arbitrarily long chains, so no uniform Hölder constant follows. A genuinely new next route is to impose a scale-dependent branching number `N(delta)` and compare the selector-chain complexity against Brownian's critical modulus

\[
\sqrt{\delta\log(1/\delta)}.
\]

A threshold of the form

\[
N(\delta)=o(\sqrt{\log(1/\delta)})
\]

or another entropy condition may let one push the critical-web obstruction from finite to growing branch complexity. This is only a proposed next route, not a theorem claimed here.

## 12. Model/scheduler control, accurately stated

The model-control limitation remains real. The automation/task control schema exposed to this worker provides task title/prompt, schedule or start offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run routing receipt**. Thus `GPT-6 / maximum` remains prompt text here; this run actually reports `GPT-5.6 Sol / UNVERIFIED` and does not claim otherwise.

Making GPT-6/maximum enforceable would require an authorized product/workspace/API surface that exposes and persists model/reasoning controls and returns trustworthy per-run routing metadata, or a platform change/support action. A repository edit cannot supply those controls.

The historical P26 `You cannot modify this task` result was authorization/context-specific: later repository task-health state records a successful P26 prompt update from a different authorized context. The lawful workaround for any task that still returns that denial is therefore the owning/authorized account or workspace context, an authorized ownership/admin change, or platform support — **not** duplication or permission bypass. This run is expressly prohibited from scheduler changes and attempted none.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  metric_before: 39
  metric_after: 40
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: "finite critical 1/2-Holder crossing webs; canonical exact-dimension-3/2 Weierstrass braid"
  theorem_ids:
    - I0077-R07-T45
    - I0077-R07-T46
  theorem_status: PROVED_ON_PAGE_SELF_CHECKED
  source_status: PARTIAL
  prior_art_status: "bounded fresh search; no explicit later exact resolution found; novelty UNVERIFIED"
  finite_core: N/A
  other_track_audits: "0/2"
  closure: false
  methods: [3, 18, 26]
  next_frontier: "countably/increasingly many critical Holder sheets; branch-entropy versus Brownian critical modulus"
```

No shared root or peer file was edited.
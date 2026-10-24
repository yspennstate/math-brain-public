Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `41 -> 42` genuinely distinct nonparabolic shape families; Section-B moves actually used: #1 CHANGE THE CATEGORY, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate.

# R07 CLOSABLE OUTSIDE — run 42: compact-rectangle locally finite critical Hölder webs

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and the frozen metric

The fixed R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative own report is

`runs/R07/20260918T0925Z_i0077_locally_finite_critical_forests_41_lf41.md`,

which moved `40 -> 41` and used methods `#2,#7,#19`. The present triple `#1,#15,#20` is different. All thirty Section-B labels have already appeared somewhere in the long I0077 chain, so I do not falsely claim globally unused numbers; what is new is the route, hypothesis, theorem and concrete shape family.

Before new mathematics I reread/recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 chain, with special attention to runs 18, 32, 34, 39, 40 and 41 because each is a plausible equivalence collision for the present family;
- the newest neighboring R15 report, `runs/R15/20260918_0957Z_successor_admission_f0111_ifra_oneatom_w55c.md`; its old Burdzy–Scheutzow Problem 7.2 / I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF`, and R15 is now doing successor screening, so there is no I0077 collision;
- C29's latest duplicate-exclusion record, which says `proposed_I0077: EXCLUDED_FROM_C29`, `I0077_owner: R07`, and `I0077_claim_status: PENDING_ADMISSION, not READY`;
- targeted intake/attempt/source searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no exact Problem-7.8 closure. The canonical claim still reserves I0077 to R07 and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared operational label rather than inventing `READY`. The old R07 KPZ/FPP route remains preserved by its immutable handoff and is not reopened or deleted. The root `RESULTS.md` R07 row is explicitly a retained stale pre-reassignment value, so the mathematical baseline is the newer immutable R07 report, not the stale root row.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector in one response without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: exact I0077 source, ownership, exclusions, neighboring scope, and prior attempts were recovered; I do not claim a literal reread of hundreds of unrelated intake rows.

Entering metric: **41**.  
Entering unchanged count: **0**.

## 2. Primary source benchmark recovered again

I reopened the primary Burdzy–Scheutzow PDF on 2026-09-18 and rechecked Definition 2.1, Definition 2.2, Theorem 4.3, and the open-problem page.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times tending to `-infinity` such that, for every **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion. This fixed-index, unconditional Brownian property is the only FBM input in the new obstruction theorem below.

For a static parabolic interval `[c_1,c_2]`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The following sentence is Problem 7.9 about forward Lévy processes and is not part of I0077.

The result below is a complete universal-obstruction theorem for a new nonparabolic family, hence source-appropriate progress on the analogue of the universal side of Theorem 4.3. It is **not** a three-way classification of all shapes, and I do not call Problem 7.8 closed.

## 3. Fresh 2026-09-18 current-status / prior-art pass

A fresh bounded search used, among others, the queries

- `"Forward Brownian Motion" Burdzy Scheutzow "Problem 7.8" "space-time shapes"`;
- `"Forward Brownian Motion" Burdzy Scheutzow citations 2025 2026 Problem 7.8`;
- `"Brownian motion" "Hölder curve" countable union graph local finiteness`;
- `"Brownian motion" graph deterministic Hölder curves "1/2"`;
- `Weixiao Shen Hausdorff dimension Weierstrass graph lambda b theorem`.

The search recovered the original paper and its publication pages, but no accessible later source explicitly resolving exact Problem 7.8 or stating the compact-rectangle-locally-finite critical-web theorem below. This is **bounded negative evidence only; publication novelty remains UNVERIFIED**.

Nearby prior art is substantial and is not claimed as new. Bass–Burdzy study Brownian local times on Hölder curves and identify `1/2` as a critical regularity scale for a different local-time problem; Lee studies first-passage densities through Hölder boundaries above exponent `1/2`; Peres–Sousi study Brownian motion with deterministic Hölder-`1/2` drift. For the concrete Weierstrass example below, Weixiao Shen proved that the classical function

\[
W_{\lambda,b}(x)=\sum_{n\ge0}\lambda^n\cos(2\pi b^n x)
\]

has graph Hausdorff dimension

\[
2+\frac{\log\lambda}{\log b}
\]

for every integer `b>=2` and `lambda in (1/b,1)` (arXiv:1505.03986; later published in *Math. Z.*). The topological finite-selector mechanism used below may be folklore; I do not claim that mechanism by itself as novel.

## 4. Method #20 — find exactly why run 41's algorithm fails

Run 41 assumed **time-local finiteness**: every compact age interval meets only finitely many sheet domains. Its proof therefore began a Brownian witness window `[U-1,U]` with a finite list of possible sheets.

The next natural family defeats that step completely. Imagine countably many critical sheets present for **every** age `u>0`. Then every compact age interval meets infinitely many domains, so the run-41 algorithm cannot even form its finite intersection graph.

But a Brownian witness segment has an additional feature that run 41 did not use: over a compact time interval, its **spatial range is compact**. Thus it is unnecessary to demand finitely many sheets in the full vertical cylinder `J x R`. We only need finitely many sheets in every compact rectangle `J x [-M,M]`.

That is the exact repair. It is strictly weaker than time-local finiteness and admits families with infinitely many active branches at each individual time.

**Outcome #20: success.** The failed finite-sheet enumeration can be rescued by clipping to the random compact spatial range of one fixed Brownian witness; the correct deterministic assumption is local finiteness in full age-space, not local finiteness after projecting to age.

## 5. Method #1 — change the category: from a time-indexed family to a locally finite embedded web

### Definition 5.1 — compact-rectangle locally finite critical Hölder web

Let

\[
\{(I_k,g_k):k\in\mathbb N\}
\]

be a countable deterministic family satisfying:

1. every `I_k` is a nonempty closed interval or closed ray relative to `(0,infinity)`;
2. `g_k:I_k->R` is continuous and locally `1/2`-Hölder;
3. the family is **compact-rectangle locally finite**: for every compact age interval `J subset (0,infinity)` and every finite `M>0`,

\[
\boxed{
\#\Big\{k:\exists u\in I_k\cap J\text{ with }|g_k(u)|\le M\Big\}<\infty.
}
\tag{5.1}
\]

Define the backward space-time web

\[
\mathcal W
=
\bigcup_{k\ge1}\{(-u,g_k(u)):u\in I_k\}.
\tag{5.2}
\]

Condition (5.1) says exactly that every compact rectangle in age-space meets only finitely many graph sheets. It does **not** say that only finitely many sheets are active at a given age. Infinitely many, or even countably infinitely many at every age, are allowed provided they escape to spatial infinity locally.

### Lemma 5.2 — bounded-range finite-selector certificate

Let `J=[a,b] subset (0,infinity)` be compact and let `h:[0,1]->R` be continuous. Suppose that for some `U` with `[U-1,U] subset J`,

\[
h(s)\in\{g_k(U-s):U-s\in I_k\}
\qquad(0\le s\le1).
\tag{5.3}
\]

If the web satisfies (5.1), then `h` is `1/2`-Hölder on `[0,1]`.

#### Proof

The continuous image `h([0,1])` is compact, so choose `M<infinity` with

\[
|h(s)|\le M\qquad(0\le s\le1).
\]

Every sheet actually selected by `h` therefore meets the compact rectangle `J x [-M,M]`. By (5.1), there are only finitely many such sheets; call their index set `K` and let `m=|K|`.

For each selected `k`, define

\[
f_k(s)=g_k(U-s)
\]

on the part of `[0,1]` where `U-s in I_k`. Since `J` is compact and `K` is finite, there is a finite constant `L` such that every active `f_k` is `1/2`-Hölder with constant at most `L` on its domain inside `[0,1]`.

Fix arbitrary `0<=s<t<=1`. For `k in K`, let

\[
A_k=\{r\in[s,t]: U-r\in I_k,\ h(r)=f_k(r)\}.
\]

The nonempty `A_k` form a finite closed cover of `[s,t]`. Form their intersection graph: two labels are adjacent when the corresponding closed sets intersect. This graph is connected. Otherwise its vertices split into two nonempty graph components; the unions of the closed sets in the two components would be disjoint nonempty closed subsets whose union is the connected interval `[s,t]`.

Choose an endpoint label `i_0` with `s in A_{i_0}`, an endpoint label `i_q` with `t in A_{i_q}`, and a simple graph path

\[
i_0,i_1,\ldots,i_q,\qquad q\le m-1.
\]

For `1<=ell<=q`, select

\[
r_\ell\in A_{i_{\ell-1}}\cap A_{i_\ell},
\]

and put `r_0=s`, `r_{q+1}=t`. At each junction the two sheets agree with `h`. Telescoping along the sheet path yields

\[
|h(t)-h(s)|
\le
\sum_{\ell=0}^{q}L|r_{\ell+1}-r_\ell|^{1/2}.
\]

The junction times need not be chronologically ordered, but all belong to `[s,t]`; hence every distance is at most `t-s`. Therefore

\[
\boxed{|h(t)-h(s)|\le mL\sqrt{t-s}.}
\tag{5.4}
\]

Since `s,t` were arbitrary, `h` is `1/2`-Hölder. `QED`

This proof is deliberately written with the compact spatial clip first. That is the new step absent from run 41.

## 6. Brownian endpoint roughness, self-contained

### Lemma 6.1 — standard Brownian motion is not `1/2`-Hölder

Let `B` be standard Brownian motion on `[0,1]`. Then

\[
\mathbb P(B\text{ is }1/2\text{-Hölder on }[0,1])=0.
\tag{6.1}
\]

#### Proof

For integer `C>=1`, let `H_C` be the event

\[
|B_t-B_s|\le C|t-s|^{1/2}
\qquad\forall s,t\in[0,1].
\]

If `H_C` occurs, then at dyadic level `n`, all `2^n` normalized increments satisfy

\[
2^{n/2}|B_{(j+1)2^{-n}}-B_{j2^{-n}}|\le C,
\qquad 0\le j<2^n.
\]

For fixed `n` these normalized increments are independent `N(0,1)`. Writing

\[
p_C=\mathbb P(|Z|\le C)<1,
\]

we obtain

\[
\mathbb P(H_C)\le p_C^{2^n}\longrightarrow0.
\]

Thus `P(H_C)=0` for every integer `C`, and a countable union over `C` proves (6.1). `QED`

## 7. Main theorem — infinitely many critical sheets may be active at every time

### I0077-R07-T49 — compact-rectangle locally finite critical-web obstruction

Let `mathcal W` be a compact-rectangle locally finite critical Hölder web in the sense of Definition 5.1. Then for **every forward Brownian motion** `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal W
\quad\forall u\ge R
\right)=0.
}
\tag{T49}
\]

#### Proof

Suppose the displayed event has positive probability. By a countable union over integer radii, choose a deterministic integer `R>=1` such that

\[
E_R:=\{(-u,X_{-u})\in\mathcal W\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be the FBM witness sequence from Definition 2.1. Since `S_j -> -infinity` almost surely along the witness sequence, choose one **fixed deterministic witness index** `j` so far to the left that

\[
\mathbb P(S_j\le -R-1)>1-p/2.
\tag{7.1}
\]

Therefore

\[
\mathbb P(E_R\cap\{S_j\le-R-1\})\ge p/2>0.
\tag{7.2}
\]

Fix an outcome in this intersection and put

\[
U=-S_j,\qquad h(s)=X_{S_j+s},\quad0\le s\le1.
\]

Then `U>=R+1`, and for every `s in [0,1]` the age `U-s` is at least `R`. Hence confinement gives

\[
h(s)\in\{g_k(U-s):U-s\in I_k\}.
\]

The interval `[U-1,U]` is compact and the path `h([0,1])` is compact. Lemma 5.2 therefore implies that `h` is `1/2`-Hölder. Subtracting the constant `h(0)=X_{S_j}` does not change this property, so

\[
B^{(j)}(s)=X_{S_j+s}-X_{S_j},\qquad0\le s\le1,
\]

is `1/2`-Hölder on this outcome.

But `j` was chosen deterministically. Definition 2.1 says that the entire process `B^{(j)}` is, **unconditionally**, standard Brownian motion. By Lemma 6.1 the event that its restriction to `[0,1]` is `1/2`-Hölder has probability zero. This contradicts (7.2).

No conditioning on `S_j` was used, and no independence between the witness time and witness path was assumed. `QED`

### Strictness relative to run 41

T49 strictly contains the run-41 locally-finite-in-time theorem: time-local finiteness implies compact-rectangle local finiteness, but the converse fails. The concrete family below has **infinitely many active branches at every age**, so run 41 is literally inapplicable while T49 applies.

## 8. Method #15 — break symmetry deliberately: a critical infinite lattice braid

The general theorem would be a weak metric point if the first example were merely countably many parallel nonintersecting translates, because then a conserved label would trivialize the geometry. I therefore force repeated branch exchanges.

Let

\[
\rho=2^{-1/2},\qquad
W(r)=\sum_{n=0}^{\infty}\rho^n\cos(2\pi2^nr).
\tag{8.1}
\]

For every integer `k`, define

\[
\boxed{g_k(u)=k+2(-1)^k W(u),\qquad u>0.}
\tag{8.2}
\]

and the backward space-time shape

\[
\boxed{
\mathcal L
=
\{(-u,g_k(u)):u>0,\ k\in\mathbb Z\}.
}
\tag{8.3}
\]

### 8.1 Exact `1/2`-Hölder regularity

For `0<delta=|x-y|<=1`, choose `N` with

\[
2^{-N-1}<\delta\le2^{-N}.
\]

For frequencies `n<=N`, the mean-value estimate gives

\[
\rho^n|\cos(2\pi2^nx)-\cos(2\pi2^ny)|
\le 2\pi\delta\,2^{n/2}.
\]

Summing the geometric series over `n<=N` gives `O(sqrt(delta))`. For `n>N`, the crude bound by `2rho^n` gives another `O(2^{-N/2})=O(sqrt(delta))`. For `delta>=1`, boundedness of `W` gives the same estimate after enlarging the constant. Thus

\[
|W(x)-W(y)|\le C\sqrt{|x-y|}
\tag{8.4}
\]

for all `x,y`, and every `g_k` is globally `1/2`-Hölder.

The direct proof is included so that the main obstruction does not depend on any external regularity theorem.

### 8.2 Infinitely many sheets are active at every age, but compact rectangles see only finitely many

Since

\[
\|W\|_\infty\le\sum_{n\ge0}\rho^n
=\frac1{1-2^{-1/2}}=:A<\infty,
\]

we have

\[
|g_k(u)|\ge |k|-2A.
\tag{8.5}
\]

Therefore if `|g_k(u)|<=M` for some `u`, then

\[
|k|\le M+2A.
\]

Only finitely many integers `k` satisfy this bound. Hence the family obeys compact-rectangle local finiteness (5.1).

At the same time, **every integer-indexed sheet is active at every `u>0`**. Thus every age interval, however small, meets infinitely many sheet domains. The time-local-finiteness hypothesis of run 41 fails maximally.

### 8.3 The branches genuinely braid; no conserved integer label survives

Adjacent branches satisfy

\[
g_k(u)-g_{k+1}(u)
=-1+4(-1)^kW(u).
\tag{8.6}
\]

Now

\[
W(0)=\frac1{1-2^{-1/2}}>\frac14.
\tag{8.7}
\]

Also `2^n mod 3` alternates between `1` and `2`, so

\[
\cos(2\pi2^n/3)=-\frac12
\]

for every `n`, and hence

\[
W(1/3)=-\frac1{2(1-2^{-1/2})}< -\frac14.
\tag{8.8}
\]

By continuity there exist `r_+,r_- in (0,1/3)` with

\[
W(r_+)=\frac14,
\qquad
W(r_-)=-\frac14.
\tag{8.9}
\]

Because `W` is `1`-periodic, these crossing levels recur at `r_++m` and `r_-+m` for every integer `m`.

At every `r_++m`, all pairs `(2j,2j+1)` meet. At every `r_-+m`, all pairs `(2j+1,2j+2)` meet. Hence over successive crossing epochs a continuous selector can walk through the integer labels. The web is not a disjoint parallel stack with a conserved branch index; it is an infinite alternating ladder of critical rough curves.

**Outcome #15: success.** Deliberately alternating the parity phase destroys the easy conserved-label proof while retaining compact-rectangle local finiteness.

## 9. I0077-R07-T50 — critical infinite-lattice-braid corollary

For the shape `mathcal L` in (8.3), every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal L
\quad\forall u\ge R
\right)=0.
}
\tag{T50}
\]

This is immediate from T49 and Sections 8.1–8.2.

### Critical fractal geometry of the example

Shen's theorem applied to `b=2`, `lambda=rho=2^{-1/2}` gives

\[
\dim_H\operatorname{graph}(W)
=2+\frac{\log(2^{-1/2})}{\log2}
=\frac32.
\tag{9.1}
\]

Every `g_k` is obtained from `W` by a nondegenerate vertical scaling/reflection and translation, so every branch also has graph dimension `3/2`. A countable union has Hausdorff dimension equal to the supremum of the branch dimensions, hence

\[
\dim_H\mathcal L=\frac32.
\tag{9.2}
\]

Thus the strict dimension-`<3/2` obstruction of run 39 is exactly silent here.

## 10. Frozen-equivalence audit: why family 42 is genuinely new

This point is not a new value of an old parameter.

- **Versus run 41:** run 41 requires finitely many branch domains on every compact age window. Here infinitely many branches are active at every single age. This property is preserved by the frozen time/space rescalings, reflection and constant translation.
- **Versus run 40:** run 40 is a globally finite critical braid. Here every fiber is countably infinite and unbounded, and the global branch set is an infinite alternating ladder.
- **Versus run 34:** that countable web is controlled by a summable bounded-variation budget. The Weierstrass branches here are critical `1/2`-rough graphs, not a summable-BV family; their exact graph dimension is `3/2`.
- **Versus run 39:** that family is ruled out by deterministic shape dimension strictly below `3/2`; this example is exactly critical at `3/2`.
- **Versus run 32:** the moving Cantor lamination has compact uncountable fibers and a conserved Cantor address under its hypotheses. Here the fibers are unbounded countable locally finite lattices, and the alternating crossing pattern allows label migration.
- **Versus run 18:** the parabolic comb has positive-width normalized teeth and a connected-component label conserved along a tail. Here the shape is zero-width, nonparabolic, critical-rough, and adjacent labels repeatedly exchange through crossings.

Brownian rescaling/reflection/constant translation cannot convert “infinitely many active branches at every age, locally finite in compact rectangles, with critical `3/2` branches and recurrent adjacent crossings” into any of these earlier structures.

Therefore the frozen metric moves

\[
\boxed{41\longrightarrow42}.
\]

`unchanged_count = 0`.

## 11. What was actually learned from the three methods

- **#20 FIND WHY THE ALGORITHM FAILS:** the run-41 time-projection finiteness assumption was stronger than the Brownian witness argument needs. The witness itself supplies a compact spatial clip.
- **#1 CHANGE THE CATEGORY:** treating the deterministic family as a locally finite collection of embedded graphs in the two-dimensional age-space plane yields the correct properness assumption (5.1) and the general theorem T49.
- **#15 BREAK THE SYMMETRY ON PURPOSE:** alternating the vertical oscillation by branch parity creates a recurrent infinite braid, preventing the new metric point from collapsing to a conserved-label comb or parallel translate family.

The three moves therefore produced one genuinely new mechanism rather than three cosmetic lemmas.

## 12. Validation / closure accounting

There is no finite combinatorial or arithmetic core in T49/T50, so no checker is warranted. The theorem-sized claim is proved on the page rather than replaced by a script. The only imported exact fact used for the optional fractal-dimension distinction is Shen's published Weierstrass graph-dimension theorem; the `1/2`-Hölder estimate needed for the FBM proof is derived directly above.

Independent OTHER-track audits for T49/T50: **0/2**.

Accordingly:

- T49/T50 status inside this report: **PROVED by R07 self-check, unaudited**;
- exact Problem 7.8 source status: **PARTIAL**;
- publication novelty: **UNVERIFIED**;
- no paper folder is created because the source is not closed under the fleet's two-audit closure standard.

## 13. Strongest next route

The new theorem makes the remaining critical obstruction very precise. Compact-rectangle local finiteness fails exactly when **infinitely many critical sheets can accumulate inside one bounded space-time rectangle**. Run 41 already exhibited a countable affine-selector construction showing that unrestricted accumulation is too much.

The next meaningful target is therefore quantitative rather than topological: for a bounded rectangle and scale `delta`, let `N(delta)` measure the number/entropy of sheet pieces distinguishable at spatial resolution comparable to `sqrt(delta)`. A plausible frontier is to prove that sufficiently slow growth of `N(delta)` forces every continuous selector to obey a modulus smaller than Brownian's critical

\[
\sqrt{\delta\log(1/\delta)},
\]

while a matching rapidly branching web can realize Brownian-scale roughness. That would replace local finiteness by a genuine branch-entropy threshold and would be a qualitatively stronger answer to Problem 7.8.

The next run should not merely weaken (5.1) by another qualitative compactness adjective; it should attack that entropy balance directly.

## 14. Scheduler/model-control status in this run

The requested `GPT-6 / maximum` setting is still **not enforceable from the exposed scheduler control surface available to this worker**. The current task-update interface exposes fields for title, prompt, schedule or start-offset, enabled state, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated applied-model receipt**. Therefore `GPT-6 / maximum` remains prompt text only here, and this report honestly identifies the runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository's current `RESULTS.md` makes an important distinction about the historical P26 `You cannot modify this task` error: P26 was later updated successfully from a different authorized context, while R-series edits were denied in another context. Thus a denial is authorization-context-specific, not evidence of an immutable mathematical or scheduler state. The legitimate remedy for a task that still refuses modification is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support. There is no legitimate worker-side permission bypass or duplicate-task workaround.

No scheduler mutation, permission change, or support request was attempted in this run, consistent with the owner prohibition.

## 15. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  lane: CLOSABLE_OUTSIDE
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  source_status_before: PARTIAL
  source_status_after: PARTIAL
  claim_ids:
    - I0077-R07-T49
    - I0077-R07-T50
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  metric_before: 41
  metric_after: 42
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_actual: [1, 15, 20]
  new_family: "compact-rectangle locally finite critical Holder webs; canonical infinite alternating Weierstrass lattice braid"
  finite_core: none
  exact_checker: not_applicable
  independent_other_track_audits: 0/2
  publication_novelty: UNVERIFIED
  canonical_claim_status: "PENDING_ADMISSION, not READY"
  ownership: "R07 exclusive provisional reservation; C29 excluded"
  next_obligation: "replace compact-rectangle local finiteness by a quantitative critical branch-entropy condition"
```

## 16. Readback obligation

This file is the single immutable R07 report for the run. After creation, it must be read back at its actual creation commit. No receipt-only commit is authorized.

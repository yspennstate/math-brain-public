Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not authenticated GPT-6 maximum. METRIC MOVEMENT:** source yes/no remains **OPEN -> OPEN**; PROB10 class metric moves to a complete proved source-compatible class: vertex-transitive `d`-regular expanders with vanishing LRE constants `c_n` satisfying `c_n^{-3} log log n = o(log n)` have rate-one continuous-time TV cutoff, with window/mixing ratio `O_epsilon((log n)^(-1/2) + [log(1/c_n)+c_n^{-3}log log n]/log n)=o(1)`. Old canonical `W_exp=1/2 provisional` is preserved, not reset or claimed improved. Three nonexhausted approaches compared: **(A) quantitative vanishing-LRE entropy stability — SUCCESS; (B) Chebyshev near-Ramanujan input — PROVED AUXILIARY / prior-art-overlap not counted as new source progress; (C) transitivity-only NBRW collision/Green estimate — FAILED at a precise nonnormality obstruction.**

# PROB10-08 — bounded substantive iteration: the long-range constant may vanish

Repository: `yspennstate/math-open-problems`, branch `master`.

Status: **PARTIAL / SOURCE OPEN / NOT AUDITED**.

## 1. Required continuity and ownership recovery

I did not restart R16 from an old title. Before doing mathematics I read the current owner contract in `operations/PROB10_2026-09-20.md`, the current root `POSTED.md`, and the canonical exclusive claim `operations/claims/I0112.md`.

The mandatory R16 handoff already exists and was recovered:

- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`.

It preserves R16's actual intervening successor H0002 (Christoph–Morawski–Wigderson Q5.1), newest report `runs/R16/2026-09-19T22-44-21Z_h0002-balanced-split-isotonic-leakage_8d31.md`, status PARTIAL, with its exact all-prefix isotonic/KKT obstruction. That work is not overwritten here.

I also recovered the I0112 chain rather than reusing it as if new:

- `runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md` — fixed Cartesian products preserve cutoff; product constructions also show fixed LRE is not necessary. This route is baseline/folklore-level and was not repeated.
- `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md` — synchronous/tensor restricted class; the `1/2` window exponent became provisional and was later recognized as the universal lower floor.
- `runs/R16/2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction.md` — moving-weight/local-Poincare route did not reach the source class.
- `runs/R16/2026-09-16T21-42-29Z_i0112-hecke-information-curvature-obstruction.md` — Hecke/information-curvature route did not give general control.
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` — first hard recovery.
- `runs/R16/2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction.md` — global relaxed sub-commutation is impossible: the optimal factor diverges on the infinite regular tree, with a high-girth finite transfer.

Canonical ownership remains R16 / I0112. The posted Abelian Cayley/product-condition manuscript is explicitly excluded by `POSTED.md` and is not this target.

## 2. Source and current-primary-lead check

Frozen source: Justin Salez, `https://arxiv.org/abs/2508.21055`, Problem 2.3: prove cutoff for every bounded-degree vertex-transitive expander sequence. The convention used below is Salez's rate-one continuous-time SRW semigroup

\[
H_t=e^{t(P-I)}.
\]

Primary lead read in detail this run: Dylan J. Altschuler, `https://arxiv.org/abs/2609.14945v1`, _Long-range expanders: construction and cutoff_. The arXiv record still has only v1, submitted 14 September 2026. A bounded search for a correction/erratum/v2 found none. This is not a claim that no private correction exists.

The exact use of long-range expansion in Altschuler's cutoff proof is now isolated:

1. Lemma 3.2 transfers graph LRE to directed growth on the oriented-edge NBRW state space.
2. Lemma 3.3 converts that directed set growth into near-maximal endpoint entropy.
3. Proposition 3.1 gives `H(K_j(x,.)) >= log n - O(log log n)` at the entropic radius.
4. Lemma 3.4 and the covering-tree radial CLT then use only spectral mixing plus that entropy deficit.

In particular, fixed `c>0` is used to keep the directed-growth survival parameter bounded below. The rest of the proof does not intrinsically require `c` to be fixed.

The current source status remains open in the bounded search. Altschuler himself describes LRE cutoff as intermediate progress between Ramanujan cutoff and the transitive spectral-expander conjecture. Salez's current lecture PDF likewise still states Problem 2.3 as open.

## 3. New idea written before any code

**Idea A:** do not try to deduce Altschuler's fixed LRE from transitivity. Instead quantify his proof with an `n`-dependent LRE constant `c_n -> 0`. If the induced NBRW entropy deficit is still `o(log n)`, the source's continuous-time spectral gap can dissipate that deficit in `o(log n)` extra time, which is enough for cutoff even if the Gaussian `sqrt(log n)` profile is lost.

This is a genuine weakening of the proof hypothesis, not a rephrasing of the fixed-`c` theorem. The calculation reveals a cubic loss `c_n -> a_n ~= c_n^3` at the graph-to-oriented-edge transfer and therefore the explicit threshold

\[
c_n^{-3}\log\log n=o(\log n).
\]

No checker was written before establishing this analytic route.

## 4. Main proved theorem — vanishing LRE still gives cutoff

Fix `d>=3`, let `q=d-1`, and let `G_n` be connected `d`-regular graphs, `|V(G_n)|=n`, with

\[
1-\lambda_2(A_n/d)\ge\gamma>0.
\tag{4.1}
\]

Assume that for some `c_n in (0,1/(16q)]`, every nonempty `S subset V(G_n)` and every integer `r>=0` satisfy

\[
|B(S,r)|\ge\min\left\{\frac{3n}{4},c_n|S|q^r\right\}.
\tag{4.2}
\]

### R16-PROB10-08-C1 — vanishing-LRE continuous-time cutoff

There is a constant `C_d` such that if

\[
D_n:=C_d\left(1+\log\frac1{c_n}+c_n^{-3}\log\log n\right)=o(\log n),
\tag{4.3}
\]

then the rate-one continuous-time SRW has TV cutoff at

\[
T_n=\frac d{d-2}\log_q n.
\tag{4.4}
\]

More quantitatively, for every fixed `epsilon in (0,1/2)`,

\[
|t_{mix}^{(n)}(\epsilon)-T_n|
\le C_{d,\gamma,\epsilon}\left(\sqrt{\log_q n}+D_n+1\right),
\tag{4.5}
\]

and hence

\[
\boxed{
\frac{t_{mix}(\epsilon)-t_{mix}(1-\epsilon)}{t_{mix}(1/2)}
=O_{d,\gamma,\epsilon}\left((\log n)^{-1/2}+\frac{\log(1/c_n)+c_n^{-3}\log\log n}{\log n}\right)=o(1).
}
\tag{4.6}
\]

This theorem does not require transitivity. Its vertex-transitive subfamily is a complete source-admissible graph class and is the class-metric movement of this run. It is still only PARTIAL relative to Salez Problem 2.3.

### Proof, Step 1: graph growth -> oriented-edge growth, with constants retained

Let `Omega={(u,v):u~v}`, `N=dn`, and `Q` be the oriented-edge NBRW. Define

\[
k_n=\min\left\{k\ge1:q^{-k}\le\frac{c_n(q-1)}2\right\}.
\]

Running Altschuler's Lemma 3.2 without freezing `c` gives

\[
|B_\Omega(F,r)|\ge a_n\min\{N,|F|q^r\},
\qquad
a_n=\frac{c_n}{2d q^{2k_n}}.
\tag{4.7}
\]

The proof is unchanged but the dependence matters. If `C` is the set of terminal vertices reached by time `2k_n` and `U` those not reached at positive time, the no-backtracking concatenation argument gives

\[
|U|\le q^{-k_n}|C|\le\frac{c_n(q-1)}2|C|.
\]

For `|C|q^ell<=n`, graph growth minus the exceptional endpoints gives

\[
|B_\Omega(F,2k_n+\ell)|\ge\frac{c_n}{2}|C|q^\ell
\ge\frac{c_n}{2d}|F|q^\ell.
\]

The first saturated radius gives at least `c_n n/(2q)` states and larger radii follow by monotonicity; radii below `2k_n` use `|B|>=|F|`. This proves (4.7).

Since `c_n<=1/(16q)`, minimality of `k_n` gives

\[
q^{-k_n}>\frac{c_n(q-1)}{2q},
\]

so

\[
\boxed{a_n\ge A_dc_n^3,\qquad A_d=\frac{(q-1)^2}{8dq^2}.}
\tag{4.8}
\]

This cubic loss is the main quantitative obstruction exposed in this run.

### Step 2: directed growth -> endpoint entropy

Put

\[
\delta_n=\frac{a_n(q-1)}{2q}.
\]

Choose `C_{0,n}` satisfying both

\[
q^{-C_{0,n}}\le\frac{a_n(q-1)}2
\]

and the fixed `d`-dependent amount needed so that

\[
h_n:=\lfloor\log_q(dn)\rfloor-C_{0,n}\le j_n-1,
\]

where `j_n` is the least integer with `d q^{j_n-1}>=n`.

Altschuler's forest induction (his Lemma 3.3) is finite-`n` and pointwise in `(a,q)`, so it applies with `a=a_n`. From one oriented edge,

\[
H(Q^{h_n}(e,\cdot))
\ge h_n\log q-\delta_n^{-1}\log(qh_n+1).
\tag{4.9}
\]

Entropy is nondecreasing under the doubly stochastic `Q`. A vertex-started NBRW first chooses one of `d` oriented edges and forgetting the predecessor costs at most `log d`. Hence, uniformly in `x` and all `j>=j_n`,

\[
H(K_j(x,\cdot))\ge\log n-D_n',
\tag{4.10}
\]

with

\[
D_n'\le C_d\left(1+\log(1/c_n)+c_n^{-3}\log\log n\right).
\tag{4.11}
\]

This is the exact quantitative replacement for Altschuler's `O(log log n)` entropy deficit.

### Step 3: continuous-time entropy dissipation uses only the one-sided source gap

Let `mu` be a law and `f=mu/pi`, where `pi` is uniform. For `mu_t=mu H_t`,

\[
-\frac d{dt}\operatorname{Ent}_\pi(f_t)=\mathcal E_P(f_t,\log f_t).
\]

The pointwise inequality

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2
\]

and Poincare give

\[
\mathcal E_P(f_t,\log f_t)
\ge4\gamma\operatorname{Var}_\pi(\sqrt{f_t})
\ge4\gamma\|\mu_t-\pi\|_{TV}^2.
\tag{4.12}
\]

The last inequality follows from Cauchy-Schwarz:

\[
\|\mu-\pi\|_{TV}^2\le\operatorname{Var}_\pi(\sqrt f).
\]

Since TV decreases along the semigroup, integration gives the explicit bound

\[
\boxed{
\|\mu H_s-\pi\|_{TV}
\le\sqrt{\frac{\log n-H(\mu)}{4\gamma s}}.
}
\tag{4.13}
\]

Thus an endpoint law with deficit at most `D_n'` becomes `epsilon/2`-mixed after

\[
s_{n,\epsilon}=\frac{D_n'+1}{\gamma\epsilon^2}.
\tag{4.14}
\]

This is where the source's continuous-time convention helps: no lower bound on the smallest eigenvalue is required, unlike Altschuler's non-lazy discrete theorem.

### Step 4: covering tree gives the window

Let `R_t` be the radius of rate-one continuous-time SRW on the infinite `d`-regular tree. Conditional on `R_t=j`, projection to `G_n` has law `K_j(x,.)`, hence

\[
H_t(x,\cdot)=\sum_{j\ge0}\Pr(R_t=j)K_j(x,\cdot).
\tag{4.15}
\]

Away from zero, radial increments are `+1` with probability `q/d` and `-1` with probability `1/d`, with drift `v=(d-2)/d`. The number of visits to zero is a.s. finite. Poissonizing the iid increment walk gives

\[
\frac{R_t-vt}{\sqrt t}\Rightarrow N(0,1).
\tag{4.16}
\]

For the upper bound, split the semigroup at time `s_{n,epsilon}`. Every term with `j>=j_n` is within `epsilon/2` by (4.10)–(4.14); the remaining mass is `Pr(R_{t-s}<j_n)`. The CLT makes that probability at most `epsilon/2` by time

\[
T_n+C_\epsilon\sqrt{\log_q n}+s_{n,\epsilon}.
\]

For the lower bound, use the ball of radius `L_n-a\sqrt{L_n}`. Its stationary mass is `O(q^{-a\sqrt{L_n}})=o(1)`, while the radial CLT puts mass at least `1-epsilon` inside it at time `T_n-C_\epsilon\sqrt{L_n}`. This proves (4.5)–(4.6) and C1.

The full expanded proof is also archived at

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T00-12-25Z_vanishing-lre-entropy-proof_6e4b.md`

(created in commit `55644ca8ddd02999d29ddd9f114ccb7079b7a1b6`).

## 5. Approach B — spectral Chebyshev input: useful, but not counted as prior-art-cleared source movement

I next asked whether the decaying-LRE theorem could be fed by a purely spectral hypothesis just above the Ramanujan interval.

Suppose all adjacency eigenvalues other than `d` and a possible bipartite `-d` obey

\[
|\lambda|\le2\sqrt q\cosh\theta_n.
\tag{5.1}
\]

Altschuler's first-kind Chebyshev polynomial now has mean-zero norm at most `2q^{r/2}e^{r\theta_n}` instead of `2q^{r/2}`. The exact same support/Cauchy-Schwarz calculation yields, uniformly also in the bipartite case after using his `(x+d)F_{r-1}/(2d)` modification,

\[
|B(S,r)|\ge\min\left\{\frac{3n}{4},\frac1{16q}e^{-2r\theta_n}|S|q^r\right\}.
\tag{5.2}
\]

If `L_n=log_q n` and

\[
\theta_nL_n\le\beta\log L_n,
\qquad \beta<1/12,
\tag{5.3}
\]

then for all radii one can take

\[
c_n=(16q)^{-1}e^{-4\theta_nL_n},
\]

which gives

\[
D_n=O_d(L_n^{12\beta}\log L_n)
\]

and therefore

\[
\frac{w_n(\epsilon)}{t_{mix}(1/2)}
=O_{d,\epsilon}\left(L_n^{-1/2}+L_n^{12\beta-1}\log L_n\right)=o(1).
\tag{5.4}
\]

This sanity-check is valuable because it independently reproduces the cubic-loss threshold. **I do not count (5.3) as a novelty-cleared new source class.** Salez's survey already says positive results extend to `(near-)Ramanujan` graphs, and the bounded search this run did not completely delimit those existing near-Ramanujan theorems from (5.3). It is retained as an auxiliary input calculation only.

## 6. Approach C — direct transitivity/Green-function attack, and the exact obstruction

A more ambitious route would bypass all volume growth and control NBRW endpoint collision entropy directly. For the oriented-edge chain `Q`,

\[
\sum_f Q^j(e,f)^2=(Q^jQ^{*j})(e,e).
\tag{6.1}
\]

Thus a transitivity-based estimate of the form

\[
(Q^jQ^{*j})(e,e)\le N^{-1}\exp(o(\log n))
\tag{6.2}
\]

at the entropic scale would imply near-maximal Renyi-2 entropy, hence Shannon entropy, and feed the continuous-time argument above.

I tried to derive (6.2) from the vertex-walk spectral gap plus transitivity. The obstruction is precise: `Q` is generally **nonnormal**, so the eigenvalue control of the reversible vertex operator `P` does not control the singular transient `Q^jQ^{*j}`. Transitivity makes the diagonal in (6.1) uniform over oriented-edge orbits only when the relevant edge action is sufficiently transitive; ordinary vertex transitivity does not diagonalize `Q` or bound its singular values. The old Hecke/information-curvature route did not supply this missing estimate, and the tree sub-commutation report already rules out replacing it by a uniform global curvature contraction.

So the genuinely source-level missing statement exposed here is not “prove another spectral-gap lemma”; it is a nonnormal NBRW collision/entropy estimate that uses symmetry beyond the ordinary Poincare inequality without assuming fixed LRE.

No theorem was retained from Approach C.

## 7. Falsification and sanity checks

I actively checked the successful route against the obvious failure modes.

1. **Fixed `c` limit.** If `c_n=c>0`, (4.11) becomes `D_n=O(log log n)`, and (4.5) recovers the `sqrt(log n)` scale of the Altschuler mechanism in continuous time.
2. **Power-log loss.** If `c_n=(log n)^{-alpha}`, then `D_n=O((log n)^{3alpha}log log n)`. The proof gives cutoff for every `alpha<1/3`; it keeps a `sqrt(log n)`-order window only for the smaller range `alpha<1/6` (up to the logarithmic factor). This matches the cubic transfer loss and prevents an accidental claim that arbitrary `c_n->0` is harmless.
3. **Spectral expansion alone does not imply the needed growth.** Altschuler's Section 2.3 gives a transitive/spectral-expander construction from two copies joined by counterpart edges which is not fixed-LRE. Thus the successful theorem does not secretly solve Salez Problem 2.3 by combining transitivity with the gap.
4. **Continuous-time periodicity.** The proof deliberately uses entropy dissipation for `exp(t(P-I))`, so bipartite `-1` eigenvalues decay at rate 2 rather than creating a discrete-time obstruction. No silent lazy/non-lazy convention swap occurs.

No finite computational core was introduced, so no exact-arithmetic checker was run. The only “tests” were theorem-level limiting/special-case checks above plus the current-primary-source and correction searches.

## 8. Prior-art boundary

Fresh bounded checks this run included:

- Altschuler `arXiv:2609.14945v1`: only v1 found; fixed-degree fixed-`c` LRE cutoff with Gaussian profile.
- Salez `arXiv:2508.21055` / current lecture PDF: Problem 2.3 remains stated open; the survey notes positive `(near-)Ramanujan` cases.
- Bordenave–Lacoin, `arXiv:1812.06769`: covered-expander/entropic-time results, including random lifts under their spectral hypotheses.

I did **not** find the exact vanishing-LRE quantitative statement (4.3)–(4.6) in this bounded search. That absence is not a novelty certificate. Before paper-level novelty claims, this theorem needs a systematic prior-art comparison and independent proof audits.

## 9. Metric accounting

### Source-level

- Before: Salez Problem 2.3 OPEN.
- After: Salez Problem 2.3 OPEN.
- No counterexample found.
- No closure/audit claim.

### PROB10 class-and-window metric

- Before this refocus run: published fixed-constant LRE class is baseline; prior R16 `W_exp=1/2 provisional` on a restricted synchronous/tensor package is preserved but does not solve the source.
- After: complete analytic theorem C1 for the source-compatible vertex-transitive subclass satisfying (4.1)–(4.3), with explicit ratio (4.6). This is **PARTIAL mechanism/class movement**, not full-source movement.
- `W_exp` remains `1/2 provisional`; the universal `sqrt(log n)` radial floor means there is no honest numerical improvement below it.

### Auxiliary changes

- The near-Ramanujan spectral calculation (5.1)–(5.4) is auxiliary because current literature already contains near-Ramanujan positive results whose exact scope was not exhaustively separated here.
- The NBRW collision identity (6.1) and nonnormality obstruction identify the next source-level target but do not themselves improve the class metric.

## 10. Remaining full-scope gap and next nonrepeating route

The full source gap is now sharply separated from Altschuler's fixed-constant assumption:

> Prove, for every bounded-degree vertex-transitive spectral expander, either (i) an endpoint-information deficit `D_n=o(log n)` for NBRW at the relevant entropic scale, without fixed LRE, or (ii) a different concentration mechanism giving an `o(log n)` mixing window relative to the `Theta(log n)` mixing time.

The cleanest next nonrepeating route is to attack (6.2) using the representation of the oriented-edge chain as a finite-state extension of a transitive Schreier walk, looking for a **window-local singular-value/Green-function estimate**. This is distinct from the exhausted global sub-commutation, moving-weight Poincare, fixed product, and Hecke-curvature routes.

## 11. Structured ledger delta

```yaml
ledger_delta:
  task: PROB10-08
  canonical_claim: I0112
  source: Salez arXiv:2508.21055 Problem 2.3
  status_before: OPEN
  status_after: PARTIAL_OPEN
  source_closed: false
  old_W_exp: "1/2 provisional"
  new_W_exp: "1/2 provisional"
  class_metric_before: "fixed-c LRE is published baseline; prior restricted R16 package provisional"
  class_metric_after: "vertex-transitive spectral expanders with c_n-WLRE and c_n^{-3} loglog n=o(log n)"
  quantitative_ratio: "O_epsilon((log n)^(-1/2) + (log(1/c_n)+c_n^(-3)loglog n)/log n)"
  theorem_label: R16-PROB10-08-C1
  novelty: UNVERIFIED
  independent_audits: 0
  finite_checker: NOT_APPLICABLE_ANALYTIC_CORE
  scheduler_changed: false
```

No email, Drive, public posting, permission change, workflow execution, scheduler edit, force push, or peer-track file edit was performed.

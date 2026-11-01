Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 maximum. SOURCE YES/NO: OPEN -> OPEN. CLASS/METRIC MOVEMENT:** proved a new sufficient class theorem: a fixed-degree spectral-expander sequence `G_n` that graph-covers a fixed-`c` long-range-expander quotient `H_n` with fiber size `k_n` and `log k_n=o(log |G_n|)` has Salez-convention continuous-time TV cutoff, with explicit relative window `O((log N)^(-1/2)+(log k_n+log log |H_n|)/log N)=o(1)`; if `log k_n=o(sqrt(log N))`, the optimal square-root Gaussian profile is recovered. Publication priority and strict separation from every published positive class remain UNVERIFIED. Three approaches compared: **large-LRE quotient / cover entropy transfer (SUCCESS); improving the inherited cubic LRE-transfer loss (ARCHITECTURAL BARRIER); transitivity-only NBRW spectral-density route (PRIOR-ART PRUNE / STILL OPEN).**

# PROB10-08 — a large long-range-expander quotient is enough for cutoff

Repository: `yspennstate/math-open-problems`, branch `master`.

Status: **PARTIAL / SOURCE OPEN / NEW REPOSITORY THEOREM / NOT INDEPENDENTLY AUDITED**.

## 1. Required continuity, source freeze, and consumed updates

I did not restart R16, revive Beck--Fiala, or overwrite the intervening H0002 work. Before research I recovered the controlling and current state:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- canonical parent claim `operations/claims/I0112.md`;
- R16 handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, preserving the actual H0002 successor and its all-prefix isotonic/KKT obstruction;
- historical I0112 product-varentropy, synchronous-tensor, moving-window/Poincare, Hecke-information/curvature, and both stuck-recovery reports;
- preceding PROB10-08 report `runs/prob10_2026-09-20/PROB10-08/2026-09-20T00-12-25Z_vanishing-lre-continuous-cutoff_6e4b.md` and its proof artifact;
- newest related cutoff reports `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T00-00-13Z__line-graph-lre-transfer.md` and `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_03-01-23__line-graph-entropy-transfer.md`.

The latter peer reports prove a line-graph/incidence transfer class outside uniform LRE. I therefore did not duplicate their line-graph theorem. The posted Abelian Cayley/product-condition manuscript remains excluded by `POSTED.md` and is not this target.

Frozen source: Justin Salez, arXiv:2508.21055v1, Problem 2.3 — every bounded-degree vertex-transitive spectral-expander sequence should have TV cutoff. The walk convention here is exactly the source rate-one continuous-time semigroup

\[
H_t=e^{t(P-I)}.
\]

No finite mixing plot is used to infer an asymptotic sequence statement.

## 2. Current primary lead and exact point where LRE enters

I rechecked Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. The current arXiv record still exposes v1; the bounded correction/erratum search found no v2 or correction. That negative search is not a guarantee about unpublished correspondence.

The proof architecture relevant here is:

1. graph LRE is transferred to directed growth on the oriented-edge NBRW state space (Lemma 3.2);
2. directed growth gives near-maximal NBRW endpoint entropy (Lemma 3.3 / Proposition 3.1);
3. spectral mixing dissipates the remaining entropy deficit;
4. the covering-tree radial CLT converts the NBRW entropic radius into the SRW cutoff center/profile.

Altschuler's Proposition 3.1 gives, for a fixed-degree fixed-`c` LRE graph `H` of size `M`, uniformly in the start and every `j` at least the entropic radius,

\[
H(K_j^H)\ge \log M-C_{d,c}\log\log M.
\tag{2.1}
\]

The previous R16 run quantified steps 1-2 when `c=c_n->0`, exposing a cubic `c_n^{-3}` entropy penalty. This run avoids trying to infer LRE for the top graph at all.

## 3. New theorem and exact metric

Let `d>=3` be fixed, `q=d-1`, and `v=(d-2)/d`. Let `(G_n)` be connected simple `d`-regular graphs with

\[
N_n=|V(G_n)|\to\infty,
\qquad 1-\lambda_2(P_{G_n})\ge\gamma>0.
\tag{3.1}
\]

Assume there is a graph covering

\[
\pi_n:G_n\to H_n
\]

onto a connected simple `d`-regular fixed-`c` LRE graph `H_n`, with constant fiber size `k_n`, so

\[
M_n:=|V(H_n)|=N_n/k_n.
\tag{3.2}
\]

### R16-PROB10-08-C2 — large-LRE-quotient cutoff theorem

For every fixed `epsilon in (0,1/2)`, put

\[
L_n=\log_q N_n,
\qquad
T_n=\frac{d}{d-2}L_n.
\tag{3.3}
\]

Then

\[
\boxed{
|t_{mix}^{(n)}(\epsilon)-T_n|
\le C_{d,c,\gamma,\epsilon}
\left(
\sqrt{L_n}+\log k_n+\log\log M_n+1
\right).
}
\tag{3.4}
\]

Consequently, if

\[
\boxed{\log k_n=o(\log N_n),}
\tag{3.5}
\]

then continuous-time SRW has cutoff and

\[
\boxed{
\frac{t_{mix}(\epsilon)-t_{mix}(1-\epsilon)}{t_{mix}(1/2)}
=O_{d,c,\gamma,\epsilon}\left(
(\log N_n)^{-1/2}
+\frac{\log k_n+\log\log M_n}{\log N_n}
\right)=o(1).
}
\tag{3.6}
\]

If additionally

\[
\log k_n=o(\sqrt{\log N_n}),
\tag{3.7}
\]

then on the optimal square-root scale the exact source-convention Gaussian profile is

\[
\boxed{
\sup_x\left|
\|\delta_xH_{T_n+z\sqrt{L_n}}-\pi_n\|_{TV}
-\Phi(-v^{3/2}z)
\right|\to0
}
\tag{3.8}
\]

for every fixed `z in R`.

For Salez Problem 2.3, restrict C2 to vertex-transitive `(G_n)`. The theorem itself does not need transitivity and, crucially, does **not** assume that `G_n` is long-range expanding.

The complete proof is archived in

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T00-47-46Z_large-lre-quotient-entropy-proof_a91e.md`

created at commit `8e6a701d0440ced5129e0225e44396969775dc69`.

## 4. Proof core — exact NBRW entropy transfer through a graph cover

A graph covering is locally bijective. Therefore every nonbacktracking path in `H_n` from `pi_n(x)` lifts uniquely once its starting lift `x` is fixed, and projection maps the uniform NBRW path measure upstairs exactly to the NBRW path measure downstairs:

\[
\boxed{
(\pi_n)_*K_j^{G_n}(x,\cdot)
=K_j^{H_n}(\pi_nx,\cdot).
}
\tag{4.1}
\]

If `Y` has the upstairs endpoint law, the entropy chain rule gives

\[
H(Y)=H(\pi_nY)+H(Y\mid\pi_nY)
\ge H(\pi_nY).
\tag{4.2}
\]

Let

\[
j_N=\min\{j:dq^{j-1}\ge N_n\}.
\]

Since `M_n<=N_n`, `j_N` is at least the quotient entropic radius. Applying Altschuler (2.1) downstairs and then (4.2) gives, for every `j>=j_N`,

\[
H(K_j^{G_n}(x,\cdot))
\ge \log M_n-C\log\log M_n
\]

and hence

\[
\boxed{
\log N_n-H(K_j^{G_n}(x,\cdot))
\le
\Delta_n:=\log k_n+C\log\log M_n+C.
}
\tag{4.3}
\]

The term `log k_n` is the exact worst-case information price of lifting from the quotient. No uniformity inside a covering fiber is assumed.

## 5. Proof core — dissipate quotient-inherited entropy with the top spectral gap

For a law `mu` on `G_n`, write `f=mu/pi_n`. Along the top rate-one semigroup,

\[
-\frac d{ds}D(\mu H_s\|\pi_n)
=\mathcal E(f_s,\log f_s).
\]

Using

\[
(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2,
\]

Poincare with gap `gamma`, and

\[
\|\mu-\pi\|_{TV}^2\le\operatorname{Var}_\pi(\sqrt f),
\]

gives

\[
\boxed{
\|\mu H_s-\pi_n\|_{TV}
\le\sqrt{\frac{D(\mu\|\pi_n)}{4\gamma s}}.
}
\tag{5.1}
\]

Thus every NBRW endpoint law in (4.3) becomes `epsilon/2`-mixed after

\[
s_{n,\epsilon}=O_{\gamma,\epsilon}(\Delta_n+1).
\tag{5.2}
\]

Only the one-sided top spectral gap is used; continuous time avoids a separate near-`-1` obstruction.

## 6. Proof core — radial CLT and the window

Let `R_t` be the radius of rate-one continuous-time SRW on the infinite `d`-regular tree. Universal-cover projection gives

\[
H_t^{G_n}(x,\cdot)
=\sum_j\Pr(R_t=j)K_j^{G_n}(x,\cdot).
\tag{6.1}
\]

The radial process has drift `v=(d-2)/d`; its root-reflection correction is tight, and Poissonization gives

\[
\frac{R_t-vt}{\sqrt t}\Rightarrow N(0,1).
\tag{6.2}
\]

Splitting the semigroup by `s_{n,epsilon}` and using (4.3)-(5.2),

\[
d_{G_n}(t+s_{n,\epsilon})
\le\Pr(R_t<j_N)+\epsilon/2.
\tag{6.3}
\]

At

\[
t=T_n+A\sqrt{L_n},
\]

the first term is at most `epsilon/2` for suitable fixed `A=A(d,epsilon)`. This proves the upper half of (3.4).

For the lower half, at `T_n-A sqrt(L_n)` use the graph ball of radius

\[
L_n-\frac{vA}{2}\sqrt{L_n}.
\]

Its stationary mass is `o(1)` because every `d`-regular ball has size at most `C_dq^r`, while (6.2) places probability at least `1-epsilon` there for suitable `A`. This gives the matching `O(sqrt(L_n))` lower side and proves (3.4)-(3.6).

Under (3.7), `Delta_n=o(sqrt(L_n))`. Choosing an entropy-dissipation time `s_n->infinity` with

\[
\Delta_n/s_n\to0,
\qquad s_n=o(\sqrt{L_n}),
\]

for example `s_n=sqrt((Delta_n+1)sqrt(L_n))`, makes the entropy error `o(1)` without perturbing the radial CLT. The corresponding ball lower bound gives (3.8).

## 7. Why this is not a restated sufficient criterion

C2 has a proved implication from explicit graph-theoretic hypotheses to cutoff. It is not the statement “if endpoint entropy is large then cutoff”: the needed endpoint entropy is itself proved by exact path lifting from a concrete fixed-LRE quotient, and the quantitative fiber penalty and final source-time mixing window are explicit.

It also differs from the preceding R16 vanishing-LRE theorem. That theorem required an LRE inequality on the **top graph itself** and paid the graph-to-oriented-edge cubic loss. C2 permits the top graph to lack any assumed LRE constant; LRE is required only on a quotient of size

\[
M_n=N_n/k_n=N_n^{1-o(1)}.
\]

I do **not** claim that this condition has been proved for every vertex-transitive spectral expander, nor that an explicit subfamily has been cleared against every older positive cutoff theorem. Thus worldwide novelty and strict class separation remain UNVERIFIED.

## 8. Three materially different attacks

### Approach A — large LRE quotient / exact cover entropy transfer: SUCCESS

The theorem above is the retained route. It separates the roles previously played together by LRE: the quotient supplies path entropy; the top graph's ordinary spectral gap supplies entropy dissipation.

### Approach B — improve the inherited `c^3` transfer: NO, PRECISE ARCHITECTURAL BARRIER

Re-reading Altschuler's Lemma 3.2 with the previous R16 constants confirms why the old argument naturally produces a cubic small-`c` loss. To make the exceptional unreached-terminal set negligible one chooses `k` with

\[
q^{-k}\lesssim c.
\]

The same proof pays a `2k` synchronization overhead before applying graph growth, leaving a directed-growth coefficient of scale

\[
cq^{-2k}=\Theta_d(c^3).
\]

Constant optimization inside that exact subtraction architecture therefore does not remove the cubic exponent; one must replace its collision/synchronization step. I did not spend the run manufacturing another checker around this exhausted mechanism.

### Approach C — transitivity-only NBRW collision/spectral density: PRIOR-ART PRUNE, FULL GAP REMAINS

Because vertex transitivity makes diagonals of automorphism-invariant kernels constant, one can try to bound endpoint entropy through the collision probability of NBRW and nonbacktracking polynomial traces. The strongest clean version naturally asks for a Sarnak--Xue-type density bound on nontrivial adjacency eigenvalues. That is already a known positive cutoff regime (Golubev--Kamber and related work), so a theorem merely assuming such spectral density would not be the requested new route to arbitrary spectral expanders.

The genuinely unresolved implication is whether **transitivity plus an ordinary fixed spectral gap alone** forces enough entropic-scale NBRW collision control. This run does not prove that implication.

## 9. Fresh prior-art/current-status check

Altschuler's current arXiv record is still v1, submitted 14 September 2026; no current correction/erratum surfaced in the bounded search. His abstract explicitly places fixed-degree LRE cutoff between Ramanujan cutoff and the still-open transitive spectral-expander conjecture.

I also searched combinations of `graph cover/lift`, `cutoff`, `expander`, `quotient`, `nonbacktracking`, and `entropy`. Older graph-lift literature and covered-expander cutoff results are relevant, but the bounded search did not identify the exact finite-cover entropy theorem C2. This is **not a novelty certificate**. In particular, Bordenave--Lacoin's covered-expander theorem and arithmetic/Sarnak--Xue results must be checked carefully before any publication claim about explicit subfamilies.

Salez Problem 2.3 remains OPEN in the current source/literature check.

## 10. Tests actually run / self-checks

No finite-enumeration claim was introduced, so no numerical checker was manufactured. The mathematical self-checks were:

1. `k_n=1` reduces C2 to the fixed-LRE endpoint-entropy mechanism and reproduces the correct continuous-time center.
2. The entropy inequality has the correct direction by the exact chain rule; no assumption of uniform conditional mass inside fibers is used.
3. The tree normalization gives drift `v=(d-2)/d`, center `d/(d-2) log_{d-1}N`, and continuous-time Gaussian constant `v^(3/2)`.
4. The entropy-dissipation estimate uses only `1-lambda_2>=gamma`; it does not silently impose an absolute spectral gap.
5. The newest NM13/P26 line-graph transfer was consumed and not duplicated: their output graph changes degree/state space and uses incidence kernels, whereas C2 uses same-degree graph coverings and exact NBRW path lifting.

These are self-checks, not independent audits.

## 11. Source before/after and remaining obligation

**Before:** source OPEN. R16 had the vanishing-top-LRE theorem `c_n^{-3}log log n=o(log n)`; the newest peer work also supplied a line-graph restricted class outside uniform LRE. Historical product, tensor, Poincare, group-curvature and tree-subcommutation routes were already consumed or obstructed.

**After:** source remains **OPEN / PARTIAL**. C2 adds a complete graph-cover class with explicit window ratio (3.6) and Gaussian profile regime (3.8). No independent validation or worldwide priority claim exists yet.

The full-scope gap is now:

\[
\boxed{
\text{derive }\log N-H(K_{j_N}(x,\cdot))=o(\log N)
\text{ from transitivity + ordinary spectral expansion alone,}
}
\]

or construct an admissible vertex-transitive expander family for which this information concentration fails strongly enough to prevent cutoff.

C2 shows one concrete obstruction to a counterexample: a source counterexample cannot simultaneously have a uniform top spectral gap and a fixed-LRE graph-cover quotient of size `N^{1-o(1)}`.

## 12. Repository/delivery boundaries

Only this immutable report and its matching PROB10-08 artifact were written. No shared root, peer-track file, scheduler setting, cadence, enablement state, email, Drive object, public post, permission, or workflow was changed.

Structured delta:

```yaml
ledger_delta:
  target: Salez arXiv:2508.21055 Problem 2.3
  source_before: OPEN
  source_after: OPEN
  status: PARTIAL
  mechanism_progress: "proved cutoff from a fixed-LRE graph-cover quotient with subpolynomial fiber entropy"
  proved_class:
    degree: "fixed d >= 3"
    top_gap: "1-lambda_2(P_G) >= gamma > 0"
    quotient: "fixed-c LRE d-regular H_n"
    map: "graph covering G_n -> H_n"
    fiber_cutoff_condition: "log k_n = o(log N_n)"
    gaussian_profile_condition: "log k_n = o(sqrt(log N_n))"
  window_ratio: "O((log N)^(-1/2) + (log k + log log |H|)/log N)"
  publication_novelty: UNVERIFIED
  independent_audits: 0
  finite_checker: NOT_APPLICABLE
  remaining_full_scope_gap: "transitivity + spectral gap -> entropic-scale NBRW information concentration, or a source-valid counterexample"
```

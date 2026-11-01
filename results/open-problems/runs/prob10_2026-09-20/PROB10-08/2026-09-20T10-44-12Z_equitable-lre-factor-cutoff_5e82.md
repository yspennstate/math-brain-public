Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime model/effort selector or telemetry establishes that setting.

# PROB10-08 — equitable LRE-factor cutoff beyond graph coverings

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL for Salez Problem 2.3; PROVED restricted source-admissible class this run; independent validation pending; worldwide novelty UNVERIFIED.**

## 0. Contract, source and continuity

The exact source remains Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the owner-frozen rate-one continuous-time SRW convention
\[
\mathsf H_t=e^{t(P-I)}:
\]
prove cutoff for every bounded-degree vertex-transitive spectral-expander sequence. This is not the posted Abelian Cayley/product-condition target.

The primary new lead remains Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. The fresh 20 September arXiv check still exposes only v1; no v2, correction or erratum surfaced in the bounded check. I re-read the full cutoff proof before using it. Long-range expansion enters exactly before spectral cleanup: Lemma 3.2 transfers LRE to the oriented-edge NBRW state space; Lemma 3.3 converts maximal-rate set growth to Shannon entropy; Proposition 3.1 gives `H(K_j)>=log m-O(log log m)` at and beyond the NBRW entropic radius; Lemma 3.4 then uses ordinary spectral expansion to dissipate that residual entropy deficit. The stronger LRE hypothesis is not inferred from transitivity.

Required repository state was recovered before the new argument:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- canonical claim `operations/claims/I0112.md`;
- preserved R16/H0002 handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`;
- R16 stuck history through `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` and its linked product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature and global/tree-subcommutation failures;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T09-47-50Z_spectral-cancellation-affine-l1_1f6c.md`;
- neighboring P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`, which owns the Green-shell/biregular-halving route;
- neighboring NM13 cutoff history through `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`, which owns the arc/Hodge/reversal/orbit route.

The R16/H0002 successor remains Christoph--Morawski--Wigderson Question 5.1, with the all-prefix isotonic/KKT obstruction preserved. Nothing in this run reassigns or overwrites it.

## 1. Why this is a different method

Several consecutive runs had no numerical `W_exp` movement, and the value `1/2 provisional` is already the possible exponent floor. Another spectral-projector or Green estimate would violate the stuck-method intent. The new route instead asks whether Altschuler's **entropy output can be transferred through a transitive graph factor without requiring a graph covering**.

The answer is yes. A local covering bijection is unnecessary: exact strong lumpability plus equal fibers is enough. This yields a complete source-admissible class and a quantitative window ratio.

## 2. New theorem proved this run

Fix constants `d>=3`, `c>0`, `gamma>0`, `alpha_0>0`. Let `G_n` be finite connected `D_n`-regular vertex-transitive graphs, with uniformly bounded `D_n`, `N_n=|V(G_n)|`, and
\[
1-\lambda_2(P_{G_n})\ge\gamma.
\]
Let `H_n` be fixed-`d`, fixed-`c` long-range expanders on `m_n->infinity` vertices, with SRW matrix `Q_n`, and let
\[
\phi_n:V(G_n)\to V(H_n)
\]
be onto with equal fibers of size
\[
k_n=N_n/m_n.
\]
Assume there is `alpha_n in [alpha_0,1]` such that for every upstairs vertex `x`,
\[
(\phi_n)_*P_{G_n}(x,\cdot)
=(1-\alpha_n)\delta_{\phi_n(x)}+\alpha_nQ_n(\phi_n(x),\cdot).
\tag{2.1}
\]
This is an exact equitable/strongly-lumpable Markov factor. It does not require a local graph-covering bijection and permits internal-fiber edges and repeated projected edge types.

Put
\[
q=d-1,\qquad L_n=\log_qm_n,\qquad
T_n=\frac d{d-2}L_n.
\]
Then for every fixed `epsilon in (0,1/2)`, the proof artifact establishes
\[
\boxed{
 t_{\rm mix}^{G_n}(1-\epsilon)
 \ge \frac{T_n}{\alpha_n}
 -C\frac{\sqrt{L_n}}{\alpha_n}
}
\tag{2.2}
\]
and
\[
\boxed{
 t_{\rm mix}^{G_n}(\epsilon)
 \le \frac{T_n}{\alpha_n}
 +C\frac{\sqrt{L_n}}{\alpha_n}
 +C\bigl(\log k_n+\log\log m_n+1\bigr),
}
\tag{2.3}
\]
with `C=C(d,c,gamma,alpha_0,epsilon)`.

Therefore, if
\[
\log k_n=o(\log m_n),
\]
the top graphs have total-variation cutoff and
\[
\boxed{
\frac{t_{\rm mix}^{G_n}(\epsilon)-t_{\rm mix}^{G_n}(1-\epsilon)}
{t_{\rm mix}^{G_n}(1/2)}
=O\left(
L_n^{-1/2}+\frac{\log k_n+\log\log m_n+1}{L_n}
\right)=o(1).
}
\tag{2.4}
\]
If
\[
\log k_n=O(\sqrt{\log m_n}),
\]
then the window is
\[
\boxed{O(\sqrt{\log N_n})}.
\tag{2.5}
\]
Thus the newly proved class attains the already-frozen R16 exponent floor `W_exp=1/2` in this regime. The numerical metric does not change; the theorem scope does.

## 3. Proof mechanism

Condition (2.1) implies the exact continuous-time factor identity
\[
(\phi_n)_*e^{t(P_{G_n}-I)}(x,\cdot)
=e^{\alpha_nt(Q_n-I)}(\phi_n(x),\cdot).
\tag{3.1}
\]
The lower cutoff edge therefore transfers by total-variation contraction under projection.

For the upper edge, use Altschuler's endpoint-entropy theorem on the quotient. At quotient time
\[
T_n+A\sqrt{L_n},
\]
choose fixed `A=A(epsilon)` so the continuous-time tree radial variable lies beyond the NBRW entropic radius with probability at least `1-epsilon/4`. Conditional on that good radial event, the quotient endpoint is a mixture of NBRW endpoint laws each satisfying
\[
H\ge\log m_n-C_0\log\log m_n.
\]

Disintegrate the upstairs endpoint over its quotient block and the auxiliary radial variable. Equal fibers then give the conditional upstairs entropy deficit
\[
D(\nu\|\pi_{G_n})
\le\log k_n+C_0\log\log m_n.
\tag{3.2}
\]
No path lift or local covering property is used here.

Finally take the upstairs time-one continuous kernel
\[
K=e^{P_{G_n}-I}.
\]
All nonconstant eigenvalues of `K` are positive and at most `e^{-gamma}`, hence its absolute gap is at least
\[
\eta=1-e^{-\gamma}.
\]
Ozawa's entropy-production inequality, in the same form used by Altschuler, gives after integer cleanup time `r`
\[
\|\nu K^r-\pi_{G_n}\|_{TV}^2
\le\frac{4D(\nu\|\pi_{G_n})}{\eta r}.
\tag{3.3}
\]
Taking
\[
r=O_{\gamma,\epsilon}(\log k_n+\log\log m_n+1)
\]
and adding the at-most-`epsilon/4` bad radial mass proves (2.3). The full proof, including the continuous-time radial CLT normalization and the exact conditional coupling, is in the matching artifact.

## 4. Relation to the earlier R16 covering theorem

The earlier `large-lre-quotient` theorem required a same-degree graph covering. The new assumption (2.1) is strictly weaker at theorem level. A graph covering corresponds to the special case `alpha_n=1` with local bijection. Here blocks may have internal edges (`alpha_n<1`) and multiple upstairs edges may induce the same quotient transition.

Altschuler's two-copy `H_m box K_2` spectral-not-LRE example illustrates the difference: projection to `H_m` has a holding component and is not a same-degree graph covering. When `H_m` is chosen LRE, it satisfies (2.1). That fixed product is **not counted as new progress** because R16 already understood products; it is only a witness that the factor theorem is genuinely broader than a cover theorem. The new theorem applies to arbitrary transitive equitable extensions satisfying (2.1), with no product decomposition assumed.

Publication priority is **UNVERIFIED**. A bounded search for cutoff theorems phrased through equitable partitions/lumpings did not surface this exact result, but that is not an exhaustive novelty certificate.

## 5. Two failed alternatives and an obstruction

### A. Quotient TV plus upstairs gap — rejected

Projected cutoff alone does not control the hidden coordinate. Even for bounded-degree expanding product chains, one factor may have mixed while the other retains order-one TV distance. The retained proof therefore transfers **conditional Shannon entropy**, not quotient TV.

### B. Remove the `log k` cleanup price by generic expansion — rejected

There is a structural bounded-degree support obstruction. Starting from at most `N/k` states, after rate-one time `s` and on the event that the Poisson jump count is at most `2s`, the walk is contained in at most
\[
C_D(N/k)D^{2s}
\]
states. For `s<=c_D log k` with small fixed `c_D`, this can occupy vanishing stationary mass while carrying probability bounded away from zero. Thus without extra fiber information a black-box factor theorem cannot generally replace the order-`log k` cleanup by `o(log k)`.

This explains why the polynomial-fiber Haiman affine family from the preceding R16 runs is not solved here: its natural fiber has `k=N^{2/5+o(1)}`, so the factor-entropy loss is macroscopic.

### C. Retained route — equitable-factor Shannon transfer

The precise gain is that Altschuler's long-range expansion is needed only in the quotient that supplies near-maximal NBRW entropy. The top graph may have completely different local geometry, provided it is a source-admissible transitive spectral expander and its hidden block entropy is sublinear in `log N`.

These three approaches are materially different from the exhausted product-varentropy, synchronous-tensor, moving-weight-Poincare, Hecke/curvature and tree-subcommutation routes, and from P26/NM13's currently owned Green-shell and arc/Hodge routes.

## 6. Source before/after

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  scope_movement: true
  new_complete_class: "uniformly gapped bounded-degree vertex-transitive equitable extensions of fixed-degree LRE factors with log fiber=o(log quotient)"
  quantitative_ratio: "O(L^-1/2 + (log k + log log m + 1)/L)"
  square_root_window_regime: "log k=O(sqrt(log m))"
  independent_audits: 0
  worldwide_novelty: "UNVERIFIED"
```

The full source conjecture is not promoted: arbitrary transitive spectral expanders need not have an LRE factor, and the theorem does not derive one.

## 7. Tests actually run

No finite mixing plot, simulation, graph census or finite-size extrapolation was used. The mathematical output is analytic. Source/version searches were used only to verify that Altschuler's current arXiv record remains v1 and to check for obvious direct prior-art overlap; negative search was not treated as proof of novelty.

## 8. Immutable proof artifacts and readback

Full proof artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T10-44-12Z_equitable-lre-factor-entropy-transfer_5e82.md`

created at commit

`3159cb04088581596ee122db4733c6569739c83c`

and read back at that exact commit before this report was written.

Readback caught one harmless symbol mismatch in Section 7: the displayed upstairs time was typeset as Greek `nu_n`, while the following formulas denote the same quantity by `u_n`. The original proof artifact was left immutable and the correction was recorded separately at

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T10-44-12Z_equitable-lre-factor-entropy-transfer_5e82_NOTATION.md`

created at commit

`07fcffd86a7c4c9961d0cc40d0033af721f90446`.

The correction changes no hypothesis, estimate or proof step.

## 9. Remaining full-scope gap

The exact missing source statement is now separated into two regimes.

1. **Small hidden entropy:** solved by Theorem 2.1 whenever a source graph has an exact LRE Markov factor with `log k=o(log m)`.
2. **No such factor / macroscopic hidden entropy:** still open. This includes the Haiman affine stress family under its natural quotient. Here one needs a direct transitivity-based Shannon/hypocoercive estimate, or an admissible counterexample family.

The next nonduplicating source attack should therefore not shave constants in another quotient theorem. It should target the macroscopic-fiber regime by proving that interleaved symmetry refresh destroys conditional information faster than the crude `log k` black-box cleanup, or prove that such a claim fails in a concrete source-admissible family.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, workflow, shared ledger, peer-track file or force push was changed.

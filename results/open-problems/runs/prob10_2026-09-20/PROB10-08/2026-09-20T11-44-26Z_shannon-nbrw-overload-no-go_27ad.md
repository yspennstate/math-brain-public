Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but no authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.**

# PROB10-08 — Shannon NBRW overload obstruction at the actual early mixing threshold

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL for Salez Problem 2.3; substantive mechanism movement; no source closure; no new concrete nonbaseline family promoted this run; independent validation pending; worldwide novelty UNVERIFIED.**

## 0. Contract and continuity

Exact target: Justin Salez, arXiv:2508.21055v1, Problem 2.3 — every bounded-degree vertex-transitive spectral-expander sequence has total-variation cutoff for rate-one continuous-time SRW `H_t=e^{t(P-I)}`. This is not the root-POSTED Abelian-Cayley/product-condition target.

Before research I read/recovered the required state:

- `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`;
- `operations/claims/I0112.md`;
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, preserving the actual R16 successor as Christoph--Morawski--Wigderson Question 5.1 with the all-prefix isotonic/KKT obstruction;
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` and the linked historical I0112 failures: product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature, local-limit/AEP and global subcommutation;
- own immediate predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T10-44-12Z_equitable-lre-factor-cutoff_5e82.md`;
- newest neighboring report found before the write, P26 `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_13-00-56__all-distance-spherical-green-transfer.md`, which owns shell-Green / spherical-spectrum / radial-clock work;
- newest NM13-01 report found, `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T09-13-06Z__growing-automorphism-memory-cutoff.md`, which owns semidirect growing-memory transfer.

No prior route was reset. This run deliberately changes from exact-factor transfer to Shannon-weighted path coalescence.

## 1. Current source boundary

The current full Altschuler proof, arXiv:2609.14945, was re-read. A bounded fresh correction/version search on 20 September 2026 still exposes **v1, submitted 14 September 2026**; no v2 or erratum surfaced.

The exact use of long-range expansion remains:

1. Lemma 3.2: LRE -> maximal-rate set growth on the oriented-edge NBRW state space;
2. Lemma 3.3: set growth -> near-maximal Shannon entropy;
3. Proposition 3.1: `H(K_j(x,.)) >= log n-C log log n` at/after the entropic radius;
4. Lemma 3.4: ordinary spectral gap cleans the residual entropy deficit;
5. covering-tree radial CLT gives the SRW cutoff window/profile.

Thus the right weakening target is the Shannon endpoint deficit itself, not an attempt to derive LRE from ordinary expansion.

## 2. Main new finite-n theorem

For a finite `d`-regular vertex-transitive graph with gap `gamma`, let `K_j(x,.)` be the length-`j` NBRW endpoint law and let `R_t` be the distance of rate-one SRW on the infinite `d`-regular tree. The universal-cover identity is
\[
H_t(x,\cdot)=\sum_j\Pr(R_t=j)K_j(x,\cdot).
\]
Define
\[
\delta_j=\log n-H(K_j(x,\cdot)),
\qquad
A(t)=\mathbb E\delta_{R_t}.
\]
For `epsilon in (0,1/2)`, put `t_-=t_mix(1-epsilon)` and `eta=1-e^{-gamma}`.

The full artifact proves
\[
\boxed{
 t_{mix}(\epsilon)-t_-
 \le
 1+\frac{4}{\eta\epsilon^2}A(t_-).
}
\tag{2.1}
\]

The proof is exact: convexity of relative entropy gives
\[
D(H_{t_-}(x,.)\|\pi)\le A(t_-),
\]
and applying Altschuler/Ozawa entropy production to the positive-spectrum kernel `H_1` yields
\[
\frac{\eta s}{4}\|H_{t_-+s}(x,.)-\pi\|_{TV}^2
\le D(H_{t_-}(x,.)\|\pi).
\]

Therefore
\[
\boxed{
A(t_{mix}(1-\epsilon))=o(\log n)
\Longrightarrow \text{cutoff}.}
\tag{2.2}
\]
The denominator is `Theta(log n)` for bounded-degree expanders, by the bounded-support lower bound and the ordinary spectral upper bound.

This is a source-wide window inequality, not merely a sufficient condition at a guessed cutoff location.

## 3. Shannon path multiplicity and the new counterexample obstruction

Let
\[
D_j=d(d-1)^{j-1}
\]
and let `M_j(x,y)` count length-`j` nonbacktracking paths from `x` to `y`. Altschuler's proof already records the identity
\[
H(K_j)=\log D_j-E\log M_j(x,Y_j).
\]
Equivalently,
\[
\boxed{
\delta_j
=E_{Y_j\sim K_j}\log(nK_j(x,Y_j))
=\log n-\log D_j+E\log M_j(x,Y_j).
}
\tag{3.1}
\]

Combining (2.1) with the universal-tree radial concentration gives the substantive obstruction proved in the artifact:

> **If Salez Problem 2.3 has a counterexample sequence, then after passing to a fixed-degree subsequence there are constants `a,b,C>0` and a fixed `epsilon` such that, at `t_n=t_mix(1-epsilon)`, a radial set of probability at least `b` inside**
> \[
> |j-(d-2)t_n/d|\le C\sqrt{\log n}
> \]
> **has the property**
> \[
> K_j\bigl(x,\{y:M_j(x,y)\ge n^a\}\bigr)\ge b.
> \tag{3.2}
> \]

So non-cutoff cannot be caused merely by rare `L2` spikes. It requires **positive-mass polynomial coalescence of nonbacktracking paths on a positive fraction of the typical shells at the actual early mixing threshold**.

The proof uses: failure of cutoff -> a linear lower bound on `A(t_n)` through (2.1); radial `O(sqrt(log n))` concentration; a threshold argument for the logarithmic likelihood; and the universal tree lower bound `t_n >= (1-o(1)) d/(d-2) log_{d-1} n`, which turns polynomial likelihood overload into polynomial actual path multiplicity.

This is stronger information than merely observing that LRE can fail.

## 4. A concrete weaker entropy target

A convenient contrapositive is also proved. If for some sufficiently large fixed `C_0=C_0(d,gamma)` and every fixed `a>0`,
\[
\sup_{\frac12\log_{d-1}n\le j\le C_0\log_{d-1}n}
K_j\{y:nK_j(x,y)\ge n^a\}\to0,
\tag{4.1}
\]
then the sequence has cutoff.

Indeed, with `L=nK_j(x,Y_j)`,
\[
\frac{\delta_j}{\log n}
\le a+K_j(L\ge n^a),
\]
so (4.1) gives a uniform `o(log n)` Shannon deficit on every shell that can carry the early mixing radial mass; (2.2) then applies.

I record (4.1) as **auxiliary mechanism progress**, not as source-level graph-class progress, because this run does not certify a genuinely new non-LRE family satisfying it. In particular, no product/tensor example is counted.

## 5. Why this differs from the neighboring Green route

For the same shell,
\[
1+\chi^2(K_j\|\pi)
=E_{K_j}[nK_j(x,Y_j)],
\]
whereas
\[
\delta_j=E_{K_j}\log(nK_j(x,Y_j)).
\]
Thus Green/chi-square uses the arithmetic mean of the overload and this run uses its logarithmic/Shannon mean. Jensen only gives
\[
\delta_j\le\log(1+\chi^2).
\]
A vanishing amount of mass can make chi-square polynomial while contributing only `o(log n)` Shannon deficit. This is precisely the unresolved possibility in the Haiman affine stress family after the earlier R16 `L1` work, and is why this run does not duplicate P26.

## 6. Second approach checked — exact radial birth-death is asymptotically vacuous

Ding--Lubetzky--Peres prove that a continuous-time birth-death family has TV cutoff iff `t_rel=o(t_mix)`, with window at most `sqrt(t_mix*t_rel)`. Markowsky records that the distance projection of SRW on a distance-regular graph is exactly a birth-death chain.

The tempting strategy is therefore: use vertex transitivity to make graph distance Markov and invoke DLP. The artifact proves/records the obstruction:

- strong lumpability of the distance partition gives constants `b_i,c_i,a_i` and, under vertex transitivity, exactly distance-regularity;
- Bang--Dubickas--Koolen--Moulton proved the Bannai--Ito conjecture: for each fixed valency `d>2`, only finitely many distance-regular graphs exist;
- a uniformly bounded-degree infinite sequence has a fixed-degree subsequence; degree two gives cycles and no uniform spectral gap.

Therefore **there is no source-admissible asymptotic sequence on which exact radial birth-death reduction can be the missing mechanism**. This route is closed unless the radial reduction is genuinely approximate/weighted.

## 7. Third approach checked — exact tree injectivity is too rigid

A deterministic local-limit/AEP repair would ask the finite graph to agree exactly with its regular-tree cover through the mixing scale. But tree injectivity to radius `r` implies the Moore bound
\[
n\ge1+d\sum_{k<r}(d-1)^k,
\qquad
r\le\log_{d-1}n+O_d(1).
\]
The rate-one tree walk only reaches this radial scale at
\[
\frac d{d-2}\log_{d-1}n
\]
because of backtracking. Thus exact trajectory/word injectivity through the full mixing time is impossible, and even exact endpoint injectivity at the entropic radius is Moore-extremal rather than a general expander feature.

This leaves **typical weighted path coalescence**, rather than deterministic no-collision geometry, as the viable replacement.

## 8. Three-method comparison

1. **Radial-average Shannon NBRW deficit / polynomial typical overload — retained.** New exact finite-n window bound and counterexample obstruction.
2. **Exact distance-radial birth-death — rejected by Bannai--Ito finiteness.** This would otherwise be a powerful DLP route, but is vacuous for bounded-degree source sequences.
3. **Exact tree/local-limit injectivity — rejected as a general mechanism by the Moore/backtracking scale mismatch.** The replacement must be probabilistic/typical, not all-path injectivity.

The work is nonduplicating relative to P26 shell-Green and NM13 growing-memory routes and does not revive the historical I0112 product/Poincare/tensor/curvature failures.

## 9. Source before / after

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
  concrete_new_nonbaseline_cutoff_family_this_run: false
  mechanism_progress:
    - "window <= constant times radial-average NBRW Shannon deficit"
    - "source counterexample must have positive-mass polynomial NBRW path coalescence on typical shells"
    - "typical polynomial-overload absence is a sufficient cutoff criterion"
    - "exact radial birth-death route ruled out by fixed-valency distance-regular finiteness"
    - "exact tree-injectivity/local-limit route ruled out as a general mechanism"
  independent_audits: 0
  worldwide_novelty: "UNVERIFIED"
```

The historical `W_exp=1/2 provisional` is already at the bounded-degree radial-fluctuation floor, so no numerical improvement is claimed.

## 10. Tests actually run

No finite mixing plots, graph enumeration, Monte Carlo simulation, or finite-size extrapolation were used. No code was needed. I did run bounded source/literature checks:

- current full Altschuler v1 proof and correction status;
- Ding--Lubetzky--Peres continuous-time birth-death cutoff theorem;
- Markowsky's exact distance-regular birth-death projection;
- Bang--Dubickas--Koolen--Moulton fixed-valency distance-regular finiteness theorem.

## 11. Matching proof artifact and persistence

Full proof artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T11-44-26Z_shannon-nbrw-overload-no-go_27ad.md`

created at commit

`4a4573f320696a265758fb96b276f283619b4ce4`,

blob

`dbee65b34de609374e89ae851354b909345b07e7`,

and read back at that exact commit before this report write.

## 12. Remaining source gap

The exact next nonduplicating source obligation is now sharper:

> prove that arbitrary vertex-transitive spectral expanders cannot have the positive-mass polynomial NBRW path coalescence in (3.2), or exhibit a source-admissible family where it actually occurs and survives into a non-sharp TV profile.

For the already-isolated Haiman affine family, this becomes a precise question: its polynomial chi-square excess is known, but does that excess sit on vanishing NBRW mass (TV-benign) or on positive NBRW mass (a genuine counterexample mechanism)? The next mathematical attack should address that Shannon/typical-mass dichotomy rather than another global `L2` estimate.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, shared ledger, peer-track file, workflow, or force push was changed.

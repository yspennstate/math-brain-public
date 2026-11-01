# A02 handoff: T336 source recovery and continuous-kernel extension

Status: substantive author proof candidate, not independently audited; T336 is not counted solved by this agent.

## Exact current sources

Located the T001–T422 frontier in `<private-repo>/06_math_research/frontier/rows/`. This is separate from the P/C/D/etc probability registry in math-open-problems. T336's source is `rows/T336/DOSSIER.md`; its original row is in `06_math_research/top200_probability_2026_10_14/list.jsonl` despite that filename. The fetched registry row is saved in T336_REGISTRY.json.

Observed main commit: 7db35f690af10b1ee850623c8caef38d6721a244. File-level blob pins and exact URLs are in COMPLETE_SOURCE_PINS.json. Existing finite-rank proofs C002, C003, C004, C005_v2 are saved beside this report. The exact worker source is `06_math_research/frontier/worker_submissions/w727/T336/proofs/`.

The registry asks for size, number of pretraining datasets, and convergence to the Bayes predictor. The repaired dossier names noisy GP predictions, positive noise, bounded context labels, uniform forward KL, an architecture, and an ERM prior-averaged bound. Its sole numbered Target 1 is finite rank. The Oct21 moves entry reports Target 1 passed; the Oct20 submission STATUS/CLAIMS still say unaudited, so those older labels should not override the later dated move without reviewing its evidence.

## New work

CONTINUOUS_KERNEL_EXTENSION.md contains a complete deterministic theorem for every continuous PSD kernel on compact X subset R^d, including infinite rank. It specifies width, depth, heads, MLP width and dense parameter count, counts the raw-input encoder, and gives uniform scalar errors and forward KL.

The key reduction projects the canonical RKHS feature map onto a finite net's sections. Its PSD residual has uniform diagonal and absolute-entry bound Omega(r0)^2. A kernel-entry perturbation lemma then gives

    |Delta mean| <= [nB/s](1+nS^2/s) a,
    |Delta variance| <= (1+nS^2/s)^2 a

for entrywise kernel error a and diagonal bound S^2. A finite cone ReLU encoder and the exact C002 Chebyshev solver complete the explicit construction. No KL triangle inequality is used.

The RBF specialization uses the classical Gaussian Taylor features centered at the cube midpoint. Retaining total degree <r gives p=binom(d+r-1,d) and residual diagonal <=R^2 U^r/r!, U=d/(4ell^2). A closed choice of r and a Lipschitz-grid encoder yield fully explicit parameters without Mercer eigenfunction or design-measure assumptions.

Output clipping and its exact one-layer implementation are supplied as an interface for A05's ERM proof. A05 separately owns the genuine GP unbounded-label tail and pretraining/generalization argument. That argument is not included or assumed complete here.

## Checks and limits

`python check_extension.py` passes 14,461 counted exact rational/combinatorial assertions in 0.14 seconds, including 150 posterior perturbation examples, infinite-rank Brownian-kernel Nyström projections, RBF multinomial/rank/tail identities, and clipping. The script has no dependencies beyond Python's standard library. The first implementation attempted SymPy, which was unavailable in both Python runtimes; it was replaced by exact Fraction matrix arithmetic. No theorem was changed for this environment issue. Results are in extension_checks.json.

The theorem is an author proof and uses existing C002/C004 exact constructions, which were read and algebraically checked here, not independently re-certified. Finite checks are not a proof. Publication novelty is not established: LITERATURE_REVIEW.md identifies directly relevant GP-transformer, Newton, Taylor-feature, and low-rank attention prior work.

The kernel continuity restriction is essential for this raw-input architecture. C003 already gives a bounded rank-one discontinuous-kernel counterexample. Thus this note cannot honestly be relabeled as the arbitrary-bounded-kernel statement or the complete T336 result. No remote writes, live-store modifications, messages to people, or additional agents were used.

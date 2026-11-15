VERDICT: PARTIAL extended the uniform positive local-road defect bound to all positive Gamma laws and sharpened its exponential constant

The earlier result holds as a literature-discovery claim. The brief new search
found no verified solution of the full continuous-law problem. The September
2026 manuscript's strict-convexity proof remains only partly audited here.

New beyond the earlier report: [PROOF.md](PROOF.md) independently proves the
positive-defect ingredient for the admissible road class, allowing every
Gamma(shape kappa, rate lambda) law with positive parameters. It uses the
stationary dominated calibration supplied by the standard Damron–Hanson
construction under a hypothetical flat face. This external theorem is stated
explicitly and its primary source was opened.

The central improvement is a bounded comparison. If the untouched route has
defect D2, the competing route has defect D1, the perturbation saves v except
on an event of probability q, and its law changes by total variation delta,
then

    E D1 + E D2 >= v(1-q-delta).

This avoids the source's Markov-event loss. With its geometry and the same
two 1/8 error tolerances, the certified exponential lower bound increases
from `a epsilon/(8 CR)` to `3 a epsilon/(8 CR)`. The proof gives explicit
Gamma constants and a checkable condition on the scale. This is an auxiliary
lemma, not strict convexity for Gamma or exponential weights.

Checks: exact Gamma entropy and an independent likelihood second moment give
the required law-change bound; two path counts verify the lower-tail
estimate; integrating tail events verifies the bounded comparison. Random
cuts, repeated traversals, pauses, support separation, and rate scaling are
checked explicitly. No numerical computation or simulation was needed.

Commands used for the earlier files and readback:

```sh
rg --files ~/codex_op_1114/briefs/T050 ~/codex_op_1114r3/briefs/T050
env OMP_NUM_THREADS=1 nice -n 15 cat ~/codex_op_1114/briefs/T050/REPORT.md ~/codex_op_1114/briefs/T050/LOG.md ~/codex_op_1114/briefs/T050/SOLVED_ELSEWHERE.md
env OMP_NUM_THREADS=1 nice -n 15 cat LOG.md PROOF.md
env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
```

The earlier folder contains no PROOF.md or research scripts. All literature
searches and successful paper reads used the web tool. Exact queries and
the mathematical checks are in [LOG.md](LOG.md).

Failures and limits: the direct PDF open initially failed, raw-PDF access was
unsupported, and shell curl failed DNS; the landing page's PDF link worked.
The sandbox rejected the requested nice priority change. No heavy program,
git, external write, subagent, or mutation outside this folder was used.
No error was found in Proposition 9.5's lower-bound argument. Proposition
15.2's statement was read, but its proof and its antecedent estimates have
not been verified. No uncertainty about that proof is resolved by improving
the lower-bound constant.

Next worker: audit the contraction side, beginning with Lemma 10.2's local
potential construction and then the dependence of the output locality and
tracking constants in Sections 15.6–15.7 on s and the auxiliary cutoffs.
The rescaling integer D must be fixed before s is chosen. Establishing a
positive lower bound alone supplies no contradiction.

Primary sources opened:

- OpenAI, *Strict convexity and differentiability of the planar exponential
  first-passage limit shape*, September 24, 2026,
  [manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
  Definition 9.1, Lemma 9.2, Proposition 9.5, Proposition 15.2.
  No arXiv identifier was located for this manuscript.
- Michael Damron and Jack Hanson, *Busemann functions and infinite geodesics
  in two-dimensional first-passage percolation*,
  [arXiv:1209.3036](https://arxiv.org/abs/1209.3036), Section 3.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 01:00:35 Asia/Tbilisi (2026-11-14 21:00:35 UTC;
receipt time not supplied).

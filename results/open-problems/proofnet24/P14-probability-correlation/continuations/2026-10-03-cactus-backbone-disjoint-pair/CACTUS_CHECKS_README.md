# Cactus apex theorem: checks and reproduction

Run from the repository root:

    python cactus_apex_real_rooted_exact.py
    python cactus_apex_real_rooted_k_independent.py

In the archived track the scripts sit beside this file; in the development
workspace they were under `random_cluster_research/`.

The author checker passes 24 exact rational leaf lifts, 12 literal
one-vertex gluing formulas, 24 unicyclic, eight disconnected-pseudoforest
and 12 connected multi-cycle cactus root cases, ten literal marked graphs,
and 78 positive-probability conditionings. It explicitly detects and skips
three forced-cycle zero measures.

The independent checker imports no author helper. It passes 20 normalization
tests, 12 abstract Schur one-sums, 12 literal split-profile one-sums, 12
genuine multi-cycle cactus root cases, one figure-eight marked case, and 64
positive-probability conditionings (32 strict, 32 equality); 17
forced-cycle zero measures are skipped. All arithmetic is exact Fraction,
determinant expansion, literal forest enumeration, and Sturm/gcd root
counting. Numerical roots are not used as proof.

The independent audit records a repaired presentation point: the shared
spoke variable in the one-sum identity must be split into distinct side
variables whose sum is the final shared variable. Reading the same variable
on both sides would double it. The final proof states the split explicitly.

Internal verification is not external peer review or a historical novelty
certificate. The source report states the precise prior-art search and
scope.

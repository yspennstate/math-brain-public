# Hostile-referee audit, 2026-10-12

Verdict: PARTIAL. The full source question is not proved, disproved, or
found solved in print. Missing model parameters are documented rather than
used to claim a trivial solution. None of the results is presented as novel.

1. **Exact source and quantifiers.** Directly read PDF page 9 and its preceding
   Wilson theorem. The broad arbitrary-group question and the embedded
   worst-case alternating-group pair conjecture are distinct. No theorem
   about a subclass was promoted to SOLVED_IN_LITERATURE.
2. **Latest literature.** arXiv, Crossref, Semantic Scholar and GitHub queries
   ran; OpenAlex metadata succeeded but citation/search requests were rate
   limited. Relevant 2024, 2025, 2026 primary texts were inspected. The
   negative search remains qualified and is not proof of openness.
3. **Randomness.** Theorem 1 uses iid uniform generators retaining duplicates;
   the environment is frozen thereafter. It does not apply the same
   independence proof after conditioning. The conditional bound is derived
   separately by division by the generation probability.
4. **Noncommutativity.** Singleton cancellation conditions on all other
   matrices, preserving factor order. Absolute traces of arbitrary products
   are bounded by dimension times operator norm. No cyclic rearrangement
   or commutative expansion is assumed. S3 checks include noncommuting matrices.
5. **Word counting.** Surviving words have at most m indices; binom(k,r)r^(2m)
   overcounts them. The ratio comparison uses k>=m explicitly. This condition
   is not omitted in either the theorem or claims record.
6. **Spectral normalization.** Matrices are contractions in counting L2,
   and passing to uniform-weighted L2 changes only a scalar normalization.
   The initial density-minus-one squared norm is n-1. TV is half the L1 norm;
   both factors of 1/2 and the square root are accounted for.
7. **Generation vs period.** Norm less than 1 rules out both nongeneration
   and a period-two eigenvalue. For the binary formula, spanning is a separate
   conditioning event. Uniform row-space counting uses equal numbers of
   ordered bases per subspace. The all-ones vector is nonzero because k>=1.
8. **Minimal-generator boundary.** k=d implies periodicity probability 1;
   k=d+s fixed implies limiting probability 2^(-s). Laziness removes that
   obstacle but changes the cutoff normalization. For the lazy basis walk
   the slow eigenvalue is 1-1/d, giving (d/2)log d, not (d/4)log d.
9. **Lower bound.** The hypercube statistic has nonpositive pair covariances
   because (1-2/d)^t <= (1-1/d)^(2t), with d>=2. Chebyshev is applied to
   both laws, giving 8d/b^2. Bounds below zero are simply uninformative.
10. **Cycle boundary.** n>=3 keeps the two neighbors distinct. The directed
    one-generator walk is deterministic; it is not conflated with the lazy
    symmetric walk. The log-gap lower bound uses n>=4; n=3 is separate.
11. **Computation.** Integer tuple counts are exact. S3 eigenvalues and TV
    recursions are floating point, explicitly labeled as numerical checks.
    The jobs are seconds in duration and far below the 1 GB limit.
12. **Formal scope.** Four finite counts were Lean kernel-checked. The
    all-group concentration and asymptotic cutoff proofs are paper proofs.
    No whole-theorem formal-verification claim is made.
13. **Remaining gap.** No sharp rate/profile for general sparse random Cayley
    walks is proved. Constant-gap expansion supplies O(log n), and does not
    by itself supply diameter-scale mixing or cutoff. The separate universal
    A_n generating-pair conjecture is untouched.

No unresolved flaw was found in the four stated partial theorems during this
self-audit. This is a self-check, not independent referee certification.

# Classical Fourier entropy–influence research checkpoint

Date: 2026-10-02. Authoring agent: `fei_attempt`.

**Status: the classical FEI conjecture has not been solved in this work.**

All logarithms in the mathematical notes are base 2. Entropy is the Shannon
entropy of the squared, uniformly normalized Fourier–Walsh coefficients.

Files:

- `split_identity_and_obstructions.md`: full derivation of the correct split
  identity; a monotone family with entropy-increment/influence ratio growing
  linearly in the number of tribes; proof that maximum-influence coordinate
  selection also fails after balanced-majority substitution.
- `three_routes.md`: independent candidate approaches, explicit reductions,
  counterexamples to overstrong formulations, and unresolved lemmas.
- `verify.py`: independent Fourier calculations, exhaustive small-function
  checks, and numerical checks of the rigorously proved family.
- `separator_probe.py`, `separator_checks.json`: finite checks of an initially
  plausible separator criterion. These checks did not expose its failure;
  the general construction in §6 of the proof notes disproves it.

Primary literature consulted:

1. González–MacManus–Pereyra, *Further evidence towards the Fourier
   Entropy-Influence conjecture*, arXiv:2606.00246v2 (2026-06-09),
   https://arxiv.org/html/2606.00246v2 . This presents the full conjecture as
   open and asks in §5.1 for a further calculation concerning the actual
   entropy increment of a prescribed split. Our tribe family calculation
   addresses that subsidiary issue, not the full FEI conjecture.
2. Han, *A new bound for the Fourier-Entropy-Influence conjecture*,
   arXiv:2312.08271; Combinatorica 45 (2025),
   https://arxiv.org/abs/2312.08271 .
3. Chakraborty–Kulkarni–Lokam–Saurabh, *Upper Bounds on Fourier Entropy*,
   ECCC TR13-052 revision 2 (2018),
   https://eccc.weizmann.ac.il/report/2013/052/revision/2/download .
4. Chakraborty et al., *Fourier Entropy-Influence Conjecture for Random
   Linear Threshold Functions*, arXiv:1903.11635,
   https://arxiv.org/abs/1903.11635 .

Novelty of the subsidiary obstruction has not yet been established by a
comprehensive literature check. No novelty or breakthrough claim is made.

C0054 statement-only packet for w607 (2026-10-10)

The exact intake statement is: "For d = 2 and fixed band width W, all bulk eigenvectors of the random band matrix on a box of side N are localised with localisation length of order exp(W^2), and the local eigenvalue statistics are Poisson as N -> infinity."

Source record: ~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl, line 54. Primary source: P. Bourgade, Random band matrices, ICM 2018, Conjecture (0.2), printed p. 2, and Section 2.2, printed p. 7; https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf ; arXiv:1807.03031.

Model and quantifier boundaries to recover from the primary source: independent centered entries up to real symmetry or complex Hermitian symmetry; a local variance profile normalized to row sum one; dimension two; fixed W while the side length N tends to infinity. "Order exp(W^2)" must be interpreted as a subsequent large-W assertion, not a limit in N at one fixed W. Fixed-W limiting density and unfolding must not silently be replaced by the Wigner semicircle law. Pure point spectrum, finite-volume eigenvector decay, dynamical localization, and Poisson statistics are distinct claims and need distinct arguments. The precise strong formulation remains to be stated by each proof author rather than attributed verbatim to the survey.

Historical prior attempt: C0054-A001 used fractional moments and reported no bulk proof. No C0054-specific H/I or Lean file was returned by targeted ID searches.

Current status: source describes the localization side as conjectural. Primary arXiv:2609.24426v2, revised 2026-10-06, improves a DELocalization/lower-bound result; the abstract uses exponent 7, replacing indexed v1's 55. This is compatible with localization when W is fixed and the system grows. Present global openness remains UNKNOWN: a bounded check is not an exhaustive novelty certificate. No parent-problem solved claim.

This packet contains no proposed proof, so w607 can independently attack its assumptions and quantifiers.

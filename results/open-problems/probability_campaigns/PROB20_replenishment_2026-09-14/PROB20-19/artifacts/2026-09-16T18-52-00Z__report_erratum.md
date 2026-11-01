# PROB20-19 readback/self-review erratum for `2026-09-16T18-45-00Z__report.md`

This additive erratum preserves the immutable report and corrects one over-broad corollary sentence discovered during post-write self-review. The main Lemma 4.1, Theorem 5.1, and Theorem 6.1 are unchanged.

## Correction to Corollary 6.2

The report says:

> Take any rooted forest on the eigen-directions, orient every edge away from the root, and require eigenvalues to be nonincreasing from each root toward its descendants. Any Givens word that builds each tree by attaching a previously untouched child along a parent-block coordinate is KL-safe, for arbitrary angles.

Edgewise parent-to-child nonincrease alone is **not sufficient** for the hypothesis of Theorem 6.1. If a very small leaf has already been attached on one branch, a later child on another branch may be smaller than its own parent but larger than the minimum eigenvalue already present in the connected component.

The correct corollary is:

> **Corrected Corollary 6.2.** Let a Givens forest be built by adding one fresh eigen-coordinate at a time. If, at every attachment, the fresh eigenvalue is no larger than **every eigenvalue already present in that connected component**, equivalently the introduction order of eigenvalues within each component is globally nonincreasing, then every attachment is nonincreasing for the retained-energy objective and the final basis is KL-safe for arbitrary angles.

Formally, if the current component has eigenvalue-index set `S_t` and the next fresh leaf is `j_t`, require

\[
\lambda_{j_t}\le \min_{k\in S_t}\lambda_k
\]

for every step `t`. This is exactly hypothesis (6.1) of Theorem 6.1, so the proof already written in the report applies verbatim.

No frozen metric, source status, or other theorem statement changes. This correction should be read together with report creation commit `dd59f3cf1497b7e80b55896cc7ca86ee304f868d`.
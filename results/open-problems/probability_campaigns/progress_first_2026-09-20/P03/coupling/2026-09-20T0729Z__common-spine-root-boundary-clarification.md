Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B technical clarification — root boundary for the common-spine occupation lemma

This is a narrow correctness clarification to the immutable report

`probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0715Z__common-spine-occupation-debt.md`

(created at `e152e40cfc696bc434ea4228bc5ccb45ed0c57be`). It does not change the interior-spine estimates, polynomials, or bounded-support examples.

The source model has a special transition rule at the root: from the root all child transitions are equally likely, rather than using `q_k(beta)=1/(1+beta k)`. Therefore Lemma 4.1 and Theorem 5.1 in the `0715Z` report must be read with the following precise boundary convention:

* `Gamma` is the pre-split ancestral geodesic **above the split but excluding the root**, and the occupation/debt estimate is stopped at the first root hit; or, equivalently for the source coupling application,
* the estimate is applied inside the post-root common super-regeneration block, where the source conditioning makes the root visited only once at the initial time.

Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865v1, Remark 3.1 explicitly notes that under the `0-SR` conditioning used for the common regeneration formula, the walks visit the root only once. Thus the root's special transition rule contributes no later reverse-mismatch term in the regeneration-block application.

With that convention, every vertex counted by `N_Gamma` is a non-root vertex and the proof is unchanged:

\[
P(N_\Gamma\ge n)\le(1-s)^{n-1},
\qquad
s=\frac{(d-1)(\beta d-1)}{d(1+\beta d)},
\]

and the two-walk pre-split common-history debt remains

\[
\mathcal D_{\rm common}(\epsilon)
\le 2R_\epsilon\frac{1+r^2}{s},
\qquad r=(\beta d)^{-1}.
\]

No claim is made here about an unconditioned episode that reaches the root and then continues through the root without stopping. The next-attack obligation is unchanged: control post-split self-history off the old common spine with a non-overlapping episode decomposition.

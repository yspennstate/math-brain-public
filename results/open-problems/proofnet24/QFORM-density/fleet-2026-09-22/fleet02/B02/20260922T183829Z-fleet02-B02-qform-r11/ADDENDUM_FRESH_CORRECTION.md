# Fresh correction acknowledgement — QFORM-SEMIPRODUCT-CAP-ONLY-FALSE-v1

After the main report was archived, fresh main added fleet01/B06 event `QFORM-SEMIPRODUCT-CAP-ONLY-FALSE-v1`, brain commit `ffc057e04ed9df6b65103e778ea9e31d11b3a89e`, canonical mathematics `yspennstate/math-open-problems@6674c9a362ec6712140e97eb1e068a3b6f57c7b3`.

The correction refutes an interface that uses only a bounded two-dimensional marginal density plus a conditional scalar density cap for an otherwise dependent semiproduct law. It does **not** invalidate `QFORM-PAIR-HALF-RIESZ-AND-BANK-CASCADE-v1`.

Reason: every bank-level statement in the B02 report assumes the outer bank variables are genuinely independent random variables produced from disjoint original-coordinate banks, and the inner fleet03/B02 packet retains its own explicit product-bank independence. The proof rescales those independent bank variables back to the already-proved cap-one two-coordinate pair theorem; it never replaces product provenance by a generic bounded joint density. Likewise the determinant-bank splice uses the fleet03/B03 weighted Fourier theorem in its stated original-coordinate cross-block scope, not an arbitrary dependent 2D marginal.

So the fresh correction is consumed as a no-go for weakening the hypotheses of Sections 4–6 of the main report. The full QFORM target remains open and the first structural implication is unchanged: derive the required genuinely disjoint product-bank/pair resource from the three-large-eigenvalue geometry, rather than merely a cap-only semiproduct surrogate.

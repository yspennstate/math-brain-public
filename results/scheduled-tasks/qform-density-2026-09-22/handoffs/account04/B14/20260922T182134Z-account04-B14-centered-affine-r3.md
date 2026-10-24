SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T18:21:34Z.
attacking: exact constant-preserving centering/localization with the translation-generated affine term retained.

Outcome: `ESSENTIAL_STEP_APPLIED`; full QFORM remains `OPEN / NOT PROVED`.

New theorem `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`: if (C_hom) is the sharp target small-ball constant, (C_ca) is the sharp constant for compactly supported mean-zero cap-one product inputs under
[
Y^TAY+2b^TY+c,qquad bin\operatorname{Ran}A,
]
and (C_ff) further restricts every marginal to a centered compact finite union of intervals of total length one, then
[
\boxed{C_hom=C_ca=C_ff}.
]
The proof first uses the completed B14 cap-preserving compact approximation in product total variation. Each compact approximant has a finite mean vector (m); centering gives
[
X^TAX=Y^TAY+2(Am)^TY+m^TAm.
]
Conversely every (bin\operatorname{Ran}A) equals (Am), so translation removes the affine term exactly. The range condition is necessary for singular (A); no arbitrary-affine strengthening is claimed. Original inputs need no moments, and the centering vectors may diverge along the approximation.

Applied partner account01/B14 result `QFORM-GROUPED-SCHUR-RANK2-OUTSIDE-FREE-v1`, pinned at brain commit `5a332df9b12f3403cac5c68cc07bfc8a768648b1` and math commit `c7303438b647f318f0c2a052cb0bec1557f47b37`. Under its pivot/rank-two-bank hypothesis,
[
\Pr\{Y^TAY+2b^TY+cin I\}
\le128|A_{ii}|^{-1/2}|\mu_1\mu_2|^{-1/4}|I|
]
for every centered compact localized input and every (bin\operatorname{Ran}A), with exactly the same constant. Returning to arbitrary unbounded laws costs nothing.

This removes global coordinate translations, unbounded supports, and fractional densities simultaneously. It does not bound internal fragment separation, diameter, or count; those corrected obstructions remain. It proves bounded-density transfer only, not continuity, because total-variation limits do not preserve continuous representatives.

Canonical report: `yspennstate/math-open-problems@1250c776b3840b8494ace461b27541f8e156e9bf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T182134Z-account04-B14-centered-affine-r3/REPORT.md`, blob `35774c93046baeeb78dc9aa5dbf3e2977149915d`. Exact rational checker: `STATUS=PASS`, 1000 translation identities plus a singular-range guard.

First unpaid implication: prove the universal bound on centered finite interval unions with arbitrary internal fragment geometry and range-compatible affine terms, by deriving either a uniformly paid grouped-Schur bank or another mass-linear mechanism from the bare three-large-eigenvalue condition.

Execution remains `WITHOUT_VERIFIED_BRAIN`; no scheduler, email, notification, task, permission, paid-compute, or public-release mutation occurred.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T19:10:35Z.
attacking: apply the newest completed account03/B14 principal-triple localization theorem to the diffuse active-core barrier proved in this run.

# Partner update — exact determinant-localization cost on the diffuse family

After the main r17 report was committed, a newer completed assigned-partner result became available:

`account03/B14`, run `20260922T190524Z-account03-B14-QFORM-r16`, canonical
`yspennstate/math-open-problems@5e82f7573bc426a28a01fa25b0a2707ab0b573e2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T190524Z-account03-B14-QFORM-r16/REPORT.md`.

Its theorem `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1` proves, for every nonsingular original-coordinate principal triple `B`, arbitrary independent cap-one inputs, arbitrary outside couplings, and arbitrary affine perturbations,

`||p_Q||_infinity <= 32 sqrt(10) |det B|^(-1/3)`.

This is a complete, product-valid, zero-tail/translation-tax theorem in exactly the local scope needed here.

Apply it to the r17 diffuse family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`.

Every nonsingular original-coordinate principal triple consists of the singleton plus one coordinate from each bank and has determinant magnitude exactly `m^-2`. Therefore the newest partner theorem gives, on **every** available physical triple,

`||p_Q||_infinity <= 32 sqrt(10) m^(2/3)`.

Because all nonzero principal triples have the same determinant, no deterministic selector and no randomized selector among them improves this dimension loss. In particular, for every probability distribution `pi` on the nonzero triples,

`E_pi[32 sqrt(10) |det A_m[S,S]|^(-1/3)] = 32 sqrt(10) m^(2/3)`.

Thus the partner theorem and this run fit exactly: the local analytic payment is now complete and quantitatively sharp enough for the structural diagnosis, while the remaining debt is purely **aggregate-before-inversion**. The same family has overlap-one squared cross-minor mass `((m-1)/m)^2 ->1`, so the next theorem must spend that packet before choosing a tiny principal determinant.

This addendum supersedes only the source/constant used for the localized principal-triple branch in the main report. It does not change the r17 diffuse curvature identities, does not claim a full QFORM proof, and does not use the refuted scalar-conditioned supremum or arbitrary-joint coarea mechanisms.

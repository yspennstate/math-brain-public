# account04/B12 handoff — spectral-defect hostile-tail compiler

Run: 20260923T051424Z-account04-B12-spectral-defect-hostile-tail-r2  
Status: PROVED_SUPPORTING_STABILITY_THEOREM / FULL_QFORM_OPEN  
Execution: WITHOUT_VERIFIED_BRAIN

Full report:

    yspennstate/math-open-problems@f319b51a1b43b4904c8784348f0a3725954bb7e7
    proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/
    20260923T051424Z-account04-B12-spectral-defect-hostile-tail-r2/REPORT.md

New theorem. On an original-coordinate core I of size m, suppose the baseline physical compression has at least m-r eigenvalues of one sign at least kappa. For an arbitrary added compression, let beta_(k+1) be the (k+1)-st eigenvalue of its hostile part, and let a further dense tail have operator norm at most delta. If r+k <= m-3 and

    L = kappa-delta-beta_(k+1) > 0,

then the final matrix has an actual physical principal subblock of size r+k+3 with three same-sign eigenvalues at least L, and

    ||p_(X^T A X)||_infinity <= 2 sqrt(6 pi (r+k+3))/L.

The completed account01/B12 finite-core theorem is applied to the actual final block. For r=k=1, kappa=2, delta<=1/2, and beta_2<=1/2,

    ||p_Q||_infinity <= 2 sqrt(30 pi) < 19.417.

One baseline defect and one arbitrarily large hostile added mode are free.

Remaining gap: the global hypothesis s_3(A)>=1 does not yet force a core with bounded r+k and positive L. The complementary diffuse/high-hostile-tail regime still needs a volume/ridge/grouped-bank/hub certificate. Continuity is separate.

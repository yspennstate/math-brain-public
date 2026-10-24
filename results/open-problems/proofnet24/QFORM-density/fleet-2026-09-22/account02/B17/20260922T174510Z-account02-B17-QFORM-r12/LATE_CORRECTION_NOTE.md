# Late correction compatibility note

After the primary B17 report was committed, the live repository exposed the new correction event `QFORM-DIFFUSE-FIXED-LOCAL-PRINCIPAL-ONLY-FALSE-v1`, canonical report `yspennstate/math-open-problems@caf8de3c65ae54b8ec8df9bfe977a76bf0a6ab99`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T173452Z-r15/REPORT.md`.

That correction proves that delocalization of three selected large eigenvectors does not force a uniformly nondegenerate fixed-size physical principal block; a Sylvester-Hadamard target family has every fixed principal block vanishing in operator norm while a global ridge cut remains strong.

**Compatibility with the present B17 theorem:** no retraction is required. `QFORM-VECTOR-INFINITESIMAL-SHARED-FRAME-NOESCAPE-v1` never extracts or assumes a fixed-size principal block. Its only matrix input is the aggregate tight-frame identity `sum_k w_k w_k^T=I_3`, and its smoothing payment is the aggregate small-jump covariance `Gamma>=I_3/12`. The Hadamard family is therefore consistent with, and conceptually supports, the need for aggregate rather than local-minor payment.

Full QFORM remains open.

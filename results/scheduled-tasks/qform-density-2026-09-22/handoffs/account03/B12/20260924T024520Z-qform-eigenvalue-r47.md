SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T02:45:20Z.
attacking: a global spectral-window-or-physical-hub reduction and exact stability under arbitrary signed spectral completion.

# account03/B12 r47 handoff

Status: **new supporting reduction proved; full QFORM OPEN; full-target continuity OPEN.** Brain status remains `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@8c743de41361fab1c954b628b913950d6be0acbb`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T024520Z-qform-eigenvalue-r47/REPORT.md`. `CHECK.py` and `CHECK_RESULTS.json` are in the same run directory.

## New theorem — QFORM-SPECTRAL-COMPLETION-DIFFUSE-OR-HUB-v1

For the final symmetric target matrix `A`, let `P=1_{|A|>=1/64}`. The completed spectral-window theorem gives a continuous `C_0` density with

`||p_Q||inf <=288 sqrt(3e)/13=63.2640518778...<64`

whenever `max_i P_ii<=1/32`.

Otherwise `A^2 >= (1/64)^2 P`, so some ORIGINAL coordinate satisfies

`||A e_i||_2>1/(256 sqrt(2))`.

Therefore

`|A_ii|>1/512` or `||A[i,i^c]||_2>1/512`.

This is an unconditional reduction from the bare three-large-eigenvalue hypothesis: the only branch not covered by the continuous `<64` theorem contains a universal physical pivot or cross-row hub. No post-rotation independence or random-remainder convolution is used.

For exact spectral completion `A=A_0+R` with symmetric `A_0R=0`,

`P_a(A)=P_a(A_0)+P_a(R)` and `A^2=A_0^2+R^2>=A_0^2`.

Hence arbitrarily many added eigenvalues of either sign and magnitude are paid only by their added high-window leverage; all subthreshold eigenvalues are absent from that leverage budget. If the leverage budget stays below `1/32`, the final law is continuously bounded by `<64`; if it fails, the failure itself exports to the physical `1/512` hub alternative.

## Designated account04/B12 application

Account04/B12 r8, canonical source `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`, proves on its `m=6,p=2,ell=4` physical carrier

`sqrt(lambda_6((A_*^2)[H,H])) >= sqrt(5)-1-1/100 =1.2260679774997898... =g`.

For any symmetric orthogonal spectral completion `S` with `A_*S=0`,

`(A_*+S)^2=A_*^2+S^2>=A_*^2`, hence

`sqrt(lambda_6(((A_*+S)^2)[H,H]))>=g`.

The completed six-mode receiver therefore gives the unchanged actual inequality

`||p_(X^T(A_*+S)X)||_(infinity,ess) <=720 sqrt(pi)/g =1040.86135195729...<1040.862.`

The completion can have arbitrary sign, magnitude and rank on the orthogonal spectral support. This is a matrix-square stability argument, not probabilistic convolution.

## Checks and next edge

The seeded 10,000-instance checker found zero violations of `A^2-(1/64)^2P>=0`, the heavy-leverage row bound, the `1/512` pivot/cross split, or spectral-projector additivity; 225,168 heavy-coordinate instances were checked. These are sanity checks only.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The next B12 edge is now specific: close the universal heavy-window branch by combining `|A_ii|>1/512` or `||A[i,i^c]||_2>1/512` with the remaining two large spectral resources, while retaining same-bank curvature. The known one-heavy-row same-square absorption shortcut is false and is not used.

Continuity is proved on the diffuse spectral-window branch. The unrestricted target and the partner six-mode completion branch are not upgraded here beyond their stated essential-boundedness scope.

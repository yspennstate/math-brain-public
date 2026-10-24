# account03/B12 r43 handoff — spectral-packet Schur budget

Run: `20260923T231212Z-qform-eigenvalue-r43`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **supporting stability theorem proved; unrestricted QFORM remains OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics:

- repository: `yspennstate/math-open-problems`
- commit: `ebb9416d7ec781fab7ad250c50951f6a803ef7c1`
- report: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T231212Z-qform-eigenvalue-r43/REPORT.md`
- correction refresh: same directory, `CORRECTION_REFRESH_ADDENDUM.md`
- checker/results: same directory, `check_spectral_packet_schur.py`, `CHECK_RESULTS.json`

## Result

`QFORM-SPECTRAL-PACKET-SCHUR-BUDGET-v1`:

For symmetric baseline `A0`, arbitrary symmetric added `E`, `delta_q=s_{q+1}(E)`, final `A=A0+E`, and any invertible `r`-coordinate ORIGINAL physical pivot of final `A` with Schur complement `S`,

` s_k(S) >= (s_{q+r+k}(A0)-delta_q)_+ `

for every `q+r+k<=n`. Thus the first `q` added eigenmodes may have arbitrary magnitude, sign and orientation, while every remaining added eigenvalue is charged only through `delta_q`; the physical completion costs exactly `r` reserve modes. Positive and negative threshold counts separately lose at most `q+r` after shifting the threshold by `delta_q`.

The proof is deterministic rank algebra: spectral truncate `E=R+T` with `rank R<=q`, `||T||=delta_q`; use singular-value rank interlacing before the update, Weyl for `T`, and the exact rank-`r` Schur latent factorization. No added quadratic term is treated as independent random noise.

The reserve count is sharp on diagonal examples.

## Source matching explicitly not reclaimed

The exact no-packet Schur step `s_{j+r}(A)<=s_j(S)` was already committed in the fresh source at `math-open-problems@93d2aedf7856c66f42a4ece7156b773db2589efe`. The `r=2,k=1` physical-pair analytic receiver was already committed at `742ac943440e41925fe09db9a8c02a96cbd83dbc`. r43's new piece is the arbitrary pre-Schur signed spectral-packet composition and its density compilation.

## Actual account04/B12 application

Partner source: `math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`, account04/B12 r7. Its proved physical compression gate

` sqrt(lambda_6((A_p^2)[H,H])) >= 7/4 `

implies globally `s_6(A_p)>=7/4`. Add a further completely arbitrary symmetric `E` with `s_4(E)<=1/4`: its first three signed eigenmodes may be unbounded. Then:

- every nonzero final scalar physical pivot leaves `s_2(S)>=3/2`;
- every final invertible physical pair leaves `||S||op>=3/2`.

The completed two-large-mode half-potential theorem therefore gives, for scalar pivot magnitude `beta`,

`||p_Q||_(infty,ess) <= (G2+1)/sqrt((3/2) beta)`,

and the completed indefinite-pair receiver gives

`||p_Q||_(infty,ess) <= 3*400^(1/3)[(3/2)|det B|^2 sigma_min(B)]^(-1/6)`.

## Corrections / status

Final source refresh observed `math-research-brain/main@c4445ef9c24eb6bc5de33dd21fe2720998e4ca4f`; OWNER CONTROL remains `2026-09-22.15`, QFORM-only, no account03/B12 pause. The newer correction `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1` was checked: it concerns a one-nonzero-eigenvalue endpoint and does not affect r43, whose scalar corollary invokes half-Riesz only after proving two residual singular values. The B01 compound-alternative wording correction is unrelated.

Finite checks: 10,000 profile tests and 5,000 sign-count tests, zero violations; these are sanity checks only.

Continuity is not claimed for the new general compiler. Full QFORM and full-target continuity remain open.

Next B12 mechanism: after the packet budget is exhausted at exactly three final large modes and all quantitative physical pivots are small, force a product-preserving diffuse/grouped/ridge/projected-crossing carrier rather than continuing the r40-r42 small-tail common-plane perturbation loop.

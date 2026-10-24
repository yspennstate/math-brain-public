# Early calculation — latest partner strong-edge endpoint is already paid

Programme `QFORM-DENSITY-3EIG-20260922`, account02/B20 run `20260924T093443Z-account02-B20-QFORM-auto11-r51`.

Newest completed designated partner consumed: account03/B20 r51, canonical math commit `ceb973b9c1549a8247baf169db9152844b9decde`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T091209Z-account03-B20-QFORM-auto11-r51/REPORT.md`.

That report's strong-edge leaf supplies a literal ORIGINAL-coordinate invertible indefinite principal pair `P` with

`D=|det P| >= D0 = 9.530157744638501e-7`,

`kappa=s_min(P) >= kappa0 = 6.075614261408114e-5`,

while the owner target supplies `s_3(A)>=1`.

Apply the proved arbitrary-rank physical-pair theorem from
`math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`:

`||p_Q||_infinity <= 3*400^(1/3) * (D^2*kappa*s_3(A))^(-1/6)`.

Therefore, monotonically substituting the partner lower bounds,

`||p_Q||_infinity <= 3*400^(1/3)*D0^(-1/3)*kappa0^(-1/6)`

`= 11328.598626026012... < 11329`.

This theorem already allows arbitrary remaining rank, arbitrary remaining spectrum, arbitrary affine terms, and all couplings. Its proof completes the same pair exactly, uses `s_3(A)<=||S||op` for the exact Schur remainder `S`, and proves the required quarter-power small-ball bound for arbitrary-rank `S`. Hence the partner's newly stated first unpaid endpoint `QFORM-R13-ULTRATHIN-R6-CARRIER-RETAINED-TAIL-ENDPOINT-v1` is not unpaid: the quantitative physical pair present earlier on that very leaf pays the FULL ambient law before the rank-six/retained-tail reduction is needed.

No tail is discarded and no rotated random coordinates are introduced. This closes the latest partner leaf but does not close the separate pair-free global r52 moderate-residual rank-12/rank-11 endpoint.

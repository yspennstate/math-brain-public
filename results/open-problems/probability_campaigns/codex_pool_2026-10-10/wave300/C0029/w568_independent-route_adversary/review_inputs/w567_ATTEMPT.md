# C0029 independent route, w567

Recorded before reading any peer proof: use the geometry of a rectangular Bernoulli matrix with one row removed. Condition only on those n-1 rows, isolate their kernel direction, and express the final-row singular-value crossing through a Schur complement. Try to retain the exact normalization through the lower singular spectrum rather than replace it by a union bound over rows. The new row is independent of the rectangular block; coordinates of its kernel vector are not asserted independent.

The exact historical target has been recovered: iid sign entries, P(s_min(B_n)<=epsilon/sqrt(n))<=epsilon+c^n for some c in (0,1), all sufficiently large n and all small epsilon>=0. Its exponential-remainder variant extends to all epsilon and all n after adjusting absolute constants. Current openness in October 2026 remains UNKNOWN. No solved or novelty claim is made.

## Prior-attempt digest and independent boundary

The dated ranking calls C0029 attempted_un, constant one. The exact intake row is problems.jsonl:29; its September scope note correctly distinguishes Sah-Sahasrabudhe-Sawhney's coefficient 1+o(1) from 1. Only one exact-ID attempt was found in the named intake, H/I attempts, and Lean packet: C0029-A001 at attempts.jsonl:23. It used Gaussian comparison and polynomial-scale hard-edge universality. It obtained no improvement. H/I and the Lean packet did not contain an additional exact C0029/Spielman-Teng attempt in the targeted scan. Team O's current board has no C0029 row.

Correction needed in C0029-A001: the expression 1-exp(-t-t^2/2) is the LIMITING real Gaussian distribution as n tends to infinity, not its finite-n exact distribution. At n=1 the true distribution is P(|g|<=t), whose slope at zero is sqrt(2/pi), not 1. This is a concrete source-row correction, independent of the open target.

After seeing that the 2025 paper also uses row deletion, reserve a disjoint main route: determinant divisibility and arithmetic separation of nonsingular sign matrices. The row-deletion calculation will be retained only as a deterministic audit aid, with no claim that it is a new method. Do not duplicate the primary paper's Gaussian replacement calculation.

## Arithmetic route

For n>=2, a nonsingular n by n sign matrix has determinant divisible by 2^(n-1), hence absolute determinant at least 2^(n-1). Its squared singular values sum to n^2. AM-GM on the largest n-1 gives

s_min(B) >= 2^(n-1) ((n-1)/n^2)^((n-1)/2) =: alpha_n.

Consequently for 0<=epsilon<sqrt(n) alpha_n the least-singular-value event equals singularity exactly. This reaches a superexponentially small regime and cannot close the interval up to the polynomial regime by itself.

## First proved result

C0029-w567-L1: for iid uniform sign entries, n>=2, P(s_min(B)=0)>=2^(1-n). Given row 1, row 2 has 2^n equally likely values and exactly two are proportional to row 1. This fixes a necessary exponential floor; it is not an upper bound.

## Hardest remaining gap

Obtain an averaged, precisely normalized small-ball estimate for the last row against the random kernel direction, with control of the singular spectrum of the rectangular block on the same event. Constant losses in this step may prevent a coefficient-one bound. The exact formulation will be fixed from sources.

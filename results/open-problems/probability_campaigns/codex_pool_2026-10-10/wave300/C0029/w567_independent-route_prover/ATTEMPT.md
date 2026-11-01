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

The initial row-deletion idea overlaps the primary paper and is retained only as L4's audit aid. The current single gap is the sharp averaged operator-norm tail of L3's full bordered inverse, with coefficient one. No bound on the interior inverse alone has closed it.

## Attempted norm reduction and why it stalls

In L3 put P=[-1^T;I_(n-1)] and e_0=(1,0,...,0). Directly from the proved block inverse,

C^(-1)=e_0 e_0^T-(1/2)P H^(-1)P^T.

Since P^T P=I+11^T, ||P||_op^2=n. The elementary upper estimate is therefore ||C^(-1)||_op<=1+(n/2)||H^(-1)||_op. Compressing to the lower-right block gives the lower bound (1/2)||H^(-1)||_op<=||C^(-1)||_op. Applying these estimates at sqrt(n)/epsilon loses a factor n and does not produce the desired probability bound.

That deterministic loss cannot simply be removed: for H=I_(n-1), the upper-left inverse entry is (3-n)/2, so ||C^(-1)||_op>=|3-n|/2 while ||H^(-1)||_op=1. This sign-matrix witness is exponentially rarer than required under the iid interior law, so it blocks only a uniform deterministic shortcut. A successful route must use the distribution of H to control the correlated terms H^(-1)1, 1^T H^(-1), and 1^T H^(-1)1 together, including the cancellation in the upper-left entry. These terms are functions of the same H and are not independent. The exact probabilistic obligation is recorded as C0029-w567-GAP.

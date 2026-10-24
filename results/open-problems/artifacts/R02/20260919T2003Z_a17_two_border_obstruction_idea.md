# R02 idea before code — strengthen the A17 border no-go from one added coordinate to two

Methods used: **#10 DERANDOMIZE, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

The preceding R02 run proved that every 18x18 sign matrix obtained by adding one row and one column to the retained exact A17 witness has discrepancy at most 6. The next natural question is whether adding **two** rows and columns can evade that obstruction.

Write

\[
D=\begin{pmatrix}A_{17}&C\\R&E\end{pmatrix}\in\{\pm1\}^{19\times19},
\]

with `C` of size 17x2, `R` of size 2x17, and `E` of size 2x2. To beat the retained normalized witness `7/sqrt(17)`, an odd-order 19x19 matrix would need discrepancy at least 9. It would therefore be enough to prove `disc(D)<=7` for every such two-border extension.

## #18 — Hamming-cube language

Keep the 3,780 projective singleton discrepancy-7 minimizers `y` of A17 from the preceding exact certificate, fixing coordinate 17 to +1. For a prospective added row `r` with `r_17=+1`,

\[
r\cdot y=17-2d_H(r,y).
\]

Thus `|r dot y|<=5` is exactly the annulus condition

\[
6\le d_H(r,y)\le 11
\]

on the first 16 coordinates. For each `r`, let `G(r)` be the singleton minimizers lying in that annulus.

If every `G(r)` has size strictly greater than half of 3780, then any two added rows `r_1,r_2` have a common singleton minimizer by inclusion-exclusion. This would remove the need for an impossible pairwise search over roughly 2^32 row pairs.

## #10 — derandomize the simultaneous two-row condition

A uniformly random singleton minimizer is a useful thought experiment only if the good fraction is uniformly >1/2 for every `r`. If the exact minimum satisfies

\[
\min_r |G(r)|>1890,
\]

then for any pair

\[
|G(r_1)\cap G(r_2)|\ge |G(r_1)|+|G(r_2)|-3780>0.
\]

That gives a deterministic common `y` simultaneously controlling both new rows.

The exact counts for all 2^16 projective `r` can be computed as one XOR convolution between the indicator of the singleton-minimizer code and the indicator of the Hamming annulus `{6,...,11}`. A Walsh-Hadamard transform gives an exact integer certificate in O(16*2^16) arithmetic rather than O(3780*2^16).

## #23 — reverse the growth strategy

Instead of searching for an order-19 improvement by extending A17, try to prove that **the entire two-border family is structurally incapable of improving**. If the annulus density test passes, choose the common singleton `y`. Its unique active A17 row has value `7 sigma` and all other A17 row sums have magnitude at most 5. For the two new signing bits `t in {+-1}^2`, the active row receives a correction in `{-2,0,2}`; at least three of the four choices do not increase its absolute value above 7. Every nonactive old row is at most `5+2=7`, while both new rows are at most `5+2=7` because `|r_j dot y|<=5`.

So the hoped-for theorem is:

> Every 19x19 sign matrix having the retained A17 as a 17x17 principal block has discrepancy at most 7.

This would imply that neither one-border nor two-border growth of the certified A17 orbit can improve the normalized lower bound. The exact annulus count is the only finite claim that needs checking before writing the proof.

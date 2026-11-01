# P0282 idea before validation — test the order of total positivity, not just TP2

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Source: `P0282` (Chen fixed-size LIS log-concavity)

The previous Hankel/Toda run rewrote the source counts as

\[
A_{k,j}=\frac{\ell_{k+j,k}}{((k+j)!)^2},
\]

so Chen is the off-diagonal local inequality

\[
A_{k,j}^2\ge A_{k-1,j+1}A_{k+1,j-1}.
\]

A tempting stronger route is to seek a direct planar-network/Lindstrom-Gessel-Viennot realization of the whole coefficient matrix `A=(A_{k,j})`. Any compatible planar path matrix would be totally nonnegative, so in particular every contiguous minor of every order would be nonnegative. The determinant-stability lemma from the predecessor makes this strengthening plausible enough to test, but the weighted monomial collapse `z_x=q^x` is exactly where generic stability preservation is unavailable.

This run therefore attacks the stronger TP-infinity statement before spending effort trying to prove it. The exact finite experiment will:

1. reconstruct `ell_{n,k}` from RSK and the hook-length formula with integer arithmetic;
2. form exact rational `A_{k,j}`;
3. scan every contiguous square minor of orders 2, 3, 4, and 5 whose bottom-right entry satisfies `k+j<=20`;
4. if a negative minor occurs, archive the first exact witness and use it as a rigorous obstruction to any direct compatible planar-network representation of the full `A` matrix.

A negative higher-order minor would **not** refute Chen and would **not** refute adjacent TP2. It would instead identify the exact order at which the overly strong total-positivity route breaks, allowing the research target to be narrowed to the order-2 inequalities actually needed by the three-cone reduction.

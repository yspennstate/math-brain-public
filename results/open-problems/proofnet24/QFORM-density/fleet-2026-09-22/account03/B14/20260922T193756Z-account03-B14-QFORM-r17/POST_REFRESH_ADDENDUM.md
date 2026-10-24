# Post-refresh addendum — compatibility with the new aggregate-bank correction

After the main report was committed, fresh control advanced to owner revision `2026-09-22.15`, still QFORM-only with no B14 pause. A new target-valid correction from account02/B07 was then consumed: `QFORM-R15-AREA-BANK-SINGLE-PACKET-FALSE-v1`, canonical source

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39:proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.

That report gives a rank-three cross-block family whose total determinant-law mass is constant while every pair-containing physical triple has squared volume `3/(8N)`. It therefore independently confirms the same order-of-operations principle established in this B14 run: **aggregate a whole bank before reciprocal inversion; selecting/normalizing a tiny packet first is non-uniform.**

The B07 report also proves `QFORM-CROSS-FIBER-PLANCHEREL-v1`: if a fixed physical cross block has rank `r>=3` and nonzero singular values `s_1,...,s_r`, with `D=prod s_i`, then

`||p_Q||_infinity <= e*r/(r-2)*D^(-1/r)`

for arbitrary self blocks, outside couplings, and affine terms. This is exactly a whole-block payment rather than a fragmentwise reciprocal-minor payment. In B07's stress family `D=1`, giving `||p_Q||_infinity <=3e` uniformly while every selected physical triple degenerates.

No new full-target claim follows: the bare three-large-eigenvalue hypothesis still needs an exhaustive mechanism guaranteeing either such a payable whole cross block or another grouped/ridge/decoupled route. The main report's fragmentwise tax theorem and replacement obligation remain unchanged and are strengthened by this independent target-valid stress.

# Late partner refresh — fleet03/B19 r36 consumed before handoff

After the main report was written, the designated partner completed fleet03/B19 r36 at

`yspennstate/math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T145843Z-fleet03-B19-QFORM-r36/REPORT.md`.

Its proved `QFORM-STAR4-THIRD-RESOURCE-CARRIER-DICHOTOMY-v1` says that the true aligned STAR4 survivor has either

`(I) rank(S)<=5, s_3(S)>=1/4`,

or an original self bank `B` with

`||B||op>0.673586637`,
`sum_(i!=j)B_ij^2>0.453717673`,

and a physical bipartition with cross Frobenius square `>0.113429418`.

This changes the first global debt to `QFORM-ALIGNED-SKELETON-OR-SELFPAIR-PAYMENT-v1`.

## Equation-level application to this run's in-plane stress family

For the family in `REPORT.md`, the STAR4 cross has exact rank two and both stars are exactly aligned, so the partner's discarded matrix `R` is exactly zero. In the orthonormal aggregate basis

`(e_h,p,r,q,s)`,

the partner skeleton is

`S = [[0, 1,-1, 1,-1],
      [1, 0, 0, 5/6,      -sqrt(2)/6],
      [-1,0, 0,-sqrt(2)/6,-4/3],
      [1, 5/6,-sqrt(2)/6,0,0],
      [-1,-sqrt(2)/6,-4/3,0,0]].`

Its characteristic polynomial factors exactly as

`det(xI-S)=(6x^2-3x-7)(6x^3+3x^2-31x-6-4sqrt(2))/36`.          (A.1)

The quadratic factor has roots

`(3+sqrt(177))/12 >1`,
`(3-sqrt(177))/12 <-3/4`,

and the cubic factor is negative at `x=1` and positive at `x=3`, so it has a root larger than one. Thus at least three eigenvalues of `S` have modulus greater than `3/4`, in particular

`boxed: s_3(S)>3/4>1/4.`                                       (A.2)

So the explicit fully-overlapping strict-N3 construction lies squarely in the partner's new finite-rank carrier branch (I), not in the self-bank carrier branch (II).

The main report then pays this concrete branch-(I) state by the owner-required union-leaf Theorem-F calculation:

`A[J union K,J union K]` has exact spectrum `{2,-2,1}` and physical three-frame leverage `<2/m`, hence

`boxed: ||p_Q||infinity <=12*4^(-1/3)<7.560.`                   (A.3)

Therefore this run removes a genuine subchamber of the new partner branch (I): a rank-at-most-five aligned carrier may have its third direction completely in-plane and still be paid whenever the union leaf block closes to a diffuse rank-three-plus-diagonal Fresnel packet.

## Updated first unpaid implication

The first compatible debt is now exactly the partner's

`QFORM-ALIGNED-SKELETON-OR-SELFPAIR-PAYMENT-v1`,

with the following additional paid exclusion from this run:

- in branch (I), exclude the union-leaf rank-three-plus-diagonal diffuse-Fresnel states of Corollary 4.1 in `REPORT.md`;
- branch (II), the overlapping self-bank cross packet still cannot be treated as source-disjoint because its couplings to the existing `J-K` bicore are genuine and cannot be deleted.

No claim is made that every rank-five skeleton satisfies the union-bank Fresnel hypotheses. The remaining obstruction is precisely uncontrolled same-bank curvature/tails in branch (I), or joint spending of the overlapping self-pair packet with the bicore in branch (II).

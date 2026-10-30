# r50 deterministic algebra checks

The proof in `REPORT.md` is exact; these checks are diagnostic only.

A fixed-seed NumPy harness tested 5,000 random symmetric `3 x 3` hub matrices `K` and random `3 x 5` hub-tail matrices `M`, omitting only numerically singular scalar pivots / full hub matrices when a floating inverse was required. With pivot `i=1`, it formed

`B=K[J,J]-K[J,i]K[i,J]/K[i,i]`,
`N=M[J,:]-K[J,i]M[i,:]/K[i,i]`,
`R=adj(K)M`.

Maximum normalized residuals were:

- `R_J = a adj(B) N`: `1.467574653995839e-13`;
- `|det A[H,{i,p,q}]| = |a det N[:,{p,q}]|`: `4.0440686001076716e-13`;
- `|det R_J[:,{p,q}]| = |det(K) det A[H,{i,p,q}]|`: `1.7696779717359445e-14`.

The identities used in the proof follow algebraically from block elimination, Cauchy-Binet, and the two-by-two adjugate formula; the floating checks are not evidence for the universal density claim.
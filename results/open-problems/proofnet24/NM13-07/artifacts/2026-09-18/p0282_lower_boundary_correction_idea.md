# P0282 idea before validation — exact lower-boundary completion correction

Date: 2026-09-18 UTC
Worker: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity

The preceding run showed that the completed residual-partition model agrees with the source through `n>=2j-1`, but fails at `n=2j-2`. The next route is to classify the failure exactly instead of extending the uncorrected cone.

I will use three Section-B moves that have not previously been used on P0282:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** at the single boundary `n=2j-2`, classify the finitely many residual partitions excluded from the source but included by polynomial completion.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** rather than attack fixed-row log-concavity directly, subtract the exact completion error and study the corrected Turan margin.
- **#26 HUNT THE SPORADIC CASE:** scan the corrected boundary exactly for a first exceptional defect and distinguish a genuine source failure from a failure of the completion certificate.

Notation from the predecessor: `E_r(n)=ell_{n,n-r}`, `Etilde_r(n)=P_r(n)/r!`, and

`Delta_tilde_j(n)=Etilde_j(n)^2-Etilde_{j-1}(n)Etilde_{j+1}(n)`.

At `n=2j-2`, the source/completion errors can be classified explicitly.

For `E_j`, the residual first-row allowance is `N=j-2`. Among partitions of `j` with first part greater than `N`, only `(j)` contributes nonzero completion mass; `(j-1,1)` has a zero residual factor. Hence

`Etilde_j(2j-2)=E_j(2j-2)+c_j`,

where

`c_j = [ (2j-2)! / ((j-1)! j!) ]^2`.

For `E_{j-1}`, the residual allowance is `j-1`, so completion is exact:

`Etilde_{j-1}(2j-2)=E_{j-1}(2j-2)`.

For `E_{j+1}`, the residual allowance is `N=j-3`. The excluded residual partitions with potentially nonzero weight are exactly

`(j+1)`, `(j,1)`, `(j-1,2)`, `(j-1,1,1)`;

all shapes with first part `j-2` have zero first residual factor. Writing the four squared normalized residual amplitudes relative to `c_j` gives

`9(j-1)^2/(j+1)^2`,

`4j^2(j-2)^2/(j+1)^2`,

`(j-2)^2(j-3)^2/4`,

`(j-1)^4(j-2)^2/[4(j+1)^2]`.

Their sum simplifies to

`rho_j = (j^6-8j^5+30j^4-52j^3+47j^2-40j+38)/(2(j+1)^2)`.

Thus

`Etilde_{j+1}(2j-2)=E_{j+1}(2j-2)+d_j`,

`d_j=c_j*rho_j`.

Therefore the exact source Turan margin at the first completion-invalid boundary is

`M_j := E_j^2-E_{j-1}E_{j+1}`

`= Delta_tilde_j(2j-2) - 2 c_j Etilde_j(2j-2) + c_j^2 + Etilde_{j-1}(2j-2) d_j`.

This identity is the object to validate and exploit. It explains the predecessor's `j=4,n=6` discrepancy without conflating failure of the completed model with failure of Chen's source inequality.

Validation plan, only after this note: (i) exact arithmetic test of the four-shape correction and corrected boundary margin across a substantial defect range; (ii) a complete exact row-81 RSK certificate to move the frozen metric if the row passes; (iii) archive only source and output needed for those finite claims.

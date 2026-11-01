SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T06:50:59Z.
attacking: exact/near double-star two-minor overlap geometry, closing the exact-star outer-square branch and quantifying the first near-star rank-three obstruction against ridge on one physical matrix.

# Early substantive checkpoint — exact-star closure

Full QFORM remains OPEN. This checkpoint uses only original-coordinate product structure and preserves the live corrections: no law-uniform scalar pointwise Fourier decay, no post-rotation independence, no arbitrary-joint coarea estimate, and no conditional projection-density cap moment.

## Source-pinned inputs actually used

1. Designated partner fleet03/B04 r26, `QFORM-THREE-MINOR-STAR-DICHOTOMY-v1`, current report path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T055256Z-fleet03-B04-qform-auto11-r26/REPORT.md`: if the canonical physical 2x2-minor three-sample row-overlap probability is zero, every supported row pair contains one physical hub and therefore deleting that row leaves rank <=1; hence the cross block has rank <=2. The same holds on columns.

2. fleet02/B04 r22, `QFORM-SQUARE-RANKR-TWOSIDED-CONTAMINATION-v1`, source commit `8f8913581643a7e7bcbe7d8c178a2255194dfc3d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T233213Z-r22/REPORT.md`: for exact physical cross rank two with nonzero singular values sigma1,sigma2 and one untouched original-coordinate square of coefficient a,

`||p_Q||_infinity <= [8 sqrt(e)/3^(1/4)] |a|^(-1/2) (sigma1 sigma2)^(-1/4)`

while allowing arbitrary self-quadratic contamination on both product banks and an arbitrary residual-dependent shift in the outer square.

## New immediate corollary: `QFORM-STAR-SUPPORT-SQUARE-CLOSURE-v1`

Let M be a physical cross block between disjoint original-coordinate product banks and suppose

`Z2=e2(M^T M)=sum_{|S|=|T|=2} det(M_ST)^2 >0`.

If either three-sample overlap probability of the canonical squared-minor law vanishes, `delta3^r=0` or `delta3^c=0`, then the partner theorem gives `rank(M)<=2`; positivity of Z2 forces `rank(M)=2`. Therefore

`sigma1 sigma2 = sqrt(Z2)`.

For

`Q=a[Z+m(X,Y,W)]^2+F(X,W)+G(Y,W)+2 X^T M Y`,

where Z is one further untouched original coordinate of density cap one and all other original coordinates remain independent, the r22 exact-rank-two theorem gives

`boxed: ||p_Q||_infinity <= [8 sqrt(e)/3^(1/4)] |a|^(-1/2) Z2^(-1/8).`

Thus the exact star residue left by fleet03/B04 r26 is analytically paid whenever the structural reduction supplies one genuine original scalar square. The square shift may reuse both contaminated banks. No minor is selected and no small local coefficient is inverted.

## Same-matrix stress point

Take

`M0=[[2,1,1],[1,1,1],[1,1,1]]`.

Every physical entry is nonzero. Its only nonzero 2x2 minors are the four choices using row 1 and column 1; all have determinant 1. Hence `Z2=4`, both row and column minor supports are exact stars, and every probability weight on nonzero minors has hub marginal 1. Therefore the entropy-weighted rank-two theorem from the preceding fleet02/B04 run has **no admissible weight for any q<2**.

The two positive singular values of M0 are `2+sqrt(2)` and `2-sqrt(2)`, so their product is 2. For

`Q0=Z^2+2 X^T M0 Y`

the symmetric matrix has spectrum

`{1, +(2+sqrt(2)), -(2+sqrt(2)), +(2-sqrt(2)), -(2-sqrt(2)), 0,0}`.

Thus Q0 is a genuinely non-diagonal indefinite target form with exactly three eigenvalues of modulus >=1. The new corollary gives

`boxed: ||p_Q0||_infinity <= [8 sqrt(e)/3^(1/4)] 2^(-1/4) = 8.427512693903992... .`

On this identical physical M0, the square-assisted ridge gate also fails at every scale. Put g=gamma^2 and

`K=M0 M0^T (g I+M0 M0^T)^(-1)`.

Direct calculation gives

`K_11=(6g+4)/(g^2+12g+4)=:k`,
`K_22=K_33=k/2`,
`theta=tr K=2k`.

Any admissible ridge exponent has `q>=2 max diag K=2k`, while the square-assisted ridge theorem requires `theta>4q/3`. But `theta=2k<=q<4q/3`, impossible. The direct ridge criterion fails a fortiori. Hence on one exact target-valid physical matrix: admissible two-volume weighting is infeasible, all present ridge scales are infeasible, while the exact-rank joint product-Fourier theorem yields the explicit uniform bound 8.428.

Next calculation: replace the exact star by a one-parameter rank-three near-star, solve the full entropy projection for every admissible q, and compare the optimized logarithmic certificate to direct ridge and exact-rank-three Fourier costs.

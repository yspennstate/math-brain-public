# Root analytic audit: parallel slabs and separated crossings

Date: 2026-10-02 UTC. Status: **PASS for the strict-separation theorem and arbitrary parallel slabs**. This is an internal analytic audit, not outside peer review or a priority certificate.

I read the repaired candidate and the full final `stripe_extension_parallel_slabs_proof.md`, and read both independent analytic audits and both finite checkers. The final theorem deliberately excludes a non-strict general separation claim; the preserved endpoint certificate disproves the influence-additivity step in that earlier claim.

## Independent checks of the argument

1. For every Boolean split, the pair-spectrum identity gives Delta H = sum P[1+h2(q)-h2(r)], with r(1-r)=(1-2q)^2/4. The elementary h2(t)>=4t(1-t) bounds the interference term by the conditional split-bit entropy. Thus Delta H<=2C with the empty atom included.

2. For a narrow interval the two exceptional branch supports are disjoint, so A=1-|B| even though B may change sign. With alpha=E B² and beta=E B, P_empty=(1-alpha)²+beta². The nonempty mass is at most 2alpha. When alpha<1/2 the empty conditional entropy is bounded by 2alpha² log2(1/alpha)+alpha² log2(e)<2alpha, using x log2(1/x) increasing on [0,1/4] and sup alpha ln(1/alpha)=1/e. When alpha>=1/2, C<=1. These checks prove Delta H<=8alpha without a halfspace estimate.

3. Under strict crossing separation, the individual pivotal slabs are disjoint. Therefore B=sum signs times B_r, |B| is their union indicator, and alpha=sum alpha_r. A nonconstant halfspace has a pivotal largest-weight coordinate, and redundant crossings can be deleted. This justifies applying the primary halfspace estimates individually; it does not assume a monotone signed derivative.

4. The sinc-squared concentration kernel has the stated triangular Fourier transform. Since each remaining weight is at most the pivot weight, cos(bt)<=exp(-b²t²/2) on the integration interval. The resulting interval bound is uniform in its center and includes atoms. In the resampling argument the mask is independent of X. Both the good-mask conditional probability and the bad-mask event can therefore be multiplied by E|B(X)|=alpha. The bound 6m alpha/sqrt((1-rho)R) is a genuinely relative estimate. Signed stability is at most E|B(X)||B(Y)|. Hypercontractivity depends only on |B| and gives alpha^(4/3), so signed B causes no change to the low-degree argument.

5. The pair-spectrum tail is obtained by the union bound over crossing halfspaces, rather than by an unsupported relative small-set noise theorem for a whole interval. The primary Keller--Klein maximal-influence bound and KOS minority-density noise bound use compatible physical influence normalization. The weighted Jensen step is valid: alpha_r<=2p_r implies ln(1/p_r)<=ln(2/alpha_r), and the entropy of alpha_r/alpha is at most ln m. Consequently a tiny remote crossing does not introduce its own maximal logarithmic scale.

6. For Q=Bhat²/alpha, the empty atom is Q_empty=(EB)²/alpha<=alpha. Separating it is essential. On positive-degree dyadic bins, the Q negative-degree moment is bounded by 18m sqrt(2) sum_(l>=1) l 2^(-l/2), while the P tail supplies P_j<=Gamma_m alpha 2^(-j/2). Nonnegativity of KL against the stated reference law gives a LOWER bound on D(Q||P); data processing has the same direction. The signed empty atom costs at most 1+log2(e)/e, yielding the explicit D_m. The included-bit entropy is alpha[log2(1/alpha)-D(Q||P)]; the excluded-bit entropy is at most alpha log2(e). Thus the final constant C_m=2[D_m+log2(e)] is justified.

7. The finite score set permits crossing perturbations preserving every Boolean value. In the arbitrary slab theorem one can avoid all width=2w equalities and use either the narrow or wide proof after each restriction. This does not preserve non-strict general crossing separation at attained endpoints, and the final proof correctly makes no such claim. Strict separation is preserved by sufficiently small perturbation and by restrictions, since all boundaries translate and the largest remaining weight decreases. Both classes therefore support the restriction induction.

## Three-crossing boundary

I read `three_crossing_largest_weight_obstruction.md` completely. Its encoded majority/point-flipped-majority pair is exact and has pivot weight N+1, uniquely largest. The central-layer derivative generating polynomial proves the majority coefficient formula. Vandermonde with binomial log-concavity gives the uniform coefficient lower bound. There are 2^(N-1) subsets of each parity; the even subsets contribute 2alpha in total, and the odd subsets supply the stated lower bound. Hence Delta H/alpha diverges for this three-crossing family. It refutes a local induction criterion, not the global FEI inequality.

## Computation and scope

The two scripts have been read in full. The slab suite computes Walsh spectra and uses floating-point entropy/stability as finite sanity checks. The obstruction checker uses exact rational coefficients and a 100-digit Decimal calculation of local entropy increments, avoiding subtraction of nearly equal whole-function entropies. The analytic proofs, not those finite computations, establish the dimension-independent statements and the asymptotic obstruction. Historical priority is unverified.

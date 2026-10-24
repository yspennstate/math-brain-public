# Signed information convolution and its anchor bound

All logarithms are base two. Let f be any Boolean sign on a finite uniform n-cube, a_S its real Fourier coefficients, p_S=a_S^2, and ell_S=log2(1/p_S) on positive atoms. Set a_S ell_S=0 at zero atoms. Define

    c_U = sum_S a_S a_(S xor U) ell_S,
    E_log = sum_(U nonempty) |U| c_U^2,
    J_R = sum_(U nonempty) p_(R xor U)/|U|.

For every occupied anchor R the following holds:

    p_R [H(f)-ell_R]^2 <= J_R E_log.                 (1)

In particular, when R maximizes p_R,

    0 <= H(f)-log2(1/p_R) <= sqrt(J_R E_log/p_R).     (2)

No dimension-independent payment of the right side is asserted.

## Complete proof; signs survive the cancellation

Let M_(U,S)=a_(U xor S). The FULL signed convolution equations give

    (M^2)_(U,V)=sum_S a_(U xor S)a_(S xor V)=delta_(U,V).

Thus M is a real symmetric orthogonal involution, a consequence using every shift, not just a bounded-order prefix. Put b_S=a_S ell_S. Then c=Mb, c_0=H, and Mc=b. At row R this says

    a_R H + sum_(U nonempty) a_(R xor U)c_U = a_R ell_R.

This is the decisive signed cancellation. Only now apply Cauchy-Schwarz to the nonempty sum, with weights |U| and 1/|U|. Its square is at most J_R E_log. This proves (1). If p_R is maximal, ell_R is the minimum information value and H>=ell_R, proving (2). All sums are finite and all logs are evaluated only on positive atoms.

The same full identity gives the exact entropy-weighted isometry

    sum_(U nonempty) c_U^2 = sum_S p_S ell_S^2-H^2
                           = Var_p(ell).            (3)

For a spectral cutoff A, d_U=sum_(S in A) a_S a_(S xor U) satisfies

    sum_(U nonempty) d_U^2 = p(A)[1-p(A)].           (4)

These are complementary consequences of M^2=Id. For each U nonempty one may subtract any constant from ell_S in c_U, precisely because the signed convolution vanishes. One may also write c_U as one half of sum_S a_S a_(S xor U)(ell_S+ell_(S xor U)), omitting pairs with a zero coefficient. Taking absolute values before M^2=Id destroys these conclusions.

For an explicit missing-hypothesis diagnostic, fix any truncation r and a set V of size r+1. The real vector a_0=3/5, a_V=4/5 has norm one and vanishing signed convolution at every nonzero shift of size at most r, but convolution at V is 24/25. For A={0,V}, the left side of (4) equals 576/625 and the right side is zero. This non-Boolean example verifies directly that the orthogonal-involution/cutoff consequence is not supplied by a fixed-order prefix. It is an illustrative independent diagnostic, not a replay of the archived dyadic G_(K,w) construction.

## Explicit paid test class: one physical point defect

For n>=3, N=2^n, f_n=1-2*1_(x=x0), q=4/N^2, p0=(1-2/N)^2, and Delta=log2(p0/q)=2log2(N/2-1), the empty atom is largest. For every U nonempty,

    c_U=-a_0 a_U Delta,
    E_log=p0 I Delta^2,
    I=2n/N,
    J_0=q A_n,  A_n=sum_(k=1..n) binom(n,k)/k.

The c formula uses cancellation of ALL other terms against the empty term; it is not an unsigned convolution. Thus the cost in (2) equals sqrt(J_0 I)*Delta. Since 1/k<=2/(k+1),

    A_n <= 2[(2^(n+1)-1)/(n+1)-1] < 4N/(n+1),
    J_0 < 16/[N(n+1)],  Delta<=2(n-1).

Consequently sqrt(J_0 I)*Delta < sqrt(32)*I < 6I. Also, t=2/N<=1/4 and -ln(1-t)<=t/(1-t) give

    ell_0/I <= 2/[n(1-2/N)ln2] <= 8/(9ln2) < 2.

The final strict inequality follows already from ln2>1/2. Hence (2) proves H(f_n)<8 I(f_n). For n=2 the four atoms are flat and H=2, I=1; n=1 is a character. This is a calibration of the signed inequality on a known easy class, not a novel FEI class or improved point-defect constant.

In fact A_n~2N/n. Proof: if K~Bin(n,1/2), then n A_n/N=E[n/K;K>0]. On |K/n-1/2|<=epsilon, n/K converges to 2 as epsilon decreases. The complementary probability is at most 2 exp(-2 epsilon^2 n), by the standard elementary binomial Chernoff argument, while n/K<=n. This gives the claimed limit.

For completeness the tail estimate follows from E exp(t(K-n/2))=cosh(t/2)^n<=exp(nt^2/8). The bound cosh z<=exp(z^2/2) follows termwise from (2j)!>=2^j j!. Markov's inequality with t=4epsilon bounds each tail by exp(-2epsilon^2 n). The exceptional contribution to E[n/K;K>0] is at most 2n exp(-2epsilon^2 n). On the central event n/K lies between 1/(1/2+epsilon) and 1/(1/2-epsilon); first let n tend to infinity and then epsilon tend to zero. Thus no unproved asymptotic concentration input is needed.

Since Delta~2n,

    sqrt(J_0 I)*Delta / I -> 4,
    [H-ell_0]/I -> 4.

The bound is therefore asymptotically tight on this family.

## Two obstructions to closure

1. E_log alone cannot be paid by a fixed multiple of I. On the SAME Boolean point-defect family, E_log/I=p0 Delta^2~4n^2. This is an analytic disproof of that helper, not FEI.

2. The anchor bound does not capture flat spectral entropy: if p is uniform on its support, c_U=0 for U nonempty, while H=ell_R can be arbitrarily large (bent functions). Even outside flat spectra, the product anchor cost need not tensorize. If f and g live on disjoint cubes, ell_(S,T)=ell_S^f+ell_T^g and cancellation makes c_(U,V)=c_U^f delta_(V,0)+delta_(U,0)c_V^g. Thus E_log is additive, as is Var(ell), but J_R/p_R generally is not.

For a tensor power h^t of the three-bit point defect h, pmax=9/16, I(h)=3/4, Delta=log2(9), and E_log(h)>0. For its largest-atom anchor,

    J_R >= [1-(9/16)^t]/(3t),
    sqrt(J_R E_log(h^t)/p_R)
      >= sqrt(E_log(h)[1-(9/16)^t]/3)*(16/9)^(t/2).

The cost grows exponentially while I(h^t)=3t/4. Hence a universal claim that the RIGHT SIDE of (2) is O(I) is FALSE, although (2) itself is true. The exact signed anchor sum can be much smaller than its weighted Cauchy bound. A universal bound for the combined anchor surprisal plus that cost is also false on this class.

## First unsupported line and next action

The bound (2), the identities (3)-(4), and the scoped calculations above are fully proved. Full FEI remains open. The unsupported inference is that the signed anchor sum (before Cauchy), together with anchor surprisal, has an influence-paid block or multiscale decomposition for arbitrary Boolean f. The naive single-anchor positive cost is now refuted by an actual Boolean tensor family, so it must not be adopted as an open universal payment target unchanged.

Next: reconstruct the signed anchor equation blockwise, preserving cross-block cancellation, and ask whether a tensor-additive logarithmic remainder can replace J_R E_log/p_R without discarding the anchor surprisal. Independent reconstruction requested from A088 (then A094); neither review has occurred.

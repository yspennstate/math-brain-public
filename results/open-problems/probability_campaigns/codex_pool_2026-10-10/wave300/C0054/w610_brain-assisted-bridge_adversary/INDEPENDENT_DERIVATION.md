# C0054 independent obstruction (saved before opening w609's proof)

2026-10-10. Author w610; independent check requested from w611, not yet received.
This does not prove or disprove the parent localization conjecture.

The candidate record asks for fixed-bandwidth, two-dimensional bulk localization, localization length on the exponential W^2 scale, and Poisson local statistics. The exact original source is still being recovered. The following obstruction concerns the concrete complex Gaussian block model in Lai--Yang, arXiv:2609.24426v2, equations (1.4)--(1.5). It applies only to the indicated elementary contraction route.

Take W a positive integer and an even block-torus side L >= 100. Each block contains W^2 sites. The variance is 1/(5 W^2) within the same block and the four neighboring blocks, and zero otherwise. Diagonal entries are real Gaussian; off-diagonal entries are circular complex Gaussian; distinct upper-triangular entries are independent. Put sigma=(5 W^2)^(-1/2). Each site has D_W=5 W^2-1 off-diagonal neighbors. Fix 0<s<1 and z=E+i eta, eta>0, and let G=(H-z)^(-1), with G^(x) the resolvent of the principal minor deleting site x.

For x != y, the exact Schur-complement identity is

    G_xy = -G_xx sum_(u != x) H_xu G^(x)_uy.

The row (H_xu)_(u != x) is independent of the minor, but is not independent of G_xx. Average over H_xx first, conditionally on the entire row and the minor. Its denominator is H_xx-a, where a=z+h_x^* G^(x) h_x has positive imaginary part. A uniform bound over a is legitimate even though a depends on the row.

For g~N_R(0,1), the optimal scalar uniform diagonal-averaging constant is

    A_s = sup_(a in C_+) E|sigma g-a|^(-s)
        = sigma^(-s) c_s,
    c_s = 2^(-s/2) Gamma((1-s)/2)/sqrt(pi).

To justify optimality: replacing a by its real part increases the integrand; the convolution of the even decreasing Gaussian density with |t|^(-s) is maximal at zero. The latter follows by layer-cake decomposition into centered intervals, whose Gaussian mass decreases under translation. Let a=i eta and eta decrease to zero to attain the supremum in the limit. The moment is integrable exactly for 0<s<1.

Fractional subadditivity and subsequent independence of row and minor give

    E|G_xy|^s <= sigma^(-s)c_s sum_u E[|H_xu|^s |G^(x)_uy|^s]
              = c_s b_s sum_(u neighbor x) E|G^(x)_uy|^s,
    b_s = Gamma(1+s/2).

Here E|H_xu|^s=sigma^s b_s because a standard circular complex Gaussian Z has E|Z|^2=1 and |Z|^2 is exponential of mean one. All powers of sigma cancel. Thus the row sum of this scalar upper-bound kernel is

    q_s(W) = (5 W^2-1) 2^(-s/2)
             Gamma((1-s)/2) Gamma(1+s/2)/sqrt(pi).

This coefficient NEVER satisfies the usual sufficient contraction condition q_s(W)<1. Indeed Jensen's inequality, applied separately to the two exponential moments, gives

    c_s b_s = E exp(-s log|g|) E exp(s log|Z|)
            >= exp(s (E log|Z|-E log|g|))
            = 2^(s/2)>1.

The log moments are E log|g|=-(gamma+log 2)/2 and E log|Z|=-gamma/2; derive them by differentiating their Gamma moment formulas at zero. Both logarithms are integrable. Consequently q_s(W)>5 W^2-1>=4 for every W>=1 and every 0<s<1. This is an analytic statement for ALL s, not a sampled optimization.

This obstructs only the route that uses (i) a sitewise uniform scalar diagonal average, (ii) absolute values and fractional subadditivity on the entire row, and (iii) the above row-sum contraction criterion. It does not exclude a block fractional-moment criterion, correlated/cancellation estimates, energy-dependent bounds, multiscale analysis, or localization itself. On a principal minor some row degrees shrink; the obstruction is to initiating a uniform full-model contraction, not a claim that every late minor has the same degree.

The prior C0054-A001 record says that band matrices have no rank-one structure. Taken literally this is false: H_xx enters as H_xx e_x e_x^*, a rank-one diagonal perturbation. The rank-one scalar average above exists. What fails here is contraction after summing many comparable off-diagonal channels, not absence of rank-one diagonal randomness.

The missing bridge for this route is an energy/scale-dependent bound on a block-boundary resolvent transfer that retains more information than a sum of positive scalar fractional moments. Such a bound must be proved uniformly over the necessary energies, exterior conditioning, and sufficiently large volumes, with the bandwidth fixed before the volume limit. Its existence is not asserted here.

NEXT: Pin original Bourgade conjecture and read w609's frozen bridge, then check whether it evades these three losses with a derived conditional law.

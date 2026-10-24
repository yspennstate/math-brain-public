# P0324 ? second serious attempt, 2026-10-12

The outstanding target is all-positive-beta analyticity for the unrestricted circular positive-exponent Riesz gas. The previous attempt reduced it to extensive factorial bounds for all total-energy cumulants, but did not establish those bounds.

Two new routes, not pursued in the first attempt:

A. Neutral-cell polymer expansion. Write positions at unit density as i+u_i and subtract the energy and first variation of the regular lattice. Pair remainders then involve the second derivative of the Riesz potential, with tail |i-j|^{-s-2} rather than |i-j|^{-s}. This tail has a summable first moment. Try a Kotecky-Preiss expansion using the single-cell measure as reference; then audit whether a constraint on u_i can be removed or replaced by blocks/defects. A compact-displacement version should yield a real theorem with all-order cumulant control, but it is not automatically a theorem for the unrestricted gas.

B. Massless Gaussian gradient expansion. Expand about the regular lattice without bounding absolute displacements. The lattice Hessian has symbol of order |theta|^{1+s}; displacement differences fluctuate, but gradients have covariance of order |i-j|^{s-2}, which is summable for s<1. A linked-cluster expansion in these gradients could preserve the necessary infrared cancellations and bypass bounded-displacement assumptions. The harmonic energy itself has explicit factorial cumulants. The main obstacles are uniform control of the nonlinear Taylor remainder, near collisions and large gaps, and convergence at arbitrary beta. This would initially target a low-temperature interval, then require further work for all temperatures.

Choice: pursue A first. Its neutral-pair bounds and summable first moment allow explicit estimates against a named polymer theorem. The test is whether the resulting theorem applies to the unrestricted model, not merely whether the formal tail looks short-range.

Brain queries made: "complete analyticity truncated correlations tree cumulant convex Gibbs Helffer Sjostrand"; "Kotecky Preiss polymer expansion tree graph analyticity"; "Ruelle one dimensional interaction first moment analyticity transfer operator". No applicable ready-made closure was returned. All cards are treated as hints.

Results and full proofs will be saved below as they are checked.

## First checked reduction: exact neutral pair decomposition

At unit density write G_N(t)=N^{-s}g_s(t/N), x_i=i+u_i, i=0,...,N-1. For a fixed 0<a<1/4 restrict u_i to [-a,a]. Put E_N=2 zeta(s)(N-N^{1-s}), already proved in ATTEMPT.md. Define

    W_{ij,N}(u_i,u_j)=2[G_N(r+delta)-G_N(r)-G_N'(r)delta],
    r=j-i, delta=u_j-u_i, i<j.

The full source Hamiltonian satisfies exactly

    H_N(x)-E_N=sum_{i<j} W_{ij,N}.

Reason: the regular lattice is a stationary point; its gradient vanishes by G_N'(N-r)=-G_N'(r), including the zero derivative at r=N/2 when N is even. Therefore the sum of the linear terms is identically zero for every vector u. This uses the source's ordered-pair convention, hence the factor 2 in W.

Let p=s+2, K=4a^2 s(s+1)(1-2a)^{-p}, and D=2K zeta(p). Taylor's integral remainder and |delta|<=2a show

    0<=W_{ij,N}<=J_{ij,N}:=K sum_{m in Z}|j-i+mN|^{-p},
    sup_i sum_{j!=i} J_{ij,N}<=D.

The row sum enumerates integers not divisible by N and is bounded by the sum over all nonzero integers. Crucially D is independent of N. A polymer proof will be completed below. The asserted conclusion will be restricted-model analyticity, not unrestricted-model analyticity.

## 1. A checked restricted-model theorem

For 0<s<1 and 0<a<1/4, define

    p=s+2,
    K=4a^2 s(s+1)(1-2a)^{-p},
    D=2K zeta(p),
    R=1/(256D).

Let u_0,...,u_{N-1} have independent uniform reference measure on [-a,a], and put

    Q_N(z)=integral exp[-z(H_N(i+u_i)-E_N)] product_i du_i/(2a).

THEOREM (restricted model only). For every N, Q_N(z) is zero-free on |z|<R. Its logarithm with log Q_N(0)=0 satisfies |log Q_N(z)|<=N there. The limit

    p_a(z)=lim_N N^{-1}log Q_N(z)

exists locally uniformly on that disk and is holomorphic. Thus the canonical cell-constrained free-energy limit is real analytic for 0<beta<R. In particular, for each fixed target beta_0>0 one can choose a sufficiently small a so that this CONSTRAINED model is analytic near beta_0. This changes the model and does not prove the assertion of P0324.

### 1.1 Full justification of the pair bounds

Let v(t)=|t|^{-s} for t!=0. For any nonzero integer d and |delta|<=2a,

    w_d(delta)=2[v(d+delta)-v(d)-v'(d)delta]
              =2 delta^2 integral_0^1 (1-t)v''(d+t delta)dt.

The segment never crosses zero and v''(x)=s(s+1)|x|^{-s-2}. Therefore w_d>=0 and

    w_d(delta)<=delta^2 s(s+1)(1-2a)^{-p}|d|^{-p}
                 <=K|d|^{-p}.                           (1.1)

The differentiated periodic kernel has an absolutely convergent second-derivative image series, and its first-derivative image series is also absolutely convergent since s>0. Its regularized additive constants disappear in Taylor differences. Integrating the second derivative along the segment gives

    W_{ij,N}=sum_{m in Z} w_{j-i+mN}(u_j-u_i).             (1.2)

This series is absolutely and uniformly convergent by (1.1). It proves the nonnegativity, the stated J bound, and the row sum bound D without manipulating the divergent unregularized potential series. The exact total-energy identity was established above by cancellation of the full first variation. The formula also shows why wrap-around pairs cannot be omitted.

### 1.2 Exact graph-to-polymer identity

Write f_{ij}(z,u)=exp[-z W_{ij,N}(u)]-1. Since W is bounded,

    |f_{ij}|<=b_{ij}:=|z| J_{ij,N} exp(|z| J_{ij,N}),
    sup_i sum_{j!=i} b_{ij}<=b:=|z|D exp(|z|D).            (1.3)

The bound follows from exp(-zW)-1=-zW integral_0^1 exp(-tzW)dt. Also J_{ij}<=D. For any vertex set S with |S|>=2 define its activity

    rho_S(z)=integral sum_{connected graphs G on S}
                    product_{edges ij in G} f_{ij}(z,u)
                    product_{i in S} du_i/(2a).

All activities are entire functions for each finite N. Expanding product_{i<j}(1+f_{ij}) and splitting every graph into its connected components shows EXACTLY that

    Q_N(z)=sum_{pairwise-disjoint families of sets S}
                   product_S rho_S(z).                  (1.4)

Isolated vertices integrate to one and need no polymer. Incompatibility is intersection, including self-intersection. No independence of the f_{ij} is asserted: the integration factors over disjoint connected components because the reference measure is a product over sites.

### 1.3 Activity majorant and explicit smallness

Every connected graph contains a spanning tree. Since all b_{ij} are nonnegative, overcounting graphs by their spanning trees yields

    sum_{connected G on S} product_{ij in G} b_{ij}
      <= sum_{trees T on S} product_{ij in T} b_{ij}
                              product_{ij not in T}(1+b_{ij})
      <= exp(|S| b/2) sum_T product_{ij in T} b_{ij}.       (1.5)

Indeed the sum of all internal edge weights is at most |S|b/2 by the row bound. Integrating cannot increase this uniform majorant.

Fix a site i. For |S|=m, label its other m-1 sites and divide by (m-1)!. For any fixed labeled tree rooted at i, summing the site assignments from the leaves inward costs at most b for each of its m-1 edges. We may drop the distinctness constraints for an upper bound; set b_{ii}=0. Cayley's tree count is m^{m-2}. Therefore

    sum_{S contains i, |S|=m} |rho_S(z)|
       <= exp(mb/2) [m^{m-2}/(m-1)!] b^{m-1}.             (1.6)

The coefficient is <=exp(m): it equals m^{m-1}/m!, which is at most m^m/m!, one term of the positive series exp(m). Consequently

    sum_{S contains i} |rho_S(z)| exp(|S|)
      <=sum_{m>=2} exp[m(2+b/2)] b^{m-1}
       = exp(2q)b/[1-exp(q)b], q=2+b/2.                  (1.7)

For |z|D<1/256, the elementary bound exp(x)<=1/(1-x) for 0<=x<1 gives b<1/255<1/128. For b<=1/128, q<=2+1/256. The exponential series gives exp(1)<3, while exp(1/256)<=256/255, so exp(q)<9(256/255)<10. Hence the right-hand side of (1.7) is at most

    100b/(1-10b)<=100/(128-10)=50/59<1.                 (1.8)

The last rational step is formally checked in ClusterConstants.lean. All bounds hold uniformly in N and throughout the complex disk |z|<R, not just on the real axis.

### 1.4 Named theorem and checked hypotheses

Known theorem used: the Kotecky-Preiss abstract-polymer criterion. If nonnegative majorants r_S and nonnegative numbers A_S satisfy

    sum_{T incompatible with S} r_T exp(A_T)<=A_S,

then the logarithmic connected-cluster series converges absolutely for activities of absolute value at most r_S. The finite polymer partition is zero-free, and its pinned logarithmic-derivative majorant is at most exp(A_S). In particular

    |log Xi|<=sum_S r_S exp(A_S).

The logarithm is the branch vanishing at zero activities. This last bound follows by integrating the pinned derivative along t rho, 0<=t<=1; the same majorant holds on this segment.

Reference read, not inferred from a title: Roberto Fernandez and Aldo Procacci, *Cluster expansion for abstract polymer models. New bounds from an old approach*, arXiv:math-ph/0605041v2 (16 October 2006), PDF pages 3-4, equations (2.7), (2.10)-(2.15). Equation (2.15) is precisely the criterion above, and (2.14) gives the pinned bound. This standard theorem is the external input; the application and numerical constants are proved here.

Use A_S=|S| and r_S equal to the uniform majorant in (1.5). A polymer incompatible with S contains at least one site of S, so (1.7)-(1.8) give

    sum_{T intersects S} r_T exp(|T|)
        <=sum_{i in S} sum_{T contains i} r_T exp(|T|)
        <=(50/59)|S|<=|S|.

Every hypothesis is now satisfied: a finite polymer family; intersection incompatibility, including self-incompatibility; entire activities; and volume-independent complex majorants. Moreover

    sum_S r_S exp(|S|)
      <=sum_i sum_{S contains i} r_S exp(|S|)<=N.

Thus Q_N is zero-free and |log Q_N|<=N on |z|<R. The cluster logarithm agrees with the actual branch by (1.4) and its value at zero. For completeness, convergence of the cluster series gives a holomorphic function L_N on each smaller disk. Near z=0 its formal connected-graph identity yields exp(L_N)=Q_N. The holomorphic identity theorem extends this equality to the disk, proving zero-freeness directly and identifying L_N as the desired logarithm. The uniform pinned bounds give its stated modulus bound. This proves the finite-volume part of the theorem.

### 1.5 Thermodynamic limit, including the periodic/interval comparison

We prove real convergence first and then holomorphic convergence; zero-freeness by itself is not called a thermodynamic-limit proof.

Define the infinite-line finite-interval energy

    U_L=sum_{0<=i<j<L} w_{j-i}(u_j-u_i),
    q_L(beta)=integral exp(-beta U_L) product_i du_i/(2a).

The positive pair terms imply, for beta>=0,

    log q_{L+M}(beta)<=log q_L(beta)+log q_M(beta).

Also 0<=U_L<=LD/2, so log q_L>=-beta LD/2. A short proof of the subadditive limit: for a fixed block length L, write n=kL+r, 0<=r<L. Subadditivity gives log q_n<=k log q_L+log q_r, with q_0=1. Dividing by n and sending n to infinity gives limsup <=(log q_L)/L. Taking the infimum over L and using the trivial lower bound by that infimum gives existence of lim_n log q_n/n, finite by the extensive bound.

By (1.2), the periodic energy differs from U_N by the nonnegative sum over nonzero images. The difference has a uniform, NONEXTENSIVE bound:

    0<=H_N-E_N-U_N
       <=K sum_{r=1}^{N-1}(N-r) sum_{m!=0}|r+mN|^{-p}
       <=2K zeta(p-1).                                 (1.9)

For the second inequality, each integer d=r+mN is counted at most once. If m=-1, N-r=|d|; if m>=1 or m<=-2, N-r<=N<=|d|. Thus each summand is bounded by |d|^{1-p}, and the entire sum is bounded by the sum over all nonzero integers, 2 zeta(p-1), which is finite because p-1=s+1>1. This is where the summable FIRST MOMENT matters.

For real beta>=0, (1.9) gives

    |log Q_N(beta)-log q_N(beta)|<=2 beta K zeta(p-1).

Consequently N^{-1}log Q_N has the same finite real limit for every beta>=0. The polymer bound makes N^{-1}log Q_N locally bounded holomorphic functions on |z|<R. Montel's theorem supplies subsequential locally uniform limits; all coincide on (0,R) with the real limit just proved, and hence coincide everywhere on the disk by the identity theorem. The whole sequence converges locally uniformly, proving the thermodynamic assertion.

The full constrained pressure with unnormalized cell Lebesgue measure is

    P_cell(beta)=log(2a)-2 beta zeta(s)+p_a(beta),

because E_N/N->2 zeta(s). It is therefore analytic on (0,R). Rotating the cell array and including the associated polynomial translation factor does not change the limiting pressure, but does not remove the one-particle-per-cell restriction.

### 1.6 The requested factorial cumulant bounds really hold in this model

For any beta_0 in (0,R), let r=(R-beta_0)/2. Cauchy's derivative estimate applied to |N^{-1}log Q_N|<=1 gives

    |kappa_{k,N,beta_0}(H_N-E_N)|<=N k! r^{-k}, k>=1.

The derivatives are cumulants because the finite-volume cell partition is a Laplace transform. For k>=2 the cumulants are unaffected by E_N. Thus the missing bound from the first attempt is PROVED for the restricted model, with explicit constants and uniformity in volume. No such bound is claimed for the unrestricted source gas.

## 2. Hostile transfer audit: why this theorem does not settle P0324

### 2.1 A rigorous positive pressure gap in an overlapping temperature regime

This goes beyond observing that the probability of a constraint might vanish. Let the unit-density circle have length N. The canonical full partition, dividing the full labeled integral by N!, is

    Z_full,phys=(N^N/N!)[(N-1)! Z_N(beta)].

Independent uniform labeled points have E H_N=0, as checked in ATTEMPT.md. Jensen's inequality gives

    Z_full,phys>=N^N/N!,
    liminf_N N^{-1}log Z_full,phys>=1.                    (2.1)

The cell event is exactly one particle in each disjoint interval [i-a,i+a], i=0,...,N-1, interpreted periodically. Its labeled integral has N! equal assignment sectors. Thus its contribution to the canonical partition is exactly

    Z_cell,phys=(2a)^N exp(-beta E_N) Q_N(beta).

For real beta>=0, the remainder energy is nonnegative, so Q_N(beta)<=1. It follows that

    limsup_N N^{-1}log Z_cell,phys
        <=log(2a)-2 beta zeta(s).

Therefore the full and cell pressures have a strictly positive separation whenever

    1-log(2a)+2 beta zeta(s)>0.                           (2.2)

This is NOT a counterexample to analyticity of the full pressure. It is a proof that the constrained analytic pressure cannot simply be substituted for the full pressure in this regime. It also gives an exponential upper bound for the full Gibbs probability of this fixed cell event, with rate at most log(2a)-2 beta zeta(s)-1<0.

The regimes do overlap. For example s=1/2, a=0.02 gives R approximately 1.09557, while beta=1 satisfies (2.2) with margin approximately 1.29817. These approximations are illustrative only; the exact criterion is (2.2). More generally, as a->0, R grows like a^{-2}, while 1-log(2a) diverges. For ANY fixed beta_0>0, choosing a sufficiently small makes both beta_0<R and (2.2) true. Thus arbitrarily tight cells can provide analyticity at a prescribed temperature and simultaneously miss an extensive amount of the actual partition.

### 2.2 Bounded matching conflicts with the source CLT

Any infinite-volume limit of the cell-constrained configurations has an ordered lattice representation x_i=i+u_i with |u_i|<=a, possibly plus a common translation. Hence

    |(x_{i+k}-x_i)-k|<=2a for every k,
    k^{-s/2}[(x_{i+k}-x_i)-k]->0 deterministically.

Boursier's Theorem 5, PDF page 5, instead gives convergence to a centered Gaussian of positive variance for the corresponding long-distance gap fluctuations in the actual Riesz_{s,beta} process. A difference of one in the source's index convention disappears after the k^{-s/2} scaling. The variance formula in that theorem is strictly positive for s in (0,1). Thus the bounded-displacement model cannot be identified with that limiting point process at any positive beta. This distributional mismatch alone would not prove a pressure gap; Section 2.1 proves a pressure gap separately where (2.2) holds.

### 2.3 Removing the constraint destroys the uniform pair bound

For unrestricted ordered configurations an adjacent distance can approach zero. In the remainder at r=1, delta approaches -1 from above, and

    w_1(delta)=2[(1+delta)^{-s}-1+s delta]->infinity.

Thus the bounded J_{ij} and the uniform product-reference estimates (1.3) are unavailable on the full source domain. The ordered domain is also not a product of unconstrained displacement intervals. It is not legitimate to keep the cell activity estimates while replacing their reference measure by the full Gibbs law.

### 2.4 Allowing occupation defects restores a nonsummable monopole tail

A natural next repair is to let cells be empty or contain multiple particles. Write a cell charge measure as nu_i=(particles in cell i)-(Lebesgue background restricted to that cell), with total charge q_i=occupancy_i-1. For two cells a distance R apart and bounded relative cell supports, Taylor expansion gives

    integral integral |R+x-y|^{-s} dnu_i(x)dnu_j(y)
       =q_i q_j R^{-s}+O(R^{-s-1}).                     (2.3)

To justify the error, on supports |x-y|<=C and R>2C the mean-value theorem bounds the difference from R^{-s} by s C (R-C)^{-s-1}; multiplying by the finite total variations of nu_i,nu_j gives the stated estimate. If both cells are neutral, applying a second-order Taylor expansion cancels the constant and linear terms and yields an R^{-s-2} bound instead. In that case the absolute double integral is bounded by a constant times R^{-s-2} times the total variations and support-size squared.

For nonzero q_i q_j, the leading tail in (2.3) is not absolutely summable in one dimension when s<1. Global canonical neutrality sum_i q_i=0 does not imply individual-cell neutrality. Alternating empty/double cells are admissible neutral canonical patterns, but the absolute monopole tail still has divergent sum_r r^{-s}. Conditional cancellation is different from the absolute majorants required by the cluster proof above. Grouping charges into neutral variable-sized blocks could recover the short-range tail, but requires volume-uniform activity bounds for those blocks, control of their sizes, and their complex-temperature dependence. None follows from the previous two-gap covariance theorem or the variance bound.

## 3. Checks and outcome

All new numerical experiments completed in seconds to minutes and used small arrays:
- second_numerics.py checks the exact periodic decomposition (including the vanishing linear sum and image contributions) for s=0.2,0.5,0.8 and N=2,3,5, using deterministic displacements in a=0.02 cells.
- It verifies the pair majorant and exhaustively enumerates connected graphs and spanning trees on 2,3,4,5 vertices, comparing the finite weighted sums in (1.5).
- second_numerics.json saves the results and the explicit disk radii for several (s,a).
- ClusterConstants.lean checks the rational majorant (1.8). The formal check does not certify the external polymer theorem, analytic integrals, or passage to the thermodynamic limit.

Remaining gap after this attempt: construct an analytic, uniformly convergent expansion for the unrestricted gas which tolerates unbounded collective displacement and variable cell occupancy while controlling the restored monopole interactions; or prove all-order energy cumulant estimates directly by a massless-gradient method. The restricted-model theorem does not bridge this gap. No full solution or counterexample for P0324 is claimed. The original verdict remains PARTIAL, with a new proved constrained-model result and a precise failure of the naive transfer.


Final verification record: second_lean_check.txt reports EXIT_CODE=0, with only an unused-variable linter warning. ClusterConstants.lean contains no sorry and uses no native_decide. Initial attempts corrected an accidentally replaced import path and the Unicode subscript in a library lemma name before the successful run. The kernel checked only the rational cutoff, not the full polymer theorem.

The maximum sampled periodic-decomposition residual was 9.06e-16; the maximum W/J ratio was 0.650283, below 1. Connected-graph/tree-majorant ratios for 2-5 vertices were approximately 0.999500, 0.998619, 0.997834, 0.996845, all below 1. A further direct test of the graph-to-polymer identity on four sites with three-point product quadrature at z=0.5+0.1i agreed within 2.23e-16 (polymer_identity_check.json). This last check is an exact finite-spin identity test subject to floating-point error, not a claim about quadrature accuracy for the continuous partition.

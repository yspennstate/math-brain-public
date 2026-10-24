# C0052: sharp boundary packet (w474)

2026-10-10. Author proof; independent review pending. Served model/account evidence is unavailable in this thread; requested runtime settings are not evidence of served identity.

## Target recovery

Primary source: Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, arXiv:1707.00520v1, section 7, equations (7.1)-(7.2), Conjecture 6, printed p. 94 (PDF index 93), https://arxiv.org/pdf/1707.00520. Exact first-half quote: "Prove that the three-dimensional Ising model is non-trivial". The source fixes ferromagnetic nearest-neighbor interactions, zero external field, and the free infinite-volume Gibbs state. Its four-dimensional half is historical: Aizenman-Duminil-Copin, https://arxiv.org/abs/1912.07973, proves Gaussian scaling in d=4. Current openness of the d=3 problem is UNKNOWN after a bounded check; no novelty claim is made.

For beta<beta_c, set G_beta(x)=E_beta[sigma_0 sigma_x], chi(beta)=sum_x G_beta(x), and xi(beta)=[lim_n -n^{-1} log G_beta(n e_1)]^{-1}. For mean-zero spins, U4(x1,x2,x3,x4)=E[sigma_x1 sigma_x2 sigma_x3 sigma_x4]-G(x1-x2)G(x3-x4)-G(x1-x3)G(x2-x4)-G(x1-x4)G(x2-x3). The source uses the SIGNED convention

    g(beta) = sum_{x2,x3,x4} U4(0,x2,x3,x4) / [chi(beta)^2 xi(beta)^3].

Its target is g(beta) NOT tending to 0 as beta increases to beta_c. Because g<=0 for this Ising model, the exact nonvanishing statement is: there exist epsilon>0 and a sequence beta_n increasing to beta_c with -g(beta_n)>=epsilon. A positive liminf would be stronger; a bound for every endpoint quadruple would be stronger still. The source does not, by this conjecture alone, ask for uniqueness of a full critical continuum limit or universality over all finite-range interactions. A non-Gaussian finite-box zero mode in a different model, boundary condition, or order of limits is not this target.

## Prior attempt and the hardest gap

C0052-A001 (attempts.jsonl:42, 2026-09-07) proposes a random-current intersection second moment. It does not establish its variance bound. Its claimed reduction to C0051 and fractal-dimension calculation are heuristic, not a proved equivalence. A lower bound on the mean number of intersections does not lower-bound the probability of any intersection without an adequate second-moment or other tail estimate. The hardest parent gap is a scale-uniform lower bound on the properly weighted four-point/random-current intersection observable, relative to the square of the block variance.

## L1: sharp Gaussian-sign residual inequality

Let (X,Y) be centered jointly Gaussian with unit variances and correlation r in [0,1]. Write b=sqrt(2/pi), H(x)=sign(x)-b*x, with sign(0) arbitrary. Then

    E[H(X)H(Y)] = (2/pi)(arcsin(r)-r)
    0 <= E[H(X)H(Y)] <= (1-2/pi)*r^3.

The constant 1-2/pi is optimal, with equality at r=1.

Proof. Represent X and Y as projections of a rotationally invariant planar standard Gaussian onto unit vectors making angle arccos(r). Its direction is uniform, so E[sign(X)sign(Y)]=(2/pi)arcsin(r). Gaussian regression gives E[X sign(Y)]=b*r and its symmetric counterpart. Expansion of H therefore gives the displayed identity. The arcsin series has positive coefficients, starts with r, and all remaining terms have degree at least 3. For 0<=r<=1 each such power is at most r^3; their coefficient sum at r=1 is pi/2-1. Multiplying by 2/pi proves the inequality. At r=1 the left side is Var(H(X))=1-2/pi, proving sharpness. No independence between different lattice sites is asserted or used.

## L2: bounded, positively associated spins with a Gaussian power-law scaling limit

For each fixed gamma in (0,3), there is a stationary, spin-flip symmetric field sigma_x in {-1,1}, x in Z^3, with positive association and

    E[sigma_0 sigma_x] = (2/pi) arcsin[(1+|x|^2)^(-gamma/2)]
                       ~ (2/pi)|x|^(-gamma).

Nevertheless, for every finite list of real compactly supported smooth tests f, the variables

    S_N(f)=N^(-3+gamma/2) sum_x f(x/N) sigma_x

converge jointly to a centered Gaussian vector with covariance

    (2/pi) integral integral f(u) h(v) |u-v|^(-gamma) du dv.

This is a claim about smeared finite-dimensional distributions; no assertion of tightness in a topology on distributions is needed or claimed. For a nonzero nonnegative test the limiting variance is strictly positive. Every on-site fourth cumulant is exactly -2. In particular gamma=1+eta for any fixed eta in (0,2) gives a positive anomalous two-point exponent and a Gaussian limit.

Proof of existence. R_gamma(x-y)=(1+|x-y|^2)^(-gamma/2) is positive definite: it equals

    1/Gamma(gamma/2) integral_0^infinity t^(gamma/2-1) exp(-t) exp(-t|x-y|^2) dt.

For each t>0 the last kernel is positive definite by its nonnegative Gaussian Fourier transform. The positive mixture has R_gamma(0)=1, hence defines a stationary unit-variance Gaussian field G_x on the countable lattice. Put sigma_x=sign(G_x). L1 proves the stated covariance, and Gaussian symmetry proves spin-flip symmetry. The single-site spin is an equiprobable sign, so E sigma_0^4 -3(E sigma_0^2)^2=1-3=-2.

Positive association. For any finite covariance matrix C with nonnegative entries, take two Gaussian vectors with common marginal covariance C and cross covariance t*C, 0<=t<=1. Gaussian differentiation gives

    d/dt E[F(X) H(Y_t)] = sum_ij C_ij E[(partial_i F)(X)(partial_j H)(Y_t)] >= 0

for smooth coordinatewise increasing bounded F,H. At t=0 the vectors are independent; at t=1 they coincide. This proves nonnegative covariance of such functions of G. Approximate increasing functions of its signs by monotone mollification and use dominated convergence; sigma inherits positive association. A singular finite covariance can first be regularized by independent Gaussian noise and then obtained by a limit. This is positive association, not an assertion of every Ising GKS/GHS or random-current identity.

Gaussian projection. Let b=sqrt(2/pi), H_x=sigma_x-b*G_x. For arbitrary fixed f, with support inside a fixed cube and bounded sup norm, L1 gives

    E|S_N(f)-b*T_N(f)|^2
      <= C_f N^(-3+gamma) sum_{|z|<=C_f N} (1+|z|^2)^(-3gamma/2),
    T_N(f)=N^(-3+gamma/2) sum_x f(x/N)G_x.

The signed f is handled by absolute values; no independence between H_x is assumed. Shell counting in Z^3 bounds the displayed error by

    C_f,gamma N^(-2gamma)                 for 0<gamma<1;
    C_f N^(-2) log(2+N)                  for gamma=1;
    C_f,gamma N^(-(3-gamma))              for 1<gamma<3.

Constants are for fixed gamma and fixed f, not uniform at the transition points. These bounds tend to zero.

Covariance limit of T_N. Rewriting its covariance as a Riemann sum gives the kernel (N^(-2)+|u-v|^2)^(-gamma/2). Off |u-v|<=delta this converges uniformly to |u-v|^(-gamma). The contribution of the diagonal and the delta-neighborhood is at most C[N^(gamma-3)+delta^(3-gamma)], by the same shell count, while the corresponding continuum integral is at most C delta^(3-gamma). Take N to infinity, then delta to zero. The Gaussian vector T_N consequently has the displayed limiting covariance without its factor b^2. Its L2-small remainder transfers joint convergence to S_N. This completes the proof.

Endpoint check. At gamma=0 take G_x=Z for every x. Then N^(-3)sum f(x/N)sigma_x tends to sign(Z) integral f, a two-point distribution for integral f !=0, so this extension is not Gaussian. At gamma=3 the stated normalization is not tight for a nonnegative test positive on a cube: Var(T_N) grows like log N while Var(S_N-b*T_N) stays bounded. For fixed M,A>0, P(|S_N|<=M)<=P(|b*T_N|<=M+A)+P(|S_N-b*T_N|>A); the first term tends to zero, and the second is bounded by C/A^2. Let A grow. These endpoints explain the stated open interval; no sharpness claim is made about every remainder rate.

Boundary verdict. L2 refutes the auxiliary implication "stationary spin-flip symmetric bounded spins + positive association + |x|^(-(1+eta)) correlations with eta>0 + a nonzero local fourth cumulant imply a non-Gaussian smeared scaling limit." It does NOT refute C0052: this sign field has not been shown to be a nearest-neighbor Ising Gibbs state, reflection positive, or to satisfy the required random-current identities. It also does not refute the prior attempt's explicitly conditional second-moment statement with its missing variance assumption added.

## L3: exact contact contribution for a translation-invariant spin field

Let sigma_x be a translation-invariant mean-zero {-1,1} field on Z^3 (or a finite group), with 0<=G(x)=E sigma_0 sigma_x<=1 and finite chi=sum_x G(x). Write B=sum_x G(x)^2. Let D be the set of ordered triples (x2,x3,x4) for which at least two of (0,x2,x3,x4) coincide. Then

    K_D := sum_D [-U4(0,x2,x3,x4)]
         = 12 chi^2 - 16 chi - 6 B + 12,
    0 <= K_D <= 12 chi^2.

Thus the magnitude of the contact contribution to the source's g(beta) is at most 12/xi(beta)^3. In any near-critical Ising regime with xi going to infinity, it vanishes. If chi also goes to infinity, K_D/chi^2 tends to 12 since B<=chi. The coefficient 12 cannot be decreased uniformly over the stated class: N perfectly correlated spins on a finite cyclic group have chi=B=N, giving K_D=12N^2-22N+12 and K_D/chi^2 tending to 12.

Proof. For one repeated pair,

    U4(a,a,b,c)=-2G(a-b)G(a-c).

Summing the negative cumulant over any one of the six pair-coincidence planes gives 2 chi^2, by translation invariance. Their sum is 12 chi^2 but counts a tuple once per equal pair. Tuples with exactly three equal indices have multiplicity 3; the four choices of singleton sum to 8(chi-1), so their excess count is twice that. Tuples forming exactly two distinct pairs have multiplicity 2; the three partitions sum to 6(B-1), so their excess is that sum. The all-equal tuple has value -U4=2 and multiplicity 6, so its excess is 10. Subtracting gives 12chi^2-16(chi-1)-6(B-1)-10, the claimed identity. Every contact term is nonnegative by these repeated-spin identities; the union is bounded by the sum of its six planes. Absolute summability follows from finite chi. This completes the proof.

Implication for the parent attempt. On-site cumulants and all exact coincidence planes are insufficient to keep the renormalized coupling nonzero. The remaining mass must come from four distinct sites. L3 only removes exact contacts: distinct sites may still be microscopically close, and no claim about all near-diagonal neighborhoods is made.

## Single hardest remaining parent gap

Prove a positive subsequential lower bound for the normalized four-DISTINCT-site sum of -U4 as beta increases to beta_c, with the source's chi^2 xi^3 normalization. In the current representation this requires a quantitatively weighted lower bound for the all-four-connected event of the union of the two specified sourced currents; a mean intersection count or a two-point exponent alone does not supply it. Existence or uniqueness of a full critical continuum field is a separate stronger problem.

NEXT: Run the fresh resource gate and bounded diagnostics; send L1-L3 with scope restrictions to w476 and prepare a concept-only DRAFT bundle.

# P0320 — research record, 2026-10-11

## Exact question and verified scope

For an infinite-volume Riesz gas, determine whether the number of points in every bounded Borel set is measurable with respect to its exterior configuration, in the band s in (d-2,d-1]. The gas ensemble, boundary convention, temperature, and choice of subsequential limit matter. No universal ensemble specification is supplied by the problem statement.

Thoma, arXiv:2303.11486v1, Introduction p. 2, explicitly says that this band remains open in all dimensions. His proved Proposition 1 instead concerns Coulomb finite-volume approximants in d>=3, inverse temperatures delta<=beta_N<=delta^-1, potentials with Laplacian bounded above, and a non-vacuum annular-density hypothesis on the limit. These hypotheses are NOT a proved Riesz theorem. The assertion in the intake that everything outside the band is settled is too broad without specifying models and parameter ranges.

For d>=2 in the present band, s>0 and the pair kernel is g(x)=|x|^-s (positive normalization factors do not change the arguments below). For d=1 the negative-exponent convention is -|x|^-s, and s=0 means -log|x|. The positive-kernel arguments below do not apply to these d=1 models.

## Proved smoothing estimate

Let d>=2, 0<s<d, s>d-2, and let nu be normalized Lebesgue measure on B_1(0). Write Ag(z)=int g(z+u) nu(du), and w(z)=(Ag(z)-g(z))_+, with w(0)=0. Then there is a finite constant C(d,s) with

    0 <= w(z) <= C(d,s)(1+|z|)^(-s-2).

In particular w is bounded and integrable on R^d.

Proof. For |z|<=2, Ag(z) is at most |B_1|^-1 int_{B_3}|v|^-s dv, which is finite because s<d. Since g>=0, this bounds w. For |z|>2, differentiation gives

    Hess g(z) = s(s+2)|z|^(-s-4) z z^T - s|z|^(-s-2) I.

The radial eigenvalue is s(s+1)|z|^-s-2, and each tangential eigenvalue is -s|z|^-s-2. Along z+tu, |u|<=1, 0<=t<=1, the Hessian operator norm is at most s max(1,s+1) 2^(s+2)|z|^-s-2. Taylor's formula with integral remainder, followed by integration in u, eliminates the first-order term because int u nu(du)=0. The absolute averaged remainder is at most half this bound times int |u|^2 nu(du), which is <=1. This proves the claimed bound, after changing C on |z|<=2. Its radial tail is int_2^infinity r^(d-s-3)dr, finite because s>d-2. All averages exist since s<d. QED.

The earlier brain attempt only observed far-field Hessian integrability. This estimate additionally handles the collision singularity in the positive averaging error.

## Proved obstruction to an unconditional extension of Thoma's Lemma 1

For d>=2 and d-2<s<d, Thoma's uniform mimicry bound for arbitrary nonnegative frozen exterior measures fails for the Riesz kernel.

Proof. Put a=-2e_1, b=2e_1, c=2e_2 and mu=M delta_c. Consider two mobile particles at a,b, and W=0. The energy is H=g(a-b)+M[g(a-c)+g(b-c)]. Moving either mobile particle to a uniform unit ball about the other gives an averaged energy difference

    c_0 - g(a-b) + M D,
    c_0 = int_{B_1} g(u)nu(du),
    D = Ag(a-c)-g(a-c) = Ag(b-c)-g(b-c).

Reflection in the first coordinate proves the equalities. On the closed unit ball about a-c the kernel is smooth, and

    Delta g(z)=s(s+2-d)|z|^-s-2 > 0.

Thus its spherical means are strictly greater than its central value for every radius in (0,1]; the identity follows by differentiating the spherical mean and applying the divergence theorem. Averaging these means in radius gives D>0. Therefore both averaged energy differences tend to infinity as M tends to infinity. No constant independent of mu can bound the better direction. The measure mu need not be a physical exterior gas: the point is precisely that the deterministic lemma quantified over arbitrary nonnegative measures. QED.

This obstruction does not disprove non-rigidity. It identifies the uniformity that a Riesz adaptation must replace with probabilistic control.

## Conditional non-rigidity theorem (proved reduction, not a solution of P0320)

Here is a precise sufficient criterion that replaces Coulomb superharmonicity and the conditioned-density theorem in Thoma's argument. It is deliberately stated with stronger assumptions than have been verified for the Riesz gases of the question.

**Theorem.** Let d>=2, max(0,d-2)<s<d, and let P_N be permutation-invariant N-particle Gibbs laws on (R^d)^N, with density proportional to

    exp(-beta_N H_N),
    H_N = sum_{i<j} |x_i-x_j|^-s + sum_i W_N(x_i).

Assume the normalizers are finite and positive and that:

1. 0<beta_N<=b for a fixed b<infinity; W_N is C^2 and Hess W_N <= L I everywhere for a fixed L>=0.
2. Globally and uniformly in N, the first and second factorial moment measures have Lebesgue densities rho_N^(1)<=a_1 and rho_N^(2)<=a_2, for finite constants a_1,a_2. Precisely, for nonnegative measurable h,

       E_N sum_i h(x_i) <= a_1 int h(x)dx,
       E_N sum_{i!=j} h(x_i,x_j) <= a_2 int h(x,y)dxdy.

3. The point-configuration laws P_N converge weakly along a subsequence to a locally finite simple process P.
4. For some delta>0, writing A_T=B_{2T}(0)\B_T(0),

       limsup_{T->infinity} P(X(A_T)>=delta T^d)=1.

Then P is not number rigid. The conclusion holds in particular in the d>=2 band of P0320 if these assumptions can be proved for its approximants.

### Proof: energy and good particles

Retain the smoothing error w and averaging measure nu above. Define the bounded, nonnegative, integrable function

    v(z)=w(z)+1_{|z|<=2},
    c_i=sum_{k!=i} v(x_i-x_k).

Call particle i good if c_i<=K. The factorial moment hypothesis and Tonelli give, for every bounded measurable D,

    E_N # {i: x_i in D, c_i>K}
       <= (a_2 |D| ||v||_1)/K.                    (1)

Indeed, K times this number is at most sum_{i:x_i in D} c_i, and the expectation of that pair sum is at most a_2 |D| ||v||_1. Thus neither pointwise exterior-density bounds nor conditioned correlation bounds have been assumed here.

For distinct i,j, let M_{i->j} replace x_i by x_j+u, averaging over nu(du). Put

    U_i=W_N(x_i)+sum_{k!=i,j}g(x_i-x_k),
    U_j=W_N(x_j)+sum_{k!=i,j}g(x_j-x_k),
    c_0=int g(u)nu(du)=d/(d-s).

Taylor's formula and Hess W_N<=L I give AW_N(x)<=W_N(x)+L/2. Each other interaction at destination x_j has averaging error at most w(x_j-x_k). Hence, if j is good,

    M_{i->j}H_N-H_N
       <= U_j-U_i-g(x_i-x_j)+c_0+L/2+K.

If i is good, the reverse direction satisfies the same inequality with U_i-U_j in place of U_j-U_i. Since g>=0, for two good particles at least one direction satisfies

    M H_N <= H_N+B,       B=c_0+L/2+K.          (2)

This is the only energy comparison needed; its elementary favorable-direction algebra is kernel-checked in TransportAlgebra.lean. All averages are finite away from the null collision set because s<d and W_N is continuous on compact sets.

For any event A on which a chosen direction satisfies (2), positivity and Jensen's inequality imply pointwise

    1_A exp(-beta_N H_N)
       <= exp(b B) 1_A M(exp(-beta_N H_N)).     (3)

The adjoint in Lebesgue measure is, for direction i->j,

    M^* f(x_1,...,x_N)
       =nu(x_i-x_j) int_{R^d} f(x_1,...,z,...,x_N)dz,

where nu(z)=1_{B_1}(z)/|B_1| and the integrated coordinate is i. This identity follows by fixing all remaining coordinates, interchanging the z,u integrations by Tonelli, and substituting x_i=x_j+u. Therefore (3) is an exact finite-volume probability comparison, not a transport heuristic.

### Proof: summed finite-volume comparison

Fix 0<r<R-1 and S>R, let I={X(B_r)>0}, and let E_n={X(B_R)=n}. Let f, 0<=f<=1, be any measurable function of X restricted to B_S\B_R. Choose T>S+4 and T>2R+4, and set

    D_T=B_{2T+2}\B_{T-2}.

Let G be the event consisting of:

* X(A_T)>=delta T^d;
* fewer than delta T^d/2 particles in A_T are bad;
* X(D_T)<=rho T^d;
* at least one good particle lies in B_r.

On E_n intersect I intersect G, there are at least delta T^d/2 ordered pairs (i,j) of good particles with x_i in B_r and x_j in A_T. For each such pair choose a favorable direction using (2), breaking ties by choosing j->i. This makes a measurable partition. Apply (3) to the weighted indicators of these pair events, multiply by f, sum over all i!=j, integrate, and divide by the Gibbs normalizer.

Both directions preserve the configuration in B_S\B_R: the source interior particle lies more than one unit inside B_R, and the far particle lies more than one unit outside B_S. Consequently the same f appears after taking the adjoint.

For the incoming direction j->i, the integrated original coordinate j ranges over A_T, of volume |A_T|. The adjoint kernel is bounded by |B_1|^-1. The resulting configuration has n+1 points in B_R. Summing over the possible ordered target pair (i,j) costs at most (n+1)^2: both are now in B_R. Dropping all other restrictions gives the upper bound

    exp(bB) |A_T| |B_1|^-1 (n+1)^2 E_N[1_{E_{n+1}} f].       (4)

For the outgoing direction i->j, the integrated original coordinate i ranges over B_r, of volume |B_r|. The resulting configuration has n-1 points in B_R, and the original far particle j stays in A_T. Before movement, goodness of j bounds the number of its other neighbours in B_2(x_j) by K. After adding i near j, the total count in this ball is at most K+2 (including j itself). Also, movement increases X(D_T) by at most one. Thus the target pair sum is bounded by

    |B_1|^-1 (K+2)(rho T^d+1).

To see this directly, sum first over j in A_T. There are at most rho T^d+1 choices; for a j satisfying the inherited local-count restriction there are at most K+2 choices for i with |x_i-x_j|<1. If that restriction fails, the relevant adjoint indicator is zero. The outgoing contribution is therefore at most

    exp(bB) |B_r| |B_1|^-1 (K+2)(rho T^d+1)
         E_N[1_{E_{n-1}} f].                                (5)

The lower bound for the summed source indicators, followed by (4)-(5), proves, for 1<=n<=m and T>=1,

    E_N[1_{E_n}1_I f]
       <= C E_N[(1_{E_{n-1}}+1_{E_{n+1}})f]+P_N(I\G),     (6)

where C is finite and depends only on d,s,b,L,delta,r,K,rho,m, not on N,S,T,f. No division by a random conditional probability or unknown partition-function ratio occurs.

By a union bound, (1), and the first-moment bound,

    P_N(I\G)
       <= P_N(X(A_T)<delta T^d)
          +2a_2 |A_T| ||v||_1/(delta T^d K)
          +a_1 |D_T|/(rho T^d)
          +a_2 |B_r| ||v||_1/K.                            (7)

For T>=4, both |A_T|/T^d and |D_T|/T^d are bounded by constants depending only on d. Thus the last three terms can be made arbitrarily small by choosing K and rho large, uniformly in N,S,T. Choosing these constants before T is essential.

### Proof: the infinite-volume limit and contradiction

The first-moment domination passes to P: for each nonnegative continuous compactly supported h, truncate int h dX at a finite level, use weak convergence, then monotone convergence to obtain E_P int h dX<=a_1 int h dx. Regular approximation yields the same domination for all Borel sets. Hence P has no points on any fixed sphere almost surely. Counts in any fixed ball or annulus therefore converge in distribution from P_N to P; integer-valued counts also give convergence of probabilities of every fixed count threshold.

Fix eta>0. Choose K and rho so that the last three terms in (7) total at most eta/2. For any S, the non-vacuum limsup supplies an arbitrarily large fixed T>S+4 with P(X(A_T)<delta T^d)<eta/2. By threshold convergence, the first term in (7) converges to this probability. Initially take f to be a bounded continuous function, valued in [0,1], of finitely many integrals against continuous compactly supported functions in the open shell B_S\closure(B_R). These f, and the ball-count indicators, are continuity functionals P-almost surely. Taking N->infinity in (6) gives

    E_P[1_{E_n}1_I f]
       <= C E_P[(1_{E_{n-1}}+1_{E_{n+1}})f]+eta.           (8)

The constant C is independent of S and the chosen T. To extend (8) to any shell-measurable f in [0,1], take a countable collection of compactly supported continuous functions generating the vague Borel sigma-field on the open shell. Conditional expectations on the first k coordinates approximate f in L^1(P) by the martingale convergence theorem. For each finite coordinate distribution, bounded continuous [0,1]-valued functions are L^1-dense, by regularity of Borel probabilities on Euclidean space. A diagonal approximation gives such cylinder functions converging to f in L^1(P); bounded event multipliers allow passage to (8). Shell boundaries have no P-points, so this proves the assertion for the stated shell sigma-field as well.

Now let F be any event measurable with respect to the full exterior X restricted to B_R^c. For S increasing to infinity, substitute f_S=E_P[1_F | X restricted to B_S\B_R] in (8). These sigma-fields increase to the exterior sigma-field, modulo the null sphere boundaries. Martingale convergence in L^1 yields

    P(E_n intersect I intersect F)
       <= C[P(E_{n-1} intersect F)+P(E_{n+1} intersect F)]+eta.       (9)

Non-vacuum guarantees that some finite r has q=P(I)>0. Choose R>r+1 and an integer m>=1 with sum_{n=1}^m P(E_n intersect I)>q/2, using local finiteness. Set eta=q/(4m), and repeat the preceding construction with this fixed r,R,m,eta. If P were number rigid, for each n there would be an exterior-measurable F_n agreeing almost surely with E_n. Substituting F_n in (9) makes both adjacent-count probabilities zero, and hence P(E_n intersect I)<=eta for every 1<=n<=m. Their sum is at most m eta=q/4, a contradiction. This completes the conditional theorem. QED.

## Literature special case in dimension one

Yan Ru Pei, arXiv:2609.28503v1 (15 September 2026), Theorem 1.2, proves that every periodic thermodynamic limit for g(x)=-|x|^a, 0<a<1, beta>0, has a stationary matching to the shifted unit lattice with E q_0^2<=C_a/beta. Cauchy-Schwarz gives E|q_0|<=sqrt(C_a/beta), so the matching has finite mean absolute transport cost. Dereudre–Digneaux, arXiv:2510.17257v2, Theorem 2.1, applies to any stationary one-dimensional point process with finite such cost and gives number rigidity. Therefore these periodic gases are number rigid for -1<s<0, s=-a. The s=0 Sine_beta endpoint was already rigid. This is a literature implication for specified periodic ensembles, not an identification with every possible container or DLR ensemble. Pei explicitly leaves ensemble equivalence separate. The full higher-dimensional interval remains unsettled by these papers.

## Checks, failure points, and remaining gap

* Sign: Delta g is strictly positive in this band. Superharmonicity cannot be silently used. The frozen-mass counterexample tests exactly this issue.
* Collision: w is bounded even though g is singular; local integrability requires s<d. The transport average creates no atomic collision probability.
* Multiplicity: outgoing local-count cutoff is K+2 including the destination particle; using K alone would be an off-by-one mistake. Incoming pair count is bounded by (n+1)^2.
* Entropy: adjoint integrations have volumes |A_T| and |B_r|, respectively. Ordered pair sums, rather than informal label cancellation, supply all counting factors.
* Conditioning: errors in (6) are unconditional additive probabilities. The proof uses bounds uniform in S, then applies martingale convergence. Merely proving a finite-shell comparison with constants growing in S would not suffice.
* Model hypotheses: no proof is supplied that the globally uniform first and second factorial-density bounds hold for the approximants of any concrete higher-dimensional gas in this band. Bulk local laws alone do not provide the global weighted-particle control in (1), including particles far outside the bulk. Peilen–Serfaty local laws are relevant but are not a substitute without further work.
* Domain: the conditional theorem is for unperiodized Euclidean positive Riesz kernels and globally smooth confining potentials with Hessian bounded above. A torus or jellium application requires verifying its kernel/one-body analogues; it cannot be asserted from the present proof.
* Formal verification: TransportAlgebra.lean passed `lake env lean` with exit 0; only three real-algebra statements are checked. The analytic, measure-theoretic, and probability arguments are written above and are not formally verified. No `sorry`, `native_decide`, or broad `import Mathlib` is used.
* Numerical check: check_smoothing.py uses deterministic radial/angular quadrature, not a gas simulation. smoothing_checks.json records positive smoothing errors and approach to the Taylor coefficient s(s+2-d)/(2(d+2)); it also records linear growth of the symmetric frozen-mass costs.

The precise remaining gap is to verify the conditional theorem's global moment and non-vacuum assumptions (or prove a replacement giving (7)) for an explicitly defined higher-dimensional infinite-volume Riesz gas, while retaining uniform constants as the conditioning shell grows. No unconditional rigidity/non-rigidity theorem for that band has been proved in this attempt. The literature search was bounded and several API requests were rate-limited, so the absence of a found higher-dimensional solution is not a certification of current open status.

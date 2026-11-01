# C0056: logarithmic cavity control and spectral purity

Author w480, 2026-10-10. Author proof only; independent review pending. No parent-problem solved claim. Current openness UNKNOWN.

## Target, source, and lane

The intake's exact C0056 record is in probability_1000_intake_claude_20260907/problems.jsonl:56. It asks for both absolutely continuous spectrum of -Delta+lambda V on Z^3 at weak disorder and GOE local statistics for finite-volume restrictions. It points to Bourgade, Random band matrices, arXiv:1807.03031, Section 2.1, page 7. The record does not specify the potential law, boundary condition, or microscopic normalization for the GOE claim. The GOE component is outside this proof route and remains unproved here.

Our precisely specified spectral subtarget uses H_lambda=-A+lambda V on l2(Z^3), nearest-neighbor adjacency A, iid V_x uniform on [-1,1], and fixed lambda>0 before the boundary limit. Find a deterministic nonempty bounded open J inside the free band (-6,6) and lambda_0>0 such that, for each fixed 0<lambda<lambda_0, almost surely the spectral restriction to J is purely absolutely continuous and nonzero. A Laplacian convention with a constant diagonal shift translates the energy interval.

The primary source has now been checked directly: its potentials are iid, centered, variance one, and its finite-volume convention is periodic with microscopic scale N^d. Our explicit uniform[-1,1] law is a chosen instance after rescaling: source V=sqrt(3)*U and source coupling alpha=lambda/sqrt(3). A source-level fixed-energy GOE theorem is not fully specified; no such theorem is asserted here. Primary source: https://arxiv.org/pdf/1807.03031 , Section 2.1, printed page 7.

A recent public primary preprint, dated 2026-09-23, claims a spectral result for this uniform-potential model in all fixed dimensions d>=3. Its d=3 interval lies just above the lower free band edge, and its threshold is existential. Neither its proof nor its key certificate construction has been independently validated by this worker. It contains no GOE conclusion in its main theorem. Its existence invalidates an unsupported assertion that the spectral target is currently open; current openness remains UNKNOWN. Source: https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex .

## Prior attempt digest

C0056-A001 (intake attempts.jsonl:45) tried a tree reduction and recorded two obstructions: Z^3 has no closed independent-branch Green-function recursion, and weak-coupling finite-time estimates do not prove a fixed-coupling boundary limit. Restriction to a spanning tree changes the operator. Targeted C0056/Anderson searches in the named H/I attempt directories found no additional matching mathematical packet; the Lean annotated ranking merely repeats attempted_un and supplies no formal proof. The Team O board had no C0056/Anderson matching task line. Peer boundary claims were sent for a distinct logarithmic entropy route.

Brain recall timed out after 60 seconds. The directly named scar perceptron_proof_open_gaps_fleet_2026_07_12 was read: a validated local repair did not close the fleet's hardest proof gap. Accordingly, the unproved logarithmic input below is kept separate from the reduction. w481's INDEPENDENT_OBSTRUCTION.md, read after our proof was saved, independently gives a diagonal operator with bounded averaged resolvent first moment and atomic sample spectral measures. It corroborates the failure mode in C1, not the entropy reduction.

## Notation and the single hardest input

Delete site x and let H_lambda^(x) be the cavity operator; h_x is its hopping vector, with ||h_x||^2=6. For z=E+i eta, eta>0, set

    Sigma_x(z)=<h_x,(H_lambda^(x)-z)^(-1)h_x>,
    b_x(E,eta)=eta+Im Sigma_x(z)>0,
    a_x(E,eta)=E+Re Sigma_x(z),
    G_xx(z)=1/(lambda V_x-a_x-i b_x),
    f_x(E,eta)=Im G_xx(z)/pi.

The cavity quantities are independent of V_x. No independence between different neighbor cavities is assumed. The spectral theorem gives b_x=eta(1+||(H_lambda^(x)-z)^(-1)h_x||^2).

The sole unproved input for THIS spectral route is:

    (LG) For a deterministic nonempty bounded open J inside (-6,6),
         for every fixed sufficiently small lambda>0,
         sup_{0<eta<=1} E integral_J log(1+1/b_0(E,eta)) dE < infinity.

The constant may depend on lambda and J. This is a claim about the infinite-volume operator. No power-law inverse moment, independence product, or exchange of volume and eta limits is included. The target includes a separate GOE problem which this route does not reduce or solve.

## L1: exact scalar entropy identity (author proof complete)

For real a, b>0, lambda>0, define y(v)=b/[pi*((lambda v-a)^2+b^2)] and Phi(t)=t log(1+t), t>=0. Then

    integral_R Phi(y(v)) dv
       = (2/lambda) log((1+sqrt(1+1/(pi*b)))/2)
       <= (1/lambda) log(1+1/(pi*b)).

Proof. Substitute t=(lambda v-a)/b and then t=tan(theta). The left side becomes

    (1/(pi*lambda)) integral_{-pi/2}^{pi/2}
               log(1+cos(theta)^2/(pi*b)) dtheta.

For c>=0 let F(c)=integral log(1+c cos(theta)^2) dtheta over this interval. Differentiation under the integral gives F'(c)=pi/c*(1-1/sqrt(1+c)) for c>0: the integral of 1/(1+c cos(theta)^2) is pi/sqrt(1+c), as follows from t=tan(theta) and the elementary arctangent integral. Since F(0)=0, integration gives F(c)=2*pi*log((1+sqrt(1+c))/2). This proves the equality. Since (1+sqrt(1+c))/2 <= sqrt(1+c), the inequality follows. All integrands are nonnegative and integrable; for differentiation on a compact c interval the derivative is bounded by 1. Translation a has canceled exactly.

If V_x has a density rho with ||rho||_infinity=R independent of the cavity, conditional integration gives

    E[Phi(f_x(E,eta)) | cavity] <= (R/lambda) log(1+1/(pi*b_x(E,eta)))
       <= (R/lambda) log(1+1/b_x(E,eta)).

For the uniform law R=1/2. The lambda factor and pi normalization are essential. This result does not apply directly to a Bernoulli site law.

## L2: (LG) implies almost-sure pure absolute continuity (author conditional proof complete)

Assume (LG) at fixed lambda. Tonelli and L1 imply sup_eta E X_x(eta)<=C_lambda<infinity, where X_x(eta)=integral_J Phi(f_x(E,eta)) dE. Translation invariance transfers the bound from x=0 to every x. Take eta_n=2^(-n). Fatou gives E liminf_n X_x(eta_n)<=C_lambda, so the liminf is finite almost surely. For each such realization and fixed x, choose a subsequence with X_x(eta_n)<=A_x(omega)<infinity. This subsequence may depend on x and omega; no deterministic uniform bound is claimed.

Let mu_x be the local spectral measure. The measures nu_n(dE)=f_x(E,eta_n)dE are its Poisson convolutions and converge weakly on R to mu_x. For every Borel O contained in J and every K>0, the entropy bound gives

    nu_n(O) <= K*|O| + A_x/log(1+K)

along the selected subsequence, by splitting f_x<=K and f_x>K. If O is open, the portmanteau inequality yields the same upper bound for mu_x(O). For any Lebesgue-null Borel N contained in J, cover N by open O contained in J with arbitrarily small Lebesgue measure. Thus mu_x(N)<=A_x/log(1+K) for all K, and letting K tend to infinity gives mu_x(N)=0. This proves mu_x restricted to J is absolutely continuous, including exclusion of singular continuous and pure point mass. Intersect the probability-one events over countably many x. The delta_x span l2, so for a null N contained in J, each projection P_N delta_x has norm squared mu_x(N)=0; therefore P_N=0 and the entire spectral restriction to J is absolutely continuous.

This argument uses conditional own-site independence once and Fatou once. It does not infer sample purity from the averaged density alone, and does not multiply conditional row estimates.

## L3: the finite-volume logarithmic obstruction (author proof complete)

Let B be any finite-dimensional self-adjoint cavity matrix and h any vector. For a bounded nonempty interval J and 0<eta<1 define b(E,eta)=eta+Im<h,(B-E-i eta)^(-1)h>. Then

    lim_{eta->0} integral_J log(1+1/b(E,eta)) dE / log(1/eta) = |J|.

Indeed, outside the finite spectrum of B,

    b(E,eta)=eta*(1+sum_j w_j/((e_j-E)^2+eta^2)),

where w_j>=0. For almost every E the parenthesis converges to a finite positive value, so the normalized logarithm converges to 1. Since b>=eta, it is bounded above by log(1+1/eta)/log(1/eta), which is at most 2 for sufficiently small eta. Dominated convergence proves the assertion. For any random finite cavity, Fubini and the same deterministic bound prove the identical annealed limit; no density assumption is needed. Consequently no fixed finite box satisfies (LG). A volume limit at each positive eta is necessary before using this infinite-volume criterion.

## C1: an averaged density alone does not prove delocalization (exact counterexample)

Let H_lambda be the one-dimensional scalar operator lambda V, V uniform on [-1,1]. Its spectral measure is delta_(lambda V) for every sample, while the expected spectral measure has density 1/(2*lambda) on [-lambda,lambda]. Its Poisson-smoothed averaged density is uniformly bounded by the same value. Here b=eta, and the entropy integral over all energies is

    2*log((1+sqrt(1+1/(pi*eta)))/2),

which diverges like log(1/eta). Thus a Wegner-type first-moment bound and a positive annealed imaginary part do not imply sample absolute continuity. This toy operator is not a counterexample to weak-disorder lattice delocalization; it refutes only that proposed implication.

## L4: rigorous perturbation reaches only a regulated regime

For bounded potentials |V_x|<=M, the resolvent identity on the deleted-site space gives

    |Sigma_lambda(E+i eta)-Sigma_0(E+i eta)| <= 6*lambda*M/eta^2,
    b_lambda(E,eta) >= b_free(E,eta)-6*lambda*M/eta^2.

Both cavity resolvents have norm at most 1/eta, so this bound is deterministic and needs no independence. If the free cavity b_free is bounded below by b_*>0 on J and 0<eta<=1, then b_lambda>=b_*/2 whenever eta^2>=12*lambda*M/b_*. In that regulated range,

    integral_J log(1+1/b_lambda) <= |J|*log(1+2/b_*).

Here is the free lower-bound argument explicitly. The free Fourier symbol is epsilon(k)=-2*(cos k_1+cos k_2+cos k_3) on the three-torus with normalized measure. Its only critical energies are -6,-2,2,6. Choose a closed interval K strictly inside (-6,-2), and an open neighborhood K' with closure still inside that range. Coarea gives a smooth positive density rho_free(E) on K': every level surface is nonempty and regular. Split the free measure using a smooth cutoff chi supported in K' and equal to 1 near K. The Cauchy transform of chi*rho_free has continuous finite boundary values on K, with imaginary part pi*rho_free>0. The transform of the remaining measure is analytic near K because its support is separated from K. Hence g_free(E+i eta) is finite and continuous on K times [0,1] and has strictly positive imaginary part there. The Schur identity gives b_free=-Im(1/g_free)=Im(g_free)/|g_free|^2. It is positive and continuous on this compact set, yielding b_*>0. Any open J with closure in K therefore has the claimed free lower bound.

This perturbative route stops at eta of order sqrt(lambda). At fixed positive lambda it supplies no estimate as eta tends to zero, so it does not prove (LG).

## L5: nonzero spectral weight is a separate bounded-perturbation fact

Let J be any nonempty open interval inside (-6,6). Choose a continuous nonnegative g compactly supported in J such that a=<delta_0,g(H_0)delta_0>>0. Such a function exists because the free Fourier spectral measure gives positive weight to every open interval in the band. For |V_x|<=M and lambda small, ||H_lambda-H_0||<=lambda*M and continuous functional calculus gives ||g(H_lambda)-g(H_0)||<a/2, uniformly over the sample. For completeness, approximate g uniformly on [-7,7] by a real polynomial p with error <a/8; ensure lambda*M<=1, and use

    ||p(H_lambda)-p(H_0)|| <= lambda*M*sum_{k>=1}|p_k|*k*7^(k-1).

Choose lambda so this is <a/4. The two approximation errors and the polynomial difference sum to <a/2. Therefore <delta_0,g(H_lambda)delta_0>>a/2, and the spectral projection onto J is nonzero. This proves mass persistence, not purity; purity still requires (LG).

## Attempt on (LG) and exact stopping point

Start from the deterministic free lower bound and apply L4. This proves the desired logarithmic control only above a lambda-dependent cutoff of order sqrt(lambda). Below it the bound loses its sign. The universal b>=eta gives only |J|*log(1+1/eta), diverging in precisely the direction needed to close (LG). L3 shows that replacing the infinite cavity by a fixed numerical box cannot repair this. C1 shows that site spectral averaging cannot close the gap by itself. Loops in Z^3 prevent replacing the missing bound with independent tree-branch recursion. No missing term has been bounded by an independence assumption, no uniform limit has been extrapolated from finite eta, and no theorem proving (LG) has been obtained.

The remaining proof task is to establish, or refute, the fixed-lambda infinite-volume bound (LG). A power-law lower tail P(b_0(E,eta)<exp(-t))<=C exp(-alpha*t), uniform in eta and integrable in E, would suffice but is stronger than necessary. More generally the integral of that tail over E and t must be uniformly finite. Any proposed certificate must control that exact quantity after the infinite-volume limit. This packet closes the scalar identity, the conditional reduction, the finite-volume obstruction, and the regulated comparison; it does not close the delocalization input or the GOE target.

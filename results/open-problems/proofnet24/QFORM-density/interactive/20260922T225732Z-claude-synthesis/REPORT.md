# Projected-gradient slicing and closure of the finite-core step

Programme QFORM-DENSITY-3EIG-20260922. Interactive record 20260922T225732Z-claude-synthesis.

**Status.** Complete supporting analytic arguments are supplied below. The unrestricted dimension-free conjecture is not proved. The new projection-field argument improves the dimension-dependent bound for general matrices, and yields an explicit, moment-free localized-core theorem. Claude's new ruled-surface calculation is justified for rough product inputs. An already-proved semidefinite rank-three theorem is restored to the combined proof map rather than claimed as new. Independent end-to-end review of this synthesis is requested; no literature-wide novelty claim is made.

## 1. Source map and the exact remaining target

The owner asks for one universal C such that, for every n, every real symmetric A with at least three eigenvalues of absolute value at least one, and independent real X_i with probability densities 0 <= f_i <= 1,

    P(X^T A X in J) <= C |J|

for every bounded interval J. Equivalently, the output has an essentially bounded density with that universal cap. No moments, centering, connected support, smoothness or log-concavity are assumed. Continuous density is a separate conclusion.

The first newest-source snapshot consumed in this invocation is

    yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837
    proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/

In that directory:

- COUNTEREXAMPLE_SEARCH.md, blob d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc: physical-coordinate fiber identity, dimension-dependent bound, ruled one-sheet estimate, and rank-two elliptic bound.
- FOURIER_ROUTE_REPORT.md, blob 9da148eed6cd43b1046a6f91d0f9329e12921cb4: volume-sampling extensions D', D5, Fresnel/mixed-hub estimates, localization split, and explicit unproved steps R1-R3.
- RESULTS.md: the lead's combined account. Neither report claims the unrestricted conjecture solved.

The published input used here is Livshyts, Paouris and Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877-889, Theorem 1.1, arXiv:1507.07949v2, DOI 10.1007/s11856-016-1431-5. An orthogonal two-dimensional marginal of a cap-one product density is bounded by 2. If the projection is the whole two-dimensional ambient space, its density is bounded by 1. This is a joint-marginal theorem, not an assertion of independence of the two projected coordinates. The theorem and its assumptions were read in the primary paper.

The new step below replaces the full gradient in Claude's physical-coordinate partition by its projection onto ONLY three substantial eigendirections. This retains arbitrary other eigenvalues and affine terms while improving the general dimensional loss from O(n) to O(sqrt(n)). It does not remove dimensional dependence.

A further Claude push arrived while this synthesis was being completed: `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, adding GEOMETRIC_ROUTE_REPORT.md in the same directory. The companion GEOMETRIC_SYNTHESIS.md applies its hyperbolic envelope, proves a determinant-only arbitrary-rank pair bound, and reduces the full conjecture to a single no-pivot density statement by a class-preserving Gaussian padding argument. That remaining density statement is not proved.

## 2. A two-dimensional reciprocal-distance estimate

**Lemma 2.1.** If Y has a probability density on R^2 bounded by M, then for every z in R^2,

    E |Y-z|^(-1) <= 2 sqrt(pi M).                              (2.1)

**Proof.** The disk estimate gives P(|Y-z| < r) <= min(1, pi M r^2). By the nonnegative layer-cake identity,

    E |Y-z|^(-1)
      = integral_0^infinity P(|Y-z| < 1/u) du
      <= integral_0^infinity min(1, pi M/u^2) du
      = 2 sqrt(pi M).

This proof needs no maximizing set or attainment assertion. QED.

## 3. Projected-gradient slicing: arbitrary rank and arbitrary affine terms

**Theorem 3.1.** Let A be a real symmetric n by n matrix. Let E be a three-dimensional A-invariant subspace such that every eigenvalue of A restricted to E has absolute value at least sigma > 0. Let P_E be the orthogonal projection onto E, and put

    ell_i = |P_E e_i|^2,             L(E) = sum_i sqrt(ell_i).

For independent real X_i with densities bounded by 1, arbitrary b in R^n and c in R, the variable

    q(X) = X^T A X + b^T X + c

has a probability density satisfying

    ||p_q||_infinity <= (2 sqrt(2 pi)/sigma) L(E)
                    <= 2 sqrt(6 pi n)/sigma.                   (3.1)

All remaining eigenvalues are unrestricted. In particular, the bound uses the chosen high-eigenvalue subspace, NOT the entire range of A. It remains valid if A is full rank with arbitrarily small or large additional eigenvalues. When n=3, the sharper bound 6 sqrt(pi)/sigma follows from the same proof.

### Proof

Write v(x)=grad q(x)=2Ax+b and g(x)=P_E v(x). Because E is invariant and A is invertible on E, there is a unique z_0 in E satisfying

    2 (A restricted to E) z_0 + P_E b = 0.

Thus

    g(x) = 2 (A restricted to E)(P_E x-z_0),
    |g(x)| >= 2 sigma |P_E x-z_0|.                             (3.2)

The set g(x)=0 is an affine subspace of codimension three and has zero probability under the absolutely continuous product law.

The essential algebraic identity is

    sum_i partial_i q(x) g_i(x) = v(x)^T P_E v(x) = |g(x)|^2.

Consequently, off that null set,

    1 <= sum_i |partial_i q(x)| |g_i(x)| / |g(x)|^2.           (3.3)

Individual summands before taking absolute values need not be positive. Inequality (3.3), rather than a fictitious positive partition, is what is used. Moreover, because g(x) lies in E,

    |g_i(x)| <= sqrt(ell_i) |g(x)|.                            (3.4)

Let psi be a nonnegative bounded compactly supported Borel function on R. Multiply (3.3) by psi(q(x)) prod_j f_j(x_j) and integrate. Tonelli applies to the resulting nonnegative terms. Fix i and then fix x_{-i}. Along the remaining original coordinate t=x_i, q(t,x_{-i}) is a polynomial of degree at most two. On its nonconstant monotonicity intervals, the one-dimensional change-of-variables formula gives

    integral_R psi(q(t,x_{-i})) f_i(t)
       |partial_i q| |g_i|/|g|^2 dt
    = integral_R psi(s)
       sum_{t: q(t,x_{-i})=s, partial_i q != 0}
          f_i(t) |g_i(t,x_{-i})|/|g(t,x_{-i})|^2 ds.            (3.5)

This identity is understood up to null critical-value sets. If the fiber polynomial is constant, its left side is zero because partial_i q is zero; that fiber contributes zero rather than an infinite root count. The critical points of a nonconstant quadratic also contribute no one-dimensional measure. Representatives with 0<=f_i<=1 everywhere can be chosen.

Choose a two-dimensional subspace E_i contained in E intersect e_i-perp. It exists because E has dimension three. Since vectors in E_i have zero i-th coordinate, Y_i=P_{E_i}X depends only on X_{-i}. For every x,

    |g(x)| >= 2 sigma |P_{E_i}x-P_{E_i}z_0|.                  (3.6)

Combining (3.4), (3.6), f_i<=1, and the fact that a nonconstant quadratic has at most two roots, the root sum in (3.5) is bounded by

    sqrt(ell_i) / [sigma |P_{E_i}x_{-i}-P_{E_i}z_0|].          (3.7)

The value on the zero-denominator set can be taken as infinity; that set has zero probability, and the bound below is integrable. The law of Y_i is a two-dimensional orthogonal marginal of the remaining original product coordinates, hence has density at most 2 by LPP. Lemma 2.1 gives

    E |Y_i-P_{E_i}z_0|^(-1) <= 2 sqrt(2 pi).                  (3.8)

Equations (3.3)-(3.8), summed over i, therefore show

    E psi(q(X)) <= (2 sqrt(2 pi)/sigma) L(E) integral psi(s) ds.

Applying this directly to interval indicators, then to countable interval covers, proves that the output law is dominated by the displayed multiple of Lebesgue measure. This establishes both absolute continuity and the essential density bound; no prior continuity or pointwise coarea density assertion is needed.

Finally sum_i ell_i = trace(P_E) = 3, so Cauchy-Schwarz gives L(E)<=sqrt(3n). If n=3, E_i is the entire coordinate complement and its density is at most one, so (3.8) improves to 2sqrt(pi); also L(E)=3. This gives 6sqrt(pi)/sigma. QED.

### Comparison with Claude's fiber estimate

For an exact-rank-three homogeneous form, taking E=range(A) gives essentially Claude's Theorem B. The difference matters at higher rank: Claude's stated bound uses sum_i |P_range(A)e_i|, which equals n for an invertible A. The projected-field identity above uses only three substantial eigendirections and gives at most sqrt(3n), while permitting arbitrary affine terms, including components outside range(A). This is a supporting refinement, not a dimension-free conclusion.

More generally, any bound L(E)<=L_0 yields a density cap 2sqrt(2pi)L_0/sigma independent of the ambient dimension. Such a bounded row-sum is an extra geometric hypothesis, not a consequence of three substantial eigenvalues. A perfectly flat three-frame has L(E)=sqrt(3n), showing that this particular estimate still loses dimension in the diffuse case.

## 4. The actual bounded-dimensional problem is closed

**Corollary 4.1.** For each integer m>=3 and sigma>0, all quadratic-plus-affine polynomials on m independent cap-one coordinates whose actual quadratic matrix has at least three eigenvalues of magnitude at least sigma satisfy

    ||p_q||_infinity <= 2 sqrt(6 pi m)/sigma.                   (4.1)

No lower bound on an individual diagonal pivot, selected 2x2 determinant, or smallest nonzero eigenvalue beyond the three substantial ones is required.

**Proof.** Choose E to span three corresponding eigenvectors and apply Theorem 3.1. QED.

This resolves R2 of the new Fourier report when R2 means the true finite-dimensional spectral problem. It is unnecessary to first prove an interpolation lemma for every possible pair of linear forms in order to obtain this bounded-dimensional conclusion.

The alternate formulation "a diagonal matrix plus a rank-three component whose three eigenvalues are large" needs an ACTUAL total-spectrum condition. Without it, take m=3, U=I_3, Lambda=I_3, D=-I_3. The total quadratic matrix is zero and the homogeneous output is an atom. A large component that can be canceled is not a substitute for the hypothesis on A itself. This elementary counterexample corrects an intermediate formulation, not the original conjecture.

## 5. A localized spectral core is robust to arbitrary dense tails

**Theorem 5.1 (physical-core stability).** Let H be a set of m original coordinates, m>=3. Suppose the physical principal block can be written

    A_HH = U_H Lambda U_H^T + T_H,

where U is an ambient n-by-3 orthonormal-column matrix, Lambda is invertible symmetric with sigma_min(Lambda)>=s>0, and

    U_H^T U_H >= a I_3,       ||T_H||_op <= epsilon < a s.      (5.1)

Every other block of A may be arbitrary. For independent cap-one inputs and arbitrary affine terms,

    ||p_q||_infinity <= 2 sqrt(6 pi m)/(a s-epsilon).           (5.2)

No moments or support bounds are imposed, and T_H need not be diagonal, low rank, or of one sign.

### Proof

Set G=U_H^T U_H and V=U_H G^(-1/2), so V has orthonormal columns. The nonzero part of U_H Lambda U_H^T is represented by

    K=G^(1/2) Lambda G^(1/2).

For every z in R^3,

    |Kz| >= sqrt(a) |Lambda G^(1/2)z|
         >= a s |z|.

Therefore the rank-three matrix U_H Lambda U_H^T has three singular values at least a s, with no sign restriction on Lambda. On the three-dimensional subspace range(V), the triangle inequality gives

    |A_HH x| >= (a s-epsilon)|x|.

The variational characterization of singular values implies

    s_3(A_HH) >= a s-epsilon.                                 (5.3)

Condition on all ORIGINAL coordinates outside H. The remaining coordinates keep their original independent densities. The conditional quadratic part is exactly A_HH and the outside variables generate arbitrary deterministic affine terms; Corollary 4.1 is uniform in those terms. Its conditional interval bound with sigma=a s-epsilon is therefore uniform in the outside value. Averaging proves (5.2). QED.

This argument does NOT compare q(X) with an unperturbed quadratic random variable. The invalid estimate epsilon |X|^2 is never treated as small. The tail is retained exactly in the physical matrix, and only its operator norm on the finite core is used to certify three substantial singular values.

In particular, if A=U Lambda U^T+T globally with ||T||<=epsilon, and three spectral directions place Gram mass at least a on at most m original coordinates, (5.2) applies regardless of the tail's signs or orientation. For m<=30, a>=4/5, s>=1, and epsilon<=1/10,

    ||p_q||_infinity <= 2 sqrt(180 pi)/(7/10) < 68.            (5.4)

The outside dimension is arbitrary. This closes the fully localized small-dense-tail branch, not the hybrid branch in which only one or two directions are localized.

### Application to the Fourier report's localization split

For an exact-rank-three A=U Lambda U^T, take H={i: |u_i|^2>delta} and L its complement, with 0<delta<1/2. Then |H|<3/delta. If all three eigenvalues of G_L=U_L^T U_L are below 2delta, then G_H=I-G_L>(1-2delta)I. Corollary 4.1 / Theorem 5.1 closes that fully localized branch with m<3/delta, a=1-2delta, epsilon=0.

If instead G_L>=2delta I, the existing diffuse Fresnel theorem applies to the physical L block. These two arguments leave precisely the one- or two-localized-direction alternatives of that particular frame split; they do not constitute an exhaustive solution. An arbitrary diagonal added to A must be retained in the actual principal-block spectral check; it can cancel the low-rank component.

## 6. Restore the already-proved semidefinite rank-three theorem

The new counterexample report lists definite rank-three forms among the remaining convex cases. The existing archive already closes them:

    math-open-problems@f8b6f4d6763094eedf3b23b845dce57e28279c55
    proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/
    20260922T123541Z-account02-B18-QFORM-r11/REPORT.md

Its Theorem 7.1 is QFORM-RANK3-SEMIDEFINITE-v1. It proves ||p_Q||<=3e for exact rank three, all three eigenvalues of one sign and magnitude at least one. The proof is reproduced compactly to reconcile the two workers' proof maps, not to claim a new result.

Reflect the output to make A positive semidefinite. Write A=U Lambda U^T with U orthonormal and lambda_j>=1. If every leverage ell_i<=1/2, use the existing sharp diffuse-frame estimate 3e (also extended to arbitrary separable phases in the interactive report at 773b7fb6f0e6a8142066f0bac08d228dfc164fdb).

Otherwise choose ell_i>1/2. Then a=A_ii>=ell_i>1/2. Complete the square in this original coordinate:

    Q=a(X_i+theta(X_-i))^2+R(X_-i).

The Schur matrix S of R is positive semidefinite of rank two. Moreover A-diag(0,S) is a positive semidefinite rank-one matrix. Rank-one eigenvalue interlacing implies that the two nonzero eigenvalues of S are at least lambda_2(A),lambda_3(A), respectively, so in particular both are >=1. Equivalently, this follows from the variational eigenvalue characterization on the codimension-one orthogonal complement of the update vector.

The two-dimensional product marginal bound and the ellipse-shell area formula give p_R<=2pi. Conditional on the other original coordinates, the square change of variables gives

    p_Q(t) <= a^(-1/2) integral_{r<t} p_R(r)(t-r)^(-1/2) dr.

For any probability density p<=M, the one-sided layer-cake bound yields

    integral_{r<t} p(r)(t-r)^(-1/2) dr <= 2sqrt(M).

Consequently ||p_Q||<=2sqrt(2pi/a)<4sqrt(pi)<3e. This closes both leverage branches. A linear term in range(A) is removed by a translation of the original coordinates. Arbitrary affine kernel leakage and arbitrary extra quadratic eigenvalues are not added to this theorem. No new continuity claim is made here.

**Updated exact-rank-three map:** semidefinite forms are already done; sufficiently diffuse indefinite forms are done; the new ruled estimate handles the one-sheet side of every exact-rank-three indefinite form. The unhandled rank-three portion is in the localized/hybrid indefinite two-sheet side, outside existing quantitative pivot and grouped-coordinate branches. Do not assign all workers to reprove the semidefinite result.

## 7. Rigorous use of Claude's ruled one-sheet estimate for rough inputs

This section supplies a limiting justification for the new geometric tool; its main ruling idea and constant are Claude's Theorem C.

**Theorem 7.1.** Let U have three orthonormal columns and let

    Q=lambda_1 (u_1^T X)^2 + lambda_2 (u_2^T X)^2 - mu (u_3^T X)^2,
    lambda_1,lambda_2,mu >=1.

For every interval J contained in (0,infinity),

    P(Q in J) <= pi sqrt(2) |J|.                              (7.1)

Thus the restriction of its law to that half-line has density bounded by pi sqrt(2). Sign reflection covers the corresponding side for signature (1,2). A linear term in range(A) shifts the critical value after completing the square in the original coordinates. The theorem is NOT the other half-line or the unrestricted conjecture.

### Smooth compactly supported product inputs

Let Y=U^T X, with smooth compactly supported density rho. Put D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(mu)) and Delta=lambda_1 lambda_2 mu. In z=D y coordinates, the quadratic is z_1^2+z_2^2-z_3^2.

For s>0, define e_theta=(cos theta,sin theta,0) and e_theta_perp=(-sin theta,cos theta,0). A ruling is

    z(theta,t)=sqrt(s)e_theta+t(e_theta_perp+e_3).

It lies on the level s. For fixed t=z_3, its planar radius is sqrt(s+t^2), and the planar polar angle differs from theta by arctan(t/sqrt(s)); the angular Jacobian is one. Ordinary polar coarea therefore gives

    integral delta(z_1^2+z_2^2-z_3^2-s) h(z) dz
      = (1/2) integral_0^{2pi} integral_R h(z(theta,t)) dt dtheta. (7.2)

This can equivalently be read as an identity against output test functions, with no distributional ambiguity.

Transforming back to y yields

    p_Q(s) = (1/(2sqrt(Delta))) integral_0^{2pi}
                integral_R rho(D^(-1)z(theta,t)) dt dtheta.   (7.3)

The line velocity is v_theta=D^(-1)(e_theta_perp+e_3), with

    |v_theta|^2 = sin^2(theta)/lambda_1
                 +cos^2(theta)/lambda_2+1/mu.                 (7.4)

The inner integral is 1/|v_theta| times a two-dimensional orthogonal marginal of Y, evaluated at the projected line offset. That marginal is also an orthogonal two-dimensional marginal of the ORIGINAL product vector X. Its density is at most 2 by LPP. Here it is continuous, so the essential bound is a pointwise bound. No assertion that Y's three coordinates are independent is made.

It follows that

    p_Q(s) <= Delta^(-1/2) integral_0^{2pi} |v_theta|^(-1) dtheta.

Since

    Delta |v_theta|^2
      =lambda_2 mu sin^2(theta)+lambda_1 mu cos^2(theta)+lambda_1lambda_2
      >=2,

the right side is at most pi sqrt(2).

### Removal of smoothness and support assumptions

Each cap-one probability density f can be approximated in L1 by smooth compactly supported probability densities still bounded by one. One explicit construction is: truncate to [-R,R], replace the missing mass delta_R by an indicator of a disjoint finite interval of length delta_R, and convolve with a nonnegative smooth compactly supported probability mollifier. The replacement differs in L1 from f by at most 2delta_R before mollification. A diagonal choice of R and mollifier scale gives L1 convergence while preserving mass one and the cap.

Apply this independently in each coordinate. The product densities converge in L1, by the telescoping bound

    ||prod_i f_i^(k)-prod_i f_i||_1 <= sum_i ||f_i^(k)-f_i||_1.

Their pushforwards under the fixed Q converge in total variation. For every fixed interval J in (0,infinity), pass the smooth-input inequality (7.1) to the limit. This proves the same interval bound for the original rough law and hence its restricted essential density bound. It avoids evaluating a merely almost-everywhere bounded marginal density on an exceptional curve. No uniform convergence of pointwise density versions or continuity of the limiting density is asserted. QED.

## 8. Full-proof attempt: which implication remains unproved

The later companion GEOMETRIC_SYNTHESIS.md refines the reduction in this section to one precisely stated no-pivot density problem. The geometric obstacles described below remain relevant to that problem.

The source-correct combined route now has the following exact components:

- Every actual finite-dimensional three-eigenvalue problem is controlled by (4.1), without pivot nondegeneracy.
- A bounded original-coordinate core retaining three substantial directions remains controlled under the dense perturbation condition (5.1); arbitrary outside couplings are allowed.
- Exact-rank-three semidefinite forms are already controlled by the fleet theorem, and the new ruled argument controls the one-sheet side for the indefinite signature.
- Claude's D', D5 and mixed-hub results, together with the earlier ridge/window and physical-pair theorems, control their respective explicit cross-volume, leverage, exact-block and pivot conditions.

The missing full-target implication is an EXHAUSTIVE, parameter-uniform passage from the bare spectral hypothesis to a compatible controlled configuration. Neither the frame split nor the bounded-dimensional result alone proves it. A frame may have only one or two localized directions, leaving its three-dimensional Gram matrix small on every bounded coordinate core while some row remains too heavy for the chosen Fourier bound. A small dense remainder on the remaining light block need not be a separable phase, and cannot be discarded on unbounded inputs.

The projected-gradient theorem shows precisely what its own unsolved part would require: the loss L(E), as large as sqrt(3n), must be replaced or compensated in this hybrid situation. No dimension-independent bound on L(E) is claimed. The ruled theorem does not pay negative levels of the (2,1) signature, and no arbitrary-joint coarea substitute is used. The exact semidefinite theorem is not extrapolated to all higher-rank semidefinite matrices.

Thus the current synthesis closes identified substeps and removes a duplicated open-case assignment, but does not supply the unrestricted universal C. It also does not prove that the remaining class contains a counterexample. The workers' sole target stays the original full theorem.

## 9. Verification and provenance boundaries

The analytic proofs are Sections 2-7. The accompanying deterministic finite checker verifies the projected-gradient identity, the root/gradient constants, the core singular-value transfer for definite and indefinite examples with dense tails, the semidefinite Schur inequalities, and the ruling coarea Jacobian. It does not certify an infinite family by numerical sampling, validate every prior worker proof, or establish novelty.

Imported research sources, with their exact roles:

1. Claude package e5f71d79eff325201dd0274053d20268ce65b837, paths and blobs in Section 1: physical-fiber idea, geometric ruling, Fourier localization split.
2. LPP Theorem 1.1, arXiv:1507.07949v2: the cap-two two-dimensional marginal theorem. Primary source: https://arxiv.org/pdf/1507.07949 .
3. account02/B18 20260922T123541Z-account02-B18-QFORM-r11/REPORT.md, pinned at f8b6f4d6763094eedf3b23b845dce57e28279c55: the already-completed semidefinite rank-three result, restored to the combined map.
4. Interactive separable-phase report at 773b7fb6f0e6a8142066f0bac08d228dfc164fdb: the matching sharp diffuse-frame bound, not a new claim in this note.
5. Previous Claude-review package at 9844891a9fbe96a65e37f71122bf0300b53dcc80: scope corrections and valid numerical-law requirements.

All work is kept in the private mathematical repositories. Repository publication is not authenticated learned-memory ingestion, an independent review, or evidence that all eighty scheduled workers have consumed the update.

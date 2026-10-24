# Stable subordination and a finite-mean obstruction

## Stable subordination reduction (complete proof)

For 0<alpha<1 and a random locally finite measure Z, define S_alpha(Z) by the conditional Laplace functional

    E[exp(-integral f dS_alpha(Z))|Z]=exp(-integral f^alpha dZ)

for bounded nonnegative compactly supported Borel f. This includes conditional independent scattering. Existence follows by conditionally sampling a Poisson measure with intensity Z(dx)c_alpha z^(-1-alpha)dz, where c_alpha=alpha/Gamma(1-alpha), and summing its weighted atoms. On each compact the small-jump expected mass and large-jump count are finite. Integration by parts and substitution u=qz give integral_0^infinity (1-exp(-qz))c_alpha z^(-1-alpha)dz=q^alpha for q>0; boundary terms vanish since 0<alpha<1, and q=0 is immediate. The Poisson Laplace formula proves the defining identity.

The map Law(Z)->Law(S_alpha(Z)) is injective. For disjoint bounded Borel sets A_i, insert f=sum_i t_i^(1/alpha)1_A_i. The Laplace functional determines E exp(-sum_i t_i Z(A_i)) for every t_i>=0. These transforms determine the vector law: for U_i=exp(-Z(A_i)) in (0,1], integer t_i determine all mixed moments of U, hence all polynomial integrals on [0,1]^n. Stone--Weierstrass gives all continuous-function integrals and therefore the law. Apply the inverse -log to recover the vector of masses. Nondisjoint sets reduce to their disjoint Boolean partition. Finite-dimensional distributions on a countable family of bounded half-open boxes determine the random Radon measure law.

For a positive deterministic locally bounded weight w, its conditional Laplace functional gives

    w S_alpha(Z) =law S_alpha(w^alpha Z).

The same identity holds for a random weight conditional on the weight and Z if the stable Poisson sampling is conditionally independent of that weight given Z. Restrict to locally finite w^alpha Z if local boundedness is unavailable.

Suppose M has law S_alpha(Z). Take Z^epsilon(A)=Z_tilde(A/epsilon), with an independent copy Z_tilde independent of omega_epsilon, and conditionally sample S_alpha(Z^epsilon). Its law is precisely that required of M^epsilon. The weight identity and injectivity now show that the star equation for M is equivalent to

    Z =law exp(alpha omega_epsilon) Z^epsilon.

This equivalence holds for every epsilon as a random-measure identity, in both directions. Source normalization gives mean(alpha omega_epsilon)=-dt-gamma^2 t/2 and its centered part gamma X_t, for epsilon=exp(-t). Therefore Z solves the ordinary mean-normalized star equation at gamma. Any directing-measure uniqueness theorem yields uniqueness in the corresponding stable-subordination class; deterministic constants transform by the power 1/alpha.

**Gap:** a general solution M is not known to admit this conditional stable representation. The reduction also does not prove uniqueness of arbitrary critical directing measures. The cluster example in ATTEMPT.md demonstrates that representation does not follow from ergodicity alone.

## Finite mean: normalization (complete proof)

Assume M is stationary, nonzero, with finite expected mass on bounded sets. Its mean measure is locally finite and translation invariant, hence m dx by uniqueness of Haar measure on R^d. Here m>0: zero mean would force M=0 almost surely by countable exhaustion. M^epsilon has mean m epsilon^(-d)dx. Independence, Tonelli and the star equation give E exp(omega_epsilon)=epsilon^d.

With epsilon=exp(-t), alpha-normalization and the Gaussian moment formula yield

    E omega_epsilon=-(d/alpha)t-(gamma^2/(2alpha))t,
    log E exp(omega_epsilon)
      =-[d/alpha-gamma^2(1-alpha)/(2alpha^2)]t.

Comparison with -dt proves the necessary relation

    (1-alpha)(d alpha-gamma^2/2)=0.

This relation requires no higher moment and is not an existence criterion.

## Finite mean: excluding the other parameter regimes

The following proof uses the standard GMC degeneracy input explicitly. Assume k has sufficient regularity for the ordinary approximants

    G_t(A)=integral_A exp(beta X_t(x)-beta^2 t/2)dx,
    beta=gamma/alpha,

to converge to zero in probability when beta^2>=2d. This input holds for the usual regular compact-support star-field setting (the source's standard critical/supercritical chaos degeneracy theorem). Conditional expectation of U_t=integral_A exp(omega_epsilon) M^epsilon(dx), given the Gaussian weight, equals mG_t(A), using the finite-mean normalization above. U_t has the fixed integrable law of M(A).

These conditional expectations are uniformly integrable even with different couplings for different t. For U>=0 integrable and Y=E[U|F], on {Y>K} we have

    Y<=E[U1_{U>K/2}|F]+K/2.

Integrate and use (K/2)P(Y>K)<=E[Y1_{Y>K}]/2 to obtain

    E[Y1_{Y>K}]<=2 E[U1_{U>K/2}].

For U_t with fixed integrable law, the right side tends to zero uniformly. If beta^2>=2d, convergence in probability of G_t(A) to zero together with uniform integrability would imply E[mG_t(A)]->0. But its expectation is m|A|>0 for a bounded A of positive volume, a contradiction. Thus beta^2<2d. If alpha<1, the necessary relation already forces gamma^2=2d alpha, so beta^2=2d/alpha>2d, again a contradiction. Hence finite mean implies alpha=1 and gamma^2<2d in this regular-kernel setting.

**Gap:** this does not prove uniqueness in the entire finite-mean subcritical class, and the degeneracy input is not claimed for arbitrary irregular kernels beyond its established hypotheses.

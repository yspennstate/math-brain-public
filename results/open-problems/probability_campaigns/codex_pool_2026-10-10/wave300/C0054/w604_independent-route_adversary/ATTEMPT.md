# C0054 independent approach, saved before paired-proof access

2026-10-10, w604. Exact intake statement and primary-source hypotheses are still being recovered. Current openness: UNKNOWN. No parent-problem solved claim.

Investigate one-site fractional-moment decoupling rather than a recorded proof's multiscale or sigma-model argument. First derive the recursion from the Schur complement with conditioning explicitly stated. Compute its contraction coefficient for the source's actual variance profile. In a row-normalized Gaussian band ensemble, both diagonal disorder and each hopping have small variance; spectral averaging may cancel the apparent smallness of individual hoppings. A sum over the band then needs genuine contraction, not just finiteness of each fractional moment. This is a candidate obstruction, not yet a theorem or verdict about the paired proof.

If one-site contraction fails, identify exactly the finite-block estimate that would replace it: a fractional-moment bound on the whole outgoing boundary sum, uniform in imaginary part, finite volume, and allowed boundary conditioning. Do not multiply marginal good-block probabilities into a joint event without independence or a derived filtration.

The exact intake row is now recovered: fixed W in d=2, bulk localization on scale exp(W^2) and Poisson local statistics as the box side grows. Source locator: Bourgade ICM 2018, Conjecture (0.2), page 2; Section 2.2, page 7. The previous attempt C0054-A001 already used fractional moments. Consequently the new independent lane is the finite-strip-to-plane limit below. The one-site calculation remains a correction/audit of that previous attempt, not a different-method solution attempt.

## Independent route: audit the strip limit before using transfer matrices

Saved before reading w603's APPROACH_PRECOMMIT.md or any proposed proof. Transfer matrices can establish localization on each strip of finite transverse width. The hardest step for this route is a quantitative estimate uniform as transverse width tends to infinity, in BOTH coordinates. Separate statements for each strip do not supply it. The following elementary model proves this logical obstruction; it is not a counterexample to the independent Gaussian band-matrix ensemble.

Let v=(v_x) be any bounded real sequence, let A on l^2(Z) be diagonal with A delta_x=v_x delta_x, and let T be the free adjacency operator on l^2(Z), (Tf)(y)=f(y-1)+f(y+1). Define H=A tensor I+I tensor T on l^2(Z^2). For M>=1 let T_M be the adjacency matrix of the path {1,...,M} with Dirichlet endpoints, and let H_M=A tensor I_M+I tensor T_M on the corresponding infinite strip.

The functions delta_x tensor u_{M,k}, where

u_{M,k}(j)=sqrt(2/(M+1)) sin(pi*k*j/(M+1)), 1<=k,j<=M,

form an orthonormal eigenbasis for H_M. Their eigenvalues are v_x+2 cos(pi*k/(M+1)). Thus every H_M has pure point spectral type and a compactly supported eigenbasis. Each basis vector satisfies an exponential bound in the full strip metric with rate 1 and a prefactor at most exp(M). Longitudinal localization is exact and uniform in M. These are assertions about an eigenbasis/spectral type, not about all vectors in potentially degenerate eigenspaces.

However, H is the orthogonal direct sum over x of v_x+T. Fourier transformation in y makes each summand multiplication by v_x+2 cos(theta) on L^2([0,2pi],dtheta/(2pi)). Its spectral measures are absolutely continuous: for every Lebesgue-null energy set B, its inverse image under 2cos(theta)+v_x has zero measure (change variables on (0,pi) and (pi,2pi), with only the endpoints exceptional). The direct sum is therefore purely absolutely continuous. H has no nonzero l^2 eigenvectors. It is also the strong limit of strip restrictions in the usual exhausting-domain sense.

The transverse loss is explicit. For M>=2 and k=1,

sum_j |u_{M,1}(j)|^4=3/(2(M+1)),

using sin^4(theta)=(3-4cos(2theta)+cos(4theta))/8 and the finite cosine sums. Thus the participation volume grows linearly with M; no uniform transverse localization follows from the finite-strip assertions. The model has correlated/absent hopping randomness and is outside C0054's hypotheses. It refutes only the naked inference from localized finite strips to a localized plane, and pinpoints the missing transverse-uniform premise.

Repair target for a genuine strip route: establish constants C,mu>0 at fixed W and a named bulk energy interval, independent of strip width and longitudinal volume, such that the expected eigenfunction correlator or fractional resolvent moment decays in the FULL two-dimensional distance. If using resolvents, include all eta>0 and justify the infinite-volume limit. This is still an unproved estimate for C0054; neither positive strip Lyapunov exponents nor finite-width pure point spectrum alone proves it. Poisson statistics also needs its own hypotheses and estimates.

NEXT: Verify Bourgade's primary statement, inspect w603's key step, and obtain w605's independent review of this counterexample and the separate one-site correction.

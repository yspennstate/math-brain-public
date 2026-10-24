# Independent derivation, saved before reading w549's proof

2026-10-10. Source read first: Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240v2, Section VI.2 (HTML lines 1688–1692). The source describes a hexatic through fast translational and slow sixfold orientational correlations. It gives a physical scenario, not an exact quantified existence theorem. Current openness remains UNKNOWN.

My disjoint lane is a quantitative obstruction to transferring orientational order from an effective field to a microscopic observable. This construction is an abstract stationary field, not a Riesz Gibbs state and not a counterexample to P0321.

## A uniformly accurate correlation comparison can lose the entire algebraic tail

Fix dimension 2, exponent 0 < a <= 2, and cutoff R >= 1. Let G have Gamma(shape=a/2, rate=1) law. Conditional on G, let K be a centered Gaussian vector with covariance 2G I_2. Let U be independent and uniform modulo 2pi. Define the unit-modulus field

    X(x) = exp(i(U + K dot x)), x in R^2.

Its law is stationary: translating x only adds K dot h to a uniform conditional phase. Its two-point correlation is

    A(r) = E[X(x) conjugate(X(y))]
         = E[exp(-G r^2)] = (1+r^2)^(-a/2), r=|x-y|.

The last equality follows by integrating the Gamma density. The field's law is also isotropic because the conditional law of K is isotropic.

Take an independent centered Gaussian Q with covariance 2R^(-2) I_2. Replacing K by K+Q gives another stationary, isotropic, unit-modulus field Y_R with correlation

    B_R(r) = A(r) exp(-(r/R)^2).

For 0 < r <= R, use 1-exp(-t) <= t and A(r) <= r^(-a):

    0 <= A(r)-B_R(r) <= r^(2-a)/R^2 <= R^(-a).

For r >= R, use A(r) <= r^(-a) <= R^(-a); at r=0 the difference is zero. Therefore

    sup over r>=0 |A(r)-B_R(r)| <= R^(-a).

For every fixed finite R and every b>0,

    lim as r->infinity r^b B_R(r) = 0,

whereas lim r^a A(r)=1. Thus any fixed positive additive tolerance, however small and even uniform over ALL distances, cannot imply an algebraic lower tail. Both correlations are realized by bounded fields; this is more than an arbitrary scalar-function example. The fields need not be ergodic, have local Gibbs specifications, or be geometric sixfold bond observables; no such conclusion is asserted.

For a sixfold notation one may write X=exp(i6theta) with theta=(U+K dot x)/6 modulo pi/3. This does not identify theta with the Delaunay bond orientation of a particle configuration.

## The sufficient bridge has an error that decays on the signal scale

Suppose an effective correlator A obeys c r^(-a) <= A(r) <= C r^(-a) for r>=r0, with real A, 0<c<=C. A microscopic complex correlator B satisfies

    |B(r)-A(r)| <= delta r^(-a), 0 <= delta < c,

for every r>=r0 in the SAME infinite-volume state. Then

    (c-delta) r^(-a) <= Re B(r) <= |B(r)| <= (C+delta) r^(-a).

Proof: Re B >= A-|B-A| and the triangle inequality. No independence is used. A finite-volume version also works if the same estimates hold with constants independent of volume and converge at each fixed r to B before r tends to infinity.

The unresolved P0321 bridge is a derivation of such a scale-relative comparison for the actual geometric bond observable of a Riesz Gibbs state, together with fast translational correlations on a nonempty common temperature interval. An effective-field algebraic bound, additive approximation, or translation invariance alone does not establish it.

Referee: w551, independent check pending. This is an elementary proof offered for review, not an independently checked proof or a solution of the phase problem.

## Optional strengthening: the obstruction also has an ergodic version

This section was saved before the paired proof was read. It removes the possible objection that the random-wavevector examples have nonergodic laws.

The kernels A(|x-y|) and B_R(|x-y|) are positive definite: exp(-t|x-y|^2) is the characteristic function of a Gaussian wavevector, A is its Gamma mixture, and B_R is the product with another such kernel. They have value 1 at zero. Therefore they are covariance kernels of centered stationary isotropic real Gaussian fields H and H_R of variance 1. Their covariances tend to zero at infinity. For any two finite cylinder blocks, the Gaussian cross-covariance matrix tends to zero under distant translations, so their joint characteristic function factors in the limit. This gives mixing for cylinder observables, and hence ergodicity.

Set S(x)=sign H(x) and T_R(x)=sign H_R(x). They are mean-zero stationary isotropic ergodic fields with values in {-1,1}; zero values of H have probability zero at any specified site. For a pair of centered unit Gaussians of correlation t, writing them as Z and tZ+sqrt(1-t^2)W with independent standard Z,W, rotational invariance of (Z,W) gives the quadrant formula and

    E[sign H(x) sign H(y)] = f(A(r)),
    E[sign H_R(x) sign H_R(y)] = f(B_R(r)),
    f(t) = (2/pi) arcsin(t).

For 0<=v<=u<=1,

    arcsin(u)-arcsin(v)
      = integral_v^u (1-t^2)^(-1/2) dt
      <= 2(sqrt(1-v)-sqrt(1-u)) <= 2 sqrt(u-v).

It follows that sup_r |f(A(r))-f(B_R(r))| <= (4/pi)R^(-a/2), which again can be made arbitrarily small. Since f(t)/t tends to 2/pi at zero, the first sign correlation is asymptotic to (2/pi)r^(-a) and the second decays faster than every power. An additional ergodicity premise therefore does not repair fixed additive correlation transfer. These are still abstract fields, not particle Gibbs states or identified geometric bond observables. The Gaussian covariance construction and the ergodicity extension require the referee's independent check.

# fleet02/B15 — multi-subdensity Fresnel receiver and rough-input audit

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260924T111432Z-fleet02-B15-QFORM-auto11
Status: SUPPORTING_LEMMA_PROVED / SOURCE_APPLIED / PARTNER_OBSTRUCTION_APPLIED / FULL_QFORM_OPEN

## First unpaid implication

The universal QFORM theorem remains open. In B15's scope, rough-input limiting and output continuity are not the missing implication. The live gap is structural: from bare s_3(A)>=1, produce a product-preserving aggregate reduction into a quantitatively paid diffuse-rank-three/diagonal, localized physical block, grouped crossing, or hub receiver before taking reciprocal local minors or worst fibres. The generic two-sheet X-ray shortcut remains invalid.

## Source theorem used

At current compatible source descendant of e5f71d79eff325201dd0274053d20268ce65b837, Theorem F states: write

A = sum_{k=1}^3 lambda_k v_k v_k^T + B,

let I be a set of original coordinates for which B_II is diagonal, put rho_i=((v_1)_i,(v_2)_i,(v_3)_i), G=sum_{i in I} rho_i rho_i^T, and assume G is invertible and

c_i := rho_i^T G^{-1} rho_i <= 1/2

for i in I. For probability inputs with densities <=1, arbitrary outside blocks and arbitrary affine terms,

|phi(t)| <= (4 pi)^{3/2}|t|^{-3/2} (|lambda_1 lambda_2 lambda_3| det G)^{-1/2},

hence

||p_Q||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G)^(-1/3).

The proof conditions on the complement of I; B_II diagonal leaves a product of one-dimensional twisted Fourier factors, and the normalized rows form a tight frame for geometric Brascamp-Lieb.

## New theorem: simultaneous subdensity refinement of Theorem F

Let S be any subset of I. For i in S replace the i-th probability density by an arbitrary subdensity h_i with

0 <= h_i <= 1,    integral h_i = m_i in [0,1].

For i in I\S one may even use an arbitrary cap-one subdensity of mass <=1. Keep the outside coordinates probabilistic. Let nu_S be the resulting finite output measure of the same quadratic-affine map. Put

L = |lambda_1 lambda_2 lambda_3|.

Then nu_S has an essentially bounded density and

||d nu_S/ds||_infinity
 <= 12 (L det G)^(-1/3)
    product_{i in S} [(2 sqrt(c_i))^(-2 c_i/3) m_i^(1-2 c_i/3)],

with the continuous convention that the factor at c_i=0 is m_i.

This is multiplicative in simultaneous rare pieces. It strictly extends the one-coordinate submass estimate.

### Proof

Fix outside coordinates. In the source Fresnel representation, the i-th twisted factor has the form

a_i(x)=h_i(x) exp(i tau_i(x)),

so |a_i|=h_i. For i in S,

||hat a_i||_infinity <= m_i,

and by Plancherel plus 0<=h_i<=1,

integral |hat a_i(u)|^2 du = 2 pi integral h_i(x)^2 dx <= 2 pi m_i.

Since p_i=1/c_i>=2,

integral |hat a_i|^{p_i}
 <= ||hat a_i||_infinity^{p_i-2} integral |hat a_i|^2
 <= 2 pi m_i^{p_i-1}.

For i not in S, complete the cap-one subdensity to a cap-one probability density and use the source L^p lemma unchanged. Therefore, relative to Theorem F, each selected coordinate contributes the factor

eta_i=(2 sqrt(c_i))^{-c_i} m_i^{1-c_i}

inside the |t|^{-3/2} envelope. Thus

|hat nu_S(t)|
 <= B |t|^{-3/2},

B=(4 pi)^{3/2}(L det G)^(-1/2) product_{i in S} eta_i.

The total mass satisfies

|hat nu_S(t)| <= M := product_{i in S} m_i.

Hence

integral_R |hat nu_S(t)| dt
 <= integral_R min(M,B|t|^{-3/2}) dt
 = 6 B^{2/3} M^{1/3}.

Fourier inversion gives the essential-height estimate

||d nu_S/ds||_infinity <= (2 pi)^(-1) 6 B^{2/3}M^{1/3},

which simplifies exactly to the displayed constant 12 and the mass exponent

(2/3)(1-c_i)+1/3 = 1-2c_i/3.

No continuity premise is used to pay this height. Absolute integrability of the Fourier transform also supplies a continuous representative as a downstream byproduct in this chamber.

### Uniform single-factor simplification

For 0<=c<=1/2,

(2 sqrt(c))^{-2c/3} <= exp(1/(12e)),

because its logarithm is -(c/3)log(4c), maximized at c=1/(4e). Also 1-2c/3>=2/3. Hence every selected factor obeys

(2 sqrt(c_i))^{-2c_i/3} m_i^{1-2c_i/3}
 <= exp(1/(12e)) m_i^{2/3}.

The exact leverage-sensitive formula is much stronger when c_i is small.

## Real target inequality: three diffuse banks with k rare coordinates

Let m>=2 and split 3m original independent coordinates into three disjoint banks. Set

Y_a = m^{-1/2} sum_{r=1}^m X_{a,r},    a=1,2,3,
Q_m = Y_1^2 + Y_2^2 - Y_3^2.

The matrix has nonzero spectrum {1,1,-1}, so it is exactly in the owner target. Here G=I_3 and every leverage is c_i=1/m. The completed source Theorem F gives the full-law inequality

||p_{Q_m}||_infinity <= 12.

Now choose any k original coordinates and replace their densities by cap-one subdensities of a common mass theta in [0,1]. For the corresponding output submeasure nu_{m,k,theta}, the new theorem gives

||d nu_{m,k,theta}/ds||_infinity
 <= 12 (2/sqrt(m))^{-2k/(3m)} theta^{k(1-2/(3m))}.

Thus simultaneous rare-coordinate pieces are multiplicatively suppressed. For fixed theta<1 and k proportional to m, the decay in theta is exponential in m; roughness does not accumulate adversarially in this diffuse rank-three family.

The source ruled Theorem C separately pays its one-sheet side by

P(Q_m in I, Q_m>=0) <= pi sqrt(2) |I|.

Theorem F is the full-law receiver here, so the convex/two-sheet side is also paid without invoking any generic X-ray claim.

## Partner fleet03/B15 result applied as a route obstruction

Newest compatible fleet03/B15 proves: for any random-center Gaussian scale mixture

Y=M+sqrt(T)G,  G~N(0,1),  E T^{-1/2}<=sqrt(2pi),

every unit interval has mass at most

q_* = 2 Phi(sqrt(pi/2))-1 = 0.7899085945560627... .

Therefore any such probability law has total-variation distance at least

1-q_* = 0.2100914054439373...

from Uniform[0,1], equivalently L1 distance at least

2(1-q_*) = 0.4201828108878746... .

This is a genuine obstruction to using a fixed inverse-scale Gaussian-mixture dense-class argument and then invoking B15 output-law stability: even one uniform marginal cannot enter a perturbative L1 regime. For n-fold products the partner's cube event gives TV gap >=1-q_*^n, tending to one. This does not contradict the new subdensity theorem; it shows that a successful rough-law decomposition must use a non-Gaussian product-preserving receiver for the residual/narrow component rather than a fixed-budget Gaussian-mixture approximation alone.

## Independent ruled / rough-input bridge audit

For q_0(z)=z_1^2+z_2^2-z_3^2 and the one-sheet ruling

F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3),

direct differentiation gives

F_theta x F_t = (1/2) grad q_0(F),

hence

d sigma/|grad q_0| = (1/2) d theta d t.

After undoing spectral scaling for curvatures (lambda_1,lambda_2,mu), the ruling direction is

v_theta=(-sin(theta)/sqrt(lambda_1), cos(theta)/sqrt(lambda_2), 1/sqrt(mu)).

The parameter t is not arclength, so the line trace contributes 1/|v_theta|. The two-dimensional product-projection cap 2 cancels the coarea factor 1/2, reproducing the source coefficient

C_+ = (lambda_1 lambda_2 mu)^(-1/2)
      integral_0^{2pi} [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta.

For rough original-coordinate marginals, mollify only those original factors. Cap one, probability mass and independence are preserved and

|| product_i f_i^(eta) - product_i f_i ||_1
 <= sum_i ||f_i^(eta)-f_i||_1 -> 0.

Restriction to the fixed conditional one-sheet event and deterministic quadratic pushforward contract total variation, so the smooth interval inequality passes with the identical constant. If an ambient conditioning step leaves an invertible active physical 3x3 block B, then

x^T B x + 2 d^T x + c
 = (x+B^{-1}d)^T B (x+B^{-1}d) + c',

which is a translation in original independent coordinates; in this scope the source affine-range correction is automatic. This passage proves essential interval domination directly and does not use output continuity.

## Regularity ledger

Qualitative absolute continuity is separate: for a nonconstant quadratic-affine map, the critical set is empty or a proper affine subspace; local coarea off that null set shows the pushforward of an absolutely continuous input law is absolutely continuous. This gives no universal height. In the results above, essential height is paid by the Fourier or ruled interval estimates. Continuous/C0 representatives, where available, are downstream.

## Remaining connection

The new simultaneous-subdensity theorem closes a regularity/decomposition interface inside the diffuse Theorem-F chamber: high-order rare pieces are paid multiplicatively and rough-input passage has zero loss. It does not supply the missing structural theorem that extracts such a chamber from an arbitrary symmetric A with s_3(A)>=1. The first unpaid implication remains aggregate-before-inversion: control high-leverage/localized and higher-rank twisted carriers without reciprocal-minor or worst-fibre dimension loss, while retaining product provenance.

## Source pins consumed

- owner brain main resolved at start: 3bc49ca35f334a553ab4f72233284cfe104672c2
- owner control revision: 2026-09-22.15
- math-open-problems master resolved during proof: 748e05ad831bd74e439cf1911c20f80d8f44a45c, verified descendant of e5f71d79eff325201dd0274053d20268ce65b837
- required source files read: RESULTS.md, FOURIER_ROUTE_REPORT.md, COUNTEREXAMPLE_SEARCH.md at the decoupling-brascamp-lieb record
- newest partner handoff read: fleet03/B15 20260924T102515Z plus correction addendum

Full QFORM remains OPEN.

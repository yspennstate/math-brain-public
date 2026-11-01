SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T11:48:04Z.
attacking: countable rational-skeleton localization with exact preservation of the full affine interval-concentration constant across rough product laws, distant fragments, unbounded supports, threshold eigenvalues, and arbitrary shifts.

# QFORM-COUNTABLE-RATIONAL-SKELETON-LOCALIZATION-v1

Programme: QFORM-DENSITY-3EIG-20260922
Worker: fleet03/B14 (Translations and localization)
Run: 20260923T114804Z-fleet03-B14-QFORM-r34
Status: SUPPORTING TARGET-LEVEL LOCALIZATION THEOREM PROVED; FULL QFORM OPEN
Continuity: NOT PROVED by this localization theorem
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Exact theorem

For n>=3 let D_n be the set of product probability laws mu=mu_1 x ... x mu_n on R^n whose one-dimensional densities satisfy 0<=f_i<=1. Let A_n be the real symmetric n x n matrices having at least three eigenvalues of modulus at least one. For A in A_n, ell in R^n, c in R, write

P_{A,ell,c}(x)=x^T A x+ell^T x+c.

For a bounded interval I of positive length define its concentration ratio

R(mu,A,ell,c,I)=mu{P_{A,ell,c} in I}/|I|.

Define C_full^aff as the supremum of R over all n>=3, mu in D_n, A in A_n, ell,c and bounded intervals I.

Define the rational skeleton S as the tuples with all of the following properties:

1. every marginal has density 1_E where E is a compact finite union of intervals with rational endpoints and |E|=1;
2. A is symmetric with rational entries, has simple nonzero spectrum, and has at least three eigenvalues satisfying |lambda|>1 strictly;
3. ell is rational, c is rational;
4. I has rational endpoints.

Let C_rat^aff be the supremum of R over this skeleton. Then, in the extended interval [0,infinity],

    C_full^aff = C_rat^aff.                                      (1.1)

There is an independent homogeneous version: if ell=c=0 on both sides, then

    C_full^hom = C_rat^hom.                                      (1.2)

Thus, for essential boundedness, the original conjecture can be proved with exactly the same universal constant by proving it only on a COUNTABLE class consisting of compact finite-fragment product inputs, rational generic matrices lying strictly inside the spectral target, and rational test intervals. No support radius, moment bound, fragment-count bound, fragment-separation bound, eigenvalue gap, or translation penalty is introduced.

The affine version is the useful translation-stable compiler. It does not assert C_full^aff=C_full^hom; singular A can prevent an affine term from being removed by a deterministic translation.

## 2. Rationalization of one finite-fragment marginal

Lemma 2.1. Let E be a compact finite union of intervals with |E|=1. There are compact finite unions E_m with rational endpoints, |E_m|=1 exactly, and |E_m Delta E|->0.

Proof. Merge touching components and discard null components, writing

    E = union_{r=1}^R [a_r,b_r],

with positive gaps and lengths l_r=b_r-a_r>0 satisfying sum_r l_r=1. If R=1, then l_1=1; choose rational alpha_m->a_1 and put E_m=[alpha_m,alpha_m+1].

For R>1 choose positive rational q_{r,m}->l_r for r<R so close that sum_{r<R}q_{r,m}<1, and set

    q_{R,m}=1-sum_{r<R}q_{r,m}.

Then q_{R,m}>0 is rational and tends to l_R. Choose rational left endpoints alpha_{r,m}->a_r. Since the original finite collection has a positive minimum gap, the approximations may be chosen sufficiently close that the intervals

    [alpha_{r,m}, alpha_{r,m}+q_{r,m}]

remain disjoint and in the same order. Their total length is exactly sum q_{r,m}=1. Endpoint convergence gives |E_m Delta E|->0. QED.

For the probability laws dmu=1_E dx and dmu_m=1_{E_m}dx,

    d_TV(mu,mu_m) = (1/2)|E Delta E_m|.                         (2.1)

For products, the standard telescoping coupling inequality gives

    d_TV( tensor_i mu_i, tensor_i mu_{i,m})
       <= sum_i d_TV(mu_i,mu_{i,m}).                            (2.2)

No common bound on the number, diameter, or locations of the components is used.

## 3. Rational generic matrices are dense in the target from the correct side

Lemma 3.1. For every A in A_n there are rational symmetric matrices A_m such that

(a) ||A_m-A||_op -> 0;
(b) A_m is invertible and has simple spectrum;
(c) A_m has at least three eigenvalues of modulus strictly greater than one.

Proof. Use an orthogonal diagonalization only to perturb the MATRIX, never the random variables. Choose three eigenvalues of A with modulus >=1. For eps_m down to zero, perturb those selected eigenvalues outward by sign(lambda) eps_m. Perturb every eigenvalue by additional distinct amounts o(eps_m) chosen to remove all coincidences and zeros. This produces a real symmetric B_m with simple nonzero spectrum, with the selected three eigenvalues strictly outside [-1,1], and ||B_m-A||_op->0.

The set of symmetric matrices having simple nonzero spectrum and at least three eigenvalues with modulus >1 is open: simplicity and nonzeroness have positive spectral gaps at each fixed B_m, and the strict threshold has positive margin. Rational symmetric matrices are dense entrywise, hence in operator norm in fixed dimension. Choose a rational symmetric A_m sufficiently close to B_m to remain in that open set, while also forcing ||A_m-A||_op->0. QED.

This step does NOT rotate X. Independence remains in the original coordinates.

## 4. Quantitative event transfer on a compact product extreme law

Fix a finite-fragment product law nu with compact support K and put

    R = sup_{x in K} ||x||_2 < infinity.

Choose rational-fragment product laws nu_m as in Lemma 2.1, rational generic A_m as in Lemma 3.1, ell_m in Q^n with ell_m->ell, and c_m in Q with c_m->c. Define

    delta_m = d_TV(nu,nu_m),
    eta_m = R^2 ||A_m-A||_op + R ||ell_m-ell||_2 + |c_m-c|.

For every x in K,

    |P_{A_m,ell_m,c_m}(x)-P_{A,ell,c}(x)| <= eta_m.            (4.1)

Hence for every bounded interval I,

    {P_{A,ell,c} in I} cap K
       subset {P_{A_m,ell_m,c_m} in I^{eta_m}},                (4.2)

where I^{eta} is the eta-neighborhood of I. Therefore

    nu{P_{A,ell,c} in I}
      <= nu_m{P_{A_m,ell_m,c_m} in I^{eta_m}} + delta_m.       (4.3)

For any rho_m>0 choose a rational-endpoint interval J_m containing I^{eta_m} and satisfying

    |J_m| <= |I| + 2 eta_m + rho_m.                            (4.4)

If every skeleton tuple obeys the bound with constant C, then (4.3)-(4.4) give the explicit localization inequality

    nu{P_{A,ell,c} in I}
      <= C ( |I| + 2 eta_m + rho_m ) + delta_m.                (4.5)

Here eta_m->0, delta_m->0 and rho_m may be sent to zero. Thus the SAME C holds for every compact finite-fragment product law, every target matrix including repeated/zero eigenvalues and eigenvalues exactly at |lambda|=1, every real affine term, and every real interval.

The radius R appears only multiplied by approximation errors that are sent to zero. There is no uniform-radius hypothesis and no radius-dependent constant.

## 5. Actual application of the designated partner result

The completed fleet04/B14 affine-family localization compiler is:

yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee
proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T001323Z-fleet04-B14-affine-mixture-compiler-r5/REPORT.md

Its finite-mixture statement says every cap-one marginal law is an L1 limit of finite convex combinations of compact finite-union indicator laws of total measure one. Expanding the product gives a finite convex combination of compact finite-fragment PRODUCT laws, and uniform affine interval estimates pass by convexity and total variation.

Apply that completed partner theorem to the inequality proved in Section 4. Let mu in D_n be arbitrary. The partner supplies approximants

    mu^(r) = sum_alpha w_{r,alpha} nu_{r,alpha},

where w_{r,alpha}>=0, sum_alpha w_{r,alpha}=1, every nu_{r,alpha} is a compact finite-fragment product extreme law, and

    tau_r = d_TV(mu,mu^(r)) -> 0.

Section 4 already gives, for the SAME A,ell,c,I and the SAME constant C,

    nu_{r,alpha}{P_{A,ell,c} in I} <= C |I|

for every alpha. Therefore the actual partner-to-target inequality is

    mu{P_{A,ell,c} in I}
      <= tau_r + mu^(r){P_{A,ell,c} in I}
      =  tau_r + sum_alpha w_{r,alpha}
                    nu_{r,alpha}{P_{A,ell,c} in I}
      <= tau_r + C |I|.                                       (5.1)

Let r->infinity. This gives

    mu{P_{A,ell,c} in I} <= C |I|                             (5.2)

for the arbitrary original cap-one product law, with NO moment, tail, support, or fragment penalty.

This is the required completed-partner result applied to an actual inequality.

## 6. Equality of optimal constants

The rational skeleton is a subclass of the full affine class, so

    C_rat^aff <= C_full^aff.                                   (6.1)

If C_rat^aff=infinity, (6.1) already forces equality. Otherwise take any C>C_rat^aff. By definition every rational-skeleton tuple obeys the interval inequality with constant C. Sections 2-5 transfer that inequality to the entire full affine class with the identical C, so C_full^aff<=C. Let C decrease to C_rat^aff. Together with (6.1) this proves (1.1).

The same argument with ell=c=0 throughout proves (1.2).

The skeleton is genuinely countable: for each n, finite lists of rational interval endpoints, rational matrix entries, rational affine coefficients, rational constants and rational test-interval endpoints form a countable set, and the countable union over n remains countable. Countability does NOT impose a finite fragment-count bound or a bounded-diameter bound.

## 7. Arbitrary translations are free in the affine compiler

For a deterministic h in R^n and X=Y+h,

    P_{A,ell,c}(Y+h)
      = Y^T A Y + (ell+2Ah)^T Y
        + c + ell^T h + h^T A h.                               (7.1)

Coordinatewise translation preserves independence and the cap-one property. Formula (7.1), together with the affine theorem, therefore handles arbitrary physical shifts and arbitrarily distant fragments without completing a square in a rotated basis or assuming A invertible.

For the original homogeneous target, (1.2) is already enough. The affine version is useful because conditioning/local physical translations elsewhere in the fleet naturally generate ell and c.

## 8. From interval concentration to an L-infinity density

If a probability law zeta on R satisfies

    zeta(I) <= C |I|

for every bounded interval I, then by decomposing open sets into countably many disjoint intervals and using outer regularity one obtains zeta(E)<=C|E| for every Borel E. Thus zeta is absolutely continuous with Radon-Nikodym derivative p satisfying ||p||_infinity<=C. Hence a universal skeleton interval bound implies exactly the essential-bounded-density conclusion of QFORM.

This argument does not imply that p has a continuous representative. TV limits of laws with continuous bounded densities need not preserve continuity without additional uniform regularity. Continuity therefore remains a separate OPEN requirement.

## 9. What this closes and what remains

Closed by this theorem, with zero constant loss:

- arbitrary deterministic shifts;
- arbitrary real affine terms;
- arbitrary unbounded input supports;
- arbitrarily distant fragments;
- arbitrary finite fragment counts at the approximation stage (with no uniform cap);
- repeated eigenvalues, zero eigenvalues away from the required three, and target eigenvalues exactly at modulus one;
- irrational matrix entries, affine coefficients, fragment endpoints and interval endpoints.

Not closed:

- the hard analytic/structural estimate on the countable skeleton itself;
- the no-pivot/grouped-bank mechanism forced only by s_3(A)>=1;
- continuity of the full target density.

In particular, this theorem is a localization compiler, not a proof of the unrestricted QFORM conjecture and not a counterexample. It is compatible with the live corrections against bounded-diameter localization and fixed fragment-count localization because the skeleton allows arbitrarily large diameters, arbitrary separations, and arbitrary finite numbers of fragments.

## 10. Source integrity

Fresh final owner control: yspennstate/math-research-brain@ccd134e403fd9445f09e4d4a286ecc877128491c, revision 2026-09-22.15.
Current programme status read: FULL_CONJECTURE_OPEN.
Current claims read: QFORM-FULL OPEN; QFORM-CONTINUOUS-REPRESENTATIVE OPEN.
Live correction inbox refreshed before this report; no rational-skeleton or partner finite-mixture correction was found.
Partner theorem source read directly at the immutable commit/path stated in Section 5.
No general rotation of the random variables, moment condition, compact-support assumption on the final law, connected-support assumption, Gaussian/log-concave assumption, or Monte Carlo premise is used.
Native receiver-memory ingestion was not observed: WITHOUT_VERIFIED_BRAIN.

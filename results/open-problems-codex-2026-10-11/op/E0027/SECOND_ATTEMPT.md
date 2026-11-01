# E0027 renewed attempt: two routes

2026-10-12. The original unrestricted question remains open in this work. This note supplements ATTEMPT.md rather than replacing its valid results.

## Two approaches not pursued in the first attempt

1. Transfer integrable remainders in the extended Kanda-Forst-Rao (EKFR) criterion, instead of transferring arbitrary finite-energy measures. Write Im psi_i=g_i+h_i with |g_i|<=A_i f(A_i) and integral |h_i|/B_i^2 finite. Try to build the sum's good/remainder decomposition directly. The new difficulty is cancellation of the two imaginary parts, which can shrink the sum denominator. Pursue a frequency split: cancellation is harmless where the sum is already sector-controlled, and only exceptional frequencies outside that region need estimating.

2. Apply local absolute continuity of Levy path laws (Hu-Sun-Wang Theorems 4.5 and 4.7, arXiv:1903.00050, PDF pp. 14-15). For a sum to be locally absolutely continuous with respect to X, one needs unchanged Gaussian covariance, an absolutely continuous increment of its Levy measure with finite Hellinger integral, and a drift compatibility equation. This may provide stability without any resolvent-density hypothesis. It is a genuinely different reduction from the previous energy method, although the neighbouring theorem itself is already published. Its restrictions prevent immediate application to arbitrary independent (H) summands.

Route 1 is selected: it directly avoids the first attempt's counterexample to energy inclusion into either summand. Route 2 will be checked as a comparison, especially to identify whether it reaches cases beyond Route 1.

## Brain questions

The required read-only math-store recall was asked about the gap, using:

* "Hunt hypothesis finite energy sum extended Kanda Forst Rao integrable remainder Hu Sun"
* "Levy local absolute continuity Hellinger change measure Hunt hypothesis"

The first query returned the known warning that failure of a Kanda-Forst bound is not a failure of (H), a general finite-energy card, and unrelated energy results. No verified lemma establishing remainder transfer was returned. The second query is being inspected. No brain-writing command is used in this renewed attempt.

## Verified inputs

Source survey Theorem 2.8, arXiv:1908.06825 PDF p. 6: under lower semicontinuity of all 1-excessive functions (equivalently here resolvent densities), the EKFR decomposition just described implies (H). The envelope is positive increasing and has divergent integral ds/(s f(s)). This input was read directly from the saved source.

Hu-Sun 2018, arXiv:1702.07396, Proposition 4.5 and proof, PDF pp. 15,17-18: one EKFR summand plus a second summand with a common Rao bound gives (H). Its proof splits frequencies where the sum imaginary part exceeds the good envelope. It does not assert closure of two arbitrary EKFR summands. We must not substitute that stronger assertion into its proof.


## Route 1 result: remainder transfer with a cancellation split

Use A_i=1+Re psi_i, B_i=|1+psi_i|, A=1+Re psi_1+Re psi_2, I=Im psi_1+Im psi_2 and B=sqrt(A^2+I^2). Assume each summand and the sum have resolvent densities. Suppose that for one finite-valued nondecreasing f>=1 with divergent integral ds/(s f(s)),

    Im psi_i=g_i+h_i,
    |g_i|<=A_i f(A_i),
    integral_R^n |h_i(z)|/B_i(z)^2 dz < infinity, i=1,2.

These are two EKFR summands, not just two Rao summands. Set G=2 A f(A), E={z: |I(z)|>G(z)}. For any fixed epsilon in (0,1], put

    C_epsilon={z in E: B(z)<epsilon max(B_1(z),B_2(z))}.

Theorem. If integral_{C_epsilon} dz/B(z)<infinity for some such epsilon, then X+Y satisfies (H). In particular, it suffices that B>=epsilon max(B_1,B_2) on E. It also suffices that (Im psi_1)(Im psi_2)>=0 almost everywhere. No inclusion of the sum-energy measures into either summand's energy class is assumed.

Proof. Independence supplies the sum exponent. Since A_i<=A and f is nondecreasing,

    |g_1+g_2| <= (A_1+A_2) f(A)
                  = (A+1) f(A) <= 2 A f(A)=G,

using A>=1. Define e=(|I|-G)_+ and h=sgn(I)e, where sgn(0)=0, and g=I-h. These are measurable. If |I|<=G, then h=0 and |g|=|I|<=G. If |I|>G, then g=sgn(I)G and |g|=G. Thus |g|<=A(2f)(A) globally.

The triangle inequality and I=(g_1+g_2)+(h_1+h_2) give |I|<=G+|h_1|+|h_2|. Taking the positive part gives

    e <= |h_1|+|h_2|.

Also e<=|I|<=B. Since e=0 outside E, it is enough to estimate its integral on E. On E minus C_epsilon, B>=epsilon B_i for both i. All denominators are positive because A_i,A>=1. Hence

    e/B^2 <= epsilon^(-2) (|h_1|/B_1^2+|h_2|/B_2^2).

Its integral there is finite by the two EKFR hypotheses. On C_epsilon,

    e/B^2 <= 1/B,

whose integral is finite by the extra cancellation-set assumption. Combining these estimates gives integral |h|/B^2 finite. The new good envelope 2f is nondecreasing and has the required divergent integral, exactly half that for f. Apply the verified EKFR theorem to the sum, using the expressly assumed resolvent densities. This proves (H).

For the same-sign corollary, let u=Im psi_1 and v=Im psi_2. If uv>=0, then

    (u+v)^2-u^2=v^2+2uv>=0,
    (u+v)^2-v^2=u^2+2uv>=0.

Also A>=A_i>=1, so B^2>=B_i^2 for both i. Consequently C_1 is empty up to a null set. Apply the theorem. Modifications on a frequency-null set do not affect the measurable integral criterion. End proof.

This is a stronger special-case deduction than the first attempt's common-Rao-envelope result: it permits nonzero integrable remainders and avoids arbitrary-measure energy transfer. No claim that it is new to the literature is made. The new condition is needed only where the sum fails the chosen pointwise envelope. Cancellation everywhere else is allowed without restriction.

### Referee audit of the theorem

* The f is genuinely common; Section 3 of ATTEMPT.md prevents merging unrelated f_i without proof.
* h_i are scalar functions, not Levy exponents. The proof never constructs processes from these pieces or assumes they are negative definite.
* All three density hypotheses are explicit. In applications, transition densities of one summand at every positive time are a sufficient way to give the sum densities, as proved in ATTEMPT.md Section 2.
* A_1+A_2=A+1, not A. The factor 2 is retained.
* The new remainder is the clipped excess of the TOTAL imaginary part, not h_1+h_2. It vanishes on the good region, which is why cancellation there needs no estimate.
* The denominators in the inherited remainder integrals are B_i^2. Transfer uses precisely B>=epsilon B_i on the complement of the exceptional set; it cannot be omitted.
* The exceptional-set estimate uses |h|<=|I|<=B. It requires the stated integral of 1/B, not a weaker unrelated energy condition.
* The EKFR criterion is sufficient and imposes more than (H). Nothing here establishes that arbitrary (H) summands have the decompositions assumed.


## Why the cancellation hypothesis cannot be erased by scalar inequalities

The following is a counterexample to closure of the FREE scalar EKFR conditions. It is explicitly not a pair of Levy exponents.

On R put Re psi_1=Re psi_2=0 and

    u_1(z)=z|z|, u_2(z)=-z|z|+z.

Then A_1=A_2=A=1. Choose g_1=g_2=0 and h_i=u_i, and use f=1. On a bounded interval |u_i|/(1+u_i^2)<=1/2, so each remainder integral is finite locally. For |z|>=2, |u_1|=z^2 and |u_2|=|z|(|z|-1)>=z^2/2, and hence

    |u_i|/(1+u_i^2) <= 1/|u_i| <= 2/z^2.

Thus both scalar EKFR remainder integrals over the whole line are finite.

But the sum imaginary part is I(z)=z. For any proposed finite-valued envelope F, its good term must have |g(z)|<=A F(A)=F(1)=M, a finite constant. If I=g+h, then |h(z)|>=|z|-M>=|z|/2 whenever |z|>=2M. For |z|>=max(1,2M),

    |h(z)|/(1+z^2) >= 1/(4|z|),

whose tail integral diverges. Thus the sum has no scalar EKFR decomposition at all. In the theorem's exceptional set, B=sqrt(1+z^2) but max B_i grows like z^2. Every C_epsilon includes a sufficiently distant tail outside E's threshold, and its integral of 1/B diverges. The hypothesis detects exactly this failure.

Why this is not a counterexample to E0027. A Levy exponent with real part identically zero can only be a deterministic drift exponent, hence has linear imaginary part. To see this directly from Levy-Khintchine, its Gaussian form and each integral of 1-cos<z,x> are nonnegative; vanishing real part for every rational frequency z forces Q=0 and forces the Levy measure to be supported on the intersection of the sets {x:<z,x> in 2 pi Z} over rational z. That intersection is {0}, excluded from a Levy measure. To justify the intersection statement, if x is nonzero choose rational z with 0<|<z,x>|<2 pi (rational vectors are dense and this defines a nonempty open set). A countable union of zero-measure complements then forces mu=0. The imaginary exponent is just its linear drift term. The functions z|z| and -z|z|+z do not have this form. Negative definiteness of genuine exponents is a missing structural input, not an assumption we may quietly omit.

This closes the attempted purely scalar proof of unconditional EKFR closure: the criterion's scalar hypotheses alone do not suffice. It does not prove that actual EKFR Levy processes fail closure, because actual exponents have substantially more structure.

## Route 2 comparison: a density-free Hellinger perturbation theorem

Here we use the source convention

    psi(z)=i<a,z>+ (1/2)<z,Qz>
            + integral [1-exp(i<z,x>)+i<z,x>1_{|x|<1}] mu(dx).

Let X have triplet (a,Q,mu) and satisfy (H). Let Y be an independent Levy process with triplet (a_Y,0,nu). Suppose nu=k mu for a finite nonnegative measurable density k (mu-almost everywhere),

    J=integral (sqrt(1+k)-1)^2 mu(dx)<infinity,
    a_Y + integral_{|x|<1} x nu(dx) belongs to range Q.

Then X+Y satisfies (H), with no resolvent-density hypothesis. This is a direct application of a published neighbouring result, not a solution to the general question and not a novelty claim.

Proof, including existence of the drift integral. Set t=sqrt(1+k)-1>=0, so k=t^2+2t. On {k<=1},

    k^2=t^2(sqrt(1+k)+1)^2 <= (sqrt(2)+1)^2 t^2 < 6t^2.

On {k>1}, divide by k and use sqrt(1+k)<=sqrt(2k) and 1<=sqrt(k) to obtain

    k <= (sqrt(2)+1)^2 t^2 < 6t^2.

Consequently integral_{k<=1} k^2 mu <=6J and integral_{k>1} k mu <=6J. The small-jump first absolute moment of nu is finite, because Cauchy-Schwarz gives

    integral_{|x|<1,k<=1} |x| k mu
       <= sqrt(integral_{|x|<1}|x|^2 mu)
          sqrt(integral_{k<=1}k^2 mu)<infinity,

and on {k>1,|x|<1} it is at most integral_{k>1}k mu. Thus the vector drift integral is absolutely defined. In particular Y has finite variation.

The sum triplet is (a+a_Y,Q,(1+k)mu). Its Gaussian covariance equals Q, its Levy measure is absolutely continuous with respect to mu with derivative K=1+k, its Hellinger integral is J, and the drift equation in Hu-Sun-Wang Theorem 4.5 is exactly

    (a+a_Y)-a+integral_{|x|<1}x[(1+k)mu-mu](dx)
       =a_Y+integral_{|x|<1}x nu(dx) in range Q.

That theorem gives local absolute continuity of the sum law with respect to X on every finite-time canonical sigma-field. Translation by any starting point preserves that assertion. Hu-Sun-Wang Theorem 1.1, or its direct Levy specialization Theorem 4.7, then transfers (H) from X to the sum. No one-time density argument is used. End proof.

Neither nu<<mu, J<infinity, Q_Y=0, nor the drift equation follows from (H) for Y. The theorem does not even require (H) for Y, so it supplies a special case of the question whenever Y also has (H).

### The route is quantitatively restrictive

If Y is an independent copy of an infinite-activity pure-jump X, then k=1 and J=(sqrt(2)-1)^2 mu(R^n\{0})=infinity. The absolute-continuity theorem does not apply even though the sum satisfies (H) by the constant-time-rescaling argument in ATTEMPT.md Section 7. If Y has a nonzero Gaussian covariance, Q changes and the local absolute-continuity criterion fails. These are genuine limits of this route, not failures of (H).

The Hellinger route also forces finite variation for the added jump component, as proved above. Thus it cannot treat a general unbounded-variation summand. This limitation is relevant to the original unrestricted gap.

### Relation to the old spectral domination result

Write nu_s=k 1_{k<=1} mu and nu_b=k 1_{k>1} mu. The latter is finite, so its zero-drift jump process is compound Poisson. For the former, define its zero-actual-drift exponent

    theta_s(z)=integral [1-exp(i<z,x>)] nu_s(dx).

It is absolutely defined by the first-moment estimate. Cauchy-Schwarz, first on finite truncations and then by convergence, gives

    |theta_s(z)|
      <= sqrt(integral_{k<=1}k^2 mu)
         sqrt(integral |1-exp(i<z,x>)|^2 mu)
      <= sqrt(12 J Re psi_X(z)).

Here |1-exp(iw)|^2=2(1-cos w), and the Gaussian part makes the real jump exponent no larger than Re psi_X. Since sqrt(r)<=1+r for r>=0, this is a constant times 1+Re psi_X.

The actual drift of Y, in finite-variation notation, is

    d_Y=-a_Y-integral_{|x|<1}x nu(dx),

which belongs to range Q by the drift equation. If Q is zero this drift is zero. If Q is nonzero, choose v with d_Y=Q^(1/2)v; Cauchy-Schwarz yields

    |<d_Y,z>| <= |v| sqrt(<z,Qz>)
                 <= |v| sqrt(2 Re psi_X(z)).

Therefore Y splits into a compound Poisson process plus a perturbation whose complete exponent is bounded by a constant times 1+Re psi_X. This explains why, WHEN the relevant densities are available, this case can also be handled by the previous domination theorem and compound-Poisson stability. The Hellinger theorem's distinct advantage here is dispensing with density assumptions, not overcoming an unrestricted spectral gap.


### An infinite-activity example under the density-free theorem

The Hellinger theorem is not confined to compound-Poisson Y. On R^2 let mu be supported on the first coordinate line, with density |x_1|^(-1-4/5) for 0<|x_1|<1, symmetric in x_1, and zero elsewhere. Let X have triplet (0,0,mu). On its invariant line it has bounded continuous transition densities: its real exponent has a lower bound c|z_1|^(4/5) for large |z_1|, obtained by integrating 1-cos(z_1 x_1) over x_1 between 1/|z_1| and 2/|z_1|; the integrand is bounded below by a positive constant there. Its imaginary exponent vanishes by symmetry, so Kanda-Forst gives (H) on each invariant line, and the invariant-coset argument in ATTEMPT.md Section 8 gives (H) on R^2. It has no resolvent densities with respect to two-dimensional Lebesgue measure, since every law and resolvent from a fixed starting point is concentrated on one line.

Set k(x_1,0)=|x_1|^(1/2), and nu=k mu. Then nu has density |x_1|^(-1-3/10), so it has infinite total mass and finite small-jump first moment. It is itself symmetric truncated-stable on the line; the same argument with exponent 3/10 proves (H) for Y with triplet (0,0,nu). Since (sqrt(1+k)-1)^2<=k^2/4 and

    integral_{0<|x_1|<1} k^2 mu
       =2 integral_0^1 x_1^(-4/5) dx_1=10,

J<=5/2 is finite. The vector drift integral is zero by symmetry and absolute integrability; the range-Q condition holds since Q=0. The Hellinger theorem therefore proves (H) for X+Y without ambient resolvent densities. This example is already benign by symmetry on its invariant line; it checks the hypotheses and confirms that infinite activity of Y is allowed, but does not exhibit a new difficult case or solve the unrestricted question.


## Final hostile-referee conclusions and remaining gap

The selected route proves a conditional EKFR stability theorem without relying on finite-energy inclusion. It succeeds under either a denominator lower bound only on frequencies where the sum exceeds its good envelope, or the weaker integrable exceptional-set condition. Same-sign imaginary exponents imply that condition automatically. This is a substantive special case with nonzero integrable remainders allowed.

The attempted unconditional extension fails at a precise point: there is no demonstrated estimate of

    integral_{C_epsilon} dz / |1+psi_1(z)+psi_2(z)|

from the two individual EKFR remainder integrals. The free scalar model proves that no argument using only the scalar decomposition bounds can supply it in general. Whether genuine negative-definite Levy exponents enforce enough extra cancellation control remains unproved here. Even solving that EKFR closure question would not settle E0027, since arbitrary (H) processes need not satisfy the global EKFR sufficient condition.

The second route supplies a density-free special case through a published change-of-measure theorem. It cannot cover arbitrary additions: the Gaussian covariance cannot change, the new Levy measure must be absolutely continuous relative to the old one with a finite Hellinger integral, and the added process is forced to have finite variation. Even independent copies of many infinite-activity (H) processes fall outside this path-law criterion, despite having an (H) sum.

Thus neither route proves the original implication or constructs a counterexample with both summands satisfying (H). The actual open gap remains: for arbitrary independent finite-dimensional Levy (H) processes, show every semipolar set for the sum is polar, or produce a semipolar nonpolar set. The first attempt's finite-energy counterexample is not undone by the new result; the new theorem avoids its premise rather than restoring the false energy lemma.

Reproduction checks are saved in second_exact_checks.py and second_checks.json. Six thousand exact rational tuples test clipping, good-region bounds, no-cancellation denominator comparison, and exceptional/complement estimates. Three thousand rational t values test the Hellinger split with k=t^2+2t. Every assertion passed. The free scalar model's clipped remainder integral over [-R,R], R>=2, is exactly

    log((1+R^2)/5)-4(atan R-atan 2),

which diverges. Its recorded values at R=10,100,1000,10000 are approximately 1.54977,5.78641,10.35548,14.95705. These are evaluations of an exact antiderivative, not a fit. All computations used small arrays or rational scalar arithmetic. A read-only process check reported a Lean process with a working set of about 92 MB. This shared machine also has other Lean jobs, so this is an observed sample, not a certificate of this job's peak usage. No large numerical experiment was run.

Lean verification of SecondScalarChecks.lean is recorded separately in second_lean_check.log when complete. Only the scalar comparisons are formalized, not the EKFR theorem, the local-absolute-continuity theorem, or the entire probability proof.


### A sharpened hypothesis in Route 1

The analytic proof of the cancellation-split theorem only uses resolvent densities for the SUM. The individual density assumptions were included to ensure each summand is known to satisfy (H) via EKFR. If (H) for the individual processes is already given as in E0027, those individual density assumptions may be dropped: it is enough to assume the two written scalar decompositions, the common envelope, the exceptional-set condition, and resolvent densities for the sum. No line of the proof uses a summand's energy criterion or a summand's resolvent density. The definition of the published EKFR class normally includes its density hypothesis, so this sharpening is stated separately rather than silently changing that terminology.


### Complete exponent bound for the Hellinger route

In fact the finite-measure part has a globally bounded exponent: |theta_b(z)|<=2 nu_b(R^n\{0}). Combining it with the two bounds already proved gives

    |psi_Y(z)| <= 2 nu_b(R^n\{0})
                 +(sqrt(12J)+sqrt(2)|v|) sqrt(Re psi_X(z)),

where v=0 if Q=0 and otherwise d_Y=Q^(1/2)v. Thus the COMPLETE added exponent is bounded by C(1+Re psi_X), for some finite C. No intermediate-density inference or removal of the compound-Poisson part is needed to identify the overlap with the old dominated-perturbation theorem. This strengthens the route comparison: its density-free conclusion is the extra feature; in the setting with the required densities, its hypotheses imply the old spectral domination condition outright.


Formal-check audit: the first renewed Lean run returned exit 1 because abs_add was not the library name of the triangle inequality. Its output is retained in second_lean_first_failure.log and is NOT a checked proof. The denominator and Hellinger statements had no sorryAx, but the clipping statement was unverified on that run. The corrected source uses abs_add_le and is being rechecked in full.


Another direct corollary of Route 1: it is sufficient that the excessive-cancellation set C_epsilon have finite Lebesgue measure, since B>=A>=1 gives integral_{C_epsilon}1/B <= Lebesgue(C_epsilon). In particular, a denominator comparison that holds on E outside a bounded frequency region suffices; no uniform comparison on that bounded region is required. This follows from the written theorem and introduces no new assumption about individual energy measures.


Final formal check: the corrected SecondScalarChecks.lean compiled successfully. All three printed axiom lists contain only propext, Classical.choice, and Quot.sound; none contains sorryAx. See second_lean_check.log. The failed run is retained separately and is not counted as verification. The only formal correction was a theorem-name reference; the mathematical inequalities did not change.

Final verdict for the user-requested second attempt: PARTIAL. The cancellation-split special case and density-free Hellinger special case are proved as deductions from explicitly verified published inputs. The unrestricted independent-sum problem has neither a proof nor a counterexample here. STATE is DONE for this attempt, with the gap stated above.

# Independent audit: arbitrary independent Bernoulli padding

1 October 2026. Natural logarithms unless a base is stated. Local follow-on audit; the previously published fair-padding package is frozen and unchanged. No additional remote write is authorized by this report. No correlated-padding theorem, Boolean realization, full derivative-lattice sufficiency, FEI solution, or novelty claim is made.

## Verdict

The product-padding extension is correct, including the unchanged signed functional when some padding bits survive initial forcing. The proof requires the explicit no-click product update and original-time coupling below.

There is one necessary wording correction. Fair bits are optimal for logarithmic cap repair per expected occupied padding coordinate. Minimum integer-rounded all-fair padding need not minimize total energy for a prescribed non-power-of-two cap threshold. For d=2,Q=5, probabilities (1/2,1/2,5/16) meet all caps with padding energy 21/16, below the three-fair-bit cost 3/2. This does not weaken the proposed energy lower bound or the uniform family-specific signed bound.

## 1. Setup and the exact cap factor

Let P be the d-block cyclic one-hot law with integers d>=2,Q>=4, original atom mass w=Q^(-(d-1)), and J(P)=d. Write

    M=Q^(d-1)/4^(d-2).

On a disjoint finite coordinate set, let B be any independent Bernoulli law with inclusion probabilities t_1,...,t_r in [0,1]. Endpoints are allowed and must be treated explicitly. Set Pprime=P tensor B. The original part is never empty, so the separate abstract indicator-normalized law

    q(empty)=1/2,
    q(T)=Pprime(T)/2 for nonempty T,
    p=1/2

is normalized. Its atom-cap family is q(T)<=4^|A|p theta_q(A)^2 for every A subset T. This cap law q is distinct from the law Pprime used in the signed functional.

For a supported T=S union U and nonempty A=A_orig union C, let a=|A_orig| and b=|C|. The original upward marginal is t_a=Q^(-a) for a<d and t_d=w. Direct substitution gives

    cap ratio = [w/(4^(a-1)t_a^2)]
                [B(U)/(4^b theta_B(C)^2)].          (1)

Here theta_B(C)>0 because C subset U and B(U)>0. There is no division by zero on a supported atom. The original factor is at most M, with equality at a=d-1. The a=0,b>0 factor is 4w<=M; a=d gives M/4. The a=d-1 choice is always available and makes A nonempty, regardless of C.

Define

    K(B)=max_(U supported, C subset U)
              B(U)/(4^|C|theta_B(C)^2).             (2)

Thus the maximum ratio over nonempty A and supported T is exactly M K(B), not merely bounded by it. Adding the empty cases gives global maximum max(1,M K(B)): T=A=empty is equality, A=empty on a nonempty T is automatic, and zero-mass T are automatic by nonnegativity. Consequently all caps hold if and only if

    M K(B)<=1.                                     (3)

## 2. Compute K for product padding, including endpoints

Each coordinate can be outside U, in U but outside C, or in C. For 0<t<1, its respective factors in (2) are

    1-t,   t,   1/(4t).

Every collection of these choices defines a supported atom and an allowed subset, so maximization separates coordinate by coordinate. Since 4t(1-t)<=1, the first candidate never exceeds the third. Therefore

    K(B)=product_j k(t_j),
    k(t)=max(t,1/(4t)) for 0<t<1,
    k(0)=k(1)=1.                                  (4)

At t=0, only the outside-U choice is supported and has factor 1. At t=1, outside U is impossible; the two supported choices have factors 1 and 1/4, so the maximum is 1. Taking a divergent t->0 limit instead of checking the exact zero endpoint would be incorrect.

One concrete maximizing choice is U={j:t_j>0} and C={j:0<t_j<=1/2}, together with any d-1 original coordinates for A_orig. Thus every failure of (3) has an explicit supported cap witness.

## 3. Sharp logarithmic-efficiency bound and its equality cases

For every t in [0,1],

    -ln k(t) <= 2 ln(2) t,                         (5)

with equality exactly at t=0 or t=1/2.

At t=0, both sides vanish. At t=1, the inequality is strict. For 0<t<=1/4, k(t)>=1, so the left side is nonpositive and the right side is positive. For 1/4<t<=1/2, k(t)=1/(4t). The function ln(4t)-2 ln(2)t has derivative 1/t-2 ln(2)>0 throughout this interval and equals zero at 1/2. It is therefore negative below 1/2. For 1/2<=t<1, k(t)=t; the function -ln t-2 ln(2)t has strictly negative derivative -1/t-2 ln(2) and vanishes at 1/2. This proves (5) with the stated equality cases.

Combining (3)-(5) gives

    ln M <= -ln K(B)
         = sum_j [-ln k(t_j)]
         <= 2 ln(2) sum_j t_j,

and hence

    Jprime=d+sum_j t_j
          >=d+(1/2)log_2 M
          =2+(d-1)log_2 Q/2.                     (6)

Equality in the final lower bound requires all nonzero padding probabilities to be 1/2 and M to be an integer power of two, with precisely log_2 M fair coordinates. These conditions are also sufficient. The constant in (5) is sharp.

This is an efficiency statement, not an exact optimizer classification at every M. For d=2,Q=5, M=5. Three fair bits have K=1/8 and energy 3/2. In contrast,

    (t_1,t_2,t_3)=(1/2,1/2,5/16),
    K=(1/2)(1/2)(4/5)=1/5,
    sum_j t_j=21/16<3/2.

The mixed choice saturates the cap threshold but does not attain the real-valued energy lower bound (6). No exact optimizer for non-power-of-two M is claimed.

## 4. Posterior factorization under the original occupied clocks

Assume 0<epsilon<=exp(-2). The process uses independent original rate-one clocks on occupied coordinates and the unchanged threshold epsilon exp(-2t), with complete instantaneous forced cascades. Original time is never reset. Take the same fixed order on original coordinates in the padded and unpadded processes; padding coordinates can occur anywhere in the extended fixed order.

We prove factorization of the actual posterior, not just independence at time zero. Given a complete pre-event record, suppose the remaining law has the form

    mu(original coordinates) tensor product_j Bernoulli(q_j).

This holds initially. There are three elementary Bayesian updates.

**No ordinary click during an interval of length h.** Conditional on a remaining occupied set Z, its no-click likelihood is exp(-h|Z|). This remains true for the original clocks because, conditional on survival to the interval start, occupied exponential clocks have the same residual survival probability exp(-h). The likelihood factors over the original set and each padding coordinate. Thus the updated original law is proportional to mu(S)exp(-h|S|), and every still-active padding probability becomes

    q_j' = q_j exp(-h)/(1-q_j+q_j exp(-h)).        (7)

The updated joint law is still a product between the original block and the individual padding coordinates.

**An ordinary click at coordinate i.** After the no-click likelihood up to that time has been applied, its event-density factor is the occupancy indicator of i, times the common unit rate. Thus the posterior conditions on i being one and removes it. This modifies only the factor containing i. Event times and identities introduce no extra cross-factor term.

**A forced reveal at coordinate i.** Conditioning on the observed zero or one and removing that coordinate also modifies only its own factor. Padding answers preserve the original law, and original answers preserve the padding factors.

Eligibility times and the choice of the next forced coordinate are determined by the known posterior, the original time, and the preceding record. Between events the no-click posterior is deterministic given the record. A threshold-triggered endpoint therefore introduces no further latent-state likelihood beyond the no-click update already accounted for. Completion of a forced cascade likewise adds no likelihood beyond its recorded answers. Induction over ordinary events and forced queries proves posterior factorization throughout the actual process.

For an active padding bit that has never clicked or been queried, (7) telescopes to the explicit absolute-time formula

    q_j(t)=t_j exp(-t)/(1-t_j+t_j exp(-t)).        (8)

No original query or other padding observation changes (8). When t_j=0 it remains deterministic zero. When t_j=1 it is eligible and forced at time zero. If 0<t_j<1 and the bit is not already forced or clicked, q_j(t)/(epsilon exp(-2t)) is strictly increasing and tends to infinity. Hence any such surviving bit reaches eligibility at a finite time. There are finitely many coordinates, and every click or query removes one, so cascades are finite.

## 5. Pathwise coupling of the original process

Couple the padded and unpadded processes using identical original source labels and identical original occupied clocks. The product posterior invariant implies that an original-coordinate marginal is precisely its marginal under mu. A padding observation leaves mu unchanged. Splitting a no-original-click interval at extra padding event times does not change the original update: the tilts by exp(-h|S|) compose by adding elapsed time.

During a fixed-time complete cascade, deleting padding queries from the transcript leaves the same ordered original queries and original answers as in the unpadded process. Padding queries do not change original eligibility. The cascade cannot stop while an original coordinate is eligible, and only finitely many padding queries can intervene. Therefore the original queries occur at the same original time and in the same original-coordinate order. Simultaneous threshold triggers cause no problem; ordinary clock ties have probability zero.

It follows that the remaining original posterior and original query transcript agree pathwise at every positive time, under the common post-complete-cascade convention. This argument includes padding bits that are not forced at time zero and may click or be forced before or after the original cyclic process resolves.

For completeness, the two terms of the signed functional both respect this coupling. With

    Gamma(mu)=sum_i Ent_(mu_without_i)(1-r_i),
    r_i=Pr(bit i=1 | all other remaining coordinates),

a padding coordinate has constant conditional probability q_j, so its entropy term is exactly zero. For an original coordinate, the conditional probability is the original r_i and does not depend on padding. Integrating the unused independent padding factor leaves its entropy term unchanged. Hence

    Gamma(mu tensor product padding)=Gamma(mu).   (9)

At a padding forced query, I(padding bit;rest | pre-query record)=0. At an original forced query, independence gives

    I(original bit;original rest,padding | record)
      =I(original bit;original rest | record).     (10)

The original query times and their exp(time) weights coincide in the coupling. Equations (9)-(10) therefore identify the entire continuous integral and every nonzero refund pathwise. Thus

    R_epsilon(Pprime)=R_epsilon(P).               (11)

For this cyclic family, finiteness follows from the original finite-lifetime proof. Padding adds identically zero continuous Gamma cost and zero forced refunds; no subtraction of infinities is used. Equation (11) makes no assertion about the separate indicator-normalized mixture q.

## 6. Uniform signed guard for all independent padding

Assume 0<epsilon<=exp(-2). When epsilon Q>1, the archived cyclic process resolves by T=(1/2)ln(epsilon Q). Its weighted continuous integrand is at most d c_Q, with c_Q<=1, and its refunds are nonnegative. Consequently

    R_epsilon(P)<=(d/2)ln(epsilon Q).

If all caps hold, (6) and (11) give

    R_epsilon(Pprime)/Jprime
      <=d ln(epsilon Q)/[4+(d-1)log_2 Q]
      <=[d/(d-1)]ln 2
      <=2 ln 2.                                  (12)

When epsilon Q<=1, every unresolved original block has one occupied coordinate among at most Q remaining candidates. Their conditional marginals sum to one, so some original coordinate is >=1/Q>=epsilon. The complete initial cascade therefore resolves all original blocks at time zero. Padding queries may interleave, but do not affect this argument or their original law. Original refunds are nonnegative, and original Gamma vanishes at all positive times. Independent padding can remain afterward, but (9)-(10) show that its signed contribution is zero. Hence R_epsilon(Pprime)<=0 in this regime as well.

Thus every member of this cyclic family repaired by arbitrary finite independent Bernoulli padding satisfies R_epsilon(Pprime)<=2 ln(2)Jprime. The result rules out restoring the earlier divergent ratio by changing independent padding biases, their number, or Q. It does not rule out correlated padding or another cap-satisfying law.

For Q=d^6, (6) also gives Jprime>=3(d-1)log_2 d+2. The known numerator remains d[H_(d-1)-O_epsilon(log d/d^2)] by (11). Consequently every full-cap product-padding sequence has limsup R_epsilon(Pprime)/Jprime<=ln(2)/3. Minimum all-fair padding attains this asymptotic constant. Biased padding can improve finite rounding costs without increasing that asymptotic limsup.

## 7. Exact bounded verification and provenance

The independent standard-library checker constructs padding and complete cap laws directly, computes upward marginals by enumerating supported atoms, and compares exact rational ratios with (3)-(4). For rational t=a/b, it verifies (5) without logarithms by testing k(t)^b 4^a>=1, including the exact equality cases. It checks the explicit mixed-bias rounding counterexample.

The Bayesian checks compare direct full-law survival tilting, forced zero/one observations, and ordinary-click one observations against separately updated factors. Exact conditional-probability identities also check padding independence and preservation of original conditional information. These are Bayesian-operation checks, not a substitute for the analytic policy proof.

A separate complete-forcing test follows an actual positive-probability path conditioned on no ordinary clicks, with epsilon=1/8, d=2,Q=32, and padding biases (1/2,12/131,4/131). The fair bit is forced at zero, the second reaches its threshold at exp(-time)=3/4, the original law is fully forced at exp(-time)=1/2, and the last padding bit remains until exp(-time)=1/4. All answer branches are enumerated in original-first and padding-first orders. This explicitly covers padding forcing before and after original resolution.

The checker passed 403 padding-factor laws, 67 full cap laws (47,443 cap ratios), 2,144 exact one-bit efficiency tests, 24 no-click factorization identities, 472 observation factorization identities, and 9,120 original conditional-information identities. The complete-forcing path check has 512 terminal answer branches across two orders. See check_results.json for all counts. Universal claims rest on Sections 1-6; bounded computation does not establish them by extrapolation.

Sources read locally: the frozen cyclic signed-lifetime REPORT.md and its checker; the polynomial-alphabet audit; the reviewed fair-padding AUDIT.md; and the root's PRODUCT_PADDING_CANDIDATE.md. The candidate remains historical input, with the optimization-language correction recorded here. The frozen fair-padding archive is commit 1fe4d53611f83d69f913003d186c2b14e2458d16, reviewed audit blob 0dfcf64a55426a1efda4bd87a3aa50d2176f9d52. This follow-on made no remote changes. Source and artifact hashes are recorded separately.


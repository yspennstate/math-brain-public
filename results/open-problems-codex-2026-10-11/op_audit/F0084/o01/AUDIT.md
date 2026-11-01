VERDICT: PASS

Independent audit of F0084, 12 October 2026.

The claimant's SOLVED_IN_LITERATURE verdict is correct for the explicitly requested quantitative upper bound. No substantive error or required repair was found. This verdict does not certify a sharp tail asymptotic or an optimal exponent.

## Exact claim and scope

ATTEMPT.md, lines 3–11, claims that for a homogeneous Poisson process of intensity 1 in R^d, with constant appetite 1 and the Euclidean stable allocation, the site's distance X from the origin satisfies

    For every integer d >= 2 there exist C(d) < infinity and s(d) > 0
    such that P(X > r) <= C(d) r^(-s(d)) for every r > 0.

This answers the source's request for “any quantitative upper bound for d >= 2.” It concerns the stable allocation, not an arbitrary optimal allocation, and the typical site's distance, not the maximum radius of a typical centre's territory. Constants may depend on dimension. It is not restricted to dimension one, a noncritical appetite, or large appetites. ATTEMPT.md explicitly excludes determination of the sharp tail from its claim.

CLAIMS.jsonl also asserts the weaker explicit bound

    P(X > r) <= K_d r^(-1/(4d)),
    K_d = max(1, 21*2^(d/2)/(10*sqrt(v_d))),

where v_d is the volume of the unit ball. I independently checked the prose proof of this additional claim in SOLUTION.md, sections 1–4.

## Independent primary-source verification

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md directly from the claimant's folder, without modifying it. I additionally read SOLUTION.md. I fetched fresh copies of the original source, the cited arXiv paper, and the published journal paper using Python requests. All three returned HTTP 200. Crossref independently confirmed the title, DOI, volume and pages. Retrieval URLs and outcomes are in retrieval_log.json; the PDFs and extracted text are retained in this audit folder.

The decisive reference is Alexander E. Holroyd, Robin Pemantle, Yuval Peres and Oded Schramm, *Poisson Matching*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 45 (2009), 266–287, DOI 10.1214/08-AIHP170, arXiv:0712.1867.

* Printed p.269, journal PDF p.4: Theorem 6(ii) gives P*(X>r) <= C r^(-s) for all r>0, with s=s(d) in (0,1) and C=C(d) in (0,infinity).
* Printed p.270, journal PDF p.5: the authors explicitly say that the two-colour results in Theorems 1, 2 and 6 extend to “Fair allocations of Lebesgue measure to a Poisson process.” They specify: “Here X denotes the distance from the origin to its allocated Poisson point.” They then explicitly identify “the resulting upper bounds on the stable allocation in Theorem 6(ii)” and contrast them with the previously absent quantitative upper bound in d>=2. This is a direct statement about the requested model, not an inferred analogy.
* Printed p.286, journal PDF p.21: the proof-adaptation remark replaces counts of long matched points by Lebesgue volumes of long allocated sites and long portions of centre territories. Mass transport gives equal expectations. This supplies the critical bridge from point matching to allocation.
* Printed pp.283–286: Theorem 19 and its proof supply the positive exponent and the integral argument. The allocation adaptation agrees with the weighted-flow proof inspected below. Theorem 19 defines the sharper exponent by equation (21); the stated values s(2) approximately 0.496 and s(3) approximately 0.449 agree with the claimant's quotation.

The arXiv copy independently contains the allocation adaptation on PDF p.34. The original HHP source, PDF p.31, contains exactly the quoted open question. Its p.6 defines X as the origin's allocation distance; p.5, Theorems 3 and 4(ii), supplies the equivariant allocation, full claimedness and satedness at criticality. Thus fair allocation at unit Poisson intensity means volume-one territories, precisely appetite 1. Lebesgue source intensity is 1 and its stationary Palm law is the ordinary law at a deterministic site. The centre Palm maximum-radius distribution is not being substituted for X.

I also repeated a bounded arXiv API search for stable marriage and Poisson. It returned *Poisson Matching*, the original paper and related tail/percolation papers. Search output is saved in search_arxiv.txt. Positive identification of the exact published extension establishes this verdict; an exhaustive search or a negative literature-status inference is unnecessary. This search does not establish that sharp asymptotics are still open as of today.

## Independent mathematical checks

The additional proof in SOLUTION.md is complete for its weaker bound:

1. Summing the nonnegative transport of distance>t site mass between unit cubes gives equality of expected sent and received mass. Campbell–Palm at centre intensity 1 then gives E^0 T_t(0)=P(X>t), where T_t is territory volume beyond distance t. Applying Campbell–Palm with deterministic spatial thresholds justifies the radial integrals. No equality of site distance and centre maximum-radius laws is used.
2. For B=B(0,R), positive site mass A assigned beyond R+|x| and positive centre territory mass D beyond R+|xi| cannot coexist. Choosing x and xi in B gives both strict preferences, because |x-xi|<R+|x| and |x-xi|<R+|xi|. A far territory point witnesses that xi covets x. Stability prohibits this blocking pair.
3. Writing H for internal allocated mass, Q_out=volume(B)-H and Q_in=N(B)-H follow from critical claimedness and unit satedness. Consequently Q_out-Q_in=Z=volume(B)-N(B). The two exclusion branches give A+D<=Q_in+Z_+. This is valid pathwise and uses no independence assumption.
4. Expected A and D both equal integral_B p(R+|y|)dy. Outside territory mass is bounded by T_(R-|xi|)(xi). Since N(B) is Poisson with mean V=v_d R^d, E Z_+<=sqrt(V). Dividing the resulting inequality by 2V gives

       p(2R) <= (1/2) E p(RW) + R^(-d/2)/(2 sqrt(v_d)),

   where W has density d(1-w)^(d-1), 0<w<1. Boundary sets have zero relevant measure.
5. With s=1/(4d), Bernoulli's inequality gives W>=U/d in a quantile coupling, so E W^(-s)<=d^s/(1-s). Therefore a=2^(s-1)E W^(-s)<=16/21<1. The estimates log(2d)<=d, exp(1/4)<=4/3 and s<=1/8 are valid for all d>=2.
6. F(L)=sup_(0<t<=L) t^s p(t) is finite on bounded intervals. The recurrence involves F(r/2), not F(r); induction over dyadic intervals is noncircular. The error term is B_d r^(s-d/2), with B_d=2^(d/2)/(2 sqrt(v_d)). For r>=1 it is at most B_d, and K>=21 B_d/5 closes the induction. For r<=1, p(r)<=1<=K r^(-s). The constant and all-r quantifier are correct.

As an independent numerical diagnostic I evaluated the exact beta-integral formula E W^(-s)=Gamma(d+1)Gamma(1-s)/Gamma(d+1-s), and checked the contraction and K inequalities at d=2,3,4,10,50,100. Contractions were respectively 0.664690, 0.620244, 0.596464, 0.547658, 0.513161, 0.507408, all below the asserted analytic bounds. Results are in independent_numeric_checks.json. These calculations supplement the all-dimensional analytic argument; they do not replace it.

## Issues and limitations by ATTEMPT.md location

* Lines 5 and 9: “resolved” must be read with the explicitly stated upper-bound scope. The paper and the independent proof do not determine sharp asymptotics. The claimant already states that limitation; no fix is needed.
* Line 11: the intake's Section 12 locator is inaccurate. The fresh original PDF places the question after Section 9 on p.31, as the claimant correctly reports. Theorem 32 is the site-distance moment divergence; Theorem 33 is the distinct centre-radius assertion. No site/centre confusion survives in the final claim.
* Lines 13–49 and 85: the historical nearcritical comparison alone supplies no quantitative critical rate. I verified the direction of Proposition 22(i) in the fresh source, the Campbell–Palm missing mass 1-beta, and the Markov split. Substitution delta=r^(-d/(2b)) gives the displayed conditional powers correctly. The needed uniform estimates are not proved, and are explicitly labelled unproved. They are not used in the successful argument.
* Lines 51–63: the quantile truncation example is an abstract counterexample to a proposed inference, not to stable Poisson allocation. Its monotonicity, missing mass and finite truncated exponential moments follow directly from its construction. It does not undermine the published upper bound.
* Lines 65–79: the small-radius identity follows from stability and the volume-one obstruction, and the zero-probability sphere event handles the endpoint. Its saturating upper bound is not a large-distance solution; the claimant explicitly says so.
* Lines 87 onward and the corresponding CLAIMS.jsonl records: finite simulation and Lean reports do not prove the continuum tail theorem. I did not rerun the claimant's simulations or Lean sessions and do not independently certify their execution histories. The decisive literature statement and the re-derived continuum proof do not rely on those reports.

There is no required correction to the claimed literature resolution. What is established is a dimension-dependent polynomial upper bound for the exact critical stable site's allocation distance in every d>=2, including a valid weaker bound with the explicit constant above. Sharp tail behavior and optimal exponents are not established by this audit.

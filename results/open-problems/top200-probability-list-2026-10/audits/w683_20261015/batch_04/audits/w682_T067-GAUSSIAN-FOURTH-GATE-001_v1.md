# T067-GAUSSIAN-FOURTH-GATE-001 v1: PASS

Exact proof SHA256: `b1e094fac2ee638d88414611f9c3abdadd99a4d673799f71ecda263072d30637`. Kind: audit; target: T067 regular q3 finite-degree range.

I read the complete curvature, quadrature and interpolation proof. The displayed two-normal logit map has mean(3s,-3s/2,-3s/2), covariance(9s/2)P, and squared operator norm9s/2. Its posterior components yield exactly the displayed F1 and radial Q formulas. Radial Q has the same conditional and unconditional expectation by permutation symmetry. Q lies in[0,36].

Using an orthonormal basis of the zero-sum plane, fourth-derivative polarization bounds an orthogonal mixed fourth entry by the diagonal constant c4, hence |Delta_P^2 f|<=4c4. The drift norm squared is27/2 and its norm is less than15/4. Thus the second signal derivative is bounded by(27/2)c2+(135/4)c31+(81/4)c4. This gives1269/40<32 for F1 and14229/4<3600 for Q, using independently audited derivative constants. The heat-semigroup differentiations and Gaussian integrations by parts are legitimate on s>=1/10: observables and requisite derivatives are bounded. No radial Hessian sign is assumed.

I independently rebuilt every truncated normal bin using erf/exp, masses, conditional means and unnormalised variances, at192-bit outward-rounded Arb precision. The first Taylor term vanishes at each bin mean. Hessian bounds give errors(9s/10)P0D0 and90sP0D0; omitted-square tails are bounded by1-P0^2 and36(1-P0^2). Both errors and tails are included before extracting directed rational endpoints. No integral or tail is ignored.

Original width1/8 certificate: I recomputed both observables at all86 endpoints on the full signed96-by96 grid, using sign symmetry only to combine equal contributions. Every own raw quadrature interval is contained in its pinned submitted interval. All86 file hashes match the report. Own exact constants match alpha,B and curvature. Exact rational interpolation margins on all85 intervals have minimum about0.2656448551>0. Receipt checks/t067_gaussian_gate96_own.json; no original arithmetic helper or source was imported.

Independent refined width1/16 calculation for degree91: I reused my already verified86 second-observable upper endpoints and computed the new fourth observable on the signed192-by192 grid at192 bits. Its exact continuous interval margins have minimum about0.01584522509633951>3/200. All rounding is accounted for by directed Arb endpoints and exact rational final arithmetic. Reusing the existing second-observable receipt is bound by SHA256. Receipt checks/t067_compensated_gaussian_own.json. Increasing every fourth-observable upper bound by1 subtracts1 from every gate margin and fails the declared threshold, as checked exactly.

The interpolation inequality is the lower endpoint chord minus C(s-a)(b-s)/2; the minimum is bounded by min(endpoint lower values)-C(b-a)^2/8. The rational grid has86 increasing endpoints from1/10 to2/3 and85 adjacent intervals without gaps. Positivity is certified on each entire closed interval, not inferred from endpoint samples. The degree100 theorem uses only its original positive gate; the refined degree91 gate is separately bound in the composition audit.

## Verdict and limits

PASS for this exact statement and its explicitly scoped dependencies. The underlying Gaussian method is Sly arXiv0811.1208, Eq4.7 and Lemma4.3, and Mossel-Sly-Sohn arXiv2212.03362, AppendixA; primary PDFs were previously fetched and checked in this audit sequence. The present constants and finite certificates were checked independently. Priority remains unverified: the bounded recent arXiv screen found a growing-alphabet robust-reconstruction paper, not a fixed-q3 finite-degree nonreconstruction result. No novelty claim is made.

This is a w683 mathematical audit, not an admission decision. The required independent exact-content review on another account and authorized recording remain necessary. An agreeing same-account lead check does not replace that gate.

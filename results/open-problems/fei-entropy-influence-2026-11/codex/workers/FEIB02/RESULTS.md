# FEIB02 results

Logs are base 2; A, B, Gamma and P are measured in bits, I in total influence. Ratios have units bits per unit influence. A value vector lists f_0 through f_n; + means +1. A mask fixes f_0=+1 and has bit t-1 set exactly when f_t=-1. Global negation preserves the results.

## Exhaustive symmetric census

Every one of the 2^(n+1) value vectors is covered through its global-sign representative. Constants are excluded from ratios. A dash denotes no balanced function with I>1. A separate integer interval census encloses every possible maximizer. Their exact logarithm expressions prove all remaining ties, and fixed-point positive-series bounds certify each supremum to 100 decimal places. Values below are rounded to ten decimal places. See extrema.csv for all objective values and value vectors, and suprema_certified.json for certified values and ties up to global sign.

| n | A/I | B/I | Gamma/I | balanced A/(I-1) | balanced B/(I-1) | balanced Gamma/(I-1) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.0000000000 | 0.0000000000 | 0.0000000000 | — | — | — |
| 2 | 1.0000000000 | 1.0000000000 | 0.2500000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 3 | 1.5833333333 | 1.3725562489 | 0.3197159723 | 2.5000000000 | 1.5000000000 | 0.0000000000 |
| 4 | 1.9375000000 | 1.4649755512 | 0.3750000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 5 | 2.1625000000 | 1.4612403997 | 0.5375056054 | 2.0701443126 | 1.7302851503 | 0.2830290180 |
| 6 | 2.3125000000 | 1.6395797732 | 0.5027543238 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 7 | 2.4174107143 | 1.6793637379 | 0.6240761636 | 1.8153188966 | 1.8663546627 | 0.5744833945 |
| 8 | 2.4941406250 | 1.7045733813 | 0.6032569566 | 1.2236904265 | 1.6832569953 | 0.7627620755 |
| 9 | 2.5525173611 | 1.7947092066 | 0.7124328611 | 1.6440193180 | 1.9565113706 | 0.7332415577 |
| 10 | 2.5984375000 | 1.8043441328 | 0.6913867472 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 11 | 2.6355646307 | 1.8442028543 | 0.7555557296 | 1.5188047829 | 2.0216917316 | 0.8207568133 |
| 12 | 2.6662597656 | 1.8924326888 | 0.7468909213 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 13 | 2.6921011118 | 1.8920507592 | 0.7915241582 | 1.4219686692 | 2.0717470758 | 0.8773900011 |
| 14 | 2.7141810826 | 1.9373920282 | 0.7936093936 | 1.1115922329 | 1.2939916937 | 0.6119346830 |
| 15 | 2.7332804362 | 1.9572617041 | 0.8186990843 | 1.3440477914 | 2.1118586424 | 0.9097639195 |
| 16 | 2.7499732971 | 1.9652300725 | 0.8301189693 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 17 | 2.7646924187 | 2.0026046689 | 0.8461492353 | 1.2794874027 | 2.1450200309 | 0.9360347092 |
| 18 | 2.7777709961 | 2.0035577982 | 0.8619129741 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 19 | 2.7894702711 | 2.0299243285 | 0.8695868178 | 1.2247866219 | 2.1730928087 | 0.9564112789 |
| 20 | 2.7999982834 | 2.0462684950 | 0.8909550348 | 0.0616202674 | 0.4962600968 | 0.2464798809 |
| 21 | 2.8095229467 | 2.0494751526 | 0.8937254295 | 1.1776144818 | 2.1973029217 | 0.9734134417 |
| 22 | 2.8181813847 | 2.0742152823 | 0.9161125801 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 23 | 2.8260867388 | 2.0770857276 | 0.9157437379 | 1.1363501098 | 2.2184952953 | 0.9879979391 |
| 24 | 2.8333332241 | 2.0972990303 | 0.9378655874 | 1.0849850257 | 1.5441951806 | 0.7199263348 |

Balanced classes in even dimensions can be very small: zeros in the balanced columns can be exact parity values rather than missing computations. census_counts.csv records their sizes, independently checked by binomial subset sums.

At n=24, P/I=0.9999998807907104; all P extrema, including balanced ratios, are in extrema.csv. A and P attain their maxima at a single-corner AND/OR vector in every enumerated dimension. This is an observation through n=24, not an all-dimensions extremal theorem.

## Larger dimensions

For the displayed dimensions all thresholds r=1,...,n and all parity-times-threshold vectors were evaluated, including every level. The parity convention is f_t=(-1)^t times the threshold at r. Hill-climbing results are lower bounds from an explicit finite proposal budget; they are not asserted to be local or global optima. Proposals emphasize the binomial bulk and use coordinate or short block flips.

| n | best threshold B/I | best threshold Gamma/I | parity-threshold B/I | parity-threshold Gamma/I | value-vector B/I | value-vector Gamma/I |
|---:|---:|---:|---:|---:|---:|---:|
| 25 | 2.1033465579 | 0.7758354212 | 0.3499415710 | 0.1676247179 | — | — |
| 32 | 2.1682671074 | 0.8251701995 | 0.3161463472 | 0.1550413162 | 2.1710467484 | 0.9495430101 |
| 64 | 2.3251391528 | 0.9505583880 | 0.2359537205 | 0.1161566058 | 2.3251392320 | 1.0798464505 |
| 128 | 2.4510546358 | 1.0550845921 | 0.1729846253 | 0.0854829145 | 2.4515773061 | 1.1733350659 |
| 256 | 2.5529916180 | 1.1402092824 | 0.1268805291 | 0.0631597516 | 2.5529916180 | 1.2291505032 |
| 512 | 2.6325316342 | 1.2095899816 | 0.0922494085 | 0.0459724315 | 2.6325316342 | 1.2726296266 |
| 1000 | 2.6921993852 | 1.2633308830 | 0.0674016594 | 0.0336456777 | 2.6921993852 | 1.3120355369 |
| 1024 | 2.6940609481 | 1.2650117709 | 0.0666551934 | 0.0332736206 | 2.6940609481 | 1.3112820724 |
| 2000 | 2.7399446601 | 1.3068207338 | 0.0485141033 | 0.0242280584 | 2.7403595436 | 1.3476072980 |

The dense threshold sweep currently covers every dimension 1 through 2000, all thresholds in each dimension; thresholds_dense.jsonl records the maxima and central threshold. For odd n the central threshold is balanced majority. The hill searches use the dimension grid above; dense parity coverage is described below.

The independent Pascal sweep covers every parity-times-threshold vector in every dimension 2 through 2000; n=1 gives a constant function and undefined influence ratios. parity_dense.jsonl and parity_family.csv give the per-dimension suprema.

Balanced paired-coordinate searches at odd dimensions through 1999 optimize the ratio over I-1 directly. balanced_large.csv gives all computed ratios and value vectors. At n=1999 they reach B/(I-1)=2.744446594676 and Gamma/(I-1)=1.360500539114. These remain bounded-search lower bounds.

Parity-family outputs preserve tiny positive ratios in log2_ratios when the ordinary ratio underflows binary64. stable_log_check.log checks rare dimension-2000 functions at both 80 and 720 digits; ratio logarithms agree without needing precision proportional to n.

The dimension-2000 value-vector column includes the independent periodic-run sweep in gamma_refinement_2000.json. The A search in hill_A_*.json used sixteen proposals per dimension and retained corner AND/OR; at n=2000 it gives A/I=2.998. Its positive influence is too small for binary64, so the output supplies log2 influence.

Ordinary parity has A=B=Gamma=P=H=0 and I=n exactly, since its spectral law is a point mass on [n]. For odd n, balanced-majority ratios over I-1 are also given in majority.csv when the dense sweep is present. The threshold at r=1 gives A/I=3-4/n-(2-4/n)2^(-n) and P/I=1-2^(1-n) exactly.

## Direct bounds and the FEI obstruction

PROOFS.md proves B<=3.459354I and Gamma<=(8/5)I for every symmetric Boolean function. Above dimension 24 the proof is analytic; below it census_cert.c verifies an integer-only rational upper bound for every representative. constants.json and rational_constant_check.json check the constant two ways. The inherited bound A<=3.3252155I-Var follows by combining the supplied FEI benchmark with Theorem 1. No new direct sharper A bound is claimed.

Theorem 1 with a uniform B/I bound cannot improve the supplied 4.650431 FEI constant: the three-variable vector +++- has B/I=1.3725562489182657..., exceeding the required 1.3252155. The dimension-2000 witnesses are much larger.

The proved optimal-constant intervals are 3<=c_A<=3.3252155 (the upper bound inherits FEI), 2/ln 2<=c_B<=3.459354, and 1/ln 2<=c_Gamma<=8/5. PROOFS.md derives the lower limits from corner AND/OR and majority; majority_law_check.json verifies the exact finite derivative law and records the constants.

## What the extremizers look like

For B, the small-dimensional maximizers start as corner AND/OR functions, then become tails with extra short runs at distant weights. They need not be monotone. At n=24 one maximizing vector is +-++++++++++++++-----++++. The bulk of its negative mass is a one-sided binomial tail; the remote isolated change adjusts the spectral cancellations. At larger n, biased thresholds provide strong starting points and a few extra runs can improve them. This describes the computed witnesses and does not classify all extremizers.

For Gamma, the maximizers have several alternating sign runs across the binomial bulk. At n=24 one is +++--+++---+++++---+++---. The unrestricted-coefficient means are small relative to the absolute restricted means, making cancellation a large fraction of dispersion. The searches at larger n favor oscillations on a scale comparable to sqrt(n), rather than a single threshold. Some seeds and proposals use that scale; the independent width/phase sweep also finds such witnesses. This describes the computed examples, not an asymptotic extremal theorem.

## Checks and provenance

census.c and census_cert.c are independent runs of the exact integer triangle. audit.py checks direct truth-table restrictions for every symmetric function through n=4, the general A+B=H and Theorem 1 identities on every Boolean function through n=4, exact Parseval and influence identities, and binomial up-transform identities at every census extremizer. audit_candidates.py checks balanced counts by a separate meet-in-the-middle subset-sum computation and compares all near-winners at 100 digits. audit_large.py checks selected large-n witnesses at high precision and tries the new inequalities on random symmetric functions. Output logs are audit.log, candidates_audit.log, family_check.log and large_audit.log.

The recalled brain memory supplied the earlier derivative-envelope method and the distinction between the best FEI constant and the within-level bound. That recall helped. All writes stayed in this worker folder; no publishing, mesh posts, shared-memory writes or git operations were performed.

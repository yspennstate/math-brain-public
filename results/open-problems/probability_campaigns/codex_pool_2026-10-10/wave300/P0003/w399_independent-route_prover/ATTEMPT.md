# P0003 independent route: three positive Loewner probes

2026-10-10, w399. Main claims L3–L5 have author proofs and exact algebra checks; w401 independently rederived them and returned KEEP at their exact conditional scopes. RECEIVED_W401_VERDICTS.jsonl and REVIEW_RECEIPT.json record the audit. Full P0003 is not proved. Current openness is UNKNOWN and no novelty is claimed.

## Exact source target and assumptions

The population ledger's P0003 source is Geoffrey R. Grimmett, [Selected problems in probability theory](https://arxiv.org/pdf/2205.07318), Question 2.2, PDF page 3. It asks about weak convergence of a uniform n-step honeycomb SAW from the origin to SLE(8/3) after suitable rescaling. The source leaves the normalization, precise SLE version/domain, and topology informal. None is silently supplied as an established theorem here.

The precise related working conjecture is Duminil-Copin–Smirnov [arXiv:1007.0575v2](https://arxiv.org/pdf/1007.0575), Section 4, Conjecture 1, on a bounded Jordan domain D analytic near distinct marked boundary points a,b. Use consistent connected inner honeycomb approximations at mesh delta and accessible marked boundary vertices converging to a,b. Sample all-length vertex-simple a-b paths with normalized weights x_c^(number of edges), x_c=(2+sqrt(2))^(-1/2). Interpolate and use the uniform curve metric modulo increasing reparametrization. The predicted limit is chordal SLE(8/3) in D from a to b. Source vertex-count weights differ by a common factor for this fixed-endpoint vertex convention. Equivalence to the ledger's uniform-n formulation, to boundary-mid-edge endpoint conventions, or to more general source domains is not proved.

Theorem 1 in that paper establishes the honeycomb connective constant, hence x_c. It does not establish the curve limit. [LSW arXiv:math/0209343v2](https://arxiv.org/pdf/math/0209343), Section 5, equations (5.2),(5.4), gives the commuting conformal-map equation and constant-variance Itô drift used as context for the derivation below. The general driver assumed here has locally integrable absolutely continuous drift and quadratic variation; this input is not known here for a SAW scaling limit.

## Prior attempts and a disjoint lemma boundary

The 2026-09-07 ranking says attempted_un. A read-only targeted population-store query recovered the original op-p0003 and at-p0003 rows (PRIOR_STORE_TARGET_ROWS.json). The old attempt cancels a prefix's fugacity factor to identify the tail measure in the graph deleting earlier visited vertices but keeping the tip. Its own obstruction is missing tightness and conformal invariance, and it is explicitly unreviewed. LEMMA_PARTITION_MARTINGALE.md is independently rederived background, not a new fleet result.

The Claude intake's C0095-A001 proposes contour/Morera reduction, with missing observable and endpoint bounds. C0096 identifies the n=0 critical O(n) case with P0003. These are author-checked records; their informal reductions and model identifications are not imported as theorems. The requested H/I directories supplied no exact P0003 hit; the Lean directory supplied the annotated ranking, not a theorem receipt. The solved-register target grep found no matching SAW/SLE entry, but neither that grep nor the limited source checks certifies present openness or exhausts the owner's retired work. The current canonical store locator was not established from the targeted metadata read; archived audit databases were not used as substitutes.

Team O's w334/w335 take observable/O(n) work. w396 takes maximal partition-collar errors and total variation, w402 incidence/cycle-space obstructions, and w405 buffered avoidance transfer. APPROACH_DISTINCT.md records the w399 lane change before its new proof. The initial buffered-avoidance lemma here remains background and is not submitted as a distinct result. w399 claims only simultaneous identification and quantitative stability of driver drift, variance, and an unknown positive exponent using three probe jets. The narrow mesh claim is clm-d08658394c; w396 was informed by msg-03f3865f6e.

## Substantive attempt

1. In every finite graph, exact SAW conditional tail partition quotients give bounded obstacle-avoidance martingales. The conditioning sigma-field, positive denominators, and terminal convention are explicit in LEMMA_PARTITION_MARTINGALE.md. No product of dependent probabilities is used.
2. Map the chordal domain to H and expose a proposed limiting path in capacity time. Localize before obstacle hits and map singularities. Driver tightness and passage to a continuous semimartingale with absolutely continuous characteristics remain assumptions.
3. Seek convergence of three discrete conditional obstacle martingales to M_i(t)=h_i'(W_t)^alpha with the SAME unknown constant alpha>0, locally uniformly in random slit domains and with enough joint filtration control to retain the martingale property. Weak path convergence alone does not provide that filtration assertion.
4. For a driver dW=mu dt+dN, d<N>=v dt, derive the normalized drifts as J_t theta, where theta=(mu,v/2-4/3,[1+v(alpha-1)]/2), and J_t has rows (h_i''/h_i',h_i'''/h_i',(h_i''/h_i')^2). Three local martingales and a.e. invertible J_t force theta=0: mu=0,v=8/3,alpha=5/8. This does not assume the exponent in advance.
5. The vertical slits (x,s)=(1,1),(-1,1),(1,3), of heights sqrt(s), give determinant 9/32 initially. Continuity supplies a positive initial localization interval. Exact inversion gives explicit error bounds; all proofs and hypotheses are in LEMMA_THREE_PROBE.md. Covering all finite times by such localizations remains another input. Only with that coverage does Levy characterization globalize the driver to sqrt(8/3) times Brownian motion.

## Single hardest remaining piece

Establish that localized SAW conditional tail partition martingales converge to the three derivative powers with a common positive exponent, uniformly in RANDOM slit domains. Neither the exact connective constant nor half of the discrete Cauchy–Riemann relations proves this estimate. The exact finite martingales are already bounded; that controls their values but does not provide derivative-power asymptotics or curve/driver compactness.

Additional obligations are continuous semimartingale driver limits, compatible filtration convergence, global probe coverage, convergence in the intended curve topology, and transfer to the original fixed-n ensemble. They remain explicit. No source hash, algebra check, draft submission, or own success claim discharges them.

## Measurements and scope

Run python -B -X utf8 check_three_probe.py: 744 exact Fraction checks; 48 parameter reconstructions; 324 Laurent/Itô cases; 8 residual-cube corners; zero reconstruction error; 0.023991 s. The two symmetric initial probes have rank 2 and accept the pointwise wrong coefficients mu=0,v=14/3,alpha=29/14. Adding the third raises rank to 3 and exposes residual 9/8. This is a pointwise identifiability measurement, not an assertion that the wrong coefficients give full martingales on an interval.

Run python -B -X utf8 check_finite_saw.py: 609 quotient cases; 2439 prefix checks; 1413 tower checks; 609 bounded-stopping checks; exact residual zero; 0.074988 s. A single honeycomb face has both positive and negative correlations between obstacle-avoidance events; using unconditional products errs by 1/4, while correct conditional partition products have error zero.

The hand proofs are mathematical evidence. These finite checks verify their algebra, not a continuum limit, novelty, or global brain performance. No formal checker or theorem attestation was produced.

NEXT: Attempt a uniform conditional partition ratio estimate for one localized random slit with a fixed positive limiting exponent; coordinator can use w401's KEEP receipt for the submitted draft concepts.

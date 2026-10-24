# account01/B18 20260925T115716Z-account01-B18-r33 — repaired-source whole-paper audit

SIGNED IN - auditing repaired five-singular-value source 98e45d53, account account01, slot B18, 2026-09-25T11:57:16Z.

## Identity and controls

Objective: `QFORM-FIVE-270-REPAIRED-AUDIT-20260925`.

Exact source:
- repository: `yspennstate/math-open-problems`
- commit: `4e530247ec0ef4101a6e5ecf621bd35a969c42aa`
- path: `proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/repaired-2026-09-25/paper.tex`
- Git blob: `98e45d53d106db9a205051a4dd4917fc39dc2e3a`
- manifest SHA-256: `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`
- 683 physical source lines; 26 proof environments.

Fresh controls were read at invocation and refreshed immediately before publication. Guarded refresh blobs:
- AGENTS.md: `b675b94968920e7f6b0dcf209b77e03a6c8127e1`
- CURRENT_OBJECTIVE.md: `a1e93e8fb929b3064fea245dc435b65d17a89085`
- scheduled_tasks/README.md: `866599c3e76b4c8d8348fbb9113ea4a6f62c8b64`
- ORDER.md: `9073ed071051417c29319ff7d9d20d7f245255d8`
- source: `98e45d53d106db9a205051a4dd4917fc39dc2e3a`.

Own acknowledgement was created before substantive mathematics and read back:
`scheduled_tasks/work/shared/five-singular-values-repaired-audit-2026-09-25/acknowledgements/account01/B18/20260925T115716Z-account01-B18-r33.json`;
acknowledgement commit `260d170f101c8c9c3c1be17e12f1d5d68fe389f2`,
blob `29b97b8223d8a5fed2aec2f26f89d1f5bba5e0b1`.

This is a fresh complete B18 pass. No mathematical PASS was inherited from earlier runs.

## Verdict

**No fatal mathematical defect found.**

The repaired proof closes for its stated full scope:
independent real coordinate densities bounded by K; arbitrary real symmetric A, dimension, signature, remaining spectrum and affine b,c; if s_5(A)>=s>0 then the essential density of
Q=X^TAX+b^TX+c is <=270 K^2/s. The supporting s_3 full negative-half-moment estimate <=77 K/sqrt(s) also closes.

The only non-PASS source findings in this run are expository/bibliographic:
1. line 74 historical attribution phrases are UNCHECKED as phrased, although the precise mathematical source claims below were verified from primary/current source records;
2. line 677 has a bibliographic metadata convention ambiguity for Rogozin; no mathematical impact.

Reference-PDF pixel/source parity remains UNCHECKED: two conversation-file searches did not surface the 15-page attachment, and no renderer-accessible reference PDF bytes were available in this run. No fresh Lean build is claimed.

## Whole-proof reconstruction

### Lines 48–76 — definitions, theorem, scope, roadmap

PASS except the historical wording on line 74.

The theorem preserves exactly the advertised hypotheses: no iid, support, moment, smoothness, sign, remaining-spectrum or rotated-independence assumption. For symmetric A, singular values are eigenvalue moduli with multiplicity and zero padding. The interval and essential-density formulations are equivalent. Line 62 is manuscript-local (“the present argument does not settle...”), not a claim of current open status.

All introduction cross-references point to the claimed theorem/section and their hypotheses match the prose.

### Lines 81–173 — Fourier, conditioning, linear algebra

PASS.

Fourier normalization gives Plancherel factor (2pi)^d; the Gaussian identity has coefficient 1/(2sqrt(pi v)); Lemma 2.2 integrates to 2ap/(p-1); the Gamma/Tonelli calculation in Lemma 2.3 gives 1/sqrt(2pi) and the final 8sqrt(u) envelope exactly.

Conditioning is only on original coordinates. Product disintegration and Tonelli give the stated measure domination.

The min-rank singular-value proof correctly handles zero-padded indices before using singular vectors. The Schur-complement count controls both signs via the inverse principal block and preserves the equality threshold through epsilon perturbation. Gram/Cauchy–Binet and the projected determinant identity are exact.

### Lines 177–241 — geometric Brascamp–Lieb and product projections

PASS.

The heat-flow derivative is
(partial_tau F-Delta F)/F = sum c_i v_i^2 - |sum c_i v_i u_i|^2 >=0
by the frame contraction. Compact-time differentiation and integration by parts are justified by Gaussian-polynomial majorants; the large- and small-time limits and monotone truncation are valid.

The repaired projection proof correctly drops every zero-beta factor, handles p(y)=0 before logarithms, and never assumes independence after rotation. The positive weights form the geometric frame and the entropy estimate gives e^(d/2). The Fourier-power lemma correctly uses independent differences and continuous inversion.

### Lines 245–399 — crossing-volume Fourier decay

PASS.

The entropy lemma is exact. In the hub lemma:
- anchor/diffuse weights and marginals are correct;
- line 315 proves domination of the **total variation** of the complex pushforward by the law of Y using finite partitions;
- lines 315–322 construct a measurable version of x -> ||nu_x||_2^2 using a fixed approximate-identity sequence before expectation and before the terminal ell'=0 branch;
- lines 323–327 explicitly apply Jensen |E F|^2 <= E|F|^2;
- the later mollification, dominated convergence and reintegration use only original-coordinate independence;
- Holder exponents, determinant Jacobians, Fourier-power factors and entropy factors combine exactly to the printed hub estimate.

The greedy promotion proof gives the theorem constant. Corollary 4.4 is correct, including the exact power comparisons certifying C3<15 and C2<12.2.

### Lines 403–518 — one/two-coordinate analysis

PASS.

The scalar square density excludes the critical atom and defines the critical density value. The definite pair uses a genuine open slit-plane chart with absolute Jacobian and explicitly discards the null seam/critical point; no rotated independence is invoked.

The hyperbolic proof uses possibly different literal original coordinates in its positive and negative tails. The Jacobian, monotonicity, rearrangement, cutoff and determinant scaling reproduce
D^(-1/2)(6+log_+(16sqrt(D)/|z-v|)); the critical level is explicitly null.

The concentration lemma's diagonal and random-physical-cut branches are correct. The Gaussian smoothing coefficient is about 18.2553192, and the supplied Gamma log-convexity/rational certificate proves it is <19. Atomlessness and the log moment follow.

J(0)=+infinity and h(0)=+infinity are defined before use. The rearrangement and pair-half-moment calculation give 12+5log2<16 in the indefinite branch.

### Lines 523–588 — random signs

PASS.

The no-pivot entry bound is valid without a sign assumption on a_ii a_jj. The symmetric dilation duplicates each positive singular value and zero-pads afterward. The Rademacher fourth moment has exactly the two ordered surviving pairings.

The repaired empty off-diagonal maximum is defined. Proposition 6.4 yields
gamma_m=(44-5sqrt(2)(2m-1))/96
with the printed lower bounds for m=1,2,3, and the crossing-volume consequence follows from the nonnegative elementary symmetric polynomial.

### Lines 592–655 — half potential, main theorem, remarks

PASS.

The no-pivot bounds are <167 and <26. In the diagonal-pivot half-potential branch, the Schur complement retains two unit-scale directions; J(0) is already defined and atomlessness makes the finite J inequality applicable almost surely; the truncated contribution is <76 and the complement <=1.

For the main theorem a diagonal pivot leaves at least four unit-scale directions and a pair pivot at least three. The definite pair is <51. The indefinite-pair branch is about 266.95135<269. The diagonal branch is sqrt(12)*77 about 266.73582<267. General scaling Y=KX gives exactly K^2/s, with the density relation stated almost everywhere.

The two closing remarks are correct. The two-star example limits the order-three crossing method only; it does not claim a four-eigenvalue density counterexample.

## Cross-reference and citation audit

Programmatic full-source check:
- 683 physical lines;
- 50 labels, all unique;
- 89 internal ref/eqref occurrences;
- 44 distinct internal targets;
- zero unresolved targets;
- 12 citation occurrences;
- 11 unique citation keys;
- 11 bibliography entries;
- zero missing bibliography keys;
- 26 proof environments.

Every internal reference used in a proof was checked against its target statement/hypotheses; no mis-targeted dependency was found.

## Primary/current source verification for line 74

PASS for the precise mathematical claims that were actually verified:
- Livshyts–Paouris–Pivovarov, arXiv:1507.07949, explicitly prove the 2^(k/2) marginal-density bound for product densities capped by one.
- Rudelson–Vershynin's primary/author paper studies AX for X with independent coordinates and small-ball concentration of linear images.
- Bennett–Carbery–Christ–Tao, arXiv:math/0505065, explicitly describe heat-equation monotonicity methods for Brascamp–Lieb.
- Carlen–Lieb–Loss, arXiv:math/0408030, explicitly use a nonlinear heat flow.
- Carbery–Wright's primary Mathematical Research Letters paper is a distributional-inequality paper for polynomials.
- Costello–Tao–Vu's published abstract states that the proof uses a quadratic Littlewood–Offord concentration result.
- de la Peña–Giné's Springer monograph is a genuine general reference for decoupling.

UNCHECKED as historical characterizations:
- “The geometric Brascamp–Lieb inequality is due to Ball and Barthe” as an exact priority attribution;
- “Small-ball bounds for polynomials go back to Carbery and Wright” as an exact historical-priority statement;
- “the random sign step is the basic move of decoupling” as an exact characterization of this particular sign-flip argument.

These phrases are expository and not proof dependencies.

## Line 677 — Rogozin bibliography

Status: **GAP (bibliographic metadata convention ambiguity), no mathematical impact.**

The source gives “An estimate for the maximum of the convolution of bounded densities,” Theory Probab. Appl. 32 (1987), 48–56.

The SIAM English article landing page for DOI 10.1137/1132004 gives the title “Estimation of the Maximum of a Convolution of Bounded Densities” and places Volume 32 Issue 1 in January 1988. However, SIAM's own later reference lists cite the same article as Theory Probab. Appl. 32 (1987), 48–56. Thus the year discrepancy reflects the original-volume/English-translation convention rather than a mathematical problem. For bibliographic precision, use the SIAM landing-page title/year or state the original/translation convention explicitly.

## Numerical diagnostics

Fresh calculations:
- C3 = 14.818337662843
- C2 = 12.0950725707965
- gamma1 = 0.3846763769597
- gamma2 = 0.2373624642125
- gamma3 = 0.09004855146534
- Gaussian small-ball coefficient = 18.255319196767
- L0 = 7.88887795833288
- sqrt(12)*77 = 266.735824365607 <267
- indefinite main branch = 266.951346330334 <269.

The exact rational margins printed in the repaired source were rechecked and are positive.

## Status

- fatal mathematical defect: none found
- whole repaired source audited: yes, all 683 physical lines accounted for in coverage.jsonl
- historical line-74 phrases: UNCHECKED as phrased
- Rogozin line 677: bibliographic GAP only
- rendered reference PDF parity: UNCHECKED
- fresh Lean build: not performed
- independent reviewer milestone: not claimed; this is one B18 identity
- native receiver integration: WITHOUT_VERIFIED_BRAIN
- full_brain_connected: false

# fleet01/B07 repaired-source audit — pass 1 partial

Exact source: `yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa`, blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`, manifest SHA-256 `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`.

This is a partial new-hash audit, not an inherited old-source pass. Substantive coverage: L140-173, L208-240, L245-399, L452-479, L532-588, L594-646. Other ranges remain UNCHECKED and are listed in coverage.jsonl. Reference-PDF visual comparison is UNCHECKED in this run.

## B07 starting lens

**PASS L143-149 — singular-value approximation and padded indices.** The repair is correct. If s_j(T)=0, including a padded index, rank(T)<j and B=T gives the approximation number zero before any right-singular-vector argument is used. In the nonzero range the SVD truncation gives the upper bound and kernel intersection gives the lower bound. Rank perturbation and orthogonal compression follow.

**PASS L151-161 — Schur spectral count.** For invertible A, S^{-1} is the lower-right principal block of A^{-1}; interlacing applied to A^{-1} and -A^{-1} gives the count outside (-1/t,1/t). The epsilon shift avoids finitely many singular shifts, has S_epsilon -> S, preserves N_A(t) at threshold t-|epsilon|, and Lemma 2.5 closes equality in the limit.

**PASS L163-173 — Gram identities.** Characteristic-polynomial coefficients plus Cauchy-Binet give the crossing-volume formula. Theta(H)>0 makes the H-row Gram block invertible, and the block determinant formula gives exactly Theta(H union T)=Theta(H)det(C_TC_T^T). Rank-deficient/out-of-range terms are consistent.

## Repaired dependency checks

**PASS L208-240.** Zero-beta factors are fiber-independent and <=1, so all may be dropped; the old cardinality interpretation is not a defect. The proof handles p(y)=0 before taking logarithms. The Fourier-power lemma uses only the density cap and original-coordinate independence.

**PASS L245-399.** The entropy lemma handles zero marginals. In the Hub Lemma, positive crossing volume forces hub-row independence; the complex pushforward has total variation dominated by the law of Y; a fixed approximate identity makes x -> ||nu_x||_2^2 measurable before its expectation and before the ell'=0 terminal branch; Jensen is explicit; mollification and dominated convergence are valid; weighted Holder and the projection-density estimate close. Greedy row promotion never spends zero mass, loses at most a factor two per promotion, stops with the diffuse condition unless k=ell, and gives exactly (sqrt(2) pi e)^ell. The exact comparisons proving C3<15 and C2<12.2 have positive rational margins.

**PASS L452-479.** The random-cut Frobenius factor is 1/4. The Gaussian smoothing integral and Gamma factor are correct. Log-convexity gives Gamma(1/4)^4<=64 pi, hence coefficient^4<=2048 e^3 pi; the printed rational upper bounds on e and pi leave positive margin below 19^4. The no-atom and logarithmic layer-cake conclusions follow.

**PASS L532-588.** The no-pivot bounds imply the printed a0 threshold. The symmetric dilation duplicates each singular value of A_{I,J} and then pads by zeros. The Rademacher fourth moment has exactly the two ordered pairings (i,j) and (j,i), with no missing factor. Compression and Weyl give s_m(A_{I,J})>gamma_m, and Lemma 2.7 yields E_m>gamma_m^(2m).

**PASS L594-646.** The no-pivot receiver and three-direction half-potential branches are consistent with the repaired earlier lemmas. In the scalar-pivot branch, J(R-a) is evaluated off zero almost surely after the no-atoms result. Schur count leaves the required 2/4/3 large directions in the supporting/main branches. The main cases are exhaustive, and Y=KX with A/s gives the density scaling K^2/s almost everywhere.

## Current verdict

No new GAP or FALSE was found in the audited ranges, and no fatal theorem obstruction was found. This does not certify the whole repaired source because substantial ranges and the rendered PDF remain UNCHECKED in this run.

Complete B07 passes on repaired blob: 0.
Brain status: WITHOUT_VERIFIED_BRAIN; full_brain_connected:false.
Model: GPT-5.6 Sol; effort telemetry: UNKNOWN.

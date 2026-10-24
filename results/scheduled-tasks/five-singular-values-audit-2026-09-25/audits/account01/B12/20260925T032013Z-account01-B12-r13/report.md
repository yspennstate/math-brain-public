# account01/B12 — fresh adversarial line audit

Run: `20260925T032013Z-account01-B12-r13`  
Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`

Source pin:
- repository `yspennstate/math-open-problems`
- commit `ec211ba2d77a4a9850168c6af1574ea651feaa7c`
- TeX `proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex`
- TeX blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`
- PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`

Fresh `AGENTS.md`, `scheduled_tasks/CURRENT_OBJECTIVE.md`, `scheduled_tasks/README.md`, and all six shared-package files were read before the sign-in. Own acknowledgement was created and read back at commit `d6ae7eae1fbe8f241e34d75500ef8d85de71cd7c`, blob `6f7c31ad34c965d5ca47014024caed857c9b928c`. Native-brain status remains `WITHOUT_VERIFIED_BRAIN`.

This is a fresh reconstruction; no previous PASS is a premise. The audit began again at the B12 Section 5 lens and then reconstructed the dependency chain backward and forward. Mathematical source lines 1–647 were checked in this run. Lines 648–675 were inspected as bibliography/end matter; bibliographic/current-priority claims remain partly UNCHECKED. Rendered PDF/source equivalence is UNCHECKED because the private PDF was not materializable through the required screenshot path. Complete full passes under the owner definition: **0**. First still-UNCHECKED source clause: line **62**, current-open-status sentence.

## Literal-source findings

1. **Line 41 — GAP (C04, presentation).** The abstract says the random-sign argument turns (2m-1) large eigenvalues into (m) large crossing singular values without saying “in the absence of a pivot”. Proposition 6.4 has the required no-pivot hypothesis. Counterexample to the unconditional wording: (A=I_5) has five large eigenvalues but every crossing block is zero. The theorem statement is unaffected.

2. **Line 62 — UNCHECKED (C07).** The examples showing one and two large eigenvalues do not suffice are correct. The sentence asserting that the three-large-eigenvalue bounded-density problem “is open” was not established by an exhaustive current primary-source search. A current search found no definitive resolution, but that is insufficient to certify an open-status claim. Minimal wording: “The present argument does not settle whether three eigenvalues ... suffice.”

3. **Line 65 — GAP (C05, presentation).** The conditional one/two-variable law does not always *have* a square-root or logarithmic singularity; the proofs establish square-root/logarithmic upper envelopes. Replace “has ... a singularity” by “admits ... an upper envelope”.

4. **Line 148 — GAP (local proof wording; strengthens C06).** The rank-approximation characterization of (s_j(T)) is correct, but the proof invokes “the first (j) right singular vectors” even when (j) lies in the padded-zero range and those vectors need not exist. Zero-loss repair: first dispose of (j>min(m,n)), where (s_j(T)=0) and the minimum is (0) by choosing (B=T); then use the printed kernel/intersection argument for (jlemin(m,n)). All downstream uses in this paper have indices within the relevant dimensions.

5. **Lines 319–322 — GAP-AS-WRITTEN (C02, zero-loss).** After the conditional Cauchy–Schwarz/Plancherel estimate, “averaging over (X_{I'})” omits the needed Jensen step
[
|mathbb E F(X_{I'})|^2le mathbb E|F(X_{I'})|^2.
]
The conditional complex measure is valid: (
u_xll P_Y), its Radon–Nikodym derivative is a conditional expectation of a unit-modulus phase, so (|
u_x|le p_Y). With the explicit Jensen line, the scaled Plancherel factor ((pi/|t|)^k) is correct.

6. **Line 398 — GAP (density-version point only).** The displayed square-law density formula is undefined literally at (z=v) because the denominator is zero. State the formula for (z
e v) and choose any density value at (v), e.g. (p_T(v)=0). The interval-preimage estimate is correct and unaffected.

7. **Line 412 — GAP-AS-WRITTEN (C01, zero-loss).** ((0,infty)	imes[0,2pi)) is not globally diffeomorphic to the punctured plane because of the angular seam. Use ((0,infty)	imes(0,2pi)) and remove the corresponding ray; the ray and critical point are null and the absolute Jacobian remains (1/(2sqrt{det B})).

8. **After line 441 — GAP-AS-WRITTEN (C03, zero-loss).** The hyperbolic proof treats (z>v) and (z<v) but does not explicitly exclude an atom at (z=v). The critical level is the union of two affine lines, hence has probability zero under the joint density. The current source correctly chooses separate original coordinates for the positive and negative tails.

No theorem-bearing FALSE statement was found.

## Independently reconstructed core chain

### Fourier and conditioning, lines 81–138
Lemma 2.1 has the correct Fourier normalization. The Gaussian identity is absolutely integrable, so Fubini is legitimate. Lemma 2.2 integrates the power envelope exactly. Lemma 2.3 follows from the Gamma representation and two Tonelli applications; the substitution gives
[
int_0^infty v^{-5/4}e^{-t^2/(4v)},dv
=4^{1/4}Gamma(1/4)|t|^{-1/2}.
]
The conditioning domination lemma is valid by product-measure Tonelli and Radon–Nikodym.

### Linear algebra, lines 140–173
The singular-value perturbation, rank-shift and orthonormal compression statements are correct after the padded-index wording repair above. The Schur-complement count loses (k), not (2k): for invertible (A), (S^{-1}) is a principal block of (A^{-1}), and two-sided interlacing controls the counts outside ([-1/t,1/t]); the (arepsilon I) argument handles singular (A). The Gram/Cauchy–Binet identities are correct.

### Geometric Brascamp–Lieb and projection bounds, lines 177–241
The heat-flow identity
[
(partial_	au F-Delta F)/F
=sum c_i v_i^2-left|sum c_i v_i u_iight|^2ge0
]
follows from (WW^T=I). The compact-support derivative bounds justify differentiation and (intDelta F=0). The large-(	au) and small-(	au) limits are supported by dominated convergence and Fatou respectively. Truncation gives the general case.

For Lemma 3.2, the row weights (eta_i=|w_i|^2) lie in ([0,1]), satisfy (sumeta_i=n-d), and Brascamp–Lieb gives
[
log p(y)le 	frac12sumeta_ilog(1/eta_i)le d/2.
]
Lemma 3.3 correctly uses the density bound for (Y-Y'), Plancherel, and the projection lemma to obtain (2pisqrt{2e/p}).

### Crossing-volume decay, lines 245–390
The entropy lemma is correct by Jensen plus the multinomial expansion. Lemma 4.3 was reconstructed all the way through:
- independent-copy Step 1 is valid;
- Step 2’s complex measure and scaled Plancherel estimate are valid after explicit Jensen C02;
- the mollifier (kappa_arepsilon) is a probability density, (L^2) approximation and dominated convergence are valid;
- the weighted Hölder identity treats zero marginals correctly;
- the joint projected vector in Step 4 has determinant (Theta(H)	heta(T'));
- the diffuse condition gives (1/alpha_ige2), so Lemma 3.3 applies;
- the entropy product in Step 5 gives exactly the displayed (omega(ell-k)^{1/2}) factor.

The greedy proof of Theorem 4.1 is correct after C02. Its constant (a_k) decreases because
[
a_{k+1}/a_k
=e^{-1/2}sqrt{omega(m-1)/omega(m)}le e^{-1/2}.
]
Corollary 4.4 is then correct for (ell=1,2,3). This run therefore independently closes the (ell=2,3) dependencies left UNCHECKED in the preceding B12 invocation.

### B12 Section 5 lens, lines 393–510
Lemma 5.1’s interval-preimage bound is correct. Lemma 5.4 is independently closed in both branches; the off-diagonal branch uses the now-reconstructed Corollary 4.4(c). A rigorous enclosure in the attached checker gives
[
2^{5/4}e^{3/4}Gamma(1/4)<18.99388512<19.
]
The no-atoms limit and layer-cake logarithmic moment are correct. Lemma 5.5’s antiderivatives, (d>1) comparison, and layer-cake rearrangement are correct. Lemma 5.6 is correct after C01/C03: definite branch (<6D^{-1/4}); indefinite branch has far contribution (8) and near contribution (4+5log2), hence (<16D^{-1/4}).

### Random signs and final proof, lines 513–647
The no-pivot entry bound is correct. The symmetric dilation has each singular value of (A_{I,J}) twice. The Rademacher fourth-moment count retains exactly the ordered pairs ((i,j)) and ((j,i)), giving the stated factor (2). Proposition 6.4 correctly compresses to (2m-1) eigendirections and obtains the (gamma_m) margins.

With Corollary 4.4 now reconstructed, Proposition 7.1 closes end-to-end after C02. Proposition 7.2 closes after C01–C03 and the line-398 density-version repair. The diagonal-pivot truncation uses Lemma 5.5 with (R-a), whose zero case is null by Lemma 5.4. The main theorem’s no-pivot, diagonal-pivot, definite-pair and indefinite-pair cases are algebraically consistent, and the final scaling (Y=KX) gives exactly (K^2/s). The theorem claim is therefore supported by the repaired chain, but the literal original remains a GAP-source because the local omissions above are unpatched.

## Constants
The attached exact/rational checker verifies rigorous enclosures sufficient for:
- (C_3<15);
- (C_2<12.2);
- (gamma_1>0.38,gamma_2>0.237,gamma_3>0.09);
- (0.237^{-1/2}<2.055) and (12.2cdot2.055<26);
- the Lemma 5.4 coefficient (<19);
- (12+5log2<16);
- the diagonal-pivot truncated contribution (<76);
- (sqrt{12},77<267), (16pi<51), and the manuscript’s indefinite-pair majorant (<269).

## Literature/render status
A current web check verified that Banks–Garza Vargas–Kulkarni–Srivastava Theorem 2.1 is indeed a bounded-density theorem for the stated bilinear random-matrix form, and independently matched several bibliography entries (BCCT, CLL, CTV, Rogozin, RV). This is not an exhaustive bibliography audit. The current-open-status claim at line 62 and remaining citation metadata/attributions stay UNCHECKED.

Rendered PDF/source formula equivalence stays UNCHECKED because the private PDF could not be passed to the required screenshot tool. Page numbers are therefore recorded only where supplied by the owner correction package (C02 page 7, C01 page 9, C03 pages 9–10); all other coverage rows use `UNKNOWN_RENDER`.

## Pass status and next cursor
- Complete owner-defined passes in this version-specific ledger: **0**.
- Mathematical proof source 1–647: reconstructed this run, with the literal local gaps listed above.
- Bibliography/end matter 648–675: inspected, partly UNCHECKED for external metadata.
- First still-UNCHECKED source clause: **line 62 current-open-status claim**.
- First essential theorem dependency still UNCHECKED: **none**, after the explicit local repairs.
- PDF render/source equivalence: **UNCHECKED**.
- No peer PASS was used as a premise and no cross-account action was performed.

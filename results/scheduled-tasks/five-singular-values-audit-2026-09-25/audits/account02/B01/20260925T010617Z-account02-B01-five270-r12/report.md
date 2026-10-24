# account02/B01 — five-singular-values line audit, pass 2 (reverse/adversarial)

## Immutable source and control

- Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`.
- Fresh control head before publication: `c3e9d4fd428335aaf59f8630655191ee3f551131`; CURRENT_OBJECTIVE blob `b167cb098b86d7f000e3fdd58efd17bcb2a58715`, unchanged.
- Source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`.
- TeX: `short/short.tex`, blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, physical lines 1–675 plus terminal newline.
- PDF: blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`, 484310 bytes, 14 pages, manifest SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.
- PDF page tree was independently parsed from the pinned bytes through the authenticated repository connector: page objects are 54,112,137,144,155,164,180,197,202,215,229,248,279,289. Named destinations independently place Theorem 1.1 on p.1; Section 2 on p.2; Theorems 2.4–2.6 on p.3; Lemma 2.7 and Section 3 on p.4; Lemmas 3.2–3.3 and Section 4 on p.5; Theorems 4.1–4.3 on p.6; Corollary 4.4 on p.8; Section 5 on p.9; Lemmas 5.4–5.5 on p.10; Lemma 5.6 and Section 6 on p.11; Lemmas/Proposition 6.3–6.4 on p.12; Section 7 and Propositions 7.1–7.2 on p.13; Remarks 7.3–7.4 and bibliography on p.14.
- A browser screenshot route to the private pinned PDF was unavailable, so glyph-by-glyph rendered-PDF/source equivalence remains UNCHECKED. Mathematical auditing is against the exact pinned TeX.

This is B01 complete manuscript pass 2, reconstructed in reverse dependency/adversarial order. Prior B01 pass 1, CORRECTIONS.md, and peer reviews were not used as premises.

## Overall verdict

The exact theorem chain remains mathematically sound **after local zero-loss repairs**, but the literal source contains one newly identified FALSE sentence in Lemma 3.2 that earlier B01/B19 and account03/B05 reviews did not flag:

> line 222: “Factors with β_i=0 are at most one and are dropped.”

The “at most one” assertion is false. Take n=4, d=2, U=[e_1,e_2], and complete U with W=[e_3,e_4]. Then the first two rows of W vanish, so β_1=β_2=0. In general there can be up to d zero rows. The proof does **not** need the false count: every β_i=0 factor is independent of the fiber variable z and is at most one, so any number of them may be dropped. The frame identity over the positive β_i remains exact, and lines 224–226 already correctly tolerate multiple zero indices. Minimal repair:

`Factors with β_i=0 are independent of z, bounded by one, and are dropped.`

No constant or downstream theorem changes. Lemma 3.2 remains valid after this repair.

This finding is independent and materially disagrees with separate evidence: account02/B19 explicitly marked line 222 PASS in its full coverage record, while account03/B05’s projection audit silently used the repaired operation “dropping only the β_i=0 factors” but did not challenge the literal “at most one” sentence.

## Other reproduced source defects

The following previously recorded issues were independently reproduced rather than inherited.

- **Line 41, p.1 — FALSE as written, theorem-neutral.** The abstract says the random-sign argument turns 2m-1 large eigenvalues into m large crossing singular values without its essential no-pivot hypothesis. A=I_5 refutes the unqualified sentence: five unit eigenvalues, every crossing block zero. Repair: add “in the absence of a pivot.” The formal Proposition 6.4 has the correct hypotheses.
- **Line 62, p.1 — UNCHECKED status claim only.** All quantitative scope/scaling/counterexample clauses pass, but the present-day statement that the three-eigenvalue bounded-density problem is open was not established by a complete primary-source search. It is not a proof dependency.
- **Line 65, p.1 — FALSE descriptive wording, theorem-neutral.** A definite two-coordinate quadratic need not “have” a singularity; what is proved is a square-root/logarithmic upper envelope. Replace “has” by “admits … an upper envelope.”
- **Line 148, p.3 — NOT_MATHEMATICAL editorial defect.** “Both follow” introduces three assertions. All three spectral assertions themselves pass independently.
- **Lines 319–322, p.7 — GAP, zero-loss repair.** From the conditional Plancherel estimate to the averaged bound one must explicitly use |E F|^2≤E|F|^2. Inserting Jensen/Cauchy–Schwarz gives the displayed inequality with no constant change.
- **Line 412, p.9 — FALSE chart wording, zero-loss repair.** The elliptic polar map from (0,∞)×[0,2π) is not literally a global diffeomorphism because of the angular seam. Remove one null ray (or use the standard a.e. polar chart); the Jacobian and density bound are unchanged.
- **Lines 415–442, pp.9–10 — GAP, zero-loss repair.** The hyperbolic changes of variables cover z>v and z<v. Density existence at z=v needs the observation that {q=v} is the union of two affine lines after an invertible linear change, hence has probability zero under the joint density. The source correctly uses separate original coordinates i and i' for the two tails; the older same-coordinate defect is not present.

No additional theorem-level FALSE statement was found.

## Theorem 1.1 quantifiers and scaling

Lines 54–60 pass exactly as written: independent, not necessarily identically distributed real coordinates; only one-dimensional density caps; arbitrary dimension, b,c, signature and remaining spectrum; essential bounded density conclusion, not global continuity.

The final scaling at lines 635–639 was reconstructed. For K,s>0 set Y=KX. Then each Y_i has density at most one and
[
Q=rac{s}{K^2}widetilde Q,qquad
widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
]
with s_5(A/s)≥1. Hence |p_Q|_∞=(K^2/s)|p_{~tilde Q}|_∞. The normalized proof gives <269, so the advertised ≤270 K^2/s follows. The interval formulation is equivalent by absolute continuity plus the interval bound/outer-regularity argument.

## Complete dependency reconstruction

- Fourier inversion, Gaussian smoothing, negative-half-moment representation, conditioning domination: PASS.
- Singular-value Lipschitz, compression monotonicity, symmetric off-diagonal singular-value pairing, Schur loss by pivot size, Gram/Cauchy–Binet: PASS. The three spectral facts are source-proved here; no new formalization was proposed.
- Heat-flow geometric Brascamp–Lieb: PASS. Differentiation, integration by parts, large-time Gaussian limit, small-time Fatou/Lebesgue differentiation, and truncation were checked.
- Product-projection lemma: PASS **after the new line-222 wording repair**. No rotated-independence claim is used.
- Fourier powers/difference-density lemma: PASS.
- Crossing-volume decay theorem: PASS after the explicit Jensen insertion at lines 319–322. Complex-measure domination, mollification, weighted Hölder, entropy, and determinant factors were checked.
- Scalar-square and definite-pair kernels: PASS after the polar-chart wording repair.
- Hyperbolic kernel: PASS after the critical-level null-set sentence; tail monotonicity, two distinct large original coordinates, and constants checked.
- Concentration/log moment, kernel convolution, pair half-potential: PASS.
- Random-sign fourth-moment identity and Proposition 6.4: PASS with its no-pivot hypothesis.
- No-pivot density, three-direction half-potential, and all pivot branches: PASS after upstream repairs.
- Remarks 7.3–7.4: PASS mathematically; the four-eigenvalue star construction is only a method obstruction and is stated that way.

## Numeric regression, independently recomputed this pass

[
gamma_1=0.3846763769597346,quad
gamma_2=0.2373624642125372,quad
gamma_3=0.0900485514653398,
]
[
C_3=14.818337662843,qquad C_2=12.095072570796486.
]
Thus
[
C_3/gamma_3=164.5594229081<167,qquad
C_2/sqrt{gamma_2}=24.8257545631<26.
]
The diagonal-pivot half-potential branch is 75.1430750104<76; the main scalar branch is (sqrt{12},77=266.7358243656<267); the definite pair branch is (16pi=50.2654824574<51); and the indefinite branch is
[
16(8+4log2+2log19)+1/e=266.9513463303<269.
]

## Status

Literal-source status for this pass: **FALSE/GAP locally, theorem chain PASS after explicit repairs**. The new line-222 FALSE sentence is theorem-neutral but should be added to the shared correction set. No release/status mutation is authorized or performed. Audit-only scope was respected; no three/four-eigenvalue research or constant improvement was done.

The full line ledger is in `coverage.jsonl`; the new repair is isolated in `repair-L222-beta-zero.md`.

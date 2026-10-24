account02/B05 five-eigenvalue paper audit

Run: 20260924T222230Z-account02-B05-five270-auto11
Source add commit: 47b4d8b244bdf4bc25cb0f74e0b4314c1ad278b7
paper.tex blob: f3e5fc173cdcee40174c19c955d813d47f32bd91
paper.tex SHA-256: 359d1e4c5ffe528dcd749f4315b426d6423944d88678544131fa3ffe090c1362

VERDICT: PASS after one local nonfatal source repair. No FALSE theorem-bearing claim found. Bibliographic/priority lines are UNCHECKED.

Complete line ledger:
1-48 PASS: metadata, abstract, quantifiers.
49-102 PASS: main and half-potential statements, scaling and architecture.
103-122 PASS: Fourier/Plancherel/Gaussian regularization.
123-153 PASS: envelope and negative-half-moment/Riesz calculation.
154-164 PASS: measurable conditioning domination on original independent banks.
165-187 PASS: singular-value perturbation/compression and Schur spectral count.
188-199 PASS: Gram/Cauchy-Binet identities.
200-232 PASS: geometric Brascamp-Lieb heat-flow proof and rough limits.
233-255 PASS: product-projection density; zero-weight factors are <=1 and are dropped, then zero entropy terms are restored. Result: ||p_{BX}||_inf <= exp(d/2)/sqrt(det(BB^T)). No projected-coordinate independence is used.
256-267 PASS: scalar Fourier-power estimate from literal independent copies.
268-284 PASS: crossing volumes and decay theorem statement.
285-295 PASS: entropy inequality.
296-396 PASS: grouped/hub compiler. Output-space Plancherel precedes duplication; only literal coordinates are hubs; mollification justifies the L2 expansion; weighted Holder exponents are >=2; the residual image is paid by a marginal density.
397-417 PASS: promotion and order 3/2/1 analytic consequences.
418-439 PASS: square and definite-pair profiles.
440-455 PASS: hyperbola parametrization/Jacobian.
456-462 GAP (presentation only): the coordinate chosen large for u need not be large for u'. For the negative tail choose a possibly different i_minus with |u'_i_minus| >= |u'|/sqrt(2). Witness to literal same-coordinate reuse: u=(1/sqrt(2),0), u'=(0,1/sqrt(2)). Since |u|=|u'|, every cutoff and constant is unchanged.
463-468 PASS after that repair: logarithmic envelope and both signs.
469-497 PASS: concentration/log potential; atom exclusion by rho->0.
498-517 PASS: square-root/log kernels and rearrangement.
518-537 PASS: pair half-potential; singular profile is integrated before averaging.
538-553 PASS: pivot definitions and eta^2+zeta=(5/48)^2.
554-565 PASS: A-DAD=2C and doubled singular spectrum of the off-diagonal block.
566-584 PASS: exact sign-chaos second moment and Frobenius bound.
585-606 PASS: random-sign Proposition 6.4; k=2m-1 large eigenvectors force s_m(A_IJ)>gamma_m.
607-622 PASS: no-pivot density and half-moment.
623-642 PASS: complete s3 half-potential <=77.
643-665 PASS: complete s5 density theorem. Branches: no pivot <167; diagonal pivot <267; definite pair <51; indefinite pair <269. Scaling gives 270 K^2/s.
666-672 PASS: half-potential scaling gives 77 K/sqrt(s).
673-685 PASS: threshold remarks, two-star obstruction, and the E2=1 logarithmic counterexample.
687-714 UNCHECKED: bibliography/priority only.

B05 projection reconstruction:
For U^T U=I_d, complete U to (U,W), set beta_i=|w_i|^2, and use Fubini in the original product density. Geometric BL gives p(y)<=prod beta_i^(-beta_i/2). Since -beta log beta<=1-beta and the zero beta terms can be restored on the right, ||p_{U^T X}||_inf<=exp(d/2). SVD gives the full-row-rank bound above.

Exceptional-slice controls:
(1) Rotated iid uniforms have a bounded projected marginal but conditional orthogonal density sup 1/(sqrt(2)-2|y|), which diverges at boundary slices.
(2) 2 X1 X2 has logarithmic density log(1/(2|t|)) near zero.
(3) X1^2 has t^(-1/2) density near zero.
(4) The paper's E2=1 example still has unbounded logarithmic output density.
These refute conditional-cap and order-two-to-Linf shortcuts, not the paper.

Random-sign reconstruction:
With no pivot, |a_ii|<1/12 and |a_ij|<5/48. For k=2m-1 selected large eigenvectors, E||Q_eps||_F^2 <= 2 a^2 k^2, so some sign vector has operator error <sqrt(2)(5/48)k. Compressing 2C=A-DAD gives
s_k(2 Phi^T C Phi)>1-1/12-sqrt(2)(5/48)k=2 gamma_m.
Compression and the doubled block spectrum give s_m(A_IJ)>gamma_m. This proves the new 5=2*3-1 crossing step.

Next obligations:
- patch lines 456-462 by naming positive and negative tail coordinates separately;
- formalize the three remaining spectral facts;
- for four eigenvalues, combine order-two crossing with physical hub/star structure and arbitrary affine terms. An exact-flat-pair receiver is supplied separately.
- unrestricted three-eigenvalue QFORM remains OPEN.

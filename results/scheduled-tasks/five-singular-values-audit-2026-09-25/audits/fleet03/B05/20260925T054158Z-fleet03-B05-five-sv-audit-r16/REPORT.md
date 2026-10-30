# fleet03/B05 r16 — five-singular-values audit, pass 2

Source: math-open-problems commit ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, exact 14-page PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

Control remained QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925. Initial main head f8ced7c931b094fb7f40db71c1ae65a7d09ae26a; pre-publication head 0952b485b752bfe96dbea5db7d2c060956e1b479. Execution remains WITHOUT_VERIFIED_BRAIN.

## Primary range: source lines 245-371

This run independently reconstructed Section 4 through the end of Lemma 4.3. The range passes except for the already-recorded literal C02 omission at lines 319-322.

Definitions: E_l(M) equals the sum of l-row Gram determinants, the l-th elementary symmetric polynomial of MM^T, and the sum of squared l-by-l minors. Principal-minor identities and Cauchy-Binet give these equalities. Theta_l and omega conventions are consistent.

Lemma 4.2: the entropy inequality passes. Finite-sum rearrangement gives sum_i alpha_i log alpha_i as a w-average. Jensen gives the logarithm of the sum of squarefree monomials. Each m-subset monomial occurs m! times in (sum alpha_i)^m and sum alpha_i=m, yielding log(m^m/m!).

Lemma 4.3 setup: positive Theta_l(H) forces hub-row independence. Orthogonal residualization gives Theta(H union T')=Theta(H) theta(T'), hence Z_H=Theta_l(H)/Theta(H). The induced weights are a probability law and the diffuse hypothesis gives alpha_i<=1/2. D=X_J-X'_J has independent original-coordinate components with density cap one by convolution. No projected coordinates are declared independent.

Step 1: Cauchy-Schwarz in the literal X_I variables, independent-copy expansion in X_J, and integration of the original independent X_i give the printed product of characteristic functions. All integrands have modulus at most one, so Fubini is valid.

Step 2: p_H<=1 gives ||a||_2<=1. Product projection bounds the density of Y=M_H X_J. For the complex measure nu_x(B)=E[exp(itR)1_B(Y)], setwise domination by the law of Y implies a Radon-Nikodym derivative of modulus at most one, so |nu_x|<=p_Y and ||nu_x||_2^2<=||p_Y||_infinity. Scaled Plancherel gives exactly the factor (pi/|t|)^k.

C02 is reproduced: the literal transition described as “averaging over X_{I'}” omits the necessary Jensen/Cauchy-Schwarz inequality |E F|^2 <= E|F|^2. Inserting that line repairs equation (4.5) with constant one. No downstream constant changes.

Mollification: the autocorrelation kernel kappa_epsilon is a probability density. Expanding the squared L2 convolution gives the independent-copy formula. Approximate-identity convergence in L2 plus Young's inequality supplies a uniform integrable bound; dominated convergence is therefore valid. Integrating X_{I'} first recovers the characteristic-function product and equation (4.6).

Step 3: alpha_i=0 factors can be dropped because |psi_i|<=1. For retained indices the total exponent is one, and positive weights give valid Holder exponents 1/w_T.

Step 4: for positive-weight T', hub rows and residual rows are orthogonal groups, with Gram determinant Theta(H)theta(T')>0. The product-projection theorem bounds the joint density of the linear image of D; this is not an independence assertion. Translating each scalar residual coordinate and applying Lemma 3.3 with p=1/alpha_i>=2 gives the printed Fourier-power factor.

Step 5: the weighted determinant factors combine to Theta_l(H)^(-1/2) exp(H(w)/2), while the alpha powers give exp((1/2) sum alpha_i log alpha_i). Lemma 4.2 yields omega(l')^(1/2), reproducing the hub constant exactly.

No additional Section 4 gap, hidden rotated-independence assumption, measurability failure, or constant mismatch was found.

## Cross-pass correction

After deriving the Section 4 block, I compared against independent fleet02/B06 and B09 audit outputs. Both independently report the Section 4 Holder/determinant/mollification chain valid except for C02.

That comparison also exposed a clause I had previously marked PASS at line 505. I independently rechecked it. The source uses h(y)=6+log_+(16/|y|) as a function on all real y. At y=0 this requires an extended-real convention that is not stated. I record this as fleet03 C11: local domain GAP, repair PASS. Define h(0)=+infinity and keep the printed formula for y!=0. Lemma 5.5 explicitly permits extended nonnegative functions, and a singleton definition changes no density integral or constant.

## Pass status

Pass 1 is complete. Pass 2 previously covered lines 372-639; after this run it covers lines 245-639. Remaining pass-2 ranges are lines 1-244 and 640-676. Next reverse-dependency cursor: line 177.

No fatal theorem-level defect was found in this run. Direct glyph-level PDF/source parity remains UNCHECKED because the private PDF is unavailable to the screenshot browser.

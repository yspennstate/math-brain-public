# fleet03/B08 r15 — pass 2, lines 336–391

Source: math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423. Pass 2 lens: B09 mollification/measurability/Fubini/DCT/kernel normalization. Prior pass-2 coverage was 323–335; this file covers 336–391.

## Lemma 4.3 Step 3, lines 337–344 — PASS
For every positive-weight T', i in T' implies alpha_i>=w_T'>0. Dropping zero-marginal factors is valid since |psi_i|<=1. For alpha_i>0, sum_{T' contains i} w_T'/alpha_i=1, so the weighted exponent identity is exact. The positive weights form a finite probability law; kappa_epsilon>=0 and equals the weighted product of its powers. Holder with exponents 1/w_T' is valid, including weight one.

## Step 4, lines 346–355 — PASS
Residual rows c_i are orthogonal to the hub row span, hence det(BB^T)=Theta(H)theta(T')>0. The copied difference vector D has independent original-coordinate densities <=1, so Lemma 3.2(b) applies to the deterministic projection (M_HD,(<c_i,D>)_i), with no projected-coordinate independence assumption. After absolute values the integrand is nonnegative; density domination and Tonelli justify the iterated integral. The z-shear has Jacobian one. u=2t(z+lambda_i.y) contributes 1/(2|t|). Diffuseness gives alpha_i<=1/2, so Lemma 3.3 at p=1/alpha_i>=2 yields pi sqrt(2e alpha_i)/|t|. kappa_epsilon integrates to one. The k=0 convention is consistent.

## Step 5, lines 357–370 — PASS
With theta(T')=Z_H w_T', the determinant product is Theta_ell(H)^(-1/2) exp(H(w)/2). The marginal product is exp((1/2)sum_i alpha_i log alpha_i), using the stated 0log0 convention. Lemma 4.2 closes the entropy factor. Combining with Step 2 gives line 367 with the correct powers of pi,e,|t| and Theta.

## Theorem 4.1, lines 372–378 — PASS
Each accepted promotion loses at most a factor two, so Theta_ell(H)>=2^-k E_ell(M)>0. Stopping with k<ell is exactly the diffuse condition required by Lemma 4.3. omega(m)/omega(m-1)>=1 gives a_(k+1)/a_k<=e^-1/2, hence a_k<=a_0. The constant simplifies exactly to (sqrt(2) pi e)^ell.

## Corollary 4.4, lines 380–391 — PASS
Taking square roots gives the stated envelope. For ell=3 the exponent 3/2 is integrable, so Lemma 2.2 yields a continuous density and C3=14.818337662842996<15. For ell=2, Lemma 2.3 gives C2=12.095072570796486<12.2. For ell=1, omega(1)=1 and E1=||M||_F^2. Continuity is not claimed in the ell=2 or ell=1 conclusions.

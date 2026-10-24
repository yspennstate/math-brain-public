# account02/B07 source-line audit — pass 1

Run: `20260925T003517Z-account02-B07-audit11`  
Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`  
Control HEAD immediately before publication: `a52da47f3f7eddb992a85639b25c648e0e465422`.

## Exact immutable source

Repository: `yspennstate/math-open-problems`  
Pinned commit: `ec211ba2d77a4a9850168c6af1574ea651feaa7c`  
LaTeX: `proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex`  
TeX blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8`  
PDF blob: `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`  
PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`  
PDF size/pages: 484310 bytes / 14 pages.

The exact TeX has 675 nontrailing source lines. I read the full source at the pinned commit. Direct private-PDF rendering was unavailable in this run, so source/render formula identity and page mapping are UNCHECKED except for page locations explicitly supplied by the shared correction package. No source or PDF file was modified.

## Verdict

**Literal manuscript: GAP, repairable locally. Main theorem chain: no FALSE step found; PASS after the local repairs C01--C03.** The two theorem-independent presentation issues C04--C05 do not alter any proof. The current-open-status clause in line 62 remains UNCHECKED as a literature-status assertion. Bibliographic priority/attribution was not re-searched.

The audited theorem is the exact claim
[
s_5(A)ge s>0quadLongrightarrowquad
|p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}le270K^2/s
]
for arbitrary independent real coordinate densities bounded by K, arbitrary real symmetric A, arbitrary b,c, dimension, signature, remaining spectrum, support and moments.

## Open literal-source issues

1. **C04, line 41, PDF p.1 — GAP (presentation).** The abstract says the random-sign argument turns (2m-1) large eigenvalues into (m) crossing singular values without stating its no-pivot hypothesis. This is false as a standalone assertion: (A=I_5) has five large eigenvalues and every off-diagonal block is zero. Proposition 6.4 itself includes the no-pivot hypothesis, so the theorem proof is unaffected. Minimal repair: insert “in the absence of a pivot”.

2. **C05, line 65, PDF p.1 — GAP (presentation).** “has a square-root or logarithmic singularity” overstates what the conditional estimates prove; the definite two-coordinate case can be bounded at the critical value. Minimal repair: “admits a square-root or logarithmic upper envelope”. No proof impact.

3. **C02, lines 319--322, PDF p.7 — GAP (omitted one-line inequality).** From the conditional bound to (4.5), insert
[
|mathbb E_{X_{I'}}F(X_{I'})|^2le mathbb E_{X_{I'}}|F(X_{I'})|^2.
]
This is Jensen/Cauchy--Schwarz. Constants and hypotheses are unchanged. I derived this before comparing with account03/B03 run `20260925T002840Z-account03-B03-fiveaudit-r1`, which independently reports the same omission.

4. **C01, line 412, PDF p.9 — GAP (literal topology wording).** The elliptic polar map from ((0,infty)	imes[0,2pi)) is not a global diffeomorphism onto the punctured plane: the inverse angle is discontinuous across the seam. Use ((0,infty)	imes(0,2pi)) onto the plane minus one ray and discard that null ray, or use the standard polar change-of-variables theorem. The Jacobian (1/(2sqrt{det B})) and density constant (pi L/sqrt{det B}) are unchanged.

5. **C03, Lemma 5.3 lines 416/441, PDF pp.9--10 — GAP (missing null critical level).** The two hyperbolic charts cover (q>v) and (q<v). To justify the statement that the whole law has a density, add that ({w:q(w)=v}) is the union of two affine lines and is null for the joint density of ((W_1,W_2)). The current source already correctly chooses separate physical coordinates (i,i') for the two tails at line 431. No constant changes.

6. **C07, line 62, PDF p.1 — UNCHECKED.** The present proof certainly does not settle the three-large-eigenvalue density question, but this run did not conduct the complete current primary-literature search needed to certify the word “open”. No theorem dependency.

7. **C06, line 148, PDF p.3 — editorial only.** “Both follow” introduces three assertions. All three singular-value assertions were checked and pass; changing to “These assertions follow” is grammatical only.

## B07 lens: Lemma 2.7 and crossing-volume combinatorics

### Lines 163--173 — PASS

For (Minmathbb R^{I	imes J}), the coefficient of (z^ell) in (det(I+zMM^T)) is both (e_ell(MM^T)) and the sum of principal (ell)-minors of (MM^T). For each row subset (S), Cauchy--Binet gives
[
det(M_SM_S^T)=sum_{|T|=ell}det(M_{S,T})^2.
]
Every unordered row subset and column subset appears exactly once. There is no factorial, orientation or ordered-minor multiplicity.

For (H) with (Theta(H)>0), the Gram Schur complement is
[
G_{TT}-G_{TH}G_{HH}^{-1}G_{HT}=M_T(I-Pi)M_T^T=C_TC_T^T,
]
hence (Theta(Hcup T)=Theta(H)det(C_TC_T^T)). The positivity hypothesis is exactly what makes (G_{HH}) invertible.

### Lines 245--249 — PASS

The crossing volume
[
E_ell(M)=sum_{|T|=ell}Theta(T)=e_ell(MM^T)
        =sum_{|S|=|T|=ell}det(M_{S,T})^2
]
uses unordered physical subsets. No hidden selection multiplicity is introduced.

### Lemma 4.3 lines 271--370 — PASS after C02

- (Theta_ell(H)>0) implies some positive full Gram minor containing H, so the H-rows are independent and (Theta(H)>0).
- The residual weights (w_{T'}=	heta(T')/Z_H) form a probability law and
  [
  alpha_i=Theta_ell(Hcup{i})/Theta_ell(H)
  ]
  exactly. No multiplicity factor is missing.
- The copy (D=X_J-X'_J) has independent coordinates, each with density at most one. Independence is only across original physical indices.
- The complex measure (
u_x) is absolutely continuous with respect to the law of (Y=M_HX_J); equivalently its Radon--Nikodym derivative is the conditional expectation of a unit-modulus phase, so (|
u_x|le p_Y).
- The scaled Plancherel factor is exactly ((pi/|t|)^k).
- The mollified (L^2) identity and dominated-convergence passage are valid because convolution by a probability density is an (L^2) contraction and (|
u_x|_2^2le|p_Y|_infty).
- In Hölder, each positive-marginal Fourier factor has total exponent (sum_{T'
i i}w_{T'}/alpha_i=1); zero marginals are dropped using (|psi_i|le1).
- In Step 4, promoted rows and projected residual rows are orthogonal, hence the Gram determinant is exactly (Theta(H)	heta(T')). The Fourier-power lemma applies because diffuseness gives (alpha_ile1/2), hence (1/alpha_ige2).
- Step 5 combines determinant weights with the entropy inequality without an extra factorial or ordering factor.

### Greedy proof lines 372--378 — PASS

Each promotion satisfies
[
Theta_ell(H_{r+1})>	frac12Theta_ell(H_r),
]
so after k promotions (Theta_ell(H_k)>2^{-k}E_ell(M)). The algorithm either reaches (k=ell) or stops with the exact diffuse hypothesis of Lemma 4.3. With
[
a_k=(2e)^{(ell-k)/2}omega(ell-k)^{1/2}2^{k/2},
]
[
a_{k+1}/a_k=e^{-1/2}
 left(rac{omega(ell-k-1)}{omega(ell-k)}ight)^{1/2}le e^{-1/2}
]
because (omega(m)/omega(m-1)=(m/(m-1))^{m-1}ge1). The stated constant ((sqrt2pi e)^ell) follows.

### Corollary 4.4 lines 380--391 — PASS

Taking square roots of Theorem 4.1 gives the envelope with the correct power (E_ell^{-1/4}|t|^{-ell/2}). The (ell=3) Fourier-inversion constant and (ell=2) half-moment constant are
[
C_3=3sqrt2 e(9/2)^{1/6}=14.81833766ldots<15,
qquad
C_2=8e^{1/2}2^{-1/8}=12.09507257ldots<12.2.
]

## Remaining proof chain

I also checked the source-level dependencies outside the initial B07 lens.

- Fourier normalization, Gaussian identity, envelope, half-moment and conditioning (lines 80--138): PASS.
- Singular-value minimax, rank perturbation, compression and Schur count (143--161): PASS.
- Heat-flow geometric Brascamp--Lieb, product projection and Fourier-power bound (177--241): PASS.
- Square profile, hyperbola tail estimates, concentration, kernel rearrangement and pair half-moment (395--510): PASS after C01/C03.
- Section 6 random signs (513--580): PASS independently in this run. The ordered-pair Rademacher expansion has exactly the two surviving contractions ((p,q)=(i,j),(j,i)). The symmetric dilation duplicates each crossing singular value exactly twice.
- Section 7 (582--639): PASS after the same local repairs. No-pivot constants, Schur losses, all pivot cases and final scaling were recomputed.

Numerical values independently recomputed:
[
gamma_1=0.3846763769ldots,quad
gamma_2=0.2373624642ldots,quad
gamma_3=0.0900485515ldots,
]
[
C_3/gamma_3=164.5594229ldots<167,qquad
C_2/sqrt{gamma_2}=24.8257546ldots<26,
]
[
sqrt{12},77=266.7358244ldots<267,quad
16pi=50.2654825ldots<51,
]
and the indefinite-pair upper bound is (266.9513464ldots<269).

## Exact finite diagnostics

Independent exact-integer/rational checks (diagnostic evidence, not universal proof) covered:
- 600 Cauchy--Binet crossing-volume cases;
- 23,950 residual Gram/Schur-complement determinant identities;
- 16,679 exact determinant-weight marginal identities;
- 593 greedy row-promotion runs.

All had zero failures.

## Coverage status

- Exact TeX source read: 675/675 nontrailing lines.
- Source-level mathematical pass completed: 1.
- Full audit cycle including direct rendered-PDF formula comparison: 0.
- First source clause left UNCHECKED: line 62 current-literature “open” status; line 74 bibliographic attributions are also not freshly source-verified.
- Direct PDF source/render comparison: UNCHECKED because the private PDF renderer was unavailable. The Git blob/SHA/byte/page identity is pinned by MANIFEST but provenance identity is not render verification.
- No FALSE proof step or theorem-level counterexample found.
- Peer comparison was performed only after independent derivation; account03/B03 independently agrees on C02.

The owner-directed audit-only objective remains active. No four-/three-eigenvalue extension or constant-improvement research was performed in this run.

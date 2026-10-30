# fleet02/B16 pass 1 — exact fourteen-page proof audit

Source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`.  
TeX blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8` (fetched in full; 676 physical lines including terminal blank).  
PDF blob: `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`.  
Manifest PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`; 484310 bytes, 14 pages.

## Verdict

No fatal defect was found in the 270 K^2/s theorem or the 77 K/sqrt(s) half-moment theorem. The **literal source is not gap-free**, but the theorem chain closes after local, constant-preserving repairs.

- **L222, p5 — FALSE harmless clause.** “Factors with beta_i=0 are at most one” is false. For n=4,d=2 take U=(e1,e2) and its orthogonal complement W=(e3,e4); rows w1,w2 vanish, so beta1=beta2=0. Repair: drop all zero-beta factors. They are bounded by one and contribute no frame mass. The projection bound is unchanged.
- **L319–321, p7 — GAP.** Insert the outer Jensen/Cauchy–Schwarz step |E F|^2 <= E|F|^2 before (4.5).
- **L412, p9 — FALSE presentation clause.** The half-open angular chart is not a global diffeomorphism. Remove one null ray and take theta in (0,2pi); the Jacobian and pi L/sqrt(det B) bound are unchanged.
- **proof closure at L442, p10 — GAP.** State that the critical level q=v is a union of two affine lines and therefore has probability zero under the joint density.
- **L41, p1 — FALSE descriptive clause.** The abstract's random-sign conversion needs the no-pivot qualifier. A=I5 has five unit eigenvalues and every crossing block is zero.
- **L65, p1 — overstatement.** Replace “has a square-root or logarithmic singularity” by “admits a square-root or logarithmic upper envelope”.
- **L62, p1 — UNCHECKED external status.** The proof itself does not settle the three-eigenvalue density question; the stronger current-literature claim was not exhaustively searched.
- **L148, p3 — wording only.** “Both follow” introduces three statements; all three mathematical statements pass.

## B16 initial lens: Section 6, L513–580, pp11–13

**PASS.** With eta=1/12, zeta=1/256 and a0=5/48, no pivot gives |aii|<eta and |aij|<a0 because eta^2+zeta=a0^2.

For a sign partition, A-DAD=2C entrywise. Ordering the parts gives C=[[0,M],[M^T,0]]. An SVD of M produces eigenvectors (u,+/-v)/sqrt(2) with eigenvalues +/-sigma, so every singular value of M is duplicated and s_{2m-1}(C)=s_m(M).

For the sign chaos Q_eps, expansion of the Frobenius square shows that, with i!=j and p!=q, only (p,q)=(i,j) and (j,i) survive expectation. Hence
E||Q_eps||_F^2 = sum_{i!=j} o_ij^2 (|phi_i|^2 |phi_j|^2 + (phi_i.phi_j)^2)
<= 2 a^2 (sum_i |phi_i|^2)^2.
No factor of two is missing.

For k=2m-1, the k-eigenvector frame has total row mass k. Averaging therefore gives a sign vector with ||Q_eps||_F < sqrt(2) a0 k. The exact compressed identity
2 Phi^T C Phi = Lambda - Phi^T Delta Phi - Q_eps
and singular-value Lipschitz yield s_k(2 Phi^T C Phi)>1-eta-sqrt(2)a0 k=2 gamma_m. Compression and the duplicated block spectrum give s_m(A_IJ)>gamma_m; the nonnegative elementary symmetric sum gives E_m>gamma_m^(2m).

Independent numerical recomputation:
gamma1=0.3846763769597346, gamma2=0.2373624642125372, gamma3=0.0900485514653398.

Existing source-pinned Lean logs were inspected only after this derivation. `run_five2.log` records the sign/Frobenius chain; `run_five3.log` records rc=0 for the spectral chain, with the printed axioms limited to propext, Classical.choice and Quot.sound. Fresh compilation in this run is **UNCHECKED**.

## Remaining sections

**L80–127, Fourier/half-moment — PASS.** Fourier normalization, Gaussian inversion, Mellin integral, Tonelli, the 1/sqrt(2pi) coefficient and the 8 sqrt(u) envelope were recomputed.

**L129–173, conditioning/linear algebra — PASS.** Conditioning is only on original coordinate banks. Distance-to-rank singular-value facts, Schur spectral count (including the singular limit), and Gram/Cauchy–Binet identities check.

**L175–241, product projections — PASS after L222 repair.** Heat-flow Brascamp–Lieb, limits and truncation check. Dropping every zero-beta row repairs L222. The Fourier-power lemma uses a literal 2m-coordinate product bank.

**L243–391, crossing compiler — PASS after explicit Jensen.** The copy is only the literal J bank. The phase-weighted complex measure is dominated by the ordinary joint law of M_H X_J. Mollification is in L2. Step 4 applies one **joint** projection-density bound to (M_H D,(<c_i,D>)_i) before scalar Fourier powers. No projected independence is asserted. Holder/entropy and the greedy hub constants check.

**L393–510, one/two-coordinate profiles — PASS after the chart/null-level repairs.** The hyperbolic tails use distinct original coordinates i and i' as required. Concentration, kernel rearrangement and pair half-potential constants check.

**L582–639, final proof — PASS after upstream repairs.** No-pivot branches are <167 and <26. The diagonal-pivot main branch is sqrt(12)*77=266.7358243656<267. The truncated diagonal-pivot half-potential term is 75.1430750104<76 before adding the outside 1. The indefinite-pair branch is 266.9513463303<269. The final rescaling is K^2/s for density and K/sqrt(s) for the half moment.

**L641–647, remarks — PASS.** The one-eigenvalue half-moment counterexample is correct. The two-star example is a limitation of the order-three-crossing method, not a four-eigenvalue density counterexample.

## Independence and inherited dependencies

No independence leakage was found. Every independence step uses original coordinates or literal independent copies. Rotations are deterministic linear-algebra/change-of-variable devices; projected coordinates are never treated as independent.

Prior audits, numerical logs and Lean logs were not used as proof premises. Direct visual PDF/source comparison remains **UNCHECKED** because this execution could fetch the private PDF blob but could not route it to the screenshot-capable viewer. Page locators are recorded in `coverage.jsonl`. Bibliographic/current-priority claims are not proof dependencies and remain unverified where marked.

`coverage.jsonl` contains 697 rows: one record for every physical source line plus clause-split records for mixed/long assertions. A future invocation should begin a reverse-dependency full pass; a favorable pass is not a stop condition.

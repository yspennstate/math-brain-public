SIGNED IN - auditing the exact fourteen-page five-singular-value proof, account account03, slot B10, 2026-09-25T04:12:11Z.

# B10 pass 2 backwards audit, lines 393-647

Pinned source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, exact PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423. Final control refresh before publication: dd5aed74154453aafbbb784aac8d888e6006a19b. Objective unchanged: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925.

I reconstructed Sections 7, 6 and 5 backwards without constant optimization or lower-threshold research. No new theorem-level defect was found.

Preserved literal defects independently reproduced:
- line 398, PDF p.9: GAP. The square-law density display is undefined at z=v. State it for z!=v or a.e.; choose the density value at v arbitrarily. P(Y=m)=0.
- line 412, PDF p.9: FALSE wording. The half-open polar chart is not a global diffeomorphism because of the angular seam. Delete one ray; it is null and the Jacobian 1/(2 sqrt(det B)) and pi L/sqrt(det B) bound are unchanged.
- lines 427-441, PDF pp.9-10: GAP. Hyperbolic charts cover q>v and q<v but omit q=v. That level is two affine lines and is null under the joint density.

Reconstructed PASS items:
- lines 634-638: exact scaling Q=(s/K^2)Qtilde and p_Q(z)=(K^2/s)p_Qtilde(K^2z/s); interval bound extends to Borel sets by open-set decomposition and outer regularity.
- lines 628-632: indefinite pair critical value has the pair Schur-complement matrix, which retains at least three large eigenvalues. The printed 269 bound follows from D^{-1/2}<=16, log_+(16 sqrt D)<=4log2+(1/2)log_+D, and sup D^{-1/2}log_+D=2/e.
- lines 623-625: diagonal pivot leaves at least four large eigenvalues; conditional square domination plus Proposition 7.2 gives sqrt(12)*77<267.
- lines 598-616: Proposition 7.2's diagonal case gives |a_ii|^{-1/2} E J(R-a); the Schur complement has norm >=1, so the concentration/log-moment and kernel estimates give truncated contribution <76 plus outside contribution <=1.
- lines 586-595: E3>gamma3^6 and E2>gamma2^4 give the source <167 and <26 bounds using C3<15, C2<12.2.
- lines 560-579: random-sign proposition reconstructed from the Rademacher Frobenius bound, the identity 2 Phi^T C Phi=Lambda-Phi^T Delta Phi-Q_epsilon, Weyl, compression, doubled crossing singular values and the Gram identity. Exact margins: gamma1-0.38>299/64000, gamma2-0.237>67/192000, gamma3-0.09>1/38400.
- lines 541-557: only the two ordered Rademacher pairings survive, giving the displayed expectation and factor 2.
- lines 524-538: eta^2+zeta=25/2304=(5/48)^2; sign conjugation and duplicated crossing-block singular values are correct.
- lines 493-509: pair half-potential layer cake and delta=1/64 rearrangement give 8+(4+5log2)<16, subject to the repaired hyperbolic critical-level clause.
- lines 473-490: kernel antiderivatives and layer-cake rearrangement are correct.
- lines 444-469: concentration split, random partition, Fourier smoothing, coefficient 2^(5/4)e^(3/4)Gamma(1/4)<19, no-atoms limit and log layer cake are correct.
- lines 645-646: the two-star closing example has spectrum 1,1,-1,-1, no pivot for N>256, and every crossing block has rank at most two.

The exact checker uses only rational/series certificates and reports ALL R04 EXACT/RIGOROUS CERTIFICATES PASS. In particular it proves Gamma(1/4)<15/4, the concentration coefficient <18.921, the source diagonal truncated bound <75.934, and the indefinite-pair coarse bound <268.736.

After deriving these results, I compared against separately executed account02/B10 run 20260925T034541Z-account02-B10-fiveaudit-auto11 and account02/B01 run 20260925T040109Z-account02-B01-five270-r15. Their diagnostics agree; account02/B10 independently records the line-398 issue.

Pass 2 now covers source lines 393-647 backwards. Next cursor: line 391, then continue backwards through Section 4. The recurring audit remains active. Execution remains WITHOUT_VERIFIED_BRAIN.

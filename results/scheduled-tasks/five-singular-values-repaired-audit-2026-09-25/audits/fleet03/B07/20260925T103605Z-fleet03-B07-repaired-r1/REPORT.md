fleet03/B07 repaired-source audit r1
source 4e530247ec0ef4101a6e5ecf621bd35a969c42aa / blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a
coverage: paper.tex lines 140-173
verdict: PASS on Lemma 2.5 padded-index repair, Lemma 2.6 Schur count, Lemma 2.7 Gram identities; no new GAP/FALSE in this lens.
Padded case: if s_j(T)=0 then rank(T)<j and B=T attains the best-rank error 0. If s_j(T)>0, j is a live singular index and the right-singular-vector kernel argument is valid.
Schur case: interlacing of S^{-1} inside A^{-1}, plus epsilon perturbation, gives N_S(t)>=N_A(t)-k at the closed threshold.
Gram case: principal-minor expansion plus Cauchy-Binet gives the complete squared minor bank; Gram Schur complement gives Theta(H union T)=Theta(H)det(C_TC_T^T).
Complete repaired-source passes: 0. Remaining: lines 1-139 and 174-683.
Rendered-page verification: UNCHECKED this run. WITHOUT_VERIFIED_BRAIN.

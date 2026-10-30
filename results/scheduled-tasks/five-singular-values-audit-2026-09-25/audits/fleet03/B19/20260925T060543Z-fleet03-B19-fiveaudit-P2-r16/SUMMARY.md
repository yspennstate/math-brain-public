fleet03/B19 P2 reverse-dependency audit r16
Source: math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8, exact 14-page PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.
Direct coverage this run: L346-L392. P2 direct coverage now L346-L646. Next exact target L286-L345.

Findings: L346-L355 Step 4 PASS locally; orthogonal Gram factor, projection density and p=1/alpha Fourier-power factor all check. L357-L370 Step 5 PASS locally; determinant and alpha products give the stated entropy factor and the hub bound. L372-L378 Theorem 4.1 greedy promotion PASS locally; a_{k+1}/a_k=e^{-1/2}(omega(m-1)/omega(m))^{1/2}<=e^{-1/2}. L380-L391 Corollary 4.4 PASS locally; constants recompute C3=14.81833766...<15 and C2=12.09507257...<12.2, and the ell=1 formula is exact.

Current-pass end-to-end closure is pending because Lemma 4.3 Step 2/Step 3, Lemma 4.2, projection/Fourier-power lemmas and Lemmas 2.2-2.3 are below the current P2 cursor; C02 at L319 must be regression-tested when reached. No new repair or fatal defect in L346-L392.

Peer comparison after derivation: fleet01/B06 r23 commits 0952b485b752bfe96dbea5db7d2c060956e1b479 / 629260c3018c7e7c9d5a6080edbda16e58c605cf agrees on this range. Existing L148 disagreement remains preserved and was not re-adjudicated.

Exact PDF render comparison remains UNCHECKED in this run; page references use the existing decoded-source map: Step 4 p7-8, Step 5/Theorem 4.1/Corollary 4.4 p8.

WITHOUT_VERIFIED_BRAIN.
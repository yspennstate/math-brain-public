# account03/B14 r11 — Pass 05, L380-L510

Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c; short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8; PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

Pass 05 rotates to a conclusion-type/pushforward lens. No fatal theorem defect was found in L380-L510.

New literal local gaps:
- B14-R11-01, L503/p11: the layer-cake display writes s^{-2} at integration endpoint s=0. Repair: integrate over (0,infinity) or define that one endpoint value. No integral/constant changes.
- B14-R11-02, L505/p11: h(y)=6+log_+(16/|y|) is used as an actual function in rearrangement, but log_+ was defined only on positive real arguments, so h(0) is undefined. Repair: set h(0)=+infinity. Lemma 5.5 already allows [0,infinity]-valued functions; one-point definition changes no density bound or integral.

Regression:
- B14-R01-01 remains a singleton density-representative gap in Lemma 5.1.
- C01 remains false literal global-diffeomorphism wording with a null-ray repair.
- C03 remains the missing explicit critical-level-null sentence.

Conclusion typing rechecked independently: Corollary 4.4(a) yields a continuous density by L1 Fourier inversion; (b) yields only a negative-half moment; (c) yields only pointwise Fourier decay. Lemmas 5.1-5.3 are pushforward density statements after the recorded local repairs; Lemma 5.4 gives no atoms; Lemma 5.5 permits extended-valued rearrangement. The Lemma 5.6 bound remains <16 D^{-1/4} after the two new domain repairs.

A fresh raw-web PDF fetch was blocked for the private source, so no new screenshot claim is made. Exact pinned TeX was fetched via authenticated GitHub and page references use the established 14-page mapping.

After independent derivation, account03/B15 r17 was compared. It independently agrees on the Corollary 4.4 regularity split and on density-vs-continuity handling, but did not audit the two new pair-half domain clauses. No contradiction was found.

Pass 05 remains IN_PROGRESS; next line L511.

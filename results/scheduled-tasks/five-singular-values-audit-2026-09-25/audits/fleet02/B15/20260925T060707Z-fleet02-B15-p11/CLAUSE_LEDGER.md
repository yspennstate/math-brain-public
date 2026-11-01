# P11 clause and repair ledger

Source: ec211ba2d77a4a9850168c6af1574ea651feaa7c, short.tex c4f2a997cf336ee974e15409b5bccdd8cca039d8, PDF 8be3aae36ecad7a9dc9b7c95978aad09499f32d0 / 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.
Page map used for rows: 1–70 p1; 71–118 p2; 119–162 p3; 163–204 p4; 205–248 p5; 249–305 p6; 306–345 p7; 346–392 p8; 393–436 p9; 437–484 p10; 485–537 p11; 538–576 p12; 577–627 p13; 628–676 p14. Pixel re-render not available this run.

## Repairs independently tested
- C01 L412: open-angle/null-ray chart; critical singleton null; same Jacobian and constant.
- C02 L319: Jensen |EF|²<=E|F|²; same Plancherel constant.
- C03 L442: critical hyperbola is union of two affine lines, hence null under the joint density.
- C04 L41: add no-pivot qualifier; A=I5 falsifies unqualified synopsis.
- C05 L65: replace actual-singularity language by upper-envelope language.
- C06 L148 grammar is not the only issue: the literal proof also needs a padded-index case split (P11-R01).
- C07 L62: leave present-day open-status assertion unverified unless separately primary-source certified.
- P11-R02 L398: density formula only for z!=v/a.e.; define value at v arbitrarily.
- P11-R03 L505: define h(0)=+infinity before rearrangement.
- P11-R04 L613: prove R atomless before E J(R-a), or extend J(0)=+infinity and then use atomlessness.

## Corollary 4.4 dependency reconstruction
Theorem 4.1 -> characteristic-function squared bound.
Taking square roots gives exponent -ell/2.
ell=3: p=3/2 envelope is L1; Lemma 2.2 yields continuous density and C3.
ell=2: p=1 is non-L1; Lemma 2.3 gives only the half-potential and C2.
ell=1: exponent -1/2 is retained pointwise and later inserted into Gaussian smoothing in Lemma 5.4.
No endpoint swaps were found.

## Density-existence mechanisms
- Fourier L1 branches: continuous density (L86, L99, Cor.4.4(a), Prop.7.1(a)).
- Conditioning L132-138: absolute continuity + a.e. domination only.
- 1D square change: a.e. density after critical-point representative repair.
- definite 2D chart: density after seam/null-critical-point repair.
- indefinite hyperbola: density on z!=v plus C03 atom exclusion.
The final theorem needs only essential boundedness.

## Independence
Every probabilistic conditioning is on literal original coordinate blocks. The projection/Gram/eigenvector operations are deterministic coefficient-space operations. No rotated random coordinates are declared independent.

Open problem F0119. Source: E. Mossel, "Survey: information flow on trees" (2004, DIMACS volume; arXiv:math/0406446),
Problem 1, Section 5, PDF p. 8: for the 3-state Potts channel on the b-ary tree (M = (1 - q epsilon) I + epsilon J with q = 3,
or the source's own parametrisation in its equation (8)), find the parameter values for which the reconstruction problem is
solvable. The source adds that the analogous problem for the Ising model with external field may be easier. Known to the
source: solvable if b lambda_2^2 > 1 (Kesten-Stigum); unsolvable if b |lambda_2| <= 1; unsolvable if
b (1 - q epsilon)^2 / (1 - (q-2) epsilon) <= 1. Read the source for the exact channel, the sign conventions (ferromagnetic and
antiferromagnetic sides) and the definition of solvability.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:math/0406446 into sources/ (plain text only) and read Sections 2-5 exactly. Then search:
   A. Sly "Reconstruction for the Potts model" (Ann. Probab. 39 (2011), arXiv:0905.3797; the Kesten-Stigum bound is tight for
   q = 3 on the ferromagnetic side for large b, and not tight for q >= 5), Sly "Reconstruction of random colourings", Mezard-
   Montanari (cavity predictions: KS tight for q = 3, q = 4 borderline), Bhatnagar-Vera-Vigoda-Weitz, Martinelli-Sinclair-Weitz,
   Mossel-Peres, Borgs-Chayes-Mossel-Roch "The Kesten-Stigum reconstruction bound is tight for roughly symmetric binary
   channels", Liu-Ning (Ising with external field, asymmetric binary channels), Kulske-Formentin, Ricci-Tersenghi-Semerjian-
   Zdeborova, Chen-Gu-... and 2011-2026 work on reconstruction for the 3-state Potts model on the binary or small-degree tree
   and on the antiferromagnetic side. State exactly which (b, epsilon) region is settled in print and by which theorem, with
   page numbers. If Problem 1 is fully answered in print (all b >= 2, both signs), stop with REPORT.md first line
   RESOLVED_IN_LITERATURE.
2. Reduce. Write the belief-propagation / distributional recursion for the root posterior on T_b for q = 3 and the second-
   order (small-magnetisation) expansion behind Sly's argument; identify exactly which b and which sign of lambda_2 the known
   proofs do not cover (for instance b = 2, 3 ferromagnetic, or the antiferromagnetic side near b |lambda_2| = 1/sqrt(b)).
3. Prove what you can, with complete proofs: KS tightness for q = 3 at a new range of b (small b, explicit constants in Sly's
   expansion), the antiferromagnetic side, census versus full reconstruction, or improved non-reconstruction bounds via a
   contraction / mutual-information argument with explicit numbers for b = 2, 3, 4. A rigorous computer-assisted interval
   argument for a specific b is acceptable if the code and the error control are complete.
4. Compute (evidence only). Population dynamics for the distributional fixed point on T_b, b = 2..6, both signs, to locate the
   reconstruction threshold numerically and compare with b lambda_2^2 = 1.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem C0101. Source: L. Levine and Y. Peres, "Laplacian growth, sandpiles and scaling limits", Bull. AMS 54 (2017),
arXiv:1611.00411, open problem (4), p. 27: describe the maximal elements of the set Gamma(Z^d) of integer superharmonic
matrices for d >= 3: are they isolated, and do they have rational entries? (For d = 2, Levine-Pegden-Smart showed the
maximal elements correspond to the circles of the Apollonian band packing and are rational.) Gamma(Z^d) = set of real
symmetric d x d matrices A such that there is g: Z^d -> Z with g(x) >= x.Ax/2 + b.x + c pattern... read the source and
Levine-Pegden-Smart (Annals 2017 "Apollonian structure in the abelian sandpile"; and "The Apollonian structure of integer
superharmonic matrices") for the exact definition (g integer-valued, discrete Laplacian Delta g <= 1, g - x.Ax/2 bounded
below / periodic), and the role of these matrices in the sandpile scaling limit.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1611.00411 and the two Levine-Pegden-Smart papers (arXiv:1309.3267, arXiv:1608.00064) into
   sources/ (text only, no page images). Search 2016-2026 for work on Gamma(Z^d) for d >= 3, higher-dimensional sandpile
   scaling limits, integer superharmonic matrices, Pegden-Smart "stability of patterns in the abelian sandpile", Kalinin-
   Shkolnikov tropical sandpiles, and anything citing LPS on d >= 3. If the question is answered in print, give the exact
   reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Algorithms. Implement the LPS-style test of membership A in Gamma(Z^d) for d = 3 (via periodic odometer / the
   "obstacle" characterisation, or by searching for periodic integer superharmonic g of small period), validate on d = 2
   by reproducing the Apollonian circle picture and known rational maximal points.
3. Explore d = 3 on low-dimensional slices (e.g. diagonal matrices diag(a,b,c), and 2-parameter families), locate the
   boundary of Gamma(Z^3), find candidate maximal elements and test isolation and rationality numerically (high
   precision / exact rational periodic certificates g of period N certify membership exactly).
4. Prove what you can: e.g. rationality or isolation of explicit maximal elements found, a structural statement
   (lifting of 2D maximal elements to 3D, block-diagonal constructions), or a counterexample (a non-isolated maximal
   element or an irrational one), with exact certificates.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof or certificate, what was checked and how, and the literature result. Keep LOG.md as you go.
Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere,
no pushes.

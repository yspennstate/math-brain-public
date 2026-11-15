You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem C0101, L. Levine and Y. Peres, "Laplacian growth, sandpiles and scaling limits", Bull. AMS 54 (2017), 355-382,
arXiv:1611.00411, open problem (4), p. 27: describe the maximal elements of the set of integer superharmonic matrices
Gamma(Z^d) for d >= 3; are they isolated, and do they have rational entries? The claim says COUNTEREXAMPLE in a qualified
sense: for literal Loewner maximality there are irrational, non-isolated maximal elements in every d >= 3, built from the
residual trace-zero points of the two-dimensional Apollonian band packing (Levine-Pegden-Smart, Annals 186 (2017),
arXiv:1309.3267v4, Theorem 1.1 and the paragraph after it) and a "zero-coordinate reduction" to higher d, with the explicit
point t = sqrt(sqrt5 - 2), a = 1 - t, b = sqrt(sqrt5 + 2) - 1. It says the survey's intended notion (circle-type cone peaks)
is not settled. It also says the published Annals Theorem 1.1 prints 2 where v4 of the arXiv version has 0 in the trace
half-space.

Break it if it is wrong.
1. Download arXiv:1611.00411, arXiv:1309.3267 (v4 and the earliest version) and arXiv:1208.4839 into sources/ as plain text.
   Read open problem (4) and Section 6 of the survey exactly, and Theorem 1.1, Theorem 1.2, Lemma 3.4 and the paragraph after
   Theorem 1.1 in LPS. State which notion of "maximal" the survey uses, in its own words, and whether the literal reading the
   claim answers is the one a reader of the survey would take.
2. Check the normalization (Delta g <= 1 versus stable height 2d-1, the shift by S = diag(2,1,1)), the trace half-space
   (0 versus 2), and whether residual trace-zero points really are Loewner maximal in d = 2. If they are, the d = 2 statement
   "maximal elements correspond to circles" is already false in the literal sense; say so and say whether LPS say it.
3. Check the zero-coordinate reduction line by line: that the d-dimensional matrix built from a 2D residual point lies in
   Gamma(Z^d), that it is maximal in Gamma(Z^d) (every PSD improvement, including ones that touch the extra coordinates), that
   it is irrational and not isolated. Check the exact algebra for the explicit point (that it lies on the residual set, not on
   or inside any circle) independently, with your own code (do not reuse claim_files/code), e.g. by exact field arithmetic in
   Q(sqrt5, t) and a separate high-precision check against many packing circles.
4. Verdict on value: is this a genuine answer to open problem (4), a remark about terminology, or wrong? What exactly remains
   open (isolation and rationality of the peaks / circle-type maximal elements in d >= 3)?
5. Literature: has open problem (4) been answered in print (2017-2026 papers citing 1611.00411 or 1309.3267: Pegden, Smart,
   Levine, Bou-Rabee, "integer superharmonic matrices" in three dimensions, "sandpile shapes", Kim-Wang)?
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

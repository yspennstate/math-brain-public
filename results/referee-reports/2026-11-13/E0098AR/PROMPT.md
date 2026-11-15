You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem E0098, from S. O'Rourke, V. Vu and K. Wang, "Eigenvectors of random matrices: a survey" (JCTA 144 (2016); arXiv:1601.03678v3,
PDF p. 13, after Corollary 4.8): is the limiting distribution of the minimum absolute coordinate ||v_j(W)||_min of a real Wigner
eigenvector universal, or does it depend on the atom variables? The claim is PARTIAL. It proves n^{3/2} min_k |v_{j_n}(k)| -> Exp(sqrt(2/pi))
and a Poisson-process version for GOE for every deterministic index sequence; it gives a construction showing that Gaussian convergence
of every sublinear set of coordinates (even in total variation) does not imply the law; it says the missing input for subgaussian Wigner
matrices is a relative small-ball estimate at scale n^{-3/2}, and that no printed theorem gives the law for general atoms.

Break it if it is wrong.
1. Get arXiv:1601.03678 into sources/ as plain text and state the question and Corollary 4.8 exactly. Check the claim's reading
   (rescaling, index regime) is fair.
2. Check the GOE proof line by line (Haar eigenvector = normalised Gaussian vector, independence of the norm, the minimum of n
   half-normals, the constant sqrt(2/pi), the Poisson version). Is this already in print (it may be classical)? Say where.
3. Check the obstruction construction: is it a valid counterexample to the implication it claims to refute? Are its hypotheses
   really the strongest known Gaussian-approximation statements, so the obstruction says something?
4. Write your own independent code (do not reuse claim_files/code): simulate GOE and a Rademacher Wigner matrix (n up to 2000 or so,
   bulk and edge indices) and compare the law of n^{3/2} min_k|v_j(k)| with Exp(sqrt(2/pi)). For Rademacher also look at whether a
   coordinate can be exactly zero with non-negligible probability (sign symmetries, small n), which would break universality.
5. Literature 2016-2026: Bourgade-Yau, Benigni, Benigni-Lopatto, Marcinek-Yau, Cipolloni-Erdos-Schroder, and any paper on "minimum
   coordinate", "no-gaps delocalization", "smallest eigenvector entry" for Wigner matrices (Rudelson-Vershynin no-gaps delocalization;
   Luh-O'Rourke; Nguyen-Tao-Vu). Is universality of the minimum proved or refuted in print?
6. Verdict on value: correct or not, novel or not, exactly what is proved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

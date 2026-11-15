You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem C0133, E. Kosygina and M. P. W. Zerner, "Excited random walks: results, methods, open problems", Bull. Inst.
Math. Acad. Sin. (N.S.) 8 (2013), 105-157, arXiv:1204.1895, Problem 4.7: for excited random walks on Z^d with i.i.d. elliptic
cookie environments (arbitrary, possibly infinite stacks) and a direction l, does X_n . l / n -> 0 a.s. on the complement of
{|X_n| -> infinity}? The claim says yes, in full generality, by a finite-history bound at fresh hyperplanes combined with
the deterministic counting Lemma 3 of Zerner (Electron. Commun. Probab. 7 (2002) 191-197), and notes d = 1 is in print
(Amir-Berger-Orenshtein 2016).

The run took about twenty minutes. Treat that as a reason to look harder. Break it if it is wrong.
1. Download arXiv:1204.1895 and Zerner 2002 into sources/. Read Problem 4.7 and its surroundings exactly: the class of
   environments, the ellipticity notion, and what the authors say makes it hard. Check the claim answers the question as posed,
   with no hidden extra hypothesis (uniform ellipticity, bounded stacks, independence within a stack, finite cookies).
2. Check every step line by line. In particular: the reduction of N to {some site visited i.o.}; the "fresh hyperplane" bound
   (what is independent of what? cookie walks are not Markov in position, so every renewal / restart / strong-Markov step must
   be justified with the full history, and the i.i.d.-over-sites structure must be used correctly: a site's stack is fresh only
   if the site was never visited); whether Zerner's Lemma 3 applies verbatim (state its hypotheses and check each one); the
   passage from the counting bound to X_n . l / n -> 0 a.s. on N (not just liminf). Name any step that would also "prove"
   something known to be false, e.g. test the argument against RWRE in Z^d (where the analogous statement is Zerner's theorem)
   and against environments that are not i.i.d.
3. If the argument is right, say whether it is essentially Zerner 2002 transferred (and whether the survey's authors would have
   seen that), and what the genuinely new step is.
4. Independent code (do not reuse claim_files/code): simulate an excited walk in d = 2 with infinite stacks that push hard in
   one direction but are recurrent-ish (e.g. stacks with drift alternating in long blocks), estimate P(N) and the speed on N.
   Numerics are a sanity check only.
5. Literature: is Problem 4.7 answered in print (2012-2026 papers citing 1204.1895, Holmes, Holmes-Salisbury, Menshikov-Popov-
   Ramirez-Vachkovskaia, Kosygina-Zerner directional transience, Berard-Ramirez, Peterson)? Say precisely what is new.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Work only in
this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.

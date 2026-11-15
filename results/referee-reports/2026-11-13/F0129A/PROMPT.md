Open problem F0129. Source: R. Pemantle, "A survey of random processes with reinforcement" (Probability Surveys 4 (2007);
arXiv:math/0610076), Section 6.1 "Drift as a function of occupation measure", PDF p. 57: the Durrett-Rogers conjecture. For the
self-repelling Brownian polymer X_t = B_t + int_0^t ds int_0^s du f(X_s - X_u) in one dimension, if f is compactly supported, odd,
with x f(x) >= 0, then X_t / t -> 0 almost surely. (Durrett-Rogers 1992 proved limsup |X_t|/t <= C for compactly supported f, and
X_t/t -> c > 0 when f >= 0 and f(0) > 0.) Read the source for the exact wording and for any further Durrett-Rogers conjectures on
the same page (growth rate t^{2/3}).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and state the conjecture exactly. Search: Durrett-Rogers
   ("Asymptotic behavior of Brownian polymers", PTRF 1992), Cranston-Le Jan, Cranston-Mountford ("The strong law of large numbers
   for a Brownian polymer", Ann. Probab. 1996), Mountford-Tarres ("An asymptotic result for Brownian polymers", AIHP 2008),
   Tarres-Toth-Valko ("Diffusivity bounds for 1d Brownian polymers", Ann. Probab. 2012), Horvath-Toth-Veto ("Diffusive limits for
   true (or myopic) self-avoiding random walks and self-repellent Brownian polymers in d >= 3"; "Relaxed sector condition"),
   Toth-Werner (true self-repelling motion), Benaim-Ciotir-Gauthier (self-interacting diffusions), Kleptsyn-Kurtzmann, Gauthier,
   Chambeu-Kurtzmann, and 2007-2026 work. Determine exactly which cases are proved (f(x) = sign(x) on [-1,1]? general compactly
   supported odd f? X_t/t -> 0 a.s., or the sharper t^{2/3} order?). If a printed theorem proves the conjecture as stated (all
   compactly supported odd f with x f(x) >= 0), give the theorem and page and stop with RESOLVED_IN_LITERATURE; if only special f,
   say which.
2. Understand: the mechanism (the local time profile L_t(x) acts as a potential via the drift -(f' * L_t)? write the drift as
   int f(X_t - y) L_t(dy)), why the odd symmetric case should give zero speed (no persistent asymmetry of the occupation profile in
   front of and behind the particle), and where the known proofs use the special form of f.
3. Prove what you can, with complete proofs: extend the known result to a larger class of f (for example odd f with x f(x) >= 0
   that are nonincreasing in |x| on the support, or f with finitely many sign-definite pieces), or prove a weaker statement for
   all such f (for example liminf |X_t|/t = 0 a.s., or E|X_t| = o(t)).
4. Compute (evidence only): simulate the polymer (Euler scheme with the local time on a grid) for several odd f, up to t large,
   and look at X_t/t and the growth exponent.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

Open problem D0027. Source: "Long time behaviour of one facilitated kinetically constrained models: results and open problems",
arXiv:2510.20461, Conjecture 2, Section 1.1, PDF p. 2: for FA-1f on Z, if there is kappa > 0 with
nu(no infected vertices in [-l, l]) = O(exp(-kappa l)) for all large l, then for every q > 0 (q in (0,1), the equilibrium
density of empty/infected sites; read the source for the exact convention) and every local function f, E_nu(f(eta(t))) converges
to pi(f) exponentially fast. (Read the source for the exact statement: the class of initial laws nu, whether nu is a product
measure or general, the class of f, what is already proved - the authors say it is proved for special initial laws - and the
related Conjecture 1 / D0026 on convergence from any law with infinitely many infected sites.)

Do this, in order, saving as you go:
1. Literature first. Download arXiv:2510.20461 into sources/ (plain text only) and read Section 1 and the proofs of the special
   cases. Search for the relevant tools and any resolution: Blondel-Cancrini-Martinelli-Roberto-Toninelli "Fredrickson-Andersen
   one spin facilitated model out of equilibrium" (2013); Mountford "Exponential convergence for attractive subcritical
   processes"; Cancrini-Martinelli-Schonmann-Toninelli "Facilitated oriented spin models: some non equilibrium results"; Chleboun-
   Faggionato-Martinelli "Relaxation to equilibrium of generalized East processes on Z^d"; Ertul; Ganguly-Lubetzky-Martinelli
   "Cutoff for the East process"; Pillai-Smith on FA-1f mixing; Hartarsky; Mareche; Blondel 2013 front propagation; and anything
   2025-2026 citing 2510.20461. If it is answered in print, give the exact reference and theorem and stop with REPORT.md first
   line RESOLVED_IN_LITERATURE.
2. Understand the gap. Explain precisely which property of the special initial laws the existing proofs use (product structure,
   a density lower bound, a uniform positive density of infection in every window, coupling with equilibrium) and why the
   exponential-gap hypothesis alone is harder (correlations in nu, the time to fill a large initial gap, the distinguished-zero
   argument).
3. Prove what you can, with complete proofs: the conjecture itself; or the conjecture for q above some threshold, or for nu
   satisfying the gap hypothesis plus a weak mixing condition, or for f supported near the origin with a stretched-exponential
   rate; or a counterexample law nu satisfying the hypothesis for which relaxation is slower than exponential, if the
   conjecture is false. Use the distinguished-zero / front-propagation and spectral-gap-on-boxes methods from the literature.
4. Compute (as evidence only). Simulate FA-1f on Z from a correlated initial law with exponentially rare gaps (for instance a
   renewal process with geometric gaps, and a hidden-Markov law), measure E(f(eta(t))) - pi(f) for a local f, and fit the decay.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

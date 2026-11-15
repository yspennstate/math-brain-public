Open problem D0026. Source: "Long time behaviour of one facilitated kinetically constrained models: results and open problems",
arXiv:2510.20461, Conjecture 1, Section 1.1, PDF p. 2: for the Fredrickson-Andersen one-spin facilitated model (FA-1f) on Z with
equilibrium density q in (0,1) of infected/empty sites, for every q and every local function f, E_nu(f(eta(t))) -> pi(f) as
t -> infinity, provided nu(there is at least one infected vertex) = 1; pi is Bernoulli(q) product measure. (Read the source for
the exact statement and conventions: general nu or product/translation-invariant nu, what is already proved and for which
special initial laws, and the related Conjecture 2 / D0027 on exponential rates under an exponential gap hypothesis. A sibling
run on D0027 is in progress elsewhere; do not coordinate with it, work independently.)

Do this, in order, saving as you go:
1. Literature first. Download arXiv:2510.20461 into sources/ (plain text only) and read Section 1 and the proofs of the special
   cases. Search for the relevant tools and any resolution: Blondel-Cancrini-Martinelli-Roberto-Toninelli "Fredrickson-Andersen
   one spin facilitated model out of equilibrium" (Markov Process. Related Fields 2013); Cancrini-Martinelli-Schonmann-Toninelli;
   Mountford "Exponential convergence for attractive subcritical processes" (and why FA-1f is not attractive); Ertul "Cutoff for
   the non reversible SSEP with reservoirs" and Ertul's FA-1f out-of-equilibrium work; Blondel "Front progression in the East
   model" and "Fredrickson-Andersen one spin facilitated model: front propagation"; Hartarsky; Mareche "Combinatorics for general
   kinetically constrained spin models"; Chleboun-Faggionato-Martinelli; Pillai-Smith; Shapira; anything 2025-2026 citing
   2510.20461. If it is answered in print, give the exact reference and theorem and stop with REPORT.md first line
   RESOLVED_IN_LITERATURE.
2. Understand the gap. Explain which property of the special initial laws the existing proofs use (positive density of zeros,
   product structure, a distinguished zero that persists, renewal structure), and what can go wrong for a general nu with a
   single infected site somewhere (e.g. nu concentrated on one infection at the origin in an otherwise healthy line: does the
   infected region spread linearly, and does the local law near the origin converge to pi?). Treat the single-infection initial
   condition and the case of infinitely many infections separately.
3. Prove what you can, with complete proofs: the conjecture; or the conjecture for the one-infection initial law delta-type
   configurations; or for q above a threshold; or for nu translation invariant (or ergodic) with nu(some infection)=1; or for f
   supported near a persistent zero. Or a counterexample nu if the conjecture is false. Use the distinguished-zero / front
   propagation, spectral gap on boxes and coupling arguments from the literature.
4. Compute (as evidence only). Simulate FA-1f on a large interval from (a) a single infected site, (b) sparse random infections
   with density decaying away from the origin, measure E(f(eta(t))) - pi(f) for local f near the origin and the spreading of the
   infected region, and report the observed behaviour.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

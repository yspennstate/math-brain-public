P0177: mode of classical and free Brownian motion at large time (Hasebe-Ueda Problem 4.6).

Paper, programs and Lean file: https://github.com/yspennstate/brownian-mode-location (main 185b844a15e23e16927bd8f26947e045d07cd65d, revision of 12 Nov 2026 on the 5 Nov paper).
Here: the independent referee's prompt, log and report (Codex gpt-6.1-sol, Mac mini 1, 12 Nov 2026) and the verification note written into the ledger row (open-problems-repo master ff91b693).

## Credits

The question is Problem 4.6 of Hasebe and Ueda, "Large time unimodality for classical and free Brownian motions with
initial distributions" (ALEA 2018, arXiv:1710.08240), and the paper uses their unimodality theorems (Theorems 3.2 and
4.3) and their form (Section 2.2) of Biane's 1997 description of the free convolution with a semicircle law. Free
convolution of measures with unbounded support is due to Bercovici and Voiculescu (1993), and free cumulants are used
as in the lectures of Nica and Speicher (2006). The first term of the classical expansion is the relation between
mean, mode and third cumulant studied by Haldane (1942), and by Hall (1980) for sums of independent random variables;
asymptotic expansions in the free central limit theorem are due to Chistyakov and Götze (2013). Related unimodality
results are due to Ibragimov (1956), Hasebe and Thorbjørnsen (2016), Hasebe and Sakuma (2017) and Hasebe, Ueda and
Wang (2022). The checks use SymPy and mpmath, and the Lean file uses Lean 4 and mathlib. Full references are in the
paper.

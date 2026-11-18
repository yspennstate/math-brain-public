Independent referee pass on the public paper variation-threshold-stationary-times (P0243, Aldous-Fill Open Problem 4.48), 12 Nov 2026.
Verdict SOUND; wording edits in public commit e311262a7e36aaf443d4aec19a628bc559e0bccb; Zenodo 10.5281/zenodo.24148645; ledger master 63ebc3eb464988a52be126c2ea871212385ff4b5.
referee/ holds the prompt, report and log; ledger_update.json is the ledger row's new fields.

## Credits

The question is Open Problem 4.48 of Aldous and Fill, "Reversible Markov Chains and Random Walks on Graphs"
(monograph, 2002, recompiled 2014), which asks whether the variation threshold is at most the average hitting time
(Kemeny's constant) and whether the relaxation time is at most the least mean of a stationary stopping time from the
worst start. The comparison of these parameters goes back to Aldous (1982), the average hitting time is studied by
Kemeny and Snell (1960), and stopping times that reach a given law in least mean by Lovász and Winkler (1995). The
paper recalls a theorem of Hermon (arXiv:2304.05878, Theorem 1.1): up to an absolute constant factor, the relaxation
time is the largest expected hitting time of a set A with pi(A) >= 1/2 for the chain started from pi conditioned on
the complement of A. The Lean file is checked with Lean 4 and mathlib. Full references are in the paper.

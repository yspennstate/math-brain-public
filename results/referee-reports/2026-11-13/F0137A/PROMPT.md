Open problem F0137. Source: C. Sabot and L. Tournier, "Random walks in Dirichlet environment: an overview" (2016),
arXiv:1601.08219, Section 6.1, PDF p. 19, the sentence after Corollary 2: for the random walk in Dirichlet environment (RWDE)
on Z^d, d >= 2, with weights alpha_1, ..., alpha_{2d} > 0, drift d_alpha = sum alpha_i e_i and
kappa = 2 sum alpha_i - max_i (alpha_i + alpha_{i+d}), Corollary 2 says: if d_alpha . l > 0 and the sufficient condition (6.1)
for Sznitman's condition (T)^gamma holds, then the renewal times in direction l satisfy E[tau_1^s] < infinity iff s < kappa.
Conjecture: (T)^gamma holds whenever d_alpha != 0 (so the renewal-moment statement holds for every directionally transient
RWDE). Read the source for (6.1), the definition of (T)^gamma, and the proofs it cites.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1601.08219 into sources/ (plain text only) and read Sections 4-6 exactly. Read Bouchet-Ramirez-
   Sabot ("Sharp ellipticity conditions for ballistic behavior of random walks in random environment", Bernoulli 2016),
   Fribergh-Kious ("Local trapping for elliptic random walks in random environments in Z^d", PTRF 2016), Campos-Ramirez
   ("Ellipticity criteria for ballistic behavior of random walks in random environment", PTRF 2014), Berger-Drewitz-Ramirez
   (effective polynomial ballisticity), Guerra-Ramirez, Perrel-Sabot (2025, invariant measure for the environment viewed from
   the particle under (T'), with a conjecture to remove it), Tournier (integrability of exit times), Bouchet (sub-ballistic
   RWDE), and 2016-2026 work citing 1601.08219 or proving (T)^gamma / (T') for Dirichlet environments. Note: a closely related
   run (F0136, d=2 ballisticity for kappa > 1) found Perrel-Sabot 2025 Theorem 2.3 and its Conjecture 1; check whether any
   paper proves (T)^gamma for all d_alpha != 0, or for d >= 3. If the conjecture is proved in print, give the exact reference
   and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. State (6.1) exactly and the region of alpha it covers; explain why (T)^gamma is a statement about
   slab-exit probabilities and why Dirichlet traps (finite edges with large weights) are the obstruction; compute exactly
   what part of the parameter space (6.1) leaves out, for d = 2 and d = 3.
3. Prove what you can, with complete proofs: (T)^gamma on a larger explicit region than (6.1) (for instance via the
   time-reversal / statistical invariance of Dirichlet environments under reversal of the drift, the Sabot-Tournier trap
   decomposition, or an effective criterion of Berger-Drewitz-Ramirez checked on a finite box with an explicit bound), or the
   renewal-moment equivalence s < kappa without (T)^gamma in a restricted case, or a precise reduction.
4. Compute (evidence only). Simulate RWDE in d = 2 and 3 for alpha outside (6.1) with d_alpha small, estimate slab-exit
   probabilities against the stretched-exponential (T)^gamma rate and the tail of renewal times.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.

# Voter 3 (rigor and verifiability)

VOTE: Hasebe-Ueda (ALEA 2018) Problem 3.3: the optimal C with mu boxplus S(0,t) unimodal for all t >= C D_mu^2

RUNNER-UP: Agresti-Veraar (2025) Problems 4, 5, critical Allen-Cahn

## Justification

A result is as strong as its weakest unproved step, and Hasebe-Ueda 3.3 is the only unpublished
candidate with no weak step. All three referees re-derived both proofs line by line and called every
inequality CLEAN; B and A each ran an independent scan (no separating minimum below 1.1285 over
430,000 pairs, min F = 1.0000); the extremal law is identified with a rigidity statement. The
load-bearing mathematics is two real-polynomial inequalities on a box (Lemma A: Psi >= 0 forces
s <= 3D^2/4; Lemma B: Phi >= 0 for s <= 3/4, D <= 1) plus a textbook Choquet step, so the Lean core
can be essentially the whole argument (nlinarith/polyrith), not an arithmetic fragment. Prior-art
risk is low on the free side (two searches, nothing); the classical D^2/4 companion must be cited as
known, not claimed.

Janson 20.2 is more important, but part (b) rests on Theorem B, a sketch whose stated growth
condition Reviewer A showed is insufficient (needs log n_r >> (log n_{r-1})^2), and it has no
formalisable core; that is not a paper this month. RRT layers is complete but is two citations plus an
identification. Agresti-Veraar is the runner-up: an exact BES(4) reduction re-derived by all three,
a manuscript and partial Lean already exist, low prior-art risk, importance at least equal; it loses
only because its core is stochastic calculus (Lean covers the algebra alone) and the Theorem 6.4
scope sentence is still unwritten.

Biggest risk: the entire proof runs through the source's Lemma 3.1 (unimodality iff every level set
of xi_R has at most two points), which no reviewer read from the PDF; if that criterion is
misquoted, or D_mu is normalised differently than assumed, the constant is wrong.

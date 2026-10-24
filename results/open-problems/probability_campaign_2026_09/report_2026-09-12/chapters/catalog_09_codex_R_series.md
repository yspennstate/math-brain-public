## Catalogue chapter 9: the R series, questions the literature had already answered

Seven rows of the Codex ledger carry an R identifier rather than a P. They are questions that a source
poses as open and that the later literature has since resolved, so none of them is admitted as an open
problem, and no attempt was made on any of them. They belong in this report for one reason: the work
of finding out that a question is spent is part of what the campaign produced, and a reader who wants
to continue should not spend a week on a problem that was settled in 2022.

Each row records the source and locator, the source's own claim that the question is open, and the
evidence that resolved it. The statements themselves were not extracted into the ledger for these
rows, so what follows states each question in the compiler's words rather than the source's, which is
a weaker record than the rest of the catalogue and is flagged as such here.

The verification words on these rows are worth reading carefully. Four of them say
`primary_status_evidence_not_full_proof_review`, two say
`exact_resolution_statement_checked_not_full_proof_reproduced`, and one says
`primary_theorem_statement_checked_not_independent_proof_review`. In every case the resolving paper's
statement was read and its proof was not. That is the right standard for an exclusion decision and it
is not a review of the resolving work.

### R0001. The complete bunkbed inequality

Source: Grimmett, *Selected problems in probability theory* (`grimmett_2022_selected`), Conjecture 4.1,
PDF page 8. The source states it as open.

The bunkbed conjecture asks, of a graph with two copies of itself joined by vertical edges, whether a
vertex is at least as likely to be connected to the copy of a vertex on its own level as to the
corresponding vertex on the other level. The complete form asserts this for every graph and every
edge-probability assignment.

Recorded status: resolved in the literature, `literature_counterexample`, with the resolving statement
at Theorem 6.1, PDF page 8 of the resolving document. Verification:
`exact_resolution_statement_checked_not_full_proof_reproduced`. The ledger does not name the resolving
authors in its own fields, so this report does not either; the locator is what was checked. Not
admitted.

### R0002. Extinction of one-dimensional Brownian snails

Source: Grimmett, `grimmett_2022_selected`, Question 6.1(i), PDF page 10, stated as open.

The question asks whether the one-dimensional Brownian snail model dies out.

Recorded status: resolved in the literature, `literature_solution`, resolved by Hartarsky and Lichev,
Theorem 1.1, PDF page 3, in *Electronic Communications in Probability* 28 (2023), article 45.
Verification: `exact_resolution_statement_checked_not_full_proof_reproduced`. Not admitted. This is one
of the two R rows where the ledger names the resolving paper in full.

### R0003. Schramm's locality conjecture for critical percolation

Source: Lyons and Peres (`lyons_peres_20260819`), Conjecture 7.45, stated as open.

The conjecture says that the critical percolation probability is a local quantity: if a sequence of
transitive graphs converges locally to a limit graph, and the critical probabilities stay away from
one, then the critical probabilities converge to that of the limit.

Recorded status: resolved in the literature, `literature_resolution`, with the evidence recorded as
"Theorem 1.1; abstract checked; 2023 preprint". Verification:
`primary_status_evidence_not_full_proof_review`. The ledger records neither the resolving authors nor a
page locator, only the theorem number, the year and that the abstract was read. Anyone relying on this
exclusion should pin the reference properly first. Not admitted.

### R0004. Generating-set invariance of free uniform-forest connectivity

Source: Lyons and Peres, `lyons_peres_20260819`, Question 10.50, stated as open.

The question asks whether the connectivity of the free uniform spanning forest of a Cayley graph is
independent of the generating set chosen.

Recorded status: resolved in the literature, `literature_resolution`, evidence recorded as "abstract
and author institutional version; *Annals of Probability* 2022". Verification:
`primary_status_evidence_not_full_proof_review`. Not admitted.

### R0005. Analyticity of the biased-walk speed on leafless Galton-Watson trees

Source: Lyons and Peres, `lyons_peres_20260819`, Question 17.34, stated as open.

The question asks whether the speed of the biased random walk on a leafless Galton-Watson tree is an
analytic function of the bias.

Recorded status: resolved in the literature, `literature_resolution`, with the evidence recorded as
"Question 17.34 immediately following sentence; original theorem conditions still to verify".
Verification: `primary_status_evidence_not_full_proof_review`. That evidence field is the weakest of
the seven: the resolution was read off the sentence that follows the question in the source itself, and
the conditions of the theorem it points to were not checked. Treat this row as an exclusion that still
needs its citation check rather than a settled one. Not admitted.

### R0006. A harmonic dimension lower bound by expected log offspring

Source: Lyons and Peres, `lyons_peres_20260819`, Question 17.28, stated as open.

The question asks for a lower bound on the harmonic dimension of a Galton-Watson tree in terms of the
expected logarithm of the offspring distribution.

Recorded status: resolved in the literature, `literature_resolution`, evidence "Theorem 1; primary
theorem statement checked". Verification: `primary_status_evidence_not_full_proof_review`. Not admitted.

### R0007. The exact quarter threshold for Gaussian ellipsoid fitting

Source: `randomstrasse_2024_v1`, Conjecture 6, PDF pages 4 to 5, stated as open.

The conjecture concerns the threshold at which a random Gaussian point set can be fitted by an
ellipsoid, and asserts that the threshold is exactly one quarter in the relevant ratio.

Recorded status: a resolution is claimed in recent primary preprints and the row is excluded pending
review, `literature_claim_excluded_pending_review`. The evidence recorded is Misiakiewicz and Wen,
Theorem 1.2, PDF page 2, giving both exact feasibility below one quarter and unrestricted infeasibility
above it, with the note that the statement was read and the 47-page proof was not reviewed.
Verification: `primary_theorem_statement_checked_not_independent_proof_review`. Not admitted, and of
the seven this is the row whose exclusion rests on the freshest and least reviewed claim.

### What the R series says about the corpus

Seven rows out of 1,025 is a low rate of already-answered questions for a corpus built from
open-problem lists, and three of the sources responsible are recent lecture notes and problem
collections whose own status claims were years old when they were written. Two independent facts from
elsewhere in the campaign point the same way: intake G found that three of the twelve candidate sources
it examined resolved earlier rows rather than posing new ones, and the 8 September session found that
the literature had already settled Aldous and Fill Open Problem 6.14 and all seven Haggstrom and
Rosenthal central limit theorem problems. The corpus contains more spent problems than the seven
recorded here, and finding them is cheaper than attacking them. Chapter 14 makes that a priority item.

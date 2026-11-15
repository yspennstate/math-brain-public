# Intake I, 14 September 2026

One hundred and seventeen records from thirty-four sources: one hundred and four open problems and
thirteen records of problems already closed. They came from five sweeps. The open count was first
written as one hundred and six; a later pass over every row for the phrases with which a paper
announces its own answer caught two labels cut from sentences their sources resolve in the next line,
and both were withdrawn from the open count and kept as rows so neither is attempted again.

1. **September 2026 arXiv probability papers** (19 records, 14 open): the randomly oriented Manhattan
   lattice, parking and the divisible sandpile, sloped height functions, the maximum relaxation time of
   a random walk on regular graphs, collisions on comb graphs, and the central limit theorem for
   rho-mixing sequences.
2. **The end of Janson's 2012 survey** (3): Problems 20.3, 20.4 and 20.11, which none of the six earlier
   ledgers carried; two are answered in the campaign's memo of 14 September.
3. **Aldous and Fill** (13, three of them already resolved): every numbered open problem in the monograph
   extracted, 31 distinct, and compared with the 21 rows the campaign had.
4. **Four more of the campaign's largest sources** (27): Schramm's problem collection (9), van der
   Hofstad's Saint-Flour notes (6), the beta-splitting overview (4), Lyons and Peres (5) and the
   first-passage percolation survey (3).
5. **Every remaining source with local text** (55): the sweep was made mechanical and run over all 191
   sources that have a local copy, matching numbered labels against the locator numbers already carried.
   The largest finds were the Randomstrasse lists of 2024 and 2025 (15), the Agresti and Veraar SPDE
   problem lists (11) and Salez's Markov notes (7).

Two sources were excluded by hand after inspection: the recursive distributional equation survey, whose
local text carries its index lines rather than its statements, and a 2026 note whose labelled conjectures
are ones it reports counterexamples to.

## How these differ from intake H

Intake H's statements were gathered by a lookup agent from abstracts and its rows carry the warning
that they were "NOT yet checked against the paper". Every statement here was read from the paper: the
PDF was fetched from arXiv, the text extracted, the passage located, and the wording quoted from it.
The locator names the section, theorem, remark or problem number the quote comes from. What is *not*
done is a literature search for a later resolution, so the open status is the source's own, as of its
posting date.

## The sources

| arXiv | paper | rows |
| --- | --- | --- |
| 2609.07621 | Bou-Rabee and Peres, the randomly oriented Manhattan lattice in 2D is transient | I0001-I0004, I0019 |
| 2609.02820 | Bou-Rabee and Panagiotis, sharpness and critical scaling of parking | I0005, I0006, I0018 |
| 2609.01499 | Adhikari, Gheissari and Peled, rigidity of sloped height functions in d >= 3 | I0007-I0009 |
| 2609.06818 | the maximum relaxation time of a random walk on regular graphs | I0010, I0011, I0015 |
| 2609.05343 | the phase transition for the number of collisions on comb graphs | I0012 |
| 2609.04638 | improvement of the central limit theorem for stationary rho-mixing sequences | I0013, I0014 |
| 2609.00399 | Liu, Shannon's problem and a conjecture of Tao | I0017 |
| 2609.07819 | Brown, Rosenthal and Zhou, Markov chain CLTs | I0016 |

## Why the resolution rows are here

Three of them close problems from lists the campaign already mines. I0015 is Aldous and Fill's Open
Problem 6.14, the spectral gap conjecture for regular graphs, proved on 30 August 2026; the Aldous and
Fill list is one of the campaign's main sources, so the row exists to stop the problem being attempted
again. I0016 records that all seven of Häggström and Rosenthal's open problems on Markov chain central
limit variances were resolved on 7 September 2026, and that one of the seven was worked out in an
extended interaction with a language model, with the authors taking responsibility for the arguments.
I0017 is Tao's 2010 discrete entropy monotonicity conjecture, proved on 31 August 2026. I0019 is the
transience of the randomly oriented Manhattan lattice, whose proof is formalised in Lean 4 with no use
of `sorry`.

## Status of every row

All but four of the open rows are `not_attempted`. The exceptions are I0020 and I0021, the two problems
from the end of Janson's survey that the campaign's memo of 14 September answers; I0022, which carries a
literature status; and I0026, Aldous and Fill's Open Problem 4.49, which carries the evidence of an
exhaustive search (the ratio it asks to be bounded has maximum exactly 2 over all connected graphs on
four to seven vertices, attained by the complete graphs).


## The Aldous and Fill gap

The monograph is the campaign's most-mined source, and thirteen of its numbered open problems were in
no row: 2.34, 3.44, 4.38, 4.49, 6.13, 6.35, 7.26, 7.30, 7.31, 8.23, 14.12, 14.29, 14.31. Three of the
thirteen had been settled long before the campaign began, which is worth knowing on its own:

- 4.38, whether the relaxation time is bounded by a constant times $\sup_A \pi(A)E_\pi T_A/\pi(A^c)$,
  was resolved by Hermon, *Relaxation times are stationary hitting times of large sets*, arXiv:2304.05878
  (2023), whose abstract says it "resolves a conjecture of Aldous and Fill".
- 7.26, the cover time of the two-dimensional torus, was resolved by Dembo, Peres, Rosen and Zeitouni,
  Ann. of Math. 160 (2004), whose $(2N\log N)^2/\pi$ is the source's $(1/\pi)n\log^2 n$ at $n = N^2$.
- 14.29, whether the interchange process has the same relaxation time as the single-particle walk, is
  Aldous's spectral gap conjecture, proved by Caputo, Liggett and Richthammer, J. Amer. Math. Soc. 23
  (2010).

The other ten are carried as open per the source, with no resolution search run.

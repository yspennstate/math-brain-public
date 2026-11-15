Open problem D0034. Source: R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open questions",
Probab. Surveys 2 (2005), 107-144, arXiv:math/0511078, Question 6 (Section 3, PDF p. 16): does there exist a strictly
stationary psi-mixing (or perhaps even 1-dependent) sequence which cannot be represented as an instantaneous function of a
strictly stationary, Harris recurrent Markov chain? Read the survey for the exact setting and answer exactly as posed.

Do this, in order, saving as you go:
1. Literature first. Download arXiv:math/0511078 into sources/ and read Section 3 around Question 6 (what Bradley proves
   about representations by Harris chains, e.g. the Berbee/Bradley results for absolutely regular sequences). Search later
   work: 1-dependent processes that are not block factors (Aaronson-Gilat-Keane-de Valk 1989, Burton-Goulet-Meester 1993,
   Holroyd-Liggett finitely dependent colorings), hidden Markov / functions of Markov chains representability, Bradley's
   later surveys and books (Introduction to Strong Mixing Conditions, 2007), and any 2005-2026 paper citing math/0511078 on
   this question. If it is answered in print, give the exact reference and theorem and stop with REPORT.md first line
   RESOLVED_IN_LITERATURE.
2. Understand why it is not trivial: every stationary sequence is a function of its own (shift) Markov chain of pasts; the
   point is Harris recurrence of that chain. Work out what Harris recurrence of a representing chain forces (e.g. some form
   of regeneration / absolute regularity of the represented sequence along a subsequence, or a constraint on the tail).
3. Either prove every psi-mixing (or every 1-dependent) sequence has such a representation (construct the chain), or find an
   obstruction and a sequence violating it. State and prove precisely what you get; give the case left open if any.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof or construction, what was checked and how, and the literature found. Keep LOG.md as you go.
Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere,
no pushes.

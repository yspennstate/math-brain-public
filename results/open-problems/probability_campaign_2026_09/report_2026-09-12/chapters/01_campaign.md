## The campaign: how the corpus was built and what its words mean

### Six intakes in five days

The corpus was not assembled by one process. Six intakes ran between 6 and 10 September 2026, each
with its own directory, its own identifier prefix, and its own append-only ledger.

The **Codex campaign** started at 15:13 UTC on 6 September under a twenty-hour clock and a mandate to
find a thousand genuine, distinct, sourced open problems in probability, check the later literature
on each, attempt each, and preserve the proofs, counterexamples, failed routes and exact obstructions.
One agent did the work; no solvers or reviewers were delegated, and its own README states the rule
that author checking is never called independent review. It recorded 590 ledger lines covering 495
distinct problems, 451 of them admitted, and produced a 606-page typeset artifact of its own on 7
September. Crucially it also wrote 25 free-standing proof files under `proofs/`, covering 28 mapped
identifiers, which are not referenced from the attempt ledger's fields and are easy to miss. Those
files are the substance of chapter 3.

**Intake C** (7 September) added 160 records, 129 admitted, and was the first intake to push material
into the mathematical brain as typed, provenance-bound claims rather than prose.

**Intakes D, E and F** (8 September) added 102, 115 and 140 records. D and E each carry a
`CORRECTIONS.md` recording an audit of their own exclusions and partials; F is the source of the
Janson results and of the sparse parity work.

**Intake G** (10 September) added 15 records from eight arXiv postings between 19 August and 9
September 2026, none of which appeared in the 426-source union of the earlier ledgers. Three of its
other candidate sources turned out to resolve earlier rows rather than pose new ones, which is a
result of a kind: Zhu's 2609.06818 proves Aldous and Fill Open Problem 6.14; Brown, Rosenthal and Zhou
2609.07819 resolve all seven Haggstrom and Rosenthal central limit theorem problems; Doumas and
Spektor 2606.21591 prove the siblings coupon-collector conjecture.

A thirty-hour Codex session on 9 September did no new intake. It reread all five ledgers, matched the
snapshot byte for byte, audited the written proofs, and wrote the count that this report treats as the
reference point for the earlier corpus. The owner stopped it at about 10:35 UTC.

### What "admitted" means, and the five status axes

A candidate URL is not an acquired source. A numbered exercise is not an open problem. A source's
historical claim that something is open is not a verified present-day status. Splitting a
parameterised question into many values does not create distinct entries. Those four rules are why
908 of 1,025 records are admitted and the rest are not.

The ledgers keep five independent status axes, and confusing them is the main way a reader can
overstate what was done.

1. *Source status*: candidate, acquired, extracted, statement checked.
2. *Historical status*: the source explicitly says open or conjectured, or it does not.
3. *Current status*: unverified, no resolution found in a documented search, resolved in later
   literature, disputed.
4. *Attempt status*: not started, partial attempt, proof candidate, counterexample candidate,
   obstruction documented.
5. *Verification*: unreviewed, author checked, independently reviewed, formally checked with a
   separate statement-fidelity review.

The report uses the ledgers' own words for these, never a stronger one. In particular:

- **author checked** means the person who wrote the argument read it again. It is not review.
- **candidate** means the argument is complete in the author's judgment and has not been
  independently verified, or its scope limits are unresolved.
- **independently read** means a second agent or session read the argument and reproduced its steps.
  That is weaker than refereeing and much weaker than certification.
- **Lean core** means a finite arithmetic or combinatorial core was stated in Lean 4 against Mathlib
  and accepted by the kernel with no `sorry`, no `native_decide`, and `#print axioms` reporting only
  `propext`, `Classical.choice` and `Quot.sound`. It does not mean the source theorem is formalised.
- **prior art not cleared** means nobody has done the citation check: pull the papers citing the
  source and search for the problem number. This is the standing gap on every result in this report.

### The mathematical brain

The campaign was also an experiment on the mathematical brain, the retrieval system that puts stored
statements in front of an agent while it works. Intake C onward deposited typed probability claims,
dependencies, counterexamples and failed routes into that store through its integrator, with the
prediction that a realistic analogous query would later retrieve the right assumptions and the right
obstruction without promoting a conjecture into a theorem.

Two things about that experiment belong in this report because they bear on how much the brain
contributed to the mathematics.

First, the retrieval lane was measurably degraded for four days in the middle of the campaign. Three
independent changes landed between 7 and 8 September and stacked: an on-topic score floor tuned on
long prompts that a one-line mathematical question cannot reach, a card budget that admitted one
whole note where three were intended, and a document-frequency cap that erased every token of the
largest stored family. Measured through the real hook on a fixed bank, the brain served the theorem a
mathematician was asking about on 35 per cent of unnamed questions, against 84 per cent on 3
September. It was repaired on 11 September to 74 and then 79 per cent. Any claim that the brain
helped or did not help during 8 to 11 September is a claim about a half-silent lane.

Second, where the brain has been measured against a solver working alone, the gain is concentrated in
one place. On proof-audit banks, where the solver can already judge the argument, the retrieved
statements do not flip verdicts and the measurable gain comes from the posture block that tells the
reader to test each step and name the first one it cannot re-derive. On locate-the-fact banks, where
the answer is a number only the store holds, the brain moves a solver from 3 correct out of 60 to 57,
with no wrong numbers in any round. The honest summary is that the store is a memory, not a
mathematician: it is worth having for what it remembers exactly, and it does not supply judgment.

On 12 September a program of five lanes went to work on the store and the retrieval path, including
one lane whose specific job is to make the campaign's own results answerable by an owner-voice
question. Before that lane ran, a read-only search of the 7,451-node store found that of 32 results
checked, 26 had a node but mostly as a problem statement or an attempt note rather than as the result
with its verification state, and 6 had no node at all.

### What this report is not

It is not a claim of priority on anything. It is not a referee report; no result here has been
refereed. It is not a formalisation; the Lean files are small checked cores inside larger arguments.
And it is not a coverage claim: the mandate said a thousand problems and the corpus holds 908 admitted
records, so the campaign fell short of its own target and the ledgers say so in their own status
fields.

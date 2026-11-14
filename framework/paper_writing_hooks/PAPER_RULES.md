# How a paper of his is written

Read this before the first sentence of a paper and again before it is posted or submitted.
The checks W01..W56 (`pw_run.py --list`, by hand `paper_lint.py <tex or folder>`) look for the
faults below. A clean lint is the floor. It is not a reading: on three rounds of the same faults put
in new words the checks caught 0 of 38, then 2 of 24, then 5 of 14. Only a reader who did not write
the paper (`paper_audit.py run <tex>`) can say it is ready.

Each rule is marked with where it comes from: **[his words]**, **[editor's letter]**, or
**[house style]** (ordinary practice he has not ruled on; these print as "should", never MUST).

## Why these exist

11 Nov 2026. Probability Theory and Related Fields declined "Extreme least singular values with
redundancy, radial ensembles, and quantitative stability of phase retrieval" on a quick opinion.
The referee called the result significant and still said no, for three reasons that are one reason:

1. the introduction did not say what was new against his own earlier paper (the square case);
2. a lemma of that earlier paper was reprinted where it should have been cited;
3. the paper "does not appear to have undergone a thorough editing process", with one paragraph
   quoted as the sample: a list of four labels ("marked-row construction", "two-normal estimate",
   "good-overlap/bad-overlap decomposition", "stability base"), none defined before page 12, opened
   by "The present paper does not use the r = 0 theorem as a black box."

An earlier referee (RMTA-D-26-00088) had said the same in other words: "generic and mechanical",
wanted "a more author-driven presentation".

## His words, with the document each was said about

- 15 Sep 2026, about a shipped paper: "don't use AI self introspection stuff ... write this like a
  professional math paper ... i want natural voices, human, stop with the self introspection."
- 4 Oct 00:14, about film transcripts and papers: transcripts are written "with my voice, which is
  human, in mind, so should papers and so on".
- 2 Nov 00:32, about a proposal: "less wordy, it sounds ai written, stronger and more to the point".
- 2 Nov 02:59, about the research statement: "i want things to be defined better so that they can
  be read by a human and understood".
- 2 Nov 04:57, about a paper in a public repository: "one line is overflow, it does not include
  funding statement, or AI acknowledgment, this is not how we write paper, fix that repo right now,
  and put in the brain this information and hooks so that this never ever happens again".
- 11 Nov 06:29, about a pitch-deck slide: "i don't like the self introspection ... it does not
  sound that human ... it is annoying".
- 11 Nov 07:06, about papers: "when we write and publish math paper, i think we need to be more
  careful to cite all relevant sources".
- 12 Nov 05:59, about papers: "more editing, more auditing, less self introspection, it is weird,
  better writing ... publishable as is", and "i want more agents working on audit, making sure
  that the million rules i have, including no self introspection, are being followed".
- 12 Nov 06:30, about papers: "it would be nice if in the appendix of paper we put notations,
  definitions and where the notation first appears", and "i have been screaming about using multiple
  words for the same thing ever since a referee found that out and it is still happening".
- 14 Nov 23:34, about every posted manuscript: "i want the AI in the beginning of the paper, in
  the introduction, and in the AI declaration to essentially acknowledge the mathematicians who
  together their work was most important for the manuscripts, and say clearly what existed before,
  what is new, and how the new ideas are related to old ideas ... with citations, that way we can
  give the humans who made the biggest contributions to the solutions ... credit".

## The rules

### The paper states mathematics. It never talks about itself. [his words]
- No sentence whose subject is the paper, the draft, the writing, the search, a check, an agent or
  an earlier version: "the present paper does not use", "these additions", "an earlier version",
  "was corrected", "we found no later paper", "re-derived line by line", "we verified numerically
  as a sanity check", "we are careful about what is and is not proved", "an honest ledger".
- A correction is silent: the corrected statement or citation simply appears.
- Attribution is one neutral clause in the present tense: "The operator W was introduced by
  Jamilov [4], who determined its two fixed points."
- The process is named only in the declaration section, as a short factual record of which system
  produced what. Not a diary, not a list of mistakes fixed.
- Never a word about how the text sounds. The same holds for comments in the source and for commit
  messages in a paper's repository.

### The introduction answers three questions in plain sentences [editor's letter]
- What was known, with the theorem stated and the paper cited.
- What fails when one tries to push it to the present setting.
- Which idea gets past that, shown as a displayed statement or inequality, not as a label.
A reader who knows the earlier case must finish page two knowing whether the extension is routine.
When the earlier paper is his own, this is the first thing an editor checks.

### One word per thing, and no name before its definition [his words; editor's letter]
- One object has one name in the text, the section titles and the appendix titles. A second word
  for the same thing is a fault, however natural it reads.
- A term of art coined in the paper is defined where it first appears, or not used until it is.
  The abstract and the introduction use no label that the body defines later.
- Every symbol is introduced before it is used; a quantity is defined once.
- A long paper ends with an appendix of notation and definitions that says where each first appears.

### Nothing is reprinted [editor's letter]
- A lemma, proof or paragraph from an earlier paper is cited by number, not copied. If a proof must
  be repeated for the reader's sake, say so in one clause and say what changed.
- `paper_lint.py <new.tex> --against <old.tex>` lists the sentences that stand word for word in
  the earlier paper; W21 does the same against the index of his posted papers.

### Citations carry weight [his words]
- Every relevant source is cited, and every cited work gets a clause saying what it does. No
  brackets of seven numbers as "background".
- The closest prior result is stated, not gestured at; who proved what, in which generality.
- Every reference can be looked up (arXiv number, DOI, journal and year). The citation hooks
  (`citation_hooks/`) check the rest.

### The people whose work carries the result get the credit [his words, 14 Nov 23:34]
- The introduction, near its start, names the mathematicians whose work the result most depends
  on, by name and with citations: who posed the problem, who proved what we build on, whose method
  we follow.
- It then says plainly what existed before (the best known result, stated, with its source), what
  is new here, and how each new idea relates to an old one: which earlier idea it extends, combines
  or replaces, and why. Cite both sides.
- The AI declaration names the same people, with citations, and says that those results are
  theirs, next to the short factual record of which system produced what.
- The credit is built during the work, not after it: CREDITS.md in the paper folder starts when
  the attack starts, gets a line when a borrowed lemma or trick is used, and marks each statement
  known, adapted or new. The introduction and the declaration are written from it.
- In the body, attribution stays one neutral present-tense clause (the 15 Sep rule). Crediting
  people is not narrating how the paper was made.
- Hooks C17..C26 in `citation_hooks/` fire at each stage: when problem_recall.py runs or a theorem
  is written (development), when the abstract or introduction is edited (writing), when the
  acknowledgments or AI declaration are edited (credit), and before posting.

### What every posted paper carries [his words, 2 Nov 04:57]
- The funding statement and the AI acknowledgment. His 2 Nov words name a paper without them as
  "not how we write paper". The 15 Sep text in CLAUDE.md speaks of the AI declaration "when he asks
  for one"; the later words are the stricter and are the ones the check (W51) follows. A paper he
  has ruled should carry none gets a file `NO_AI_DECLARATION` beside its .tex.
- The finished grant NSF OISE-2401227 is not acknowledged in new work (W53).
- No overfull line, no "??", no undefined reference, no TODO, a fresh log from the final source.
- His name and affiliation, and the data and code line with the repository that really holds
  them. [house style]

### Plain strong prose [his words]
- Short declarative sentences; the mathematical content first. Less wordy, stronger, to the point.
  Cut "remarkably", "strikingly", "notably", "delve", "headline", "crucially", "it is worth noting".
- No bold runs, no emoji, no exclamation marks, no defensive phrases ("clearly labelled").
- Things are defined well enough that a person can read the page and understand it.

### Structure a person would choose [house style]
- Sections exist because the argument has parts. No "Conclusion" that repeats the abstract, no
  "Open problems" appendix as padding, no "proof template", no roadmap that only lists section
  numbers; the roadmap says what each section proves and why in that order.
- The abstract is a few sentences of statement, without citations, colon lists or "we show that
  ... we also show that ... finally we show".
- Theorems are stated completely: hypotheses, quantifiers, constants and what they depend on.
- No slogans where a statement belongs, no promise the text does not keep, no em-dash runs.

### Before it leaves [his words, 12 Nov 05:59: "more editing, more auditing"]
1. `paper_lint.py <folder>` with no MUST finding, and every "should" either fixed or judged.
2. An audit by a reader that did not write it (`paper_audit.py run <tex>`): mathematics line by
   line, then the prose against this file, then the introduction read as an editor of the target
   journal. The paper is ready when the audit on record for this exact source says SEND AS IS with
   no must-fix item; W43 reads that verdict, not the presence of a report.
3. The PDF looked at page by page, not only the source.
4. For a journal: the journal's own scope and recent papers read; the cover letter states the
   advance against the closest prior work in two sentences.

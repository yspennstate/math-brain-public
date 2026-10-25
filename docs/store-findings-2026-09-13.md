# What a read of the store found, 13 September 2026

On 13 September the whole math store (7,831 claim nodes at the time) was read for defects that the ingest checks
cannot see from the code alone, and several ranking ideas for the math hook were measured against the recall banks.
Two defects turned up, neither of which moved a score much. Most of the ranking ideas were refused. The numbers are
here so that anyone proposing one of them again can start from the measurement.

## The same card under two names

48 groups of nodes share a title and an identical full body. In 46 of them the two copies carry different logical
ids, because the same source article was fetched once under its title and once under an alias:

| first id | second id |
|---|---|
| `wiki-arzel-ascoli-theorem` | `wiki-ascoli-arzel-theorem` |
| `wiki-uniform-boundedness-principle` | `wiki-banach-steinhaus-theorem` |
| `wiki-vapnik-chervonenkis-dimension` | `wiki-vc-dimension` |
| `wiki-composition-series` | `wiki-jordan-h-lder-theorem` |
| `wiki-kirchhoff-s-theorem` | `wiki-matrix-tree-theorem` |
| `wiki-surface-topology` | `wiki-classification-of-surfaces` |

The ingest step refuses a resubmission only when the new draft has the same logical id and the same statement digest
as a stored one. The id is built from the name the submitter chose, so a harvester that follows a redirect and names
the card after the alias lands a second copy, and nothing compares the text.

The cost to retrieval is small. On the theorem bank, 35 of 136 answer blocks spend two of their three slots on such a
pair. But only five of those are near misses and one is a miss, because the duplicated pair is usually the answer
said twice. The real costs are store growth and a reader handed the same lead under two names.

The fix indexes stored statements by digest as a second key, so an identical statement arriving under a new name is
caught the same way an identical resubmission is. It sits behind the setting `MATHBRAIN_DEDUP_BY_CONTENT`, off by
default; when off, it only reports the pair and still stores both.

The negative control matters more than the fix. The self-avoiding-walk corpus holds thousands of records whose titles
and bodies differ by a single character, such as "avoid the sites (-2,0)" against "(2,0)". These are mirror problems
that share a walk count, and both are true. A digest that normalised punctuation would merge them and delete real
mathematics. The control feeds such a pair through with deduplication on and requires both to survive. The same
corpus misleads looser comparisons:

- a folding key that dropped the minus sign reported 91 true twins and 574 redundant copies;
- comparing only the first 600 characters of each body did the same;
- in fact the full bodies differ in all 235 groups whose bytes differ.

## Kinds the store cannot record

211 nodes begin their body with the kind their campaign gave them ("Theorem (campaign status: audited-pass): ...",
"Numeric ...", "Open_gap ...", "Failed_route ...", "Conjecture ...", "Lemma ..."), and 209 of them are stored with the
kind `concept`. This is lawful, not careless:

- none of the 209 carries a proof text, and the draft specification requires one for `lemma` and `theorem`;
- the specification's whole vocabulary is `definition`, `lemma`, `theorem` and `concept`, so a numeric result, an
  open gap, a failed route or a conjecture has no kind of its own.

The retrieval consequence is real. On a question that asks for a value, every candidate reads `concept`, so the ranker
has no way to tell the card holding the number from the cards around it. In one miss, both cards holding the value
(1.2579) clear the word-overlap floor at ranks 5 and 7 of 300; retrieval is fine and the ranking is wrong. The repair
is either a wider kind vocabulary in the specification or the campaign's own label carried in node metadata, where
the ranker can read it.

## Ranking ideas measured and refused

| idea | what it was worth |
|---|---|
| stay silent when the top two cards score almost alike | 1 answer of 30 |
| raise the word-overlap floor before ranking | gains 1 answer, loses 2 correct fires |
| prefer "theorem" or "inequality" in the title | 14 gained, up to 12 lost |
| tell a theorem from a definition by how its text opens | 7 gained, 61 at risk |
| the same, applied only when the question asks for a result | 2 gained, 11 at risk |
| prefer cards that carry a decimal, on value questions | 16 to 17 of 20 on the campaign bank, but on a fresh bank a Ramsey theorem asked without its name loses its hit and its rank 1 |

Two signals did help that day. Ranking by how much of the question's names a card's title covers was the best signal
measured. The kind field the store already records, used as a tie-break that puts a definition below the result that
uses it, was worth two answers.

A refusal recorded only in an experiment ledger is invisible to recall, because recall indexes the record files and
not the ledger. Twelve proposals were put to recall phrased as ideas, before any work: the three refusals that had a
record came back at rank 1, and none of the seven that lived only in the ledger returned anything relevant. After
records were written for those seven, five came back in the top five. A refused idea is therefore written up as a
record, with the number that refused it.

# Equal tools, five arms (5 October 2026)

The first stage-one runs of early October gave the arms different tools, so part of each gap was computation, not
recall: the brain arms could call Lean as a calculator and the others could not. This run gave every arm the same
tools, named in the same words in every prompt, so that the arms differ only in what they can read and recall.

## Design

Every arm had Python (exact integers and fractions, sympy, mpmath, numpy, no network, 120 seconds a call), a Lean
check (90 seconds), and file reading and search on its own folder and its documents. One empty working folder per
problem, ten minutes a problem, Claude Sonnet in every arm.

| arm | what it adds |
|---|---|
| tools only | nothing |
| documents | the memory folder and a snapshot of the store |
| documents and recall | the ranked recall over the memory folder |
| math brain v4n | the hooks of version v4n with their served notes, and math recall |
| math brain v5 | version v5 without served notes (chosen by the pre-check below) |

The bank was the first 300 problems of a hard computation bank. The two primary comparisons were fixed before any
answer existed: v5 against documents and recall, and v5 against v4n (exact two-sided McNemar on the paired problems).
The written prediction was that with Python in every arm the five would land within about five points of one another
and neither primary comparison would be significant.

## Pre-check

Before the main run, v5 was checked on 200 store questions of a second bank (store retrieval, two-hop store questions,
and questions about earlier results), with the same tools, to choose between serving notes and not. A difference of
two or fewer was to go to the simpler variant.

| arm | correct of 200 |
|---|---|
| documents and recall | 193 |
| v5 with served notes | 198 |
| v5 without served notes | 196 |

Served notes against none was 2 to 0 (p = 0.5), so the main run took v5 without served notes. Against documents and
recall, v5 with notes was 5 to 0 (p = 0.06).

## Results

| arm | correct of 300 | 95% interval | problems with a refused tool call | median seconds | cost (dollars) |
|---|---|---|---|---|---|
| tools only | 299 | 98.1-99.9 | 2 | 55.5 | 4.44 |
| documents | 297 | 97.1-99.7 | 10 | 55.5 | 4.66 |
| documents and recall | 284 | 91.5-96.7 | 42 | 55.3 | 4.76 |
| math brain v4n | 291 | 94.4-98.4 | 66 | 61.5 | 11.09 |
| math brain v5 | 297 | 97.1-99.7 | 4 | 50.5 | 10.84 |

v5 against documents and recall: 15 to 2, p = 0.0024. v5 against v4n: 9 to 3, p = 0.15. Against tools only,
documents and recall lost 0 to 15 (p = 6e-5) and v4n 1 to 9 (p = 0.02); documents and v5 tied with tools only.

## What the gaps were

The first primary comparison came out significant and the prediction failed, but not for a mathematical reason. In the
arms whose prompt named document folders, the solver often built the path to the Python or Lean helper through those
folders. The path resolved to the allowed script, but the permission layer matched the command text literally and
refused it, and the solver then stopped computing. The losses of documents and recall and of v4n are almost all of
this kind: their unanswered rows say the tool call was refused. With the refused problems set aside, every arm got 297
to 300 of the problems its tools reached, and v4n got none of those wrong.

So on this bank, with working tools, no arm adds accuracy: tools alone reach 299 of 300. The bank had become a
computation bank and could no longer separate the arms, and the tests that followed moved to proof audits and
reasoning items (see "Solving and auditing, 61 items" in `TESTS.md`). The harness fix the run called for is to check
a tool command on its resolved path rather than its text, or to tell the solver to copy the command exactly. The brain
arms cost about 2.4 times tools only and bought nothing here.

---
name: sixteen_referee_reads_before_a_paper_release_2026_11_13
description: "A posted paper (the Ising perceptron at nonzero margin, certified bounds along the replica-symmetric curve) went through sixteen independent first-reader referee reads before its v2.1 release. Every read returned minor edits with 3-6 must-fix items, and late reads still caught false sentences, one of them introduced by the previous read's fix. What the reads found, in order of frequency, and the stopping rule that came out of it."
metadata:
  type: project
  created: 2026-11-13
  status: verified
---

The paper: "The Ising perceptron at nonzero margin: certified bounds along the replica-symmetric curve", released as
v2.1 on Zenodo (DOI 10.5281/zenodo.24181576; concept DOI 10.5281/zenodo.23329765). Before release it was read
sixteen times by fresh first-reader sessions, each acting as a journal's first referee with no memory of the earlier
reads.

What the reads kept finding, most frequent first:
1. One object, several names (a threshold, the patterns, a contraction product, enclosures of a critical value).
   Fix: choose one name and search for every other.
2. A number in the prose that the code does not produce. A slope near the endpoint had been written as one value;
   the scan gives a range, and the text now quotes the range.
3. Figures labelled in code notation rather than the paper's.
4. Uncited tools: the interval libraries and the proof assistant used for checks (FLINT and python-flint, Lean) need
   citations like any other prior work.

Late reads still mattered. The 14th caught a false claim that a width entered at second order; measured, the
enclosure width is linear in the distance from the anchor. The 15th caught a sentence saying five checks ran on all
1,680 slabs when two of them ran on 1,500. The 16th caught a sentence that the rewrite after read 15 had introduced:
a condition stated over all functions when it is a condition over points of the plane.

Release hygiene. A moved tag is not a fixed reference: v2.0 was left where it was and the new release tagged v2.1.
The PDF's checksum was compared with the file on the archive record.

Stopping rule. Run one read, fix, rebuild and read again; stop when a read's must-fix list is only names and
citations. Check every number in the prose against the output file the code wrote, never against memory. Every fix
is new text and can carry a new fault, so a fix is not done until a fresh read has passed over it.

Acknowledgement. The replica-symmetric prediction the paper certifies along is from the statistical-physics
literature on the perceptron that began with Gardner and Derrida (1988), and the rigorous line it builds on includes
Ding and Sun's lower bound for the Ising perceptron capacity (2019). The paper itself carries the full citations.

Related: [[public_edition_papers_carry_dead_private_repo_links_rewrite_before_doi_2026_11_12]],
[[paper_shelf_refereed_arxiv_moves_and_check_2026_11_14]].

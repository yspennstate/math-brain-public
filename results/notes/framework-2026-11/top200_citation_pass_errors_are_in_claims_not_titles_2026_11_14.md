---
name: top200_citation_pass_errors_are_in_claims_not_titles_2026_11_14
description: "Checking [verify] tags on the top-200 list? Crossref confirms titles in one call, but the errors found 14 Nov were in claims (HRS range 0<=k<=2, MMP in law+pathwise, a wrong year, a missing source): read the arXiv abstract for ranges"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T06:17:18+02:00
  status: verified
  evidence: "Crossref and arXiv lookups 14 Nov (scratchpad look13/16/17/04/07/02.out); ledger VERIFY_RESOLVED_1114.tsv; pushes 182-187 verified on GitHub"
---

The [verify] tags on the top-200 probability list (06_math_research/top200_probability_2026_10_14/src/rows_NN.py) were checked against Crossref and arXiv abstracts on 14 Nov 2026, rows_02 to rows_17. About 170 tags were resolved; about 80 remain, mostly content claims (who proved what, exact ranges) rather than bibliographic gaps. Ledger: top200_vet_agent_2026_11_11/VERIFY_RESOLVED_1114.tsv. Pushes 182-187 on brain-repo main.

Most tags were correct citations that only lacked a journal and volume. The errors that turned up were in claims, not titles:
- Heap-Radziwill-Soundararajan (Q. J. Math. 70, 2019) prove the sharp upper bound for 0 <= k <= 2; the row said 0 <= k <= 1.
- Mueller-Mytnik-Perkins (Ann. Probab. 42, 2014): non-uniqueness both in law and pathwise (zero solution vs a nonzero one from 0); the row left it open.
- Guivarc'h-Le Jan is Ann. Sci. ENS 26 (1993), not 1990.
- A source (GKK, STOC 2008) the row relied on was missing from its src field.
- Bansal-Jiang's Komlos bound is STOC 2026 (arXiv 2025); Jagannath-Tobasco is PTRF 167 (2017, online 2016).

How to apply: a Crossref title search confirms a reference in one call (curl api.crossref.org/works?query.bibliographic=...&rows=2); it cannot confirm a claimed range or attribution. For those, read the arXiv abstract (export.arxiv.org/api/query, over https - plain http returned nothing). Resolve only what a lookup confirms and narrow the tag otherwise ([verify: X]). Never edit rows, LIST.md, list.jsonl or the ledger while a push carrying them is verifying.


Added 14 Nov 09:2x (pass finished, zero bracketed tags on the 469 rows, ledger 06_math_research/top200_vet_agent_2026_11_11/VERIFY_RESOLVED_1114.tsv): a tag that looks like a harmless "later work [verify]" can hide a wrong attribution. T041 (Talagrand convolution) credited the cube log-log bound to Eldan-Lee-Lehec 2017; it is Chen, arXiv:2511.19374 (2025). Sorting an arXiv search by submittedDate (abs:Talagrand AND abs:convolution AND abs:conjecture) found it plus an independent proof of the Lu-Guo-Fang result (Shaposhnikov 2609.11290), which a title search would not have.

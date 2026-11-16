---
name: open_problem_catalogue_1128_probability_networks_computation_2026_11_16
description: "[VERIFIED] Catalogue of 1,128 open problems (probability, networks, computation; ids CN0001..), each with source page, quote and dated open-status search; 1,018 checked open"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T03:15:42+02:00
  status: provisional
  evidence: ""
---

Built 15-16 Nov 2026 as a list of about 1,000 open problems with sources, focus computational and probability. Twelve Codex briefs (CAT01..CAT12, codex_swarm_1115, run on Mac mini 1) each harvested about 100 rows from public problem lists (erdosproblems.com, TOPP, Open Problem Garden, COLT open problems, ordos-problems, survey papers). Merged by merge_catalogue.py: 1,194 rows -> 1,128, 66 cross-brief duplicates dropped, none duplicating the 673 problems the brain already held (title Jaccard 0.6, and 0 even at 0.45).

Where: 12_cognitive_architecture/loops/catalogue_1115/catalogue/ - catalogue.jsonl (full records: title, statement, url, quote, locator, open_check, computational angle, difficulty, area, status), CATALOGUE.md (one line per problem by area), audit_catalogue.py, set_status.py, quote_check.jsonl.

How far to trust a row: status checked_open (1,018) = the row's quote was found word for word in the page the worker fetched (checked on the Mac against briefs/*/sources, 1,044 of 1,128 found) AND its open-status search ran. needs_check (110) = quote not found in a fetched page (84; mostly PDFs the check skips) or the search did not run (26; HTTP 429 etc). Weakness: most quotes are 1-5 words (805 under 6), so the quote proves the page was read, not that the statement is copied whole; 'open' means a dated web/arXiv search found no resolution, not a literature review. Two rows share a TOPP page URL but are distinct problems.

Areas: erdos 137, algorithms 124, complexity 113, stat-physics 99, learning-optimization 98, probability 96, quantum-crypto-coding 95, distributed 90, graph-theory 88, random-graphs-networks 85, markov-mixing 62, geometry 41. 1,093 carry a computational angle (a finite check or experiment that could bear on them).

Next use: pick computational/probability rows for solving; before working one, search literature and GitHub for a solution (standing rule).

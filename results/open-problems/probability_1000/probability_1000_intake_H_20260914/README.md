# Intake H (14 September 2026): candidate rows, not yet admitted

Twenty-five statements from fourteen arXiv papers posted July to September 2026, collected by a lookup agent
(model: Sonnet) from arXiv abstract and HTML pages on 14 September 2026, with the authors' own words quoted where
the agent could reach them. Three duplicate rows already in the ledgers (Flammant Conjecture 2.2 = G0004, Cerf
Conjecture 1.1 = the theta(p_c) = 0 rows, Tang and Zhang's pairwise negative correlation = C0091) are marked
`duplicate`. Every other row is `candidate_unverified` and `admitted: false`: nobody in the session has yet opened
the papers to confirm the statements and that the authors call them open. Admission requires that check, row by row,
exactly as intakes C to G were done. The raw agent output is `intake_H_candidates.md` beside this file.

## Source check, 14 September 2026 (second pass)

A second lookup agent fetched each of the 22 non-duplicate papers (PDF text extracted locally where the HTML
was truncated) and compared every row with the paper's own sentence; the quotes are in
`intake_H_verification.md`. 21 rows confirmed verbatim and called open by their authors: these are now
`admitted: true`, status `unverified` (the campaign's word for an admitted open problem with no result). H0024's
label was wrong (Theorem 3.5(ii) and Remark 3.6, not 5(ii)/6) and is corrected. H0025 (the RRS conjecture) is
resolved in the non-extremal regime by the paper that states it and stays `admitted: false`. The candidate
file before this pass is `problems.jsonl.bak_candidates_20260914`.

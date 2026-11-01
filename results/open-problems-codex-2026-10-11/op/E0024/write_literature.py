from pathlib import Path
import json
log=json.loads(Path('search_log.json').read_text())
head='''# Literature verification — E0024

Date: 2026-10-12. No paper found that states and proves Question 4/4′ under precisely its unrestricted hypotheses. This is a bounded negative search, not a proof that no solution exists. VERDICT is not SOLVED_IN_LITERATURE.

## Exact source and scope

Ze-Chun Hu and Wei Sun, *Hunt’s Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, 19 August 2019; published in *Acta Mathematica Sinica, English Series* **37** (2021), 491–508, DOI 10.1007/s10114-021-9343-7. Downloaded the 27-page arXiv PDF into source_pdf.pdf; its extracted text is source.txt. Crossref verified the journal reference. The following quotations normalize only PDF line breaks and mathematical subscripts.

PDF p. 15:
> Question 4. Let S be a nonempty proper subspace of R^n. Assume that the two projection processes X_S and X_{S⊥} of X on S and S⊥, respectively, are independent and satisfy (H). Does X satisfy (H)?

PDF p. 18:
> Question 4’. Let X_1 and X_2 be Lévy processes on R^n and R^m, respectively. Suppose that X_1 and X_2 are independent and both of them satisfy (H). Does the R^{n+m}-valued Lévy process X = (X_1, X_2) satisfy (H)?

There are NO transition-density, resolvent-density, Gaussian, symmetry, or sector assumptions in this question. The density hypotheses at the start of Section 4 apply to that section, not to Question 4′. (H) means every semipolar set is polar; hitting times use t>0, not t≥0. The dimensions in the product question are positive. Question 4 uses a nonzero proper linear subspace, not an arbitrary set.

PDF p. 19 gives Proposition 3.9 (one factor compound Poisson) and Proposition 3.10 (both satisfy condition (S)); these are special cases. PDF pp. 4 and 20 give Rao’s Theorem 2.3 and the finite-energy criterion Theorem 4.2. Proposition 4.8, PDF p. 21 and proof pp. 24–25, concerns only measures η⊗ξ, not arbitrary correlated measures. Remark 5.1(ii), PDF p. 25, gives the implication from product closure to sum closure.

## Search ledger

All requests used Python urllib from the shell. Complete URLs, responses/failures, dates, and local raw-file names are retained in search_log.json. A failed request was not counted as a successful negative search.

'''
rows=[]
for r in log:rows.append(f"- {r['date']} — `{r['service_query']}`: {r['url']} — {r['status']}; saved `{r.get('file','no response file')}`.")
refs='''

## Relevant results and later leads

- Hu–Sun, *Hunt’s hypothesis (H) and Getoor’s conjecture for Lévy processes*, Stochastic Processes and their Applications 122 (2012), 2319–2328; DOI 10.1016/j.spa.2012.03.013. Survey Theorems 2.5–2.6 cover nondegenerate Gaussian parts and condition (S).
- Hu–Sun–Zhang, *New Results on Hunt’s Hypothesis (H) for Lévy Processes*, Potential Analysis 42 (2015), 585–605; DOI 10.1007/s11118-014-9446-1. Survey Theorem 4.2 is its Theorem 5.1; this is the criterion used in ATTEMPT.md.
- Hu–Sun, *Further study on Hunt’s hypothesis (H) for Lévy processes*, Science China Mathematics 59 (2016), 2205–2226; DOI 10.1007/s11425-015-0600-2, arXiv:1406.2013. Weaker measure-dependent criteria do not automatically tensorize.
- Hu–Sun, *Hunt’s Hypothesis (H) for the Sum of Two Independent Lévy Processes*, Communications in Mathematics and Statistics 6 (2018), 227–247; DOI 10.1007/s40304-018-0136-y, arXiv:1702.07396. Survey Theorem 2.16 has additional energy and imaginary-part hypotheses. Its title is not a proof of unrestricted sum closure.
- Hu–Sun–Wang, *Two Theorems on Hunt’s Hypothesis (H) for Markov Processes*, arXiv:1903.00050v3 (24 April 2019), published Potential Analysis, DOI 10.1007/s11118-020-09848-2. Downloaded full PDF and extracted two_theorems_pdf.txt. Main results concern local absolute continuity and subordination by a clock with positive drift, not unrestricted products. Publication after 2019 does not make it a solution of the question.
- Murali Rao, *Hunt’s hypothesis for Lévy processes*, Proceedings of the AMS 104 (1988), 621–624; DOI 10.1090/S0002-9939-1988-0962838-6 (also indexed DOI 10.2307/2047022). Rao’s sufficient criterion is reproduced as survey Theorem 2.3.
- Liping Li, *Hunt’s hypothesis and symmetrization for general 1-dimensional diffusions*, arXiv:2107.06163v2, 23 July 2021. Downloaded full paper, li_pdf.txt. Concerns continuous strong Markov processes on the line and asymmetric shunt points. Not a product-of-Lévy-processes theorem.
- Jing Zhang, Ze-Chun Hu, Wei Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471v2, 17 October 2023; DOI 10.1007/s10473-025-0211-x. Downloaded full paper, concentration_pdf.txt. A citing work about concentration probabilities, not (H) product closure. Metadata publication years differ across services; use arXiv version date for the fetched text.
- Zhen-Qing Chen and Jie-Ming Wang, *Boundary Harnack principle for non-local operators on metric measure spaces*, arXiv:2312.02455v1 (5 December 2023); DOI 10.1214/24-AOP1734. Downloaded full paper, bhp2023_pdf.txt. BHP for specified Hunt processes, not Hunt’s hypothesis product closure. “Hunt process” and “satisfies (H)” are different assertions.
- Zhen-Qing Chen, *Boundary Harnack principle for jump diffusions*, Discrete and Continuous Dynamical Systems – S 18(10) (2025), 2937–2955; DOI 10.3934/dcdss.2025104. Downloaded published PDF, bhp2025_pdf.txt. BHP survey, not the requested theorem.
- Zhen-Qing Chen and Jie-Ming Wang, *Boundary Harnack principle for diffusion with jumps on metric measure spaces*, arXiv:2608.13976 (2026). Downloaded full PDF, bhp2026_pdf.txt. BHP under quantitative assumptions, not an unrestricted product result.

OpenAlex distinguishes arXiv work W2968964261 (zero citing works in its response) from published work W3121518416 (three citing works). Both were queried. The published citing list contains concentration, nonlocal BHP, and the 2025 BHP survey. Semantic Scholar’s arXiv citing list contains concentration and the 2023/2026 BHP papers. These are all leads, not a solution in print. The arXiv API returned HTTP 429 or timed out; the successful arxiv.org HTML search was inspected title by title, with Li’s 2021 diffusion paper the only post-survey match on the mathematical (H) topic. Broad unquoted searches produced irrelevant “Hunt” results; quoted and bibliographic follow-ups were therefore run. GitHub returned zero for the mathematical query and five cybersecurity repositories for the broader phrase; none is mathematical evidence.

## Read-only brain and earlier work

Before attempting: brain.py recall "Hunt hypothesis Levy product mistakes"; math_recall.py "Hunt hypothesis Kanda Forst product Levy"; brain.py node a_pure_jump_subordinator_can_break_kanda_forst_2026_09_13. These are hints only. The subordinator memory explicitly labels its proposed polarity estimate heuristic, despite a stronger summary label; it was not used as a proved counterexample or (H) example.

Read intake records E0024-A001 and E0024 in probability_1000_intake_E_20260908 (saved relevant records to earlier_records.json). Read origin/master:prob1000_lean_20260908/ultracode_20260909/E0024/memo.md and U_E0024.lean using git show, with no working-tree changes. These contain a sector perturbation reduction and the unresolved symmetric-partner energy problem. This session re-proves that reduction with the sharp algebraic constant, and does not claim the reduction itself is new. The older intake’s unconditional resolvent-density product assertion is not justified; ATTEMPT.md gives the exact counterexample to that assertion and uses explicit product-density hypotheses instead. The earlier memo already had those hypotheses stated correctly.
'''
Path('LITERATURE.md').write_text(head+'\n'.join(rows)+refs,encoding='utf8')
Path('STATUS.md').write_text('STATE: WORKING\nNEXT: Finish full proofs of sum/product equivalence and sharp energy comparison; complete Lean/referee checks.\nVERDICT: PARTIAL\n\n2026-10-12: Exact source confirmed. All requested services queried; API failures logged. No exact solution found. Earlier attempt audited; common Rao criterion requires explicit density hypotheses here. Sharp algebra and stable cancellation numerically tested.\n',encoding='utf8')

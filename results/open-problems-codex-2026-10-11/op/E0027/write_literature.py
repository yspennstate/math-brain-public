from pathlib import Path
import json
p=Path('LITERATURE.md')
head='''# E0027 literature audit

Audit date: 2026-10-12. No paper found that states and proves the unrestricted independent-sum question. This is a bounded search result, not a proof that no solution exists. Verdict remains PARTIAL, not SOLVED_IN_LITERATURE.

## Verified source and exact scope

Ze-Chun Hu and Wei Sun, *Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, 19 August 2019. Published as *Acta Mathematica Sinica, English Series* 37(3) (2021), 491-508, DOI 10.1007/s10114-021-9343-7. The question locator refers to the arXiv PDF p. 25, Question 7; that PDF was downloaded and its text extracted in source.txt.

The following is the exact wording, with the PDF's split lines rejoined and its accented character normalized to Unicode:

'''
s=Path('source.txt').read_text(encoding='utf-8')
a=s.find('Question 7.');b=s.find('Remark 5.1',a)
quote=' '.join(s[a:b].split()).replace('L\u00b4evy','L\u00e9vy')
head+='> '+quote+'\n\n'
head+='''The only hypotheses are independent n-dimensional Levy processes and (H) for each. No extra hypotheses appear. (H) means every semipolar set is polar, with hitting times defined as inf{t>0: X_t is in D}.

Remark 5.1(i) links a positive answer to Question 6 (the unbounded-variation one-dimensional problem), citing Kesten's Theorem 1(f). Remark 5.1(ii) reduces it to the independent-product problem, Question 4. These are implications, not solutions.

## Relevant references and what they actually prove

1. Hu and Sun, source above. Theorems 2.14 and 2.15, arXiv PDF p. 8: compound Poisson perturbations of (H) processes, and independent sums of two processes satisfying condition (S). Theorem 2.16, pp. 8-9: a result with resolvent densities, finite-energy inclusion, and control of the second exponent's imaginary part. It explicitly leaves Question 7 open. Lemma 3.1, pp. 13-14, gives preservation under projection; Question 4', p. 18, asks product stability. Proposition 2.13, p. 8, gives the criterion used in ATTEMPT.md.
2. Ze-Chun Hu and Wei Sun, *Hunt's Hypothesis (H) for the Sum of Two Independent Levy Processes*, *Communications in Mathematics and Statistics* 6(2) (2018), 227-247, DOI 10.1007/s40304-018-0136-y; arXiv:1702.07396. Full arXiv PDF downloaded, 21 pages. Despite the matching title, it is NOT an answer under just (H)+(H). Theorem 4.1 and Proposition 4.2, PDF p. 14, require extra energy/exponent hypotheses. Theorem 3.2 treats condition (S). Proposition 4.5, PDF p. 15, extends a Rao-type argument with an integrable remainder; it still imposes explicit bounds. The survey also records a correction to an auxiliary lemma of this paper in Remark 3.8, PDF p. 18: an additional projection-(H) hypothesis is needed in its Lemma 3.5; Theorem 3.1 remains valid.
3. Murali Rao, *Hunt's hypothesis for Levy processes*, *Proceedings of the American Mathematical Society* 104(2) (1988), 621-624, DOI 10.1090/S0002-9939-1988-0962838-6. Theorem 2, journal p. 622 / PDF p. 2, is the increasing-envelope sufficient condition. Actual four-page PDF downloaded as rao_actual.pdf. The first AMS URL returned a 93-page rendering of a journal contents page despite HTTP 200; this is NOT treated as the paper. The alternate /journals/proc/ URL returned the real article.
4. Ze-Chun Hu, Wei Sun and Li-Fei Wang, *Two Theorems on Hunt's Hypothesis (H) for Markov Processes*, arXiv:1903.00050; published *Potential Analysis* (2020 online), DOI 10.1007/s11118-020-09848-2. Full 25-page arXiv PDF downloaded. Theorem 1.1, p. 3, concerns local absolute continuity of process laws; Theorem 1.3, p. 4, concerns subordination by an independent subordinator with positive drift. Neither asserts the independent-sum question. This is a lead if one could verify local absolute continuity for a particular sum; it is not automatic.
5. Liping Li, *Hunt's hypothesis and symmetrization for general 1-dimensional diffusions*, arXiv:2107.06163v2, 23 July 2021. Full 14-page PDF downloaded. Concerns continuous one-dimensional strong Markov diffusions, symmetry and shunt-point classifications; not arbitrary Levy sums. No theorem matching Question 7 found there.
6. Ze-Chun Hu and Wei Sun, *Further study on Hunt's hypothesis (H) for Levy processes*, *Science China Mathematics* 59 (2016), 2205-2226, DOI 10.1007/s11425-015-0600-2; arXiv:1406.2013. Identified from the source references and API records; not independently downloaded in this attempt. Survey Theorems 2.11-2.12 cite its measure-dependent criteria. These criteria cannot simply be replaced by a global pointwise envelope.
7. Ze-Chun Hu, Wei Sun and Jing Zhang, *New Results on Hunt's Hypothesis (H) for Levy Processes*, *Potential Analysis* 42 (2015), 585-605, DOI 10.1007/s11118-014-9446-1; arXiv:1210.2016. Identified in survey and API records; not independently downloaded. The survey's Theorem 2.8 attributes an extended Kanda-Forst-Rao condition to it; it is a lead outside ordinary global-envelope arguments.
8. Ze-Chun Hu and Wei Sun, *Hunt's hypothesis (H) and Getoor's conjecture for Levy processes*, *Stochastic Processes and their Applications* 122 (2012), 2319-2328, DOI 10.1016/j.spa.2012.03.013; arXiv:1101.3038. Survey Theorems 2.5-2.6 cite its Gaussian/condition-(S) results. Identified, not independently downloaded.

## Forward citations checked under the correct identities

OpenAlex distinguishes the arXiv source W2968964261 (zero citing works returned) from the journal source W3121518416 (three citing works). Both were queried. Querying just the arXiv record would miss the following three journal citations:

* Jing Zhang, Ze-Chun Hu and Wei Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471v2 (17 October 2023); journal DOI 10.1007/s10473-025-0211-x, OpenAlex reports volume 45(2), 473-492 and year 2024. The DOI contains 2025, so the journal year metadata is recorded without resolving the discrepancy. Full 25-page preprint downloaded. Main results bound standardized mass concentration of infinitely divisible laws. PDF p. 2 calls Getoor's conjecture unsolved. This is not sum stability for (H).
* Zhen-Qing Chen, *Boundary Harnack principle for jump diffusions*, *Discrete and Continuous Dynamical Systems - S* 18(10) (October 2025), 2937-2955, DOI 10.3934/dcdss.2025104. Full 19-page PDF downloaded. Theorem 4.12, PDF p. 17 / journal p. 2953, states (H) for certain subordinate Brownian motions with a positive Gaussian component and additional subordinator assumptions. This is a special class, not Question 7; its main subject is boundary Harnack principles.
* Zhen-Qing Chen and Jieming Wang, *Boundary Harnack principle for nonlocal operators on metric measure spaces*, *Annals of Probability* 53(4) (2025), 1287-1330, DOI 10.1214/24-AOP1734. OpenAlex abstract and the preceding survey's detailed account were checked. It treats weak-duality Hunt processes and subordinate Brownian motions with Gaussian components, with geometric/comparability assumptions. No unrestricted sum-stability claim was identified. Its own full text was not retrieved, so this is a metadata/survey check, not a full-paper verification.

The 2018 sum paper's journal identity W2729024139 has four indexed citing works: the survey's journal and arXiv versions, and the transformation paper's journal and arXiv versions. No later solution appeared in this citation set.

Semantic Scholar's exact-phrase bulk query returned 31 records (including irrelevant lexical matches and duplicate journal/preprint versions); the newest relevant mathematical work found was Li's 2021 diffusion paper. Its broader query returned 1,000 of 1,526 records, so that broader query is not represented as exhaustive. The exact query and arXiv HTML search supplement it. Semantic Scholar's journal-source citation endpoint returned no citations, in conflict with OpenAlex's journal-source count; we used both rather than treating the empty response as decisive.

## Exhaustive service/query log for this attempt

Every request below was made on 2026-10-12 from Python urllib, never a built-in web-search tool. URL query parameters are the exact service query. Raw responses and error/status records are retained in this directory. HTTP 429 requests failed and carry no negative-search weight. An HTTP 200 is checked for relevance rather than assumed to be a theorem.

'''
rows=[]
for ln in Path('search_log.jsonl').read_text(encoding='utf-8').splitlines():
 d=json.loads(ln)
 status=str(d.get('http_status',d.get('error')))
 rows.append('- **'+d['service']+'**, '+d['date']+': `'+d['query_url']+'`; '+status+('; raw '+d['file'] if d.get('file') else ''))
head+='\n'.join(rows)+'\n'
head+='''

## Read-only local research searches

* math_recall.py query "Hunt hypothesis sum Levy Kanda Forst". Returned the subordinator-envelope caution and general Levy-process cards, not a verified sum theorem.
* brain.py recall "Hunt hypothesis Levy sums" and "Hunt hypothesis mistakes". Its output unexpectedly reported an automatic detached index refresh; we did not invoke a memory-write command and made no further brain.py calls. This side effect was reported by the mandated recall script, not explicitly requested by this attempt.
* Read-only intake search for E0027 in problems.jsonl, attempts.jsonl and sources.jsonl under probability_1000_intake_* identified E0027-A001 dated 2026-09-08. Its arbitrary-Rao-envelope closure inference is corrected in ATTEMPT.md Section 3. Its claim of general resolvent-density inheritance is not used; Section 6 gives an explicit obstruction without (H).
* Checked the codex_pool_2026_10_10 top-level problem ledger, ledger and manifest for E0027: no match returned. This is not a recursive audit of every worker file.
* git ls-tree -r --name-only origin/master, filtered for E0027: no matching path. No repository was changed; no files from its working tree were read. The first unfiltered command produced excessive output; the repeat filtered it within Python.

No exact theorem proving or disproving Question 7 was located. Accordingly no SOLVED_IN_LITERATURE theorem quote or line-by-line solution attribution is claimed.
'''
p.write_text(head,encoding='utf-8')
print('Saved LITERATURE.md,',len(head),'characters;',len(rows),'network requests logged')

from pathlib import Path
import json,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parent
header='''# F0118 literature check — 12 October 2026

## Status
No retrieved paper states and proves Mossel's full Conjecture 4 with arbitrary fixed integer q1<q2, the same positive eigenvalue, and the same b-ary tree. This is a bounded negative search result, not a claim that the problem is definitely still open. **Not SOLVED_IN_LITERATURE.** OpenAlex source and citation lookups were blocked by HTTP 429; Semantic Scholar searches were rate-limited and direct source identifiers returned 404. These limitations are material.

## Source verified directly
Elchanan Mossel, **Survey: Information flow on trees**, DIMACS Series in Discrete Mathematics and Theoretical Computer Science 63 (2004), DOI **10.1090/dimacs/063/12**, arXiv **math/0406446v1**. Download: https://arxiv.org/pdf/math/0406446 . Cached PDF: `mossel_pdf.raw`; extracted text: `mossel.txt`.

PDF page 10, Section 5.2, gives:

> Conjecture 4. Consider two symmetric channels M1 and M2 (as in (8)) on q1 and q2 symbols respectively, where q1 < q2. If 0 < λ2(M1) = λ2(M2) and the reconstruction problem is solvable for M1, then it is also solvable for M2.

The following sentences state the divisible case and q1=2 case as known. Section 2, PDF page 2, defines λ2(M) as **the eigenvalue** having second largest absolute value (possibly complex), not the nonnegative absolute value itself. Thus the positive hypothesis selects ferromagnetic channels. Ergodicity excludes λ=1. Equation (8), Section 5, PDF page 7, gives Mii=1-(q-1)ε and Mij=ε for i≠j; the displayed eigenvalue is 1-qε. For this question ε=(1-λ)/q and Mq=λI+(1-λ)J/q. The b-ary tree is the common tree in the surrounding setting. Proposition 2.1, PDF page 3, permits uniform-root mutual-information and posterior formulations.

The source's Theorem 3.1, PDF page 4, says binary reconstruction holds if and only if bλ²>1, including non-reconstruction at equality. Theorem 4.1, PDF page 6, gives the strict census inequalities and leaves its equality case unstated. Neither solves the remaining arbitrary-alphabet comparison.

## Main later leads inspected in full text

* Allan Sly, **Reconstruction of symmetric Potts Models**, arXiv **0811.1208v1** (2008); journal version **Reconstruction for the Potts model**, Annals of Probability (2011), DOI **10.1214/10-AOP584**. Download https://arxiv.org/pdf/0811.1208 . Theorems 1.1 and 1.2, PDF page 4: the KS threshold is sharp for q=3 at sufficiently large degree; for q>=5 it is not sharp. Theorem 1.3 gives fixed-q large-degree asymptotics. These assertions do not compare every q1<q2 at a fixed arbitrary degree. Cached `sly.txt`.
* Elchanan Mossel, Allan Sly, Youngtak Sohn, **Exact Phase Transitions for Stochastic Block Models and Reconstruction on Trees**, arXiv **2212.03362v2**, https://arxiv.org/pdf/2212.03362 . Theorem 1.12, PDF page 5, proves KS sharpness for q=3,4 at sufficiently large mean degree under Assumptions 1.10 and 1.11, with non-reconstruction at equality. Theorem 1.13, PDF page 6, concerns failure of KS sharpness. The deterministic-offspring case gives the regular tree. This proves additional special cases by implication, not the posed full conjecture. Cached `mss.txt`.
* Yuzhou Gu, Yury Polyanskiy, **Non-linear Log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems**, arXiv **2005.05444v2** (2 December 2022), https://arxiv.org/pdf/2005.05444 . Theorems 5 and 6, PDF pages 8–9, give sufficient conditions for non-reconstruction via the uniform-input KL contraction coefficient. A monotone bound, even if available, is not a comparison of the exact thresholds. Cached `gu_polyanskiy.txt`.
* Yuzhou Gu, Yury Polyanskiy, **Uniqueness of BP fixed point for the Potts model and applications to community detection**, arXiv **2303.14688v2**, https://arxiv.org/pdf/2303.14688 . The abstract and main results give BP uniqueness under dλ² >= 1+C max{λ,q^(-1)} log q. Its degradation arguments operate within a common q-alphabet. It does not prove reconstruction monotonicity across all alphabet sizes. Cached `bp.txt`.
* Heon Lee, **Robust Reconstruction on Trees with a Growing Alphabet**, arXiv **2609.33263v1** (27 September 2026), https://arxiv.org/pdf/2609.33263 . Theorem 1.7, PDF page 5, compares noisy and noiseless posteriors in a joint q→∞ and depth kq→∞ limit, under Assumption 1.5; it is not a monotonicity statement for two fixed finite q's. In particular the order of limits cannot be substituted without proof. Cached `growing.txt`.

## Earlier reference and prior attempts

* Elchanan Mossel, Yuval Peres, **Information flow on trees**, Annals of Applied Probability 13(3) (2003), 817–844, DOI **10.1214/aoap/1060202828**, arXiv **math/0107033**. Download https://arxiv.org/pdf/math/0107033 . The retrieved arXiv PDF contains the alphabet monotonicity question as Conjecture 2, Section 8.3, PDF page 23. This is an earlier statement, not a solution. Its positivity wording is not identical to the later survey; we use the later survey's explicit positive hypothesis.
* Read-only intake `probability_1000_intake_F_20260908/problems.jsonl` row F0118 and `attempts.jsonl` F0118-A001 (9 September 2026) identify the independent-recoloring obstruction. It is independently re-proved in ATTEMPT.md using edge covariances. No directly matching file was returned by the filename scan of `origin/master` in the published-answer repository. This is not a repository-wide content-search claim.
* Read-only brain queries: `brain.py recall "Potts reconstruction monotonicity mistakes"`, `brain.py recall "Potts tree reconstruction"`, and `math_recall.py "Potts tree reconstruction Mossel Sly monotonicity"`. Results were largely off-topic. The methodological warning about unjustified monotonicity was retained; no brain card is used as proof.

## Every remote request / search

The following table is generated from `search_log.jsonl`, which records exact URLs and outcomes. All searches were run on **2026-10-12** by Python urllib, without built-in web search. Download requests are included for reproducibility.

| Name / service | Exact URL (query included) | Outcome |
|---|---|---|
'''
rows=[]
for line in (ROOT/'search_log.jsonl').read_text(encoding='utf8').splitlines():
    r=json.loads(line)
    outcome=str(r.get('status',r.get('error','unknown')))
    if 'reason' in r: outcome+=': '+r['reason']
    rows.append('| '+r['name']+' | '+r.get('url','No request could be constructed without a verified work ID.')+' | '+outcome+' |')
tail='''

The OpenAlex works-citing-source step was specifically attempted by resolving the verified survey DOI to an OpenAlex work ID, then preparing its `filter=cites:W...` request. DOI resolution returned 429, so no valid citing-work request could be issued. This is a blocked citation search, not an empty citation list. Crossref and arXiv were usable; all resulting payloads were saved. Semantic Scholar did not provide a usable source record. GitHub returned one repository for "Potts reconstruction", long-mathematics/openai-math-extensions, containing Christopher D. Long's 11 October 2026 heterogeneous four-state capacity manuscript, and zero for "Potts monotonicity". The mathematical repository was inspected and its four-state OpenAI dependencies followed directly. These are leads rather than an arbitrary-alphabet comparison theorem.

## Other returned mathematical leads (abstract-level screening)

'''
ns={'a':'http://www.w3.org/2005/Atom'}
root=E.parse(ROOT/'arxiv_tree.raw').getroot()
for e in root.findall('a:entry',ns):
    title=e.find('a:title',ns).text
    if any(x in title.lower() for x in ['potts','reconstruction on trees','entropy bound','asymmetric ising','phase transitions in bayesian']):
        authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
        tail+='* '+authors+'. **'+title.strip()+'**. '+e.find('a:id',ns).text+', submitted '+e.find('a:published',ns).text[:10]+'.\n'
tail+='\nThe retrieved abstracts of the additional leads concern within-model threshold bounds, computation of posterior-distribution recursions, asymmetric binary models, or physics predictions; none states the posed general alphabet monotonicity theorem. Irrelevant imaging/Fourier/metric reconstruction hits were screened out. No related theorem has been labeled a solution in print.\n'
(ROOT/'LITERATURE.md').write_text(header+'\n'.join(rows)+tail,encoding='utf8')
print('Wrote LITERATURE.md with',len(rows),'recorded requests and outcomes.',flush=True)

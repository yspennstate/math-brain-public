import pathlib,json,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parent
ns={'a':'http://www.w3.org/2005/Atom'}
intro='''# D0064 literature audit — 11 October 2026

## Verdict and scope

No fetched theorem proves the four-case classification for all solutions under the source's intended hypotheses. This is a bounded search, not a proof of absence of a later solution. OpenAlex was rate limited; Semantic Scholar search was rate limited but its source citation endpoint succeeded. The recent supercritical uniqueness paper concerns limits of regularizations, not all star-equation fixed points. Overall result: PARTIAL, not SOLVED_IN_LITERATURE.

## Verified source

Rémi Rhodes and Vincent Vargas, *Gaussian multiplicative chaos and applications: A review*, Probability Surveys **11** (2014), 315–392, DOI 10.1214/13-PS218; arXiv:1305.6221. Source fetched from https://arxiv.org/pdf/1305.6221 using curl on 2026-10-11; stored as source_curl.pdf and source.txt. The first Python requests fetch failed with SSL UNEXPECTED_EOF; curl succeeded.

Conjecture 6.4 is on printed/PDF page 52, Section 6.3. Relevant definitions: Definition 2.17, equations (2.17)–(2.18), page 17; Definition 2.18, pages 17–18; Theorem 2.19, page 18. Section 1.2, printed page 6, states: “Finally, γ will denote the intermittency parameter. We will suppose that γ ⩾ 0.”

Section 6.3's hypothesis paragraph reads (line breaks joined):

> It is conjectured that all the non-trivial ergodic lognormal star scale invariant random measures (actually, we need to impose a stronger dependence decay than ergodicity) belong to one of the families listed below, up to a constant multiplicative factor. At least, we ask for ergodicity to get rid of the irrelevant random factor Y of Theorem 2.19.

It then requires an α in (0,1] with E[exp(α ωε(r))]=ε^d, writes the centered weight as (γ/α) X_t with the normalized continuous covariance kernel in (6.10), and gives γ²≤2d. The additional decay condition is not specified quantitatively.

Conjecture 6.4, mathematical symbols normalized from PDF extraction:

> 1. If α = 1 and γ² < 2d then the law of the solution M is the standard Gaussian multiplicative chaos, as stated in Theorem 2.19.
> 2. If α = 1 and γ² = 2d, then the law of the solution M is that of the derivative martingale M′ described in section 6.1.
> 3. If α < 1 and γ² < 2d, then M is an atomic Gaussian multiplicative chaos of the dual phase as described in subsection 6.2.
> 4. If α < 1 and γ² = 2d, then M is an atomic Gaussian multiplicative chaos of the frozen phase.

## Searches and retrieval outcomes

All queries below ran on 2026-10-11 via shell Python/curl. An initial requests-based pass attempted all eight queries in search_literature.py and failed with SSL UNEXPECTED_EOF (including HTTP arXiv after redirect). The curl pass then retried them. Importing search_literature in search_followup.py repeated that eight-query curl pass, with the same response classes; these are retries, not independent evidence. Raw responses are saved under the service names and full URLs/parameters are in search_log.json and followup_search_log.json.

'''
lines=[intro]
for logfile in ['search_log.json','followup_search_log.json']:
 lines.append('### '+logfile+'\n\n')
 for row in json.loads((root/logfile).read_text(encoding='utf8')):
  lines.append('- **'+row['service']+'** — query '+json.dumps(row.get('query',{}),ensure_ascii=False)+'; HTTP '+str(row.get('http_status','failure'))+'; '+row['url']+'\n')
 lines.append('\n')
lines.append('An attempted OpenAlex DOI-to-work lookup was rate limited, so the canonical work ID could not be resolved. The fallback DOI-form citing filter also returned 429 and is not treated as a successful or validated citing-works retrieval. Semantic Scholar supplied the first 100 citing records, which were inspected. GitHub broad search returned repositories, not peer-reviewed classification theorems.\n\n')
lines.append('## Relevant arXiv records returned by these searches\n\n')
ids={'1102.1895','1201.5219','1407.4418','1506.05099','1808.06838','1310.5574','1206.1671','2504.07552','2504.06956','2302.03010'}
seen=set()
for filename in ['arxiv.txt','arxiv_star.txt','arxiv_uniqueness.txt','arxiv_freezing.txt']:
 for e in ET.parse(root/filename).findall('a:entry',ns):
  url=e.find('a:id',ns).text
  if not any(i in url for i in ids) or url in seen: continue
  seen.add(url)
  title=' '.join(e.find('a:title',ns).text.split())
  authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
  published=e.find('a:published',ns).text[:10]
  lines.append('- '+authors+', *'+title+'*, '+url+' (initial publication '+published+').\n')
lines.append('''
## Theorems inspected and why they do not settle D0064

1. **Allez, Rhodes, Vargas**, *Lognormal star-scale invariant random measures*, arXiv:1102.1895v3; Probability Theory and Related Fields **155** (2013), 751–788, DOI 10.1007/s00440-012-0412-9. Downloaded allez.pdf; extracted allez.txt. Theorem 4, page 5, assumes a finite 1+δ moment and good covariance regularity; Theorem 10, page 6, gives the multidimensional version with an extra differentiability hypothesis. The ergodic multiplier is deterministic. This is the established moment-restricted subcritical classification. It does not classify infinite-mean critical/atomic measures. Its convention includes ε^d in the scaling of M^ε, unlike the review's shifted convention; normalized weight means differ accordingly.

2. **Alexander Shamov**, *On Gaussian multiplicative chaos*, arXiv:1407.4418v4 (downloaded shamov.pdf and shamov.txt); Journal of Functional Analysis **270** (2016), 3224–3261. The subcritical uniqueness result concerns a GMC jointly coupled to a specified Gaussian field with its Cameron–Martin transformation rule and deterministic mean. The star equation alone does not establish those assumptions. The introduction on page 5 explicitly excludes atomic supercritical distributional limits from its definition. The old intake assertion that Shamov alone proves unrestricted case (1) was therefore not accepted.

3. **Thomas Madaule, Rémi Rhodes, Vincent Vargas**, *Glassy phase and freezing of log-correlated Gaussian potentials*, arXiv:1310.5574; Annals of Applied Probability **26** (2016), 643–690, DOI 10.1214/14-AAP1071. Downloaded freezing.pdf and freezing.txt. Theorem 2.2 (Freezing theorem), page 4 of the arXiv PDF, and Corollary 2.3 give convergence of a specific normalized Gaussian approximation to a stable atomic measure directed by critical derivative chaos. The seed covariance satisfies Assumption (A): continuity/nonnegativity, k(0)=1, compact support, and a Lipschitz bound near zero. This establishes an approximation limit in the frozen family, not the assertion that every star-equation solution belongs to it.

4. **Federico Bertacco, Martin Hairer**, *Uniqueness of supercritical Gaussian multiplicative chaos*, arXiv:2504.07552v3 (27 November 2025; manuscript dated 1 December 2025). Downloaded uniqueness_supercritical.pdf and uniqueness_supercritical.txt. Theorem A, PDF page 4, assumes a given log-correlated Gaussian field on a bounded domain, g in local Sobolev H^s for s>d, and a mollifier satisfying (A1)–(A2). Its conclusion is stable convergence of the particular measures in equation (1.8) to a constant times the atomic critical-directed measure. The word “uniqueness” in the title refers to independence of the regularization up to a constant. It does not quantify over arbitrary star-equation solutions. Lemma 2.7, page 8, contains the stable-weight identity used in the independently proved reduction in REDUCTIONS.md.

5. **Junnila–Saksman** arXiv:1506.05099 and **Junnila–Saksman–Webb** arXiv:1808.06838 are approximation/decomposition uniqueness leads. Their arXiv records were read; full theorem hypotheses were not used as if they proved fixed-point classification.

6. **Bertacco–Hairer**, *How does the supercritical GMC converge?*, arXiv:2504.06956v2, and arXiv:2302.03010 (*Universality of Poisson–Dirichlet law for log-correlated Gaussian fields via level set statistics*) concern extrema, approximation limits, or normalized atom sizes. No arbitrary-solution classification was extracted from their records.

These are related results and leads. No theorem is designated a solution in print, and no unproved implication from approximation uniqueness to fixed-point uniqueness is used.

## Read-only research-brain and earlier-attempt checks

- math_recall.py queried “Gaussian multiplicative chaos star scale invariance Rhodes Vargas” and later “stable independently scattered random measure subordination”. Relevant hints were the ordinary GMC construction/interpolation and the stable-distribution definition; no classification theorem card was found. The irrelevant returned cards were not used.
- brain.py recall queried “Gaussian multiplicative chaos star equation mistakes” and “Gaussian multiplicative chaos”. No specific usable solution was returned. The advertised recall printed that a detached index refresh failed; no explicit write/remember operation was invoked.
- rg searched D0064 across the allowed 06_math_research ledgers. The D_20260908 problems/attempts entries were inspected, as was the 2026-10-10 intake summary. The prior smoothing-transform analogy is a lead, not a proof. Its statement about finite Laplace exponents failing with infinite mean is incorrect for locally finite random measures.
- git ls-tree on origin/master of ~/math-open-problems, with D0064/d0064 path patterns, found no matching recorded-answer path. No working-tree or repository change was made.
''')
(root/'LITERATURE.md').write_text(''.join(lines),encoding='utf8')
print('Wrote LITERATURE.md',len(''.join(lines)))

import pathlib,json
p=pathlib.Path('search_log.json');log=json.loads(p.read_text(encoding='utf8'))
intro='''# Literature verification for P0030

Date: 2026-10-12. All network requests used Python urllib from the shell; no built-in web search was used. Raw responses and request URLs are saved in this folder. This is a bounded search, not proof of absence from the literature.

## Outcome

No inspected paper states and proves Problems 7.1–7.3 with their exact hypotheses. Verdict is PARTIAL, not SOLVED_IN_LITERATURE. OpenAlex returned HTTP 429 on every attempt, so its source record and works-citing-source coverage could not be completed. Semantic Scholar search/source metadata returned HTTP 429, but its source-citations endpoint succeeded and returned one citing paper without a next-page marker. Coverage is limited by the services' indexes as well as the rate limit.

## Exact source and statements

Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian motion*, Probability Theory and Related Fields **160** (2014), nos.1–2, 95–126. DOI: 10.1007/s00440-013-0524-x. arXiv:1302.6958v4, 29 March 2013. Crossref's online publication date is 27 August 2013; the volume citation is 2014. Downloaded Washington-hosted PDF has 27 pages; Definitions 2.1–2.2 on pp.2–3 and Problems 7.1–7.3 on pp.25–26. The exact transcribed questions and definitions appear in ATTEMPT.md. The provided source URL is https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf (saved as source.pdf and source.txt).

Theorem 5.1, p.18, says word for word:

> Theorem 5.1. If X is strongly decomposable and ET_k < ∞ then X is 2BM.

The subscript is transcribed from PDF notation. This is a proved special case in the source, not a solution to Problem 7.1: Definition 2.2 permits independent nonidentically distributed stopped pieces and infinite means, while Theorem 5.1 assumes identical distributions and finite mean. Its proof uses renewal stationarization and total variation convergence. Theorems 5.2 and 5.3 give decomposable processes not BBM, so they do not supply counterexamples with the additional BBM hypothesis. Theorem 6.1 and Proposition 6.2 give FBM+BBM without 2BM, but that process is not decomposable and does not admit the independent cut needed in 7.2/7.3.

## Citing paper inspected

Jim Pitman and Wenpin Tang, *The Slepian zero set, and Brownian bridge embedded in Brownian motion by a spacetime shift*, Electronic Journal of Probability **20** (2015), paper 61, 1–28. DOI: 10.1214/EJP.v20-3911. arXiv:1411.0040v2, 11 June 2015. Semantic Scholar labels the initial preprint 2014. Full PDF downloaded from https://arxiv.org/pdf/1411.0040 and saved as pitman_tang.pdf and pitman_tang.txt.

Theorem 1.3 on PDF p.3 says:

> Theorem 1.3. There exists a random time T ≥ 0 such that (B_{T+u} − B_T; 0 ≤ u ≤ 1) has the same distribution as (b^0_u; 0 ≤ u ≤ 1).

This embeds one unit-length Brownian bridge into a Brownian path. It assumes an already Brownian process and gives one finite-window marginal; it neither treats arbitrary decomposable FBM+BBM nor proves a two-sided Wiener law after a common shift. It is a lead on shift-coupling, not a solution in print. Page 3 explicitly discusses Burdzy–Scheutzow and says the general case with pieces not identically distributed is left open (their informal summary must not be read as an exact restatement of Problem 7.1). The cited general shift-coupling and allocation results are possible tools, not automatically a solution to the compatibility question.

## Further exact references (leads cited in inspected papers)

- Günter Last, Peter Mörters and Hermann Thorisson, *Unbiased shifts of Brownian motion*, Annals of Probability **42** (2014), no.2, 431–463. This starts from Brownian motion and characterizes certain shifts preserving its law; it does not by that description stationarize an arbitrary FBM+BBM. Reference and relevance checked against Pitman–Tang pp.3 and 26–27; full theorem not checked here.
- Hermann Thorisson, *Transforming random elements and shifting random fields*, Annals of Probability **24** (1996), no.4, 2057–2064. General shift-coupling lead, cited as [83] by Pitman–Tang, and used in their Theorem 5.9. No application supplying the missing invariant-law hypotheses has been proved here.
- Hermann Thorisson, *Coupling, stationarity, and regeneration*, Springer, New York, 2000. Background in source Theorem 5.1 and Pitman–Tang references; no claim that its general theorems alone answer this question.
- J. Bertoin and M. Savov, *Some applications of duality for Lévy processes in a half-line*, Bulletin of the London Mathematical Society **43** (2011), no.1, 97–110. Source's Example 2.8 cites it for a duality example, not a compatibility solution.

## Search log

'''
lines=[intro]
for i,x in enumerate(log,1):
 name=x['service'];status=x.get('status','download inspected');file=x.get('file','')
 lines.append(f"{i}. Date {x['date']}; service/query `{name}`; outcome `{status}`. Request: {x['url']} . Raw record: {file}.\n")
lines.append('''
## Search results and limitations by service

- arXiv exact phrase "forward Brownian motion" returned the source and an unrelated Brownian-web paper. HTTP and HTTPS requests had the same two entries. Author query Burdzy AND Scheutzow returned only the source. The query for decomposable AND Brownian returned 30 heterogeneous items (reflecting Brownian motion, stochastic finance, stretched Brownian motion, loop soups, etc.); titles and abstracts were inspected and none addressed the exact compatibility questions. The backward-Brownian phrase returned one unrelated SPDE/derivative-pricing paper. The forward-Brownian/stationary-or-coupling query returned no entries. Search limits and full queries are retained above.
- Crossref title search identified the correct source DOI. The compatibility query returned forward/backward stochastic differential equation papers (including G-Brownian motion), rather than this path-decomposition model. The direct DOI response confirmed authors, volume, pages and online date, and counted one reference to the source; Crossref is not used here as a comprehensive reverse-citation index.
- Semantic Scholar citation endpoint returned Pitman–Tang only. Its PDF was read for its actual theorem and discussion of the source; this is the most relevant subsequent item found.
- GitHub exact phrase query returned zero repositories. Brownian decomposable returned eleven finance/simulation repositories, all unrelated on title and description. No repository result was treated as a proved mathematical solution.
- OpenAlex source/title/compatibility/citation attempts all failed with HTTP 429. The first direct DOI guess (10.1214/13-EJP3343) was an unverified locator and is NOT the source DOI; it failed and was superseded by the Crossref-confirmed DOI. The attempted `references.doi` citation filter is not a validated OpenAlex filter; it also failed before any response data. Consequently no source OpenAlex work ID could be resolved and no valid ID-based citing-works enumeration was possible. The DOI/source-identifier searches are logged as failed attempts, not successful coverage.

## Read-only earlier work and brain checks

Before mathematics, read-only math_recall queries: "Burdzy Scheutzow forward Brownian decomposable backward"; later "Thorisson shift coupling stationary regeneration Brownian". Brain recall queries: "forward Brownian motion mistakes" and "Compatibility forward backward Brownian decompositions". Recall hints identify the earlier common-splice obstruction and a candidate solution to the different Problem 7.5; none is accepted as a verdict on 7.1–7.3.

Intake `problems.jsonl`, `attempts.jsonl`, and `sources.jsonl` were searched for P0030 in the probability_1000_intake_* directories. Campaign records were searched in codex_pool_2026_10_10. The origin/master file probability_campaigns/codex_pool_2026-10-10/team_O/w332/reports/P0030_attempt.md was read with git show. Auditor w346's rows 12–13 correct the older phrase "finite Brownian bridge" to "finite Brownian-motion segment" and retain the future-selection mean obstruction. No repository working tree, ledger, brain, or store was intentionally modified.
''')
pathlib.Path('LITERATURE.md').write_text('\n'.join(lines),encoding='utf8')
print('wrote LITERATURE.md;',len(log),'network requests logged')

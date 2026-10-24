from pathlib import Path
import json,urllib.parse
p=Path('LITERATURE.md'); t=p.read_text(encoding='utf-8-sig')
t+='''
## Search ledger (all executed 2026-10-12)

'''
for a in json.loads(Path('search_log.json').read_text(encoding='utf8')):
 q=urllib.parse.parse_qs(urllib.parse.urlparse(a['url']).query)
 query=a.get('query',q)
 t+=f"- {a['service']}: `{a['url']}`. Query: `{json.dumps(query,ensure_ascii=False)}`. Result: {a.get('status',a.get('error'))}.\n"
t+='''
The HTTP arXiv API endpoint redirected to HTTPS and timed out. The HTTPS broad search and a narrower retry also timed out. Successful direct arXiv PDF downloads supplemented these failed API searches; the API failures are not negative search results. Semantic Scholar returned HTTP 429 for the source-citation query and broad search. OpenAlex retrieved 52 works citing the published source and zero citing its separately indexed arXiv record. All 52 titles/metadata were screened; no title or metadata identified an exact solving theorem. These were not all read in full. Crossref's first broad ancestor query was noisy, so a title-focused Brownian-net search was added. GitHub returned two unrelated mobile geometric network repositories (jalt-online/brownian-networks; jalt-research/brownian-networks-2).

## Relevant papers and checked scope

1. E. Schertzer, R. Sun, J. M. Swart, The Brownian Web, the Brownian Net, and their Universality (source above). Checked equation (8.3) and Conjecture 8.3 on p.72; Proposition 2.7 (coalescing point-set density), Corollary 2.8, Theorem 2.11 (web special points), Theorem 3.2 (left/right marginals), Theorem 3.9 (wedge characterization), Proposition 3.14 (containment), Proposition 3.18 (deterministic-time density), Remark 3.21 (exceptional random times), Theorem 3.24 (net special points), Proposition 4.7 (relevant separation points), and Proposition 4.9 (finite graph). The relevant-separation theorem concerns dual time reversal, not reversal of the incoming forward paths in the PMRCA definition. It is a lead, not a solution of the conjecture.
2. E. Schertzer, R. Sun, J. M. Swart, Special points of the Brownian net, Electronic Journal of Probability 14 (2009), Paper 30, 805–864. DOI 10.1214/EJP.v14-641; arXiv:0806.2326. Downloaded special_points.pdf. Theorem 1.12 (structure of special points), printed PDF p.13, extends incoming/outgoing equivalence to full net paths. Conjecture 1.13 (three-connected points), printed PDF p.15, is a related unproved local-finiteness assertion. Our conditional three-arm reduction is in ATTEMPT.md Section 5; it is not a solution in print.
3. R. Sun, J. M. Swart, The Brownian net, Annals of Probability 36 (2008), 1153–1208. DOI 10.1214/07-AOP357. Results used through their statements in the checked survey; the original PDF was not fetched in this attempt.
4. R. Kou, Special times for the point set process of the Brownian Net, arXiv:2512.10761v1 (11 December 2025). Downloaded special_times.pdf. Theorem 1, PDF p.2: the set of times at which Xi_t has cluster points has Hausdorff dimension 1/2 almost surely. This concerns time slices rather than first meetings. It does not settle Conjecture 8.3 and does not justify local finiteness at a random first-contact time. Title/abstract/main theorem and text searches checked.
5. R. Sun, J. M. Swart, J. Yu, Universality of the Brownian net, arXiv:2401.09370v2 (15 September 2026). Downloaded universality.pdf. The main result concerns scaling limits of weakly branching/coalescing random walks with crossing paths and finite (3+epsilon)-moment increments. Title/abstract and full-text searches for ancestors, PMRCA, meeting points and conjecture references did not identify an exact theorem about M. Related scaling-limit work, not a printed solution.
6. E. Schertzer, R. Sun, J. M. Swart, Stochastic flows in the Brownian web and net, Memoirs of the AMS 227 (2014), no.1065; DOI 10.1090/S0065-9266-2013-00687-9. Proposition 6.5 is the origin of the finite graph result cited in survey Proposition 4.9. Consulted via the survey; not fetched in full.

The metadata references for all OpenAlex citation candidates are saved in citation_candidates.md. No source inspected states and proves the exact F0036 question. Literature status is “no exact solution identified in this bounded search”; no assertion of certified current openness is made.

## Earlier local research consulted read-only

- Intake ledger probability_1000_intake_F_20260908, F0036-A001: an explicitly unverified inward-extremal identification. Only the earliest-time inequality follows from containment.
- `git show origin/master:prob1000_lean_20260908/ultracode_20260909/F0036/memo.md` in ~/math-open-problems: a 2026-09-09 partial memo, not an accepted proof. Its claim that same-source witnesses contribute exactly one point also does not follow merely from a lower bound on first meeting time; we do not use it. Its recursive “equivalence” after random meeting times has not been proved and is not accepted here.
- The same repository's bruteforce_check.py was read as a method hint. We wrote an independent script in this folder with its own initial-time treatment and fresh exact checks.
- A filtered `git ls-tree` search for F0036 / Brownian-net / PMRCA paths identified the above files. A first unfiltered listing was unnecessarily large; no working-tree changes were made.
- During the attempt, a second math-store query, “Schertzer Sun Swart Brownian net three connected points”, was issued; any returned cards remain hints requiring source checks.
'''
p.write_text(t,encoding='utf8')
d=json.loads(Path('citing_published.response').read_text(encoding='utf8'))
lines=['# OpenAlex citation candidates screened — 2026-10-12','', 'Metadata screen only unless LITERATURE.md explicitly records a full-text check.','']
for a in d['results']:
 authors=', '.join(x['author']['display_name'] for x in a.get('authorships',[]))
 lines.append(f"- {authors}. {a.get('title')}. {a.get('publication_year')}. DOI: {a.get('doi')}. OpenAlex: {a['id']}.")
Path('citation_candidates.md').write_text('\n'.join(lines)+'\n',encoding='utf8')

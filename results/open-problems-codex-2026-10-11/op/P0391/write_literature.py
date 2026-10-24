import pathlib,json,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parent
lines=['# Literature and provenance — P0391, 11 October 2026','',
'## Status of the literature check','',
'No inspected paper states and proves the full arbitrary-gamma, finite-second-service-moment, empty-start diffusion theorem. This is NOT a certificate of current openness: OpenAlex returned HTTP 429 on all requests, so its citation graph could not be inspected. No SOLVED_IN_LITERATURE verdict is warranted.','',
'## Exact primary reference','',
'Bert Zwart (2022), “Conjectures on symmetric queues in heavy traffic,” Queueing Systems 100(3–4), 369–371. DOI 10.1007/s11134-022-09746-x. arXiv:2202.02366v1, posted 4 February 2022; manuscript dated 8 February 2022. Downloaded PDF and extracted text are source_pdf.pdf and source.txt. Problem 1 is on PDF p. 2, with hypotheses beginning on p. 1.','',
'The source defines gamma(n,i) as both the service share at position i and the probability of insertion at i into a queue of new size n. Gamma is fixed, nonnegative, and sums to one. Poisson arrival rates vary; the service law is fixed, has mean m>0 and finite second moment. The parameter r(1-rho_r) tends to a real constant, not necessarily positive. The formal problem sentence does not specify initial state; PDF p. 2 explicitly limits the universal fixed-time marginal identity to Q_r(0)=0. The attempt follows the user’s empty-start caveat.','',
'## Searches actually run','']
for file in ['search_log.json','followup_log.json','last_sources_log.json']:
 if (root/file).exists():
  for item in json.loads((root/file).read_text(encoding='utf-8')):
   lines+=['- Date '+item['date']+'; service '+item['service']+'; exact request: `'+item['query']+'`; result: '+item['result']+'.']
lines+=['',
'The first arXiv phrase search returned two records: the source and Guillemin–Simonian (2013), “Stationary analysis of the Shortest Queue First service policy: the asymmetric case,” arXiv:1305.3496, a different two-queue model. GitHub returned total_count=0 for the quoted phrase. Crossref returned the source DOI and otherwise mostly unrelated heavy-traffic papers. The OpenAlex DOI-resolution requests failed before a canonical work ID could be obtained; the attempted DOI-based citing filter also returned 429. Therefore the requested OpenAlex works-citing search remains unavailable, rather than being represented as an empty citation set.','',
'The successful Semantic Scholar citation endpoint for the source DOI returned two records: the stable-local-time paper and the proportional-fairness paper below. Their metadata years are 2021 and 2014 respectively, although later publication metadata exist. The retrieved arXiv versions and publication metadata are kept distinct.','',
'## Relevant references and leads','',
'1. Brian Fralix and Bert Zwart (2011), “Time-dependent properties of symmetric queues,” Queueing Systems 67(1), 33–45, DOI 10.1007/s11134-010-9202-1. Crossref has online date 24 November 2010. Source reference [2] and PDF p. 2 explicitly credit the empty-start fixed-time queue-length identity to this paper. It is a marginal-law input, not the requested process theorem. The publisher landing-page fetch was attempted separately.','',
'2. Frank P. Kelly (1979), Reversibility and stochastic networks, Wiley, Chichester. Source reference [4]. Used for the standard full stationary residual-service product form; ATTEMPT.md gives its balance calculation. This is not a diffusion-limit theorem.','',
'3. H. C. Gromoll (2004), “Diffusion approximation for a processor sharing queue in heavy traffic,” Annals of Applied Probability 14(2), 555–611, arXiv:math/0405298. Source [3]. PS special case with stronger service moments; not universal gamma.','',
'4. A. L. Puha and R. J. Williams (2004), “Invariant states and rates of convergence for a critical fluid model of a processor sharing queue,” Annals of Applied Probability 14(2), 517–554. Source [10]. PS fluid model, not arbitrary gamma.','',
'5. A. Lambert, F. Simatos, and B. Zwart (2013), “Scaling limits via excursion theory: interplay between Crump-Mode-Jagers branching processes and processor-sharing queues,” Annals of Applied Probability 23(6), 2357–2381. Source [7]. The source explicitly credits this paper with removing the fourth-moment assumption for PS with Poisson arrivals. Used only as the known PS finite-second-moment input.','',
'6. V. Limic (2000), “On the behavior of LIFO preemptive resume queues in heavy traffic,” Electronic Communications in Probability 5, 13–27, DOI 10.1214/ecp.v5-1014; V. Limic (2001), “A LIFO queue in heavy traffic,” Annals of Applied Probability 11(2), 301–331. Source [8], [9]. LCFS special cases, not universal gamma.','',
'7. W. Whitt (2002), Stochastic-process limits, Springer, New York. Source [12]. Standard workload FCLT and reflection-map input, not the conjectured queue-length theorem.','',
'8. A. Lambert and F. Simatos (2014), “The weak convergence of regenerative processes using some excursion path decompositions,” Annales de l’Institut Henri Poincare, Probabilites et Statistiques 50(2), 492–511. Source [5]. A possible general framework, but excursion convergence hypotheses must still be established for arbitrary gamma.','',
'9. Maria Vlasiou, Jiheng Zhang, and Bert Zwart, “Insensitivity of proportional fairness in critically loaded bandwidth sharing networks,” arXiv:1411.4841; retrieved manuscript dated 2 June 2021; later DOI 10.1007/s11134-026-09978-1 appears in Semantic Scholar. Retrieved PDF abstract concerns proportional fairness and a dense class of service laws in bandwidth-sharing networks. The allocation model and quantifier are not arbitrary rank-based symmetric gamma. A related lead, not an exact solution.','',
'10. “Stochastic Volterra equations for the local times of spectrally positive stable processes,” arXiv:2105.02349, DOI 10.1214/23-AAP2017 (Semantic Scholar citation record). Local times of stable processes concern a different limit regime, not the universal finite-variance symmetric queue theorem. Author and publication details are recorded from the fetched PDF below if available.','',
'## Broader arXiv query results','']
file=root/'arxiv_broad.txt'
if file.exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.parse(file).getroot().findall('a:entry',ns):
  authors=', '.join(x.find('a:name',ns).text for x in e.findall('a:author',ns))
  lines+=['- '+authors+'; '+e.find('a:title',ns).text.replace('\n',' ')+'; '+e.find('a:id',ns).text+'; posted '+e.find('a:published',ns).text+'.']
lines+=['',
'## Brain and earlier-attempt provenance','',
'Read-only math recall: “symmetric queues Zwart heavy traffic”; walked claim_62a81d9a9cbfc54c216f7baa59f5a4c1f0ef1c5d4f6c3f2a818f1942f1f67925. The earlier card establishes the constants and flags uniform state-space collapse as the gap; no complete theorem was claimed.','',
'Read-only memory recalls: “symmetric queue heavy traffic” and “symmetric queue heavy traffic mistakes.” Returned mostly unrelated records; none was used as mathematical evidence. The recall utility reported an internal failed detached-index refresh; this task issued only the specifically requested recall commands and no brain-write command.','',
'Initial rg lookup of a literal wildcard directory failed on Windows. A subsequent Python glob/rglob search over the requested intake and codex-pool locations saved prior_records.txt (no P0391 matches at those paths). The read-only origin/master git tree was searched, with relevant paths saved in prior_git_paths.txt; git grep results are saved in prior_git_hits.txt. No repository working tree was changed.','']
(root/'LITERATURE.md').write_text('\n'.join(lines),encoding='utf-8')
print('Wrote LITERATURE.md,',len(lines),'lines')
